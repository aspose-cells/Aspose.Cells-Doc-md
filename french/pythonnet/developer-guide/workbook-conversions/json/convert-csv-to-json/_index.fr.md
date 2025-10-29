---
title: Convertir un fichier CSV en JSON
type: docs
weight: 220
url: /fr/python-net/convert-csv-to-json/
description: Convertir un CSV en JSON en utilisant l API Aspose.Cells pour Python via .NET.
keywords: Convertir CVS en JSON, Convertir un CSV en JSON en Python via NET, Convertir un CSV en JSON en Python, Enregistrer un CSV en JSON
---

## **Convertir CSV en JSON**

Aspose.Cells pour Python via .NET prend en charge la conversion de CSV en JSON. Pour cela, l'API fournit les classes [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions) et [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility). La classe [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions) fournit les options pour exporter la plage en JSON. La classe [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions) a les propriétés suivantes.

- [**export_as_string**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/export_as_string/): Cela exporte la valeur de chaîne des cellules au format JSON.
- [**has_header_row**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/has_header_row/): Indique si la plage contient une ligne d'en-tête.
- [**indent**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/indent/): Indique l'indentation.

La classe [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility) exporte le JSON en utilisant les options d'export définies avec la classe [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions).

Le code d'exemple suivant démontre l'utilisation des classes [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions) et [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility) pour charger le [fichier CSV source](104398879.csv) et afficher la sortie JSON dans la console.

### **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.py" >}}

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
{{< app/cells/assistant language="python-net" >}}
