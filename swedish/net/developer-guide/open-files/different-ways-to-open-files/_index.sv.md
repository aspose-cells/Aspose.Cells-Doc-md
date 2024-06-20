---
title: Olika sätt att öppna filer
type: docs
weight: 10
url: /sv/net/different-ways-to-open-files/
description: Denna artikel förklarar hur man öppnar en Excel fil med Aspose.Cells for .NET API.
keywords: C# Öppna en Excel fil utan Excel, Hur öppnar jag en Excel fil.
---

{{% alert color="primary" %}}

Med Aspose.Cells är det enkelt att öppna filer, till exempel för att hämta data, eller att använda en designmall för att snabba på utvecklingsprocessen.

{{% /alert %}}

## **Så öppnar du en Excel-fil via en sökväg**

Utvecklare kan öppna en Microsoft Excel-fil genom att ange dess filväg på den lokala datorn genom att specificera det i klasskonstruktören [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook). Ange helt enkelt filvägen i konstruktören som en *string*. Aspose.Cells kommer automatiskt att upptäcka filformatet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughPath-1.cs" >}}

## **Så öppnar du en Excel-fil via en ström**

Det är också enkelt att öppna en Excel-fil som en ström. För att göra detta, använd en överlagrad version av konstruktören som tar *Stream*-objektet som innehåller filen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughStream-1.cs" >}}

## **Så öppnar du en fil med endast data**

För att öppna en fil med endast data, använd [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) och [**LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadfilter) klasserna för att ställa in de relaterade attributen och alternativen för klasserna för mönsterfilen som ska laddas.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilewithDataOnly-1.cs" >}}

## **Så lastar du bara synliga ark**

När du laddar en [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) kan det hända att du endast behöver data i synliga arkmallar i en arbetsbok. Aspose.Cells låter dig hoppa över data i osynliga arkmallar när du laddar en arbetsbok. För att göra detta kan du skapa en anpassad funktion som ärver från klassen [**LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadfilter) och skicka dess instans till egenskapen [**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-1.cs" >}}

Här är implementeringen av klassen *CustomnLoad* som refereras till i ovanstående kodsnutt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-2.cs" >}}

{{% alert color="primary" %}}

Ett undantag kommer att kastas om du försöker att öppna icke-ursprungliga Excel-filer eller andra filformat (till exempel PPT/PPTX, DOC/DOCX, etc.) med Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

Det finns en rättvis chans att [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) konstruktören kan kasta *System.OutOfMemoryException* när du laddar stora kalkylblad. Detta undantag tyder på att minnet är otillräckligt för att helt ladda kalkylarket i minnet, därför måste kalkylarket laddas med aktiverade minnesinställningar.

{{% /alert %}}
