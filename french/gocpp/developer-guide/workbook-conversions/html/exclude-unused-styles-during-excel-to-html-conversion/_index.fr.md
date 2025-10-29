---
title: Exclure les styles inutilisés lors de la conversion Excel en HTML avec Golang via C++
linktitle: Exclure les styles inutilisés
type: docs
weight: 30
url: /fr/go-cpp/exclude-unused-styles-during-excel-to-html-conversion/
description: Découvrez comment exclure les styles inutilisés lors de la conversion d Excel en HTML en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Les fichiers Microsoft Excel peuvent contenir de nombreux styles inutilisés. Lors de l'exportation du fichier Excel en format HTML, ces styles inutilisés sont également exportés, ce qui peut augmenter la taille du HTML. Vous pouvez exclure ces styles inutilisés lors de la conversion d'un fichier Excel en HTML en utilisant la propriété [**HtmlSaveOptions.GetExcludeUnusedStyles()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexcludeunusedstyles/). Lorsqu'elle est définie à **true**, tous les styles inutilisés sont exclus du HTML de sortie. La capture d'écran suivante montre un style inutilisé dans le HTML de sortie.

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Exclure les styles inutilisés lors de la conversion d'Excel en HTML**

Le code d'exemple ci-dessous crée un classeur et crée également un style nommé inutilisé. Comme la propriété [**HtmlSaveOptions.GetExcludeUnusedStyles()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexcludeunusedstyles/) est définie à **true**, ce style inutilisé ne sera pas exporté dans le [HTML de sortie](61767778.zip). Cependant, si vous la définissez à **false**, ce style inutilisé sera présent dans le HTML de sortie, que vous pouvez voir dans la balise HTML comme montré dans la capture d'écran ci-dessus.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExcludeUnusedStylesDuringExcelToHtmlConversion.go" >}}
