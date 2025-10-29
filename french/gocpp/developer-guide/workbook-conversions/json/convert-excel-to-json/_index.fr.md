---
title: Conversion d Excel en JSON avec Golang via C++
linktitle: Convertir Excel en JSON
type: docs
weight: 300
url: /fr/go-cpp/convert-excel-to-json/
description: Apprenez comment convertir un fichier Excel en JSON avec Aspose.Cells en utilisant C++.
keywords: Exporter le classeur au format JSON sans office 2013, office 2016, office 2019 et office 365
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge la conversion d'un classeur en fichier Json(JavaScript Object Notation).

{{% /alert %}}

## **Convertir un classeur Excel en JSON**

Inutile de vous demander comment convertir un classeur Excel en JSON, car la bibliothèque Aspose.Cells for C++ offre la meilleure solution. L’API Aspose.Cells supporte la conversion des feuilles de calcul en format JSON. Pour exporter le classeur en JSON, passez [**SaveFormat.Json**](https://reference.aspose.com/cells/go-cpp/saveformat/) comme deuxième paramètre de la méthode [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). Vous pouvez également utiliser la classe [**JsonSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/jsonsaveoptions/) pour spécifier des paramètres additionnels d’exportation de la feuille de calcul en JSON.

L’exemple de code ci-dessous montre comment exporter un classeur Excel en JSON. Veuillez consulter le code pour convertir le [fichier source](sample.xlsx) en fichier JSON généré par le code en référence.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertExcelToJson.go" >}}
L’exemple de code suivant utilisant la classe JsonSaveOptions pour spécifier des paramètres additionnels montre comment exporter un classeur Excel en JSON. Veuillez consulter le code pour convertir le [fichier source](sample.xlsx) en fichier JSON généré par le code en référence.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertExcelToJson-1.go" >}}
