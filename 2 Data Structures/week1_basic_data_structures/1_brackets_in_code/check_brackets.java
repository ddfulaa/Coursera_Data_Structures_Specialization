import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Stack;

class Bracket {
    Bracket(char type, int position) {
        this.type = type;
        this.position = position;
    }

    boolean Match(char c) {
        if (this.type == '[' && c == ']')
            return true;
        if (this.type == '{' && c == '}')
            return true;
        if (this.type == '(' && c == ')')
            return true;
        return false;
    }

    char type;
    int position;
}

class check_brackets {
    public static void main(String[] args) throws IOException {
        InputStreamReader input_stream = new InputStreamReader(System.in);
        BufferedReader reader = new BufferedReader(input_stream);
        String text = reader.readLine();
	String salida="Success";
        Stack<Bracket> opening_brackets_stack = new Stack<Bracket>();
        for (int position = 0; position < text.length(); ++position) {
            char next = text.charAt(position);
            Bracket siguiente= new Bracket(next,position);
            if (next == '(' || next == '[' || next == '{') {
                // Process opening bracket, write your code here
                opening_brackets_stack.push(siguiente);
            }

            if (next == ')' || next == ']' || next == '}') {
                // Process closing bracket, write your code here
		if (opening_brackets_stack.empty()){
                    salida=Integer.toString(position+1);
                    break;
		}else{
                    Bracket topStack = opening_brackets_stack.pop();
                    if (!topStack.Match(next)){
                        salida=Integer.toString(position+1);
                        break;
                    }
                }
            }
        }

        // Printing answer, write your code here
        if (!opening_brackets_stack.empty() && salida.equals("Success")){
            salida=Integer.toString(opening_brackets_stack.pop().position+1);
        }
        System.out.println(salida);
    }
}
