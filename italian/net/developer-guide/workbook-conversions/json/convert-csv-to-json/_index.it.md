---
title: Converti CSV in JSON
type: docs
weight: 220
url: /it/net/convert-csv-to-json/
description: Converti il file CSF in JSON utilizzando la semplice API Aspose.Cells for .NET semplice da utilizzare.
keywords: Converti, Converti CVS in JSON, CSV in JSON, CSV, JSON, Converti CSV in JSON CSharp, codice c# per convertire CSV in JSON
---

## **Convertire CSV in JSON**

Aspose.Cells supporta la conversione di CSV in JSON. A tale scopo, l'API fornisce le classi [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions) e [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility). La classe [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions) fornisce le opzioni per esportare l'intervallo in JSON. La classe [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions) ha le seguenti proprietà.

- [**ExportAsString**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/exportasstring): Questo esporta il valore stringa delle celle in JSON.
- [**HasHeaderRow**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/hasheaderrow): Questo indica se l'intervallo contiene una riga di intestazione.
- [**Indent**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/indent): Indica l'indentazione.

La classe [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) esporta il JSON utilizzando le opzioni di esportazione impostate con la classe [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions).

Il seguente esempio di codice dimostra l'uso delle classi [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions) e [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) per caricare il [file CSV di origine](104398879.csv) e visualizza l'output JSON sulla console.

### **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.cs" >}}

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
{{< app/cells/assistant language="csharp" >}}
