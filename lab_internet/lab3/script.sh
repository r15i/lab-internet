

kathara vstart -n pc1 --eth 0:A
kathara vstart -n r1  --eth 0:Y 1:X 2:A

kathara vstart -n pc2 --eth 0:B  
kathara vstart -n r3  --eth 0:X 1:Z 2:B

kathara vstart -n pc3 --eth 0:C
kathara vstart -n r2 --eth 0:Z 1:Y 2:C
