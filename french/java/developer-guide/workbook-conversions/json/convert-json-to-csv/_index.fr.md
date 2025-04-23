---
title: Convertir JSON en CSV
type: docs
weight: 160
url: /fr/java/convert-json-to-csv/
---

Aspose.Cells prend en charge la conversion de JSON simple ainsi que JSON imbriqué en CSV. Pour cela, l'API fournit les classes [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) et [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility). La classe [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) offre des options pour la disposition du JSON comme [**IgnoreArrayTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle) (ignore le titre si le tableau est une propriété d'un objet) ou [**ArrayAsTable**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable) (traite le tableau comme un tableau). La classe [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) traite le JSON en utilisant les options de disposition définies avec la classe [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions).

L'exemple de code suivant démontre l'utilisation des classes [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) et [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) pour charger le [fichier JSON source](SampleJson.json) et générer le [fichier CSV de sortie](SampleJson_out.csv).

## Code d'exemple

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.java" >}}
{{< app/cells/assistant language="java" >}}
