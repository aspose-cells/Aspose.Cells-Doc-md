---
title: Paramètres d'alignement
type: docs
weight: 20
url: /fr/net/cells-alignment-settings/
---
## **Configuration des paramètres d'alignement**

### **Paramètres d'alignement dans Microsoft Excel**

Quiconque a utilisé Microsoft Excel pour formater des cellules connaîtra les paramètres d'alignement dans Microsoft Excel.

Comme vous pouvez le voir sur la figure ci-dessus, il existe différents types d'options d'alignement :

- Alignement du texte (horizontal et vertical)
- Échancrure.
- Orientation.
- Contrôle du texte.
- Sens du texte.

Tous ces paramètres d'alignement sont entièrement pris en charge par Aspose.Cells et sont discutés plus en détail ci-dessous.

### **Paramètres d'alignement dans Aspose.Cells**

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , qui représente un fichier Excel. Le[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe contient un[**Feuilles de travail**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe offre une[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) le recueil. Chaque élément de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection représente un objet de la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)classe.

 Aspose.Cells fournit[**ObtenirStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) et[**DéfinirStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) méthodes pour la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) class qui sont utilisées pour obtenir et définir la mise en forme d'une cellule. Le[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)fournit des propriétés utiles pour configurer les paramètres d'alignement.

 Sélectionnez n'importe quel type d'alignement de texte à l'aide de la[**Type d'alignement de texte**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype) énumération. Les types d'alignement de texte prédéfinis dans le[**Type d'alignement de texte**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype)l'énumération sont :

|**Types d'alignement de texte**|**Description**|
|:- |:- |
|Fond|Représente l'alignement du texte inférieur|
|Centre|Représente l'alignement du texte au centre|
|CenterAcross|Représente le centre sur l'alignement du texte|
|Distribué|Représente l'alignement de texte distribué|
|Remplir|Représente l'alignement du texte de remplissage|
|Général|Représente l'alignement général du texte|
|Justifier|Représente l'alignement du texte justifié|
|Gauche|Représente l'alignement du texte à gauche|
|Droit|Représente l'alignement du texte à droite|
|Haut|Représente l'alignement supérieur du texte|
|JustifiéBas|Aligne le texte avec une longueur kashida ajustée pour le texte arabe.|
|ThaïDistribué|Distribue le texte thaï en particulier, car chaque caractère est traité comme un mot.|

{{% alert color="primary" %}}

 Vous pouvez également appliquer le paramètre de justification distribuée à l'aide de la[**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/isjustifydistributed) la propriété.

{{% /alert %}}

#### **Alignement horizontal**

 Utilisez le[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objets[**AlignementHorizontal**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/horizontalalignment)propriété pour aligner le texte horizontalement.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentHorizontal-1.cs" >}}

#### **Alignement vertical**

 Semblable à l'alignement horizontal, utilisez le[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objets[**Alignement vertical**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/verticalalignment)propriété pour aligner le texte verticalement.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentVertical-1.cs" >}}

#### **Échancrure**

 Il est possible de définir le niveau d'indentation du texte dans une cellule avec la[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objets[**Niveau d'indentation**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/indentlevel)la propriété.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Indentation-1.cs" >}}

#### **Orientation**

 Définissez l'orientation (rotation) du texte dans une cellule avec la[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objets[**Angle de rotation**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/rotationangle)la propriété.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Orientation-1.cs" >}}

#### **Contrôle du texte**

La section suivante explique comment contrôler le texte en définissant l'habillage du texte, le rétrécissement et d'autres options de formatage.

##### **Habillage du texte**

 L'habillage du texte dans une cellule facilite la lecture : la hauteur de la cellule s'ajuste pour s'adapter à tout le texte, au lieu de le couper ou de déborder dans les cellules adjacentes. Activez ou désactivez l'habillage du texte avec le[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objets[**EstEnveloppéTexte**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)la propriété.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

##### **Rétrécir pour s'adapter**

 Une option d'habillage du texte dans un champ consiste à réduire la taille du texte pour l'adapter aux dimensions d'une cellule. Cela se fait en réglant le[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objets[**EstEnveloppéTexte**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped) propriété à**vrai**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-ShrinkingToFit-1.cs" >}}

##### **Fusion Cells**

 Comme Microsoft Excel, Aspose.Cells prend en charge la fusion de plusieurs cellules en une seule. Aspose.Cells propose deux approches pour cette tâche. Une façon consiste à appeler le[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) de la collection[**Fusionner**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) méthode. Le[**Fusionner**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index)prend les paramètres suivants pour fusionner les cellules :

- Première ligne : la première ligne à partir de laquelle commencer la fusion.
- Première colonne : la première colonne à partir de laquelle commencer la fusion.
- Nombre de lignes : le nombre de lignes à fusionner.
- Nombre de colonnes : le nombre de colonnes à fusionner.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}

 L'autre façon est d'appeler d'abord le[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) de la collection[**CréerPlage**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) méthode pour créer une plage de cellules à fusionner. Le[**CréerPlage**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) prend le même jeu de paramètres que celui de la[**Fusionner**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) méthode décrite ci-dessus et renvoie un[**Intervalle**](https://reference.aspose.com/cells/net/aspose.cells/range) objet. Le[**Intervalle**](https://reference.aspose.com/cells/net/aspose.cells/range) l'objet fournit également un[**Fusionner**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge) méthode qui fusionne la plage spécifiée dans le[**Intervalle**](https://reference.aspose.com/cells/net/aspose.cells/range)objet.

##### **Sens du texte**

Il est possible de définir l'ordre de lecture du texte dans les cellules. L'ordre de lecture est l'ordre visuel dans lequel les caractères, les mots, etc. sont affichés. Par exemple, l'anglais est une langue de gauche à droite tandis que l'arabe est une langue de droite à gauche.

 L'ordre de lecture est défini avec le[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objets[**Direction du texte**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/textdirection) la propriété. Aspose.Cells fournit des types de direction de texte prédéfinis dans le[**TextDirectionType**](https://reference.aspose.com/cells/net/aspose.cells/textdirectiontype)énumération.

|**Types d'orientation du texte**|**Description**|
|:- |:- |
|Contexte|L'ordre de lecture cohérent avec la langue du premier caractère saisi|
|De gauche à droite|Ordre de lecture de gauche à droite|
|De droite à gauche|Ordre de lecture de droite à gauche|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChangeTextDirection-1.cs" >}}

## **Sujets avancés**
- [Modifier l'alignement Cells et conserver la mise en forme existante](/cells/fr/net/change-cells-alignment-and-keep-existing-formatting/)
- [Sauts de ligne et retour à la ligne](/cells/fr/net/line-breaks-and-text-wrapping/)

