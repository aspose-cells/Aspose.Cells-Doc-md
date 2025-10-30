---
title: Olika sätt att öppna filer
type: docs
weight: 10
url: /sv/python-net/different-ways-to-open-files/
description: Denna artikel förklarar hur man öppnar en Excel fil med Aspose.Cells för Python via .NET API.
keywords: Python Öppna en Excel fil utan Excel, Hur öppnar jag en Excel fil.
---

{{% alert color="primary" %}}

Med Aspose.Cells för Python via .NET är det enkelt att öppna filer, till exempel för att hämta data eller använda en designer-mall för att snabba upp utvecklingsprocessen.

{{% /alert %}}

## **Så öppnar du en Excel-fil via en sökväg**

Utvecklare kan öppna en Microsoft Excel-fil med dess filväg på den lokala datorn genom att specificera den i [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-klasskonstruktören. Ange helt enkelt sökvägen som en *sträng* i konstruktören. Aspose.Cells för Python via .NET kommer automatiskt att upptäcka filformatet.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFilesThroughPath-1.py" >}}

## **Så öppnar du en Excel-fil via en ström**

Det är också enkelt att öppna en Excel-fil som en ström. För att göra detta, använd en överlagrad version av konstruktören som tar *Stream*-objektet som innehåller filen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFilesThroughStream-1.py" >}}

## **Så öppnar du en fil med endast data**

För att öppna en fil med endast data, använd [**LoadOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions) och [**LoadFilter**](https://reference.aspose.com/cells/python-net/aspose.cells/loadfilter) klasserna för att ställa in de relaterade attributen och alternativen för klasserna för mönsterfilen som ska laddas.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFilewithDataOnly-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
