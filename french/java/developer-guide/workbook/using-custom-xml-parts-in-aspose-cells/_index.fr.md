---
title: Utilisation de parties XML personnalisées dans Aspose.Cells
type: docs
weight: 570
url: /fr/java/using-custom-xml-parts-in-aspose-cells/
---
{{% alert color="primary" %}} 

 Les parties XML personnalisées sont les données XML stockées par différentes applications telles que SharePoint, etc. dans le fichier Excel. Ces données sont consommées par différentes applications qui en ont besoin. Microsoft Excel n'utilise pas ces données, il n'y a donc pas d'interface graphique pour les ajouter. Vous pouvez afficher ces données en modifiant l'extension de**.xlsx** dans**.Zip *: français** puis en l'ouvrant avec**WinRAR** . Les données sont présentes à l'intérieur du**customXml** dossier comme indiqué sur cette image.

![tâche : image_autre_texte](using-custom-xml-parts-in-aspose-cells_1.png)

 Vous pouvez ajouter des parties XML personnalisées en utilisant Aspose.Cells via le[Classeur.getContentTypeProperties().add()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add\(java.lang.Object\)) méthode.

{{% /alert %}} 
## **Utilisation de parties XML personnalisées dans Aspose.Cells**
 L'exemple de code suivant utilise[Classeur.getContentTypeProperties().add()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add\(java.lang.Object\) ) et ajoute la méthode**Catalogue de livres Xml** et son nom est**Librairie**L'image suivante montre le résultat de ce code. Comme vous pouvez le voir, Book Catalog Xml est ajouté à l'intérieur du nœud BookStore qui est le nom de cette propriété.

![tâche : image_autre_texte](using-custom-xml-parts-in-aspose-cells_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingCustomXmlParts-UsingCustomXmlParts.java" >}}
## **Article associé**
{{% alert color="primary" %}} 

- [Ajout de propriétés personnalisées visibles dans le panneau Informations sur le document](/cells/fr/java/adding-custom-properties-visible-inside-document-information-panel/)

{{% /alert %}}
