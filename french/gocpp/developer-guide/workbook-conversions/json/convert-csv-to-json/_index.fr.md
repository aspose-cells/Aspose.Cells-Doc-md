---
title: Convertir CSV en JSON avec Golang via C++
linktitle: Convertir un fichier CSV en JSON
type: docs
weight: 220
url: /fr/go-cpp/convert-csv-to-json/
description: Convertir un fichier CSV en JSON en utilisant l’API simple Aspose.Cells for C++.
keywords: Convertir, Convertir CSV en JSON, CSV en JSON, CSV, JSON, Convertir CSV en JSON C++, code C++ pour convertir CSV en JSON
---

## **Convertir CSV en JSON**

Aspose.Cells supporte la conversion de CSV en JSON. À cet effet, l’API fournit les classes [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/) et [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/). La classe [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/) offre les options pour exporter une plage en JSON. La classe [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/) possède les propriétés suivantes.

- [**GetExportAsString()**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/getexportasstring/): Cela exporte la valeur de chaîne des cellules au format JSON.
- [**GetHasHeaderRow()**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/gethasheaderrow/) : Indique si la plage contient une ligne d’en-tête.
- [**GetIndent()**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/getindent/) : Indique l’indentation.

La classe [**JsonUtility**](https://reference.aspose.com/cells/go-cpp/jsonutility/) exporte le JSON en utilisant les options d’exportation configurées avec la classe [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/).

Le code suivant démontre l’utilisation des classes [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/) et [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) pour charger le fichier CSV [source](104398879.csv) et affiche la sortie JSON dans la console.

### **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertCsvToJson.go" >}}
### **Sortie console**
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
