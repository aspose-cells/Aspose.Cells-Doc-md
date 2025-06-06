---
title: Exclure les styles inutilisés lors de la conversion d Excel en HTML
type: docs
weight: 30
url: /fr/python-net/exclude-unused-styles-during-excel-to-html-conversion/
---

## **Scénarios d'utilisation possibles**

Le fichier Microsoft Excel peut contenir de nombreux styles inutilisés. Lorsque vous exportez le fichier Excel au format HTML, ces styles inutilisés sont également exportés. Cela peut augmenter la taille du HTML. Vous pouvez exclure les styles inutilisés lors de la conversion du fichier Excel en HTML en utilisant la propriété [**HtmlSaveOptions.exclude_unused_styles**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/exclude_unused_styles). Lorsque vous la définissez sur **true**, tous les styles inutilisés sont exclus du HTML de sortie. La capture d'écran suivante affiche un exemple de style inutilisé à l'intérieur du HTML de sortie.

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Exclure les styles inutilisés lors de la conversion d'Excel en HTML**

Le code d'exemple suivant crée un classeur et crée également un style nommé inutilisé. Puisque la propriété [**HtmlSaveOptions.exclude_unused_styles**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/exclude_unused_styles) est définie sur **true**, ce style nommé inutilisé ne sera pas exporté vers le [HTML de sortie](61767778.zip). Mais si vous la définissez sur **false**, alors ce style inutilisé sera présent à l'intérieur du HTML de sortie que vous pourrez ensuite voir dans le marquage HTML, comme le montre la capture d'écran ci-dessus.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExcludeUnusedStylesInExcelToHTML.py" >}}
