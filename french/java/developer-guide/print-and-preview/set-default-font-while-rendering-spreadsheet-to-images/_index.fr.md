---
title: Définir la police par défaut lors du rendu de la feuille de calcul en images
type: docs
weight: 840
url: /fr/java/set-default-font-while-rendering-spreadsheet-to-images/
---
{{% alert color="primary" %}} 

 Veuillez utiliser le[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) propriété pour définir la police par défaut lors du rendu de la feuille de calcul en images. Cette propriété ne sera effective que lorsque la police par défaut du classeur ne pourra pas restituer vos caractères. La police par défaut spécifiée avec[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) La propriété est utilisée pour toutes les cellules qui ont des polices invalides ou inexistantes.

{{% /alert %}} 
## **Définir la police par défaut lors du rendu de la feuille de calcul en images**
L'exemple de code suivant crée un classeur, ajoute du texte dans la cellule A4 de la première feuille de calcul et définit sa police sur une police non valide ou inexistante. Ensuite, il prend deux images de la feuille de calcul. La première image est prise en réglant le[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) propriété à*Courrier Nouveau* et la deuxième image est prise en réglant le[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) propriété à*Times New Roman*.

 Il s'agit de l'image de sortie après avoir défini le[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) propriété à*Courrier Nouveau*.

![tâche : image_autre_texte](set-default-font-while-rendering-spreadsheet-to-images_1.png)

 Il s'agit de l'image de sortie après avoir défini le[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) propriété à*Times New Roman*.

![tâche : image_autre_texte](set-default-font-while-rendering-spreadsheet-to-images_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToImages-.java" >}}
