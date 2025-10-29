---
title: Créer un accès et copier les plages nommées
type: docs
weight: 200
url: /fr/python-net/create-access-and-copy-named-ranges/
description: Cet article montre comment créer un accès et copier des plages nommées avec l API Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Python Excel, Créer un accès et copier des plages nommées en Python, Créer des plages nommées en Python, Copier des plages nommées en Python, Accéder à toutes les plages nommées dans une feuille de calcul en Python.
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

## **Travailler avec une plage nommée en utilisant Aspose.Cells pour la bibliothèque Excel Python**

Ici, nous utilisons l'API Aspose.Cells pour Python via .NET pour effectuer la tâche.
Aspose.Cells pour Python via .NET fournit une classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contient une collection [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fournit une collection [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells).

### **Créer une plage nommée**

Il est possible de créer une plage nommée en appelant la méthode surchargée [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str-str) de la collection [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Une version typique de la méthode [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str-str) prend les paramètres suivants :

- Nom de la cellule en haut à gauche, nom de la cellule en haut à gauche dans la plage.
- Nom de la cellule inférieure droite, le nom de la cellule inférieure droite de la plage.

Lorsque la méthode [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str-str) est appelée, elle renvoie la plage nouvellement créée en tant qu'instance de la classe [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range). Utilisez cet objet [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) pour configurer la plage nommée. Par exemple, définissez le nom de la plage en utilisant la propriété [**name**](https://reference.aspose.com/cells/python-net/aspose.cells/range/name). L'exemple suivant montre comment créer une plage nommée de cellules qui s'étend de B4 à G14.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-CreateNamedRangeofCells-1.py" >}}

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-InputDataInCellsInRange-1.py" >}}

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-IdentifyCellsinNamedRange-1.py" >}}

### **Accéder aux plages nommées**

#### **Accéder à une plage nommée spécifique**

Appelez la méthode [**get_range_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/get_range_by_name/#str) de la collection [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) pour obtenir une plage par le nom spécifié. Une méthode [**get_range_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/get_range_by_name/#str) typique prend le nom de la plage nommée et renvoie la plage nommée spécifiée en tant qu'instance de la classe [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range). L'exemple suivant montre comment accéder à une plage spécifiée par son nom.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-AccessSpecificNamedRange-1.py" >}}

#### **Accéder à toutes les plages nommées dans une feuille de calcul**

Appelez la méthode [**get_named_ranges**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/get_named_ranges/#) de la collection [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) pour obtenir toutes les plages nommées dans une feuille de calcul. La méthode [**get_named_ranges**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/get_named_ranges/#) renvoie un tableau de toutes les plages nommées dans la collection [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/).

L'exemple suivant montre comment accéder à toutes les plages nommées dans un classeur.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-AccessAllNamedRanges-1.py" >}}

### **Copier les plages nommées**

Aspose.Cells pour Python via .NET fournit une [**Range.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy/#aspose.cells.Range) méthode pour copier une plage de cellules avec mise en forme dans une autre plage.

L'exemple suivant montre comment copier une plage source de cellules dans une autre plage nommée.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-CopyNamedRanges-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
