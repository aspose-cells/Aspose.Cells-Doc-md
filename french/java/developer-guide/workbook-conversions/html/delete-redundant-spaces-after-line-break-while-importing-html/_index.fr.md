---
title: Supprimer les espaces redondants après un saut de ligne lors de l'importation HTML
type: docs
weight: 620
url: /fr/java/delete-redundant-spaces-after-line-break-while-importing/
---
{{% alert color="primary" %}} 

 Veuillez utiliser[HtmlLoadOptions.DeleteRedundantSpaces](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#DeleteRedundantSpaces) propriété et définissez-la**vrai** pour supprimer tous les espaces redondants venant après la balise de saut de ligne. Par défaut, cette propriété est**faux**et les espaces redondants sont conservés dans les fichiers Excel de sortie.

{{% /alert %}} 
## **Effet de la définition de la propriété HtmlLoadOptions.DeleteRedundantSpaces sur false et true**
 La capture d'écran suivante montre l'effet de la définition de cette propriété sur**faux** et**vrai**.

![tâche : image_autre_texte](delete-redundant-spaces-after-line-break-while-importing-html_1.png)
## **Supprimer les espaces redondants après un saut de ligne lors de l'importation HTML**
 L'exemple de code suivant montre l'utilisation de[HtmlLoadOptions.DeleteRedundantSpaces](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#DeleteRedundantSpaces) la propriété. Veuillez le régler**vrai** ou alors**faux** pour obtenir la sortie comme indiqué dans la capture d'écran ci-dessus.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-DeleteRedundantSpacesFromHtml-1.java" >}}
