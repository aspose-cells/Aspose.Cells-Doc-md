---
title: Exclure les styles inutilisés lors de la conversion d Excel en HTML
type: docs
weight: 30
url: /fr/java/exclude-unused-styles-during-excel-to-html-conversion/
---

## **Scénarios d'utilisation possibles**

Le fichier Microsoft Excel peut contenir de nombreux styles inutilisés. Lorsque vous exportez le fichier Excel au format HTML, ces styles inutilisés sont également exportés. Cela peut augmenter la taille du HTML. Vous pouvez exclure les styles inutilisés lors de la conversion du fichier Excel en HTML en utilisant la propriété [**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExcludeUnusedStyles). Lorsque vous la définissez sur **true**, tous les styles inutilisés sont exclus du HTML de sortie. La capture d'écran suivante affiche un exemple de style inutilisé dans le HTML de sortie.

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Exclure les styles inutilisés lors de la conversion d'Excel en HTML**

Le code d'échantillon suivant crée un classeur et crée également un style nommé inutilisé. Puisque [**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExcludeUnusedStyles) est défini sur **true**, ce style nommé inutilisé ne sera pas exporté vers le [HTML de sortie](61767781.zip). Mais si vous le définissez sur **false**, ce style inutilisé sera présent dans le HTML de sortie que vous pourrez ensuite voir dans le marquage HTML comme montré dans la capture d'écran ci-dessus.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExcludeUnusedStylesInExcelToHTML.java" >}}
{{< app/cells/assistant language="java" >}}
