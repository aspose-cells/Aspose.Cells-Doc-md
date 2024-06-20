---
title: Définir la police par défaut lors du rendu de feuilles de calcul en images
type: docs
weight: 840
url: /fr/java/set-default-font-while-rendering-spreadsheet-to-images/
---

{{% alert color="primary" %}} 

Veuillez utiliser la propriété [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) pour définir la police par défaut lors du rendu de la feuille de calcul en images. Cette propriété ne sera efficace que lorsque la police par défaut du classeur ne peut pas afficher vos caractères. La police par défaut spécifiée avec la propriété [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) est utilisée pour toutes ces cellules qui ont des polices invalides ou inexistantes.

{{% /alert %}} 
## **Définir la police par défaut lors du rendu de la feuille de calcul en images**
Le code d'exemple suivant crée un classeur, ajoute du texte dans la cellule A4 de la première feuille de calcul et défini sa police sur une police invalide ou inexistante. Ensuite, il prend deux images de la feuille de calcul. La première image est prise en définissant la propriété [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) sur *Courier New* et la deuxième image est prise en définissant la propriété [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) sur *Times New Roman*.

Voici l'image de sortie après avoir défini la propriété [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) sur *Courier New*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

Voici l'image de sortie après avoir défini la propriété [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) sur *Times New Roman*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToImages-.java" >}}
