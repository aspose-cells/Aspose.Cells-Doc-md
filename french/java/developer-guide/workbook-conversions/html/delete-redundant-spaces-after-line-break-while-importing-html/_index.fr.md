---
title: Supprimez les espaces redondants après un saut de ligne lors de l importation du HTML
type: docs
weight: 620
url: /fr/java/delete-redundant-spaces-after-line-break-while-importing/
---

{{% alert color="primary" %}} 

Veuillez utiliser la propriété [HtmlLoadOptions.DeleteRedundantSpaces](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#DeleteRedundantSpaces) et la définir sur **true** pour supprimer tous les espaces redondants après la balise de saut de ligne. Par défaut, cette propriété est **false** et les espaces redondants sont conservés dans les fichiers Excel de sortie.

{{% /alert %}} 
## **Effet de définir la propriété HtmlLoadOptions.DeleteRedundantSpaces sur false et true**
La capture d'écran suivante montre l'effet de définir cette propriété sur **false** et **true**.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)
## **Supprimer les espaces redondants après un saut de ligne lors de l'importation d'HTML**
L'exemple de code suivant montre l'utilisation de la propriété [HtmlLoadOptions.DeleteRedundantSpaces](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#DeleteRedundantSpaces). Veuillez la définir sur **true** ou **false** pour obtenir le résultat montré dans la capture d'écran ci-dessus.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-DeleteRedundantSpacesFromHtml-1.java" >}}
{{< app/cells/assistant language="java" >}}
