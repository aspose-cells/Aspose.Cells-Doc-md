---
title: Ajouter des parties XML personnalisées et les sélectionner par ID
type: docs
weight: 70
url: /fr/net/add-custom-xml-parts-and-select-them-by-id/
---
## **Scénarios d'utilisation possibles**

Les parties XML personnalisées sont les données XML stockées dans les documents Excel Microsoft et utilisées par les applications qui les traitent. Il n'existe aucun moyen direct de les ajouter à l'aide de l'interface utilisateur Excel Microsoft pour le moment. Cependant, vous pouvez les ajouter par programme de différentes manières, par exemple en utilisant VSTO, en utilisant Aspose.Cells, etc. Veuillez utiliser[**Classeur.CustomXmlParts.Add()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add)si vous souhaitez ajouter une partie XML personnalisée à l'aide de Aspose.Cells API. Vous pouvez également définir son ID à l'aide de la[**CustomXmlPart.IDCustomXmlPart.IDCustomXmlPart.IDCustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id)propriété. De même, si vous souhaitez sélectionner Custom XML Part by ID, vous pouvez utiliser[**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid)méthode.

## **Ajouter des parties XML personnalisées et les sélectionner par ID**

L'exemple de code suivant ajoute d'abord quatre parties XML personnalisées à l'aide de[**Classeur.CustomXmlParts.Add()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add)méthode. Il définit ensuite leurs identifiants à l'aide[**CustomXmlPart.IDCustomXmlPart.IDCustomXmlPart.IDCustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id) propriété. Enfin, il trouve ou sélectionne l'une des parties XML personnalisées ajoutées à l'aide de[**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid)méthode. Veuillez également consulter la sortie de la console du code ci-dessous pour référence.

## **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-AddCustomXMLPartsAndSelectThemByID.cs" >}}

## **Sortie console**

{{< highlight "java" >}}

 Found: CustomXmlPart ID Sport

{{< /highlight >}}
