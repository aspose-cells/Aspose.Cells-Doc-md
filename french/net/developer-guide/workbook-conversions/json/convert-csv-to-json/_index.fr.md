---
title: Convertir un fichier CSV en JSON
type: docs
weight: 220
url: /fr/net/convert-csv-to-json/
description: Convertir un fichier CSF en JSON en utilisant l API simple à utiliser Aspose.Cells for .NET.
keywords: Convertir, Convertir CVS en JSON, CSV en JSON, CSV, JSON, Convertir CSV en JSON CSharp, code c# pour convertir CSV en JSON
---

## **Convertir CSV en JSON**

Aspose.Cells prend en charge la conversion de CSV en JSON. Pour cela, l'API fournit les classes [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions) et [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility). La classe [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions) fournit les options pour exporter la plage vers JSON. La classe [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions) a les propriétés suivantes.

- [**ExportAsString**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/exportasstring): Cela exporte la valeur de chaîne des cellules au format JSON.
- [**HasHeaderRow**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/hasheaderrow): Indique si la plage contient une ligne d'en-tête.
- [**Indent**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/indent): Indique l'indentation.

La classe [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) exporte le JSON en utilisant les options d'export définies avec la classe [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions).

Le code d'exemple suivant démontre l'utilisation des classes [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions) et [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) pour charger le [fichier CSV source](104398879.csv) et afficher la sortie JSON dans la console.

### **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.cs" >}}

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
