---
title: Définir la police par défaut lors du rendu de la feuille de calcul en HTML
type: docs
weight: 370
url: /fr/python-net/set-default-font-while-rendering-spreadsheet-to/
---

{{% alert color="primary" %}}

Aspose.Cells vous permet de définir la police par défaut lors du rendu de la feuille de calcul en HTML. Veuillez utiliser [**HtmlSaveOptions.default_font_name**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/default_font_name) à cette fin. Cette propriété est utile lorsqu'il y a des cellules dans une feuille de calcul qui ont des polices invalides ou inexistantes. Alors, ces cellules seront rendues dans une police spécifiée avec la propriété [**HtmlSaveOptions.default_font_name**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/default_font_name).

{{% /alert %}}

## Définir la police par défaut lors du rendu de la feuille de calcul en HTML

Le code d'exemple suivant crée un classeur et ajoute un texte dans la cellule B4 de la première feuille de calcul et défini sa police sur une police inconnue/inexistante. Ensuite, il sauvegarde le classeur en HTML en définissant différents noms de police par défaut tels que Courier New, Arial, Times New Roman, etc.

La capture d'écran montre l'effet de définir différents noms de police par défaut via la propriété [**HtmlSaveOptions.default_font_name**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/default_font_name).

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

Le code génère le [fichier HTML de sortie avec Courier New](5115516), le [fichier HTML de sortie avec Arial](5115518), et le [fichier HTML de sortie avec Times New Roman](5115517).

## Code d'exemple

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-SetDefaultFontWhileRendering-1.py" >}}
