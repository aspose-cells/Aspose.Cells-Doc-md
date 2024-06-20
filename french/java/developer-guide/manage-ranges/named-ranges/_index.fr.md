---
title: Plages nommées
type: docs
weight: 40
url: /fr/java/named-ranges/
---

{{% alert color="primary" %}} 

Normalement, les étiquettes de colonnes et de lignes sont utilisées pour faire référence à des cellules individuelles. Il est possible de créer des noms descriptifs pour représenter des cellules, des plages de cellules, des formules ou des valeurs constantes. Le mot **nom** peut faire référence à une chaîne de caractères qui représente une cellule, une plage de cellules, une formule ou une valeur constante. Affecter un nom à une plage signifie que cette plage de cellules peut être référencée par son nom. Utilisez des noms faciles à comprendre, tels que Produits, pour faire référence à des plages difficiles à comprendre, telles que Ventes!C20:C30. Les étiquettes peuvent être utilisées dans des formules qui font référence à des données sur la même feuille de calcul ; si vous souhaitez représenter une plage sur une autre feuille de calcul, vous pouvez utiliser un nom. *Les plages nommées font partie des fonctionnalités les plus puissantes de Microsoft Excel, en particulier lorsqu'elles sont utilisées comme plage source pour les contrôles de liste, les tableaux croisés dynamiques, les graphiques, etc.*

{{% /alert %}} 
## **Création d'une plage nommée**
### **Utilisation de Microsoft Excel**
Les étapes suivantes décrivent comment nommer une cellule ou une plage de cellules à l'aide de Microsoft Excel. Cette méthode s'applique à Microsoft Office Excel 2003, Microsoft Excel 97, 2000 et 2002.

1. Sélectionnez la cellule ou la plage de cellules que vous souhaitez nommer.
1. Cliquez sur la zone de nom à l'extrémité gauche de la barre de formule.
1. Saisissez le nom des cellules.
1. Appuyez sur ENTRÉE.

{{% alert color="primary" %}} 

Vous ne pouvez pas nommer une cellule pendant que vous modifiez le contenu de la cellule.

{{% /alert %}} 
### **Utilisation d'Aspose.Cells**
Ici, nous utilisons l'API Aspose.Cells pour effectuer la tâche.

Aspose.Cells fournit une classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contient une collection [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) fournit une collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells).

Il est possible de créer une plage nommée en appelant la méthode surchargée [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\)) de la collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Une version typique de la méthode [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\)) prend les paramètres suivants :

- Nom de la cellule supérieure gauche, le nom de la cellule supérieure gauche dans la plage.
- Nom de la cellule inférieure droite, le nom de la cellule inférieure droite de la plage.

Lorsque la méthode [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\)) est appelée, elle renvoie la plage nommée nouvellement créée en tant qu'instance de la classe [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range).

L'exemple suivant montre comment créer une plage nommée de cellules s'étendant sur B4:G14.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreateNamedRangeofCells-CreateNamedRangeofCells.java" >}}
#### **Accès à toutes les plages nommées dans une feuille de calcul**
Appelez la méthode [getNamedRanges](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges\(\)) de la collection [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) pour obtenir toutes les plages nommées dans une feuille de calcul. La méthode [getNamedRanges](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges\(\)) renvoie un tableau de toutes les plages nommées dans la collection [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection).

L'exemple suivant montre comment accéder à toutes les plages nommées dans un classeur.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessAllNamedRanges-AccessAllNamedRanges.java" >}}
#### **Accéder à une plage nommée spécifique**
Appelez la méthode [getRangeByName](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName\(java.lang.String\)) de la collection [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) pour obtenir une plage spécifiée par son nom. Une méthode typique [getRangeByName](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName\(java.lang.String\)) prend le nom de la plage nommée et renvoie la plage nommée spécifiée en tant qu'instance de la classe [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range).

L'exemple suivant montre comment accéder à une plage spécifiée par son nom.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessSpecificNamedRange-AccessSpecificNamedRange.java" >}}
#### **Identifier les cellules dans une plage nommée**
À l'aide d'Aspose.Cells, vous pouvez insérer des données dans les cellules individuelles d'une plage. Supposons que vous ayez une plage nommée de cellules, c'est-à-dire A1:C4. Ainsi, la matrice constituera 4 * 3 = 12 cellules et les cellules de plage individuelles sont disposées de manière séquentielle. Aspose.Cells vous propose certaines propriétés utiles de la classe [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) pour accéder aux cellules individuelles dans la plage. Vous pouvez utiliser les méthodes suivantes pour identifier les cellules dans la plage:

- [getFirstRow](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow) renvoie l'index de la première ligne dans la plage nommée.
- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn) renvoie l'index de la première colonne dans la plage nommée.

L'exemple suivant montre comment saisir certaines valeurs dans les cellules d'une plage spécifiée.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-IdentifyCellsinNamedRange-IdentifyCellsinNamedRange.java" >}}
#### **Saisir des données dans les cellules de la plage nommée**
À l'aide d'Aspose.Cells, vous pouvez insérer des données dans les cellules individuelles d'une plage. Supposons que vous ayez une plage nommée de cellules, à savoir H1:J4. Ainsi, la matrice constituera 4 * 3 = 12 cellules et les cellules de plage individuelles sont disposées de manière séquentielle. Aspose.Cells vous propose certaines propriétés utiles de la classe [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) pour accéder aux cellules individuelles dans la plage. Vous pouvez utiliser les propriétés suivantes pour identifier les cellules dans la plage:

- [getFirstRow](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow) renvoie l'index de la première ligne dans la plage nommée.
- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn) renvoie l'index de la première colonne dans la plage nommée.

L'exemple suivant montre comment saisir certaines valeurs dans les cellules d'une plage spécifiée.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-InputDataInCellsInRange-InputDataInCellsInRange.java" >}}
#### **Format des plages... Définition de la couleur de fond et des attributs de police pour une plage nommée**
Pour appliquer une mise en forme, définissez un objet [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) pour spécifier les paramètres de style et appliquez-le à l'objet [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range).

L'exemple suivant montre comment définir la couleur de remplissage solide (couleur ombrage) avec les paramètres de police pour une plage.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges1-FormatRanges1.java" >}}
#### **Format des plages... Ajout de bordures à une plage nommée**
Il est possible d'ajouter des bordures à une plage de cellules au lieu d'une seule cellule. L'objet [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) fournit une méthode [setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders\(int,%20com.aspose.cells.Color\)) qui prend les paramètres suivants pour ajouter une bordure à la plage de cellules:

- borderStyle: le type de bordure, sélectionné dans l'énumération [CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType).
- borderColor: la couleur de ligne de la bordure, sélectionnée dans l'énumération [Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color).

L'exemple suivant montre comment définir une bordure de contour à une plage.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges2-FormatRanges2.java" >}}


Le résultat suivant serait généré après l'exécution du code ci-dessus : 

![todo:image_alt_text](named-ranges_1.png)
#### **Appliquer un style aux cellules dans une plage**
Parfois, vous voulez appliquer un style aux cellules dans une [Plage](https://reference.aspose.com/cells/java/com.aspose.cells/range). Pour cela, vous pouvez parcourir les cellules de la plage et utiliser la méthode [Cell.setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) pour appliquer le style à la cellule.

L'exemple suivant montre comment appliquer des styles aux cellules dans une plage.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ConvertCellsAddresstoRangeorCellArea-ConvertCellsAddresstoRangeorCellArea.java" >}}
#### **Supprimer une Plage Nommée**
Aspose.Cells fournit la méthode [NameCollection.RemoveAt()](https://reference.aspose.com/cells/java/com.aspose.cells/namecollection#removeAt\(int\)) pour effacer le nom de la plage. Pour effacer le contenu de la plage, utilisez la méthode [Cells.ClearRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#clearRange\(com.aspose.cells.CellArea\)) .
L'exemple suivant montre comment supprimer une plage nommée avec son contenu.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RemoveANamedRange-RemoveANamedRange.java" >}}


borderColors 
