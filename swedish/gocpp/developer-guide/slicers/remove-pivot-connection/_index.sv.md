---
title: Ta bort pivottillbehör med Golang via C++
linktitle: Ta bort pivotkoppling
type: docs
weight: 30
url: /sv/go-cpp/remove-pivot-connection/
description: Lär dig hur du tar bort pivottabellanslutning med Aspose.Cells biblioteket med C++.
keywords: Ta bort pivotkoppling utan Office 2013, Office 2016, Office 2019 och Office 365.
---

## **Möjliga användningsscenario**

Om du vill avassociera en slicer och en pivottabell i Excel, måste du högerklicka på slicern och välja "Rapportkopplingar...". I alternativlistan kan du använda kryssrutan. På liknande sätt om du vill avassociera en slicer och pivottabell med Aspose.Cells API programmatiskt, använd [**Slicer.RemovePivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/go-cpp/slicer/removepivotconnection/)-metoden. Den kommer att avassosciera slicern och pivottabellen.

## **Bryt isär snitt och pivottabell**

Följande provkod laddar in [provmappen](remove-pivot-connection.xlsx) som innehåller en befintlig slicer. Den går igenom slicerna och sedan avassocierar den slicern och pivottabellen. Slutligen sparar den arbetsboken som [output Excel-fil](remove-pivot-connection-out.xlsx). 

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RemovePivotConnection.go" >}}
