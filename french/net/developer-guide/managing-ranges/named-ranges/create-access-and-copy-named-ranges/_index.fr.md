---
title: Créer un accès et copier les plages nommées
type: docs
weight: 200
url: /fr/net/create-access-and-copy-named-ranges/
---

## **Introduction**

Normalement, les étiquettes de colonnes et de lignes sont utilisées pour faire référence à des cellules individuelles. Il est possible de créer des noms descriptifs pour représenter des cellules, des plages de cellules, des formules ou des valeurs constantes. Le mot **nom** peut faire référence à une chaîne de caractères représentant une cellule, une plage de cellules, une formule ou une valeur constante. Assigner un nom à une plage signifie que cette plage de cellules peut être référencée par son nom. Utilisez des noms faciles à comprendre, comme Produits, pour faire référence à des plages difficiles à comprendre, comme Ventes!C20:C30. Les étiquettes peuvent être utilisées dans les formules qui font référence aux données sur la même feuille de calcul; si vous souhaitez représenter une plage sur une autre feuille de calcul, vous pouvez utiliser un nom. *Les plages nommées figurent parmi les fonctionnalités les plus puissantes de Microsoft Excel, notamment lorsqu'elles sont utilisées comme plage source pour les contrôles de liste, les tableaux croisés dynamiques, les graphiques, etc.*

## **Travailler avec les plages nommées en utilisant Microsoft Excel**

### **Créer des plages nommées**

Les étapes suivantes décrivent comment attribuer un nom à une cellule ou à une plage de cellules à l'aide d'**MS Excel**. Cette méthode s'applique à **Microsoft Office Excel 2003**, **Microsoft Excel 97**, **2000** et **2002**.

1. Sélectionnez la cellule ou la plage de cellules que vous souhaitez nommer.
1. Cliquez sur la **Zone de nom** située à l'extrémité gauche de la barre de formule.
1. Saisissez le nom des cellules.
1. Appuyez sur ENTRÉE.

{{% alert color="primary" %}}

Vous ne pouvez pas nommer une cellule pendant que vous modifiez le contenu de la cellule.

{{% /alert %}}

## **Travailler avec la plage nommée en utilisant Aspose.Cells**

Ici, nous utilisons l'API Aspose.Cells pour effectuer la tâche.
Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fournit une collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells).

### **Créer une plage nommée**

Il est possible de créer une plage nommée en appelant la méthode surchargée [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) de la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Une version typique de la méthode [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/3) prend les paramètres suivants :

- Nom de la cellule en haut à gauche, nom de la cellule en haut à gauche dans la plage.
- Nom de la cellule inférieure droite, le nom de la cellule inférieure droite de la plage.

Lorsque la méthode [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/3) est appelée, elle renvoie la plage nouvellement créée en tant qu'instance de la classe [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range). Utilisez cet objet [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) pour configurer la plage nommée. Par exemple, définissez le nom de la plage en utilisant la propriété [**Name**](https://reference.aspose.com/cells/net/aspose.cells/range/properties/name). L'exemple suivant montre comment créer une plage nommée de cellules qui s'étend de B4 à G14.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CreateNamedRangeofCells-1.cs" >}}

### **Saisir des données dans les cellules de la plage nommée**

Vous pouvez insérer des données dans les cellules individuelles d'une plage en suivant le modèle

- **C#**: Range[row,column]
- **VB**: Range(row,column)

Disons que vous avez une plage nommée de cellules qui s'étend de A1 à C4. La matrice comprend 4 * 3 = 12 cellules. Les cellules individuelles de la plage sont disposées séquentiellement : Plage[0,0], Plage[0,1], Plage[0,2], Plage[1,0], Plage[1,1], Plage[1,2], Plage[2,0], Plage[2,1], Plage[2,2], Plage[3,0], Plage[3,1], Plage[3,2].

Utilisez les propriétés suivantes pour identifier les cellules dans la plage :

- La propriété FirstRow renvoie l'index de la première ligne de la plage nommée.
- La propriété FirstColumn renvoie l'index de la première colonne de la plage nommée.
- La propriété RowCount renvoie le nombre total de lignes dans la plage nommée.
- La propriété ColumnCount renvoie le nombre total de colonnes dans la plage nommée.

L'exemple suivant montre comment saisir certaines valeurs dans les cellules d'une plage spécifiée.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-InputDataInCellsInRange-1.cs" >}}

### **Identifier les cellules dans la plage nommée**

Vous pouvez insérer des données dans les cellules individuelles d'une plage en suivant le schéma :

- **C#**: Range[row,column]
- **VB**: Range(row,column)

Si vous avez une plage nommée qui s'étend de A1 à C4, la matrice contient 4 * 3 = 12 cellules. Les cellules individuelles de la plage sont disposées séquentiellement : Plage[0,0], Plage[0,1], Plage[0,2], Plage[1,0] ,Plage[1,1], Plage[1,2], Plage[2,0], Plage[2,1], Plage[2,2], Plage[3,0], Plage[3,1], Plage[3,2].

Utilisez les propriétés suivantes pour identifier les cellules dans la plage :

- La propriété FirstRow renvoie l'index de la première ligne de la plage nommée.
- La propriété FirstColumn renvoie l'index de la première colonne de la plage nommée.
- La propriété RowCount renvoie le nombre total de lignes dans la plage nommée.
- La propriété ColumnCount renvoie le nombre total de colonnes dans la plage nommée.

L'exemple suivant montre comment saisir certaines valeurs dans les cellules d'une plage spécifiée.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IdentifyCellsinNamedRange-1.cs" >}}

### **Accéder aux plages nommées**

#### **Accéder à une plage nommée spécifique**

Appelez la méthode [**GetRangeByName**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getrangebyname) de la collection [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) pour obtenir une plage par le nom spécifié. Une méthode [**GetRangeByName**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getrangebyname) typique prend le nom de la plage nommée et renvoie la plage nommée spécifiée en tant qu'instance de la classe [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range). L'exemple suivant montre comment accéder à une plage spécifiée par son nom.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-AccessSpecificNamedRange-1.cs" >}}

#### **Accéder à toutes les plages nommées dans une feuille de calcul**

Appelez la méthode [**GetNamedRanges**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getnamedranges) de la collection [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) pour obtenir toutes les plages nommées dans une feuille de calcul. La méthode [**GetNamedRanges**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getnamedranges) renvoie un tableau de toutes les plages nommées dans la collection [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection).

L'exemple suivant montre comment accéder à toutes les plages nommées dans un classeur.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-AccessAllNamedRanges-1.cs" >}}

### **Copier les plages nommées**

Aspose.Cells fournit la méthode [**Range.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/copy/index) pour copier une plage de cellules avec mise en forme dans une autre plage.

L'exemple suivant montre comment copier une plage source de cellules dans une autre plage nommée.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CopyNamedRanges-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
