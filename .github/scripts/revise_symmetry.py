from pathlib import Path
import re
symmetry_path=Path('Emergent_Mathematics_Symmetry.tex')
counting_path=Path('Emergent_Mathematics_Counting.tex')
agents_path=Path('AGENTS.md')
symmetry=symmetry_path.read_text()
counting=counting_path.read_text()
def env_pattern(env,title):
    return re.compile(rf'\n*\\begin\{{{env}\}}\[{re.escape(title)}\].*?\\end\{{{env}\}}\n*',re.S)
def pop_env(text,env,title):
    pattern=env_pattern(env,title)
    match=pattern.search(text)
    if not match:
        raise RuntimeError(f'missing {env} block: {title}')
    block=match.group(0).strip()+'\n\n'
    return text[:match.start()]+'\n\n'+text[match.end():],block
def replace_env(text,env,title,replacement):
    pattern=env_pattern(env,title)
    text2,count=pattern.subn(lambda _: '\n\n'+replacement.strip()+'\n\n',text,count=1)
    if count!=1:
        raise RuntimeError(f'expected one {env} block: {title}; found {count}')
    return text2
moved=[]
for env,title in [('definition','Symmetric powers'),('exercise','Symmetric-power trace identity'),('definition','Fredholm determinant'),('exercise','Fredholm determinant and trace identity')]:
    symmetry,block=pop_env(symmetry,env,title)
    moved.append(block)
symmetry,probability_block=pop_env(symmetry,'definition','Probability spaces and convergence')
symmetry,eisenstein_block=pop_env(symmetry,'definition','Eisenstein series and the discriminant')
symmetry,e8_block=pop_env(symmetry,'exercise','Eisenstein series and the $E_8$ shell')
marker='\\section{Exact State Counting}\n'
if marker not in counting:
    raise RuntimeError('Exact State Counting section not found')
counting=counting.replace(marker,marker+'\n'+''.join(moved),1)
partition_marker='\\begin{exercise}[Partition asymptotics]'
if partition_marker not in counting:
    raise RuntimeError('Partition asymptotics exercise not found')
counting=counting.replace(partition_marker,eisenstein_block+e8_block+partition_marker,1)
random_marker='\\section{Random Matrices}\n'
if random_marker not in counting:
    raise RuntimeError('Random Matrices section not found')
counting=counting.replace(random_marker,random_marker+'\n'+probability_block,1)
symmetry,trace_definition=pop_env(symmetry,'definition','Trace and Hilbert--Schmidt classes')
symmetry,trace_exercise=pop_env(symmetry,'exercise','Trace ideals')
compact_spectral=r'''
\begin{exercise}[Compact spectral theorem]
For a compact normal operator $K$, prove that every nonzero spectral value is
an eigenvalue of finite multiplicity, that the nonzero eigenvalues can
accumulate only at zero, and that
\[
K=\sum_{\lambda\in\spec(K)\setminus\{0\}}
\lambda E_K(\{\lambda\})
\]
in operator norm.
\end{exercise}
'''
symmetry=replace_env(symmetry,'exercise','Compact spectral theorem',compact_spectral)
trace_spectral=r'''
\begin{exercise}[Trace-class spectral formula]
Prove that every trace-class operator is compact.  For $K\geq0$ in
$S_1(H)$, prove
\[
\Tr K
=\sum_{\lambda\in\spec(K)\setminus\{0\}}
\lambda\dim E_K(\{\lambda\})H<\infty.
\]
\end{exercise}
'''
coefficient_marker='\\begin{definition}[Coefficient transforms]'
if coefficient_marker not in symmetry:
    raise RuntimeError('Coefficient transforms insertion point not found')
symmetry=symmetry.replace(coefficient_marker,trace_definition+trace_exercise+trace_spectral+'\n'+coefficient_marker,1)
symmetry,haar_block=pop_env(symmetry,'definition','Locally compact groups and Haar measure')
topology_pattern=re.compile(r'(\\begin\{definition\}\[Topological spaces\].*?\\end\{definition\})',re.S)
symmetry,count=topology_pattern.subn(lambda m:m.group(1)+'\n\n'+haar_block.strip(),symmetry,count=1)
if count!=1:
    raise RuntimeError('Topological spaces insertion point not found')
symmetry=symmetry.replace('With normalized Haar measure on $\\T=\\R/2\\pi\\Z$, define\n\\[\n\\widehat f(k)=\\int_\\T f(x)e^{-ikx}\\,dx,\\qquad k\\in\\Z.\n','Equip $\\T=\\R/2\\pi\\Z$ with normalized Haar measure\n$dm_{\\T}(x)=dx/(2\\pi)$.  Define\n\\[\n\\widehat f(k)=\\int_\\T f(x)e^{-ikx}\\,dm_{\\T}(x),\\qquad k\\in\\Z.\n',1)
old_lattice='''Its \\emph{reciprocal lattice} is the annihilator
\\[
\\Gamma^*=\\{\\xi\\in\\R^n:\\xi\\cdot\\gamma\\in2\\pi\\mathbb Z
\\text{ for every }\\gamma\\in\\Gamma\\}.
\\]
\\end{definition}'''
new_lattice='''Its \\emph{reciprocal lattice} is the annihilator
\\[
\\Gamma^*=\\{\\xi\\in\\R^n:\\xi\\cdot\\gamma\\in2\\pi\\mathbb Z
\\text{ for every }\\gamma\\in\\Gamma\\}.
\\]
For the arithmetic dual
$L^*=\\{y:\\langle x,y\\rangle\\in\\Z\\text{ for every }x\\in L\\}$
used below, the corresponding physical reciprocal lattice is $2\\pi L^*$.
\\end{definition}'''
if old_lattice not in symmetry:
    raise RuntimeError('reciprocal-lattice block not found')
symmetry=symmetry.replace(old_lattice,new_lattice,1)
tangent_minimal=r'''
\begin{definition}[Tangent spaces]
For a smooth manifold $M$, the tangent space $T_pM$ is the linear space of
derivations $v:C^\infty(M)\to\R$ at $p$, satisfying
\[
v(fg)=f(p)v(g)+g(p)v(f).
\]
For a smooth map $F:M\to N$, define
$dF_p(v)(f)=v(f\circ F)$.
\end{definition}
'''
symmetry=replace_env(symmetry,'definition','Tangent and cotangent spaces',tangent_minimal)
symmetry,_=pop_env(symmetry,'definition','Ordinary hypergeometric series')
symmetry,_=pop_env(symmetry,'exercise','Gauss hypergeometric theorem')
jacobi_marker='\\begin{definition}[Jacobi polynomials]'
compact_gauss=r'''
\begin{definition}[Pochhammer symbols and the Gauss series]
For $n\geq0$, define
\[
(a)_0=1,\qquad (a)_n=a(a+1)\cdots(a+n-1).
\]
If $c\notin\{0,-1,-2,\ldots\}$, define
\[
{}_2F_1\!\left(\begin{matrix}a,b\\c\end{matrix};z\right)
=\sum_{n=0}^{\infty}\frac{(a)_n(b)_n}{(c)_n}\frac{z^n}{n!}
\]
for $|z|<1$, with termination when $a$ or $b$ is a nonpositive integer.
\end{definition}
'''
if jacobi_marker not in symmetry:
    raise RuntimeError('Jacobi definition not found')
symmetry=symmetry.replace(jacobi_marker,compact_gauss+'\n'+jacobi_marker,1)
jacobi_exercise=r'''
\begin{exercise}[Jacobi spectral equation]
Substitute the terminating Gauss series in the hypergeometric differential
equation and prove
\[
\left((1-x^2)\frac{d^2}{dx^2}
+\bigl(\beta-\alpha-(\alpha+\beta+2)x\bigr)\frac{d}{dx}\right)
P_n^{(\alpha,\beta)}
=-n(n+\alpha+\beta+1)P_n^{(\alpha,\beta)}.
\]
Derive the Rodrigues formula, use it to prove orthogonality on $[-1,1]$
with weight $(1-x)^\alpha(1+x)^\beta$, and derive the three-term recurrence
from symmetry of multiplication by $x$.
\end{exercise}
'''
symmetry=replace_env(symmetry,'exercise','Jacobi spectral equation',jacobi_exercise)
spherical_pattern=re.compile(r'(with \$C_\{\\ell m\}\$ fixed by unit norm\.)( Separate the Coulomb Hamiltonian)',re.S)
symmetry,count=spherical_pattern.subn(lambda m:m.group(1)+'  For the rotation $R_y(\\theta)$, prove that each Wigner coefficient $d^j_{m\'m}(\\theta)=\\langle jm\',R_y(\\theta)jm\\rangle$ is a Jacobi polynomial in $\\cos\\theta$ multiplied by the endpoint powers of $\\sin(\\theta/2)$ and $\\cos(\\theta/2)$, with normalization fixed by unitarity.'+m.group(2),symmetry,count=1)
if count!=1:
    raise RuntimeError('Wigner--Jacobi insertion point not found')
peter_weyl=r'''
\begin{exercise}[Compact convolution operators]
Let $G$ be compact with normalized Haar measure.  For $f\in C(G)$, prove
that left convolution by $f$ is compact on $L^2(G)$ and commutes with the
right regular representation.  Show that its nonzero spectral subspaces are
finite-dimensional invariant subspaces.  Construct finite
matrix-coefficient approximate identities and prove density of matrix
coefficients in $C(G)$ and $L^2(G)$.
\end{exercise}

\begin{exercise}[Peter--Weyl decomposition]
Derive Schur orthogonality and prove the intrinsic Hilbert direct sum
\[
L^2(G)\cong
\mathop{\widehat{\bigoplus}}_{\pi\in\widehat G}
H_\pi\otimes H_\pi^*.
\]
Show that the left regular representation acts as
$\pi\otimes I_{H_\pi^*}$ on the $\pi$-summand and that its multiplicity is
$\dim H_\pi$.
\end{exercise}

\begin{exercise}[Compact Fourier inversion]
For $f\in L^2(G)\subseteq L^1(G)$, define
\[
\widehat f(\pi)=\int_Gf(g)\pi(g)^*\,dg.
\]
Prove
\[
f=\sum_{\pi\in\widehat G}
(\dim H_\pi)\Tr\!\bigl(\widehat f(\pi)\pi(\,\cdot\,)\bigr),
\qquad
\|f\|_2^2=\sum_{\pi\in\widehat G}
(\dim H_\pi)\|\widehat f(\pi)\|_{\rm HS}^2,
\]
with the first sum converging in $L^2(G)$.  For $f\in C(G)$, prove uniform
convergence of the corresponding summability means.
\end{exercise}
'''
symmetry=replace_env(symmetry,'exercise','Peter--Weyl theorem',peter_weyl)
spectral_lines=r'''
\begin{exercise}[Spectral lines and time evolution]
\label{ex:spectral-lines}
Let $A$ be self-adjoint, let $B\in B(H)$, and set
$B(t)=e^{itA/\hbar}Be^{-itA/\hbar}$.  For $x,y\in H$, define on measurable
rectangles
\[
\nu^B_{x,y}(S\times T)=\langle E_A(S)x,BE_A(T)y\rangle.
\]
Prove that this extends to a finite complex measure on $\R^2$ and that
\[
\langle x,B(t)y\rangle
=\int_{\R^2}e^{it(\mu-\lambda)/\hbar}
\,d\nu^B_{x,y}(\mu,\lambda).
\]
For pure-point spectrum, deduce in the weak operator topology
\[
B(t)=\sum_{\lambda,\mu}
e^{it(\mu-\lambda)/\hbar}P_\mu BP_\lambda.
\]
Prove that the line at $(\mu-\lambda)/\hbar$ is absent exactly when the
corresponding spectral block vanishes.  For an initial unit vector
$\psi\in P_\lambda H$, identify its transition strength as
$\|P_\mu B\psi\|^2$.
\end{exercise}
'''
symmetry=replace_env(symmetry,'exercise','Spectral lines and time evolution',spectral_lines)
hc_transform=r'''
\begin{exercise}[Harish-Chandra transform on $\mathbb H^2$]
For
\[
\Delta_{\mathbb H^2}=y^2(\partial_x^2+\partial_y^2),
\]
derive
\[
\Delta_{\rm rad}=\frac{d^2}{dr^2}+\coth r\frac d{dr}
\]
and prove that the normalized radial solution of
\[
\Delta\varphi_\lambda=-(\lambda^2+\tfrac14)\varphi_\lambda,
\qquad \varphi_\lambda(0)=1,
\]
is
\[
\varphi_\lambda(r)=P_{-1/2+i\lambda}(\cosh r).
\]
Derive the Lagrange--Wronskian identity for $\varphi_\lambda$ and
$\varphi_\mu$ on $[0,R]$.  After fixing one self-adjoint boundary condition
at $R$, prove orthogonality only for the discrete parameters satisfying
that boundary condition.  Let $R\to\infty$ and derive distributional
orthogonality with density proportional to $|c(\lambda)|^{-2}$.
\end{exercise}
'''
symmetry=replace_env(symmetry,'exercise','Harish-Chandra transform on $\\mathbb H^2$',hc_transform)
symmetry,_=pop_env(symmetry,'definition','Discrete-series characters')
rank_one=r'''
\begin{exercise}[Rank-one Plancherel and wave propagation]
For a smooth compactly supported radial function on $\mathbb H^2$, define
\[
\widetilde f(\lambda)=2\pi\int_0^\infty
f(r)P_{-1/2+i\lambda}(\cosh r)\sinh r\,dr.
\]
Use the spectral theorem for the radial Sturm--Liouville operator to prove
inversion and Plancherel with
\[
c(\lambda)=C\frac{\Gamma(i\lambda)}
{\Gamma(\tfrac12+i\lambda)},
\qquad
|c(\lambda)|^{-2}=C'\lambda\tanh(\pi\lambda),
\]
where the constants are fixed by the Haar and Euclidean Fourier
normalizations.  Derive
\[
p_t(r)=C_G\int_0^\infty
e^{-t(\lambda^2+1/4)}P_{-1/2+i\lambda}(\cosh r)
|c(\lambda)|^{-2}\,d\lambda,
\]
\[
G_\zeta(r)=C_G\int_0^\infty
\frac{P_{-1/2+i\lambda}(\cosh r)}
{\lambda^2+1/4-\zeta}|c(\lambda)|^{-2}\,d\lambda.
\]
For $u_{tt}=\Delta_{\mathbb H^2}u$ with radial initial displacement $f$
and zero initial velocity, prove
\[
u(t,r)=C_G\int_0^\infty
\cos\!\left(t\sqrt{\lambda^2+\tfrac14}\right)
\widetilde f(\lambda)P_{-1/2+i\lambda}(\cosh r)
|c(\lambda)|^{-2}\,d\lambda.
\]
Deduce the predicted radial waveform, attenuation, and arrival profile for
a finite hyperbolic network before boundary reflections return to the
observation region, and separate finite-boundary, loss, and discretization
effects from the infinite-space prediction.
\end{exercise}
'''
symmetry=replace_env(symmetry,'exercise','Spherical Plancherel formula',rank_one)
for env,title in [('definition','Orbital representations'),('exercise','Kirillov correspondence'),('exercise','Kirillov character formula')]:
    symmetry,_=pop_env(symmetry,env,title)
canonical_weyl=r'''
\begin{exercise}[Canonical commutation and Weyl relations]
Prove
\[
[Q_\ell,P_v]=i\hbar\ell(v)I.
\]
For physical momentum $p\in V^*$, define
\[
(T_q\psi)(x)=\psi(x-q),
\qquad
(M_p^\hbar\psi)(x)=e^{ip(x)/\hbar}\psi(x).
\]
Prove
\[
M_p^\hbar T_q=e^{ip(q)/\hbar}T_qM_p^\hbar.
\]
For
\[
W_\hbar(q,p)=e^{-ip(q)/(2\hbar)}M_p^\hbar T_q,
\]
prove
\[
W_\hbar(z)W_\hbar(z')
=e^{i\omega(z,z')/(2\hbar)}W_\hbar(z+z').
\]
Show that $W_\hbar(z)=\pi_{1/\hbar}(z,0)$ is obtained by composing the
Schr\"odinger representation with the canonical section $z\mapsto(z,0)$.
The section is not a group homomorphism, and its failure is exactly the
displayed multiplier.
\end{exercise}
'''
symmetry=replace_env(symmetry,'exercise','Canonical commutation and Weyl relations',canonical_weyl)
stone=r'''
\begin{exercise}[Stone--von Neumann theorem]
Prove directly that $\pi_\lambda$ is irreducible for $\lambda\ne0$.  Let
$U$ be a strongly continuous irreducible representation of
$\mathbb H(V\oplus V^*,\omega)$ with central character $e^{i\lambda s}$.
Use the commuting translation subgroup, the spectral theorem, and the Weyl
relations to construct a unitary intertwiner from $U$ to $\pi_\lambda$.
Deduce uniqueness up to unitary equivalence.
\end{exercise}
'''
symmetry=replace_env(symmetry,'exercise','Stone--von Neumann theorem',stone)
fourier_wigner_definition=r'''
\begin{definition}[Fourier--Wigner transform]
Let $V$ be an $n$-dimensional real linear space with Lebesgue measure $dq$,
and equip $V^*$ with the dual measure $dp$ for which $\mathcal F_\hbar$ is
unitary.  With $W_\hbar$ defined above, set
\[
\mathcal W_\hbar(A)(z)
=(2\pi\hbar)^{-n/2}\Tr(AW_\hbar(z)),
\qquad A\in S_1(L^2(V)).
\]
\end{definition}
'''
symmetry=replace_env(symmetry,'definition','Fourier--Wigner transform',fourier_wigner_definition)
fourier_wigner_exercise=r'''
\begin{exercise}[Fourier--Wigner Plancherel]
Prove $W_\hbar(z)^*=W_\hbar(-z)$.  For
$A,B\in S_1(L^2(V))\cap S_2(L^2(V))$, prove
\[
\int_{V\oplus V^*}
\overline{\mathcal W_\hbar(A)(z)}\mathcal W_\hbar(B)(z)\,dz
=\Tr(A^*B).
\]
Deduce that $\mathcal W_\hbar$ extends uniquely to a unitary map
\[
S_2(L^2(V))\longrightarrow L^2(V\oplus V^*)
\]
and, whenever $\mathcal W_\hbar(A)$ is integrable, prove
\[
A=(2\pi\hbar)^{-n/2}\int_{V\oplus V^*}
\mathcal W_\hbar(A)(z)W_\hbar(z)^*\,dz
\]
in the weak operator topology.
\end{exercise}
'''
symmetry=replace_env(symmetry,'exercise','Fourier--Wigner Plancherel',fourier_wigner_exercise)
old_sentence='Derive this identity both from the Schr\\\"odinger kernel and from the\nKirillov character formula on $\\mathcal O_\\lambda$.'
new_sentence='Derive this identity from the Schr\\\"odinger kernel and verify it by integrating the ordinary Fourier transform over the explicitly computed coadjoint orbit $\\mathcal O_\\lambda$.'
if old_sentence not in symmetry:
    raise RuntimeError('Heisenberg Plancherel derivation sentence not found')
symmetry=symmetry.replace(old_sentence,new_sentence,1)
synthesis=r'''
\begin{exercise}[Symmetry transforms]
Compare the four decompositions developed in this part: characters of
locally compact abelian groups, matrix coefficients of compact groups,
zonal spherical functions on $\mathbb H^2$, and the Schr\"odinger
representations of the Heisenberg group.  In each case identify the
transform kernel, spectral parameter space, Plancherel measure, inversion
formula, and the special functions that encode a measurable frequency,
transition amplitude, or propagation profile.
\end{exercise}
'''
symmetry=symmetry.rstrip()+'\n\n'+synthesis.strip()+'\n'
symmetry=re.sub(r'\n{4,}','\n\n\n',symmetry)
counting=re.sub(r'\n{4,}','\n\n\n',counting)
section_titles=re.findall(r'\\section\{([^}]*)\}',symmetry)
expected=['Spectral Theory','Fourier Analysis','Peter--Weyl Theory','Harish--Chandra Theory','Kirillov Orbit Method']
if section_titles!=expected:
    raise RuntimeError(f'section titles changed: {section_titles}')
for token in ['\\emph{Question.}','Discrete-series characters','Kirillov correspondence','Eisenstein series and the $E_8$ shell','restriction of $\\pi_1$']:
    if token in symmetry:
        raise RuntimeError(f'forbidden token remains: {token}')
if symmetry.index('Locally compact groups and Haar measure')>symmetry.index('Regular representation'):
    raise RuntimeError('Haar measure still introduced after use')
for required in ['W_\\hbar','Rank-one Plancherel and wave propagation','transition strength','Trace-class spectral formula']:
    if required not in symmetry:
        raise RuntimeError(f'required revision missing: {required}')
for required in ['Symmetric-power trace identity','Fredholm determinant and trace identity','Eisenstein series and the $E_8$ shell','Probability spaces and convergence']:
    if required not in counting:
        raise RuntimeError(f'moved counting block missing: {required}')
symmetry_path.write_text(symmetry)
counting_path.write_text(counting)
agents=agents_path.read_text()
agents=agents.replace('- Except for the required opening physical question in each section, the body\n  should consist of definitions and exercises stating major results.\n','- Each section body should consist of definitions and exercises stating major results.\n')
agents=re.sub(r'\n### Opening physical questions\n.*?(?=\n- After changing the TeX source)','\n### Section openings\n\n- Place definitions or exercises directly after each `\\section` heading; do not add a free-standing opening question or introductory paragraph.\n',agents,flags=re.S)
if 'Opening physical questions' in agents or 'required opening physical question' in agents:
    raise RuntimeError('opening-question rules remain in AGENTS.md')
agents_path.write_text(agents)
