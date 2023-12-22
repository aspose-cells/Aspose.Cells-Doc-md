---
title: Paramètres de bordure
description: Comment utiliser la bibliothèque Aspose.Cells dans C# pour définir le style de bordure et la couleur des cellules. En ajustant la largeur, le style et la couleur de la bordure, vous avez davantage de contrôle sur l’apparence et l’apparence des cellules.
keywords: Aspose.Cells, Cell Border Settings, C#, Border Width, Border Style, Border Color
type: docs
weight: 40
url: /fr/net/cells-border-settings/
---
##  **Ajout de bordures au Cells**

Microsoft Excel permet aux utilisateurs de formater les cellules en ajoutant des bordures. Le type de bordure dépend de l'endroit où elle est ajoutée. Par exemple, une bordure supérieure est une bordure ajoutée à la position supérieure d'une cellule. Les utilisateurs peuvent également modifier le style et la couleur des lignes des bordures.

Avec Aspose.Cells, les développeurs peuvent ajouter des bordures et personnaliser leur apparence de la même manière flexible que dans Microsoft Excel.

###  **Ajout de bordures au Cells**

 Aspose.Cells propose un cours,[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Excel Microsoft. Le[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contient un[**Des feuilles de calcul**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection qui permet d’accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fournit le[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection. Chaque élément du[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) la collection représente un objet de la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)classe.

 Aspose.Cells fournit le[**ObtenirStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index)méthode dans le[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)classe. Le[**Définir le style**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index)La méthode est utilisée pour définir le style de formatage d’une cellule. Le[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)La classe fournit des propriétés pour ajouter des bordures aux cellules.

####  **Ajout de bordures à un Cell**

Les développeurs peuvent ajouter des bordures à une cellule en utilisant l'outil[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objets[**Les frontières**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) collection. Le type de bordure est transmis sous forme d'index au[**Les frontières**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) collection. Tous les types de bordures sont prédéfinis dans le[**Type de bordure**](https://reference.aspose.com/cells/net/aspose.cells/bordertype) énumération.

**Dénombrement des frontières**

|**Types de bordures**|**Description**|
| :- | :- |
|Bordure inférieure|Une ligne de bordure inférieure|
|Diagonale vers le bas|Une ligne diagonale du haut à gauche vers le bas à droite|
|Diagonale vers le haut|Une ligne diagonale du bas à gauche vers le haut à droite|
|Bordure Gauche|Une ligne de bordure gauche|
|Bordure droite|Une frontière droite|
|Bordure supérieure|Une ligne de bordure supérieure|

Le[**Les frontières**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders)la collection stocke toutes les frontières. Chaque frontière dans le[**Les frontières**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) la collection est représentée par un[**Frontière**](https://reference.aspose.com/cells/net/aspose.cells/border) objet qui fournit deux propriétés,[**Couleur**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/color) et[**Style de ligne**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle)pour définir respectivement la couleur et le style de la ligne d'une bordure.

Pour définir la couleur de ligne d'une bordure, sélectionnez une couleur à l'aide de l'énumération Color (qui fait partie du Framework .NET) et affectez-la à la propriété Color de l'objet Border.

 Le style de ligne de la bordure est défini en sélectionnant un style de ligne dans la liste[**Type de bordure de cellule**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)énumération.

**Énumération CellBorderType**

|**Styles de lignes**|**Description**|
| :- | :- |
|DashDot|Fine ligne en pointillés|
|DashDotDot|Fine ligne tiret-pointillé|
|En pointillés|Ligne pointillée|
|Pointé|Ligne pointillée|
|Double|Double ligne|
|Cheveux|Racine des cheveux|
|Point de tiret moyen|Ligne pointillée moyenne|
|MediumDashDotDot|Ligne tiret-pointillé moyenne|
|Pointillé moyen|Ligne pointillée moyenne|
|Aucun|Pas de ligne|
|Moyen|Ligne moyenne|
|Point de tiret incliné|Ligne pointillée moyenne inclinée|
|Épais|Ligne épaisse|
|Mince|Ligne fine|
Sélectionnez l'un des styles de ligne, puis attribuez-le au[**Frontière**](https://reference.aspose.com/cells/net/aspose.cells/border) objets[**Style de ligne**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle) propriété.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBordersToCells-1.cs" >}}

{{% alert color="primary" %}}

Vous devez définir à la fois le style de ligne et la couleur. Les deux lignes de bordure diagonales doivent avoir le même style et la même couleur.

{{% /alert %}}

####  **Ajout de bordures à une plage de Cells**

 Il est également possible d'ajouter des bordures à une plage de cellules plutôt qu'à une seule cellule. Pour ce faire, créez d’abord une plage de cellules en appelant le[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) la collection[**Créer une plage**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) méthode. Il prend les paramètres suivants :

- First Row, la première rangée de la gamme.
- Première colonne, représente la première colonne de la plage.
- Nombre de lignes, nombre de lignes dans la plage.
- Nombre de colonnes, le nombre de colonnes dans la plage.

 Le[**Créer une plage**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) la méthode renvoie un[**Gamme**](https://reference.aspose.com/cells/net/aspose.cells/range) objet, qui contient la plage de cellules spécifiée. Le[**Gamme**](https://reference.aspose.com/cells/net/aspose.cells/range) l'objet fournit un[**Définir la bordure du contour**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder) méthode qui prend les paramètres suivants pour ajouter une bordure à la plage de cellules :

-  *Border Type**, le type de bordure, sélectionné dans le[**Type de bordure**](https://reference.aspose.com/cells/net/aspose.cells/bordertype)énumération.
-  *Style de ligne**, le style de ligne de bordure, sélectionné parmi[**Type de bordure de cellule**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)énumération.
- *Couleur**, la couleur de la ligne, sélectionnée dans l'énumération Couleur.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBorderstoRange-1.cs" >}}
