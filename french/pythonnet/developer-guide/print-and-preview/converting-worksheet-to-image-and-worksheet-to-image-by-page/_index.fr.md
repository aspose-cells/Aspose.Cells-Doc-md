---
title: Conversion de la feuille de calcul en image et de la feuille de calcul en image par page
type: docs
weight: 80
url: /fr/python-net/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}

Ce document est conçu pour fournir aux développeurs une compréhension détaillée de la manière de convertir une feuille de calcul en un fichier image et une feuille de calcul avec plusieurs pages en un fichier image par page.

Parfois, vous pourriez avoir besoin de présenter des feuilles de calcul sous forme d’images, par exemple pour les utiliser dans des applications ou des pages web. Vous pourriez avoir besoin d’insérer ces images dans un document Word, un fichier PDF, une présentation PowerPoint, ou de les utiliser dans un autre scénario. En résumé, vous souhaitez rendre la feuille de calcul en tant qu’image. Aspose.Cells pour Python via .NET supporte la conversion de feuilles de calcul dans des fichiers Excel en images. De plus, Aspose.Cells pour Python via .NET supporte la conversion d’un classeur en plusieurs fichiers image, un par page.

Vous pourriez utiliser l'automatisation Office pour y parvenir, mais l'automatisation Office a ses propres inconvénients. Il existe plusieurs raisons et problèmes impliqués : par exemple la sécurité, la stabilité, la scalabilité/la vitesse, le prix et les fonctionnalités. En bref, il existe de nombreuses raisons, mais la principale est que Microsoft elle-même déconseille fortement l'automatisation Office.

{{% /alert %}}

## **Utilisation d'Aspose.Cells pour convertir une feuille de calcul en un fichier image**

Cet article montre comment créer une application console dans Visual Studio, convertir une feuille de calcul en image, et convertir une feuille de calcul en une image pour chaque feuille avec quelques lignes de code simples utilisant l’API Aspose.Cells pour Python via .NET.

Vous devez importer l'espace de noms [**aspose.cells.rendering**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering) dans votre programme/projet. Il possède plusieurs classes précieuses, telles que [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender), et ainsi de suite. La classe [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender) représente une feuille de calcul pour rendre des images pour la feuille de calcul et possède une méthode [**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str) surchargée qui peut convertir une feuille de calcul en fichiers image directement avec des attributs ou des options définis. Il peut renvoyer un objet System.Drawing.Bitmap et vous pouvez enregistrer un fichier image sur le disque/le flux. Plusieurs formats d'image sont pris en charge, par exemple, BMP, PNG, GIF, JPG, JPEG, TIFF, EMF, et d'autres.

Cet article explique comment convertir une feuille de calcul en image. Cette tâche montre comment utiliser Aspose.Cells pour Python via .NET pour convertir une feuille de calcul d’un classeur modèle en un fichier image.


### **Convertir une feuille de calcul en un fichier image**

J'ai créé un nouveau classeur dans Microsoft Excel et ajouté des données dans la première feuille de calcul : **Testbook.xlsx** (1 feuille de calcul). Ensuite, convertissez la feuille de calcul du fichier modèle en un fichier image appelé SheetImage.jpg.

Voici le code utilisé par le composant pour accomplir la tâche. Il convertit la Feuille1 dans **Testbook.xlsx** en un fichier image pour expliquer à quel point cette conversion est facile.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-ConvertWorksheettoImageFile-1.py" >}}

## **Utilisation d'Aspose.Cells pour convertir une feuille de calcul en fichier image par page**

Cet exemple montre comment utiliser Aspose.Cells pour Python via .NET pour convertir une feuille de calcul d’un classeur modèle contenant plusieurs pages en un fichier image par page.

### **Convertir une feuille de calcul en image par page**

J'ai créé un nouveau classeur dans Microsoft Excel et ajouté des données dans la première feuille de calcul : **Testbook2.xlsx** (1 feuille de calcul).

Maintenant, convertissez la feuille de calcul du fichier modèle en fichiers image (un fichier par page). Comme j'ai déjà créé l'application console pour effectuer la tâche de copie, je vais ignorer ces étapes de création de l'application console et passer directement aux étapes de conversion de la feuille de calcul.

Voici le code utilisé par le composant pour accomplir la tâche. Il convertit Sheet1 dans Testbook2.xls en fichiers image par page.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-ConvertWorksheetToImageByPage-1.py" >}}

