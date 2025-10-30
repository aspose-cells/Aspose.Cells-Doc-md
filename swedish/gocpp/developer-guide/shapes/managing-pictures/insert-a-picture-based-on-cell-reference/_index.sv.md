---
title: Infoga en bild baserad på cellreferens med Golang via C++
linktitle: Infoga en bild baserat på cellreferens
type: docs
weight: 150
url: /sv/go-cpp/insert-a-picture-based-on-cell-reference/
description: Lär dig hur man infogar en bild baserad på cellreferens med hjälp av Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Ibland har du en tom bild och behöver visa data eller innehåll i bilden genom att ange en cellreferens i formelfältet. Aspose.Cells stöder den här funktionen (Microsoft Excel 2010).

{{% /alert %}}

## Infoga en bild baserad på cellreferens

Aspose.Cells stöder att visa innehållet i en kalkylbladscell i en bildform. Du kan länka bilden till cellen som innehåller datan du vill visa. Eftersom cellen eller cellintervallet är länkad till den grafiska objektet visar ändringar som du gör i datan i den cellen eller cellintervallet automatiskt upp i det grafiska objektet. Lägg till en bild i kalkylbladet genom att använda [**AddPicture**](https://reference.aspose.com/cells/go-cpp/shapecollection/addpicture_int_int_int_int_stream/) metoden i [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) samlingen (inkapslad i [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) objektet). Ange cellintervallet genom att använda [**Formula**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/getformula/) attributet i [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/) objektet.

### Kodexempel

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertAPictureBasedOnCellReference.go" >}}
