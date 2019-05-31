#include <stdio.h>
#include <stdlib.h>
#include "malloc.h"
#include <string.h>
#include "tictactoe.h"

void main()
{

  struct game *statepointer = malloc(sizeof(struct game));
  struct game state = *statepointer;

  int i;
  for (i = 0; i < 9; i++) {
	state.board[i] = ' ';
  }
  state.board[9] = '\0';
  state.player = 'x';

  gameloop(&state);

}
