---
title: Exclure les styles inutilisés lors de la conversion d Excel en HTML
type: docs
weight: 30
url: /fr/python-java/exclude-unused-styles-during-excel-to-html-conversion/
---

## **Exclure les styles inutilisés lors de la conversion d'Excel en HTML**
Les fichiers Microsoft Excel peuvent contenir de nombreux styles inutilisés. Lorsque ces fichiers sont exportés au format HTML, les styles inutilisés sont également exportés. Cela entraîne une augmentation de la taille du fichier HTML de sortie. Aspose.Cells pour Python via Java prend en charge l'exclusion de ces styles lors de la conversion du fichier Excel en HTML. Pour cela, l'API fournit la propriété [HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles). En définissant la valeur de la propriété [HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) à **True**, tous les styles inutilisés seront exclus du fichier HTML de sortie.

La capture d'écran suivante montre les styles inutilisés dans le fichier HTML qui seront supprimés en définissant la valeur de la propriété [HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) à **True**.

![todo:image_alt_text](HtmlSaveOptions-Exclude-Unused-Styles.png)

Le code d'exemple suivant démontre la suppression des styles inutilisés lors de la conversion d'Excel en HTML.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExcludeUnusedStylesInExcelToHTML.py" >}}
