---
title: Converti CSV in JSON
type: docs
weight: 220
url: /it/python-net/convert-csv-to-json/
description: Converti CSV in JSON utilizzando Aspose.Cells per Python API via .NET.
keywords: Converti CVS in JSON, Converti CSV in JSON in Python via NET, Converti CSV in JSON in Python, Salva CSV in JSON
---

## **Convertire CSV in JSON**

Aspose.Cells per Python via .NET supporta la conversione di CSV in JSON. A questo scopo, l'API fornisce le classi [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions) e [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility). La classe [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions) fornisce le opzioni per esportare il range in JSON. La classe [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions) ha le seguenti proprietà.

- [**export_as_string**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/export_as_string/): Questo esporta il valore stringa delle celle in JSON.
- [**has_header_row**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/has_header_row/): Questo indica se l'intervallo contiene una riga di intestazione.
- [**indent**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/indent/): Indica l'indentazione.

La classe [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility) esporta il JSON utilizzando le opzioni di esportazione impostate con la classe [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions).

Il seguente esempio di codice dimostra l'uso delle classi [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions) e [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility) per caricare il [file CSV di origine](104398879.csv) e visualizza l'output JSON sulla console.

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.py" >}}

### **Output della console**
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
