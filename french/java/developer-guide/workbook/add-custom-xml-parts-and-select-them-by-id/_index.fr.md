---
title: Ajouter des parties XML personnalisées et les sélectionner par ID
type: docs
weight: 10
url: /fr/java/add-custom-xml-parts-and-select-them-by-id/
---
## **Scénarios d'utilisation possibles**

Les parties XML personnalisées sont les données XML stockées dans les documents Excel Microsoft et utilisées par les applications qui les traitent. Il n'existe aucun moyen direct de les ajouter à l'aide de l'interface utilisateur Excel Microsoft pour le moment. Cependant, vous pouvez les ajouter par programme de différentes manières, par exemple en utilisant*VSTO*, utilisant*Aspose.Cells*etc. Veuillez utiliser[**Classeur.getCustomXmlParts().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add(java.lang.Object)) si vous souhaitez ajouter une partie XML personnalisée à l'aide de Aspose.Cells API. Vous pouvez également définir son ID à l'aide de la[**CustomXmlPart.IDCustomXmlPart.IDCustomXmlPart.IDCustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#ID)propriété. De même, si vous souhaitez sélectionner Custom XML Part by ID, vous pouvez utiliser[**Classeur.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID(java.lang.String)) méthode.

## **Ajouter des parties XML personnalisées et les sélectionner par ID**

L'exemple de code suivant ajoute d'abord quatre parties XML personnalisées à l'aide de[**Classeur.getCustomXmlParts().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add(java.lang.Object)) méthode. Il a ensuite défini leurs identifiants à l'aide[**CustomXmlPart.IDCustomXmlPart.IDCustomXmlPart.IDCustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#ID)propriété. Enfin, il trouve ou sélectionne l'une des parties XML personnalisées ajoutées à l'aide de[**Classeur.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID(java.lang.String)) méthode. Veuillez également consulter la sortie console du code ci-dessous pour référence.

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-AddCustomXMLPartsAndSelectThemByID.java" >}}

## **Sortie console**

{{< highlight "java" >}}

Found: CustomXmlPart ID Sport

{{< /highlight >}}
