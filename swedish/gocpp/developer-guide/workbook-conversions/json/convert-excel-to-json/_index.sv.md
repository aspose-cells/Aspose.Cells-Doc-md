---
title: Konvertera Excel till JSON med Golang via C++
linktitle: Konvertera Excel till JSON
type: docs
weight: 300
url: /sv/go-cpp/convert-excel-to-json/
description: Lär dig hur man konverterar Excel fil till JSON med Aspose.Cells och C++.
keywords: Exportera arbetsbok till json utan Office 2013, Office 2016, Office 2019 och Office 365
---

{{% alert color="primary" %}}

Aspose.Cells stödjer att konvertera en arbetsbok till JSON-fil (JavaScript Object Notation).

{{% /alert %}}

## **Konvertera Excel-arbetsbok till JSON**

Det är ingen anledning att undra hur man konverterar Excel-arbetsbok till JSON, för bibliotek Aspose.Cells for C++ har den bästa lösningen. API:n Aspose.Cells stöder konvertering av kalkylblad till JSON-format. För att exportera arbetsboken till JSON, skicka [**SaveFormat.Json**](https://reference.aspose.com/cells/go-cpp/saveformat/) som andra parameter till [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) metoden. Du kan även använda klassen [**JsonSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/jsonsaveoptions/) för att specificera ytterligare inställningar för export av kalkylblad till JSON.

Nedan visar kodexemplet export av Excel-arbetsbok till JSON. Se koden för att konvertera [källdokument](sample.xlsx) till den JSON-fil som genereras av koden för referens.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertExcelToJson.go" >}}
Nästa kodexempel använder JsonSaveOptions-klassen för att specificera ytterligare inställningar och visar export av Excel-arbetsbok till JSON. Se koden för att konvertera [källdokument](sample.xlsx) till den JSON-fil som genereras av koden för referens.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertExcelToJson-1.go" >}}
