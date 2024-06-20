---
title: Convertir JSON en CSV
type: docs
weight: 210
url: /fr/net/convert-json-to-csv/
---

## **Convertir JSON en CSV**

Aspose.Cells prend en charge la conversion de JSON simple ainsi que de JSON imbriqué en CSV. Pour cela, l'API fournit les classes [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) et [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility). La classe [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) fournit les options pour la disposition du JSON comme [**IgnoreArrayTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle) (ignore le titre si le tableau est une propriété d'un objet) ou [**ArrayAsTable**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable) (traite le tableau comme une table). La classe [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) traite le JSON en utilisant les options de disposition définies avec la classe [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions).

Le code d'exemple suivant démontre l'utilisation des classes [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) et [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) pour charger le [fichier JSON source](104398869.json) et générer le [fichier CSV en sortie](104398870.csv).

### **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.cs" >}}
