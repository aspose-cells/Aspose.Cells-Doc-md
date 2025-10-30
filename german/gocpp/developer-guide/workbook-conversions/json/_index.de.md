---
title: Arbeitsmappe in JSON mit Golang über C++ konvertieren
linktitle: Arbeitsmappe in JSON konvertieren
type: docs
weight: 300
url: /de/go-cpp/convert-workbook-to-json/
description: Erfahren Sie, wie Sie Excel Arbeitsmappen mit Aspose.Cells for C++ in JSON Format umwandeln.
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt die Konvertierung einer Arbeitsmappe in eine JSON (JavaScript Object Notation)-Datei.

{{% /alert %}}

## **Excel-Arbeitsmappe in JSON konvertieren**

Das Aspose.Cells API unterstützt die Konvertierung von Tabellenblättern in JSON-Format. Um die Arbeitsmappe in JSON zu exportieren, übergeben Sie [**SaveFormat::Json**](https://reference.aspose.com/cells/go-cpp/saveformat/) als zweiten Parameter der [**Workbook::Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)-Methode. Sie können auch die [**JsonSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/jsonsaveoptions/)-Klasse verwenden, um zusätzliche Einstellungen für den Export des Arbeitsblatts in JSON anzugeben.

Das folgende Codebeispiel zeigt, wie das aktive Arbeitsblatt mit der [**SaveFormat::Json**](https://reference.aspose.com/cells/go-cpp/saveformat/)-Aufzählungsmitglied in JSON exportiert wird. Bitte beachten Sie den Code zum Konvertieren der [Quelldatei](book1.xlsx) in die [Ausgabe-JSON-Datei](book1.json), die vom Code generiert wurde.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Json.go" >}}
## **Erweiterte Themen**
- [Konvertieren von CSV in JSON](/cells/de/cpp/convert-csv-to-json/)
- [Excel nach JSON konvertieren](/cells/de/cpp/convert-excel-to-json/)
- [JSON in CSV konvertieren](/cells/de/cpp/convert-json-to-csv/)
- [JSON in Excel konvertieren](/cells/de/cpp/convert-json-to-excel/)
