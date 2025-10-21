using System;
using System.Collections.Generic;
using System.Configuration;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using bilioteca;

namespace semana10_C
{
    internal class Program
    {
        static void Main(string[] args)
        {
            cajero c = new cajero();
            int opc;
            string conti;


        do {
            Console.WriteLine("Bienvenido al sistema de cajero\n");
            Console.WriteLine("1. consultar saldo");
            Console.WriteLine("2. depositar dinero");
            Console.WriteLine("3. retirar dinero");
            Console.WriteLine("4. Salir\n");


            do
            {
                Console.Write("ingrese una opcion: ");
                opc = int.Parse(Console.ReadLine());
                if (opc < 0 | opc > 4)
                    Console.WriteLine("opcion no valida, ingrese nuevamente");
            } while (opc < 0 | opc > 4);

            switch (opc)
            {
                case 1: Console.WriteLine("saldo disponible: " + c.consultar()); break;
                case 2: c.depositar(0); break;
                case 3: c.retirar(0); break;
                case 4: break;
            }
           
            while (true)
            {
                Console.WriteLine("\n¿Deseas continuar? (s/n)");
                conti = Console.ReadLine();

                if (conti != "s" & conti != "n")
                {
                    Console.WriteLine("error solo se permite s o n.");
                }
                else break;
            }
            Console.Clear();
            }while(conti == "s");
        }
    }
}
