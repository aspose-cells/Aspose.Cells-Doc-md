---
title: Generera diagram genom att bearbeta smarta markörer
type: docs
weight: 2100
url: /sv/net/generate-chart-by-processing-smart-markers/
---
{{% alert color="primary" %}}

 Aspose.Cells API:er tillhandahåller[**Arbetsboksdesigner**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)klass för att arbeta med Smart Markers där formateringen och formlerna placeras i designerkalkylbladen och sedan bearbetas med[**Arbetsboksdesigner**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)klass för att fylla i data enligt specificerade Smart Markers. Det är också möjligt att skapa Excel-diagram genom att bearbeta smarta markörer, vilket kräver följande steg.

- Skapande av designerkalkylblad
- Bearbetar designerkalkylblad mot den angivna datakällan
- Skapande av diagram baserat på ifyllda data

{{% /alert %}}

## Skapande av designerkalkylblad

Ett designerkalkylblad är en enkel Excel-fil skapad med Microsoft Excel-applikationen eller Aspose.Cells API:er som innehåller visuell formatering, formler och smarta markörer, där innehållet kan fyllas i under körning.

För enkelhetens skull kommer vi att skapa designerkalkylarket med hjälp av Aspose.Cells för .NET API och senare bearbeta det mot en dynamiskt skapad datakälla för demonstrationsändamål.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfDesignerSpreadsheet.cs" >}}

## Bearbetar Designer-kalkylblad

För att bearbeta designerkalkylarket måste man ha en datakälla som motsvarar de smarta markörer som används i designerkalkylarket. Vi har till exempel skapat en Smart Marker-post som &=Försäljning.År, som representerar kolumnen År i DataTable Sales. Om en motsvarande kolumn inte är tillgänglig i datakällan, kommer Aspose.Cells API:erna att hoppa över bearbetningen för just den smarta markören, och som ett resultat kommer data för den specifika smarta markören inte att fyllas i.

För att demonstrera detta användningsfall kommer vi att skapa datakällan från början och bearbeta den mot designerkalkylbladet som skapades i föregående steg. Men i ett realtidsscenario kan data redan vara tillgängliga för vidare bearbetning så att du kan hoppa över skapandet av datakälla om data redan är tillgänglig.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingDesignerSpreadsheet.cs" >}}

Bearbetningen av smarta markörer är ganska enkel, vilket visas av följande kodavsnitt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingOfSmartMarkers.cs" >}}

{{% alert color="primary" %}}

 Ovanstående kodavsnitt använder den befintliga instansen av[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook)klass skapad i det första steget. Om du redan har designarkfilen på disk eller minne kan du skapa en instans av[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook)klass genom att ladda det befintliga designerkalkylarket.

{{% /alert %}}

## Skapande av diagram

 När data är på plats behöver vi bara skapa ett diagram baserat på datakällan. För att hålla exemplet enkelt kommer vi att använda[**Chart.SetChartDataRange**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/setchartdatarange)metod så att vi inte behöver konfigurera diagrammet ytterligare.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfChart.cs" >}}
