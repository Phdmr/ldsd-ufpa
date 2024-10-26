import java.rmi.Remote;
import java.rmi.RemoteException;

// A interface 'Calculator' estende 'Remote', que indica que seus métodos podem ser chamados remotamente.
public interface Calculator extends Remote {

    // Declaração de métodos que poderão ser invocados remotamente. Eles devem lançar 'RemoteException'.
    public int soma(int a, int b) throws RemoteException;

    public int subtrai(int a, int b) throws RemoteException;
}
