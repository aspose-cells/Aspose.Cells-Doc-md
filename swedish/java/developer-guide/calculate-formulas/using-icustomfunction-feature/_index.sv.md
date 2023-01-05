---
title: Använder ICustomFunction-funktionen
type: docs
weight: 890
url: /sv/java/using-icustomfunction-feature/
---
{{% alert color="primary" %}} 

Den här artikeln ger en detaljerad förståelse för hur du använder ICustomFunction-funktionen för att implementera anpassade funktioner med Aspose.Cells API:er.

ICustomFunction-gränssnittet gör det möjligt att lägga till anpassade formelberäkningsfunktioner för att utöka Aspose.Cells' kärnberäkningsmotor för att uppfylla vissa krav. Den här funktionen är användbar för att definiera anpassade (användardefinierade) funktioner i en mallfil eller i kod där den anpassade funktionen kan implementeras och utvärderas med Aspose.Cells API:er som vilken annan standard Microsoft Excel-funktion som helst.

 Observera att detta gränssnitt har ersatts av[AbstractCalculation Engine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) och kommer att tas bort i framtiden. Några tekniska artiklar/exempel om den nya API:[här](/cells/sv/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/) och[här](/cells/sv/java/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}} {{% alert color="primary" %}} 

 Om du är ny med Aspose.Cells for Java API:er, kontrollera[detta](https://docs.aspose.com/cells/java/installation/) artikel för att veta hur du kan förvärva och referera till Aspose.Cells for Java i ditt projekt.

{{% /alert %}} 
## **Skapa och utvärdera en användardefinierad funktion**
Den här artikeln visar implementeringen av ICustomFunction-gränssnittet för att skriva en anpassad funktion och använda den i kalkylarket för att få resultaten. Vi kommer att definiera en anpassad funktion efter namn**MyFunc** som accepterar 2 parametrar med följande detaljer.

- Den första parametern hänvisar till en enskild cell
- Den andra parametern hänvisar till ett cellintervall

Den anpassade funktionen kommer att lägga till alla värden från cellområdet som anges som 2:a parametern och dividera resultatet med värdet i den 1:a parametern.

Så här har vi implementerat calculateCustomFunction-metoden.

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

Så här använder du den nydefinierade funktionen i ett kalkylblad

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
## **Översikt**
Aspose.Cells API:erna placerar bara ReferredArea-objektet i "paramsList" när motsvarande parameter är en referens eller dess beräknade resultat är referens. Om du behöver själva referensen kan du använda ReferredArea direkt. Om du behöver få värdet på en enskild cell från referensen som motsvarar formelns position, kan du använda metoden ReferredArea.getValue(rowOffset, int colOffset). Om du behöver en cellvärdesarray för hela området kan du använda metoden ReferredArea.getValues.

Eftersom Aspose.Cells API:erna ger ReferredArea i "paramsList", kommer ReferredAreaCollection i "contextObjects" inte att behövas längre (i gamla versioner kunde den inte alltid ge en-till-en-karta till parametrarna för den anpassade funktionen) därför har tagits bort från "contextObjects".

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
