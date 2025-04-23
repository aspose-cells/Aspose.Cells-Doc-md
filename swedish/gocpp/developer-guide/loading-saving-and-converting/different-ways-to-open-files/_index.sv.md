---
title: Olika sätt att öppna filer
linktitle: Olika sätt att öppna filer
type: docs
weight: 10
url: /sv/go-cpp/different-ways-to-open-files/
---

{{% alert color="primary" %}}

Med Aspose.Cells kan du öppna filer, till exempel för att hämta data eller använda en designer-mall för att påskynda utvecklingsprocessen. Aspose.Cells kan öppna ett brett utbud av olika filer, som Microsoft Excel-kalkylblad (XLS, XLSX, XLSM, XLSB), CSV eller TabDelimited-filer.

{{% /alert %}}

## **Öppna en fil via en sökväg**

Utvecklare kan öppna en Microsoft Excel-fil med dess filväg på den lokala datorn genom att ange det i [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) klassen konstructor. Skicka vägen som en sträng i konstruktorn. Aspose.Cells kommer automatiskt att upptäcka filformatet.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadWorkbookUsingPath.go" >}}

## **Öppna en fil med hjälp av en stream**

Det är också möjligt att öppna en Excel-fil som en ström. För att göra det, använd en överlagrad version av konstruktorn som tar emot *Stream*objektet som innehåller filen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadWorkbookUsingStream.go" >}}
