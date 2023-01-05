---
title: Exclure les styles inutilisés lors de la conversion d'Excel en HTML
type: docs
weight: 30
url: /fr/net/exclude-unused-styles-during-excel-to-html-conversion/
---
## **Scénarios d'utilisation possibles**

Microsoft Le fichier Excel peut contenir de nombreux styles inutilisés. Lorsque vous exportez le fichier Excel au format HTML, ces styles inutilisés sont également exportés. Cela peut augmenter la taille de HTML. Vous pouvez exclure les styles inutilisés lors de la conversion du fichier Excel en HTML à l'aide de la[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/excludeunusedstyles) la propriété. Lorsque vous le réglez**vrai**, tous les styles inutilisés sont exclus de la sortie HTML. La capture d'écran suivante affiche un exemple de style inutilisé dans la sortie HTML.

![tâche : image_autre_texte](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Exclure les styles inutilisés lors de la conversion d'Excel en HTML**

L'exemple de code suivant crée un classeur et crée également un style nommé inutilisé. Depuis le[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/excludeunusedstyles) est réglé sur**vrai** , ce style nommé inutilisé ne sera pas exporté vers[sortie HTML](61767778.zip) . Mais si vous le réglez sur**faux**, alors ce style inutilisé sera présent dans la sortie HTML que vous pouvez ensuite voir dans le balisage HTML comme indiqué dans la capture d'écran ci-dessus.

## **Exemple de code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExcludeUnusedStylesInExcelToHTML.cs" >}}
