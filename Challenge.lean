/- Copyright (c) 2026 Polona Durcik. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
This file was assembled by Claude from the statement files `TrianglesInThePlane/Auto/Theorems.lean`
and `TrianglesInThePlane/Auto/Definitions.lean`, whose statements were checked against the
blueprint by the author.
-/

module

public import Mathlib.Algebra.Order.Archimedean.Real.Hom
public import Mathlib.Analysis.Distribution.SchwartzSpace.Basic
public import Mathlib.Analysis.Fourier.AddCircle
public import Mathlib.Analysis.Fourier.Notation
public import Mathlib.Analysis.Normed.Lp.MeasurableSpace
public import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv
public import Mathlib.LinearAlgebra.AffineSpace.FiniteDimensional
public import Mathlib.MeasureTheory.Integral.Prod
public import Mathlib.MeasureTheory.Measure.Haar.OfBasis
public import Mathlib.MeasureTheory.Measure.RegularityCompacts
public import Mathlib.Order.CompletePartialOrder
public import Mathlib.Topology.UniformSpace.Uniformizable

/-!
# Challenge file for Comparator
-/

open MeasureTheory Real Set Filter Topology
open scoped ENNReal NNReal FourierTransform InnerProductSpace SchwartzMap ComplexConjugate

@[expose] public noncomputable section

namespace Auto

/-- The Euclidean plane `ℝ²`. -/
scoped notation "ℝ²" => EuclideanSpace ℝ (Fin 2)

/-- The closed axis-parallel square `z + [0,L]²` with lower-left corner `z` and side length `L`. -/
def squareAt (z : ℝ²) (L : ℝ) : Set ℝ² := {x | ∀ i, x i ∈ Icc (z i) (z i + L)}

/-- The upper Banach density
$$d^*(E)=\limsup_{L\to\infty}\sup_{z\in\mathbb{R}^2}\frac{|E\cap(z+[0,L]^2)|}{L^2},$$
where `|·|` is Lebesgue measure. -/
def upperBanachDensity (E : Set ℝ²) : ℝ≥0∞ :=
  limsup (fun L : ℝ => ⨆ z : ℝ², volume (E ∩ squareAt z L) / ENNReal.ofReal (L ^ 2)) atTop

/-- The rotation by a right angle, `J(x₁, x₂) = (-x₂, x₁)`. -/
def J : ℝ² →L[ℝ] ℝ² :=
  LinearMap.toContinuousLinearMap
    { toFun := fun x => !₂[-x 1, x 0]
      map_add' := fun x y => by
        ext i; fin_cases i <;> simp [add_comm]
      map_smul' := fun c x => by
        ext i; fin_cases i <;> simp }

/-- The linear map `aI + bJ` of the plane, i.e. multiplication by the complex number `a + bi`. -/
def simil (a b : ℝ) : ℝ² →L[ℝ] ℝ² := a • ContinuousLinearMap.id ℝ ℝ² + b • J

/-- The counterclockwise rotation by angle `t`: `R_t = (cos t) I + (sin t) J`. -/
abbrev rot (t : ℝ) : ℝ² →L[ℝ] ℝ² := simil (Real.cos t) (Real.sin t)

/-- **Triangles in sets of positive upper density in the plane.** Let `a`, `b`, `c` be three
noncollinear points of the plane, forming a triangle `Δ = {a, b, c}`, and let `E` be a
(null-)measurable subset of the plane with positive upper Banach density. Then there is a
threshold `λ₀ > 0` such that for every scale `λ ≥ λ₀` the set `E` contains a translated and
rotated copy of the dilated triangle `λΔ`: there are a translation vector `x` and an angle `t`
such that `x + R_t(λp) ∈ E` for each vertex `p` of `Δ`. -/
theorem triangles_in_the_plane (a b c : ℝ²) (hΔ : ¬ Collinear ℝ ({a, b, c} : Set ℝ²)) (E : Set ℝ²)
    (hE : NullMeasurableSet E volume) (hd : 0 < upperBanachDensity E) :
    ∃ lam₀ : ℝ, 0 < lam₀ ∧ ∀ lam : ℝ, lam₀ ≤ lam →
      ∃ (x : ℝ²) (t : ℝ), ∀ p ∈ ({a, b, c} : Set ℝ²), x + rot t (lam • p) ∈ E :=
  sorry

end Auto
