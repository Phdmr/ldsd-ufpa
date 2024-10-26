import java.rmi.Naming;
import java.rmi.RemoteException;

// 'CalculatorServer' é a classe que cria e registra o serviço de calculadora no RMI Registry.
public class CalculatorServer {
    public static void main(String[] args) {
        try {
            // Cria uma instância da implementação da calculadora.
            Calculator calc = new CalculatorImpl();
            
            // Registra o objeto remoto com um nome específico no RMI Registry para que os clientes possam acessá-lo.
            Naming.rebind("rmi://localhost/CalculadoraService", calc);
            
            System.out.println("Serviço de Calculadora está rodando...");
        } catch (Exception e) {
            System.out.println("Erro no servidor: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
