using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace bilioteca
{
    public class cajero
    {
        double saldo = 1000;

        public double consultar() 
        {
            return saldo;
        }

        public void depositar(double monto) 
        {
            while (true)
            {

                Console.Write("\nIngrese el monto a depositar: ");
                string en = Console.ReadLine();

            
                try
                {
                    monto = Convert.ToDouble(en);

                    if (monto > 0)
                    {
                        saldo += monto;
                        Console.WriteLine("deposito exitoso.");
                    }
                    else 
                    {
                        Console.WriteLine("Error. tiene que ser mayor a 0");
                        continue;
                    }
                        
                }
                catch (Exception)
                {
                    Console.WriteLine("Error. el deposito tiene que ser un monto valido.");
                    continue;
                }


            }        
        }


            public void retirar(double monto)
            {
                while (true)
                {

                    Console.Write("\nIngrese el monto a retirar: ");
                    string en = Console.ReadLine();


                    try
                    {
                        monto = Convert.ToDouble(en);

                    if (monto <= saldo)
                    {
                        saldo -= monto;
                        Console.WriteLine("retiro exitoso.");
                        break;
                    }
                    else if (monto < 0)
                    {
                        Console.WriteLine("Error. tiene que ser un retiro mayor a 0");
                        continue;
                    }

                    else 
                    {
                        Console.WriteLine("Error saldo insuficiente.");
                    }

                    }
                    catch (Exception)
                    {
                        Console.WriteLine("Error. el retiro tiene que ser un monto valido.");
                        continue;
                    }


                }
            }
        
    }
}

