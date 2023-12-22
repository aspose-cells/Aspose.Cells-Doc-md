---
title: Convertir CSV en JSON
type: docs
weight: 220
url: /fr/python-net/convert-csv-to-json/
description: Convertissez CSV en JSON en utilisant Aspose.Cells for Python via .NET API.
keywords: Convert CVS to JSON, Convert CSV to JSON in Python via NET, Python convert CSV to JSON, Save CSV to JSON
---
##  **Convertir CSV en JSON**

Aspose.Cells for Python via .NET prend en charge la conversion de CSV en JSON. Pour cela, le API fournit**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**et**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)** Des classes. Le**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**La classe fournit les options d'exportation de la plage vers JSON. La classe**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**la classe a les propriétés suivantes.

- *[export_as_string](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/export_as_string/)** : Ceci exporte la valeur de chaîne des cellules vers JSON.
- *[has_header_row](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/has_header_row/)** : Cela indique si la plage contient une ligne d'en-tête.
- *[retrait](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/indent/)** : Indique le retrait.

Le**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)**classe exporte le JSON en utilisant les options d'exportation définies avec le**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**classe.

L'exemple de code suivant illustre l'utilisation de**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**et**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)** classes pour charger le[fichier source CSV](104398879.csv)et imprime la sortie JSON dans la console.

###  **Exemple de code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.py" >}}

###  **Sortie console**
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