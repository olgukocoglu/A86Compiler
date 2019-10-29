begin 
  a := 278;
  b := 28 ; 
  while (b) do begin 
       t := b ; 
       b := a mod b ; 
       a := t 
  end ; 
  print a
end 
