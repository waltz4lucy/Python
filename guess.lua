guessesTaken = 0
math.randomseed(os.time())
number = math.random(1, 20)

print(number)
print('Well, I am thinking of a number between 1 and 20.')

while guessesTaken < 6 do
print('Take a guess.')
guess = tonumber(io.read())
guessesTaken = guessesTaken + 1

  if guess < number then
    print('Your guess is too low.')
  elseif guess > number then
    print('Your guess is too high.')
  elseif guess == number then
    print('Good job, You guessed my number in ' .. guessesTaken .. ' guesses!')
    break
  end
end

while guessesTaken == 6 do
  print('Nope. The number I was thinking of was ' .. number)
  break
end
