---
title: Convertir JSON en CSV
type: docs
weight: 160
url: /fr/java/convert-json-to-csv/
---
Aspose.Cells prend en charge la conversion de JSON simples et imbriqués en CSV. Pour cela, le API fournit[**JsonLayoutOptionsJsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)et[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)Des classes. Le[**JsonLayoutOptionsJsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)La classe fournit les options pour la mise en page JSON comme[**IgnoreArrayTitleIgnoreArrayTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle)(ignore le titre si le tableau est une propriété d'un objet) ou[**TableauCommeTable**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable)(traite le tableau comme une table). Le[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)traite le JSON en utilisant les options de mise en page définies avec la[**JsonLayoutOptionsJsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)classe.

L'exemple de code suivant illustre l'utilisation de[**JsonLayoutOptionsJsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)et[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)classes pour charger[fichier source JSON](SampleJson.json)et génère le[fichier de sortie CSV](SampleJson_out.csv).

## Exemple de code

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.java" >}}
