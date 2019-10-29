begin
  n := 3 ;
  m := 4 ;
  sum := 0 ; 
  while(n) do begin 
    while(m) do begin 
      sum := sum + n + m
	  m := m-1
    end 
	sum := sum + n
	n:=n-1
  end ; 
  print sum  
end 
