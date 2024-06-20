---
title: Olika sätt att öppna filer
type: docs
weight: 10
url: /sv/python-net/different-ways-to-open-files/
---

{{% alert color="primary" %}}

Med Aspose.Cells är det enkelt att öppna filer, till exempel för att hämta data, eller att använda en designmall för att snabba på utvecklingsprocessen.

{{% /alert %}}

## **Öppna en fil via en sökväg**

Utvecklare kan öppna en Microsoft Excel-fil med dess filväg på den lokala datorn genom att ange den i klasskonstruktören för **Workbook**. Ange helt enkelt sökvägen i konstruktören som en *string*. Aspose.Cells kommer automatiskt att upptäcka filformatstypen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFileViaPath.py" >}}

## **Öppna en fil via en ström**

Det är också enkelt att öppna en Excel-fil som en ström. Använd en överlagrad version av konstruktören som tar *BufferStream*-objektet som innehåller filen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFileViaStream.py" >}}

## **Öppna en fil med endast data**

För att öppna en fil med endast data, använd **LoadOptions** och **LoadFilter**-klasserna för att ställa in de relaterade attributen och alternativen för klasserna för den mallfil som ska laddas.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFilewithDataOnly.py" >}}

{{% alert color="primary" %}}

Ett undantag kommer att kastas om du försöker att öppna icke-ursprungliga Excel-filer eller andra filformat (till exempel PPT/PPTX, DOC/DOCX, etc.) med Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

Det finns rätt stora chanser att **Workbook**-konstruktören kan kasta *System.OutOfMemoryException* när den laddar stora kalkylblad. Detta undantag antyder att minnet är otillräckligt för att helt ladda kalkylarket i minnet och därför måste kalkylarket laddas med aktiverade Minnesinställningar.

{{% /alert %}}
