---
title: Converte CSV in JSON con Golang tramite C++
linktitle: Converti CSV in JSON
type: docs
weight: 220
url: /it/go-cpp/convert-csv-to-json/
description: Converti file CSV in JSON usando l API semplice da usare Aspose.Cells for C++.
keywords: Converti, Converti CSV in JSON, CSV in JSON, CSV, JSON, Converti CSV in JSON C++, codice C++ per convertire CSV in JSON
---

## **Convertire CSV in JSON**

Aspose.Cells supporta la conversione di CSV in JSON. Per questo, l'API fornisce le classi [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/) e [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/). La classe [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/) fornisce le opzioni per esportare l'intervallo in JSON. La classe [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/) ha le seguenti proprietà.

- [**GetExportAsString()**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/getexportasstring/): Questo esporta il valore stringa delle celle in JSON.
- [**GetHasHeaderRow()**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/gethasheaderrow/): Indica se l'intervallo contiene una riga di intestazione.
- [**GetIndent()**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/getindent/): Indica l'indentazione.

La classe [**JsonUtility**](https://reference.aspose.com/cells/go-cpp/jsonutility/) esporta il JSON utilizzando le opzioni di esportazione impostate con la classe [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/).

Il seguente esempio di codice illustra l'uso delle classi [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/) e [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) per caricare il file CSV di origine e stampare l'output JSON nel console.

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertCsvToJson.go" >}}
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
