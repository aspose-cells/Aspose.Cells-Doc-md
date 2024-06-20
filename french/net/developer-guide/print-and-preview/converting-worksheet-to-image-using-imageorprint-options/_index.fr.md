---
title: Convertir une feuille de calcul en image en utilisant des options ImageOrPrint
type: docs
weight: 90
url: /fr/net/converting-worksheet-to-image-using-imageorprint-options/
---

{{% alert color="primary" %}}

Ce document est conçu pour fournir une compréhension détaillée de la manière de convertir une feuille de calcul en fichier image et d'appliquer différentes options d'image et d'impression pour l'image, comme la résolution, la compression TIFF, le format d'image et la qualité de page.

{{% /alert %}}

## **Enregistrement de feuilles de calcul en images - différentes approches**

Parfois, vous pourriez avoir besoin de présenter vos feuilles de calcul sous forme de représentation imagée. Vous devez présenter les images de feuilles de calcul dans vos applications ou pages web. Vous pourriez avoir besoin d'insérer les images dans un document Word, un fichier PDF, une présentation PowerPoint ou les utiliser dans un autre contexte. Tout simplement, vous souhaitez une feuille de calcul rendue sous forme d'image afin de pouvoir l'utiliser ailleurs. Aspose.Cells prend en charge la conversion des feuilles de calcul dans des fichiers Excel en images. De plus, Aspose.Cells prend en charge la définition de différentes options telles que le format d'image, la résolution (verticale et horizontale), la qualité d'image et d'autres options d'image et d'impression.

Vous pourriez essayer l'automatisation Office, mais l'automatisation Office a ses propres inconvénients. Il y a plusieurs raisons et problèmes associés : par exemple, la sécurité, la stabilité, la scalabilité et la vitesse, le prix et les fonctionnalités. En bref, il y a de nombreuses raisons, la principale étant que Microsoft lui-même déconseille fortement l'automatisation Office à partir de solutions logicielles.

Cet article montre comment créer une application console dans Visual Studio .NET, effectuer la conversion d'une feuille de calcul en image en utilisant différentes options d'image et d'impression avec quelques lignes de code les plus simples à l'aide de l'API Aspose.Cells.

Vous devez importer [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering) espace de noms dans votre programme/projet. Il comporte plusieurs classes précieuses, par exemple : [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender) etc.

La classe [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) représente une feuille de calcul pour afficher des images pour la feuille de calcul, elle comporte une méthode [**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index) surchargée qui peut directement convertir une feuille de calcul en un fichier image spécifié avec les attributs ou options que vous avez demandés. Elle peut renvoyer un objet System.Drawing.Bitmap et vous pouvez enregistrer un fichier image sur le disque/flux. Plusieurs formats d'image sont pris en charge, comme BMP, PNG, GIF, JPEG, TIFF, EMF, etc.

## **Utilisation d'Aspose.Cells pour convertir une feuille de calcul en image en utilisant des options ImageOrPrint.**

### **Création d'un classeur modèle dans Microsoft Excel**

J'ai créé un nouveau classeur dans MS Excel et ajouté des données dans la première feuille de calcul. Maintenant, je vais convertir la feuille de calcul du fichier modèle "Feuille1" en un fichier image "FeuilleImage.tiff" et appliquer différentes options d'image comme les résolutions horizontales et verticales, la compression Tiff, etc.

### **Téléchargez et installez Aspose.Cells**

Tout d'abord, vous avez besoin de [télécharger](https://downloads.aspose.com/cells/net) Aspose.Cells pour .Net. Installez-le sur votre ordinateur de développement. Tous les [Aspose](http://www.aspose.com/) composants, une fois installés, fonctionnent en mode évaluation. Le mode d'évaluation n'a pas de limite de temps et il insère uniquement des filigranes dans les documents générés.

### **Créer un projet**

Démarrer Visual Studio. Net et créer une nouvelle application console. Cet exemple montrera une application console C#, mais vous pouvez également utiliser VB.NET.

### **Ajouter des références**

Ce projet utilisera Aspose.Cells. Vous devez donc ajouter une référence au composant Aspose.Cells dans votre projet. Par exemple, ajoutez une référence à ….\Program Files\Aspose\Aspose.Cells for .NET\Bin\Net1.0\Aspose.Cells.dll.

### **Convertir une feuille de calcul en un fichier image**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-WorksheetToAnImage-1.cs" >}}

## **Options de conversion**

Il est possible d'enregistrer des pages spécifiques en tant qu'images. Le code suivant convertit les première et deuxième feuilles de calcul dans un classeur en images JPG.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-SpecificPagesToImage-1.cs" >}}

## **Conversion d'image à l'aide de WorkbookRender**

Une image TIFF peut contenir plus d'une trame. Vous pouvez enregistrer l'ensemble du classeur en une seule image TIFF avec plusieurs trames ou pages :

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-UseWorkbookRenderForImageConversion-1.cs" >}}

