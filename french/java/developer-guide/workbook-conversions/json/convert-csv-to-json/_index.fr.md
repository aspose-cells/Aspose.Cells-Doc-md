---
title: Convertir un fichier CSV en JSON
type: docs
weight: 170
url: /fr/java/convert-csv-to-json/
---

## **Convertir CSV en JSON**

Aspose.Cells prend en charge la conversion du CSV en JSON. Pour cela, l'API fournit les classes [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) et [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility). La classe [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) fournit les options pour exporter la plage en JSON. La classe [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) a les propriétés suivantes.

- [**ExportAsString**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#ExportAsString): Cela exporte la valeur de chaîne des cellules au format JSON.
- [**HasHeaderRow**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#HasHeaderRow): Indique si la plage contient une ligne d'en-tête.
- [**Indent**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#Indent): Indique l'indentation.

La classe [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) exporte le JSON en utilisant les options d'export définies avec la classe [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions).

L'exemple de code suivant démontre l'utilisation des classes [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) et [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) pour charger le fichier CSV source (SampleCsv.csv) et afficher la sortie JSON (SampleJson_out.csv) dans la console.

### **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.java" >}}

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
