---
title: Contrôles dans les graphiques
linktitle: Formes dans le graphique
type: docs
weight: 60
url: /fr/java/controls-in-charts/
---

{{% alert color="primary" %}}

Parfois, vous avez besoin d'insérer des objets de dessin comme des étiquettes, des boîtes de texte, des images, etc. dans un graphique. Aspose.Cells peut ajouter les contrôles à un graphique à l'exécution.

{{% /alert %}}

## **Ajout de contrôle d'étiquette au graphique**

Les étiquettes fournissent un moyen de fournir des informations aux utilisateurs sur le contenu d'une feuille de calcul. Aspose.Cells vous permet d'ajouter et de manipuler des étiquettes même dans les graphiques.

La classe [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) fournit une méthode nommée [**addLabelInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLabelInChart(int,%20int,%20int,%20int)), utilisée pour ajouter un contrôle d'étiquette à un graphique. Ci-dessous se trouve une liste des paramètres utilisés pour la méthode:

- **haut** – le décalage vertical de l'étiquette depuis le coin supérieur gauche en unités de 1/4000 de la zone du graphique.
- **gauche** – le décalage horizontal de l'étiquette depuis le coin supérieur gauche en unités de 1/4000 de la zone du graphique.
- **hauteur** – la hauteur de l'étiquette, en unités de 1/4000 de la zone du graphique.
- **largeur** – la largeur de l'étiquette, en unités de 1/4000 de la zone du graphique.

La méthode retourne un objet de la classe [**Label**](https://reference.aspose.com/cells/java/com.aspose.cells/Label), où la classe [**Label**](https://reference.aspose.com/cells/java/com.aspose.cells/Label) représente une étiquette dans le graphique. Elle possède des membres importants détaillés ci-dessous :

- La propriété [**Text**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Text) spécifie une chaîne de légende d'étiquette.
- La propriété [**Fill**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Fill) spécifie les attributs de couleur de remplissage.

L'exemple suivant montre comment ajouter une étiquette au graphique. L'exemple utilise un fichier de concepteur qui contient un graphique. Nous utilisons ce fichier pour insérer une étiquette dans le graphique.

Ci-dessous, une capture d'écran du fichier de concepteur.

**Le graphique du designer**

![todo:image_alt_text](controls-in-charts_1.png)

Ci-dessous se trouve le code original pour ajouter une étiquette au graphique. La sortie suivante est générée lors de l'exécution du code.

**Une étiquette est ajoutée dans le graphique**

![todo:image_alt_text](controls-in-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingLabelControl-AddingLabelControl.java" >}}

## **Ajout d'un contrôle TextBox au graphique**

Une manière de mettre en évidence des informations importantes dans un rapport est d'utiliser une zone de texte. Par exemple, saisissez du texte pour mettre en valeur le nom de l'entreprise ou pour indiquer la région géographique avec le plus de ventes. La classe [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) fournit une méthode appelée [**addTextBoxInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addTextBoxInChart(int,%20int,%20int,%20int)), qui est utilisée pour ajouter un contrôle de zone de texte à un graphique. Voici la liste des paramètres utilisés pour la méthode :

- **top** - le décalage vertical de la zone de texte depuis le coin supérieur gauche en unités de 1/4000 de la zone du graphique.
- **gauche** – le décalage vertical de la zone de texte du coin supérieur gauche en unités de 1/4000 de la zone du graphique.
- **height** - la hauteur de la zone de texte, en unités de 1/4000 de la zone du graphique.
- **width** - la largeur de la zone de texte, en unités de 1/4000 de la zone du graphique.

La méthode renvoie un objet de la classe [**TextBox**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox) où la classe [**TextBox**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox) représente une zone de texte dans le graphique.

L'exemple suivant montre comment ajouter une zone de texte à un graphique. L'exemple utilise le fichier de conception précédent qui contient un graphique. Nous utilisons ce fichier pour insérer une zone de texte dans le graphique afin d'afficher le titre du graphique.

Ci-dessous se trouve le code original pour ajouter une zone de texte au graphique. La sortie suivante est générée lors de l'exécution du code.

**Une zone de texte est ajoutée dans le graphique**

![todo:image_alt_text](controls-in-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingTextBoxControl-AddingTextBoxControl.java" >}}

## **Ajout d'une image au graphique**

Aspose.Cells vous permet d'insérer des images dans un graphique. Par exemple, ajoutez une image pour mettre en avant ou donner plus de sens à un graphique ou à son contenu, ou insérez un fichier image de marque.

La classe [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) fournit une méthode nommée [**addPictureInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPictureInChart(int,%20int,%20java.io.InputStream,%20int,%20int)), qui est utilisée pour ajouter un objet image au graphique. Voici la liste des paramètres utilisés pour la méthode :

- **top** - le décalage vertical de l'image depuis le coin supérieur gauche en unités de 1/4000 de la zone du graphique.
- **left** - le décalage vertical de l'image depuis le coin supérieur gauche en unités de 1/4000 de la zone du graphique.
- **stream** - un objet flux qui contient les données de l'image.
- **widthScale** - l'échelle de la largeur de l'image, une valeur en pourcentage.
- **heightScale** - l'échelle de la hauteur de l'image, une valeur en pourcentage.

La méthode renvoie un objet de la classe [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture) où la classe [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture) représente un objet image dans le graphique.

L'exemple suivant montre comment ajouter une image au graphique. L'exemple utilise le fichier de conception précédent qui contient un graphique. Nous utilisons ce fichier pour insérer une image dans le graphique.

Ci-dessous se trouve le code original pour ajouter une image au graphique. La sortie suivante est générée lors de l'exécution du code

**Une image est insérée dans le graphique**

![todo:image_alt_text](controls-in-charts_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingPictureToChart-AddingPictureToChart.java" >}}

## **Ajout d'une case à cocher dans le graphique**

Aspose.Cells vous permet d'insérer des cases à cocher dans une feuille de graphique en utilisant l'énumération [**MsoDrawingType**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoDrawingType). L'exemple suivant démontre l'ajout d'une case à cocher à une feuille de graphique.

L'image suivante montre la feuille de graphique avec la case à cocher dans le fichier de sortie.

![todo:image_alt_text](controls-in-charts_5.jpg)

Le [fichier de sortie](InsertCheckboxInChartSheet_out.xlsx) généré par le code suivant est joint à titre indicatif.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-InsertCheckboxInChartSheet-1.java" >}}
