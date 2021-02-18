CC = clang++
STD = -std=c++14
CFLAGS = -Wall -Wextra -Wfloat-equal -O2

SOURCE = PdfDir
MAIN = buildContent

run:
	$(CC) $(MAIN).cpp $(SOURCE).cpp $(STD) $(CFLAGS) -o $(MAIN)
	./$(MAIN) test