---
title: Utilizzo della funzione ICustomFunction
type: docs
weight: 890
url: /it/java/how-to-calculate-custom-fuctions/
description: Questo articolo descrive come creare una funzione personalizzata in Microsoft Excel utilizzando la funzionalità ICustomFunction nella libreria Aspose.Cells. Caricando un file Excel esistente o creandone uno nuovo, possiamo utilizzare i metodi forniti da Aspose.Cells per definire e registrare funzioni personalizzate e ottenere i risultati. Infine, salviamo il file Excel modificato su disco.
keywords: Aspose.Cells, Excel, funzionalità ICustomFunction, funzioni personalizzate, come calcolare funzioni personalizzate.
---

{{% alert color="primary" %}} 

Questo articolo fornisce una comprensione dettagliata di come utilizzare la funzione ICustomFunction per implementare funzioni personalizzate con le API di Aspose.Cells.

L'interfaccia ICustomFunction consente di aggiungere funzioni di calcolo delle formule personalizzate per estendere il motore di calcolo centrale di Aspose.Cells al fine di soddisfare determinati requisiti. Questa funzione è utile per definire funzioni personalizzate (definite dall'utente) in un file di modello o nel codice, dove la funzione personalizzata può essere implementata e valutata utilizzando le API di Aspose.Cells come qualsiasi altra funzione predefinita di Microsoft Excel.

Si prega di notare che questa interfaccia è stata sostituita da [AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) e verrà rimossa in futuro. Alcuni articoli/esempi tecnici sulla nuova API: [qui](/cells/it/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/) e [qui](/cells/it/java/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}} {{% alert color="primary" %}} 

Se sei nuovo alle API Aspose.Cells for Java, controlla [questo](https://docs.aspose.com/cells/java/installation/) articolo per sapere come puoi acquisire e fare riferimento alle Aspose.Cells for Java nel tuo progetto

{{% /alert %}} 
## **Creazione e valutazione di una funzione definita dall'utente**
Questo articolo illustra l'implementazione dell'interfaccia ICustomFunction per scrivere una funzione personalizzata e utilizzarla nel foglio di calcolo per ottenere i risultati. Definiremo una funzione personalizzata con il nome **MyFunc** che accetterà 2 parametri con i seguenti dettagli.

- Il primo parametro si riferisce a una singola cella
- Il secondo parametro si riferisce a un intervallo di celle

La funzione personalizzata sommerà tutti i valori dell'intervallo di celle specificato come secondo parametro e dividerà il risultato per il valore nel primo parametro.

Ecco come abbiamo implementato il metodo calculateCustomFunction

**Java**

{{< highlight csharp >}}

 public class CustomFunction implements ICustomFunction

{

    @Override

    public Object calculateCustomFunction(String functionName, java.util.ArrayList paramsList, java.util.ArrayList contextObjects)

    {

        double result = 0f;

        double sum = 0;

        //Get the value of 1st parameter

        Object firstParamB1 = paramsList.get(0);

        if (firstParamB1 instanceof ReferredArea)

        {

            ReferredArea ra = (ReferredArea)firstParamB1;

            firstParamB1 = ra.getValue(0, 0);

        }

        //Get values of 2nd parameter

        Object secondParamC1C5 = paramsList.get(1);

        if (secondParamC1C5 instanceof ReferredArea)

        {

            ReferredArea ra = (ReferredArea)secondParamC1C5;

            for (int i = ra.getStartRow(); i <= ra.getEndRow(); i++)

            {

                //Add all values

                sum += (double)ra.getValue(i, 0);

            }

        }

        result = sum / (double)firstParamB1;

        // Return result of the function

        return result;

    }

}

{{< /highlight >}}

Ecco come utilizzare la funzione appena definita in un foglio di calcolo

**Java**

{{< highlight csharp >}}

 //Open the workbook

Workbook workbook = new Workbook();

//Obtaining the reference of the first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Adding a sample value to "A1" cell

worksheet.getCells().get("B1").putValue(5);

//Adding a sample value to "A2" cell

worksheet.getCells().get("C1").putValue(100);

//Adding a sample value to "A3" cell

worksheet.getCells().get("C2").putValue(150);

//Adding a sample value to "B1" cell

worksheet.getCells().get("C3").putValue(60);

//Adding a sample value to "B2" cell

worksheet.getCells().get("C4").putValue(32);

//Adding a sample value to "B2" cell

worksheet.getCells().get("C5").putValue(62);

//Adding custom formula to Cell A1

worksheet.getCells().get("A1").setFormula("=MyFunc(B1,C1:C5)");

//Calcualating Formulas

workbook.calculateFormula(false, new CustomFunction());

//Assign resultant value to Cell A1

worksheet.getCells().get("A1").putValue(worksheet.getCells().get("A1").getValue());

//Save the file

workbook.save(dir + "UsingICustomFunction.xls");

{{< /highlight >}}
## **Panoramica**
Le API di Aspose.Cells inseriscono semplicemente l'oggetto ReferredArea nel "paramsList" quando il parametro corrispondente è un riferimento o il suo risultato calcolato è un riferimento. Se hai bisogno del riferimento stesso, puoi utilizzare direttamente ReferredArea. Se hai bisogno di ottenere il valore di una singola cella dal riferimento corrispondente alla posizione della formula, puoi utilizzare il metodo ReferredArea.getValue(rowOffset, colOffset). Se hai bisogno dell'array dei valori delle celle per l'intera area, puoi utilizzare il metodo ReferredArea.getValues

Poiché le API di Aspose.Cells restituiscono ReferredArea in "paramsList", la ReferredAreaCollection in "contextObjects" non sarà più necessaria (nelle vecchie versioni non era sempre in grado di dare una mappatura uno a uno ai parametri della funzione personalizzata) pertanto è stata rimossa da "contextObjects".

{{< highlight java >}}

 public Object calculateCustomFunction(String functionName, ArrayList paramsList, ArrayList contextObjects)

{

    ...

    Object o = paramsList.get(i);

    if(o is ReferredArea) //fetch data from reference

    {

        ReferredArea ra = (ReferredArea)o;

        if(ra.isArea())

        {

            o = ra.getValues();

        }

        else

        {

            o = ra.getValue(0, 0);

        }

    }

    if (o is Array)

    {

        ...

    }

    else if...

    ...

}

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
