import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class RingMatrixToFile {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Введите высоту (m): ");
        int m = scanner.nextInt();

        System.out.print("Введите ширину (n): ");
        int n = scanner.nextInt();

        int[][] matrix = new int[m][n];

        int layers = Math.min(m, n) / 2 + Math.min(m, n) % 2;

        for (int layer = 0; layer < layers; layer++) {
            int value = layer + 1;

            for (int i = layer; i < m - layer; i++) {
                for (int j = layer; j < n - layer; j++) {
                    matrix[i][j] = value;
                }
            }
        }

        // Сохраняем в файл
        try (FileWriter writer = new FileWriter("output.txt")) {
            for (int[] row : matrix) {
                for (int num : row) {
                    writer.write(num + " ");
                }
                writer.write("\n");
            }
            System.out.println("Массив успешно записан в файл output.txt");
        } catch (IOException e) {
            System.out.println("Ошибка при записи в файл: " + e.getMessage());
        }

        scanner.close();
    }
}
