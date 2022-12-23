---
title: Insérez des images et des formes de fichiers Excel.
linktitle: Formes
type: docs
weight: 140
url: /fr/net/insert-shapes/
description: Gérer les images, oleobject, formes dans des fichiers Excel.
---
{{% alert color="primary" %}}

Parfois, vous devez insérer certaines formes nécessaires dans la feuille de calcul. Vous devrez peut-être insérer la même forme dans différentes positions de la feuille de calcul. Ou vous devez insérer des formes par lots dans la feuille de calcul.

 Ne t'en fais pas![Aspose.Cells](https://products.aspose.com/cells/)prend en charge toutes ces opérations.

{{% /alert %}}

Les formes dans Excel sont principalement divisées en types suivants :
- **Des photos**
- **OleObjects**
- **Lignes**
- **rectangles**
- **Formes de base**
- **Bloquer les flèches**
- **Formes d'équation**
- **Organigrammes**
- **Étoiles et bannières**
- **Légendes**

 Ce document guide sélectionnera une ou deux formes de chaque type pour créer des échantillons. Grâce à ces exemples, vous apprendrez à utiliser[Aspose.Cells](https://products.aspose.com/cells/) pour insérer la forme spécifiée dans la feuille de calcul.

## **Ajout d'images dans la feuille de calcul Excel dans C#**

Ajouter des images à une feuille de calcul est très simple. Cela ne prend que quelques lignes de code :
 Appelez simplement le[**Ajouter**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) méthode de la[**Des photos**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection) collection (encapsulée dans le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) objet). Le[**Ajouter**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)méthode prend les paramètres suivants :

- **Index de la ligne supérieure gauche**, l'index de la ligne supérieure gauche.
- **Index de la colonne en haut à gauche**, l'indice de la colonne supérieure gauche.
- **Nom du fichier image**, le nom du fichier image, complet avec le chemin.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-AddingPictures-1.cs" >}}


## **Insertion d'objets OLE dans une feuille de calcul Excel dans C#**

Aspose.Cells prend en charge l'ajout, l'extraction et la manipulation d'objets OLE dans les feuilles de calcul. Pour cette raison, Aspose.Cells a le[**OleObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobjectcollection) classe, utilisée pour ajouter un nouvel objet OLE à la liste de collection. Une autre classe,[**OleObject**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject), représente un objet OLE. Il compte quelques membres importants :

-  Le[**ImageData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/imagedata)La propriété spécifie les données d'image (icône) de type tableau d'octets. L'image s'affichera pour montrer l'objet OLE dans la feuille de calcul.
-  Le[**ObjectData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/objectdata)La propriété spécifie les données de l'objet sous la forme d'un tableau d'octets. Ces données seront affichées dans son programme associé lorsque vous double-cliquez sur l'icône de l'objet OLE.

L'exemple suivant montre comment ajouter un ou plusieurs objets OLE dans une feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-InsertingOLEObjects-1.cs" >}}

## **Insertion d'une ligne dans une feuille de calcul Excel dans C#**

 La forme de la ligne appartient à la**lignes** Catégorie.

***Dans Microsoft Excel (par exemple 2007) :***

- Sélectionnez la cellule où vous voulez insérer la ligne
- Cliquez sur le menu Insertion et cliquez sur Formes.
- Ensuite, sélectionnez la ligne dans "Formes récemment utilisées" ou "Lignes"

![](line.png)

***En utilisant Aspose.Cells***

Vous pouvez utiliser la méthode suivante pour insérer une ligne dans la feuille de calcul.

{{% alert color="primary" %}}

[public Forme de ligne AddLine(
 int upperLeftRow,
 en haut,
 int upperLeftColumn,
 int gauche,
 hauteur int,
 largeur entière
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)

 La méthode retourne un[Forme de ligne](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) objet.

{{% /alert %}}

L'exemple suivant montre comment insérer une ligne dans une feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Line.cs" >}}

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants :

![](line2.png)



## **Insertion d'une flèche de ligne dans la feuille de calcul Excel dans C#**

 La forme de la flèche de ligne appartient à la**Lignes** catégorie. C'est un cas particulier de ligne.

***Dans Microsoft Excel (par exemple 2007) :***

- Sélectionnez la cellule où vous souhaitez insérer la flèche de ligne
- Cliquez sur le menu Insertion et cliquez sur Formes.
- Ensuite, sélectionnez la flèche de ligne dans "Formes récemment utilisées" ou "Lignes"

![](line_arrow1.png)

***En utilisant Aspose.Cells***

Vous pouvez utiliser la méthode suivante pour insérer une flèche de ligne dans la feuille de calcul.

{{% alert color="primary" %}}

[public Forme de ligne AddLine(
 int upperLeftRow,
 en haut,
 int upperLeftColumn,
 int gauche,
 hauteur int,
 largeur entière
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)

 La méthode retourne un[Forme de ligne](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) objet.

{{% /alert %}}

L'exemple suivant montre comment insérer une flèche de ligne dans une feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-LineArrow.cs" >}}

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants :

![](line_arrow2.png)



## **Insertion d'un rectangle dans une feuille de calcul Excel dans C#**

 La forme du rectangle appartient à la**rectangles** Catégorie.

***Dans Microsoft Excel (par exemple 2007) :***

- Sélectionnez la cellule où vous souhaitez insérer le rectangle
- Cliquez sur le menu Insertion et cliquez sur Formes.
- Ensuite, sélectionnez le rectangle dans "Formes récemment utilisées" ou "Rectangles"

![](rectangle.png)

***En utilisant Aspose.Cells***

Vous pouvez utiliser la méthode suivante pour insérer un rectangle dans la feuille de calcul.

{{% alert color="primary" %}}

[public RectangleShape AddRectangle(
 int upperLeftRow,
 en haut,
 int upperLeftColumn,
 int gauche,
 hauteur int,
 largeur entière
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle)

 La méthode retourne un[Forme Rectangle](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) objet.

{{% /alert %}}

L'exemple suivant montre comment insérer un rectangle dans une feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Rectangle.cs" >}}

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants :

![](rectangle2.png)



## **Insertion d'un cube dans une feuille de calcul Excel dans C#**

La forme du cube appartient à la**Formes de base** Catégorie.

***Dans Microsoft Excel (par exemple 2007) :***

- Sélectionnez la cellule où vous souhaitez insérer le cube
- Cliquez sur le menu Insertion et cliquez sur Formes.
-  Ensuite, sélectionnez le cube à partir de**Formes de base**

![](cube.png)

***En utilisant Aspose.Cells***

Vous pouvez utiliser la méthode suivante pour insérer un cube dans la feuille de calcul.

{{% alert color="primary" %}}

[forme publique AddAutoShape(
 Type de forme automatique,
 int upperLeftRow,
 en haut,
 int upperLeftColumn,
 int gauche,
 hauteur int,
 largeur entière
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 La méthode retourne un[Façonner](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) objet.

{{% /alert %}}

L'exemple suivant montre comment insérer un cube dans une feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Cube.cs" >}}

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants :

![](cube2.png)



## **Insertion d'une flèche quadruple de légende dans la feuille de calcul Excel dans C#**

 La forme de la flèche quadruple de la légende appartient au**Bloquer les flèches** Catégorie.

***Dans Microsoft Excel (par exemple 2007) :***

- Sélectionnez la cellule dans laquelle vous souhaitez insérer la flèche quadruple de la légende
- Cliquez sur le menu Insertion et cliquez sur Formes.
-  Ensuite, sélectionnez la flèche quadruple de la légende à partir de**Bloquer les flèches**

![](callout_quad_arrow.png)

***En utilisant Aspose.Cells***

Vous pouvez utiliser la méthode suivante pour insérer une flèche quadruple de légende dans la feuille de calcul.

{{% alert color="primary" %}}

[forme publique AddAutoShape(
 Type de forme automatique,
 int upperLeftRow,
 en haut,
 int upperLeftColumn,
 int gauche,
 hauteur int,
 largeur entière
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 La méthode retourne un[Façonner](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) objet.

{{% /alert %}}

L'exemple suivant montre comment insérer une flèche quadruple de légende dans une feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.cs" >}}

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants :

![](callout_quad_arrow2.png)



## **Insertion d'un signe de multiplication dans la feuille de calcul Excel dans C#**

 La forme du signe de multiplication appartient au**Formes d'équation** Catégorie.

***Dans Microsoft Excel (par exemple 2007) :***

- Sélectionnez la cellule où vous souhaitez insérer le signe de multiplication
- Cliquez sur le menu Insertion et cliquez sur Formes.
-  Ensuite, sélectionnez le signe de multiplication de**Formes d'équation**

![](multiplication_sign.png)

***En utilisant Aspose.Cells***

Vous pouvez utiliser la méthode suivante pour insérer un signe de multiplication dans la feuille de calcul.

{{% alert color="primary" %}}

[forme publique AddAutoShape(
 Type de forme automatique,
 int upperLeftRow,
 en haut,
 int upperLeftColumn,
 int gauche,
 hauteur int,
 largeur entière
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 La méthode retourne un[Façonner](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) objet.

{{% /alert %}}

L'exemple suivant montre comment insérer un signe de multiplication dans une feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.cs" >}}

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants :

![](multiplication_sign2.png)



## **Insertion d'un multidocument dans une feuille de calcul Excel dans C#**

 La forme de multidocument appartient à la**Organigrammes** Catégorie.

***Dans Microsoft Excel (par exemple 2007) :***

- Sélectionnez la cellule où vous souhaitez insérer le multidocument
- Cliquez sur le menu Insertion et cliquez sur Formes.
-  Sélectionnez ensuite le multidocument dans**Organigrammes**

![](multidocument.png)

***En utilisant Aspose.Cells***

Vous pouvez utiliser la méthode suivante pour insérer un multidocument dans la feuille de calcul.

{{% alert color="primary" %}}

[forme publique AddAutoShape(
 Type de forme automatique,
 int upperLeftRow,
 en haut,
 int upperLeftColumn,
 int gauche,
 hauteur int,
 largeur entière
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 La méthode retourne un[Façonner](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) objet.

{{% /alert %}}

L'exemple suivant montre comment insérer plusieurs documents dans une feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Multidocument.cs" >}}

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants :

![](multidocument2.png)



## **Insertion d'une étoile à cinq branches dans la feuille de calcul Excel dans C#**

 La forme de l'étoile à cinq branches appartient à la**Étoiles et bannières** Catégorie.

***Dans Microsoft Excel (par exemple 2007) :***

- Sélectionnez la cellule où vous souhaitez insérer l'étoile à cinq branches
- Cliquez sur le menu Insertion et cliquez sur Formes.
-  Ensuite, sélectionnez l'étoile à cinq branches de**Étoiles et bannières**

![](star_5_points.png)

***En utilisant Aspose.Cells***

Vous pouvez utiliser la méthode suivante pour insérer une étoile à cinq branches dans la feuille de calcul.

{{% alert color="primary" %}}

[forme publique AddAutoShape(
 Type de forme automatique,
 int upperLeftRow,
 en haut,
 int upperLeftColumn,
 int gauche,
 hauteur int,
 largeur entière
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 La méthode retourne un[Façonner](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) objet.

{{% /alert %}}

L'exemple suivant montre comment insérer une étoile à cinq branches dans une feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-FivePointedStar.cs" >}}

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants :

![](star_5_points2.png)



## **Insertion d'un nuage de bulles de pensée dans la feuille de calcul Excel dans C#**

 La forme du nuage de bulles de pensée appartient à la**Légendes** Catégorie.

***Dans Microsoft Excel (par exemple 2007) :***

- Sélectionnez la cellule dans laquelle vous souhaitez insérer le nuage de bulle de pensée
- Cliquez sur le menu Insertion et cliquez sur Formes.
-  Ensuite, sélectionnez le nuage de bulles de pensée à partir de**Légendes**

![](thought_bubble_cloud.png)

***En utilisant Aspose.Cells***

Vous pouvez utiliser la méthode suivante pour insérer un nuage de bulles de pensée dans la feuille de calcul.

{{% alert color="primary" %}}

[forme publique AddAutoShape(
 Type de forme automatique,
 int upperLeftRow,
 en haut,
 int upperLeftColumn,
 int gauche,
 hauteur int,
 largeur entière
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 La méthode retourne un[Façonner](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) objet.

{{% /alert %}}

L'exemple suivant montre comment insérer un nuage de bulles de pensée dans une feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.cs" >}}

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants :

![](thought_bubble_cloud2.png)

## **Sujets avancés**
- [Modifier les valeurs d'ajustement de la forme](/cells/fr/net/change-adjustment-values-of-the-shape/)
- [Copier des formes entre des feuilles de calcul](/cells/fr/net/copy-shapes-between-worksheets/)
- [Données sous forme non primitive](/cells/fr/net/data-in-non-primitive-shape/)
- [Recherche de la position absolue de la forme dans la feuille de calcul](/cells/fr/net/finding-absolute-position-of-shape-inside-the-worksheet/)
- [Obtenir des points de connexion à partir de la forme](/cells/fr/net/get-connection-points-from-shape/)
- [Gestion des contrôles](/cells/fr/net/managing-controls/)
- [Ajouter des icônes à la feuille de calcul](/cells/fr/net/insert-svg-to-excel/)
- [Gestion des objets OLE](/cells/fr/net/managing-ole-objects/)
- [Gestion des images](/cells/fr/net/managing-pictures/)
- [Gérer l'art intelligent](/cells/fr/net/managing-smartart/)
- [Gestion de la zone de texte](/cells/fr/net/managing-textbox-of-excel/)
- [Ajouter un filigrane WordArt à la feuille de calcul](/cells/fr/net/add-wordart-watermark-to-worksheet/)
- [Actualiser les valeurs des formes liées](/cells/fr/net/refresh-values-of-linked-shapes/)
- [Envoyer la forme avant ou arrière dans la feuille de calcul](/cells/fr/net/send-shape-front-or-back-inside-the-worksheet/)
- [Gérer les options de forme](/cells/fr/net/managing-shape-options/)
- [Gérer les options de texte de forme](/cells/fr/net/managing-shape-text-options/)
- [Extensions Web - Compléments Office](/cells/fr/net/web-extensions-office-add-ins/)

