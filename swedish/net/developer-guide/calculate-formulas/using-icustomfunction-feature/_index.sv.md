---
title: Använder ICustomFunction-funktionen
type: docs
weight: 30
url: /sv/net/using-icustomfunction-feature/
---
{{% alert color="primary" %}} 

Den här artikeln ger en detaljerad förståelse för hur du använder ICustomFunction-funktionen för att implementera anpassade funktioner med Aspose.Cells API:er.

ICustomFunction-gränssnittet gör det möjligt att lägga till anpassade formelberäkningsfunktioner för att utöka Aspose.Cells' kärnberäkningsmotor för att uppfylla vissa krav. Den här funktionen är användbar för att definiera anpassade (användardefinierade) funktioner i en mallfil eller i kod där den anpassade funktionen kan implementeras och utvärderas med Aspose.Cells API:er som alla andra standardfunktioner i Microsoft Excel.

{{% /alert %}} 
## **Skapa och utvärdera en användardefinierad funktion**
Den här artikeln visar implementeringen av ICustomFunction-gränssnittet för att skriva en anpassad funktion och använda den i kalkylarket för att få resultaten. Vi kommer att definiera en anpassad funktion efter namn**MyFunc** som accepterar 2 parametrar med följande detaljer.

- Den första parametern hänvisar till en enskild cell
- Den andra parametern hänvisar till ett cellintervall

Den anpassade funktionen kommer att lägga till alla värden från cellområdet som anges som 2:a parametern och dividera resultatet med värdet i den 1:a parametern.

Så här har vi implementerat CalculateCustomFunction-metoden.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-ICustomFunction.cs" >}}


Så här använder du den nydefinierade funktionen i ett kalkylblad



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-UsingICustomFunctionFeature.cs" >}}
## **Översikt**
Aspose.Cells API:erna placerar bara ReferredArea-objektet i "paramsList" när motsvarande parameter är en referens eller dess beräknade resultat är referens. Om du behöver själva referensen kan du använda ReferredArea direkt. Om du behöver få värdet på en enskild cell från referensen som motsvarar formelns position, kan du använda metoden ReferredArea.GetValue(rowOffset, int colOffset). Om du behöver en cellvärdesarray för hela området kan du använda metoden ReferredArea.GetValues.

Eftersom Aspose.Cells API:erna ger ReferredArea i "paramsList", kommer ReferredAreaCollection i "contextObjects" inte att behövas längre (i gamla versioner kunde den inte alltid ge en-till-en-karta till parametrarna för den anpassade funktionen) därför har tagits bort från "contextObjects".

{{< highlight "java" >}}

 public object CalculateCustomFunction(string functionName, ArrayList paramsList, ArrayList contextObjects)

{

    ...

    object o = paramsList[i];

    if(o is ReferredArea) //fetch data from reference

    {

        ReferredArea ra = (ReferredArea)o;

        if(ra.IsArea)

        {

            o = ra.GetValues();

        }

        else

        {

            o = ra.GetValue(0, 0);

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
