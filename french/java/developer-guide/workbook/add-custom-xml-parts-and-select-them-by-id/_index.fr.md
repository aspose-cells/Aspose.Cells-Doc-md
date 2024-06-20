---
title: Ajouter des parties XML personnalisées et les sélectionner par ID
type: docs
weight: 10
url: /fr/java/add-custom-xml-parts-and-select-them-by-id/
---

## **Scénarios d'utilisation possibles**

Les Custom XML Parts sont les données XML stockées à l'intérieur des documents Microsoft Excel et sont utilisées par les applications qui les manipulent. Il n'y a actuellement aucun moyen direct de les ajouter à l'aide de l'interface utilisateur de Microsoft Excel. Cependant, vous pouvez les ajouter de manière programmée de différentes façons, par exemple en utilisant *VSTO*, en utilisant *Aspose.Cells* etc. Utilisez la méthode [**Workbook.getCustomXmlParts().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add(java.lang.Object)) si vous souhaitez ajouter des Custom XML Part en utilisant l'API Aspose.Cells. Vous pouvez également définir son ID, en utilisant la propriété [**CustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#ID). De même, si vous souhaitez sélectionner un Custom XML Part par ID, vous pouvez utiliser la méthode [**Workbook.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID(java.lang.String)).

## **Ajouter des parties XML personnalisées et les sélectionner par ID**

Le code d'exemple suivant ajoute d'abord quatre Custom XML Parts en utilisant la méthode [**Workbook.getCustomXmlParts().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add(java.lang.Object)). Ensuite, il définit leurs IDs en utilisant la propriété [**CustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#ID). Enfin, il trouve ou sélectionne l’une des Custom XML Part ajoutées en utilisant la méthode [**Workbook.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID(java.lang.String)). Veuillez également consulter la sortie de console du code ci-dessous pour référence.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-AddCustomXMLPartsAndSelectThemByID.java" >}}

## **Sortie console**

{{< highlight java >}}

Found: CustomXmlPart ID Sport

{{< /highlight >}}
