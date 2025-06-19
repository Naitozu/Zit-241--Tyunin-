import java.util.Scanner;

public class ClosestSquare {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Введите число: ");
            int N = scanner.nextInt();

            int M = (int) Math.round(Math.sqrt(N));

            System.out.println("Число, квадрат которого ближе всего к " + N + ": " + M);
            System.out.println("Квадрат этого числа: " + (M * M));
        }
    }
}
