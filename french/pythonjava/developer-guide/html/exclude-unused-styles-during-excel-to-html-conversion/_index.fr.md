---
title: Exclure les styles inutilisés lors de la conversion d'Excel en HTML
type: docs
weight: 30
url: /fr/python-java/exclude-unused-styles-during-excel-to-html-conversion/
---
## **Exclure les styles inutilisés lors de la conversion d'Excel en HTML**
Microsoft Les fichiers Excel peuvent contenir de nombreux styles inutilisés. Lorsque ces fichiers sont exportés au format HTML, les styles inutilisés sont également exportés. Il en résulte une augmentation de la taille du HTML de sortie. Aspose.Cells for Python via Java prend en charge l'exclusion de ces styles lors de la conversion du fichier Excel en HTML. Pour cela, le API fournit le[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles)propriété. Réglage de la valeur de[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) propriété à**Vrai** exclura tous les styles inutilisés du HTML de sortie.

La capture d'écran suivante montre les styles inutilisés dans le fichier HTML qui seront supprimés en définissant la valeur de[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) propriété à**Vrai**.

![tâche : image_autre_texte](HtmlSaveOptions-Exclude-Unused-Styles.png)

L'exemple de code suivant illustre la suppression des styles inutilisés lors de la conversion d'Excel en HTML.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExcludeUnusedStylesInExcelToHTML.py" >}}
