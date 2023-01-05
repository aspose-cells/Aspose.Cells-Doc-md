---
title: Contrôles dans les graphiques
linktitle: Formes dans le graphique
type: docs
weight: 60
url: /fr/java/controls-in-charts/
---
{{% alert color="primary" %}}

Parfois, vous devez insérer des objets de dessin tels que des étiquettes, des zones de texte, des images, etc. dans un graphique. Aspose.Cells peut ajouter les contrôles à un graphique lors de l'exécution.

{{% /alert %}}

## **Ajout d'un contrôle d'étiquette au graphique**

Les libellés permettent de fournir des informations aux utilisateurs sur le contenu d'une feuille de calcul. Aspose.Cells vous permet d'ajouter et de manipuler des étiquettes même dans les graphiques.

 Le[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) classe fournit une méthode nommée[**addLabelInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLabelInChart(int,%20int,%20int,%20int)), utilisé pour ajouter un contrôle d'étiquette à un graphique. Voici une liste des paramètres utilisés pour la méthode :

- **Haut** – le décalage vertical de l'étiquette à partir du coin supérieur gauche en unités de 1/4000 de la zone du graphique.
- **gauche** – le décalage vertical de l'étiquette à partir du coin supérieur gauche en unités de 1/4000 de la zone du graphique.
- **la taille** – la hauteur de l'étiquette, en unités de 1/4000 de la surface du graphique.
- **largeur** – la largeur de l'étiquette, en unités de 1/4000 de la surface du graphique.

 La méthode renvoie un objet de la[**Étiquette**](https://reference.aspose.com/cells/java/com.aspose.cells/Label) classe, où le[**Étiquette**](https://reference.aspose.com/cells/java/com.aspose.cells/Label)class représente une étiquette dans le graphique. Il a quelques membres importants comme détaillé ci-dessous:

- [**Texte**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Text)La propriété spécifie la chaîne de légende d'une étiquette.
- [**Remplir**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Fill) La propriété spécifie les attributs de couleur de remplissage.

L'exemple suivant montre comment ajouter une étiquette au graphique. L'exemple utilise un fichier de concepteur contenant un graphique. Nous utilisons ce fichier pour insérer une étiquette dans le graphique.

Vous trouverez ci-dessous une capture d'écran du fichier de concepteur.

**La charte du créateur**

![tâche : image_autre_texte](controls-in-charts_1.png)

Vous trouverez ci-dessous le code d'origine pour ajouter une étiquette au graphique. La sortie suivante est générée lors de l'exécution du code.

**Une étiquette est ajoutée dans le graphique**

![tâche : image_autre_texte](controls-in-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingLabelControl-AddingLabelControl.java" >}}

## **Ajout du contrôle TextBox au graphique**

 Une façon de mettre en évidence des informations importantes dans un rapport consiste à utiliser une zone de texte. Par exemple, saisissez du texte pour mettre en surbrillance le nom de l'entreprise ou pour indiquer la région géographique avec les ventes les plus élevées. Le[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) classe fournit une méthode nommée[**addTextBoxInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addTextBoxInChart(int,%20int,%20int,%20int)), qui est utilisé pour ajouter un contrôle de zone de texte à un graphique. Voici la liste des paramètres utilisés pour la méthode :

- **Haut** – le décalage vertical de la zone de texte à partir du coin supérieur gauche en unités de 1/4000 de la zone du graphique.
- **gauche** – le décalage vertical de la zone de texte à partir du coin supérieur gauche en unités de 1/4000 de la zone du graphique.
- **la taille**– la hauteur de la zone de texte, en unités de 1/4000 de la zone du graphique.
- **largeur** – la largeur de la zone de texte, en unités de 1/4000 de la zone du graphique.

 La méthode renvoie un objet de la[**Zone de texte**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox) classe où le[**Zone de texte**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox)la classe représente une zone de texte dans le graphique.

L'exemple suivant montre comment ajouter une zone de texte à un graphique. L'exemple utilise le fichier de concepteur précédent qui contient un graphique. Nous utilisons ce fichier pour insérer une zone de texte dans le graphique afin d'afficher le titre du graphique.

Vous trouverez ci-dessous le code d'origine pour ajouter une zone de texte au graphique. La sortie suivante est générée lors de l'exécution du code.

**Une zone de texte est ajoutée dans le graphique**

![tâche : image_autre_texte](controls-in-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingTextBoxControl-AddingTextBoxControl.java" >}}

## **Ajouter une image au graphique**

Aspose.Cells vous permet d'insérer des images dans un graphique. Par exemple, ajoutez une image pour souligner ou donner plus de sens à un graphique ou à son contenu, ou insérez un fichier d'image de marque.

 Le[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) classe fournit une méthode nommée[**addPictureInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPictureInChart(int,%20int,%20java.io.InputStream,%20int,%20int)), qui est utilisé pour ajouter un objet image au graphique. Voici la liste des paramètres utilisés pour la méthode :

- **Haut**– le décalage vertical de l'image par rapport au coin supérieur gauche en unités de 1/4000 de la zone de carte.
- **gauche**– le décalage vertical de l'image par rapport au coin supérieur gauche en unités de 1/4000 de la zone de carte.
- **flux** – un objet flux qui contient les données d'image.
- **Échellelargeur** – l'échelle de la largeur de l'image, une valeur en pourcentage.
- **Échelle de hauteur** – l'échelle de la hauteur de l'image, une valeur en pourcentage.

 La méthode renvoie un objet de la[**Photo**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture) classe où le[**Photo**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)La classe représente un objet image dans le graphique.

L'exemple suivant montre comment ajouter une image au graphique. L'exemple utilise le fichier de concepteur précédent qui contient un graphique. Nous utilisons ce fichier pour insérer une image dans le graphique.

Vous trouverez ci-dessous le code d'origine pour ajouter une image au graphique. La sortie suivante est générée lors de l'exécution du code

**Une image est insérée dans le graphique**

![tâche : image_autre_texte](controls-in-charts_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingPictureToChart-AddingPictureToChart.java" >}}

## **Ajouter une case à cocher dans le graphique**

Aspose.Cells vous permet d'insérer des cases à cocher dans une feuille de graphique en utilisant[**MsoDrawingTypeMsoDrawingType**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoDrawingType) énumération. L'exemple suivant illustre l'ajout d'une case à cocher à une feuille de graphique.

L'image suivante montre la feuille de graphique avec la case à cocher dans le fichier de sortie.

![tâche : image_autre_texte](controls-in-charts_5.jpg)

Le[fichier de sortie](InsertCheckboxInChartSheet_out.xlsx)généré par l'extrait de code suivant est joint pour votre référence.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-InsertCheckboxInChartSheet-1.java" >}}
