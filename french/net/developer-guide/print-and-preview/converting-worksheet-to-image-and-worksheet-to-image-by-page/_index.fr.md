---
title: Conversion de la feuille de calcul en image et de la feuille de calcul en image par page
type: docs
weight: 80
url: /fr/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}

Ce document est conçu pour fournir aux développeurs une compréhension détaillée de la manière de convertir une feuille de calcul en un fichier image et une feuille de calcul avec plusieurs pages en un fichier image par page.

Parfois, vous pourriez avoir besoin de présenter des feuilles de calcul en tant qu'images, par exemple, pour les utiliser dans des applications ou des pages web. Vous pourriez avoir besoin d'insérer les images dans un document Word, un fichier PDF, une présentation PowerPoint ou les utiliser dans un autre scénario. Fondamentalement, vous voulez afficher la feuille de calcul sous forme d'image. Aspose.Cells prend en charge la conversion des feuilles de calcul dans les fichiers Microsoft Excel en images. De plus, Aspose.Cells prend en charge la conversion d'un classeur en plusieurs fichiers image, un par page.

Vous pourriez utiliser l'automatisation Office pour y parvenir, mais l'automatisation Office a ses propres inconvénients. Il existe plusieurs raisons et problèmes impliqués : par exemple la sécurité, la stabilité, la scalabilité/la vitesse, le prix et les fonctionnalités. En bref, il existe de nombreuses raisons, mais la principale est que Microsoft elle-même déconseille fortement l'automatisation Office.

{{% /alert %}}

## **Utilisation d'Aspose.Cells pour convertir une feuille de calcul en un fichier image**

Cet article montre comment créer une application console dans Visual Studio, convertir une feuille de calcul en une image et convertir une feuille de calcul en une image pour chaque feuille de calcul avec quelques lignes de code simples à l'aide de l'API Aspose.Cells.

Vous devez importer l'espace de noms [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering) dans votre programme/projet. Il possède plusieurs classes précieuses, telles que [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender), et ainsi de suite. La classe [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) représente une feuille de calcul pour rendre des images pour la feuille de calcul et possède une méthode [**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index) surchargée qui peut convertir une feuille de calcul en fichiers image directement avec des attributs ou des options définis. Il peut renvoyer un objet System.Drawing.Bitmap et vous pouvez enregistrer un fichier image sur le disque/le flux. Plusieurs formats d'image sont pris en charge, par exemple, BMP, PNG, GIF, JPG, JPEG, TIFF, EMF, et d'autres.

Cet article explique comment :

- Convertir une feuille de calcul en une image
- Convertir chaque page d'une feuille de calcul en une image

Cette tâche montre comment utiliser Aspose.Cells pour convertir une feuille de calcul à partir d'un classeur modèle en un fichier image.

### **Configurer le projet**

1. Tout d'abord, [téléchargez Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
1. Installez-le sur votre ordinateur de développement. Tous les [Aspose](http://www.aspose.com/) composants, une fois installés, fonctionnent en mode évaluation. Le mode évaluation n'a pas de limite de temps et il injecte uniquement des filigranes dans les documents produits. Maintenant, démarrez Visual Studio.Net et créez une nouvelle application console. Cet exemple utilise une application console C#, mais vous pouvez également utiliser VB.NET. Ajoutez une référence à Aspose.Cells dans le projet créé.

### **Convertir une feuille de calcul en un fichier image**

J'ai créé un nouveau classeur dans Microsoft Excel et ajouté des données dans la première feuille de calcul : **Testbook.xlsx** (1 feuille de calcul). Ensuite, convertissez la feuille de calcul du fichier modèle en un fichier image appelé SheetImage.jpg.

Voici le code utilisé par le composant pour accomplir la tâche. Il convertit la Feuille1 dans **Testbook.xlsx** en un fichier image pour expliquer à quel point cette conversion est facile.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheettoImageFile-1.cs" >}}

## **Utilisation d'Aspose.Cells pour convertir une feuille de calcul en fichier image par page**

Cet exemple montre comment utiliser Aspose.Cells pour convertir une feuille de calcul d'un classeur modèle comportant plusieurs pages en un fichier image unique par page.

### **Convertir une feuille de calcul en image par page**

J'ai créé un nouveau classeur dans Microsoft Excel et ajouté des données dans la première feuille de calcul : **Testbook2.xlsx** (1 feuille de calcul).

Maintenant, convertissez la feuille de calcul du fichier modèle en fichiers image (un fichier par page). Comme j'ai déjà créé l'application console pour effectuer la tâche de copie, je vais ignorer ces étapes de création de l'application console et passer directement aux étapes de conversion de la feuille de calcul.

Voici le code utilisé par le composant pour accomplir la tâche. Il convertit Sheet1 dans Testbook2.xls en fichiers image par page.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToImageByPage-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
