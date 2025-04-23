---
title: Formater les cellules
description: Apprenez à formater et à styliser les cellules dans Aspose.Cells for .NET, y compris le formatage des nombres, le formatage des dates, les styles de police et d autres options de style de cellule. Notre guide vous aidera à créer des feuilles de calcul attrayantes et professionnelles.
keywords: Aspose.Cells for .NET, formatage des cellules, stylisation, formatage des nombres, formatage des dates, style de police, options de style de cellule, feuille de calcul, créer, aspect professionnel, formatage des lignes et des colonnes.
linktitle: Formater les cellules
type: docs
weight: 120
url: /fr/net/cells-formatting/
---

## **Introduction**

{{% alert color="primary" %}}

Aspose.Cells fournit les méthodes [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) et [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) de la classe [Cellule](https://reference.aspose.com/cells/net/aspose.cells/cell), utilisées pour obtenir/définir le style de formatage d'une cellule. Aspose.Cells fournit également une classe [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style).

{{% /alert %}}

## **Comment formater les cellules en utilisant les méthodes GetStyle et SetStyle**

Appliquer différents types de styles de formatage sur les cellules pour définir des couleurs de fond ou de premier plan, des bordures, des polices, des alignements horizontaux et verticaux, le niveau d'indentation, la direction du texte, l'angle de rotation et bien plus encore.

### **Comment utiliser les méthodes GetStyle et SetStyle**

Si les développeurs ont besoin d'appliquer différents styles de formatage à différentes cellules, il est préférable d'obtenir le [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) de la cellule en utilisant la méthode [**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle), spécifier les attributs de style et appliquer le formatage à l'aide de la méthode [**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle). Un exemple est donné ci-dessous pour illustrer cette approche d'application de divers formatages sur une cellule.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.cs" >}}

### **Comment utiliser l'objet de style pour formater différentes cellules**

Si les développeurs ont besoin d'appliquer le même style de formatage à différentes cellules, ils peuvent utiliser l'objet [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style). Veuillez suivre les étapes ci-dessous pour utiliser l'objet [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) :

1. Ajouter un objet [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) en appelant la méthode [**CreateStyle**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle) de la classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)
1. Accéder au nouvel objet [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) ajouté
1. Définir les propriétés/attributs souhaités de l'objet [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) pour appliquer les paramètres de formatage souhaités
1. Attribuer l'objet [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) configuré à vos cellules souhaitées

Cette approche peut grandement améliorer l'efficacité de vos applications et économiser de la mémoire également.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingStyleObject-1.cs" >}}

### **Comment utiliser les styles prédéfinis de Microsoft Excel 2007**

Si vous avez besoin d'appliquer différents styles de formatage pour Microsoft Excel 2007, appliquez les styles en utilisant l'API Aspose.Cells. Un exemple est donné ci-dessous pour illustrer cette approche d'application d'un style prédéfini sur une cellule.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.cs" >}}



## **Comment formater des caractères sélectionnés dans une cellule**

La gestion des paramètres de police explique comment formater du texte dans les cellules, mais cela explique seulement comment formater tout le contenu de la cellule. Et si vous voulez formater uniquement des caractères sélectionnés ?

Aspose.Cells prend également en charge cette fonctionnalité. Ce sujet explique comment nous utilisons cette fonctionnalité de manière efficace.

### **Comment formater des caractères sélectionnés**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contient la collection [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fournit une collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Chaque élément dans la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

La classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) fournit la méthode [**Characters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters) qui prend les paramètres suivants pour sélectionner une plage de caractères à l'intérieur d'une cellule :

- **Index de début**, l'index du caractère à partir duquel la sélection commence.
- **Nombre de caractères**, le nombre de caractères à sélectionner.

La méthode [**Characters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters) retourne une instance de la classe [**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) qui permet aux développeurs de formater les caractères de la même manière qu'une cellule comme indiqué ci-dessous dans l'exemple de code. Dans le fichier de sortie, dans la cellule A1, le mot 'Visite' sera formaté avec la police par défaut mais 'Aspose!' est en gras et bleu.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormattingSelectedCharacters-1.cs" >}}

{{% alert color="primary" %}}

Si vous souhaitez mettre en forme une partie du texte enrichi dans une cellule, envisagez d'utiliser les méthodes [**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) & [**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters). La [[**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) méthode est utilisée pour accéder aux portions du texte et les modifications peuvent être effectuées à l'aide de la méthode [**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) tandis que la méthode **Get** renvoie un tableau d'objets [**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) pouvant être manipulé pour régler diverses propriétés telles que le nom de la police, la couleur de la police, la mise en gras, etc. et la méthode **Set** peut être utilisée pour appliquer les modifications.

{{% /alert %}}

## **Comment formater les lignes et les colonnes**

Parfois, les développeurs doivent appliquer le même formatage sur des lignes ou des colonnes. Appliquer le formatage sur chaque cellule prend souvent plus de temps et n'est pas une bonne solution.
Pour résoudre ce problème, Aspose.Cells offre une solution simple et rapide qui est discutée en détail dans cet article.

### **Mise en forme des lignes & colonnes**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représentent un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fournit une collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). La collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) fournit une collection [**Rows**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows).

### **Comment formater une ligne**

Chaque élément dans la collection [**Rows**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows) représente un objet [**Row**](https://reference.aspose.com/cells/net/aspose.cells/row). L'objet [**Row**](https://reference.aspose.com/cells/net/aspose.cells/row) offre la méthode [**ApplyStyle**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) utilisée pour définir le format de la ligne. Pour appliquer le même formatage à une ligne, utilisez l'objet [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style). Les étapes ci-dessous montrent comment l'utiliser.

1. Ajouter un objet [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) à la classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) en appelant sa méthode [**CreateStyle**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle).
1. Définir les propriétés de l'objet [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) pour appliquer les paramètres de formatage.
1. Activer les attributs pertinents pour l'objet [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag).
1. Affecter l'objet [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) configuré à l'objet [**Row**](https://reference.aspose.com/cells/net/aspose.cells/row).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingARow-1.cs" >}}

### **Comment formater une colonne**

La collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) fournit également une collection [**Columns**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns). Chaque élément dans la collection [**Columns**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns) représente un objet [**Column**](https://reference.aspose.com/cells/net/aspose.cells/column). Tout comme un objet [**Row**](https://reference.aspose.com/cells/net/aspose.cells/row), l'objet [**Column**](https://reference.aspose.com/cells/net/aspose.cells/column) offre également la méthode [**ApplyStyle**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) pour formater une colonne.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingAColumn-1.cs" >}}

## **Sujets avancés**
- [Paramètres d'alignement](/cells/fr/net/cells-alignment-settings/)
- [Paramètres de bordure](/cells/fr/net/cells-border-settings/)
- [Définir les formats conditionnels des fichiers Excel et ODS.](/cells/fr/net/conditional-formatting/)
- [Thèmes et couleurs d'Excel](/cells/fr/net/excel-themes-and-colors/)
- [Paramètres de remplissage](/cells/fr/net/cells-fill-settings/)
- [Paramètres de police](/cells/fr/net/cells-font-settings/)
- [Formater les cellules de feuille de calcul dans un classeur](/cells/fr/net/format-worksheet-cells-in-a-workbook/)
- [Mise en œuvre du système de date 1904](/cells/fr/net/implement-1904-date-system/)
- [Fusionner et scinder des cellules](/cells/fr/net/merging-and-unmerging-cells/)
- [Paramètres de nombre](/cells/fr/net/cells-number-settings/)
- [Obtenir et définir le style des cellules](/cells/fr/net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

{{< app/cells/assistant language="csharp" >}}
