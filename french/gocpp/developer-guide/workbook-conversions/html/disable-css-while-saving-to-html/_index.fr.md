---
title: Désactiver CSS lors de l enregistrement en HTML avec Golang via C++
linktitle: Désactiver le CSS lors de l enregistrement en HTML
type: docs
weight: 320
url: /fr/go-cpp/disable-css-while-saving-to-html/
description: Apprenez comment désactiver CSS lors de l enregistrement de fichiers Excel en HTML en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

 Lorsque vous enregistrez votre fichier Excel en HTML à page unique, généralement les éléments CSS seront intégrés dans le fichier HTML et situés dans la section HEAD. Si vous attachez ce fichier comme contenu/corps d’un email, les éléments CSS seront supprimés par la plupart des clients de messagerie, ce qui entraînera un rendu incorrect. La version 24.12 d'Aspose.Cells introduit une option permettant de désactiver de manière optionnelle CSS, permettant aux styles d’être appliqués directement dans les éléments HTML eux-mêmes. Si vous souhaitez définir le HTML comme contenu/corps de l’email, veuillez utiliser la propriété [**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisablecss/) et la définir à **true**.

## **Désactiver le CSS lors de l'enregistrement en HTML**

 Le code d'exemple suivant montre l’utilisation de la propriété [**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisablecss/).

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DisableCssWhileSavingToHtml.go" >}}
