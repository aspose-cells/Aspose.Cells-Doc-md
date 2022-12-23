---
title: Insérer des formes dans la feuille de calcul dans Aspose.Cells
type: docs
weight: 5
url: /fr/java/insert-shapes-to-worksheet-in-aspose-cells/
---
{{% alert color="primary" %}}

Parfois, vous devez insérer certaines formes nécessaires dans la feuille de calcul. Vous devrez peut-être insérer la même forme dans différentes positions de la feuille de calcul. Ou vous devez insérer des formes par lots dans la feuille de calcul.

 Ne t'en fais pas![Aspose.Cells](https://products.aspose.com/cells/)prend en charge toutes ces opérations.

{{% /alert %}}

Les formes dans Excel sont principalement divisées en types suivants :
- **Lignes**
- **rectangles**
- **Formes de base**
- **Bloquer les flèches**
- **Formes d'équation**
- **Organigrammes**
- **Étoiles et bannières**
- **Légendes**

 Ce document guide sélectionnera une ou deux formes de chaque type pour créer des échantillons. Grâce à ces exemples, vous apprendrez à utiliser[Aspose.Cells](https://products.aspose.com/cells/) pour insérer la forme spécifiée dans la feuille de calcul.



## **Insertion d'une ligne dans la feuille de calcul**

 La forme de la ligne appartient à la**lignes** Catégorie.

***Dans Microsoft Excel (par exemple 2007) :***

- Sélectionnez la cellule où vous voulez insérer la ligne
- Cliquez sur le menu Insertion et cliquez sur Formes.
- Ensuite, sélectionnez la ligne dans "Formes récemment utilisées" ou "Lignes"

![](line.png)

***En utilisant Aspose.Cells***

Vous pouvez utiliser la méthode suivante pour insérer une ligne dans la feuille de calcul.

{{% alert color="primary" %}}

[public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 La méthode retourne un[Façonner](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) objet.

{{% /alert %}}

L'exemple suivant montre comment insérer une ligne dans une feuille de calcul.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Line.java" >}}

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants :

![](line2.png)



## **Insertion d'une flèche de ligne dans la feuille de calcul**

 La forme de la flèche de ligne appartient à la**Lignes** catégorie. C'est un cas particulier de ligne.

***Dans Microsoft Excel (par exemple 2007) :***

- Sélectionnez la cellule où vous souhaitez insérer la flèche de ligne
- Cliquez sur le menu Insertion et cliquez sur Formes.
- Ensuite, sélectionnez la flèche de ligne dans "Formes récemment utilisées" ou "Lignes"

![](line_arrow1.png)

***En utilisant Aspose.Cells***

Vous pouvez utiliser la méthode suivante pour insérer une flèche de ligne dans la feuille de calcul.

{{% alert color="primary" %}}

[public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 La méthode retourne un[Façonner](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) objet.

{{% /alert %}}

L'exemple suivant montre comment insérer une flèche de ligne dans une feuille de calcul.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-LineArrow.java" >}}

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants :

![](line_arrow2.png)



## **Insertion d'un rectangle dans la feuille de calcul**

 La forme du rectangle appartient à la**rectangles** Catégorie.

***Dans Microsoft Excel (par exemple 2007) :***

- Sélectionnez la cellule où vous souhaitez insérer le rectangle
- Cliquez sur le menu Insertion et cliquez sur Formes.
- Ensuite, sélectionnez le rectangle dans "Formes récemment utilisées" ou "Rectangles"

![](rectangle.png)

***En utilisant Aspose.Cells***

Vous pouvez utiliser la méthode suivante pour insérer un rectangle dans la feuille de calcul.

{{% alert color="primary" %}}

[public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 La méthode retourne un[Façonner](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) objet.

{{% /alert %}}

L'exemple suivant montre comment insérer un rectangle dans une feuille de calcul.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Rectangle.java" >}}

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants :

![](rectangle2.png)



## **Insertion d'un cube dans une feuille de calcul**

La forme du cube appartient à la**Formes de base** Catégorie.

***Dans Microsoft Excel (par exemple 2007) :***

- Sélectionnez la cellule où vous souhaitez insérer le cube
- Cliquez sur le menu Insertion et cliquez sur Formes.
-  Ensuite, sélectionnez le cube à partir de**Formes de base**

![](cube.png)

***En utilisant Aspose.Cells***

Vous pouvez utiliser la méthode suivante pour insérer un cube dans la feuille de calcul.

{{% alert color="primary" %}}

[public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 La méthode retourne un[Façonner](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) objet.

{{% /alert %}}

L'exemple suivant montre comment insérer un cube dans une feuille de calcul.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Cube.java" >}}

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants :

![](cube2.png)



## **Insertion d'une flèche quadruple de légende dans la feuille de calcul**

 La forme de la flèche quadruple de la légende appartient au**Bloquer les flèches** Catégorie.

***Dans Microsoft Excel (par exemple 2007) :***

- Sélectionnez la cellule dans laquelle vous souhaitez insérer la flèche quadruple de la légende
- Cliquez sur le menu Insertion et cliquez sur Formes.
-  Ensuite, sélectionnez la flèche quadruple de la légende à partir de**Bloquer les flèches**

![](callout_quad_arrow.png)

***En utilisant Aspose.Cells***

Vous pouvez utiliser la méthode suivante pour insérer une flèche quadruple de légende dans la feuille de calcul.

{{% alert color="primary" %}}

[public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 La méthode retourne un[Façonner](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) objet.

{{% /alert %}}

L'exemple suivant montre comment insérer une flèche quadruple de légende dans une feuille de calcul.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.java" >}}

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants :

![](callout_quad_arrow2.png)



## **Insertion d'un signe de multiplication dans la feuille de travail**

 La forme du signe de multiplication appartient au**Formes d'équation** Catégorie.

***Dans Microsoft Excel (par exemple 2007) :***

- Sélectionnez la cellule où vous souhaitez insérer le signe de multiplication
- Cliquez sur le menu Insertion et cliquez sur Formes.
-  Ensuite, sélectionnez le signe de multiplication de**Formes d'équation**

![](multiplication_sign.png)

***En utilisant Aspose.Cells***

Vous pouvez utiliser la méthode suivante pour insérer un signe de multiplication dans la feuille de calcul.

{{% alert color="primary" %}}

[public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 La méthode retourne un[Façonner](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) objet.

{{% /alert %}}

L'exemple suivant montre comment insérer un signe de multiplication dans une feuille de calcul.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.java" >}}

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants :

![](multiplication_sign2.png)



## **Insertion d'un multidocument dans Worksheet**

 La forme de multidocument appartient à la**Organigrammes** Catégorie.

***Dans Microsoft Excel (par exemple 2007) :***

- Sélectionnez la cellule où vous souhaitez insérer le multidocument
- Cliquez sur le menu Insertion et cliquez sur Formes.
-  Sélectionnez ensuite le multidocument dans**Organigrammes**

![](multidocument.png)

***En utilisant Aspose.Cells***

Vous pouvez utiliser la méthode suivante pour insérer un multidocument dans la feuille de calcul.

{{% alert color="primary" %}}

[public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 La méthode retourne un[Façonner](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) objet.

{{% /alert %}}

L'exemple suivant montre comment insérer plusieurs documents dans une feuille de calcul.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Multidocument.java" >}}

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants :

![](multidocument2.png)



## **Insertion d'une étoile à cinq branches dans la feuille de calcul**

 La forme de l'étoile à cinq branches appartient à la**Étoiles et bannières** Catégorie.

***Dans Microsoft Excel (par exemple 2007) :***

- Sélectionnez la cellule où vous souhaitez insérer l'étoile à cinq branches
- Cliquez sur le menu Insertion et cliquez sur Formes.
-  Ensuite, sélectionnez l'étoile à cinq branches de**Étoiles et bannières**

![](star_5_points.png)

***En utilisant Aspose.Cells***

Vous pouvez utiliser la méthode suivante pour insérer une étoile à cinq branches dans la feuille de calcul.

{{% alert color="primary" %}}

[public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 La méthode retourne un[Façonner](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) objet.

{{% /alert %}}

L'exemple suivant montre comment insérer une étoile à cinq branches dans une feuille de calcul.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-FivePointedStar.java" >}}

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants :

![](star_5_points2.png)



## **Insertion d'un nuage de bulles de pensée dans la feuille de calcul**

 La forme du nuage de bulles de pensée appartient à la**Légendes** Catégorie.

***Dans Microsoft Excel (par exemple 2007) :***

- Sélectionnez la cellule dans laquelle vous souhaitez insérer le nuage de bulle de pensée
- Cliquez sur le menu Insertion et cliquez sur Formes.
-  Ensuite, sélectionnez le nuage de bulles de pensée à partir de**Légendes**

![](thought_bubble_cloud.png)

***En utilisant Aspose.Cells***

Vous pouvez utiliser la méthode suivante pour insérer un nuage de bulles de pensée dans la feuille de calcul.

{{% alert color="primary" %}}

[public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 La méthode retourne un[Façonner](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) objet.

{{% /alert %}}

L'exemple suivant montre comment insérer un nuage de bulles de pensée dans une feuille de calcul.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.java" >}}

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants :

![](thought_bubble_cloud2.png)
