---
title: Convertir CSV en JSON
type: docs
weight: 170
url: /fr/java/convert-csv-to-json/
---
## **Convertir CSV en JSON**

Aspose.Cells prend en charge la conversion de CSV en JSON. Pour cela, le API fournit[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)et[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)Des classes. La[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)La classe fournit les options d'exportation de la plage vers JSON. La[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)classe a les propriétés suivantes.

- [**Exporter en tant que chaîne**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#ExportAsString)cela exporte la valeur de chaîne des cellules vers JSON.
- [**HasHeaderRowHasHeaderRow**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#HasHeaderRow): Cela indique si la plage contient une ligne d'en-tête.
- [**Retrait**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#Indent): Indique le retrait.

La[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)classe exporte le JSON en utilisant les options d'exportation définies avec la[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)classer.

L'exemple de code suivant illustre l'utilisation de[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)et[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)classes pour charger[fichier source CSV](SampleCsv.csv)et imprime le[JSON](SampleJson_out.csv) sortie dans la console.

### **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.java" >}}

### **Sortie console**

[ { "id": 1, "language": "Java", "edition": "troisième", "author": "Herbert Schildt", "streetAddress": 126, "city": "San Jone", "état": "CA", "code postal": 394221 }, { "id": 2, "langue": "C++", "édition": "deuxième", "author": "EAAAA", "streetAddress": 126, "city": "San Jones", "state": "CA", "postalCode": 394221 }, { "id": 3 , "language": ".Net", "edition": "second", "author": "E.Balagurusamy", "streetAddress": 126, "city": "San Jone", " état": "CA", "code postal": 394221 } ]