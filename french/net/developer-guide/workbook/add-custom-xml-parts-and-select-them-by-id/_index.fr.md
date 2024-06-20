---
title: Ajouter des parties XML personnalisées et les sélectionner par ID
type: docs
weight: 70
url: /fr/net/add-custom-xml-parts-and-select-them-by-id/
---

## **Scénarios d'utilisation possibles**

Les Parties XML personnalisées sont les données XML stockées à l'intérieur des documents Microsoft Excel et utilisées par les applications qui y traitent. Il n'y a actuellement aucun moyen direct de les ajouter à l'aide de l'interface utilisateur de Microsoft Excel. Cependant, vous pouvez les ajouter de manière programmatique de diverses manières, par exemple en utilisant VSTO, en utilisant Aspose.Cells, etc. Veuillez utiliser la méthode [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add) si vous souhaitez ajouter une Partie XML personnalisée en utilisant l'API Aspose.Cells. Vous pouvez également définir son identifiant en utilisant la propriété [**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id). De même, si vous souhaitez sélectionner une Partie XML personnalisée par ID, vous pouvez utiliser la méthode [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid).

## **Ajouter des parties XML personnalisées et les sélectionner par ID**

Le code d'exemple suivant ajoute d'abord quatre Parties XML personnalisées en utilisant la méthode [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add). Ensuite, il définit leurs identifiants à l'aide de la propriété [**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id). Enfin, il trouve ou sélectionne l'une des Parties XML personnalisées ajoutées en utilisant la méthode [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid). Veuillez également consulter la sortie console du code donné ci-dessous pour référence.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-AddCustomXMLPartsAndSelectThemByID.cs" >}}

## **Sortie console**

{{< highlight java >}}

 Found: CustomXmlPart ID Sport

{{< /highlight >}}
