---
title: Kopiera rader och kolumner
type: docs
weight: 40
url: /sv/python-net/copying-rows-and-columns/
description: Denna artikel visar hur man kopierar rader och kolumner genom Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Python Så här kopierar och klistrar du in rader och kolumner med Aspose.Cells for Python via .NET, Python Klistra in flera rader och kolumner, Python Så här kopierar du och klistrar in enstaka rad eller kolumn.
---

## **Introduktion**

Ibland behöver du kopiera rader och kolumner i en arbetsbok utan att kopiera hela arbetsboken. Med Aspose.Cells är det möjligt att kopiera rader och kolumner inom eller mellan arbetsböcker.
När en rad (eller kolumn) kopieras, kopieras också den data som finns i den, inklusive formler - med uppdaterade referenser - och värden, kommentarer, formatering, dolda celler, bilder och andra ritobjekt.

## **Hur man kopierar rader och kolumner med Microsoft Excel**

1. Markera raden eller kolumnen som du vill kopiera.
1. För att kopiera rader eller kolumner, klicka på **Kopiera** på **Standard** verktygsfältet, eller tryck på **CTRL**+**C**.
1. Välj en rad eller en kolumn nedanför eller till höger om där du vill kopiera ditt val.
1. När du kopierar rader eller kolumner, klicka på **Kopierade celler** på menyn **Infoga**.

{{% alert color="primary" %}}

Om du klickar på **Klistra in** på **Standard** verktygsfältet eller trycker på **CTRL**+**V** istället för att klicka på en kommando i **Infoga** menyn, ersätts eventuella innehåll i destinationens celler.

{{% /alert %}}

## **Hur man klistrar in rader och kolumner med hjälp av klistra in-alternativ med Microsoft Excel**

1. Välj cellerna som innehåller data eller andra attribut som du vill kopiera.
1. På fliken Hem, klicka på **Kopiera**.
1. Klicka på den första cellen i det område där du vill **klistra in** det du kopierade.
1. På fliken Hem, klicka på pilen bredvid **Klistra in**, och välj sedan **Klistra in** Special.
1. Välj de **alternativ** du vill.

## **Hur man kopierar rader och kolumner med Aspose.Cells för Python via .NET**

## **Hur man kopierar enskilda rader**

Aspose.Cells tillhandahåller metoden [**copy_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_row/#aspose.cells.Cells-int-int) i klassen [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Denna metod kopierar alla typer av data inklusive formler, värden, kommentarer, cellformat, dolda celler, bilder och andra ritobjekt från källraden till destinationsraden.

Metoden [**copy_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_row/#aspose.cells.Cells-int-int) tar följande parametrar:

- källobjektet [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells),
- källradindex, samt
- destinationsradindex.

Använd den här metoden för att kopiera en rad inom ett blad, eller till ett annat blad. Metoden [**copy_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_row/#aspose.cells.Cells-int-int) fungerar på ett liknande sätt som Microsoft Excel. Så till exempel behöver du inte ställa in höjden på destinationsraden explicit, det värdet kopieras också.

Följande exempel visar hur man kopierar en rad i en arbetsbok. Det använder en mall Microsoft Excel-fil och kopierar den andra raden (komplett med data, formatering, kommentarer, bilder och så vidare) och klistrar in den i den 12:e raden i samma arbetsbok.

Du kan hoppa över steget som hämtar källradens höjd med hjälp av metoden [**Cells.get_row_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/get_row_height/#int) och sedan ställer in destinationsradens höjd med hjälp av metoden [**Cells.set_row_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_row_height/#int-float) eftersom metoden [**copy_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_row/#aspose.cells.Cells-int-int) automatiskt tar hand om radhöjden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Copying-CopyingRows-1.py" >}}

{{% alert color="primary" %}}

Vid kopiering av rader är det viktigt att notera relaterade bilder, diagram eller andra ritobjekt eftersom detta är detsamma med Microsoft Excel:

1. Om källradens index är 5, kopieras bilden, diagrammet osv. om den finns i de tre raderna (startindexet är 4 och slutindexet är 6).
1. De befintliga bilderna, diagrammen osv. i destinationsraden kommer inte att tas bort.

{{% /alert %}}

## **Hur man kopierar flera rader**

Du kan också kopiera flera rader till en ny destination med hjälp av [**Cells.copy_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_rows/#aspose.cells.Cells-int-int-int) metoden som tar en ytterligare parameter av typen integer för att ange antalet källrader som ska kopieras.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Copying-CopyingMultipleRows-1.py" >}}


## **Hur man kopierar kolumner**

Aspose.Cells tillhandahåller metoden [**copy_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_column/#aspose.cells.Cells-int-int) i klassen [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells), denna metod kopierar alla typer av data, inklusive formler - med uppdaterade referenser - och värden, kommentarer, cellformat, dolda celler, bilder och andra ritobjekt från källkolumnen till destinationskolumnen.

Metoden [**copy_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_column/#aspose.cells.Cells-int-int) tar följande parametrar:

- källobjektet [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells),
- källkolumnens index och
- destinationskolumnens index.

Använd metoden [**copy_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_column/#aspose.cells.Cells-int-int) för att kopiera en kolumn inom en kalkylblad eller till ett annat kalkylblad.

Detta exempel kopierar en kolumn från ett blad och klistrar in den i ett blad i en annan arbetsbok.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Copying-CopyingColumns-1.py" >}}

## **Hur man kopierar flera kolumner**

På liknande sätt som [**Cells.copy_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_rows/#aspose.cells.Cells-int-int-int)-metoden tillhandahåller också Aspose.Cells API:er metoden [**Cells.copy_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_columns/) för att kopiera flera källkolumner till en ny plats.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Copying-CopyingMultipleColumns-1.py" >}}


## **Hur man klistrar in rader och kolumner med klistringsalternativ**

Aspose.Cells tillhandahåller nu [**PasteOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pasteoptions) medan man använder funktionerna [**copy_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_rows/#aspose.cells.Cells-int-int-int-aspose.cells.CopyOptions-aspose.cells.PasteOptions) och [**copy_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_columns/#aspose.cells.Cells-int-int-int-aspose.cells.PasteOptions). Det gör det möjligt att ställa in lämpligt klistringsalternativ liknande Excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Copying-PastingRowsColumnsWithPasteOptions-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
