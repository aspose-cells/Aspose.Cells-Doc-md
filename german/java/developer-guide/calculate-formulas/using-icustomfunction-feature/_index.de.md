---
title: Verwenden der ICustomFunction-Funktion
type: docs
weight: 890
url: /de/java/using-icustomfunction-feature/
---
{{% alert color="primary" %}} 

Dieser Artikel bietet detaillierte Informationen zur Verwendung der ICustomFunction-Funktion zum Implementieren benutzerdefinierter Funktionen mit Aspose.Cells-APIs.

Die ICustomFunction-Schnittstelle ermöglicht das Hinzufügen benutzerdefinierter Formelberechnungsfunktionen zur Erweiterung der Aspose.Cells'-Kernberechnungs-Engine, um bestimmte Anforderungen zu erfüllen. Diese Funktion ist nützlich, um benutzerdefinierte (benutzerdefinierte) Funktionen in einer Vorlagendatei oder in Code zu definieren, wobei die benutzerdefinierte Funktion mithilfe von Aspose.Cells-APIs wie jede andere Standard-Excel-Funktion Microsoft implementiert und ausgewertet werden kann.

 Bitte beachten Sie, dass diese Schnittstelle durch ersetzt wurde[AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) und wird in Zukunft entfernt. Einige Fachartikel/Beispiele zur neuen API:[Hier](/cells/de/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/) Und[Hier](/cells/de/java/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}} {{% alert color="primary" %}} 

 Wenn Sie mit den APIs Aspose.Cells for Java noch nicht vertraut sind, überprüfen Sie dies bitte[Das](https://docs.aspose.com/cells/java/installation/) In diesem Artikel erfahren Sie, wie Sie die Aspose.Cells for Java in Ihrem Projekt erwerben und referenzieren können.

{{% /alert %}} 
##  **Erstellen und Auswerten einer benutzerdefinierten Funktion**
 Dieser Artikel demonstriert die Implementierung der ICustomFunction-Schnittstelle zum Schreiben einer benutzerdefinierten Funktion und deren Verwendung in der Tabelle, um die Ergebnisse zu erhalten. Wir werden eine benutzerdefinierte Funktion nach Namen definieren**MyFunc** welches 2 Parameter mit folgenden Details akzeptiert.

- Der 1. Parameter bezieht sich auf eine einzelne Zelle
- Der 2. Parameter bezieht sich auf einen Zellbereich

Die benutzerdefinierte Funktion addiert alle Werte aus dem als 2. Parameter angegebenen Zellbereich und dividiert das Ergebnis durch den Wert im 1. Parameter.

So haben wir die Methode „calculeCustomFunction“ implementiert.

**Java**

{{< highlight "csharp" >}}

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

Hier erfahren Sie, wie Sie die neu definierte Funktion in einer Tabellenkalkulation verwenden

**Java**

{{< highlight "csharp" >}}

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
##  **Überblick**
Die Aspose.Cells-APIs fügen das ReferredArea-Objekt einfach in die „paramsList“ ein, wenn der entsprechende Parameter eine Referenz oder sein berechnetes Ergebnis eine Referenz ist. Wenn Sie die Referenz selbst benötigen, können Sie die ReferredArea direkt verwenden. Wenn Sie den Wert einer einzelnen Zelle aus der Referenz abrufen müssen, die der Position der Formel entspricht, können Sie die Methode ReferredArea.getValue(rowOffset, int colOffset) verwenden. Wenn Sie ein Array mit Zellenwerten für den gesamten Bereich benötigen, können Sie die Methode „ReferredArea.getValues“ verwenden.

Da die Aspose.Cells-APIs die ReferredArea in „paramsList“ angeben, wird die ReferredAreaCollection in „contextObjects“ nicht mehr benötigt (in alten Versionen war es nicht immer möglich, den Parametern der benutzerdefinierten Funktion eine Eins-zu-eins-Zuordnung zu geben), daher ist dies der Fall wurde aus den „contextObjects“ entfernt.

{{< highlight "java" >}}

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
