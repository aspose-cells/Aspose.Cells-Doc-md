---
title: Masquer le contenu superposé avec CrossHideRight lors de la sauvegarde en HTML avec Golang via C++
linktitle: Masquer le contenu superposé avec CrossHideRight lors de l enregistrement en HTML
type: docs
weight: 100
url: /fr/go-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
description: Utilisez CrossHideRight avec Aspose.Cells en C++ pour masquer le contenu superposé lors de l’enregistrement en HTML.
---

## **Scénarios d'utilisation possibles**

Lorsque vous enregistrez votre fichier Excel en HTML, vous pouvez spécifier différents types de croisement pour les chaînes de cellules. Par défaut, Aspose.Cells génère du HTML selon Microsoft Excel, mais lorsque vous modifiez le type de croisement en [**CrossHideRight**](https://reference.aspose.com/cells/go-cpp/htmlcrosstype), il masque toutes les chaînes situées à droite de la cellule qui sont overlay ou qui se chevauchent avec la chaîne de la cellule.

## **Masquer le contenu superposé avec CrossHideRight lors de l'enregistrement en HTML**

Le code d’exemple suivant charge le [fichier Excel d'exemple](64716894.xlsx) et l’enregistre en [HTML de sortie](64716893.zip) après avoir réglé [**HtmlSaveOptions.GetHtmlCrossStringType()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/gethtmlcrossstringtype/) comme [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype). La capture d’écran explique comment [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype) influence le HTML de sortie par rapport à la sortie par défaut.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HidingOverlaidContentWithCrosshiderightWhileSavingToHtml.go" >}}
