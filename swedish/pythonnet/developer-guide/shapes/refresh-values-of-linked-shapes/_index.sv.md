---
title: Uppdatera värdena för länkade former
type: docs
weight: 3200
url: /sv/python-net/refresh-values-of-linked-shapes/
---

{{% alert color="primary" %}}

Ibland har du en länkat form i ditt Excel-fil som är kopplat till en cell. I Microsoft Excel ändras värdet på den länkade cellen också, vilket ändrar värdet på den länkade formen. Detta fungerar också utmärkt med Aspose.Cells för Python via .NET om du vill spara din arbetsbok i XLS eller XLSX-format. Men om du vill spara arbetsboken i PDF- eller HTML-format måste du kalla [**Worksheet.Shapes.update_selected_value()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/update_selected_value)-metoden för att uppdatera värdet på den länkade formen.

{{% /alert %}}

## Exempel

Nedan skärmbild visar den ursprungliga Excelfilen som används i koden nedan. Den har en länkad bild kopplad till cellerna A1 till E4. Vi kommer att ändra värdet i cell B4 med Aspose.Cells för Python via .NET och sedan anropa [**Worksheet.Shapes.update_selected_value()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/update_selected_value)-metoden för att uppdatera värdet på bilden och spara det i PDF-format.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

Du kan ladda ner [käll-Excel-filen](95584291.xlsx) och [utmatnings-PDF-filen](95584292.pdf) från de angivna länkarna.

### C#-kod för att uppdatera värdena för länkade former

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-RefreshValueOfLinkedShapes-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
