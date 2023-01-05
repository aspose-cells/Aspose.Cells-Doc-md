---
title: Olika sätt att öppna filer
type: docs
weight: 10
url: /sv/python-net/different-ways-to-open-files/
---
{{% alert color="primary" %}}

Med Aspose.Cells är det enkelt att öppna filer, till exempel för att hämta data, eller att använda en designermall för att påskynda utvecklingsprocessen.

{{% /alert %}}

## **Öppna en fil via en sökväg**

 Utvecklare kan öppna en Microsoft Excel-fil med dess sökväg på den lokala datorn genom att ange den i**Arbetsbok**klass konstruktör. Passera helt enkelt vägen i konstruktorn som en*sträng*. Aspose.Cells kommer automatiskt att upptäcka filformatstypen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFileViaPath.py" >}}

## **Öppna en fil via en ström**

Det är också enkelt att öppna en Excel-fil som en stream. För att göra det, använd en överbelastad version av konstruktorn som tar*BufferStream*objekt som innehåller filen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFileViaStream.py" >}}

## **Öppna en fil med endast data**

 För att öppna en fil med endast data, använd**LoadOptions** och**LoadFilter**klasser för att ställa in det relaterade attributet och alternativen för klasserna för mallfilen som ska laddas.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFilewithDataOnly.py" >}}

{{% alert color="primary" %}}

Ett undantag kommer att skapas om du försöker öppna icke-inbyggda Excel-filer eller andra filformat (till exempel PPT/PPTX, DOC/DOCX, etc.) med Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

 Det finns rimliga chanser att**Arbetsbok** konstruktör kan kasta*System.OutOfMemoryException* medan du laddar stora kalkylblad. Detta undantag tyder på att det tillgängliga minnet är otillräckligt för att fullständigt ladda kalkylarket i minnet, därför måste kalkylarket laddas samtidigt som minnesinställningarna aktiveras.

{{% /alert %}}
