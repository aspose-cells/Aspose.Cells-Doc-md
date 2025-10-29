---
title: Définir la police par défaut lors du rendu de la feuille de calcul en HTML avec Golang via C++
linktitle: Définir la police par défaut lors du rendu de la feuille de calcul en HTML
type: docs
weight: 370
url: /fr/go-cpp/set-default-font-while-rendering-spreadsheet-to/
description: Apprenez comment définir la police par défaut lors de la rendu d une feuille de calcul en HTML en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

 Aspose.Cells vous permet de définir la police par défaut lors de la rendu d'une feuille de calcul en HTML. Veuillez utiliser [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdefaultfontname/) à cette fin. Cette propriété est utile lorsqu'il y a des cellules dans une feuille de calcul avec des polices invalides ou inexistantes. Ces cellules seront alors rendues avec la police spécifiée par la propriété [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdefaultfontname/).

{{% /alert %}}

## Définir la police par défaut lors du rendu de la feuille de calcul en HTML

Le code d'exemple suivant crée un classeur et ajoute un texte dans la cellule B4 de la première feuille de calcul et défini sa police sur une police inconnue/inexistante. Ensuite, il sauvegarde le classeur en HTML en définissant différents noms de police par défaut tels que Courier New, Arial, Times New Roman, etc.

 La capture d'écran montre l'effet de la définition de différents noms de police par défaut via la propriété [**HtmlSaveOptions.GetDefaultFontName()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdefaultfontname/).

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

Le code génère le [fichier HTML de sortie avec Courier New](5115516), le [fichier HTML de sortie avec Arial](5115518), et le [fichier HTML de sortie avec Times New Roman](5115517).

## Code d'exemple

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetDefaultFontWhileRenderingSpreadsheetToHtml.go" >}}
