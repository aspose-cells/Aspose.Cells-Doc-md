---
title: Insérer des formes dans la feuille de calcul dans Aspose.Cells
type: docs
weight: 5
url: /fr/java/insert-shapes-to-worksheet-in-aspose-cells/
---


{{% alert color="primary" %}}

Parfois, vous avez besoin d'insérer certaines formes nécessaires dans la feuille de calcul. Vous devrez peut-être insérer la même forme à différentes positions de la feuille de calcul. Ou vous devez insérer en lot des formes dans la feuille de calcul.

Ne vous inquiétez pas! [Aspose.Cells](https://products.aspose.com/cells/) prend en charge toutes ces opérations.

{{% /alert %}}

Les formes dans Excel sont principalement divisées en plusieurs types :
- **Lignes**
- **Rectangles**
- **Formes de base**
- **Flèches de base**
- **Formes d'équation**
- **Organigrammes**
- **Étoiles et bannières**
- **Appels**

Ce document guide sélectionnera une ou deux formes de chaque type pour en faire des échantillons. Grâce à ces exemples, vous apprendrez comment utiliser [Aspose.Cells](https://products.aspose.com/cells/) pour insérer la forme spécifiée dans la feuille de calcul.



## **Insérer une ligne dans la feuille de calcul**

La forme de la ligne appartient à la catégorie **lignes**.

***Dans Microsoft Excel (par exemple 2007) :***

- Sélectionnez la cellule où vous souhaitez insérer la ligne
- Cliquez sur le menu Insérer, puis sur Formes.
- Ensuite, sélectionnez la ligne dans 'Formes récemment utilisées' ou 'Lignes'

![](line.png)

***Utilisation d'Aspose.Cells***

Vous pouvez utiliser la méthode suivante pour insérer une ligne dans la feuille de calcul.

{{% alert color="primary" %}}

[**public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

La méthode renvoie un objet [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

L'exemple suivant montre comment insérer une ligne dans une feuille de calcul.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Line.java" >}}

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants:

![](line2.png)



## **Insérer une flèche de ligne dans la feuille de calcul**

La forme de la flèche de ligne appartient à la catégorie **Lignes**. C'est un cas spécial de ligne.

***Dans Microsoft Excel (par exemple 2007) :***

- Sélectionnez la cellule où vous souhaitez insérer la flèche de ligne
- Cliquez sur le menu Insérer, puis sur Formes.
- Ensuite, sélectionnez la flèche de ligne dans 'Formes récemment utilisées' ou 'Lignes'

![](line_arrow1.png)

***Utilisation d'Aspose.Cells***

Vous pouvez utiliser la méthode suivante pour insérer une flèche de ligne dans la feuille de calcul.

{{% alert color="primary" %}}

[**public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

La méthode renvoie un objet [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

L'exemple suivant montre comment insérer une flèche de ligne dans une feuille de calcul.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-LineArrow.java" >}}

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants:

![](line_arrow2.png)



## **Insérer un rectangle dans la feuille de calcul**

La forme du rectangle appartient à la catégorie **Rectangles**.

***Dans Microsoft Excel (par exemple 2007) :***

- Sélectionnez la cellule où vous souhaitez insérer le rectangle
- Cliquez sur le menu Insérer, puis sur Formes.
- Ensuite, sélectionnez le rectangle dans 'Formes récemment utilisées' ou 'Rectangles'

![](rectangle.png)

***Utilisation d'Aspose.Cells***

Vous pouvez utiliser la méthode suivante pour insérer un rectangle dans la feuille de calcul.

{{% alert color="primary" %}}

[**public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

La méthode renvoie un objet [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

L'exemple suivant montre comment insérer un rectangle dans une feuille de calcul.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Rectangle.java" >}}

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants:

![](rectangle2.png)



## **Insérer un cube dans la feuille de calcul**

La forme du cube appartient à la catégorie **Formes de base**.

***Dans Microsoft Excel (par exemple 2007) :***

- Sélectionnez la cellule où vous souhaitez insérer le cube
- Cliquez sur le menu Insérer, puis sur Formes.
- Ensuite, sélectionnez le cube dans la catégorie **Formes de base**

![](cube.png)

***Utilisation d'Aspose.Cells***

Vous pouvez utiliser la méthode suivante pour insérer un cube dans la feuille de calcul.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

La méthode renvoie un objet [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

L'exemple suivant montre comment insérer un cube dans une feuille de calcul.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Cube.java" >}}

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants:

![](cube2.png)



## **Insérer une flèche de repère quadri-directionnel dans la feuille de calcul**

La forme de la flèche de callout quad appartient à la catégorie **Block Arrows**.

***Dans Microsoft Excel (par exemple 2007) :***

- Sélectionnez la cellule où vous souhaitez insérer la flèche de callout quad
- Cliquez sur le menu Insérer, puis sur Formes.
- Ensuite, sélectionnez la flèche de callout quad dans **Block Arrows**

![](callout_quad_arrow.png)

***Utilisation d'Aspose.Cells***

Vous pouvez utiliser la méthode suivante pour insérer une flèche de callout quad dans la feuille de calcul.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

La méthode renvoie un objet [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

L'exemple suivant montre comment insérer une flèche de callout quad dans une feuille de calcul.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.java" >}}

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants:

![](callout_quad_arrow2.png)



## **Insérer un signe de multiplication dans la feuille de calcul**

La forme du signe de multiplication appartient à la catégorie **Equation Shapes**.

***Dans Microsoft Excel (par exemple 2007) :***

- Sélectionnez la cellule où vous souhaitez insérer le signe de multiplication
- Cliquez sur le menu Insérer, puis sur Formes.
- Ensuite, sélectionnez le signe de multiplication dans **Equation Shapes**

![](multiplication_sign.png)

***Utilisation d'Aspose.Cells***

Vous pouvez utiliser la méthode suivante pour insérer un signe de multiplication dans la feuille de calcul.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

La méthode renvoie un objet [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

L'exemple suivant montre comment insérer un signe de multiplication dans une feuille de calcul.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.java" >}}

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants:

![](multiplication_sign2.png)



## **Insérer un multidocument dans la feuille de calcul**

La forme du multimédia appartient à la catégorie **FlowCharts**.

***Dans Microsoft Excel (par exemple 2007) :***

- Sélectionnez la cellule où vous souhaitez insérer le multimédia
- Cliquez sur le menu Insérer, puis sur Formes.
- Ensuite, sélectionnez le multimédia de la catégorie **FlowCharts**

![](multidocument.png)

***Utilisation d'Aspose.Cells***

Vous pouvez utiliser la méthode suivante pour insérer un multimédia dans la feuille de calcul.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

La méthode renvoie un objet [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

L'exemple suivant montre comment insérer un multimédia dans une feuille de calcul.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Multidocument.java" >}}

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants:

![](multidocument2.png)



## **Insérer une étoile à cinq branches dans la feuille de calcul**

La forme de l'étoile à cinq branches appartient à la catégorie **Étoiles et bannières**.

***Dans Microsoft Excel (par exemple 2007) :***

- Sélectionnez la cellule où vous souhaitez insérer l'étoile à cinq branches
- Cliquez sur le menu Insérer, puis sur Formes.
- Ensuite, sélectionnez l'étoile à cinq branches dans la catégorie **Étoiles et bannières**

![](star_5_points.png)

***Utilisation d'Aspose.Cells***

Vous pouvez utiliser la méthode suivante pour insérer une étoile à cinq branches dans la feuille de calcul.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

La méthode renvoie un objet [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

L'exemple suivant montre comment insérer une étoile à cinq branches dans une feuille de calcul.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-FivePointedStar.java" >}}

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants:

![](star_5_points2.png)



## **Insérer un nuage de bulles de pensée dans la feuille de calcul**

La forme du nuage de bulles de pensée appartient à la catégorie **Appels**.

***Dans Microsoft Excel (par exemple 2007) :***

- Sélectionnez la cellule où vous souhaitez insérer le nuage de bulles de pensée
- Cliquez sur le menu Insérer, puis sur Formes.
- Ensuite, sélectionnez le nuage de bulles de pensée dans **Callouts**

![](thought_bubble_cloud.png)

***Utilisation d'Aspose.Cells***

Vous pouvez utiliser la méthode suivante pour insérer un nuage de bulles de pensée dans la feuille de calcul.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

La méthode renvoie un objet [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

L'exemple suivant montre comment insérer un nuage de bulles de pensée dans une feuille de calcul.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.java" >}}

Exécutez le code ci-dessus, vous obtiendrez les résultats suivants:

![](thought_bubble_cloud2.png)
