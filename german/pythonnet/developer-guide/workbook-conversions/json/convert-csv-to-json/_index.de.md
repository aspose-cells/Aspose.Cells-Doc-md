---
title: Konvertieren Sie CSV in JSON
type: docs
weight: 220
url: /de/python-net/convert-csv-to-json/
description: Konvertieren Sie CSV in JSON, indem Sie Aspose.Cells for Python via .NET API verwenden.
keywords: Convert CVS to JSON, Convert CSV to JSON in Python via NET, Python convert CSV to JSON, Save CSV to JSON
---
##  **Konvertieren Sie CSV in JSON**

Aspose.Cells for Python via .NET unterstützt die Konvertierung von CSV in JSON. Dafür sorgt die API**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**Und**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)** Klassen. Der**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**Die Klasse bietet die Optionen zum Exportieren des Bereichs nach JSON. Die**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**Die Klasse hat die folgenden Eigenschaften.

- *[export_as_string](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/export_as_string/)**: Dadurch wird der Zeichenfolgenwert der Zellen nach JSON exportiert.
- *[has_header_row](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/has_header_row/)**: Dies gibt an, ob der Bereich eine Kopfzeile enthält.
- *[Einzug](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/indent/)**: Gibt den Einzug an.

Der**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)**Die Klasse exportiert JSON mithilfe der Exportoptionen, die mit festgelegt wurden**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**Klasse.

Das folgende Codebeispiel demonstriert die Verwendung von**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**Und**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)** Klassen zum Laden der[Quelldatei CSV](104398879.csv)und gibt die Ausgabe JSON in der Konsole aus.

###  **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.py" >}}

###  **Konsolenausgabe**
```json
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
```