---
title: Formatera kalkylblad Cells i en arbetsbok
type: docs
weight: 2000
url: /sv/net/format-worksheet-cells-in-a-workbook/
---
{{% alert color="primary" %}}

Den här artikeln visar hur du:

1. Använd stilar för att snabbt formatera data.
1. Formatera celler i rader och kolumner.
1. Använd kanter och färger för att framhäva data.
1. Använd talformat för att betona data.
1. Använd teckensnitt och attribut för att markera data.
1. Formatera data i ett namngivet intervall.
1. Ändra datajustering och orientering.
1. Ställ in radhöjd och kolumnbredd.

 Exempelprojektet utför alla dessa uppgifter och ger utvecklare en detaljerad beskrivning av hur man skapar en arbetsbok, lägger till data i och tillämpar formatering med[Aspose.Cells](https://products.aspose.com/cells/net/).

{{% /alert %}}

## **Dataformatering**

Formatering används för att skilja mellan olika typer av information och för att visa data tydligt.

Ett format representerar en stil och definieras som en uppsättning egenskaper, såsom teckensnitt och teckenstorlekar, talformat, cellkanter, cellskuggning, indrag, justering och textorientering. Gränser ger ytterligare sätt att lyfta fram information. En kantlinje är en linje som ritas runt en cell eller en grupp av celler.

Talformat gör också data mer meningsfulla. Genom att använda olika sifferformat kan du ändra utseendet på siffror utan att ändra numret bakom utseendet.

Aspose.Cells ger dig möjlighet att enkelt rita gränser runt celler och intervall. Det låter dig också tillämpa teckensnitt och skugga celler. Komponenten är tillräckligt effektiv för att du kan formatera en hel rad eller kolumn, ställa in justeringar, radbryta och rotera text i celler. Aspose.Cells stöder vidare alla talformat som stöds av Microsoft Excel.

Den här artikeln visar hur du skapar en konsolapplikation i Visual Studio.Net som genererar en årlig försäljningsrapport. Arbetsboken skapas från grunden, sedan infogas data och kalkylbladet formateras. Vi visar hur man skapar en enkel konsolapplikation som skapar en Excel-arbetsbok (du kan också använda en mallfil), infogar försäljningsdata i det första kalkylbladet, formaterar data och sparar en Excel-fil.

### **Bearbeta**

Nedan följer stegen för hur man skapar ett kalkylblad och formaterar olika celler i olika rader och kolumner i ett kalkylblad.

1. Ladda ner och installera Aspose.Cells:
   1. [Ladda ner](https://downloads.aspose.com/cells/net) Aspose.Cells for .NET.
 1. Installera det på din utvecklingsdator.
1. Skapa ett projekt och lägg till referenser:
 1. Starta Visual Studio.Net.
 1. Skapa en ny konsolapplikation.
 1. Lägg till en referens till Aspose.Cells, till exempel …\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. Lägg till följande kod till projektet:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FormatWorksheetCells-1.cs" >}}
