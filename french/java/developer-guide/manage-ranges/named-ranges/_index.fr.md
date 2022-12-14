---
title: Plages nommées
type: docs
weight: 40
url: /fr/java/named-ranges/
---
{{% alert color="primary" %}} 

Normalement, les étiquettes de colonne et de ligne sont utilisées pour faire référence à des cellules individuelles. Il est possible de créer des noms descriptifs pour représenter des cellules, des plages de cellules, des formules ou des valeurs constantes. Le mot**Nom** peut faire référence à une chaîne de caractères qui représente une cellule, une plage de cellules, une formule ou une valeur constante. Attribuer un nom à une plage signifie que cette plage de cellules peut être référencée par son nom. Utilisez des noms faciles à comprendre, tels que Produits, pour faire référence à des gammes difficiles à comprendre, telles que Ventes ! C20 : C30. Les étiquettes peuvent être utilisées dans des formules faisant référence à des données sur la même feuille de calcul ; si vous souhaitez représenter une plage sur une autre feuille de calcul, vous pouvez utiliser un nom. * Les plages nommées font partie des fonctionnalités les plus puissantes de Microsoft Excel, en particulier lorsqu'elles sont utilisées comme plage source pour les contrôles de liste, les tableaux croisés dynamiques, les graphiques, etc.

{{% /alert %}} 
## **Création d'une plage nommée**
### **Utilisation d'Excel Microsoft**
Les étapes suivantes décrivent comment nommer une cellule ou une plage de cellules à l'aide de Microsoft Excel. Cette méthode s'applique à Microsoft Office Excel 2003, Microsoft Excel 97, 2000 et 2002.

1. Sélectionnez la cellule, la plage de cellules que vous souhaitez nommer.
1. Cliquez sur la zone de nom à l'extrémité gauche de la barre de formule.
1. Tapez le nom des cellules.
1. Appuyez sur Entrée.

{{% alert color="primary" %}} 

Vous ne pouvez pas nommer une cellule pendant que vous modifiez le contenu de la cellule.

{{% /alert %}} 
### **En utilisant Aspose.Cells**
Ici, nous utilisons le Aspose.Cells API pour effectuer la tâche.

 Aspose.Cells fournit une classe,[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , qui représente un fichier Excel Microsoft. La[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classe contient un[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classer. La[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) la classe offre une[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)le recueil.

 Il est possible de créer une plage nommée en appelant le surchargé[createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\) ) méthode de la[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) le recueil. Une version typique du[createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\)) prend les paramètres suivants :

- Nom de la cellule supérieure gauche, nom de la cellule supérieure gauche de la plage.
- Nom de la cellule inférieure droite, nom de la cellule inférieure droite de la plage.

 Quand le[createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\) ) est appelée, elle renvoie la plage nommée nouvellement créée en tant qu'instance de[Intervalle](https://reference.aspose.com/cells/java/com.aspose.cells/range) classer.

L'exemple suivant montre comment créer une plage de cellules nommée qui s'étend sur B4:G14.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreateNamedRangeofCells-CreateNamedRangeofCells.java" >}}
#### **Accéder à toutes les plages nommées dans une feuille de calcul**
 Appeler le[getNamedRanges](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges\(\) ) méthode de la[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) pour obtenir toutes les plages nommées dans une feuille de calcul. La[getNamedRanges](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges\(\) ) renvoie un tableau de toutes les plages nommées dans le[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection).

L'exemple suivant montre comment accéder à toutes les plages nommées dans un classeur.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessAllNamedRanges-AccessAllNamedRanges.java" >}}
#### **Accéder à une plage nommée spécifique**
 Appeler le[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) de la collection[getRangeByName](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName\(java.lang.String\) ) pour obtenir une plage spécifiée par nom. Un typique[getRangeByName](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName\(java.lang.String\) ) prend le nom de la plage nommée et renvoie la plage nommée spécifiée en tant qu'instance de la[Intervalle](https://reference.aspose.com/cells/java/com.aspose.cells/range)classer.

L'exemple suivant montre comment accéder à une plage spécifiée par son nom.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessSpecificNamedRange-AccessSpecificNamedRange.java" >}}
#### **Identifier Cells dans une plage nommée**
En utilisant Aspose.Cells, vous pouvez insérer des données dans les cellules individuelles d'une plage. Supposons que vous ayez une plage de cellules nommée, c'est-à-dire A1:C4. Ainsi, la matrice ferait 4 * 3 = 12 cellules et les cellules de plage individuelles sont disposées séquentiellement. Aspose.Cells vous fournit des propriétés utiles de la classe [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) pour accéder aux cellules individuelles de la plage. Vous pouvez utiliser les méthodes suivantes pour identifier les cellules de la plage :

- [getFirstRow](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow) renvoie l'index de la première ligne de la plage nommée.
- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn)renvoie l'index de la première colonne de la plage nommée.

L'exemple suivant montre comment saisir des valeurs dans les cellules d'une plage spécifiée.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-IdentifyCellsinNamedRange-IdentifyCellsinNamedRange.java" >}}
#### **Données d'entrée dans le Cells dans la plage nommée**
En utilisant Aspose.Cells, vous pouvez insérer des données dans les cellules individuelles d'une plage. Supposons que vous ayez une plage de cellules nommée, c'est-à-dire H1: J4. Ainsi, la matrice ferait 4 * 3 = 12 cellules et les cellules de plage individuelles sont disposées séquentiellement. Aspose.Cells vous fournit des propriétés utiles de la classe [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) pour accéder aux cellules individuelles de la plage. Vous pouvez utiliser les propriétés suivantes pour identifier les cellules de la plage :

- [getFirstRow](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow)renvoie l'index de la première ligne de la plage nommée.
- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn)renvoie l'index de la première colonne de la plage nommée.

L'exemple suivant montre comment saisir des valeurs dans les cellules d'une plage spécifiée.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-InputDataInCellsInRange-InputDataInCellsInRange.java" >}}
#### **Plages de format... Définition de la couleur d'arrière-plan et des attributs de police dans une plage nommée**
 Pour appliquer le formatage, définissez un[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) objet pour spécifier les paramètres de style et les appliquer à l'objet[Intervalle](https://reference.aspose.com/cells/java/com.aspose.cells/range)objet.

L'exemple suivant montre comment définir une couleur de remplissage unie (couleur d'ombrage) avec des paramètres de police sur une plage.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges1-FormatRanges1.java" >}}
#### **Formater les plages... Ajouter des bordures à une plage nommée**
 Il est possible d'ajouter des bordures à une plage de cellules au lieu d'une seule cellule. La[Intervalle](https://reference.aspose.com/cells/java/com.aspose.cells/range) l'objet fournit un[setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders\(int,%20com.aspose.cells.Color\)qui prend les paramètres suivants pour ajouter une bordure à la plage de cellules :

-  borderStyle : le type de bordure, sélectionné dans le[CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)énumération.
-  borderColor : la couleur de ligne de la bordure, sélectionnée dans le[Couleur](https://reference.aspose.com/cells/java/com.aspose.cells/Color) énumération.

L'exemple suivant montre comment définir une bordure de contour sur une plage.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges2-FormatRanges2.java" >}}


 La sortie suivante serait générée après l'exécution du code ci-dessus :

![tâche : image_autre_texte](named-ranges_1.png)
#### **Appliquer un style aux cellules d'une plage**
Parfois, vous voulez créer appliquer un style aux cellules d'un[Intervalle](https://reference.aspose.com/cells/java/com.aspose.cells/range) . Pour cela, vous pouvez parcourir les cellules de la plage et utiliser le[Cell.setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) pour appliquer le style à la cellule.

L'exemple suivant montre comment appliquer des styles aux cellules d'une plage.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ConvertCellsAddresstoRangeorCellArea-ConvertCellsAddresstoRangeorCellArea.java" >}}
#### **Supprimer une plage nommée**
 Aspose.Cells fournit le[NameCollection.RemoveAt()](https://reference.aspose.com/cells/java/com.aspose.cells/namecollection#removeAt\(int\) ) méthode pour effacer le nom de la plage. Pour effacer le contenu de la plage, utilisez[Cells.ClearRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#clearRange\(com.aspose.cells.CellArea\)) méthode.
L'exemple suivant montre comment supprimer une plage nommée avec son contenu.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RemoveANamedRange-RemoveANamedRange.java" >}}


borderColors
