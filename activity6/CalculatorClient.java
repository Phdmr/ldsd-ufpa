import java.rmi.Naming;
import java.util.Scanner;

public class CalculatorClient {
    public static void main(String[] args) {
        try {
            Scanner scanner = new Scanner(System.in);

            // Solicita ao usuário que digite o endereço IP do servidor
            System.out.print("Digite o endereço IP do servidor: ");
            String serverIp = scanner.nextLine();
            
            // Obtém a referência ao objeto remoto registrado no RMI Registry
            Calculator calc = (Calculator) Naming.lookup("rmi://" + serverIp + "/CalculadoraService");
            
            // Solicita ao usuário que escolha a operação
            System.out.println("Escolha a operação (1: soma, 2: subtração): ");
            int operacao = scanner.nextInt();

            // Solicita ao usuário que digite os números
            System.out.print("Digite o primeiro número: ");
            int num1 = scanner.nextInt();
            System.out.print("Digite o segundo número: ");
            int num2 = scanner.nextInt();
            
            // Executa a operação escolhida
            int resultado = 0;
            switch (operacao) {
                case 1:
                    resultado = calc.soma(num1, num2);
                    System.out.println("Resultado da soma: " + resultado);
                    break;
                case 2:
                    resultado = calc.subtrai(num1, num2);
                    System.out.println("Resultado da subtração: " + resultado);
                    break;
                default:
                    System.out.println("Operação inválida.");
            }

        } catch (Exception e) {
            System.out.println("Erro no cliente: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
