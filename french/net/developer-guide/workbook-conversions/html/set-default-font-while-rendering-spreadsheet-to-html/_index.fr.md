---
title: Définir la police par défaut lors du rendu de la feuille de calcul sur HTML
type: docs
weight: 370
url: /fr/net/set-default-font-while-rendering-spreadsheet-to/
---
{{% alert color="primary" %}}

 Aspose.Cells vous permet de définir la police par défaut lors du rendu de la feuille de calcul sur HTML. Veuillez utiliser le[**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname) dans ce but. Cette propriété est utile lorsque certaines cellules d'une feuille de calcul contiennent des polices non valides ou inexistantes. Ensuite, ces cellules seront rendues dans une police spécifiée avec le[**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname) la propriété.

{{% /alert %}}

## Définir la police par défaut lors du rendu de la feuille de calcul sur HTML

L'exemple de code suivant crée un classeur et ajoute du texte dans la cellule B4 de la première feuille de calcul et définit sa police sur une police inconnue/inexistante. Ensuite, il enregistre le classeur en HTML en définissant différents noms de police par défaut tels que Courier New, Arial, Times New Roman, etc.

 La capture d'écran montre l'effet de la définition de différents noms de police par défaut via[**HtmlSaveOptions.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/defaultfontname)la propriété.

![tâche : image_autre_texte](set-default-font-while-rendering-spreadsheet-to-html_1.png)

 Le code génère le[fichier de sortie HTML avec Courier New](5115516) , le[sortie HTML avec Arial](5115518) , et le[fichier de sortie HTML avec Times New Roman](5115517).

## Exemple de code

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetDefaultFontWhileRendering-1.cs" >}}
