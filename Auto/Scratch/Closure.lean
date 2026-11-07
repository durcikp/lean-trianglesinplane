import Auto
open Lean Meta Elab Command
partial def go (env : Environment) (todo : List Name) (seen : NameSet) : NameSet :=
  match todo with
  | [] => seen
  | n :: rest =>
    if seen.contains n then go env rest seen else
    let seen := seen.insert n
    match env.find? n with
    | none => go env rest seen
    | some ci =>
      let cs := ci.type.getUsedConstants ++ ((ci.value? (allowOpaque := true)).map (·.getUsedConstants) |>.getD #[])
      let cs := match ci with
        | .inductInfo i => cs ++ i.ctors.toArray
        | _ => cs
      let new := cs.toList.filter (fun c => c.getRoot == `Auto)
      go env (new ++ rest) seen
elab "#closure" : command => do
  let env ← getEnv
  let mut roots : List Name := []
  for n in [`Auto.intro_density, `Auto.intro_smoothing] do
    let some ci := env.find? n | throwError "no {n}"
    roots := roots ++ (ci.type.getUsedConstants.toList.filter (·.getRoot == `Auto))
  let s := go env roots {}
  let names := s.toList.filter (fun n => !n.isInternal) |>.map toString |>.toArray.qsort (· < ·)
  for n in names do
    let mod := (env.getModuleIdxFor? n.toName).map (fun i => env.header.moduleNames[i.toNat]!) |>.getD `none
    logInfo m!"{mod} {n}"
#closure
