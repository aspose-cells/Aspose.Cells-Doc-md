---
title: Wandeln Sie CSV in JSON um
type: docs
weight: 220
url: /de/net/convert-csv-to-json/
description: Konvertieren Sie die CSF-Datei in JSON, indem Sie das einfach zu verwendende Aspose.Cells for .NET API verwenden.
keywords: Convert, Convert CVS to JSON, CSV to JSON, CSV, JSON, Convert CSV to JSON CSharp, c# code to convert CSV to JSON
---
## **Wandeln Sie CSV in JSON um**

Aspose.Cells unterstützt die Umwandlung von CSV in JSON. Dafür sorgt die API**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**und**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)** Klassen. Das**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**Klasse bietet die Optionen für den Exportbereich bis JSON. Die**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**Klasse hat die folgenden Eigenschaften.

- **[ExportAsString](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/exportasstring)**: Dies exportiert den Zeichenfolgenwert der Zellen nach JSON.
- **[HasHeaderRow](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/hasheaderrow)**: Gibt an, ob der Bereich eine Kopfzeile enthält.
- **[Einzug](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/indent)**: Gibt den Einzug an.

Das**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**Die Klasse exportiert die JSON unter Verwendung der mit der eingestellten Exportoptionen**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**Klasse.

Das folgende Codebeispiel veranschaulicht die Verwendung von**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**und**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)** Klassen zum Laden der[Quelldatei CSV](104398879.csv)und druckt die Ausgabe JSON in der Konsole.

### **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.cs" >}}

### **Konsolenausgabe**
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