---
title: Formes dans les graphiques avec Golang via C++
linktitle: Formes dans les graphiques
description: Apprenez comment utiliser Aspose.Cells for C++ pour ajouter des contrôles et personnaliser les graphiques dans Microsoft Excel. Notre guide montrera comment manipuler les éléments du graphique, ajuster le formatage et améliorer l apparence et la convivialité générales de vos graphiques.
keywords: Aspose.Cells for C++, Contrôles de graphique, Personnalisation du graphique, Microsoft Excel, Éléments du graphique, Mise en forme.
type: docs
weight: 70
url: /fr/go-cpp/controls-in-charts/
---

{{% alert color="primary" %}}

Parfois, vous avez besoin d'insérer des objets de dessin comme des étiquettes, des boîtes de texte, des images, etc. dans un graphique. Aspose.Cells peut ajouter les contrôles à un graphique à l'exécution.

{{% /alert %}}

## **Ajout de contrôle d'étiquette au graphique**

Les étiquettes fournissent un moyen de donner des informations aux utilisateurs sur le contenu d'une feuille de calcul.
Aspose.Cells vous permet d'ajouter et de manipuler des étiquettes même dans des graphiques.

La classe [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/go-cpp/shapecollection/) fournit une méthode nommée [**AddLabelInChart**](https://reference.aspose.com/cells/go-cpp/shapecollection/addlabelinchart/), utilisée pour ajouter un contrôle d’étiquette à un graphique. Voici la liste des paramètres utilisés pour la méthode :

- **haut** – le décalage vertical de l'étiquette depuis le coin supérieur gauche en unités de 1/4000 de la zone du graphique.
- **gauche** – le décalage horizontal de l'étiquette depuis le coin supérieur gauche en unités de 1/4000 de la zone du graphique.
- **hauteur** – la hauteur de l'étiquette, en unités de 1/4000 de la zone du graphique.
- **largeur** – la largeur de l'étiquette, en unités de 1/4000 de la zone du graphique.

La méthode retourne un objet [**Aspose::Cells::Drawing::Label**](https://reference.aspose.com/cells/go-cpp/label/). La classe [**Label**](https://reference.aspose.com/cells/go-cpp/label/) représente une étiquette dans le graphique. Elle possède quelques membres importants :

- [**Text**](https://reference.aspose.com/cells/go-cpp/shape/gettext/) (propriété) – spécifie la chaîne de légende d'une étiquette.
- [**Fill**](https://reference.aspose.com/cells/go-cpp/shape/getfill/) (propriété) - spécifie les attributs de couleur de remplissage.

L'exemple suivant montre comment ajouter une étiquette au graphique. L'exemple utilise un fichier de concepteur (**exp_piechart.xls**) qui contient un graphique. Nous utilisons ce fichier pour insérer une étiquette dans le graphique. Ci-dessous se trouve le code d'origine pour ajouter une étiquette au graphique. La sortie suivante est générée lors de l'exécution du code.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShapesInCharts.go" >}}
## **Ajout d'un contrôle TextBox au graphique**

Une façon de mettre en valeur des informations importantes dans un rapport est d'utiliser une zone de texte. Par exemple, entrez du texte pour mettre en valeur le nom de l'entreprise ou pour indiquer la région géographique avec les meilleures ventes. La classe [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/go-cpp/shapecollection/) fournit une méthode nommée [**AddTextBoxInChart**](https://reference.aspose.com/cells/go-cpp/shapecollection/addtextboxinchart/), qui est utilisée pour ajouter un contrôle de zone de texte à un graphique. Voici la liste des paramètres utilisés pour la méthode :

- **top** - le décalage vertical de la zone de texte depuis le coin supérieur gauche en unités de 1/4000 de la zone du graphique.
- **left** - le décalage vertical de la zone de texte depuis le coin supérieur gauche en unités de 1/4000 de la zone du graphique.
- **height** - la hauteur de la zone de texte, en unités de 1/4000 de la zone du graphique.
- **width** - la largeur de la zone de texte, en unités de 1/4000 de la zone du graphique.

La méthode retourne un objet [**Aspose::Cells::Drawing::TextBox**](https://reference.aspose.com/cells/go-cpp/textbox/). La classe [**TextBox**](https://reference.aspose.com/cells/go-cpp/textbox/) représente une zone de texte dans le graphique.

L'exemple suivant montre comment ajouter une zone de texte à un graphique. L'exemple utilise le fichier de concepteur précédent (**exp_piechart.xls**) qui contient un graphique. Nous utilisons ce fichier pour insérer une zone de texte dans le graphique pour afficher le titre du graphique. Ci-dessous se trouve le code d'origine pour ajouter une zone de texte au graphique.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShapesInCharts-1.go" >}}
## **Ajout d'une image au graphique**

Aspose.Cells vous permet d'insérer des images dans un graphique. Par exemple, ajoutez une image pour mettre en avant ou donner plus de sens à un graphique ou à son contenu, ou insérez un fichier image de marque.

La classe [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/go-cpp/shapecollection/) fournit une méthode nommée [**AddPictureInChart**](https://reference.aspose.com/cells/go-cpp/shapecollection/addpictureinchart/), utilisée pour ajouter un objet image au graphique. Voici la liste des paramètres utilisés pour la méthode :

- **top** - le décalage vertical de l'image depuis le coin supérieur gauche en unités de 1/4000 de la zone du graphique.
- **left** - le décalage vertical de l'image depuis le coin supérieur gauche en unités de 1/4000 de la zone du graphique.
- **stream** - un objet flux qui contient les données de l'image.
- **widthScale** - l'échelle de la largeur de l'image, une valeur en pourcentage.
- **heightScale** - l'échelle de la hauteur de l'image, une valeur en pourcentage.

La méthode retourne un objet [**Aspose::Cells::Drawing::Picture**](https://reference.aspose.com/cells/go-cpp/picture/). La classe [**Picture**](https://reference.aspose.com/cells/go-cpp/picture/) représente un objet image dans le graphique.

L'exemple suivant montre comment ajouter une image au graphique. L'exemple utilise le fichier de conception précédent (**exp_piechart.xls**) qui contient un graphique. Nous utilisons ce fichier pour insérer une image dans le graphique. Ci-dessous se trouve le code d'origine pour ajouter une image au graphique.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShapesInCharts-2.go" >}}
## **Ajout d'une case à cocher dans le graphique**

Aspose.Cells vous permet d'insérer des cases à cocher dans une feuille de graphique en utilisant l'énumération [**MsoDrawingType**](https://reference.aspose.com/cells/go-cpp/msodrawingtype/). L'exemple suivant montre comment ajouter une case à cocher à une feuille de graphique.

L'image suivante montre la feuille de graphique avec la case à cocher dans le fichier de sortie.

![todo:image_alt_text](controls-in-charts_1.jpg)

Le [fichier de sortie](101089316.xlsx) généré par le snippet de code suivant est joint à titre de référence.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShapesInCharts-3.go" >}}
## **Sujets avancés**
- [Ajouter un filigrane WordArt au graphique](/cells/fr/cpp/add-wordart-watermark-to-chart/)
