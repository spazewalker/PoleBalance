# PoleBalance

AI tries to balance a pole on a cart. This project was a procrastinating method when author had quizzes to prepare for but didn't feel like doing so XD. A neural Network is trining to balance a pole which is started from a random angle by moving the cart left or right(with acc of 2g).

<img src="Screenshot from 2021-04-05 21-29-53.png" width=50%><img src="Screenshot from 2021-04-05 21-29-54.png" width=50%>

## Dependencies
* Numpy
* pygame

## Usage
clone this repo. -> Fire up your terminal -> cd into the cloned folder -> run `python3 combined.py`
If for some reason, you want to play it yourself then run `python3 -m game.py`

## Details
The project contains two parts, an environment/game and a Neural Network. The script `combined.py` controls both game and network training.

### Environment
The environment consists of a cart having a pole hinged at it's center placed on a surface. The game is governed by the simple physics. Actions possible by the player is `Move Left` and `Move Right`. Whenever a user requests to move left or right an appropriate acceleration of 2g is applid on the cart. Score is given by the number of seconds for which the pole was balanced i.e. time required by the pole to touch the cart.

### Neural Network
The ANN used here was implemented from scratch using numpy and was not specifically written for a RL implementation and is not perfect (I'm aware of that and didn't want to put a lot of time in writing it). It uses Stocastic Gradient Descent and the error used to backpropogate is tanh of the angle. The maximum score i could get while training it was 19. Not bad if you ask me.

<strong>Note: I don't have much knowledge of reinforced learning, as of writing this. Whatever implemented here is from my understanding of reinforcements (from UG Psychology course) and ANNs. Hence, this is not a proper Reinforcement Learning Model. Also, I'm aware that the loss function i used is not very effective. I should've implemented a way to retain previous steps in memory and take decision based on them. But implementing them in plain numpy is not easy, hence i stuck to a basic ANN</strong>
