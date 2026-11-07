# Error report

Definitive mathematical errors found in `blueprint/triangles_in_the_plane_blueprint.tex`, discrepancies
between displayed constants and the proved Lean bounds, and other substantial deviations of the
formalization from the blueprint. Each entry records the date/time and the blueprint source line.

## Deviations

- (2026-11-06T12:53-08:00, recording time) Scope: the formalization targets Theorems A (`intro:density`) and B
  (`intro:smoothing`) and their prerequisites. Section `sec:inverse` (tex lines 4084–4179) is not
  used by either theorem and is out of scope.
- (2026-11-06T12:53-08:00, recording time) `def:form` (tex line 1917): a finite complex Borel measure is represented by a
  presentation `ν = φ_*(w·m)` (`Auto.FCMeasure`); its total variation is that of the presentation,
  `∫|w| dm`, which equals `‖ν‖_TV` for the polar presentation and dominates it otherwise. Statements
  quantify over all presentations, so no strength is lost.
- (2026-11-06T12:53-08:00, recording time) `rig:degree-integration` (tex ~2243): the null-set assertion is stated as
  `μ(E ∩ π_j⁻¹N) = 0` for planar null `N` (what the proof gives; holds globally as well).
- (2026-11-06T12:53-08:00, recording time) `rig:kernel-stability` (tex ~2382): formalized in uniform form — for given
  `c, t` and distance constant `C`, one threshold `η₀` works for every core of degree `c` satisfying the
  distance estimate of `rig:kernel-gap` with constant `C` (this encodes "the threshold may be chosen using
  only `c, t, C_E` and the modulus", including base translates).
- (2026-11-06T12:53-08:00, recording time) `rig:pieces` (tex ~2546): stated for a given orthonormal basis; "agrees on `E'`"
  is taken almost everywhere on `E'`.
- (2026-11-06T12:53-08:00, recording time) `rig:kernel-ui` (tex ~2351): the constant `C_M` is existential (the proof gives √2).
- (2026-11-06T12:53-08:00, recording time) `cj:bookkeeping` (tex ~1063): subspace counts are for Mathlib's
  `Combinatorics.Subspace` structures (labelled variable sets), the count the proof uses; composition and
  concatenation are stated as equalities of coordinate maps (stronger).
- (2026-11-06T12:53-08:00, recording time) `cj:insensitive-facts`: "fixing any collection of coordinates" is formalized via a
  split `Fin r ⊕ Fin s ≃ Fin n` into free and fixed coordinates.
- (2026-11-06T12:53-08:00, recording time) `cj:equal-slices` (tex ~1408): ν is defined on words over any finite coordinate set
  (needed for the background word in `cj:transfer-equal`); `ν_{k,n}` is the case `Fin n`.
- (2026-11-06T12:53-08:00, recording time) `cj:tile-one`, `cj:tile-two`: the finite tiling family is a `Finset` of subspaces with
  pairwise disjoint point sets.
- (2026-11-06T12:53-08:00, recording time) `cj:density-increment` (tex ~1654): the threshold `N(d,δ)` is existential, since it
  depends on the existential threshold of `cj:transfer-uniform`.
- (2026-11-06T12:53-08:00, recording time) Section `ext:section`, lines ~207, ~570: `[0,2π)` with `dθ/(2π)` is modelled as
  `AddCircle (2π)` with its Haar probability measure, matching Section 4.
- (2026-11-06T12:53-08:00, recording time) `ext:bounded-support` (tex ~363): "supp φ" is read as the closed support `tsupport φ`.
- (2026-11-06T12:53-08:00, recording time) `ext:kernel-definition` (tex ~871): measurable kernels are allowed with any measurable
  target space (not only `ℝ^q`), so that product kernels in `ext:kernel-integration` fit.
- (2026-11-06T12:53-08:00, recording time) `ann:sequence`, `ann:local` (tex ~2784, ~3250): the box `Q` is allowed to be any bounded set
  (harmless generalisation).
- (2026-11-06T12:53-08:00, recording time) `ann:fibers` (consequence, tex ~3070) and `ann:atomic-rigidity` (tex ~3162) are stated for
  arbitrary measurable sub-probability kernels (stronger; the proofs use only these properties).
- (2026-11-06T12:53-08:00, recording time) `ann:localize` (tex ~3290): `|μ_n|({|u|>U})` and the unit-ball support of `P_n` are expressed via
  the presentation variation `varOn`, an upper bound for the true variation (slightly stronger hypothesis, which is what
  the applications establish); cutoffs `χ_j` are real-valued.
- (2026-11-06T12:53-08:00, recording time) `tail:telescoping` (tex ~3718): `H` is `ℝ≥0∞`-valued and monotone on `(0,∞)`; boundedness is
  then automatic in the statement.
- (2026-11-06T12:53-08:00, recording time) `tail:separation` (tex ~3520): "translates the z-frequency supports by −w" is formalized as
  `T_j v_j = w`.
- (2026-11-06T12:53-08:00, recording time) `ann:form` (tex ~2957): finite tensor sums are represented by coefficients on `e_s ⊗ e_t`; `ℓ_p`
  is a raw bilinear map with the bound (ann:cs).
- (2026-11-06T12:53-08:00, recording time) `tail:bound`, `tail:convolved-tail`: the frequency-ball constant of `ann:global` is "sufficiently
  large" in the form `∃ C₀₀, ∀ C₀ ≥ C₀₀`; dyadic `R ≥ 1` is `2^K`.
- (2026-11-06T13:21:42-08:00) `ext:ttstar` (tex ~499–520): proof route changed (no error). Instead of the projection argument, Lean proves
  "A*A compact ⇒ A compact" (ε-net and ‖A(x−x')‖² = Re⟨A*A(x−x'),x−x'⟩) and applies it to T* and then T.
- (2026-11-06T13:21:42-08:00) `ext:weakstar` (tex ~563–605): proof route changed (no error). The limit is obtained by diagonal Banach–Alaoglu
  on the dual of the separable space L¹ together with an L¹–L∞ duality proved in Lean, instead of the manuscript's
  Radon–Nikodym construction.
- (2026-11-06T13:32:49-08:00) `ext:fourier-uniqueness` (tex ~318): proof route changed (no error). The measure is split into four finite
  positive measures (Re±, Im±); conjugate symmetry separates real and imaginary parts and Mathlib's
  `Measure.ext_of_charFun` concludes, instead of Gaussian smoothing.
- (2026-11-06T13:32:49-08:00) `ext:pd-integrable` (tex ~617): proof route changed (no error). Nonnegativity of the Fourier transform is
  obtained by averaging the defining inequality over independent Gaussian samples, instead of a Riemann-sum step.
- (2026-11-06T13:32:49-08:00) `ext:measurable-spectral` (tex ~831): proof route changed (no error). Measurability is shown for bounded
  continuous test functions via Gaussian regularization, then for closed sets via thickened indicators and for all
  Borel sets by a π-system argument, instead of Schwartz tests and smooth cutoffs of open sets.
- (2026-11-06T13:35:47-08:00) `ext:analytic-zero` (tex ~985–1027): proof route changed (no error). Instead of a nonvanishing directional
  derivative plus Rolle along lines, Lean proves the statement by induction on dimension (one-dimensional identity
  theorem, then slices and Fubini), which holds in every dimension; the restriction `d ∈ {1,2,3}` is not needed.
- (2026-11-06T13:53:56-08:00) `cj:binary` (tex ~1084): proof route changed (no error). The bound on the central binomial coefficient is
  proved by induction, (r+1)·C(2r,r)² ≤ 16^r, instead of the exponential/integral estimate.
- (2026-11-06T13:53:56-08:00) `cj:transfer-uniform` (tex ~1480–1540): proof route changed (no error). The Chebyshev/limit argument is replaced
  by an explicit second-moment bound E[(P_w/μ−1)²] ≤ k^r r²/n and Cauchy–Schwarz, giving the explicit threshold
  N = max(r, ⌈r²k^r/(4ζ²)⌉+1).
- (2026-11-06T13:53:56-08:00) `cj:transfer-equal` (tex ~1540–1590): only the pointwise likelihood bound P_w ≤ C·ν is proved (the blueprint
  computes the exact likelihood); the resulting total-variation bound 1−C⁻¹ is the same.
- (2026-11-06T14:24:56-08:00) `cj:binary-pairs` (tex ~1735–1770): proof route slightly changed (no error): uniformity of the pair of chain
  words on each slice comes from a general orbit–stabilizer counting lemma.
- (2026-11-06T14:24:56-08:00) `cj:density-increment` (tex ~1808–1840): proof route slightly changed (no error): in the case a(φ) ≥ α+ε,
  `cj:transfer-equal` is applied directly with r = d (no partition step); in case 2 the two Markov bounds are replaced
  by one weighted average of (2/κ)a + b. Constants unchanged.
- (2026-11-06T14:24:56-08:00) `cj:dhj3` (tex ~1925–1931): the closing "partition [3]^n for n > n_K" step is unnecessary since
  `cj:density-increment` holds for all n ≥ N(d,δ).
- (2026-11-06T14:35:25-08:00) `lem:circle-compact` (tex ~2053–2119): proof route changed (no error). The small-set bound is proved by L²
  duality with the same splitting w_N ≤ H / w_N > H (no measurability of W needed); compactness of TT* is shown by
  writing it as an averaging operator over 𝕋² and a Hilbert–Schmidt (Bessel) argument for the truncated part, without
  constructing the Radon–Nikodym kernel K(z,y).
- (2026-11-06T14:35:25-08:00) `lem:triple-l2` (tex ~2121): the constant C_M is the explicit constant of the reused reference proof,
  N_M/(2π)·(2/|β|)^{1/2} with N_M = ⌈π/h_M⌉+1, h_M = |β|/(4(1+α²+β²)); the statement keeps C_M existential.
- (2026-11-06T14:48:51-08:00) Lean translation fix (not a blueprint error), `rig:def-kernel` (tex ~2294): the auxiliary existence lemma
  `aux_incidenceOp_exists` and `incidenceOp_ae` lacked the hypothesis that the vertex sets X_j are measurable, which
  `rig:def-core` assumes; without it the statement is false (non-measurable X_j). The hypothesis was added; no public
  theorem statement changed. Resolved.
- (2026-11-06T14:48:51-08:00) `rig:kernel-gap` (tex ~2307–2350): proof route changed (no error). Instead of forming A^{-1/2}D*DA^{-1/2}, Lean
  proves ‖D_E f‖² = ⟨Af,f⟩ + ⟨Kf,f⟩ with K compact (off-diagonal blocks via `lem:circle-compact`) and uses a
  real-Hilbert-space version of `ext:compact-gap`.
- (2026-11-06T15:35:17-08:00) `rig:common-core` (tex ~2470): pruning starts from E ∩ E_h ∩ ⋂_j π_j⁻¹(X_j − h), which differs from E ∩ E_h by a
  null set, so that Y_{j,h} ⊆ X_j ∩ (X_j − h) holds exactly (no error).
- (2026-11-06T15:35:17-08:00) `rig:pieces` (tex ~2560–2595): proof route changed (no error). With P(h) = exp(h₁T₁+h₂T₂), the normalized rows
  Φ_j(z)P(−z) are shown to take countably many values a.e. (two-variable Fubini), and E' is a positive-measure level set,
  instead of the six-variable Fubini and change of variables.
- (2026-11-06T15:35:17-08:00) `rig:analytic-rigidity` (tex ~2620–2685): same strategy, different execution (no error): differentiating along
  curves and the θ ↦ θ+π parity give KM = λI = MᵀK directly, hence λ = 0 since β ≠ 0, without the θ-integration step.
- (2026-11-06T16:05:16-08:00) `tail:fourier` (tex ~3446–3473): the limit is taken one slot at a time; only compact Fourier support of f₂ is
  used (no error).
- (2026-11-06T16:05:16-08:00) `tail:partition` (tex ~3570–3612): the L² identity 𝓕(𝓕⁻m * f) = m f̂ is proved by duality; the uniform L¹ kernel
  bound uses a modulation-plus-dilation formula; absolute summability uses u₀u₁ ≤ u₀²+u₁² (no error).
- (2026-11-06T16:05:16-08:00) `tail:one-triple`, `tail:increment`, `tail:bound`: explicit choices C₀₀ = (Σ_j‖V_j‖+1)·D, c = d/4, C = D+d, and an
  explicit partition of unity φ(z) = φ₁(z₀)φ₁(z₁) with Q_* = [0,2]² (no error).
- (2026-11-06T16:17:19-08:00) `ann:form` (tex ~2950–3010): proof route changed (no error): the bounded bilinear form is built on the closures
  of the character spans and composed with orthogonal projections; density of tensor characters in L²(ν₁⊗ν₂) is not
  needed for existence (it is needed later, for `ann:invariance`).
- (2026-11-06T16:40:00-08:00) `ann:displacement` (tex ~3268–3293): proof route changed (no error). Instead of averaging over h, s ∈ [0,H] (which
  would pass an integral through the raw form ℓ_p), discrete Cesàro averages over h ∈ ℕ and h ∈ √2·ℕ isolate {Φ = 0} via
  irrationality of √2. Only the identity needed by the statement (a = 1, G ∈ {1, e_y⊗e_{My}}) is proved.
- (2026-11-06T16:40:00-08:00) `ann:local` (tex ~3178–3215): the cutoff is the indicator of the closure of Q (Q need not be measurable) (no error).
- (2026-11-06T16:44:23-08:00) `tail:bounded-smoothing` (tex ~3746–3781): proof route changed (no error). Existence of the cutoff χ is proved
  explicitly; the low-frequency term is written as ∫ρ_ε(v)(G(v)−G(0))dv and bounded by B³‖q_R(·−v)−q_R‖₁ split at |v| = δ,
  instead of dominated convergence.
- (2026-11-06T16:44:23-08:00) `tail:smoothing` (tex ~3783–3823): `ann:localize` is applied with κ_n = ρ_{ε_n} − δ₀, P_n = δ₀, U = 2; the passage from
  sequences to ε ↓ 0 replaces each sequence by an eventually-equal positive one (no error).
- (2026-11-06T16:57:33-08:00) `den:continuity` (tex ~3831–3855): the auxiliary density ρ is the indicator of the unit square rather than a smooth
  bump; `tail:smoothing` only needs an L¹ probability density (no error).
- (2026-11-06T16:57:33-08:00) `den:select-scales` (tex ~3997–4027): the recursion requires λ_{k+1} > max(λ_k, (k+1)λ_k/η), which still gives
  Σ_{j<k} λ_j < ηλ_k (no error).
- (2026-11-06T16:57:33-08:00) `den:main` (tex ~4029–4082): squares of side L ≥ 5S are used (instead of 2S/(√2−1)) to get |Q+[−S,S]²| ≤ 2|Q|, and
  Σ_{J≠∅} 3^{n−|J|} ≤ 4^n is taken from the binomial identity instead of `den:line-number`; same contradiction (no error).
- (2026-11-06T17:01:57-08:00) `ann:localize` (tex ~3218–3315): proof route changed (no error). The lattice partition of unity is replaced by a
  continuous one (integral over translations q ∈ ℝ²); the tail error is bounded directly by |μ_n|({|u|>U}); Σ_q r_j r_k is
  replaced by ∫(r_j² + r_k²) dq via Tonelli; large parts are truncated at height T‖g‖₂ with Chebyshev.
- (2026-11-06T17:01:57-08:00) `ann:global` (tex ~3316–3377): proof route changed (no error). The R-dependent kernel q_R is replaced, for each η, by
  a fixed C_c^∞ function g with ‖p − g‖₁ ≤ η, so that the Lipschitz bound O(R) follows from g's fixed Lipschitz constant;
  the cost O(η) is uniform in R. The limit is taken by contradiction along R_n → ∞ via `ann:localize` and `ann:local`.
- (2026-11-06T17:04:53-08:00) Resolution of the scope entry above: at the user's request (P8) Section `sec:inverse` ("The Fourier inverse
  consequence", former tex lines 4267–4344, labels `inv:smooth`, `inv:consequence`) was removed from the blueprint, since
  neither Theorem A nor Theorem B uses it; its Status.md entries were removed with it.
