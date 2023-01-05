---
title: Conversion d'une feuille de calcul en image et d'une feuille de calcul en image par page
type: docs
weight: 80
url: /fr/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---
{{% alert color="primary" %}}

Ce document est conçu pour fournir aux développeurs une compréhension détaillée de la façon de convertir une feuille de calcul en un fichier image et une feuille de calcul avec plusieurs pages en un fichier image par page.

Parfois, vous devrez peut-être présenter des feuilles de calcul sous forme d'images, par exemple, pour les utiliser dans des applications ou des pages Web. Vous devrez peut-être insérer les images dans un document Word, un fichier PDF, une présentation PowerPoint ou les utiliser dans un autre scénario. Simplement, vous voulez rendre la feuille de calcul sous forme d'image. Aspose.Cells prend en charge la conversion des feuilles de calcul dans les fichiers Excel Microsoft en images. En outre, Aspose.Cells prend en charge la conversion d'un classeur en plusieurs fichiers image, un par page.

Vous pouvez utiliser la bureautique pour y parvenir, mais la bureautique a ses propres inconvénients. Il y a plusieurs raisons et problèmes impliqués : par exemple la sécurité, la stabilité, l'évolutivité/la vitesse, le prix et les fonctionnalités. Bref, les raisons sont multiples, mais la principale est que le Microsoft lui-même déconseille fortement la bureautique.

{{% /alert %}}

## **Utilisation de Aspose.Cells pour convertir une feuille de calcul en fichier image**

Cet article montre comment créer une application console dans Visual Studio, convertir une feuille de calcul en image et convertir une feuille de calcul en une image pour chaque feuille de calcul avec quelques lignes de code simples à l'aide du Aspose.Cells API.

 Vous devez importer le[**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering) namespace à votre programme/projet. Il a plusieurs classes précieuses, telles que[**FeuilleRendu**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**Options d'image ou d'impression**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**ClasseurRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender), etc. Le[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) la classe représente une feuille de calcul pour restituer des images pour la feuille de calcul et a une surcharge[**VersImage**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index)méthode qui peut convertir une feuille de calcul en fichiers image directement avec n'importe quel ensemble d'attributs ou d'options. Il peut renvoyer un objet System.Drawing.Bitmap et vous pouvez enregistrer un fichier image sur le disque/flux. Plusieurs formats d'image sont pris en charge, par exemple, BMP, PNG, GIF, JPG, JPEG, TIFF, EMF et autres.

Cet article explique comment :

- Convertir une feuille de calcul en image
- Convertir chaque page d'une feuille de calcul en image

Dans cette tâche, vous apprendrez à utiliser Aspose.Cells pour convertir une feuille de calcul d'un modèle de classeur en fichier image.

### **Projet d'installation**

1.  Première,[télécharger Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
1.  Installez-le sur votre poste de développement. Tout[Aspose](http://www.aspose.com/)les composants, une fois installés, fonctionnent en mode d'évaluation. Le mode d'évaluation n'a pas de limite de temps et il injecte uniquement des filigranes dans les documents produits. Maintenant, démarrez Visual Studio.Net et créez une nouvelle application console. Cet exemple utilise une application console C#, mais vous pouvez également utiliser VB.NET. Ajoutez une référence à Aspose.Cells dans le projet créé.

### **Convertir une feuille de calcul en fichier image**

 J'ai créé un nouveau classeur dans Microsoft Excel et ajouté des données dans la première feuille de calcul :**Testbook.xlsx** (1 feuille de travail). Ensuite, convertissez la feuille de calcul Sheet1 du fichier de modèle en un fichier image appelé SheetImage.jpg.

 Voici le code utilisé par le composant pour accomplir la tâche. Il convertit Sheet1 en**Testbook.xlsx** dans un fichier image pour expliquer à quel point cette conversion est facile.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheettoImageFile-1.cs" >}}

## **Utilisation de Aspose.Cells pour convertir une feuille de calcul en fichier image par page**

Cet exemple montre comment utiliser Aspose.Cells pour convertir une feuille de calcul à partir d'un modèle de classeur comportant plusieurs pages en un fichier image par page.

### **Convertir une feuille de calcul en image par page**

 J'ai créé un nouveau classeur dans Microsoft Excel et ajouté des données dans la première feuille de calcul :**Testbook2.xlsx** (1 feuille de travail).

Maintenant, convertissez la feuille de calcul Sheet1 du fichier de modèle en fichiers image (un fichier par page). Comme j'ai déjà créé l'application console pour effectuer la tâche de copie, je vais ignorer ces étapes de création d'application console et passer directement aux étapes de conversion de la feuille de calcul.

Voici le code utilisé par le composant pour accomplir la tâche. Il convertit Sheet1 dans Testbook2.xls en fichiers image par page.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToImageByPage-1.cs" >}}

