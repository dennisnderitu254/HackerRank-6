//Enter your code here. Read input from STDIN. Print output to STDOUT
[<EntryPoint>]
let main args = 
  let inputs = 
    Seq.initInfinite (fun _ -> System.Console.ReadLine())
    |> Seq.takeWhile (fun s -> s <> null)
    |> Seq.map int
    |> List.ofSeq
  let s, xs = List.head inputs, List.tail inputs
  List.iter (fun x ->
    for i in 1..s do
      printfn "%i" x) xs
  0
