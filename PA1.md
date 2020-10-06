# PA1

## Hurdles

Upfront, the biggest hurdle was understanding the problem. I was thrown off by the new information about DNA, and had to reread to filter out the problem we were solving. 

Once I understood the problem, I was looking for input files. ~~I didn't realize we had to create our own~~. I eventually found them in the examples section.

The next step was planning. I had to start with the part I was unsure about: exceptions. I thought of and listed out all the exceptions I could anticipate. I then left them till the end to implement since I already mapped them out.

I then planned my code in comments and got to work (like a savage).

## Source Code

```py
TODO: add exceptions first
```

## Input Files

```sh
tail -n +1 pa1_input/* | xclip
----
==> pa1_input/seq1.txt <==
ACTGACTTTT

==> pa1_input/seq2.txt <==
TTTAGCCGAT

==> pa1_input/seq3.txt <==
TTTTGTCGAT

==> pa1_input/seq4.txt <==
TTTAGCCGATT

==> pa1_input/seq5.txt <==
ACTGAGCT

==> pa1_input/seq6.txt <==
ACTBCGACTA
```

## Example runs
```sh
Enter mode (0 = match, 1 = contiguous): 1
Enter max number of shifts to test (no entry = default, default = 5):
First sequence (1-5): 1
Second sequence (1-5): 4

Lengths do not match!

Terminating program...

```

```sh
Enter mode (0 = match, 1 = contiguous): 1
Enter max number of shifts to test (no entry = default, default = 5): 2
First sequence (1-5): 3
Second sequence (1-5): 2

Shifting first sequence by 0
Shifts          : 0
First Sequence  : TTTTGTCGAT
Second Sequence : TTTAGCCGAT
Score           : 4
-

```

```sh
Enter mode (0 = match, 1 = contiguous, default = match): 1
Enter max number of shifts to test (no entry = default, default = 5):
First sequence (1-5): 1
Second sequence (1-5): 2

Shifting first sequence by 4
Shifts          : 4
First Sequence  : ----ACTGACTTTT
Second Sequence : TTTAGCCGAT----
Score           : 2
-

```
