"""Generate the skeleton of automation/Status.md from blueprint/triangles_in_the_plane_blueprint.tex (run once)."""
import re, datetime, subprocess
tex = open('blueprint/triangles_in_the_plane_blueprint.tex').read().split('\n')
ts = subprocess.check_output(['date', '+%Y-%m-%dT%H:%M:%S%z']).decode().strip()
files = {
 'Introduction and foundations': 'Auto/IntroductionFoundations/IntroductionFoundations.lean',
 'Analytic prerequisites with proofs': 'Auto/AnalyticPrerequisitesProofs/',
 'Fourier analysis in the required form': 'Auto/AnalyticPrerequisitesProofs/FourierAnalysisRequiredForm.lean',
 'The compactness facts used for circle operators': 'Auto/AnalyticPrerequisitesProofs/CompactnessFactsCircleOperators.lean',
 'Spectral measures of the correlation functions': 'Auto/AnalyticPrerequisitesProofs/SpectralMeasuresCorrelationFunctions.lean',
 'Local matrix groups and analytic zero sets': 'Auto/AnalyticPrerequisitesProofs/LocalMatrixGroupsAnalyticZeroSets.lean',
 'Finite words, binary density, and tilings': 'Auto/FiniteWordsBinaryDensityTilings/FiniteWordsBinaryDensityTilings.lean',
 'Equal-slices averaging and the three-letter theorem': 'Auto/FiniteWordsBinaryDensityTilings/EqualSlicesAveragingThreeLetterTheorem.lean',
 'Geometry, forms, and elementary estimates': 'Auto/GeometryFormsElementaryEstimates/GeometryFormsElementaryEstimates.lean',
 'Finite-dimensional scalar kernels': 'Auto/FiniteDimensionalScalarKernels/FiniteDimensionalScalarKernels.lean',
 'Analytic pieces and measurable rigidity': 'Auto/AnalyticPiecesMeasurableRigidity/AnalyticPiecesMeasurableRigidity.lean',
 'Translation correlations and local cancellation': 'Auto/TranslationCorrelationsLocalCancellation/TranslationCorrelationsLocalCancellation.lean',
 'Localization and a global annular estimate': 'Auto/LocalizationGlobalAnnularEstimate/LocalizationGlobalAnnularEstimate.lean',
 'Summation over frequency annuli': 'Auto/SummationFrequencyAnnuli/SummationFrequencyAnnuli.lean',
 'Approximation of the counting form': 'Auto/ApproximationCountingForm/ApproximationCountingForm.lean',
 'From smoothing to triangles': 'Auto/FromSmoothingTriangles/FromSmoothingTriangles.lean',
}
out = ['# Formalization status', '',
 'Definitions use `Todo` or `Completed`. Theorems use `Todo`, `Statement completed`, or `Proof completed`; '
 'the latter means that the proof is sorry-free and depends only on standard axioms.', '']
blocks = []  # (level, title, defs, thms)
cur = None
i = 0
while i < len(tex):
    l = tex[i]
    m = re.match(r'\\(sub)?section\{(.*?)\}', l)
    if m:
        cur = ['##' if not m.group(1) else '###', m.group(2), [], []]
        blocks.append(cur); i += 1; continue
    m = re.match(r'\\begin\{(definition|theorem|lemma|proposition|corollary|maintheorem)\}', l)
    if m:
        kind = m.group(1)
        seg = l + (tex[i+1] if i + 1 < len(tex) else '')
        lab = re.findall(r'\\label\{([^}]*)\}', seg)[0]
        (cur[2] if kind == 'definition' else cur[3]).append(lab)
    i += 1
for lev, title, defs, thms in blocks:
    out += [f'{lev} {title}', '', f'Lean file: {files.get(title, "")}', '']
    if not defs and not thms:
        continue
    out += ['#### Definitions', '']
    out += [f'\\label{{{d}}}: [Todo] (Lean: ) ({ts})' for d in defs]
    out += ['', '#### Theorems', '']
    out += [f'\\label{{{t}}}: [Todo] (Lean: ) ({ts})' for t in thms]
    out += ['']
open('automation/Status.md', 'w').write('\n'.join(out) + '\n')
