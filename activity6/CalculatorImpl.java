import java.rmi.server.UnicastRemoteObject;
import java.rmi.RemoteException;

// 'CalculatorImpl' implementa a interface remota e estende 'UnicastRemoteObject' para suportar chamadas remotas.
public class CalculatorImpl extends UnicastRemoteObject implements Calculator {

    // Construtor que lança 'RemoteException' e chama o construtor da superclasse.
    public CalculatorImpl() throws RemoteException {
        super();  // Chama o construtor da classe 'UnicastRemoteObject'.
    }

    // Implementação do método remoto 'soma' que realiza a adição de dois números inteiros.
    public int soma(int a, int b) throws RemoteException {
        return a + b;
    }

    // Implementação do método remoto 'subtrai' que realiza a subtração de dois números inteiros.
    public int subtrai(int a, int b) throws RemoteException {
        return a - b;
    }
}
