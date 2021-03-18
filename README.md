Advent of Code 2020
=====================
My [Advent of Code 2020][aoc] Python solutions here.

[aoc]: https://adventofcode.com/2020

<!-- 
Summaries & Code
-----------------------------------------
| Challenge |  Summaries  |   Code    |
| --------- | ----------- | --------- |
| Day  1    | [x][d01r]   | [x][d01g] |
| Day  2    | [x][d02r]   | [x][d02g] |
| Day  3    | [x][d03r]   | [x][d03g] |
| Day  4    | [x][d04r]   | [x][d04g] |
| Day  5    | [x][d05r]   | [x][d05g] |
| Day  6    | [x][d06r]   | [x][d06g] |
| Day  7    | [x][d07r]   | [x][d07g] |
| Day  8    | [x][d08r]   | [x][d08g] |
| Day  9    | [x][d09r]   | [x][d09g] |
| Day 10    | [x][d10r]   | [x][d10g] |
| Day 11    | [x][d11r]   | [x][d11g] |
| Day 12    | [x][d12r]   | [x][d12g] |
| Day 13    | [x][d13r]   | [x][d13g] |
| Day 14    | [x][d14r]   | [x][d14g] |
| Day 15    | [x][d15r]   | [x][d15g] |
| Day 16    | [x][d16r]   | [x][d16g] |
| Day 17    | [x][d17r]   | [x][d17g] |
| Day 18    | [x][d18r]   | [x][d18g] |
| Day 19    | [x][d19r]   | [x][d19g] |
| Day 20    | [x][d20r]   | [x][d20g] |
| Day 21    | [x][d21r]   | [x][d21g] |
| Day 22    | [x][d22r]   | [x][d22g] |
| Day 23    | [x][d23r]   | [x][d23g] |
| Day 24    | [x][d24r]   | [x][d24g] |
| Day 25    | [x][d25r]   | [x][d25g] |

[d01g]: https://github.com/kggurram/advent-of-code-2020/blob/master/src/AOC/Challenge/Day01.hs
[d01r]: https://github.com/kggurram/advent-of-code-2020/blob/master/reflections.md#day-1
[d02g]: https://github.com/kggurram/advent-of-code-2020/blob/master/src/AOC/Challenge/Day02.hs
[d02r]: https://github.com/kggurram/advent-of-code-2020/blob/master/reflections.md#day-2
[d03g]: https://github.com/kggurram/advent-of-code-2020/blob/master/src/AOC/Challenge/Day03.hs
[d03r]: https://github.com/kggurram/advent-of-code-2020/blob/master/reflections.md#day-3
[d04g]: https://github.com/kggurram/advent-of-code-2020/blob/master/src/AOC/Challenge/Day04.hs
[d04r]: https://github.com/kggurram/advent-of-code-2020/blob/master/reflections.md#day-4
[d05g]: https://github.com/kggurram/advent-of-code-2020/blob/master/src/AOC/Challenge/Day05.hs
[d05r]: https://github.com/kggurram/advent-of-code-2020/blob/master/reflections.md#day-5
[d06g]: https://github.com/kggurram/advent-of-code-2020/blob/master/src/AOC/Challenge/Day06.hs
[d06r]: https://github.com/kggurram/advent-of-code-2020/blob/master/reflections.md#day-6
[d07g]: https://github.com/kggurram/advent-of-code-2020/blob/master/src/AOC/Challenge/Day07.hs
[d07r]: https://github.com/kggurram/advent-of-code-2020/blob/master/reflections.md#day-7
[d08g]: https://github.com/kggurram/advent-of-code-2020/blob/master/src/AOC/Challenge/Day08.hs
[d08r]: https://github.com/kggurram/advent-of-code-2020/blob/master/reflections.md#day-8
[d09g]: https://github.com/kggurram/advent-of-code-2020/blob/master/src/AOC/Challenge/Day09.hs
[d09r]: https://github.com/kggurram/advent-of-code-2020/blob/master/reflections.md#day-9
[d10g]: https://github.com/kggurram/advent-of-code-2020/blob/master/src/AOC/Challenge/Day10.hs
[d10r]: https://github.com/kggurram/advent-of-code-2020/blob/master/reflections.md#day-10
[d11g]: https://github.com/kggurram/advent-of-code-2020/blob/master/src/AOC/Challenge/Day11.hs
[d11r]: https://github.com/kggurram/advent-of-code-2020/blob/master/reflections.md#day-11
[d12g]: https://github.com/kggurram/advent-of-code-2020/blob/master/src/AOC/Challenge/Day12.hs
[d12r]: https://github.com/kggurram/advent-of-code-2020/blob/master/reflections.md#day-12
[d13g]: https://github.com/kggurram/advent-of-code-2020/blob/master/src/AOC/Challenge/Day13.hs
[d13r]: https://github.com/kggurram/advent-of-code-2020/blob/master/reflections.md#day-13
[d14g]: https://github.com/kggurram/advent-of-code-2020/blob/master/src/AOC/Challenge/Day14.hs
[d14r]: https://github.com/kggurram/advent-of-code-2020/blob/master/reflections.md#day-14
[d15g]: https://github.com/kggurram/advent-of-code-2020/blob/master/src/AOC/Challenge/Day15.hs
[d15r]: https://github.com/kggurram/advent-of-code-2020/blob/master/reflections.md#day-15
[d16g]: https://github.com/kggurram/advent-of-code-2020/blob/master/src/AOC/Challenge/Day16.hs
[d16r]: https://github.com/kggurram/advent-of-code-2020/blob/master/reflections.md#day-16
[d17g]: https://github.com/kggurram/advent-of-code-2020/blob/master/src/AOC/Challenge/Day17.hs
[d17r]: https://github.com/kggurram/advent-of-code-2020/blob/master/reflections.md#day-17
[d18g]: https://github.com/kggurram/advent-of-code-2020/blob/master/src/AOC/Challenge/Day18.hs
[d18r]: https://github.com/kggurram/advent-of-code-2020/blob/master/reflections.md#day-18
[d19g]: https://github.com/kggurram/advent-of-code-2020/blob/master/src/AOC/Challenge/Day19.hs
[d19r]: https://github.com/kggurram/advent-of-code-2020/blob/master/reflections.md#day-19
[d20g]: https://github.com/kggurram/advent-of-code-2020/blob/master/src/AOC/Challenge/Day20.hs
[d20r]: https://github.com/kggurram/advent-of-code-2020/blob/master/reflections.md#day-20
[d21g]: https://github.com/kggurram/advent-of-code-2020/blob/master/src/AOC/Challenge/Day21.hs
[d21r]: https://github.com/kggurram/advent-of-code-2020/blob/master/reflections.md#day-21
[d22g]: https://github.com/kggurram/advent-of-code-2020/blob/master/src/AOC/Challenge/Day22.hs
[d22r]: https://github.com/kggurram/advent-of-code-2020/blob/master/reflections.md#day-22
[d23g]: https://github.com/kggurram/advent-of-code-2020/blob/master/src/AOC/Challenge/Day23.hs
[d23r]: https://github.com/kggurram/advent-of-code-2020/blob/master/reflections.md#day-23
[d24g]: https://github.com/kggurram/advent-of-code-2020/blob/master/src/AOC/Challenge/Day24.hs
[d24r]: https://github.com/kggurram/advent-of-code-2020/blob/master/reflections.md#day-24
[d25g]: https://github.com/kggurram/advent-of-code-2020/blob/master/src/AOC/Challenge/Day25.hs
[d25r]: https://github.com/kggurram/advent-of-code-2020/blob/master/reflections.md#day-25 -->
