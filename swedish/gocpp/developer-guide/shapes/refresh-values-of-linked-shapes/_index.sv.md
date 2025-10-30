---
title: Uppdatera värden för länkade former med Golang via C++
linktitle: Uppdatera värdena för länkade former
type: docs
weight: 3200
url: /sv/go-cpp/refresh-values-of-linked-shapes/
description: Lär dig hur du uppdaterar värden på länkade figurer i Excel filer med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Ibland har du en länkad form i din Excel-fil som är länkad till någon cell. I Microsoft Excel ändrar ändra värdet i den länkade cellen även värdet för den länkade formen. Det fungerar också bra med Aspose.Cells om du vill spara din arbetsbok i XLS- eller XLSX-format. Om du dock vill spara din arbetsbok i PDF- eller HTML-format måste du ringa [**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/go-cpp/shapecollection/updateselectedvalue/)-metoden för att uppdatera värdet för den länkade formen.

{{% /alert %}}

## Exempel

Följande skärmdump visar käll-Excel-filen som används i exempelnumret nedan. Den har en länkad bild kopplad till cellerna A1 till E4. Vi kommer att ändra värdet i cell B4 med Aspose.Cells och sedan anropa [**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/go-cpp/shapecollection/updateselectedvalue/)-metoden för att uppdatera värdet på bilden och spara den i PDF-format.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

Du kan ladda ner [källa-Excelfilen](95584291.xlsx) och [utdata-PDF](95584292.pdf) från angivna länkar.

### C++ kod för att uppdatera värden för länkade figurer

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RefreshValuesOfLinkedShapes.go" >}}
