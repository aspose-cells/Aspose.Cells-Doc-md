---
title: Insérer des images et des formes de fichiers Excel.
linktitle: Formes
type: docs
weight: 140
url: /fr/net/insert-shapes/
description: Gérer des images, des objets OLE, des formes dans les fichiers Excel.
---

{{% alert color="primary" %}}

Parfois, vous avez besoin d'insérer certaines formes nécessaires dans la feuille de calcul. Vous devrez peut-être insérer la même forme à différentes positions de la feuille de calcul. Ou vous devez insérer en lot des formes dans la feuille de calcul.

Ne vous inquiétez pas! [Aspose.Cells](https://products.aspose.com/cells/) prend en charge toutes ces opérations.

{{% /alert %}}

Les formes dans Excel sont principalement divisées en plusieurs types :
- **Images**
- **Objets OLE**
- **Lignes**
- **Rectangles**
- **Formes de base**
- **Flèches de base**
- **Formes d'équation**
- **Organigrammes**
- **Étoiles et bannières**
- **Appels**

Ce document guide sélectionnera une ou deux formes de chaque type pour en faire des échantillons. Grâce à ces exemples, vous apprendrez comment utiliser [Aspose.Cells](https://products.aspose.com/cells/) pour insérer la forme spécifiée dans la feuille de calcul.

## **Ajouter des images dans une feuille de calcul Excel en C#**

Ajouter des images à une feuille de calcul est très facile. Il suffit de quelques lignes de code :
Il suffit d’appeler la méthode [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) de la collection [**Pictures**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection) (encapsulée dans l’objet [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)). La méthode [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) prend les paramètres suivants :

- **Index de la ligne supérieure gauche**, l'index de la ligne supérieure gauche.
- **Index de la colonne supérieure gauche**, l'index de la colonne supérieure gauche.
- **Nom du fichier image**, le nom du fichier image, complet avec le chemin.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-AddingPictures-1.cs" >}}


## **Insertion d'objets OLE dans une feuille de calcul Excel en C#**

Aspose.Cells prend en charge l'ajout, l'extraction et la manipulation des objets OLE dans les feuilles de calcul. Pour cette raison, Aspose.Cells possède la classe [**OleObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobjectcollection), utilisée pour ajouter un nouvel objet OLE à la liste de collections. Une autre classe, [**OleObject**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject), représente un objet OLE. Elle contient des membres importants.

- La propriété [**ImageData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/imagedata) spécifie les données d'image (icône) de type tableau d'octets. L'image sera affichée pour montrer l'objet OLE dans la feuille de calcul.
- La propriété [**ObjectData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/objectdata) spécifie les données d'objet sous forme d'un tableau d'octets. Ces données seront affichées dans leur programme associé lorsque vous double-cliquez sur l'icône d'objet OLE.

L'exemple suivant montre comment ajouter un ou des objets OLE dans une feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-InsertingOLEObjects-1.cs" >}}

## **Insérer une ligne dans une feuille de calcul Excel en C#**

La forme de la ligne appartient à la catégorie **lignes**.

***Dans Microsoft Excel (par exemple 2007) :***

- Sélectionnez la cellule où vous souhaitez insérer la ligne
- Cliquez sur le menu Insérer, puis sur Formes.
- Ensuite, sélectionnez la ligne dans 'Formes récemment utilisées' ou 'Lignes'

![](line.png)

***Utilisation d'Aspose.Cells***

Vous pouvez utiliser la méthode suivante pour insérer une ligne dans la feuille de calcul.

{{% alert color="primary" %}}

[**public LineShape AddLine(int upperLeftRow, int top, int upperLeftColumn, int left,	int height,	int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)

La méthode renvoie un objet [LineShape](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape).

{{% /alert %}}

L'exemple suivant montre comment insérer une ligne dans une feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Line.cs" >}}

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants:

![](line2.png)



## **Insérer une flèche de ligne dans une feuille de calcul Excel en C#**

La forme de la flèche de ligne appartient à la catégorie **Lignes**. C'est un cas spécial de ligne.

***Dans Microsoft Excel (par exemple 2007) :***

- Sélectionnez la cellule où vous souhaitez insérer la flèche de ligne
- Cliquez sur le menu Insérer, puis sur Formes.
- Ensuite, sélectionnez la flèche de ligne dans 'Formes récemment utilisées' ou 'Lignes'

![](line_arrow1.png)

***Utilisation d'Aspose.Cells***

Vous pouvez utiliser la méthode suivante pour insérer une flèche de ligne dans la feuille de calcul.

{{% alert color="primary" %}}

[**public LineShape AddLine(int upperLeftRow, int top, int upperLeftColumn,	int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)

La méthode renvoie un objet [LineShape](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape).

{{% /alert %}}

L'exemple suivant montre comment insérer une flèche de ligne dans une feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-LineArrow.cs" >}}

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants:

![](line_arrow2.png)



## **Insérer un rectangle dans une feuille de calcul Excel en C#**

La forme du rectangle appartient à la catégorie **Rectangles**.

***Dans Microsoft Excel (par exemple 2007) :***

- Sélectionnez la cellule où vous souhaitez insérer le rectangle
- Cliquez sur le menu Insérer, puis sur Formes.
- Ensuite, sélectionnez le rectangle dans 'Formes récemment utilisées' ou 'Rectangles'

![](rectangle.png)

***Utilisation d'Aspose.Cells***

Vous pouvez utiliser la méthode suivante pour insérer un rectangle dans la feuille de calcul.

{{% alert color="primary" %}}

[**public RectangleShape AddRectangle(int upperLeftRow,	int top, int upperLeftColumn, int left,	int height,	int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle)

La méthode renvoie un objet [RectangleShape](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape).

{{% /alert %}}

L'exemple suivant montre comment insérer un rectangle dans une feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Rectangle.cs" >}}

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants:

![](rectangle2.png)



## **Insérer un cube dans une feuille de calcul Excel en C#**

La forme du cube appartient à la catégorie **Formes de base**.

***Dans Microsoft Excel (par exemple 2007) :***

- Sélectionnez la cellule où vous souhaitez insérer le cube
- Cliquez sur le menu Insérer, puis sur Formes.
- Ensuite, sélectionnez le cube dans la catégorie **Formes de base**

![](cube.png)

***Utilisation d'Aspose.Cells***

Vous pouvez utiliser la méthode suivante pour insérer un cube dans la feuille de calcul.

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

La méthode renvoie un objet [Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape).

{{% /alert %}}

L'exemple suivant montre comment insérer un cube dans une feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Cube.cs" >}}

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants:

![](cube2.png)



## **Insérer une flèche quadruple de légende dans une feuille de calcul Excel en C#**

La forme de la flèche de callout quad appartient à la catégorie **Block Arrows**.

***Dans Microsoft Excel (par exemple 2007) :***

- Sélectionnez la cellule où vous souhaitez insérer la flèche de callout quad
- Cliquez sur le menu Insérer, puis sur Formes.
- Ensuite, sélectionnez la flèche de callout quad dans **Block Arrows**

![](callout_quad_arrow.png)

***Utilisation d'Aspose.Cells***

Vous pouvez utiliser la méthode suivante pour insérer une flèche de callout quad dans la feuille de calcul.

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

La méthode renvoie un objet [Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape).

{{% /alert %}}

L'exemple suivant montre comment insérer une flèche de callout quad dans une feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.cs" >}}

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants:

![](callout_quad_arrow2.png)



## **Insérer un signe de multiplication dans la feuille de calcul Excel en C#**

La forme du signe de multiplication appartient à la catégorie **Equation Shapes**.

***Dans Microsoft Excel (par exemple 2007) :***

- Sélectionnez la cellule où vous souhaitez insérer le signe de multiplication
- Cliquez sur le menu Insérer, puis sur Formes.
- Ensuite, sélectionnez le signe de multiplication dans **Equation Shapes**

![](multiplication_sign.png)

***Utilisation d'Aspose.Cells***

Vous pouvez utiliser la méthode suivante pour insérer un signe de multiplication dans la feuille de calcul.

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

La méthode renvoie un objet [Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape).

{{% /alert %}}

L'exemple suivant montre comment insérer un signe de multiplication dans une feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.cs" >}}

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants:

![](multiplication_sign2.png)



## **Insertion d'un multimédia dans une feuille de calcul Excel en C#**

La forme du multimédia appartient à la catégorie **FlowCharts**.

***Dans Microsoft Excel (par exemple 2007) :***

- Sélectionnez la cellule où vous souhaitez insérer le multimédia
- Cliquez sur le menu Insérer, puis sur Formes.
- Ensuite, sélectionnez le multimédia de la catégorie **FlowCharts**

![](multidocument.png)

***Utilisation d'Aspose.Cells***

Vous pouvez utiliser la méthode suivante pour insérer un multimédia dans la feuille de calcul.

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

La méthode renvoie un objet [Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape).

{{% /alert %}}

L'exemple suivant montre comment insérer un multimédia dans une feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Multidocument.cs" >}}

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants:

![](multidocument2.png)



## **Insérer une étoile à cinq branches dans une feuille de calcul Excel en C#**

La forme de l'étoile à cinq branches appartient à la catégorie **Étoiles et bannières**.

***Dans Microsoft Excel (par exemple 2007) :***

- Sélectionnez la cellule où vous souhaitez insérer l'étoile à cinq branches
- Cliquez sur le menu Insérer, puis sur Formes.
- Ensuite, sélectionnez l'étoile à cinq branches dans la catégorie **Étoiles et bannières**

![](star_5_points.png)

***Utilisation d'Aspose.Cells***

Vous pouvez utiliser la méthode suivante pour insérer une étoile à cinq branches dans la feuille de calcul.

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

La méthode renvoie un objet [Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape).

{{% /alert %}}

L'exemple suivant montre comment insérer une étoile à cinq branches dans une feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-FivePointedStar.cs" >}}

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants:

![](star_5_points2.png)



## **Insérer un nuage de bulles de pensée dans une feuille de calcul Excel en C#**

La forme du nuage de bulles de pensée appartient à la catégorie **Appels**.

***Dans Microsoft Excel (par exemple 2007) :***

- Sélectionnez la cellule où vous souhaitez insérer le nuage de bulles de pensée
- Cliquez sur le menu Insérer, puis sur Formes.
- Ensuite, sélectionnez le nuage de bulles de pensée dans **Callouts**

![](thought_bubble_cloud.png)

***Utilisation d'Aspose.Cells***

Vous pouvez utiliser la méthode suivante pour insérer un nuage de bulles de pensée dans la feuille de calcul.

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

La méthode renvoie un objet [Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape).

{{% /alert %}}

L'exemple suivant montre comment insérer un nuage de bulles de pensée dans une feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.cs" >}}

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants:

![](thought_bubble_cloud2.png)

## **Sujets avancés**
- [Modifier les valeurs d'ajustement de la forme](/cells/fr/net/change-adjustment-values-of-the-shape/)
- [Copier des formes entre les feuilles de calcul](/cells/fr/net/copy-shapes-between-worksheets/)
- [Données dans une forme non primitive](/cells/fr/net/data-in-non-primitive-shape/)
- [Trouver la position absolue de la forme dans la feuille de calcul](/cells/fr/net/finding-absolute-position-of-shape-inside-the-worksheet/)
- [Obtenir les points de connexion de la forme](/cells/fr/net/get-connection-points-from-shape/)
- [Gestion des contrôles](/cells/fr/net/managing-controls/)
- [Ajouter des icônes à la feuille de calcul](/cells/fr/net/insert-svg-to-excel/)
- [Gestion des objets OLE](/cells/fr/net/managing-ole-objects/)
- [Gestion des images](/cells/fr/net/managing-pictures/)
- [Gérer les Smart Art](/cells/fr/net/managing-smartart/)
- [Gestion de la zone de texte](/cells/fr/net/managing-textbox-of-excel/)
- [Ajouter un filigrane WordArt à la feuille de calcul](/cells/fr/net/add-wordart-watermark-to-worksheet/)
- [Actualiser les valeurs des formes liées](/cells/fr/net/refresh-values-of-linked-shapes/)
- [Envoyer la forme à l'avant ou à l'arrière dans la feuille de calcul](/cells/fr/net/send-shape-front-or-back-inside-the-worksheet/)
- [Gérer les options de la forme](/cells/fr/net/managing-shape-options/)
- [Gérer les options de texte de la forme](/cells/fr/net/managing-shape-text-options/)
- [Extensions Web - Compléments Office](/cells/fr/net/web-extensions-office-add-ins/)

{{< app/cells/assistant language="csharp" >}}
