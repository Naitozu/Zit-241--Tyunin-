public class BracketValidator {
    public static boolean isValid(String s) {
        int balance = 0;

        for (char ch : s.toCharArray()) {
            if (ch == '(') {
                balance++;
            } else if (ch == ')') {
                balance--;
                if (balance < 0) {
                    return false; // Закрывающая скобка раньше открывающей
                }
            }
        }

        return balance == 0; // Все открытые скобки закрыты
    }

    public static void main(String[] args) {
        System.out.println(isValid("()"));               // true
        System.out.println(isValid("(()()((())))"));     // true
        System.out.println(isValid("(((()))"));          // false
        System.out.println(isValid(")("));               // false
        System.out.println(isValid("()(()))(()"));       // false
    }
}
