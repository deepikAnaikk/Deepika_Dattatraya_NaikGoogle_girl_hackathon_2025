module example (input a, b, output c);
  assign temp = a & b;
  assign c = temp | a;
endmodule
