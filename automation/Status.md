# Formalization status

## Introduction and foundations

Lean file: Auto/IntroductionFoundations/IntroductionFoundations.lean

#### Definitions


#### Theorems

\label{intro:density}: [Proof completed] (Lean: Auto.intro_density) (2026-11-06T17:01:48-08:00)
\label{intro:smoothing}: [Proof completed] (Lean: Auto.intro_smoothing) (2026-11-06T17:01:48-08:00)

## Analytic prerequisites with proofs

Lean file: Auto/AnalyticPrerequisitesProofs/

### Fourier analysis in the required form

Lean file: Auto/AnalyticPrerequisitesProofs/FourierAnalysisRequiredForm.lean

#### Definitions

\label{ext:fourier-convention}: [Completed] (Lean: Auto.FCMeasure, Auto.FCMeasure.fourier, Auto.gaussKernel) (2026-11-06T12:48:28-08:00)
\label{ext:bounded-support}: [Completed] (Lean: Auto.HasFourierSupportIn, Auto.HasL2FourierSupportIn) (2026-11-06T12:48:28-08:00)

#### Theorems

\label{ext:young}: [Proof completed] (Lean: Auto.ext_young_one, Auto.ext_young_two, Auto.ext_young_top) (2026-11-06T13:32:49-08:00)
\label{ext:approximation}: [Proof completed] (Lean: Auto.ext_approximation_dense, Auto.ext_approximation_translation, Auto.ext_approximation_translation_config, Auto.ext_approximation_dilation) (2026-11-06T13:32:49-08:00)
\label{ext:gaussian}: [Proof completed] (Lean: Auto.ext_gaussian_integral, Auto.ext_gaussian_fourier, Auto.ext_gaussian_pointwise, Auto.ext_gaussian_uniform) (2026-11-06T13:32:49-08:00)
\label{ext:fourier}: [Proof completed] (Lean: Auto.ext_fourier_maps, Auto.ext_fourier_onto, Auto.ext_fourier_inversion, Auto.ext_fourier_plancherel, Auto.ext_fourier_unitary) (2026-11-06T12:53:22-08:00)
\label{ext:fourier-uniqueness}: [Proof completed] (Lean: Auto.ext_fourier_uniqueness, Auto.ext_fourier_uniqueness_dense) (2026-11-06T13:32:49-08:00)
\label{ext:reproduction}: [Proof completed] (Lean: Auto.ext_reproduction_L2, Auto.ext_reproduction_bounded, Auto.ext_reproduction_agree) (2026-11-06T13:32:49-08:00)

### The compactness facts used for circle operators

Lean file: Auto/AnalyticPrerequisitesProofs/CompactnessFactsCircleOperators.lean

#### Definitions

\label{ext:compact-definition}: [Completed] (Lean: IsCompactOperator) (2026-11-06T12:48:28-08:00)

#### Theorems

\label{ext:compact-facts}: [Proof completed] (Lean: Auto.ext_compact_facts_norm_adjoint, Auto.ext_compact_facts_norm_comp_adjoint, Auto.ext_compact_facts_finite_rank, Auto.ext_compact_facts_limit, Auto.ext_compact_facts_integral, Auto.ext_compact_facts_weak) (2026-11-06T13:21:42-08:00)
\label{ext:ttstar}: [Proof completed] (Lean: Auto.ext_ttstar) (2026-11-06T13:21:42-08:00)
\label{ext:compact-gap}: [Proof completed] (Lean: Auto.ext_compact_gap_ker, Auto.ext_compact_gap) (2026-11-06T13:21:42-08:00)
\label{ext:weakstar}: [Proof completed] (Lean: Auto.ext_weakstar_plane, Auto.ext_weakstar_plane_countable, Auto.ext_weakstar_config, Auto.ext_weakstar_config_countable) (2026-11-06T13:21:42-08:00)

### Spectral measures of the correlation functions

Lean file: Auto/AnalyticPrerequisitesProofs/SpectralMeasuresCorrelationFunctions.lean

#### Definitions

\label{ext:pd-definition}: [Completed] (Lean: Auto.IsPositiveDefinite) (2026-11-06T12:48:28-08:00)
\label{ext:kernel-definition}: [Completed] (Lean: Auto.IsMeasurableKernel) (2026-11-06T12:48:28-08:00)

#### Theorems

\label{ext:pd-integrable}: [Proof completed] (Lean: Auto.ext_pd_integrable_elementary, Auto.ext_pd_integrable_fourier) (2026-11-06T13:32:49-08:00)
\label{ext:tight-measures}: [Proof completed] (Lean: Auto.ext_tight_measures) (2026-11-06T13:32:49-08:00)
\label{ext:bochner}: [Proof completed] (Lean: Auto.ext_bochner, Auto.ext_bochner_mass_le_one) (2026-11-06T13:32:49-08:00)
\label{ext:measurable-spectral}: [Proof completed] (Lean: Auto.ext_measurable_spectral) (2026-11-06T13:32:49-08:00)
\label{ext:kernel-integration}: [Proof completed] (Lean: Auto.ext_kernel_integration_measurable, Auto.ext_kernel_integration_measurable_complex, Auto.ext_kernel_integration_measure, Auto.ext_kernel_integration_prod) (2026-11-06T13:32:49-08:00)

### Local matrix groups and analytic zero sets

Lean file: Auto/AnalyticPrerequisitesProofs/LocalMatrixGroupsAnalyticZeroSets.lean

#### Definitions


#### Theorems

\label{ext:matrix-group}: [Proof completed] (Lean: Auto.ext_matrix_group, Auto.ext_matrix_group_analytic) (2026-11-06T13:35:47-08:00)
\label{ext:analytic-zero}: [Proof completed] (Lean: Auto.ext_analytic_zero, Auto.ext_analytic_zero_config) (2026-11-06T13:35:47-08:00)

## Finite words, binary density, and tilings

Lean file: Auto/FiniteWordsBinaryDensityTilings/FiniteWordsBinaryDensityTilings.lean

#### Definitions

\label{cj:def-words}: [Completed] (Lean: Auto.unifDensity, Auto.subspacePts, Auto.relDensity, Auto.binEmb, Auto.binaryCube, Auto.binaryFace, Auto.concatW, Auto.suffixFiber, Auto.ContainsSubspace, Auto.ContainsLine) (2026-11-06T12:36:07-08:00)
\label{cj:insensitive}: [Completed] (Lean: Auto.InsEquiv, Auto.IsInsensitive, Auto.IsInsensitiveIn) (2026-11-06T12:36:07-08:00)

#### Theorems

\label{cj:bookkeeping}: [Proof completed] (Lean: Auto.cj_bookkeeping_card, Auto.cj_bookkeeping_comp, Auto.cj_bookkeeping_concat, Auto.cj_bookkeeping_count_subspaces, Auto.cj_bookkeeping_count_lines) (2026-11-06T12:36:07-08:00)
\label{cj:binary}: [Proof completed] (Lean: Auto.C_cj_binary, Auto.cj_binary) (2026-11-06T13:53:56-08:00)
\label{cj:binary-multi}: [Proof completed] (Lean: Auto.C_cj_binary_multi, Auto.cj_binary_multi) (2026-11-06T13:53:56-08:00)
\label{cj:fiber}: [Proof completed] (Lean: Auto.C_cj_fiber, Auto.cj_fiber) (2026-11-06T13:53:56-08:00)
\label{cj:binary-face}: [Proof completed] (Lean: Auto.C_cj_binary_face, Auto.cj_binary_face) (2026-11-06T13:53:56-08:00)
\label{cj:insensitive-facts}: [Proof completed] (Lean: Auto.cj_insensitive_facts_union, Auto.cj_insensitive_facts_inter, Auto.cj_insensitive_facts_compl, Auto.cj_insensitive_facts_fix, Auto.cj_insensitive_facts_preimage, Auto.cj_insensitive_facts_face) (2026-11-06T12:36:07-08:00)
\label{cj:tile-one}: [Proof completed] (Lean: Auto.C_cj_tile_one, Auto.cj_tile_one) (2026-11-06T13:53:56-08:00)
\label{cj:tile-two}: [Proof completed] (Lean: Auto.C_cj_tile_two, Auto.cj_tile_two) (2026-11-06T13:53:56-08:00)

### Equal-slices averaging and the three-letter theorem

Lean file: Auto/FiniteWordsBinaryDensityTilings/EqualSlicesAveragingThreeLetterTheorem.lean

#### Definitions

\label{cj:equal-slices}: [Completed] (Lean: Auto.equalSlices, Auto.dTV) (2026-11-06T12:36:07-08:00)
\label{cj:restriction}: [Completed] (Lean: Auto.restrictMap, Auto.restrictPre) (2026-11-06T12:36:07-08:00)
\label{cj:collapse}: [Completed] (Lean: Auto.collapse, Auto.collapseSet, Auto.collapseBoth, Auto.binaryTrace) (2026-11-06T12:36:07-08:00)

#### Theorems

\label{cj:probability-facts}: [Proof completed] (Lean: Auto.cj_probability_facts_atom, Auto.cj_probability_facts_binary_face_mass, Auto.cj_probability_facts_tv_function, Auto.cj_probability_facts_mixture) (2026-11-06T13:53:56-08:00)
\label{cj:transfer-uniform}: [Proof completed] (Lean: Auto.cj_transfer_uniform) (2026-11-06T13:53:56-08:00)
\label{cj:transfer-equal}: [Proof completed] (Lean: Auto.cj_transfer_equal, Auto.cj_transfer_equal_average) (2026-11-06T13:53:56-08:00)
\label{cj:binary-pairs}: [Proof completed] (Lean: Auto.cj_binary_pairs_insensitive, Auto.cj_binary_pairs_bound, Auto.cj_binary_pairs_forbidden) (2026-11-06T14:24:56-08:00)
\label{cj:density-increment}: [Proof completed] (Lean: Auto.C_cj_density_increment, Auto.cj_density_increment) (2026-11-06T14:24:56-08:00)
\label{cj:dhj3}: [Proof completed] (Lean: Auto.cj_dhj3) (2026-11-06T14:24:56-08:00)

## Geometry, forms, and elementary estimates

Lean file: Auto/GeometryFormsElementaryEstimates/GeometryFormsElementaryEstimates.lean

#### Definitions

\label{def:geometry}: [Completed] (Lean: Auto.J, Auto.M, Auto.Lv, Auto.Ang, Auto.u, Auto.v, Auto.σ, Auto.μinc, Auto.proj, Auto.FCMeasure.sigma) (2026-11-06T12:23:06-08:00)
\label{def:form}: [Completed] (Lean: Auto.FCMeasure, Auto.form, Auto.endNorm, Auto.formNorm, Auto.FCMeasure.tv, Auto.FCMeasure.dil) (2026-11-06T12:23:06-08:00)
\label{def:fourier}: [Completed] (Lean: Auto.e, Auto.scaleR) (2026-11-06T12:23:06-08:00)

#### Theorems

\label{lem:geometry}: [Proof completed] (Lean: Auto.lem_geometry_differences, Auto.lem_geometry_commute, Auto.lem_geometry_normalization, Auto.lem_geometry_measurePreserving) (2026-11-06T14:35:25-08:00)
\label{lem:form-basic}: [Proof completed] (Lean: Auto.lem_form_basic_integrable, Auto.lem_form_basic_bound, Auto.lem_form_basic_scaling, Auto.lem_form_basic_ae, Auto.lem_form_basic_translate) (2026-11-06T14:35:25-08:00)
\label{lem:convolution-translate}: [Proof completed] (Lean: Auto.lem_convolution_translate, Auto.lem_convolution_translate_norm, Auto.lem_convolution_translate_general) (2026-11-06T14:35:25-08:00)
\label{lem:fourier-form}: [Proof completed] (Lean: Auto.lem_fourier_form, Auto.lem_fourier_form_multiplier) (2026-11-06T14:35:25-08:00)
\label{lem:circle-difference}: [Proof completed] (Lean: Auto.lem_circle_difference) (2026-11-06T14:35:25-08:00)
\label{lem:circle-compact}: [Proof completed] (Lean: Auto.circleOp, Auto.lem_circle_compact_small, Auto.lem_circle_compact) (2026-11-06T14:35:25-08:00)
\label{lem:triple-l2}: [Proof completed] (Lean: Auto.lem_triple_l2, Auto.lem_triple_l2_sigma) (2026-11-06T14:35:25-08:00)
\label{lem:small-support}: [Proof completed] (Lean: Auto.lem_small_support) (2026-11-06T14:35:25-08:00)

## Finite-dimensional scalar kernels

Lean file: Auto/FiniteDimensionalScalarKernels/FiniteDimensionalScalarKernels.lean

#### Definitions

\label{rig:def-core}: [Completed] (Lean: Auto.degree, Auto.IsCoreData, Auto.IsCore) (2026-11-06T12:28:18-08:00)
\label{rig:def-kernel}: [Completed] (Lean: Auto.HE, Auto.incidenceOp, Auto.incidenceOp_ae, Auto.kernelSpace) (2026-11-06T14:48:51-08:00)

#### Theorems

\label{rig:degree-integration}: [Proof completed] (Lean: Auto.rig_degree_integration, Auto.rig_degree_integration_bounds, Auto.rig_degree_integration_total, Auto.rig_degree_integration_null) (2026-11-06T14:48:51-08:00)
\label{rig:prune}: [Proof completed] (Lean: Auto.rig_prune) (2026-11-06T14:48:51-08:00)
\label{rig:kernel-gap}: [Proof completed] (Lean: Auto.rig_kernel_gap_finiteDimensional, Auto.rig_kernel_gap) (2026-11-06T14:48:51-08:00)
\label{rig:kernel-ui}: [Proof completed] (Lean: Auto.rig_kernel_ui) (2026-11-06T14:48:51-08:00)
\label{rig:kernel-stability}: [Proof completed] (Lean: Auto.rig_kernel_stability) (2026-11-06T14:48:51-08:00)

## Analytic pieces and measurable rigidity

Lean file: Auto/AnalyticPiecesMeasurableRigidity/AnalyticPiecesMeasurableRigidity.lean

#### Definitions


#### Theorems

\label{rig:common-core}: [Proof completed] (Lean: Auto.rig_common_core) (2026-11-06T15:35:17-08:00)
\label{rig:translation-matrices}: [Proof completed] (Lean: Auto.rig_translation_matrices) (2026-11-06T15:35:17-08:00)
\label{rig:pieces}: [Proof completed] (Lean: Auto.rig_pieces) (2026-11-06T15:35:17-08:00)
\label{rig:analytic-rigidity}: [Proof completed] (Lean: Auto.rig_analytic_rigidity) (2026-11-06T15:35:17-08:00)
\label{rig:exact}: [Proof completed] (Lean: Auto.rig_exact) (2026-11-06T15:35:17-08:00)

## Translation correlations and local cancellation

Lean file: Auto/TranslationCorrelationsLocalCancellation/TranslationCorrelationsLocalCancellation.lean

#### Definitions

\label{ann:sequence}: [Completed] (Lean: Auto.IsAdmissibleSeq, Auto.annT, Auto.annWeakStar) (2026-11-06T12:50:39-08:00)
\label{ann:polynomials}: [Completed] (Lean: Auto.charE, Auto.trigPoly, Auto.tensorPoly, Auto.polyTranslate, Auto.tensorTranslate) (2026-11-06T12:50:39-08:00)

#### Theorems

\label{ann:extract}: [Proof completed] (Lean: Auto.ann_extract) (2026-11-06T16:17:19-08:00)
\label{ann:spectral}: [Proof completed] (Lean: Auto.ann_spectral) (2026-11-06T16:17:19-08:00)
\label{ann:factor}: [Proof completed] (Lean: Auto.ann_factor_one, Auto.ann_factor_two) (2026-11-06T16:17:19-08:00)
\label{ann:form}: [Proof completed] (Lean: Auto.ann_form) (2026-11-06T16:17:19-08:00)
\label{ann:invariance}: [Proof completed] (Lean: Auto.ann_invariance) (2026-11-06T16:40:00-08:00)
\label{ann:fibers}: [Proof completed] (Lean: Auto.annH, Auto.ann_fibers, Auto.ann_fibers_hyperplane) (2026-11-06T16:17:19-08:00)
\label{ann:selectors}: [Proof completed] (Lean: Auto.ann_selectors) (2026-11-06T16:17:19-08:00)
\label{ann:atomic-rigidity}: [Proof completed] (Lean: Auto.ann_atomic_rigidity) (2026-11-06T16:40:00-08:00)
\label{ann:displacement}: [Proof completed] (Lean: Auto.ann_displacement) (2026-11-06T16:40:00-08:00)
\label{ann:local}: [Proof completed] (Lean: Auto.ann_local) (2026-11-06T16:40:00-08:00)

## Localization and a global annular estimate

Lean file: Auto/LocalizationGlobalAnnularEstimate/LocalizationGlobalAnnularEstimate.lean

#### Definitions


#### Theorems

\label{ann:localize}: [Proof completed] (Lean: Auto.ann_localize) (2026-11-06T16:44:23-08:00)
\label{ann:global}: [Proof completed] (Lean: Auto.ann_global) (2026-11-06T17:01:48-08:00)

## Summation over frequency annuli

Lean file: Auto/SummationFrequencyAnnuli/SummationFrequencyAnnuli.lean

#### Definitions

\label{tail:annular-definition}: [Completed] (Lean: Auto.tailPsi, Auto.tailQ, Auto.tailK, Auto.tailForm, Auto.aux_tail_annular_definition) (2026-11-06T16:05:16-08:00)
\label{tail:coordinates}: [Completed] (Lean: Auto.tailA, Auto.tailT) (2026-11-06T12:50:39-08:00)
\label{tail:partition-definition}: [Completed] (Lean: Auto.latticePt, Auto.tailP, Auto.tailSquare, Auto.tailMu, Auto.tailContributing) (2026-11-06T12:50:39-08:00)
\label{tail:mass-definition}: [Completed] (Lean: Auto.tailH) (2026-11-06T12:50:39-08:00)

#### Theorems

\label{tail:fourier}: [Proof completed] (Lean: Auto.tail_fourier) (2026-11-06T16:05:16-08:00)
\label{tail:separation}: [Proof completed] (Lean: Auto.tailV, Auto.tail_separation_identities, Auto.tail_separation_comparable, Auto.tail_separation_modulation, Auto.tail_separation_translate) (2026-11-06T16:05:16-08:00)
\label{tail:partition}: [Proof completed] (Lean: Auto.tail_partition) (2026-11-06T16:05:16-08:00)
\label{tail:one-triple}: [Proof completed] (Lean: Auto.tail_one_triple) (2026-11-06T16:05:16-08:00)
\label{tail:increment}: [Proof completed] (Lean: Auto.tail_increment) (2026-11-06T16:05:16-08:00)
\label{tail:telescoping}: [Proof completed] (Lean: Auto.tail_telescoping) (2026-11-06T16:05:16-08:00)
\label{tail:bound}: [Proof completed] (Lean: Auto.tail_bound, Auto.tail_bound_tendsto) (2026-11-06T17:01:48-08:00)

## Approximation of the counting form

Lean file: Auto/ApproximationCountingForm/ApproximationCountingForm.lean

#### Definitions


#### Theorems

\label{tail:exhaustion}: [Proof completed] (Lean: Auto.tail_exhaustion) (2026-11-06T16:44:23-08:00)
\label{tail:convolved-tail}: [Proof completed] (Lean: Auto.tail_convolved_tail, Auto.tail_convolved_tail_sum) (2026-11-06T17:01:48-08:00)
\label{tail:bounded-smoothing}: [Proof completed] (Lean: Auto.tail_bounded_smoothing) (2026-11-06T17:01:48-08:00)
\label{tail:smoothing}: [Proof completed] (Lean: Auto.tail_smoothing) (2026-11-06T17:01:48-08:00)

## From smoothing to triangles

Lean file: Auto/FromSmoothingTriangles/FromSmoothingTriangles.lean

#### Definitions

\label{den:definitions}: [Completed] (Lean: Auto.squareAt, Auto.upperBanachDensity, Auto.triangleCount, Auto.IsMissed) (2026-11-06T12:23:06-08:00)
\label{den:lines}: [Completed] (Lean: Auto.lineVarSet, Auto.subsum) (2026-11-06T12:49:07-08:00)

#### Theorems

\label{den:continuity}: [Proof completed] (Lean: Auto.den_continuity) (2026-11-06T17:01:48-08:00)
\label{den:dense-squares}: [Proof completed] (Lean: Auto.den_dense_squares_exists, Auto.den_dense_squares_borel, Auto.den_dense_squares_missed, Auto.den_dense_squares_copy) (2026-11-06T14:05:18-08:00)
\label{den:line-number}: [Proof completed] (Lean: Auto.den_line_number_fixed, Auto.den_line_number) (2026-11-06T14:05:18-08:00)
\label{den:weighted-lower}: [Proof completed] (Lean: Auto.den_weighted_lower) (2026-11-06T14:05:18-08:00)
\label{den:select-scales}: [Proof completed] (Lean: Auto.den_select_scales) (2026-11-06T17:01:48-08:00)
\label{den:main}: [Proof completed] (Lean: Auto.den_main, Auto.den_main_general) (2026-11-06T17:01:48-08:00)
