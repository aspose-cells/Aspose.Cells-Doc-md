---
title: Définir la police par défaut lors du rendu de la feuille de calcul en HTML
type: docs
weight: 370
url: /fr/net/set-default-font-while-rendering-spreadsheet-to/
---

{{% alert color="primary" %}}

Aspose.Cells vous permet de définir la police par défaut lors du rendu de la feuille de calcul en HTML. Veuillez utiliser [**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname) à cette fin. Cette propriété est utile lorsqu'il y a des cellules dans une feuille de calcul qui ont des polices invalides ou inexistantes. Alors, ces cellules seront rendues dans une police spécifiée avec la propriété [**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname).

{{% /alert %}}

## Définir la police par défaut lors du rendu de la feuille de calcul en HTML

Le code d'exemple suivant crée un classeur et ajoute un texte dans la cellule B4 de la première feuille de calcul et défini sa police sur une police inconnue/inexistante. Ensuite, il sauvegarde le classeur en HTML en définissant différents noms de police par défaut tels que Courier New, Arial, Times New Roman, etc.

La capture d'écran montre l'effet de définir différents noms de police par défaut via la propriété [**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname).

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

Le code génère le [fichier HTML de sortie avec Courier New](5115516), le [fichier HTML de sortie avec Arial](5115518), et le [fichier HTML de sortie avec Times New Roman](5115517).

## Code d'exemple

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetDefaultFontWhileRendering-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
