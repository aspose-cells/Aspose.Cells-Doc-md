---
title: Formes dans les graphiques
description: Découvrez comment utiliser Aspose.Cells for .NET pour ajouter des contrôles et personnaliser des graphiques dans Microsoft Excel. Notre guide vous montrera comment manipuler les éléments du graphique, ajuster le formatage et améliorer l'apparence générale et la convivialité de vos graphiques.
keywords: Aspose.Cells for .NET, Chart Controls, Chart Customization, Microsoft Excel, Chart Elements, Formatting.
type: docs
weight: 70
url: /fr/net/controls-in-charts/
---
{{% alert color="primary" %}}

Parfois, vous devez insérer des objets de dessin tels que des étiquettes, des zones de texte, des images, etc. dans un graphique. Aspose.Cells peut ajouter les contrôles à un graphique au moment de l'exécution.

{{% /alert %}}

##  **Ajout d'un contrôle d'étiquette au graphique**

Les étiquettes permettent de fournir des informations aux utilisateurs sur le contenu d'une feuille de calcul.
Aspose.Cells vous permet d'ajouter et de manipuler des étiquettes même dans des graphiques.

Le[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) la classe fournit une méthode nommée[**AddLabelInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabelinchart), utilisé pour ajouter un contrôle d'étiquette à un graphique. Vous trouverez ci-dessous une liste des paramètres utilisés pour la méthode :

- **haut**– le décalage vertical de l'étiquette par rapport au coin supérieur gauche en unités de 1/4000 de la zone du graphique.
- **gauche**– le décalage vertical de l'étiquette par rapport au coin supérieur gauche en unités de 1/4000 de la zone du graphique.
- **hauteur** – la hauteur de l'étiquette, en unités de 1/4000 de la zone cartographique.
- **largeur** – la largeur de l'étiquette, en unités de 1/4000 de la zone de la carte.

 La méthode renvoie[**Aspose.Cells.Drawing.Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label)objet. Le[**Étiquette**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) la classe représente une étiquette dans le graphique. Il compte quelques membres importants :

- [**Texte**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)(propriété) – spécifie la chaîne de légende d'une étiquette.
- [**Remplir**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fill) (propriété) – spécifie les attributs de couleur de remplissage.

L'exemple suivant montre comment ajouter une étiquette au graphique. L'exemple utilise un fichier de concepteur (**exp_piechart.xls**) qui contient un graphique. Nous utilisons ce fichier pour insérer une étiquette dans le graphique. Vous trouverez ci-dessous le code original pour ajouter une étiquette au graphique. La sortie suivante est générée lors de l'exécution du code.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingLabelControl-1.cs" >}}

##  **Ajout d'un contrôle TextBox au graphique**

Une façon de mettre en évidence des informations importantes dans un rapport consiste à utiliser une zone de texte. Par exemple, saisissez du texte pour mettre en surbrillance le nom de l'entreprise ou pour indiquer la région géographique avec les ventes les plus élevées. Le[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) la classe fournit une méthode nommée[**AddTextBoxInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addtextboxinchart), qui est utilisé pour ajouter un contrôle de zone de texte à un graphique. Voici la liste des paramètres utilisés pour la méthode :

- **haut** – le décalage vertical de la zone de texte par rapport au coin supérieur gauche en unités de 1/4000 de la zone du graphique.
- **gauche** – le décalage vertical de la zone de texte par rapport au coin supérieur gauche en unités de 1/4 000 de la zone du graphique.
- **hauteur** – la hauteur de la zone de texte, en unités de 1/4000 de la zone du graphique.
- **largeur** – la largeur de la zone de texte, en unités de 1/4000 de la zone du graphique.

 La méthode renvoie[**Aspose.Cells.Drawing.TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox) objet. Le[**Zone de texte**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox)la classe représente une zone de texte dans le graphique.

L'exemple suivant montre comment ajouter une zone de texte à un graphique. L'exemple utilise le fichier de concepteur précédent (**exp_piechart.xls**) qui contient un graphique. Nous utilisons ce fichier pour insérer une zone de texte dans le graphique afin d'afficher le titre du graphique. Vous trouverez ci-dessous le code original pour ajouter une zone de texte au graphique.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingTextBoxControl-1.cs" >}}

##  **Ajout d'une image au graphique**

Aspose.Cells vous permet d'insérer des images dans un graphique. Par exemple, ajoutez une image pour mettre en valeur ou donner plus de sens à un graphique ou à son contenu, ou insérez un fichier image de marque.

 Le[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) la classe fournit une méthode nommée[**Ajouter une image dans le graphique**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpictureinchart), qui est utilisé pour ajouter un objet image au graphique. Voici la liste des paramètres utilisés pour la méthode :

- **haut** – le décalage vertical de l'image par rapport au coin supérieur gauche en unités de 1/4000 de la zone de la carte.
- **gauche** – le décalage vertical de l'image par rapport au coin supérieur gauche en unités de 1/4000 de la zone de la carte.
- **flux** – un objet flux qui contient les données d'image.
- **échelle de largeur** – l'échelle de largeur de l'image, une valeur en pourcentage.
- **échelle de hauteur** – l'échelle de hauteur de l'image, une valeur en pourcentage.

 La méthode renvoie un[**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) objet. Le[**Image**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)la classe représente un objet image dans le graphique.

L'exemple suivant montre comment ajouter une image au graphique. L'exemple utilise le fichier de concepteur précédent (**exp_piechart.xls**) qui contient un graphique. Nous utilisons ce fichier pour insérer une image dans le graphique. Vous trouverez ci-dessous le code original pour ajouter une image au graphique.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingPictureToChart-1.cs" >}}

##  **Ajout d'une case à cocher dans le graphique**

 Aspose.Cells vous permet d'insérer des cases à cocher dans une feuille graphique en utilisant[**MsoDrawingType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msodrawingtype) énumération. L'exemple suivant montre l'ajout d'une case à cocher à une feuille graphique.

L'image suivante montre la feuille graphique avec la case à cocher dans le fichier de sortie.

![tâche : image_alt_text](controls-in-charts_1.jpg)

 Le[fichier de sortie](101089316.xlsx) généré par l'extrait de code suivant est joint pour votre référence.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-InsertCheckboxInChartSheet-1.cs" >}}

##  **Sujets avancés**
- [Ajouter un filigrane WordArt au graphique](/cells/fr/net/add-wordart-watermark-to-chart/)
