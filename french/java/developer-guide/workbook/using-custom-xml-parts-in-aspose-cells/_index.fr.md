---
title: Utilisation de pièces de XML personnalisées dans Aspose.Cells
type: docs
weight: 570
url: /fr/java/using-custom-xml-parts-in-aspose-cells/
---

{{% alert color="primary" %}} 

Les pièces de XML personnalisées sont les données XML stockées par différentes applications comme SharePoint etc. à l'intérieur du fichier excel. Ces données sont utilisées par différentes applications qui en ont besoin. Microsoft Excel n'utilise pas ces données, donc il n'y a pas d'interface graphique pour les ajouter. Vous pouvez visualiser ces données en changeant l'extension de **.xlsx** en **.zip** et en l'ouvrant avec **WinRAR**. Les données sont présentes à l'intérieur du dossier **customXml** comme le montre cette image.

![todo:image_alt_text](using-custom-xml-parts-in-aspose-cells_1.png)

Vous pouvez ajouter des parties XML personnalisées à l'aide d'Aspose.Cells via la méthode [Workbook.getContentTypeProperties().add()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add-java.lang.Object-)

{{% /alert %}} 
## **Utilisation de pièces de XML personnalisées dans Aspose.Cells**
Le code suivant utilise la méthode [Workbook.getContentTypeProperties().add()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add-java.lang.Object-) pour ajouter le **Book Catalog Xml** dont le nom est **BookStore**. L'image suivante montre le résultat de ce code. Comme vous pouvez le voir, le Book Catalog Xml est ajouté à l'intérieur du nœud BookStore, qui est le nom de cette propriété.

![todo:image_alt_text](using-custom-xml-parts-in-aspose-cells_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingCustomXmlParts-UsingCustomXmlParts.java" >}}
## **Article connexe**
{{% alert color="primary" %}} 

- [Ajout de propriétés personnalisées visibles dans le volet Informations sur le document](/cells/fr/java/adding-custom-properties-visible-inside-document-information-panel/)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
