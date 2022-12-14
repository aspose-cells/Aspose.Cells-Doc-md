---
title: Exclure les styles inutilisés lors de la conversion d'Excel en HTML
type: docs
weight: 30
url: /fr/java/exclude-unused-styles-during-excel-to-html-conversion/
---
## **Scénarios d'utilisation possibles**

Microsoft Le fichier Excel peut contenir de nombreux styles inutilisés. Lorsque vous exportez le fichier Excel au format HTML, ces styles inutilisés sont également exportés. Cela peut augmenter la taille du HTML. Vous pouvez exclure les styles inutilisés lors de la conversion du fichier Excel en HTML à l'aide de la[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExcludeUnusedStyles)propriété. Lorsque vous le réglez**vrai**tous les styles inutilisés sont exclus du HTML de sortie. La capture d'écran suivante affiche un exemple de style inutilisé dans le code HTML de sortie.

![tâche : image_autre_texte](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Exclure les styles inutilisés lors de la conversion d'Excel en HTML**

L'exemple de code suivant crée un classeur et crée également un style nommé inutilisé. Depuis le[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExcludeUnusedStyles)est réglé sur**vrai**, donc ce style nommé inutilisé ne sera pas exporté vers[sortie HTML](61767781.zip). Mais si vous le réglez**faux**, alors ce style inutilisé sera présent dans le HTML de sortie que vous pourrez ensuite voir dans le balisage HTML, comme indiqué dans la capture d'écran ci-dessus.

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExcludeUnusedStylesInExcelToHTML.java" >}}
