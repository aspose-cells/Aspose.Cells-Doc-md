---
title: CSV in JSON mit Golang über C++ konvertieren
linktitle: Konvertieren von CSV in JSON
type: docs
weight: 220
url: /de/go-cpp/convert-csv-to-json/
description: Konvertieren Sie CSV Datei in JSON mit der einfach zu verwendenden Aspose.Cells for C++ API.
keywords: Konvertieren, CSV in JSON konvertieren, CSV zu JSON, CSV, JSON, CSV zu JSON C++, C++ Code zum Konvertieren von CSV in JSON
---

## **Konvertieren von CSV in JSON**

Aspose.Cells unterstützt die Konvertierung von CSV in JSON. Hierfür stellt die API die Klassen [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/) und [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) bereit. Die Klasse [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/) bietet die Optionen für den Exportbereich nach JSON. Die Klasse [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/) hat die folgenden Eigenschaften.

- [**GetExportAsString()**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/getexportasstring/): Exportiert den Zeichenfolgenwert der Zellen in JSON.
- [**GetHasHeaderRow()**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/gethasheaderrow/): Gibt an, ob der Bereich eine Kopfzeile enthält.
- [**GetIndent()**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/getindent/): Gibt die Einrückung an.

Die [**JsonUtility**](https://reference.aspose.com/cells/go-cpp/jsonutility/)-Klasse exportiert JSON unter Verwendung der mit der [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/)-Klasse festgelegten Exportoptionen.

Das folgende Codebeispiel demonstriert die Verwendung der Klassen [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/) und [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) zum Laden der [Quelle CSV-Datei](104398879.csv) und druckt die JSON-Ausgabe in der Konsole.

### **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertCsvToJson.go" >}}
### **Konsolenausgabe**
{{< highlight java >}}

[
{
"id": 1,
"language": "Java",
"edition": "third",
"author": "Herbert Schildt",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
},
{
"id": 2,
"language": "C++",
"edition": "second",
"author": "EAAAA",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
},
{
"id": 3,
"language": ".Net",
"edition": "second",
"author": "E.Balagurusamy",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
}
]

{{< /highlight >}}
