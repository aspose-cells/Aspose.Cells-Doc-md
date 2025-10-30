---
title: Formatera slicer med Golang via C++
linktitle: Formatering av Slicer
type: docs
weight: 20
url: /sv/go-cpp/formatting-slicer/
description: Formatera slicers i Microsoft Excel med Aspose.Cells med Golang via C++.
---

## **Möjliga användningsscenario**

Du kan formatera slicern i Microsoft Excel genom att ställa in antalet kolumner eller genom att ställa in dess stil etc. Aspose.Cells tillåter dig också att göra detta med hjälp av [**Slicer.GetNumberOfColumns()**](https://reference.aspose.com/cells/go-cpp/slicer/getnumberofcolumns/) och [**Slicer.GetStyleType()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/getstyletype/) egenskaper.

## **Formatera skärva**

Se följande kod; den laddar filen [sample Excel](67338473.xlsx) som innehåller en slicer. Den nås slicern och ställer in dess antal kolumner och stiltyp och sparar den som [utdata Excel](67338474.xlsx). Skärmbilden visar hur slicern ser ut efter att ha kört exemplet.

![todo:image_alt_text](formatting-slicer_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingSlicer.go" >}}
