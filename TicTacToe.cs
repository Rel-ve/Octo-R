using System;
using System.Globalization;

namespace TicTacToe{
    class Logic
    {
        public static string[,] Board;
        public static string User;
        public static bool IsUserTypeComputer, HasUserWon;
        private static bool CheckDiagonal, CheckInverseDiagonal, CheckRow, CheckColumn, IsSpotOccupied ;
        public Logic(string[,] arr, int User)
        {
            Board = arr;
            if (User == 0)
            {
                IsUserTypeComputer = true;
            }
            else
            {
                IsUserTypeComputer = false;
            }
            for(int i = 0;  i < arr.GetLength(0); i++)
            {
                for(int j = 0;j<arr.GetLength(1); j++)
                {
                    Board[i, j] = "_";
                }
            }
            //  LogicBoard = BoardImplementation.Board.Clone() as string[,];
        }
        private bool IsOccupied(int x, int y)
        {
            if (Board[x,y] == "X" || Board[x,y] == "O")
            {
                IsSpotOccupied = true;
            }
            else
            {
                IsSpotOccupied = false;
            }
                return IsSpotOccupied;
        }
        public string[,] UserInput(int UserTurn)
        {
            int x, y;
            if (!(UserTurn % 2 == 0))
            {
                 User = "X";
            }
            else
            {
                 User = "O";
            }
            Console.WriteLine($"Input both the column and row for where {User} is placed");
            while (true)
            {
            Console.Write($"Input which row: ");
            
            x = Convert.ToInt32( Console.ReadLine() ) - 1; 
            Console.Write($"Input which column: ");
            y = Convert.ToInt32( Console.ReadLine() ) - 1;
                try
                {
                if (IsOccupied(x, y))
                {
                    Console.WriteLine("Please choose an appropiate option");
                    continue;
                }
                    Board[x, y] = User;
                    break;
                }
                catch (Exception e) {
                    Console.WriteLine(e.Message);
                }
                 Console.WriteLine("Input the value again");
            }

            return Board;
        }
        public static bool Linear()
        {
            for(int n = 0; n < Board.GetLength(0); n++)
            {
                if (Board[0,n] == Board[1,n] && Board[0, n] == Board[2, n])
                {
                    if (Board[0,n] == "X" || Board[0,n] == "O")
                    {
                        CheckRow = true;
                    }
                }
                if (Board[n, 0] == Board[n, 1] && Board[n, 0] == Board[n, 2])
                {
                    if (Board[n, 0] == "X" || Board[n, 0] == "O")
                    {
                        CheckColumn = true;
                    }
                }
            }
            return CheckColumn || CheckRow;
        }
        public static bool Diagonal()
        {
             if ((Board[0, 0] == "X" || Board[0, 0] == "O"))
             {
                 CheckDiagonal = (Board[0, 0] == Board[1, 1]) && (Board[0, 0] == Board[2, 2]);  
              }if((Board[0, 2] == "X" || Board[0, 2] == "O"))
             {
                 CheckInverseDiagonal = (Board[0, 2] == Board[1, 1]) && (Board[0, 2] == Board[2, 0]);
             }
            return CheckInverseDiagonal || CheckDiagonal;

        }
        public static (bool UserStatus, string User) CheckIfUserWin()
        {
            for (int i = 0; Board.GetLength(0) > i; i++) {
                if (Linear()||Diagonal())
                {
                    HasUserWon = true;
                    break;
                }else if (i == 2)
                {
                    HasUserWon = false;
                }

            }
            return (HasUserWon, User);
        }
    }
    class ComputerUser
    {
        public static bool IsComputerUser;
        public ComputerUser()
        {
            IsComputerUser = Logic.IsUserTypeComputer;
        }
        public void ComputerTurn(int UserVal)
        {
            if(UserVal == 0)
            {

            }
        }
    }
    class BoardImplementation
    {
        public static string[,] BoardPrint;
        public BoardImplementation() {
            BoardPrint = Logic.Board;
        }
        public void PrintBoard()
        {
            for(int i = 0; i < BoardPrint.GetLength(0); i++)
            {
                Console.WriteLine("\n");
                for(int j = 0; j < BoardPrint.GetLength(1); j++) {
                Console.Write($" | {BoardPrint[i,j]} | ");
                }
                Console.WriteLine("\n");
            }
        }
    }
    
    class Visible_Board
    {
        static void Main(String[] args)
        {
            string[,] board = new string[3,3];

            Console.WriteLine("Welcome to TicTacToe. You can either choose to play with the Computer, or play with another person");
            Console.Write("Input with whom do you wanna play(0 for computer, 1 for Person): ");
            int InputOfUser = Convert.ToInt32(Console.ReadLine());
            
            if(!(InputOfUser == 1 || InputOfUser ==0))
            {
                throw new IndexOutOfRangeException("Not a correct value");
            }
            Logic obj = new Logic(board, InputOfUser);
            BoardImplementation obj2 = new BoardImplementation();
            ComputerUser obj3 = new ComputerUser();
            obj2.PrintBoard();
            Console.WriteLine("To play the game, you have to state which row and which column should your player should go to");
            
            for(int i = 1; i <= 9; i++)
            {
                if (Logic.IsUserTypeComputer && i==1)
                {
                    Console.WriteLine("What user do you want to play?");
                    Console.WriteLine("0 for X, 1 for O");
                    try
                    {
                    int UserType = Convert.ToInt32(Console.ReadLine());

                    }
                    catch
                    {
                        i--;
                    }
                }
                else if(Logic.IsUserTypeComputer){

                }
                else{
                obj.UserInput(i);
                obj2.PrintBoard();
                }

                if (Logic.CheckIfUserWin().UserStatus)
                {
                    Console.WriteLine($"{Logic.CheckIfUserWin().User} has won");
                    break;
                }
            }
        }
    }
}
