---
title: Lägg till pivottillbehör med Golang via C++
linktitle: Lägg till pivottabellanslutning
type: docs
weight: 30
url: /sv/go-cpp/add-pivot-connection/
description: Lär dig hur du lägger till pivottabellanslutning med Aspose.Cells biblioteket med hjälp av C++.
keywords: Lägg till pivottabellanslutning utan Office 2013, Office 2016, Office 2019 och Office 365.
---

## **Möjliga användningsscenario**

Om du vill associera slicer och pivottabell i Excel måste du högerklicka på slicern och välja alternativet "Rapportanslutningar...". I alternativlistan kan du använda kryssrutan. På liknande sätt, om du vill associera slicer och pivottabell med hjälp av Aspose.Cells API programmatiskt, använd [**Slicer.AddPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/go-cpp/slicer/addpivotconnection/) metoden. Den kommer att associera slicer och pivottabell.

## **Associera slicer och Pivottabell**

Följande exempelkod laddar in den [exempel-Excel-filen](add-pivot-connection.xlsx) som innehåller en befintlig slicer. Den får åtkomst till slicern och associerar sedan slicer och pivottabell. Slutligen sparar den arbetsboken som [utdata-Excel-fil](add-pivot-connection-out.xlsx). 

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddPivotConnection.go" >}}
