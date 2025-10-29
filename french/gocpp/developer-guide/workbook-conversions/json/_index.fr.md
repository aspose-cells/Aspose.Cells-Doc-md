---
title: Convertir le classeur en JSON avec Golang via C++
linktitle: Convertir le classeur en JSON
type: docs
weight: 300
url: /fr/go-cpp/convert-workbook-to-json/
description: Apprenez à convertir les classeurs Excel en format JSON en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells supporte la conversion d’un classeur en fichier JSON (JavaScript Object Notation).

{{% /alert %}}

## **Convertir un classeur Excel en JSON**

L'API Aspose.Cells offre la prise en charge de la conversion des feuilles de calcul en format JSON. Pour exporter le classeur en JSON, passez [**SaveFormat::Json**](https://reference.aspose.com/cells/go-cpp/saveformat/) comme second paramètre de la méthode [**Workbook::Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). Vous pouvez également utiliser la classe [**JsonSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/jsonsaveoptions/) pour spécifier des paramètres supplémentaires lors de l'exportation de la feuille de calcul en JSON.

L'exemple de code ci-dessous montre comment exporter la feuille active en JSON en utilisant le membre d'énumération [**SaveFormat::Json**](https://reference.aspose.com/cells/go-cpp/saveformat/). Veuillez voir le code pour convertir [fichier source](book1.xlsx) en [fichier JSON de sortie](book1.json) généré par le code à titre de référence.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Json.go" >}}
## **Sujets avancés**
- [Convertir CSV en JSON](/cells/fr/cpp/convert-csv-to-json/)
- [Convertir Excel en JSON](/cells/fr/cpp/convert-excel-to-json/)
- [Convertir JSON en CSV](/cells/fr/cpp/convert-json-to-csv/)
- [Convertir JSON en Excel](/cells/fr/cpp/convert-json-to-excel/)
