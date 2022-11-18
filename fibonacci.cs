using System;

namespace Program
{
    class Program
    {
        static void Main(string[] args)
        {

            Console.Write("Enter how many times Fibonacci Series Pattern should loop: ");
            string a = Console.ReadLine();
            int b = Convert.ToInt32(a);
            while (b>=0) {
                int num = 0, x = 0, y = 0;
                for (int i = 0; i <= b; i++) {
                    if (i < 2) {
                        if (i == 0) {
                            Console.Write(num + " ");
                            num++;
                        }
                        else {
                            x = num;
                            Console.Write(num + " ");
                        }
                    }
                    else {
                        y = x;
                        x = num;
                        num = x + y;
                        Console.Write(num + " ");
                    }
                }
             Console.WriteLine();
             b--;
            }
        }
    }
}
