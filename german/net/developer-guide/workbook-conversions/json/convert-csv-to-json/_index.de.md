---
title: Konvertieren von CSV in JSON
type: docs
weight: 220
url: /de/net/convert-csv-to-json/
description: CSF Datei in JSON konvertieren, indem Sie die einfache zu verwendende Aspose.Cells for .NET API verwenden.
keywords: Konvertieren, CVS in JSON konvertieren, CSV in JSON konvertieren, CSV, JSON, CSV in JSON CSharp konvertieren, c# Code zum Konvertieren von CSV in JSON
---

## **Konvertieren von CSV in JSON**

Aspose.Cells unterstützt die Umwandlung von CSV in JSON. Hierfür bietet die API die [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)- und [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)-Klassen. Die [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)-Klasse bietet Optionen zum Exportieren des Bereichs als JSON. Die [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)-Klasse hat folgende Eigenschaften.

- [**ExportAsString**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/exportasstring): Exportiert den Zeichenfolgenwert der Zellen in JSON.
- [**HasHeaderRow**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/hasheaderrow): Gibt an, ob der Bereich eine Kopfzeile enthält.
- [**Indent**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/indent): Gibt die Einrückung an.

Die Klasse [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) exportiert das JSON unter Verwendung der Exportoptionen, die mit der Klasse [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions) festgelegt sind.

Der folgende Beispielcode zeigt die Verwendung der [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)- und [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)-Klassen zum Laden der [Quell-CSV-Datei](104398879.csv) und gibt die JSON-Ausgabe in der Konsole aus.

### **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.cs" >}}

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
