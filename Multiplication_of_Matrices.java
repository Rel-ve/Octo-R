import java.util.Scanner;
class Size_And_Compatibility {
    public int[] size_of_matrices(int a) {
        Scanner scan = new Scanner(System.in);
        System.out.printf("Enter how many rows in %d matrix: ", a);
        int x = scan.nextInt();
        System.out.printf("Enter how many columns in %d matrix: ", a);
        int y = scan.nextInt();
        int[] Arr = {x, y};
        return Arr;
    }
    public void print_matrix(int[][] arr){
        for (int k = 0; arr.length>k;k++) {
            for (int l = 0; arr[0].length > l; l++) {
                System.out.print(arr[k][l] + " ");
            }
            System.out.println(" ");
        }
    }
    public boolean condition(int arr[][], int i) {
        if (arr[0].length == i) {
            return true;
        } else {
            return false;
        }
    }

    public int sum(int arr[][], int arr_1[][], int i, int j) {
        int sum = 0;
        for (int z = 0; arr.length > z; z++) {
//            System.out.println(arr[j][z]); => row
//            System.out.println(arr_1[z][j]); => column
            sum = sum + (arr[j][z] * arr_1[z][j]);
        }
        return sum;
    }

    public int[][] multiply_Matrices(int arr[][], int arr_1[][]) {
        int[][] Array = new int[arr.length][arr_1[0].length];
        for (int i = 0; Array.length > i; i++) {
            for (int j = 0; Array[0].length > j; j++) {
                Array[i][j] = sum(arr, arr_1, i, j);
            }

        }
        return Array;
    }

}
public class Multiplication_of_Matrices {

    static int[][] Matrix(int x,int y){
        Size_And_Compatibility Class_object = new Size_And_Compatibility();
        Scanner scan = new Scanner(System.in);
        System.out.printf("A %d x %d Matrix will be generated. Input the values corresponding to the matrix \n",x,y);
        int[][] z = new int[x][y];
        for(int i = 0;z.length>i;i++){
            for(int j=0;z[0].length>j;j++){
                System.out.printf("Input Value a[%d %d] \n",i+1,j+1);
                z[i][j] = scan.nextInt();
            }
        }
        Class_object.print_matrix(z);
        return z;
    }
    public static void main(String[] args) {
        int[][] product, Matrix_1, Matrix_2;
        int i = 0;
        int j = 0;
        Scanner scan = new Scanner(System.in);
        Size_And_Compatibility obj = new Size_And_Compatibility();

        System.out.println("Enter how many matrices are to be multiplied");
        int a = scan.nextInt();
        int[] Values = obj.size_of_matrices(1);
        Matrix_1 = Matrix(Values[0],Values[1]);

        for(int x = 1;a>x;x++) {
            Values = obj.size_of_matrices(x+1);
                i = Values[0];
                j = Values[1];
          
            boolean A = obj.condition(Matrix_1,i);
             if(!A){
                System.out.println("The matrices can't be multiplied, please try again");
                x--;
                continue;
            }
                Matrix_2 = Matrix(i, j);
                product = obj.multiply_Matrices(Matrix_1, Matrix_2);
                if(x>1){
                    product = obj.multiply_Matrices(product, Matrix_2);
                }
                if(x+1==a){
                    System.out.println("The required matrix is: ");
                    obj.print_matrix(product);
                }
        }
    }
}
