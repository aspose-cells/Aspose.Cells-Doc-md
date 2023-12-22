---
title: Convertire CSV in JSON
type: docs
weight: 220
url: /it/python-net/convert-csv-to-json/
description: Convertire CSV in JSON utilizzando Aspose.Cells for Python via .NET API.
keywords: Convert CVS to JSON, Convert CSV to JSON in Python via NET, Python convert CSV to JSON, Save CSV to JSON
---
##  **Convertire CSV in JSON**

Aspose.Cells for Python via .NET supporta la conversione da CSV a JSON. Per questo, API fornisce**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**E**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)** classi. IL**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**fornisce le opzioni per esportare l'intervallo a JSON. Il file**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**la classe ha le seguenti proprietà.

- *[esporta_come_stringa](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/export_as_string/)**: esporta il valore stringa delle celle a JSON.
- *[has_header_row](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/has_header_row/)**: indica se l'intervallo contiene una riga di intestazione.
- *[trattino](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/indent/)**: Indica il rientro.

IL**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)**esporta lo JSON utilizzando le opzioni di esportazione impostate con il file**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**classe.

Nell'esempio di codice seguente viene illustrato l'utilizzo di**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**E**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)** classi per caricare il file[file sorgente CSV](104398879.csv)e stampa l'output JSON nella console.

###  **Codice d'esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.py" >}}

###  **Uscita della console**
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