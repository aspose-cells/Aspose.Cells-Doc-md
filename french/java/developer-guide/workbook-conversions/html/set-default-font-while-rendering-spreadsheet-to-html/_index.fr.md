---
title: Définir la police par défaut lors du rendu de la feuille de calcul en HTML
type: docs
weight: 830
url: /fr/java/set-default-font-while-rendering-spreadsheet-to/
---

{{% alert color="primary" %}} 

Aspose.Cells vous permet de définir la police par défaut lors du rendu de la feuille de calcul en HTML. Veuillez utiliser la propriété [HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName) à cet effet. Cette propriété est utile lorsque certaines cellules d'une feuille de calcul ont des polices invalides ou n'existantes. Ensuite, ces cellules seront rendues dans une police spécifiée avec la propriété [HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName).

{{% /alert %}} 
## **Définir la police par défaut lors du rendu de la feuille de calcul en HTML**
Le code d'exemple suivant crée un classeur et ajoute un texte dans la cellule B4 de la première feuille de calcul et défini sa police sur une police inconnue/inexistante. Ensuite, il sauvegarde le classeur en HTML en définissant différents noms de police par défaut tels que Courier New, Arial, Times New Roman, etc.

La capture d'écran montre l'effet de la définition de différents noms de police par défaut via la propriété [HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName).

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

Le code génère le [fichier HTML de sortie avec Courier New](5472568), le [fichier HTML de sortie avec Arial](5472567) et le [fichier HTML de sortie avec Times New Roman](5472565).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToHTML-.java" >}}
{{< app/cells/assistant language="java" >}}
