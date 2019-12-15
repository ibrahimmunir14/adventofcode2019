-- puzzle input: 165432 707912
-- solution:     countPasswords 165432 707912

countPasswords :: Int -> Int -> Int
countPasswords min max
  = length (filter validPassword [min..max])

validPassword :: Int -> Bool
validPassword x
  = nonDecreasing lx && twoSameAdjacents' lx
  where
    lx = toList x

-- Convert an integer into a list of its digits in base 10
toList :: Int -> [Int]
toList x
  | quo == 0  = [rem]
  | otherwise = (toList quo) ++ [rem]
  where
    quo = x `div` 10
    rem = x `mod` 10

-- Check if a list contains non-decreasing terms only
nonDecreasing :: [Int] -> Bool
nonDecreasing []            = True
nonDecreasing [x]           = True
nonDecreasing (x : y : xs)  = x <= y && nonDecreasing (y : xs)

-- Check if a list contains at least two adjacent matching terms
twoSameAdjacents :: [Int] -> Bool
twoSameAdjacents []             = False
twoSameAdjacents [x]            = False
twoSameAdjacents (x : y : xs)   = x == y || twoSameAdjacents (y : xs)

-- Check if a list contains exactly two adjacents matching terms
  -- not part of a larger group of matching terms
twoSameAdjacents' :: [Int] -> Bool
twoSameAdjacents' []      = False
twoSameAdjacents' [x]     = False
twoSameAdjacents' [x, y]  = x == y
twoSameAdjacents' (x : y : z : xs) 
  | x == y && y == z  = twoSameAdjacents' (dropWhile (==x) xs)
  | x == y            = True
  | otherwise         = twoSameAdjacents' (y : z : xs)