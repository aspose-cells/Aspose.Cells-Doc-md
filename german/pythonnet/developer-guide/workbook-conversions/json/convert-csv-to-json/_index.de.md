---
title: Konvertieren von CSV in JSON
type: docs
weight: 220
url: /de/python-net/convert-csv-to-json/
description: Konvertieren Sie CSV in JSON, indem Sie die Aspose.Cells für die Python via .NET API verwenden.
keywords: Konvertieren Sie CVS in JSON, konvertieren Sie CSV in JSON in Python via NET, Python konvertieren CSV in JSON, CSV in JSON speichern
---

## **Konvertieren von CSV in JSON**

Aspose.Cells für Python via .NET unterstützt die Konvertierung von CSV in JSON. Dazu bietet die API die Klassen [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions) und [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility). Die Klasse [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions) bietet die Optionen für den Exportbereich nach JSON. Die Klasse [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions) hat die folgenden Eigenschaften.

- [**export_as_string**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/export_as_string/): Exportiert den Zeichenfolgenwert der Zellen in JSON.
- [**has_header_row**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/has_header_row/): Gibt an, ob der Bereich eine Kopfzeile enthält.
- [**indent**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/indent/): Gibt die Einrückung an.

Die Klasse [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility) exportiert das JSON unter Verwendung der Exportoptionen, die mit der Klasse [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions) festgelegt sind.

Der folgende Beispielcode zeigt die Verwendung der [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)- und [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)-Klassen zum Laden der [Quell-CSV-Datei](104398879.csv) und gibt die JSON-Ausgabe in der Konsole aus.

### **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.py" >}}

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
