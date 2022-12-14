---
title: Filtrera objekt när du laddar arbetsbok eller arbetsblad
type: docs
weight: 330
url: /sv/net/filter-objects-while-loading-workbook-or-worksheet/
---
## **Möjliga användningsscenarier**
Snälla använd[LoadOptions.LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)egenskap medan du filtrerar data från arbetsboken. Men om du vill filtrera data från enskilda kalkylblad måste du åsidosätta[LoadFilter.StartSheet](https://reference.aspose.com/cells/net/aspose.cells/loadfilter/methods/startsheet)metod. Vänligen ange lämpligt värde från[LoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)uppräkning medan du skapar eller arbetar med[LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter).

 De[LoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)uppräkning har följande möjliga värden.

- Allt
- Bokinställningar
- CellBlank
- CellBool
- CellData
- CellError
- CellNumeric
- CellString
- CellValue
- Diagram
- Villkorlig formatering
- Datavalidering
- Definerade namn
- Dokument egenskaper
- Formel
- Hyperlänkar
- MergedArea
- Pivottabell
- inställningar
- Form
- SheetData
- Bladinställningar
- Strukturera
- Stil
- Tabell
- VBA
- XmlMap
## **Filtrera objekt medan arbetsboken laddas**
 Följande exempelkod illustrerar hur du filtrerar diagram från arbetsboken. Vänligen kontrollera[exempel på excel-fil](5115258.xlsx) används i den här koden och[mata ut PDF](5115257.pdf)genereras av det. Som du kan se i PDF-filen har alla diagram filtrerats bort från arbetsboken.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-FilteringObjects.cs" >}}
## **Filtrera objekt medan kalkylblad laddas**
 Följande exempelkod laddar[source excel-fil](5115255.xlsx) och filtrerar följande data från sina kalkylblad med hjälp av ett anpassat filter.

- Det filtrerar diagram från kalkylblad som heter NoCharts.
- Det filtrerar former från kalkylblad som heter NoShapes.
- Det filtrerar villkorlig formatering från kalkylbladet som heter NoConditionalFormatting.

 En gång laddar den[source excel-fil](5115255.xlsx) med ett anpassat filter tar den bilderna av alla kalkylblad en efter en. Här är utdatabilderna för din referens. Som du kan se har den första bilden inga diagram, den andra bilden har inga former och den tredje bilden har inte villkorlig formatering.

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-CustomFilteringPerWorksheet-1.cs" >}}


Så här använder du klassen CustomLoadFilter enligt kalkylbladsnamn.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-CustomFilteringPerWorksheet-2.cs" >}}
