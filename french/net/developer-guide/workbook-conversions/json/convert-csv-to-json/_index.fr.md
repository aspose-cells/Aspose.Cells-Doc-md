---
title: Convertir CSV en JSON
type: docs
weight: 220
url: /fr/net/convert-csv-to-json/
description: Convertissez le fichier CSF en JSON en utilisant le simple à utiliser Aspose.Cells for .NET API.
keywords: Convert, Convert CVS to JSON, CSV to JSON, CSV, JSON, Convert CSV to JSON CSharp, c# code to convert CSV to JSON
---
## **Convertir CSV en JSON**

Aspose.Cells prend en charge la conversion de CSV en JSON. Pour cela, le API fournit**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**et**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)** Des classes. La**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**La classe fournit les options d'exportation de la plage vers JSON. La**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**classe a les propriétés suivantes.

- **[ExportAsString](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/exportasstring)**cela exporte la valeur de chaîne des cellules vers JSON.
- **[HasHeaderRow](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/hasheaderrow)**: Cela indique si la plage contient une ligne d'en-tête.
- **[Retrait](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/indent)**: Indique le retrait.

La**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**classe exporte le JSON en utilisant les options d'exportation définies avec la**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**classer.

L'exemple de code suivant illustre l'utilisation de**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**et**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**classes pour charger[fichier source CSV](104398879.csv)et imprime la sortie JSON dans la console.

### **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.cs" >}}

### **Sortie console**
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