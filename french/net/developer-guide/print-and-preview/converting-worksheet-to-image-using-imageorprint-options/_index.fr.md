---
title: Conversion d'une feuille de calcul en image à l'aide des options ImageOrPrint
type: docs
weight: 90
url: /fr/net/converting-worksheet-to-image-using-imageorprint-options/
---
{{% alert color="primary" %}}

Ce document est conçu pour fournir une compréhension détaillée de la façon de convertir une feuille de calcul en fichier image et d'appliquer différentes options d'image et d'impression pour l'image, des options telles que la résolution, la compression TIFF, le format d'image et la qualité de la page.

{{% /alert %}}

##  **Enregistrement de feuilles de calcul sur des images - différentes approches**

Parfois, vous devrez peut-être présenter vos feuilles de calcul sous forme de représentation graphique. Vous devez présenter les images de la feuille de calcul dans vos applications ou vos pages Web. Vous devrez peut-être insérer les images dans un document Word, un fichier PDF, une présentation PowerPoint ou les utiliser dans un autre scénario. Vous voulez simplement qu'une feuille de calcul soit rendue sous forme d'image afin que vous puissiez l'utiliser ailleurs. Aspose.Cells prend en charge la conversion de feuilles de calcul dans des fichiers Excel en images. En outre, Aspose.Cells prend en charge la définition de différentes options telles que le format d'image, la résolution (verticale et horizontale), la qualité d'image et d'autres options d'image et d'impression.

Vous pouvez essayer la bureautique, mais la bureautique a ses propres inconvénients. Il y a plusieurs raisons et problèmes impliqués : par exemple, la sécurité, la stabilité, l'évolutivité et la vitesse, le prix et les fonctionnalités. En bref, il existe de nombreuses raisons, la principale étant que Microsoft lui-même déconseille fortement la bureautique à partir de solutions logicielles.

Cet article montre comment créer une application console dans Visual Studio .NET, effectuer la conversion d'une feuille de calcul en image à l'aide de différentes options d'image et d'impression avec quelques lignes de code simples à l'aide de Aspose.Cells API.

 Vous devez importer[**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering)namespace à votre programme/projet. Il a plusieurs classes utiles, par exemple,[**FeuilleRendu**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**Options d'image ou d'impression**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**ClasseurRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)etc.

Le[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) la classe représente une feuille de calcul pour rendre les images de la feuille de calcul, elle a une surcharge[**VersImage**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index)méthode qui peut convertir directement une feuille de calcul en fichier(s) image spécifié(s) avec les attributs ou options souhaités. Il peut renvoyer l'objet System.Drawing.Bitmap et vous pouvez enregistrer un fichier image sur le disque/flux. Plusieurs formats d'image sont pris en charge, par exemple BMP, PNG, GIFF, JPEG, TIFF, EMF, etc.

##  **Utilisation de Aspose.Cells pour convertir une feuille de calcul en image à l'aide des options ImageOrPrint.**

###  **Création d'un classeur de modèle dans Microsoft Excel**

J'ai créé un nouveau classeur dans MS Excel et ajouté des données dans la première feuille de calcul. Maintenant, je vais convertir la feuille de calcul "Sheet1" du fichier modèle en un fichier image "SheetImage.tiff" et appliquer différentes options d'image comme les résolutions horizontales et verticales, TiffCompression, etc.

###  **Téléchargez et installez Aspose.Cells**

 Tout d'abord, vous devez[télécharger](https://downloads.aspose.com/cells/net) Aspose.Cells pour .Net. Installez-le sur votre poste de développement. Tous[Aspose](http://www.aspose.com/)les composants, une fois installés, fonctionnent en mode d'évaluation. Le mode d'évaluation n'a pas de limite de temps et il injecte uniquement des filigranes dans les documents produits.

###  **Créer un projet**

Démarrez Visual Studio. Net et créez une nouvelle application console. Cet exemple montre une application console C#, mais vous pouvez également utiliser VB.NET.

###  **Ajouter des références**

Ce projet utilisera Aspose.Cells. Vous devez donc ajouter une référence au composant Aspose.Cells dans votre projet. Par exemple, ajoutez une référence à ….\Program Files\Aspose\Aspose.Cells for .NET\Bin\Net1.0\Aspose.Cells.dll

###  **Convertir une feuille de calcul en fichier image**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-WorksheetToAnImage-1.cs" >}}

##  **Options de conversion**

Il est possible d'enregistrer des pages spécifiques à l'image. Le code suivant convertit les première et deuxième feuilles de calcul d'un classeur en images JPG.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-SpecificPagesToImage-1.cs" >}}

##  **Conversion d'images à l'aide de WorkbookRender**

Une image TIFF peut contenir plusieurs images. Vous pouvez enregistrer l'ensemble du classeur dans une seule image TIFF avec plusieurs cadres ou pages :

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-UseWorkbookRenderForImageConversion-1.cs" >}}

