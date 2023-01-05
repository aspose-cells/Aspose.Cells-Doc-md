---
title: Converti CSV in JSON
type: docs
weight: 220
url: /it/net/convert-csv-to-json/
description: Converti il file CSF in JSON utilizzando il semplice da usare Aspose.Cells for .NET API.
keywords: Convert, Convert CVS to JSON, CSV to JSON, CSV, JSON, Convert CSV to JSON CSharp, c# code to convert CSV to JSON
---
## **Converti CSV in JSON**

Aspose.Cells supporta la conversione da CSV a JSON. Per questo, API fornisce**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**e**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)** classi. Il**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**class fornisce le opzioni per l'esportazione dell'intervallo a JSON. Il**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**class ha le seguenti proprietà.

- **[Esporta come stringa](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/exportasstring)**: Questo esporta il valore stringa delle celle in JSON.
- **[HasHeaderRow](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/hasheaderrow)**: Indica se l'intervallo contiene una riga di intestazione.
- **[Rientro](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/indent)**: Indica il rientro.

Il**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**class esporta lo JSON utilizzando le opzioni di esportazione impostate con il file**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**classe.

L'esempio di codice seguente illustra l'utilizzo di**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**e**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)** classi per caricare il file[fonte CSV file](104398879.csv)e stampa l'output JSON nella console.

### **Codice d'esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.cs" >}}

### **Uscita console**
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