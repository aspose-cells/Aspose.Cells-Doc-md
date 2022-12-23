---
title: Créer un accès et copier des plages nommées
type: docs
weight: 200
url: /fr/net/create-access-and-copy-named-ranges/
---
## **Introduction**

Normalement, les étiquettes de colonne et de ligne sont utilisées pour désigner des cellules individuelles. Il est possible de créer des noms descriptifs pour représenter des cellules, des plages de cellules, des formules ou des valeurs constantes. Le mot**Nom** peut faire référence à une chaîne de caractères qui représente une cellule, une plage de cellules, une formule ou une valeur constante. Attribuer un nom à une plage signifie que cette plage de cellules peut être référencée par son nom. Utilisez des noms faciles à comprendre, tels que Produits, pour faire référence à des gammes difficiles à comprendre, telles que Ventes ! C20 : C30. Les étiquettes peuvent être utilisées dans des formules faisant référence à des données sur la même feuille de calcul ; si vous souhaitez représenter une plage sur une autre feuille de calcul, vous pouvez utiliser un nom. * Les plages nommées font partie des fonctionnalités les plus puissantes de Microsoft Excel, en particulier lorsqu'elles sont utilisées comme plage source pour les contrôles de liste, les tableaux croisés dynamiques, les graphiques, etc.

## **Travailler avec une plage nommée à l'aide d'Excel Microsoft**

### **Créer des plages nommées**

 Les étapes suivantes décrivent comment nommer une cellule ou une plage de cellules à l'aide de**Microsoft Excel** . Cette méthode s'applique à**Microsoft OfficeExcel 2003**, **Microsoft Excel 97**, **2000** et**2002**.

1. Sélectionnez la cellule, la plage de cellules que vous souhaitez nommer.
1.  Clique le**Boîte de nom** à l'extrémité gauche de la barre de formule.
1. Tapez le nom des cellules.
1. Appuyez sur Entrée.

{{% alert color="primary" %}}

Vous ne pouvez pas nommer une cellule pendant que vous modifiez le contenu de la cellule.

{{% /alert %}}

## **Travailler avec une plage nommée à l'aide de Aspose.Cells**

Ici, nous utilisons le Aspose.Cells API pour effectuer la tâche.
 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Excel Microsoft. Le[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe contient un[**Feuilles de travail**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe offre une[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) le recueil.

### **Créer une plage nommée**

 Il est possible de créer une plage nommée en appelant le surchargé[**CréerPlage**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) méthode de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) le recueil. Une version typique de[**CréerPlage**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/3) méthode prend les paramètres suivants :

- Nom de la cellule supérieure gauche, nom de la cellule supérieure gauche de la plage.
- Nom de la cellule inférieure droite, nom de la cellule inférieure droite de la plage.

 Quand le[**CréerPlage**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/3) est appelée, elle renvoie la plage nouvellement créée en tant qu'instance de la[**Intervalle**](https://reference.aspose.com/cells/net/aspose.cells/range) classe. Utilisez ceci[**Intervalle**](https://reference.aspose.com/cells/net/aspose.cells/range) objet pour configurer la plage nommée. Par exemple, définissez le nom de la plage à l'aide de la[**Nom**](https://reference.aspose.com/cells/net/aspose.cells/range/properties/name) la propriété. L'exemple suivant montre comment créer une plage de cellules nommée qui s'étend sur B4:G14.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CreateNamedRangeofCells-1.cs" >}}

### **Données d'entrée dans le Cells dans la plage nommée**

Vous pouvez insérer des données dans les cellules individuelles d'une plage en suivant le modèle

- **C#**: Plage[ligne,colonne]
- **VB**: Plage(ligne,colonne)

Supposons que vous ayez une plage de cellules nommée qui s'étend sur A1: C4. La matrice fait 4 * 3 = 12 cellules. Les cellules de plage individuelles sont disposées séquentiellement : Range[0,0], Range[0,1], Range[0,2], Range[1,0], Range[1,1], Range[1,2], Plage[2,0], Plage[2,1], Plage[2,2], Plage[3,0], Plage[3,1], Plage[3,2].

Utilisez les propriétés suivantes pour identifier les cellules de la plage :

- FirstRow renvoie l'index de la première ligne de la plage nommée.
- FirstColumn renvoie l'index de la première colonne de la plage nommée.
- RowCount renvoie le nombre total de lignes dans la plage nommée.
- ColumnCount renvoie le nombre total de colonnes dans la plage nommée.

L'exemple suivant montre comment saisir des valeurs dans les cellules d'une plage spécifiée.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-InputDataInCellsInRange-1.cs" >}}

### **Identifiez Cells dans la plage nommée**

Vous pouvez insérer des données dans les cellules individuelles d'une plage en suivant le modèle :

- **C#**: Plage[ligne,colonne]
- **VB**: Plage(ligne,colonne)

Si vous avez une plage nommée qui s'étend sur A1:C4. La matrice fait 4 * 3 = 12 cellules. Les cellules de plage individuelles sont disposées séquentiellement : Range[0,0], Range[0,1], Range[0,2], Range[1,0] ,Range[1,1], Range[1,2], Plage[2,0], Plage[2,1], Plage[2,2], Plage[3,0], Plage[3,1], Plage[3,2].

Utilisez les propriétés suivantes pour identifier les cellules de la plage :

- FirstRow renvoie l'index de la première ligne de la plage nommée.
- FirstColumn renvoie l'index de la première colonne de la plage nommée.
- RowCount renvoie le nombre total de lignes dans la plage nommée.
- ColumnCount renvoie le nombre total de colonnes dans la plage nommée.

L'exemple suivant montre comment saisir des valeurs dans les cellules d'une plage spécifiée.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IdentifyCellsinNamedRange-1.cs" >}}

### **Accéder aux plages nommées**

#### **Accéder à une plage nommée spécifique**

 Appeler le[**Feuilles de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) de la collection[**GetRangeByName**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getrangebyname) méthode pour obtenir une plage par le nom spécifié. Un typique[**GetRangeByName**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getrangebyname) prend le nom de la plage nommée et renvoie la plage nommée spécifiée en tant qu'instance de la[**Intervalle**](https://reference.aspose.com/cells/net/aspose.cells/range) classe. L'exemple suivant montre comment accéder à une plage spécifiée par son nom.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-AccessSpecificNamedRange-1.cs" >}}

#### **Accéder à toutes les plages nommées dans une feuille de calcul**

 Appeler le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) de la collection[**GetNamedRanges**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getnamedranges) méthode pour obtenir toutes les plages nommées dans une feuille de calcul. Le[**GetNamedRanges**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getnamedranges) renvoie un tableau de toutes les plages de noms dans le[**Feuilles de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) le recueil.

L'exemple suivant montre comment accéder à toutes les plages nommées dans un classeur.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-AccessAllNamedRanges-1.cs" >}}

### **Copier les plages nommées**

 Aspose.Cells fournit[**Range.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/copy/index) méthode pour copier une plage de cellules avec mise en forme dans une autre plage.

L'exemple suivant montre comment copier une plage source de cellules dans une autre plage nommée.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CopyNamedRanges-1.cs" >}}
