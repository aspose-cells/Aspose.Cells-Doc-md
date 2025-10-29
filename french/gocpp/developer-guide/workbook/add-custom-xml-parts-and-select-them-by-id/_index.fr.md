---
title: Ajoutez des parties XML personnalisées et sélectionnez les par ID avec Golang via C++
linktitle: Ajouter des parties XML personnalisées et les sélectionner par ID
type: docs
weight: 70
url: /fr/go-cpp/add-custom-xml-parts-and-select-them-by-id/
description: Apprenez comment ajouter et sélectionner des parties XML personnalisées dans les fichiers Excel en utilisant Aspose.Cells avec Golang via C++.
---

## **Scénarios d'utilisation possibles**

Les parties XML personnalisées sont des données XML stockées à l'intérieur des documents Microsoft Excel et sont utilisées par des applications qui interagissent avec elles. Il n'existe actuellement aucun moyen direct de les ajouter via l'UI de Microsoft Excel. Cependant, vous pouvez les ajouter de manière programmatique de plusieurs façons, comme en utilisant VSTO ou Aspose.Cells. Utilisez la méthode [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/go-cpp/customxmlpartcollection/add/) pour ajouter une partie XML personnalisée via l'API Aspose.Cells. Vous pouvez également définir son ID en utilisant la propriété [**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/). De même, si vous souhaitez sélectionner une partie XML personnalisée par ID, vous pouvez utiliser la méthode [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/selectbyid/).

## **Ajouter des parties XML personnalisées et les sélectionner par ID**

Le code exemple suivant ajoute d'abord quatre parties XML personnalisées en utilisant la méthode [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/go-cpp/customxmlpartcollection/add/). Ensuite, il définit leurs IDs en utilisant la propriété [**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/). Enfin, il trouve ou sélectionne l'une des parties XML ajoutées en utilisant la méthode [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/selectbyid/). Veuillez également consulter la sortie de la console ci-dessous pour référence.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddCustomXmlPartsAndSelectThemById.go" >}}
## **Sortie console**

{{< highlight java >}}
Found: CustomXmlPart ID Sport
{{< /highlight >}}
