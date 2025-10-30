---
title: Excel in JSON mit Golang über C++ umwandeln
linktitle: Excel in JSON konvertieren
type: docs
weight: 300
url: /de/go-cpp/convert-excel-to-json/
description: Erfahren Sie, wie Sie mit Aspose.Cells und C++ Excel Dateien in JSON konvertieren.
keywords: Exportieren von Arbeitsmappe nach JSON ohne Office 2013, Office 2016, Office 2019 und Office 365
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt die Umwandlung einer Arbeitsmappe in eine JSON (JavaScript Object Notation)-Datei.

{{% /alert %}}

## **Excel-Arbeitsmappe in JSON konvertieren**

Sie müssen sich keine Sorgen machen, wie man eine Excel-Arbeitsmappe in JSON konvertiert, denn die Aspose.Cells for C++-Bibliothek hat die beste Lösung. Die Aspose.Cells API bietet Unterstützung für die Konvertierung von Tabellenkalkulationen in JSON-Format. Um die Arbeitsmappe in JSON zu exportieren, übergeben Sie [**SaveFormat.Json**](https://reference.aspose.com/cells/go-cpp/saveformat/) als zweiten Parameter der [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)-Methode. Sie können auch die Klasse [**JsonSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/jsonsaveoptions/) verwenden, um zusätzliche Einstellungen für den Export des Arbeitsblatts nach JSON festzulegen.

Das folgende Codebeispiel zeigt den Export einer Excel-Arbeitsmappe nach JSON. Bitte sehen Sie sich den Code an, um die [Quelldatei](sample.xlsx) zu konvertieren, sowie die durch den Code generierte JSON-Datei zur Referenz.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertExcelToJson.go" >}}
Das folgende Codebeispiel verwendet die JsonSaveOptions-Klasse, um zusätzliche Einstellungen festzulegen, und demonstriert den Export einer Excel-Arbeitsmappe nach JSON. Bitte sehen Sie sich den Code an, um die [Quelle Datei](sample.xlsx) in die durch den Code generierte JSON-Datei zu konvertieren.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertExcelToJson-1.go" >}}
