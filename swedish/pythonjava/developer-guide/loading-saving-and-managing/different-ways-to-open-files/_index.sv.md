---
title: Olika sätt att öppna filer
type: docs
weight: 10
url: /sv/python-java/different-ways-to-open-files/
---
{{% alert color="primary" %}}

Med Aspose.Cells är det enkelt att öppna filer, till exempel för att hämta data, eller att använda en designermall för att påskynda utvecklingsprocessen.

{{% /alert %}}

## **Öppna en fil via en sökväg**

 Utvecklare kan öppna en Microsoft Excel-fil med dess sökväg på den lokala datorn genom att ange den i**[Arbetsbok](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook)**klass konstruktör. Passera helt enkelt vägen i konstruktorn som en*sträng*. Aspose.Cells kommer automatiskt att upptäcka filformatstypen.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFileViaPath.py" >}}

## **Öppna en fil via en ström**

Det är också enkelt att öppna en Excel-fil som en stream. För att göra det, använd en överbelastad version av konstruktorn som tar*BufferStream*objekt som innehåller filen.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFileViaStream.py" >}}

## **Öppna en fil med endast data**

 För att öppna en fil med endast data, använd**[LoadOptions](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions)** och**[LoadFilter](https://reference.aspose.com/cells/python-java/asposecells.api/LoadFilter)**klasser för att ställa in det relaterade attributet och alternativen för klasserna för mallfilen som ska laddas.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFilewithDataOnly.py" >}}

{{% alert color="primary" %}}

Ett undantag kommer att skapas om du försöker öppna icke-inbyggda Excel-filer eller andra filformat (till exempel PPT/PPTX, DOC/DOCX, etc.) med Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

 Det finns rimliga chanser att**[Arbetsbok](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook)** konstruktör kan kasta*System.OutOfMemoryException* medan du laddar stora kalkylblad. Detta undantag tyder på att det tillgängliga minnet är otillräckligt för att fullständigt ladda kalkylarket i minnet, därför måste kalkylarket laddas samtidigt som minnesinställningarna aktiveras.

{{% /alert %}}
