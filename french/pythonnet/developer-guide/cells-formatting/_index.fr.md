---
title: Formater les cellules
description: Apprenez comment formater et styliser les cellules dans Aspose.Cells pour Python via .NET, y compris le formatage des nombres, la mise en forme des dates, les styles de police, et autres options de style de cellule. Notre guide vous aidera à créer des feuilles de calcul attrayantes et professionnelles.
keywords: Aspose.Cells pour Python via .NET, formatage de cellule, stylisation, formatage de nombres, mise en forme de dates, style de police, options de style de cellule, feuille de calcul, création, aspect professionnel, formatage des lignes et colonnes.
linktitle: Formater les cellules
type: docs
weight: 120
url: /fr/python-net/cells-formatting/
---

## **Introduction**

{{% alert color="primary" %}}

Aspose.Cells pour Python via .NET fournit les méthodes [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) et [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) de la classe [Cell](https://reference.aspose.com/cells/python-net/aspose.cells/cell), utilisées pour obtenir/configurer le style de formatage d'une cellule. Aspose.Cells pour Python via .NET fournit également une classe [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style).

{{% /alert %}}

## **Comment formater les cellules en utilisant les méthodes GetStyle et SetStyle**

Appliquer différents types de styles de formatage sur les cellules pour définir des couleurs de fond ou de premier plan, des bordures, des polices, des alignements horizontaux et verticaux, le niveau d'indentation, la direction du texte, l'angle de rotation et bien plus encore.

### **Comment utiliser les méthodes GetStyle et SetStyle**

Si les développeurs ont besoin d'appliquer différents styles de formatage à différentes cellules, il est préférable d'obtenir le [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) de la cellule en utilisant la méthode [**Cell.get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style), spécifier les attributs de style et appliquer le formatage à l'aide de la méthode [**Cell.set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style). Un exemple est donné ci-dessous pour illustrer cette approche d'application de divers formatages sur une cellule.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.py" >}}

### **Comment utiliser l'objet de style pour formater différentes cellules**

Si les développeurs ont besoin d'appliquer le même style de formatage à différentes cellules, ils peuvent utiliser l'objet [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style). Veuillez suivre les étapes ci-dessous pour utiliser l'objet [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) :

1. Ajouter un objet [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) en appelant la méthode [**create_style**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/create_style) de la classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)
1. Accéder au nouvel objet [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) ajouté
1. Définir les propriétés/attributs souhaités de l'objet [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) pour appliquer les paramètres de formatage souhaités
1. Attribuer l'objet [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) configuré à vos cellules souhaitées

Cette approche peut grandement améliorer l'efficacité de vos applications et économiser de la mémoire également.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApproachesToFormatData-UsingStyleObject-1.py" >}}

### **Comment utiliser les styles prédéfinis de Microsoft Excel 2007**

Si vous avez besoin d'appliquer différents styles de formatage pour Microsoft Excel 2007, appliquez les styles en utilisant l'API Aspose.Cells pour Python via .NET. Un exemple est donné ci-dessous pour démontrer cette approche d'application d'un style prédéfini sur une cellule.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.py" >}}



## **Comment formater des caractères sélectionnés dans une cellule**

La gestion des paramètres de police explique comment formater du texte dans les cellules, mais cela explique seulement comment formater tout le contenu de la cellule. Et si vous voulez formater uniquement des caractères sélectionnés ?

Aspose.Cells pour Python via .NET supporte également cette fonctionnalité. Ce sujet explique comment utiliser cette fonctionnalité efficacement.

### **Comment formater des caractères sélectionnés**

Aspose.Cells pour Python via .NET fournit une classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contient la collection [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) qui permet d’accéder à chaque feuille de calcul dans un fichier Excel. Une feuille est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fournit une collection [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). Chaque élément de la collection [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

La classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) fournit la méthode [**characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/characters) qui prend les paramètres suivants pour sélectionner une plage de caractères à l'intérieur d'une cellule :

- **Index de début**, l'index du caractère à partir duquel la sélection commence.
- **Nombre de caractères**, le nombre de caractères à sélectionner.

La méthode [**characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/characters) retourne une instance de la classe [**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting) qui permet aux développeurs de formater les caractères de la même manière qu'une cellule comme indiqué ci-dessous dans l'exemple de code. Dans le fichier de sortie, dans la cellule A1, le mot 'Visite' sera formaté avec la police par défaut mais 'Aspose!' est en gras et bleu.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-FormattingSelectedCharacters-1.py" >}}

{{% alert color="primary" %}}

Si vous souhaitez formater une partie du texte enrichi dans une cellule, envisagez d'utiliser les méthodes [**Cell.get_characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters) et [**Cell.set_characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters). La méthode [**Cell.get_characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters) doit être utilisée pour accéder aux parties du texte, puis des modifications peuvent être effectuées en utilisant la méthode [**Cell.set_characters**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters), tandis que la méthode **Get** renvoie un tableau d'objets [**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting) qui peuvent être manipulés pour définir diverses propriétés telles que le nom de police, la couleur de police, le gras, etc., et la méthode **Set** peut être utilisée pour appliquer les modifications.

{{% /alert %}}

## **Comment formater les lignes et les colonnes**

Parfois, les développeurs doivent appliquer le même formatage sur des lignes ou des colonnes. Appliquer le formatage sur chaque cellule prend souvent plus de temps et n'est pas une bonne solution.
Pour résoudre ce problème, Aspose.Cells pour Python via .NET offre une méthode simple et rapide, décrite en détail dans cet article.

### **Mise en forme des lignes & colonnes**

Aspose.Cells pour Python via .NET fournit une classe, la [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contient une collection [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) permettant d’accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) offre une collection [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). La collection [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) fournit une collection [**rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/rows).

### **Comment formater une ligne**

Chaque élément dans la collection [**rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/rows) représente un objet [**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row). L'objet [**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row) offre la méthode [**apply_style**](https://reference.aspose.com/cells/python-net/aspose.cells/row/apply_style) utilisée pour définir le format de la ligne. Pour appliquer le même formatage à une ligne, utilisez l'objet [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style). Les étapes ci-dessous montrent comment l'utiliser.

1. Ajouter un objet [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) à la classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) en appelant sa méthode [**create_style**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/create_style).
1. Définir les propriétés de l'objet [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) pour appliquer les paramètres de formatage.
1. Activer les attributs pertinents pour l'objet [**StyleFlag**](https://reference.aspose.com/cells/python-net/aspose.cells/styleflag).
1. Affecter l'objet [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) configuré à l'objet [**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-FormatRowsColumns-FormattingARow-1.py" >}}

### **Comment formater une colonne**

La collection [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) fournit également une collection [**columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/columns). Chaque élément dans la collection [**columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/columns) représente un objet [**Column**](https://reference.aspose.com/cells/python-net/aspose.cells/column). Tout comme un objet [**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row), l'objet [**Column**](https://reference.aspose.com/cells/python-net/aspose.cells/column) offre également la méthode [**apply_style**](https://reference.aspose.com/cells/python-net/aspose.cells/row/apply_style) pour formater une colonne.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-FormatRowsColumns-FormattingAColumn-1.py" >}}

## **Sujets avancés**
- [Paramètres d'alignement](/cells/fr/python-net/cells-alignment-settings/)
- [Paramètres de bordure](/cells/fr/python-net/cells-border-settings/)
- [Définir les formats conditionnels des fichiers Excel et ODS.](/cells/fr/python-net/conditional-formatting/)
- [Thèmes et couleurs d'Excel](/cells/fr/python-net/excel-themes-and-colors/)
- [Paramètres de remplissage](/cells/fr/python-net/cells-fill-settings/)
- [Paramètres de police](/cells/fr/python-net/cells-font-settings/)
- [Formater les cellules de feuille de calcul dans un classeur](/cells/fr/python-net/format-worksheet-cells-in-a-workbook/)
- [Mise en œuvre du système de date 1904](/cells/fr/python-net/implement-1904-date-system/)
- [Fusionner et scinder des cellules](/cells/fr/python-net/merging-and-unmerging-cells/)
- [Paramètres de nombre](/cells/fr/python-net/cells-number-settings/)
- [Obtenir et définir le style des cellules](/cells/fr/python-net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

