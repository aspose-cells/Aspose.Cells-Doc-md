---
title: Convertir JSON en CSV avec Golang via C++
linktitle: Convertir JSON en CSV
type: docs
weight: 210
url: /fr/go-cpp/convert-json-to-csv/
description: Apprenez comment convertir JSON en CSV en utilisant Aspose.Cells for C++ avec des exemples JSON simples et imbriqués.
---

## **Convertir JSON en CSV**

Aspose.Cells prend en charge la conversion de JSON simple ainsi que de JSON imbriqué en CSV. Pour cela, l'API fournit les classes [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/) et [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/). La classe [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/) offre les options pour la disposition JSON comme [**SetIgnoreTitle**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/setignoretitle/) (ignore le titre si le tableau est une propriété d'un objet) ou [**GetArrayAsTable()**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/getarrayastable/) (traite le tableau comme une table). La classe [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) traite le JSON en utilisant les options de disposition définies avec la classe [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/).

L'exemple de code suivant montre l'utilisation des classes [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/) et [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) pour charger le fichier JSON source et générer le fichier CSV de sortie.

### **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertJsonToCsv.go" >}}
