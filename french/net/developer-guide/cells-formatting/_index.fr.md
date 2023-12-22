---
title: Formater les cellules
description: Découvrez comment formater et styliser les cellules dans Aspose.Cells for .NET, y compris le formatage des nombres, le formatage de la date, les styles de police et d'autres options de style de cellule. Notre guide vous aidera à créer des feuilles de calcul attrayantes et d’aspect professionnel.
keywords: Aspose.Cells for .NET, cell formatting, styling, number formatting, date formatting, font style, cell style options, spreadsheet, create, professional look, format rows and columns.
linktitle: Formater les cellules
type: docs
weight: 120
url: /fr/net/cells-formatting/
---
##  **Introduction**

{{% alert color="primary" %}}

 Aspose.Cells fournit le[**ObtenirStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) et[**Définir le style**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) méthodes du[Cell](https://reference.aspose.com/cells/net/aspose.cells/cell) classe, utilisée pour obtenir/définir le style de formatage d’une cellule. Aspose.Cells fournit également un[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)classe.

{{% /alert %}}

##  **Comment formater Cells à l'aide des méthodes GetStyle et SetStyle**

Appliquez différents types de styles de formatage sur les cellules pour définir les couleurs d'arrière-plan ou de premier plan, les bordures, les polices, les alignements horizontaux et verticaux, le niveau d'indentation, la direction du texte, l'angle de rotation et bien plus encore.

###  **Comment utiliser les méthodes GetStyle et SetStyle**

 Si les développeurs doivent appliquer différents styles de formatage à différentes cellules, il est préférable d'obtenir le[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) de la cellule utilisant[**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) , spécifiez les attributs de style, puis appliquez le formatage à l'aide de[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)méthode. Un exemple est donné ci-dessous pour démontrer cette approche pour appliquer divers formats sur une cellule.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.cs" >}}

###  **Comment utiliser un objet de style pour formater différents Cells**

 Si les développeurs doivent appliquer le même style de formatage à différentes cellules, ils peuvent utiliser[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objet. Veuillez suivre les étapes ci-dessous pour utiliser le[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)objet:

1.  Ajouter un[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objet en appelant le[**Créer un style**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle) méthode du[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook)classe
1.  Accédez au nouveau[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) object
1.  Définissez les propriétés/attributs souhaités du[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)objet pour appliquer les paramètres de formatage souhaités
1.  Attribuer le configuré[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)s'opposer aux cellules souhaitées

Cette approche peut considérablement améliorer l'efficacité de vos applications et économiser de la mémoire.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingStyleObject-1.cs" >}}

###  **Comment utiliser les styles prédéfinis Microsoft Excel 2007**

Si vous devez appliquer différents styles de mise en forme pour Microsoft Excel 2007, appliquez les styles à l'aide du Aspose.Cells API. Un exemple est donné ci-dessous pour illustrer cette approche pour appliquer un style prédéfini sur une cellule.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.cs" >}}



##  **Comment formater les caractères sélectionnés dans un Cell**

Gestion des paramètres de police explique comment formater le texte dans les cellules, mais explique uniquement comment formater tout le contenu des cellules. Que faire si vous souhaitez formater uniquement les caractères sélectionnés ?

Aspose.Cells prend également en charge cette fonctionnalité. Cette rubrique explique comment utiliser cette fonctionnalité efficacement.

###  **Comment formater les caractères sélectionnés**

 Aspose.Cells propose un cours,[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Excel Microsoft. Le[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contient le[**Des feuilles de calcul**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)collection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fournit un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection. Chaque élément du[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) la collection représente un objet de la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)classe.

 Le[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) la classe fournit le[**Personnages**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters)méthode qui prend les paramètres suivants pour sélectionner une plage de caractères à l'intérieur d'une cellule :

- *Start Index**, l'index du caractère à partir duquel la sélection commence.
- *Nombre de caractères**, le nombre de caractères à sélectionner.

 Le[**Personnages**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters) La méthode renvoie une instance du[**Paramètres de police**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)classe qui permet aux développeurs de formater les caractères de la même manière qu'ils le feraient pour une cellule, comme indiqué ci-dessous dans l'exemple de code. Dans le fichier de sortie, dans la cellule A1, le mot « Visite » sera formaté avec la police par défaut mais « Aspose ! est gras et bleu.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormattingSelectedCharacters-1.cs" >}}

{{% alert color="primary" %}}

Si vous souhaitez formater une partie du texte enrichi dans une cellule, envisagez d'utiliser l'option[**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) & [**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) méthodes. Le[[**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) La méthode doit être utilisée pour accéder aux parties du texte, puis des modifications peuvent être apportées à l'aide de la méthode[**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) méthode alors que le**Obtenir** La méthode renvoie un tableau de[**Paramètres de police**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) des objets qui peuvent être manipulés pour définir diverses propriétés telles que le nom de la police, la couleur de la police, l'audace, etc. et**Ensemble** La méthode peut être utilisée pour appliquer les modifications.

{{% /alert %}}

##  **Comment formater les lignes et les colonnes**

Parfois, les développeurs doivent appliquer la même mise en forme aux lignes ou aux colonnes. Appliquer le formatage sur les cellules une par une prend souvent plus de temps et n'est pas une bonne solution.
Pour résoudre ce problème, Aspose.Cells propose un moyen simple et rapide, expliqué en détail dans cet article.

###  **Formatage des lignes et des colonnes**

 Aspose.Cells propose une classe, le[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Excel Microsoft. Le[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contient un[**Des feuilles de calcul**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection qui permet d’accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fournit un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection. Le[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) la collection fournit un[**Lignes**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows)collection.

###  **Comment formater une ligne**

 Chaque élément du[**Lignes**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows) la collection représente un[**Rangée**](https://reference.aspose.com/cells/net/aspose.cells/row) objet. Le[**Rangée**](https://reference.aspose.com/cells/net/aspose.cells/row)l'objet offre le[**Appliquer le style**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) méthode utilisée pour définir la mise en forme de la ligne. Pour appliquer la même mise en forme à une ligne, utilisez le[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)objet. Les étapes ci-dessous montrent comment l'utiliser.

1.  Ajouter un[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) s'opposer à la[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe en appelant son[**Créer un style**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle)méthode.
1.  Met le[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)propriétés de l'objet pour appliquer les paramètres de formatage.
1.  Activez les attributs pertinents pour le[**StyleDrapeau**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)objet.
1.  Attribuer le configuré[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) s'opposer à la[**Rangée**](https://reference.aspose.com/cells/net/aspose.cells/row)objet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingARow-1.cs" >}}

###  **Comment formater une colonne**

 Le[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) la collection fournit également un[**Colonnes**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns) collection. Chaque élément du[**Colonnes**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns) la collection représente un[**Colonne**](https://reference.aspose.com/cells/net/aspose.cells/column) objet. Semblable à un[**Rangée**](https://reference.aspose.com/cells/net/aspose.cells/row) objet, le[**Colonne**](https://reference.aspose.com/cells/net/aspose.cells/column) l'objet offre également le[**Appliquer le style**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle)méthode de formatage d’une colonne.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingAColumn-1.cs" >}}

##  **Sujets avancés**
- [Paramètres d'alignement](/cells/fr/net/cells-alignment-settings/)
- [Paramètres de bordure](/cells/fr/net/cells-border-settings/)
- [Définissez les formats conditionnels des fichiers Excel et ODS.](/cells/fr/net/conditional-formatting/)
- [Thèmes et couleurs Excel](/cells/fr/net/excel-themes-and-colors/)
- [Paramètres de remplissage](/cells/fr/net/cells-fill-settings/)
- [Paramètres de police](/cells/fr/net/cells-font-settings/)
- [Formater la feuille de calcul Cells dans un classeur](/cells/fr/net/format-worksheet-cells-in-a-workbook/)
- [Implémenter le système de date 1904](/cells/fr/net/implement-1904-date-system/)
- [Fusion et dissociation Cells](/cells/fr/net/merging-and-unmerging-cells/)
- [Paramètres numériques](/cells/fr/net/cells-number-settings/)
- [Obtenir et définir le style des cellules](/cells/fr/net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

