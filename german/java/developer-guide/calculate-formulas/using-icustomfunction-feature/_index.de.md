---
title: Verwendung der ICustomFunction Funktion
type: docs
weight: 890
url: /de/java/how-to-calculate-custom-fuctions/
description: Dieser Artikel beschreibt, wie man eine benutzerdefinierte Funktion in Microsoft Excel mithilfe des ICustomFunction Features in der Aspose.Cells Bibliothek erstellt. Durch Laden einer vorhandenen Excel Datei oder Erstellen einer neuen Excel Datei können wir die von Aspose.Cells bereitgestellten Methoden verwenden, um benutzerdefinierte Funktionen zu definieren und zu registrieren und die Ergebnisse zu erhalten. Schließlich speichern wir die modifizierte Excel Datei auf der Festplatte.
keywords: Aspose.Cells, Excel, ICustomFunction Funktionen, benutzerdefinierte Funktionen, wie man benutzerdefinierte Funktionen berechnet.
---

{{% alert color="primary" %}} 

Dieser Artikel bietet eine ausführliche Erklärung zur Verwendung des ICustomFunction-Features zur Implementierung benutzerdefinierter Funktionen mit Aspose.Cells-APIs.

Die ICustomFunction-Schnittstelle ermöglicht die Hinzufügung benutzerdefinierter Formelberechnungsfunktionen, um den Kernberechnungsmotor von Aspose.Cells zu erweitern, um bestimmte Anforderungen zu erfüllen. Diese Funktion ist nützlich, um benutzerdefinierte Funktionen in einer Vorlagendatei oder im Code zu definieren, wo die benutzerdefinierte Funktion mit Aspose.Cells-APIs wie jede andere Standard-Microsoft Excel-Funktion implementiert und ausgewertet werden kann.

Bitte beachten Sie, dass diese Schnittstelle durch [AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) ersetzt wurde und in Zukunft entfernt wird. Einige technische Artikel/Beispiele zur neuen API finden Sie [hier](/cells/de/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/) und [hier](/cells/de/java/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}} {{% alert color="primary" %}} 

Wenn Sie neu bei Aspose.Cells for Java-APIs sind, überprüfen Sie bitte [diesen](https://docs.aspose.com/cells/java/installation/) Artikel, um zu erfahren, wie Sie die Aspose.Cells for Java in Ihrem Projekt erwerben und referenzieren können.

{{% /alert %}} 
## **Erstellen und Auswerten einer benutzerdefinierten Funktion**
Dieser Artikel demonstriert die Implementierung der ICustomFunction-Schnittstelle, um eine benutzerdefinierte Funktion zu schreiben und sie in der Tabellenkalkulation zu verwenden, um die Ergebnisse zu erhalten. Wir definieren eine benutzerdefinierte Funktion namens **MyFunc**, die 2 Parameter mit folgenden Details akzeptiert.

- Der erste Parameter bezieht sich auf eine einzelne Zelle
- Der zweite Parameter bezieht sich auf einen Zellenbereich

Die benutzerdefinierte Funktion wird alle Werte aus dem als 2. Parameter angegebenen Zellbereich addieren und das Ergebnis durch den Wert im 1. Parameter dividieren.

So haben wir die Methode calculateCustomFunction implementiert.

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

So verwenden Sie die neu definierte Funktion in einer Tabellenkalkulation

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
## **Übersicht**
Die Aspose.Cells-APIs legen einfach das ReferredArea-Objekt in die "paramsList" ab, wenn der entsprechende Parameter eine Referenz ist oder sein berechnetes Ergebnis eine Referenz ist. Wenn Sie die Referenz selbst benötigen, können Sie direkt ReferredArea verwenden. Wenn Sie den Wert einer einzelnen Zelle aus der Referenz, die der Position der Formel entspricht, benötigen, können Sie die Methode ReferredArea.getValue(rowOffset, int colOffset) verwenden. Wenn Sie ein Zellwerte-Array für den gesamten Bereich benötigen, können Sie die Methode ReferredArea.getValues verwenden.

Da die Aspose.Cells-APIs die ReferredArea in "paramsList" erhalten, wird die ReferredAreaCollection in "contextObjects" nicht mehr benötigt (in älteren Versionen konnte sie nicht immer eine eins-zu-eins-Mapping zu den Parametern der benutzerdefinierten Funktion erstellen), daher wurde sie aus den "contextObjects" entfernt.

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
