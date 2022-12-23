---
title: Définir la police par défaut lors du rendu de la feuille de calcul sur HTML
type: docs
weight: 830
url: /fr/java/set-default-font-while-rendering-spreadsheet-to/
---
{{% alert color="primary" %}} 

 Aspose.Cells vous permet de définir la police par défaut lors du rendu de la feuille de calcul sur HTML. Veuillez utiliser le[HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName)dans ce but. Cette propriété est utile lorsque certaines cellules d'une feuille de calcul contiennent des polices non valides ou inexistantes. Ensuite, ces cellules seront rendues dans une police spécifiée avec[HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName) la propriété.

{{% /alert %}} 
## **Définir la police par défaut lors du rendu de la feuille de calcul sur HTML**
L'exemple de code suivant crée un classeur et ajoute du texte dans la cellule B4 de la première feuille de calcul et définit sa police sur une police inconnue/inexistante. Ensuite, il enregistre le classeur en HTML en définissant différents noms de police par défaut tels que Courier New, Arial, Times New Roman, etc.

 La capture d'écran montre l'effet de la définition de différents noms de police par défaut via[HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName)la propriété.

![tâche : image_autre_texte](set-default-font-while-rendering-spreadsheet-to-html_1.png)

 Le code génère le[fichier de sortie HTML avec Courier New](5472568) , le[sortie HTML avec Arial](5472567) et le[fichier de sortie HTML avec Times New Roman](5472565).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToHTML-.java" >}}
