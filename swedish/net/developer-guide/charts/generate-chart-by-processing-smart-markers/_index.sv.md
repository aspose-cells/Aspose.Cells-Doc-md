---
title: Skapa diagram genom att bearbeta Smart Markers
description: Lär dig hur du genererar diagram med smarta markörer med hjälp av Aspose.Cells for .NET. Vår guide kommer att visa dig hur du behandlar smarta markörer och deras egenskaper för att förbättra utseendet och användbarheten hos dina diagram.
keywords: Aspose.Cells for .NET, diagramgenerering, smarta markörer, utseende, användbarhet, behandling.
type: docs
weight: 2100
url: /sv/net/generate-chart-by-processing-smart-markers/
---

{{% alert color="primary" %}}

Aspose.Cells API:erna tillhandahåller [**WorkbookDesigner**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) klassen för att arbeta med Smart Markers där formatering och formler placeras i designerblad och sedan behandlas med [**WorkbookDesigner**](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) klassen för att fylla på data enligt angivna Smart Markers. Det är också möjligt att skapa Excel-diagram genom att behandla Smart Markers, vilket kommer att kräva följande steg.

- Skapande av designer-kalkylblad
- Behandling av designerblad mot angiven datakälla
- Skapande av diagram baserat på ifylld data

{{% /alert %}}

## Skapande av Designerblad

Ett designerblad är en enkel Excel-fil skapad med Microsoft Excel-applikation eller Aspose.Cells API:er som innehåller visuell formatering, formler och smarta markörer, där innehållet kan fyllas på vid runtime.

För enkelhets skull kommer vi att skapa designerbladet med hjälp av Aspose.Cells for .NET API:n och senare behandla det mot en dynamiskt skapad datakälla för demonstrationsändamål.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfDesignerSpreadsheet.cs" >}}

## Behandling av Designerblad

För att behandla designerbladet måste man ha en datakälla som överensstämmer med de Smarta Markörer som används i designerbladet. Till exempel har vi skapat en Smart Marker-post som &=Sales.Year, som representerar Årskolumnen i DataTable Sales. Om en motsvarande kolumn inte är tillgänglig i datakällan kommer Aspose.Cells API:erna att hoppa över behandlingen för den specifika Smarta Markören och som ett resultat kommer inte data för den specifika Smarta Markören att fyllas på.

För att demonstrera detta användningsfall kommer vi att skapa datakällan från grunden och behandla den mot designerbladet som skapats i det föregående steget. Dock kan i en realtidssituation data redan vara tillgänglig för ytterligare behandling så att du kan hoppa över skapandet av datakällan om data redan är tillgänglig.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingDesignerSpreadsheet.cs" >}}

Behandlingen av Smarta Markörer är ganska enkel som demonstrerat av den följande kodsnutten.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-ProcessingOfSmartMarkers.cs" >}}

{{% alert color="primary" %}}

Den ovanstående kodsnutten använder den befintliga instansen av [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klassen skapad i det första steget. Om du redan har designerbladsfilen på disk eller i minnet kan du skapa en instans av [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klassen genom att ladda den befintliga designerbladet.

{{% /alert %}}

## Skapande av Diagram

När datan är på plats behöver vi bara skapa ett diagram baserat på datakällan. För att hålla exemplet enkelt kommer vi att använda [**Chart.SetChartDataRange**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/setchartdatarange) metoden så att vi inte behöver konfigurera diagrammet ytterligare.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GenerateChartByProcessingSmartMarkers-CreationOfChart.cs" >}}
{{< app/cells/assistant language="csharp" >}}
