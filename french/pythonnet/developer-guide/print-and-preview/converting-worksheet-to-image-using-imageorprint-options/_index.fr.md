---
title: Convertir une feuille de calcul en image en utilisant des options ImageOrPrint
type: docs
weight: 90
url: /fr/python-net/converting-worksheet-to-image-using-imageorprint-options/
---

{{% alert color="primary" %}}

Ce document est conçu pour fournir une compréhension détaillée de la manière de convertir une feuille de calcul en fichier image et d'appliquer différentes options d'image et d'impression pour l'image, comme la résolution, la compression TIFF, le format d'image et la qualité de page.

{{% /alert %}}

## **Enregistrement de feuilles de calcul en images - différentes approches**

Parfois, vous pourriez avoir besoin de présenter vos feuilles de calcul sous forme d’image picturale. Vous souhaitez rendre les images des feuilles de calcul dans vos applications ou pages web. Vous pourriez avoir besoin d’insérer ces images dans un document Word, un fichier PDF, une présentation PowerPoint, ou de les utiliser dans un autre scénario. En résumé, vous voulez une feuille de calcul rendue comme une image pour pouvoir l’utiliser ailleurs. Aspose.Cells pour Python via .NET supporte la conversion de feuilles de calcul Excel en images. De plus, Aspose.Cells pour Python via .NET supporte la configuration de différentes options telles que le format d’image, la résolution (verticale et horizontale), la qualité de l’image, et d’autres options d’image et d’impression.

Vous pourriez essayer l'automatisation Office, mais l'automatisation Office a ses propres inconvénients. Il y a plusieurs raisons et problèmes associés : par exemple, la sécurité, la stabilité, la scalabilité et la vitesse, le prix et les fonctionnalités. En bref, il y a de nombreuses raisons, la principale étant que Microsoft lui-même déconseille fortement l'automatisation Office à partir de solutions logicielles.

Cet article montre comment créer une application console dans Visual Studio .NET, effectuer la conversion d'une feuille de calcul en image en utilisant différentes options d'image et d'impression avec quelques lignes de code simples utilisant l'API Aspose.Cells pour Python via .NET.

Vous devez importer [**aspose.cells.rendering**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering) espace de noms dans votre programme/projet. Il comporte plusieurs classes précieuses, par exemple : [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender) etc.

La classe [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender) représente une feuille de calcul pour afficher des images pour la feuille de calcul, elle comporte une méthode [**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str) surchargée qui peut directement convertir une feuille de calcul en un fichier image spécifié avec les attributs ou options que vous avez demandés. Elle peut renvoyer un objet System.Drawing.Bitmap et vous pouvez enregistrer un fichier image sur le disque/flux. Plusieurs formats d'image sont pris en charge, comme BMP, PNG, GIF, JPEG, TIFF, EMF, etc.

## **Utilisation d'Aspose.Cells pour convertir une feuille de calcul en image en utilisant les options ImageOrPrint**

### **Création d'un classeur modèle dans Microsoft Excel**

J'ai créé un nouveau classeur dans MS Excel et ajouté des données dans la première feuille de calcul. Maintenant, je vais convertir la feuille de calcul du fichier modèle "Feuille1" en un fichier image "FeuilleImage.tiff" et appliquer différentes options d'image comme les résolutions horizontales et verticales, la compression Tiff, etc.

### **Convertir une feuille de calcul en un fichier image**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-WorksheetToAnImage-1.py" >}}


## **Conversion d'image à l'aide de WorkbookRender**

Une image TIFF peut contenir plus d'une trame. Vous pouvez enregistrer l'ensemble du classeur en une seule image TIFF avec plusieurs trames ou pages :

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-UseWorkbookRenderForImageConversion-1.py" >}}

