from validitycheck import Chess


sample1 = """1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O b5 6. Bb3 Bc5
7. a4 Rb8 8. Nxe5 Nxe5 9. d4 Bxd4 10. Qxd4 d6 11. f4 Nc6
12. Qc3 Ne7 13. axb5 axb5 14. e5 Ne4 15. Qf3 Nc5 16. Ba2 O-O
17. Be3 Bb7 18. Qh3 Ne4 19. Nc3 Nxc3 20. bxc3 Bd5 21. f5 Bxa2
22. Rxa2 dxe5 23. f6 gxf6 24. Bh6 Re8 25. Ra6 Rb6 26. Rxb6
cxb6 27. Qg3+ Ng6 28. h4 f5 29. h5 f4 30. hxg6 hxg6 31. Qg4
Qc8 32. Qh4 Qc5+ 33. Kh2 Qd6 34. Bg5 f5 35. Rf3 e4 36. Rh3 f3+
37. Bf4 Qd7 38. Qh8+ Kf7 39. Rh7+ Ke6 40. Qe5# 1-0"""

sample2 = """1. e4 e5 2. Nf3 Nf6 3. Nxe5 d6 4. Nf3 Nxe4 5. Bd3 Nc5 6. Be2
Be7 7. O-O d5 8. d4 Ne4 9. c4 c6 10. Nc3 O-O 11. Qb3 dxc4
12. Bxc4 Nd6 13. Bd3 Bf6 14. Qc2 h6 15. Bf4 Bg4 16. Ne5 Be6
17. Rad1 Ne8 18. Rfe1 Bg5 19. Bxg5 Qxg5 20. Ne4 Qh4 21. Nc5
Bd5 22. Nxb7 Nf6 23. Nd6 Ng4 24. Bh7+ 1-0"""

s3 = """"1. d4 d5 2. c4 Nf6 3. e3 Nc6 4. cxd5 Qxd5 5. Bc4 Qxg2 6. Bf1 Qxh1 7. Nf3 Bg4 8.
Nbd2 O-O-O 9. Ke2 e6 10. b3 Bb4 11. Bb2 Bxd2 12. Qxd2 Bxf3+ 13. Kd3 Be4+ 14. Kc3
Nd5+ 15. Kc4 Nxd4 16. Kxd4 Nf6+ 17. Ke5 Rxd2 18. Bc3 Qxh2+ 19. f4 Qh5+ 20. f5
Qxf5# 0-1"""


game = Chess()

print(game.analyse(s3))
