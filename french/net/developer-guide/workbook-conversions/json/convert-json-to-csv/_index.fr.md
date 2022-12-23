---
title: Convertir JSON en CSV
type: docs
weight: 210
url: /fr/net/convert-json-to-csv/
---
## **Convertir JSON en CSV**

Aspose.Cells prend en charge la conversion de JSON simples et imbriqués en CSV. Pour cela, le API fournit**[JsonLayoutOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)** et**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)** Des classes. Le**[JsonLayoutOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)**La classe fournit les options pour la mise en page JSON comme**[IgnoreArrayTitle](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle)**(ignore le titre si le tableau est une propriété d'un objet) ou**[ArrayAsTable](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable)**(traite le tableau comme une table). Le**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**traite le JSON en utilisant les options de mise en page définies avec la**[JsonLayoutOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)**classe.

L'exemple de code suivant illustre l'utilisation de**[JsonLayoutOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)**et**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)** classes pour charger[fichier source JSON](104398869.json) et génère le[fichier de sortie CSV](104398870.csv).

### **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.cs" >}}
