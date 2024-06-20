---
title: Använda funktionen ICustomFunction
description: Denna artikel beskriver hur man skapar en anpassad funktion i Microsoft Excel med hjälp av ICustomFunction funktionen i Aspose.Cells biblioteket. Genom att ladda en befintlig Excel fil eller skapa en ny Excel fil kan vi använda de metoder som tillhandahålls av Aspose.Cells för att definiera och registrera anpassade funktioner och få resultaten. Till slut sparar vi den modifierade Excel filen på disk.
keywords: Aspose.Cells, Excel, ICustomFunction funktioner, anpassade funktioner
type: docs
weight: 30
url: /sv/net/using-icustomfunction-feature/
---

{{% alert color="primary" %}} 

Den här artikeln ger en detaljerad förståelse för hur man använder ICustomFunction-funktionen för att implementera anpassade funktioner med Aspose.Cells API:er.

ICustomFunction-gränssnittet tillåter att lägga till anpassade formelberäkningsfunktioner för att utöka Aspose.Cells kärnberäkningsmotor för att uppfylla vissa krav. Denna funktion är användbar för att definiera anpassade (användardefinierade) funktioner i en mallfil eller i kod där den anpassade funktionen kan implementeras och utvärderas med Aspose.Cells API:er som vilken annan standardfunktion som helst i Microsoft Excel.

Observera att detta gränssnitt har ersatts av [AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/) och kommer att tas bort i framtiden. Några tekniska artiklar/exempel om den nya API:en: [här](/cells/sv/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/) och [här](/cells/sv/net/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}} 
## **Skapa och utvärdera en användardefinierad funktion**
Den här artikeln demonstrerar implementeringen av ICustomFunction-gränssnittet för att skriva en anpassad funktion och använda den i kalkylarket för att få resultaten. Vi kommer att definiera en anpassad funktion vid namn **MyFunc** som kommer att acceptera 2 parametrar med följande detaljer.

- Första parametern hänvisar till en enda cell
- Andra parametern hänvisar till en rad av celler

Den anpassade funktionen kommer att lägga till alla värden från cellområdet som anges som 2: a parameter och dela resultatet med värdet i den första parametern.

Här är hur vi har implementerat metoden CalculateCustomFunction.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-ICustomFunction.cs" >}}


Här är hur du använder den nyligen definierade funktionen i ett kalkylblad



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-UsingICustomFunctionFeature.cs" >}}
## **Översikt**
Aspose.Cells-API:erna sätter helt enkelt in ReferredArea-objektet i "paramsList" när det motsvarande parametern är en referens eller dess beräknade resultat är en referens. Om du behöver referensen själv kan du använda ReferredArea direkt. Om du behöver få värdet av en enskild cell från referensen som motsvarar formelns position kan du använda ReferredArea.GetValue(rowOffset, int colOffset) metoden. Om du behöver en array av cellvärden för hela området kan du använda ReferredArea.GetValues-metoden.

Eftersom Aspose.Cells API: er ger ReferredArea i "paramsList", kommer ReferredAreaCollection i "contextObjects" inte längre att behövas (i äldre versioner kunde den inte ge en-ett-karts till anpassade funktioners parametrar alltid) därför har den tagits bort från "contextObjects".

{{< highlight java >}}

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
