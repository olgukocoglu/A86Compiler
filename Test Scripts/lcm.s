begin 
  a := 89 ; 
  b := 67 ; 
  aa := a ; 
  bb := b ; 
  while (b) do begin 
       t := b ; 
       b := a mod b ; 
       a := t 
  end ; 
  gcd := a ; 
  lcm := (aa*bb) / gcd ; 
  print lcm 
end 
