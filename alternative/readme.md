It's possible a system uses a different standard for NEC codes. This summary was provided by a user on the retrotink discord server.

My issues with the codes were that:

- My system was assuming all NEC "address" codes were 8bit + 8bit checksum, but the reality is that many NEC codes actually use a 16bit address, this includes the Disney codes. The "command" section remains 8bit + 8bit with checksum. I've now changed my own IR blaster to support 16bit address codes.
- My system also expects the bits for both address and command values to be reversed (LSB vs MSB). 

Number1 - 0xE144A25D

Number2 - 0xE144629D

Number3 - 0xE144E21D

Number4 - 0xE14412ED

Number5 - 0xE144926D

Number6 - 0xE14452AD

Number7 - 0xE144D22D

Number8 - 0xE14432CD

Number9 - 0xE144B24D

Number0 - 0xE144728D (Loads Profile 10)
