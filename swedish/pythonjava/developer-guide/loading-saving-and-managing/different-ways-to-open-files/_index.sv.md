---
title: Olika sätt att öppna filer
type: docs
weight: 10
url: /sv/python-java/different-ways-to-open-files/
---

{{% alert color="primary" %}}

Med Aspose.Cells är det enkelt att öppna filer, till exempel för att hämta data, eller att använda en designmall för att snabba på utvecklingsprocessen.

{{% /alert %}}

## **Öppna en fil via en sökväg**

Utvecklare kan öppna en Microsoft Excel-fil genom att ange dess filväg på den lokala datorn genom att specificera det i klasskonstruktören [**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook). Ange helt enkelt filvägen i konstruktören som en *string*. Aspose.Cells kommer automatiskt att upptäcka filformatet.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFileViaPath.py" >}}

## **Öppna en fil via en ström**

Det är också enkelt att öppna en Excel-fil som en ström. Använd en överlagrad version av konstruktören som tar *BufferStream*-objektet som innehåller filen.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFileViaStream.py" >}}

## **Öppna en fil med endast data**

För att öppna en fil med endast data, använd [**LoadOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions) och [**LoadFilter**](https://reference.aspose.com/cells/python-java/asposecells.api/LoadFilter) klasserna för att ställa in de relaterade attributen och alternativen för klasserna för mönsterfilen som ska laddas.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFilewithDataOnly.py" >}}

{{% alert color="primary" %}}

Ett undantag kommer att kastas om du försöker att öppna icke-ursprungliga Excel-filer eller andra filformat (till exempel PPT/PPTX, DOC/DOCX, etc.) med Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

Det finns en rättvis chans att [**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook) konstruktören kan kasta *System.OutOfMemoryException* när du laddar stora kalkylblad. Detta undantag tyder på att minnet är otillräckligt för att helt ladda kalkylarket i minnet, därför måste kalkylarket laddas med aktiverade minnesinställningar.

{{% /alert %}}
