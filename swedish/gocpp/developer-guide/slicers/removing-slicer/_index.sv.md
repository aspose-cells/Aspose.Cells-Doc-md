---
title: Ta bort slicer med Golang via C++
linktitle: Ta bort slicer
type: docs
weight: 30
url: /sv/go-cpp/removing-slicer/
description: Lär dig hur du tar bort slicers i Excel filer programmässigt med hjälp av Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Om du vill ta bort en slicer i Microsoft Excel, välj den och tryck på *Delete*-knappen. På liknande sätt, om du vill ta bort den med Aspose.Cells API-programmering, använd [**Worksheet.Slicers.Remove()**](https://reference.aspose.com/cells/go-cpp/slicercollection/remove/)-metoden. Det tar bort slicern från arket.

## **Ta bort slicer**

Följande exempelkod laddar den [provmappen](67338478.xlsx) som innehåller en befintlig snitt. Den kommer åt snittet och tar bort det. Slutligen sparar den arbetsboken som [utmatningsmapp](67338477.xlsx). Följande skärmbild visar snittet som kommer att tas bort efter körningen av exempelkoden.

![todo:image_alt_text](removing-slicer_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RemovingSlicer.go" >}}
