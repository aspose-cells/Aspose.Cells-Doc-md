---
title: Formater les cellules
linktitle: Formater les cellules
type: docs
weight: 120
url: /fr/net/cells-formatting/
description: Définissez le format numérique, la bordure et la couleur d'arrière-plan des fichiers Excel sur les plates-formes .NET Framework, .NET Core, Mono ou Xamarin.
---
## **Introduction**

{{% alert color="primary" %}}

 Aspose.Cells fournit le[**ObtenirStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) et[**DéfinirStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) méthodes de la[Cell](https://reference.aspose.com/cells/net/aspose.cells/cell) classe, utilisée pour obtenir/définir le style de formatage d'une cellule. Aspose.Cells fournit également un[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)classe.

{{% /alert %}}

## **Formater Cells à l'aide des méthodes GetStyle et SetStyle**

Appliquez différents types de styles de mise en forme sur les cellules pour définir les couleurs d'arrière-plan ou de premier plan, les bordures, les polices, les alignements horizontaux et verticaux, le niveau d'indentation, la direction du texte, l'angle de rotation et bien plus encore.

### **Utilisation des méthodes GetStyle et SetStyle**

 Si les développeurs doivent appliquer différents styles de mise en forme à différentes cellules, il est préférable d'obtenir le[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) de la cellule à l'aide[**Cell.GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) méthode, spécifiez les attributs de style, puis appliquez la mise en forme à l'aide[**Cell.SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle)méthode. Un exemple est donné ci-dessous pour démontrer cette approche pour appliquer divers formatages sur une cellule.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingGetStyleSetStyle-1.cs" >}}

### **Utilisation d'un objet de style pour formater différents Cells**

 Si les développeurs doivent appliquer le même style de mise en forme à différentes cellules, ils peuvent utiliser[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objet. Veuillez suivre les étapes ci-dessous pour utiliser le[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)objet:

1.  Ajouter un[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objet en appelant le[**CréerStyle**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle) méthode de la[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook)classe
1.  Accéder au nouveau[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)objet
1.  Définissez les propriétés/attributs souhaités du[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)objet pour appliquer les paramètres de formatage souhaités
1. Attribuez la configuration[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)objectez à vos cellules désirées

Cette approche peut grandement améliorer l'efficacité de vos applications et également économiser de la mémoire.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingStyleObject-1.cs" >}}

### **Utilisation des styles prédéfinis Microsoft Excel 2007**

Si vous devez appliquer différents styles de mise en forme pour Microsoft Excel 2007, appliquez les styles à l'aide de Aspose.Cells API. Un exemple est donné ci-dessous pour illustrer cette approche pour appliquer un style prédéfini sur une cellule.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-UsingExcelPredefinedStyles-1.cs" >}}



## **Formatage des caractères sélectionnés dans un Cell**

La gestion des paramètres de police explique comment formater le texte dans les cellules, mais explique uniquement comment formater tout le contenu de la cellule. Que faire si vous souhaitez formater uniquement les caractères sélectionnés ?

Aspose.Cells prend également en charge cette fonctionnalité. Cette rubrique explique comment utiliser efficacement cette fonctionnalité.

### **Formatage des caractères sélectionnés**

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Excel Microsoft. Le[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe contient le[**Feuilles de travail**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe offre une[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) le recueil. Chaque élément de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection représente un objet de la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)classe.

 Le[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) la classe fournit la[**Personnages**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters)méthode qui prend les paramètres suivants pour sélectionner une plage de caractères à l'intérieur d'une cellule :

- **Index de départ**, l'index du caractère à partir duquel la sélection commence.
- **Nombre de caractères**, le nombre de caractères à sélectionner.

 Le[**Personnages**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/characters) La méthode renvoie une instance de[**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)classe qui permet aux développeurs de formater les caractères de la même manière qu'ils le feraient pour une cellule, comme indiqué ci-dessous dans l'exemple de code. Dans le fichier de sortie, dans la cellule A1, le mot 'Visite' sera formaté avec la police par défaut mais 'Aspose!' est gras et bleu.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormattingSelectedCharacters-1.cs" >}}

{{% alert color="primary" %}}

 Si vous souhaitez mettre en forme une partie de texte enrichi dans une cellule, envisagez d'utiliser la[**Cell.GetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) & [**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) méthodes. Le[[**Cell.GetCharacters**]](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters) méthode doit être utilisée pour accéder aux parties du texte, puis les modifications peuvent être effectuées à l'aide de la[**Cell.SetCharacters**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) méthode alors que la**Obtenir**méthode renvoie un tableau de[**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) des objets qui peuvent être manipulés pour définir diverses propriétés telles que le nom de la police, la couleur de la police, l'audace, etc. et**Ensemble** peut être utilisée pour appliquer les modifications.

{{% /alert %}}

## **Formatage des lignes et des colonnes**

Parfois, les développeurs doivent appliquer le même formatage sur des lignes ou des colonnes. Appliquer une mise en forme sur les cellules une par une prend souvent plus de temps et n'est pas une bonne solution.
Pour résoudre ce problème, Aspose.Cells fournit un moyen simple et rapide décrit en détail dans cet article.

### **Formatage des lignes et des colonnes**

 Aspose.Cells fournit une classe, la[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Excel Microsoft. Le[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe contient un[**Feuilles de travail**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe offre une[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) le recueil. Le[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collecte offre une[**Lignes**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows)le recueil.

### **Formater une ligne**

 Chaque élément de la[**Lignes**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/rows) la collection représente un[**Ligne**](https://reference.aspose.com/cells/net/aspose.cells/row) objet. Le[**Ligne**](https://reference.aspose.com/cells/net/aspose.cells/row)l'objet offre le[**AppliquerStyle**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) méthode utilisée pour définir le formatage de la ligne. Pour appliquer le même formatage à une ligne, utilisez la[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)objet. Les étapes ci-dessous montrent comment l'utiliser.

1.  Ajouter un[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) s'opposer à la[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe en appelant sa[**CréerStyle**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/createstyle)méthode.
1.  Met le[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)propriétés de l'objet pour appliquer les paramètres de formatage.
1.  Activez les attributs pertinents pour le[**StyleDrapeau**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)objet.
1. Attribuez la configuration[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) s'opposer à la[**Ligne**](https://reference.aspose.com/cells/net/aspose.cells/row)objet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingARow-1.cs" >}}

### **Formater une colonne**

 Le[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection offre également une[**Colonnes**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns) le recueil. Chaque élément de la[**Colonnes**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/columns) la collection représente un[**Colonne**](https://reference.aspose.com/cells/net/aspose.cells/column) objet. Semblable à un[**Ligne**](https://reference.aspose.com/cells/net/aspose.cells/row) objet, le[**Colonne**](https://reference.aspose.com/cells/net/aspose.cells/column) objet offre également la[**AppliquerStyle**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle)méthode de formatage d'une colonne.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-FormatRowsColumns-FormattingAColumn-1.cs" >}}

## **Sujets avancés**
- [Paramètres d'alignement](/cells/fr/net/cells-alignment-settings/)
- [Paramètres de bordure](/cells/fr/net/cells-border-settings/)
- [Définissez les formats conditionnels des fichiers Excel et ODS.](/cells/fr/net/conditional-formatting/)
- [Thèmes et couleurs Excel](/cells/fr/net/excel-themes-and-colors/)
- [Paramètres de remplissage](/cells/fr/net/cells-fill-settings/)
- [Paramètres de police](/cells/fr/net/cells-font-settings/)
- [Formater la feuille de calcul Cells dans un classeur](/cells/fr/net/format-worksheet-cells-in-a-workbook/)
- [Mettre en œuvre le système de date 1904](/cells/fr/net/implement-1904-date-system/)
- [Fusion et défusion Cells](/cells/fr/net/merging-and-unmerging-cells/)
- [Paramètres du numéro](/cells/fr/net/cells-number-settings/)
- [Obtenir et définir le style des cellules](/cells/fr/net/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

