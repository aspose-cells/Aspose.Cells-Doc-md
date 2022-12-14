---
title: Convertir JSON en CSV
type: docs
weight: 160
url: /fr/java/convert-json-to-csv/
---
Aspose.Cells prend en charge la conversion de JSON simple et imbriqué en CSV. Pour cela, le API fournit[**JsonLayoutOptionsJsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)et[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)Des classes. La[**JsonLayoutOptionsJsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)La classe fournit les options pour la mise en page JSON comme[**IgnoreArrayTitleIgnoreArrayTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle)(ignore le titre si le tableau est une propriété d'un objet) ou[**TableauCommeTable**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable)(traite le tableau comme une table). La[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)traite le JSON à l'aide des options de mise en page définies avec la[**JsonLayoutOptionsJsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)classer.

L'exemple de code suivant illustre l'utilisation de[**JsonLayoutOptionsJsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)et[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)classes pour charger[fichier JSON source](SampleJson.json)et génère le[fichier CSV de sortie](SampleJson_out.csv).

## Exemple de code

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.java" >}}
