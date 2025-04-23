---
title: Définir la police par défaut lors du rendu de feuilles de calcul en images
type: docs
weight: 360
url: /fr/net/set-default-font-while-rendering-spreadsheet-to-images/
---

{{% alert color="primary" %}}

Veuillez utiliser la propriété [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) pour définir la police par défaut lors du rendu des feuilles de calcul en images. Cette propriété ne sera efficace que lorsque la police par défaut du classeur ne pourra pas afficher vos caractères. La police par défaut spécifiée avec la propriété [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) est utilisée pour toutes les cellules qui ont des polices invalides ou inexistantes.

{{% /alert %}}

## Définir la police par défaut lors du rendu de feuilles de calcul en images

Le code d'exemple suivant crée un classeur, ajoute du texte dans la cellule A4 de la première feuille de calcul, et définit sa police sur une police invalide ou inexistante. Ensuite, il prend deux images de la feuille de calcul. La première image est prise en définissant la propriété [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) sur *Courier New* et la deuxième image est prise en définissant la propriété [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) sur *Times New Roman*.

Voici l'image de sortie après avoir défini la propriété [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) sur *Courier New*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

Voici l'image de sortie après avoir défini la propriété [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont) sur *Times New Roman*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

## Code d'exemple

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetDefaultFontWhileRenderingSpreadsheet-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
