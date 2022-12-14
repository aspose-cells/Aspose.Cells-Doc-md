---
title: Olika sätt att öppna filer
type: docs
weight: 10
url: /sv/net/different-ways-to-open-files/
---
{{% alert color="primary" %}}

Med Aspose.Cells är det enkelt att öppna filer, till exempel för att hämta data, eller att använda en designermall för att påskynda utvecklingsprocessen.

{{% /alert %}}

## **Öppna en fil via en sökväg**

 Utvecklare kan öppna en Microsoft Excel-fil med hjälp av dess sökväg på den lokala datorn genom att ange den i**[Arbetsbok](https://reference.aspose.com/cells/net/aspose.cells/workbook)**klass konstruktör. Passera helt enkelt vägen i konstruktorn som en*sträng*. Aspose.Cells kommer automatiskt att upptäcka filformatstypen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughPath-1.cs" >}}

## **Öppna en fil via en ström**

 Det är också enkelt att öppna en Excel-fil som en stream. För att göra det, använd en överbelastad version av konstruktorn som tar*Ström*objekt som innehåller filen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughStream-1.cs" >}}

## **Öppna en fil med endast data**

 För att öppna en fil med endast data, använd**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** och**[LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter)**klasser för att ställa in det relaterade attributet och alternativen för klasserna för mallfilen som ska laddas.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilewithDataOnly-1.cs" >}}

## **Laddar endast synliga ark**

 När du laddar en**[Arbetsbok](https://reference.aspose.com/cells/net/aspose.cells/workbook)**ibland behöver du kanske bara data i synliga kalkylblad i en arbetsbok. Aspose.Cells låter dig hoppa över data i osynliga kalkylblad medan du laddar en arbetsbok. För att göra detta, skapa en anpassad funktion som ärver**[LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter)**klass och skicka sin instans till**[LoadOptions.LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)**fast egendom.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-1.cs" >}}

Här är genomförandet av*CustomnLoad*klass som hänvisas till i kodavsnittet ovan.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-2.cs" >}}

{{% alert color="primary" %}}

Ett undantag kommer att skapas om du försöker öppna icke-inbyggda Excel-filer eller andra filformat (till exempel PPT/PPTX, DOC/DOCX, etc.) med Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

 Det finns rimliga chanser att**[Arbetsbok](https://reference.aspose.com/cells/net/aspose.cells/workbook)** konstruktör kan kasta*System.OutOfMemoryException* medan du laddar stora kalkylblad. Detta undantag tyder på att det tillgängliga minnet är otillräckligt för att fullständigt ladda kalkylarket i minnet, därför måste kalkylarket laddas samtidigt som minnesinställningarna aktiveras.

{{% /alert %}}
