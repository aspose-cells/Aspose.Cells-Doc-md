---
title: Formes dans les graphiques
description: Apprenez à utiliser Aspose.Cells for .NET pour ajouter des contrôles et personnaliser les graphiques dans Microsoft Excel. Notre guide démontrera comment manipuler les éléments de graphique, ajuster la mise en forme et améliorer l apparence générale et l utilisabilité de vos graphiques.
keywords: Aspose.Cells for .NET, Contrôles de graphique, Personnalisation de graphique, Microsoft Excel, Éléments de graphique, Mise en forme.
type: docs
weight: 70
url: /fr/net/controls-in-charts/
---

{{% alert color="primary" %}}

Parfois, vous avez besoin d'insérer des objets de dessin comme des étiquettes, des boîtes de texte, des images, etc. dans un graphique. Aspose.Cells peut ajouter les contrôles à un graphique à l'exécution.

{{% /alert %}}

## **Ajout de contrôle d'étiquette au graphique**

Les étiquettes fournissent un moyen de donner des informations aux utilisateurs sur le contenu d'une feuille de calcul.
Aspose.Cells vous permet d'ajouter et de manipuler des étiquettes même dans des graphiques.

La classe [**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) fournit une méthode nommée [**AddLabelInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabelinchart), utilisée pour ajouter un contrôle d'étiquette à un graphique. Voici une liste des paramètres utilisés pour la méthode :

- **haut** – le décalage vertical de l'étiquette depuis le coin supérieur gauche en unités de 1/4000 de la zone du graphique.
- **gauche** – le décalage horizontal de l'étiquette depuis le coin supérieur gauche en unités de 1/4000 de la zone du graphique.
- **hauteur** – la hauteur de l'étiquette, en unités de 1/4000 de la zone du graphique.
- **largeur** – la largeur de l'étiquette, en unités de 1/4000 de la zone du graphique.

La méthode retourne un objet [**Aspose.Cells.Drawing.Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label). La classe [**Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) représente une étiquette dans le graphique. Elle a quelques membres importants :

- [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) (propriété) - spécifie la chaîne de légende d'une étiquette.
- [**Fill**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fill) (propriété) - spécifie les attributs de couleur de remplissage.

L'exemple suivant montre comment ajouter une étiquette au graphique. L'exemple utilise un fichier de concepteur (**exp_piechart.xls**) qui contient un graphique. Nous utilisons ce fichier pour insérer une étiquette dans le graphique. Ci-dessous se trouve le code d'origine pour ajouter une étiquette au graphique. La sortie suivante est générée lors de l'exécution du code.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingLabelControl-1.cs" >}}

**Remarque :** Ce type de contrôle d’étiquette n’est pris en charge que dans les fichiers XLS. Si vous souhaitez un effet similaire dans un fichier XLSX, veuillez utiliser l’une des alternatives suivantes :

1. Utilisez plutôt le Contrôle TextBox, il existe une alternative similaire au contrôle d’étiquette dans les fichiers XLSX.
- [**Example**](https://docs.aspose.com/cells/net/controls-in-charts/#adding-textbox-control-to-the-chart) pour TextBox, les fichiers XLSX peuvent le prendre en charge.

2. Ajoutez une Feuille dont le type est "SheetType.Chart", puis ajoutez un Graphique et un Contrôle sur cette feuille.
- [**Example**](https://docs.aspose.com/cells/net/controls-in-charts/#adding-checkbox-in-the-chart) pour l'ajout de SheetType.Chart.

## **Ajout d'un contrôle TextBox au graphique**

Une manière de mettre en évidence des informations importantes dans un rapport est d'utiliser une zone de texte. Par exemple, saisissez du texte pour mettre en valeur le nom de l'entreprise ou pour indiquer la région géographique avec le plus de ventes. La classe [**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) fournit une méthode appelée [**AddTextBoxInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addtextboxinchart), qui est utilisée pour ajouter un contrôle de zone de texte à un graphique. Voici la liste des paramètres utilisés pour la méthode :

- **top** - le décalage vertical de la zone de texte depuis le coin supérieur gauche en unités de 1/4000 de la zone du graphique.
- **left** - le décalage vertical de la zone de texte depuis le coin supérieur gauche en unités de 1/4000 de la zone du graphique.
- **height** - la hauteur de la zone de texte, en unités de 1/4000 de la zone du graphique.
- **width** - la largeur de la zone de texte, en unités de 1/4000 de la zone du graphique.

La méthode renvoie un objet [**Aspose.Cells.Drawing.TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox). La classe [**TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox) représente une zone de texte dans le graphique.

L'exemple suivant montre comment ajouter une zone de texte à un graphique. L'exemple utilise le fichier de concepteur précédent (**exp_piechart.xls**) qui contient un graphique. Nous utilisons ce fichier pour insérer une zone de texte dans le graphique pour afficher le titre du graphique. Ci-dessous se trouve le code d'origine pour ajouter une zone de texte au graphique.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingTextBoxControl-1.cs" >}}

## **Ajout d'une image au graphique**

Aspose.Cells vous permet d'insérer des images dans un graphique. Par exemple, ajoutez une image pour mettre en avant ou donner plus de sens à un graphique ou à son contenu, ou insérez un fichier image de marque.

La classe [**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) fournit une méthode nommée [**AddPictureInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpictureinchart), qui est utilisée pour ajouter un objet image au graphique. Voici la liste des paramètres utilisés pour la méthode :

- **top** - le décalage vertical de l'image depuis le coin supérieur gauche en unités de 1/4000 de la zone du graphique.
- **left** - le décalage vertical de l'image depuis le coin supérieur gauche en unités de 1/4000 de la zone du graphique.
- **stream** - un objet flux qui contient les données de l'image.
- **widthScale** - l'échelle de la largeur de l'image, une valeur en pourcentage.
- **heightScale** - l'échelle de la hauteur de l'image, une valeur en pourcentage.

La méthode renvoie un objet [**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture). La classe [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) représente un objet image dans le graphique.

L'exemple suivant montre comment ajouter une image au graphique. L'exemple utilise le fichier de conception précédent (**exp_piechart.xls**) qui contient un graphique. Nous utilisons ce fichier pour insérer une image dans le graphique. Ci-dessous se trouve le code d'origine pour ajouter une image au graphique.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingPictureToChart-1.cs" >}}

## **Ajout d'une case à cocher dans le graphique**

Aspose.Cells vous permet d'insérer des cases à cocher dans une feuille de graphique en utilisant l'énumération [**MsoDrawingType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msodrawingtype). L'exemple suivant montre comment ajouter une case à cocher à une feuille de graphique.

L'image suivante montre la feuille de graphique avec la case à cocher dans le fichier de sortie.

![todo:image_alt_text](controls-in-charts_1.jpg)

Le [fichier de sortie](101089316.xlsx) généré par le snippet de code suivant est joint à titre de référence.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-InsertCheckboxInChartSheet-1.cs" >}}

## **Sujets avancés**
- [Ajouter un filigrane WordArt au graphique](/cells/fr/net/add-wordart-watermark-to-chart/)
{{< app/cells/assistant language="csharp" >}}
