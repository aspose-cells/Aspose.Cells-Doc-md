---
title: Imprimer des feuilles de calcul
type: docs
weight: 20
url: /fr/net/print-spreadsheets/
---
Les paramètres de mise en page fournissent également plusieurs options d'impression (également appelées options de feuille ) qui permettent aux utilisateurs de contrôler leurs pages imprimées de feuilles de calcul. Ces options d'impression permettent aux utilisateurs de :

- Sélectionnez une zone d'impression spécifique de la feuille de calcul
- Titres imprimés
- Imprimer le quadrillage
- Imprimer les en-têtes de ligne/colonne
- Atteindre la qualité brouillon
- Imprimer les commentaires
- Erreurs d'impression Cell
- Définir l'ordre des pages
  **Définition des options d'impression/feuille**

Aspose.Cells prend en charge toutes ces options d'impression et les développeurs peuvent facilement configurer ces options pour les feuilles de calcul souhaitées à l'aide des différentes propriétés proposées par la classe PageSetup. L'utilisation de ces propriétés de la classe PageSetup est décrite ci-dessous plus en détail.
## **Définir la zone d'impression**
Par défaut, seule la zone d'impression est sélectionnée qui intègre toute la zone de la feuille de calcul, qui contient des données, mais les développeurs peuvent également établir une zone d'impression spécifique de la feuille de calcul en fonction de leur souhait.

 Pour sélectionner une zone d'impression spécifique, les développeurs peuvent utiliser set**Zone d'impression** méthode de la**Mise en page** classer. Vous pouvez fournir la plage de cellules de la zone d'impression à cette méthode en tant qu'argument.

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Specifying the cells range (from A1 cell to T35 cell) of the print area

pageSetup.PrintArea = "A1:T35";


{{< /highlight >}}
## **Définir les titres d'impression**
 Aspose.Cells vous permet de désigner les en-têtes de ligne et de colonne que vous souhaitez voir répétés sur toutes les pages de votre feuille de calcul imprimée. Pour ce faire, les développeurs peuvent utiliser set**PrintTitleColumns** et**setPrintTitleRows** méthodes de la**Mise en page** classer.

Les lignes ou colonnes (à répéter sur toutes les pages de la feuille de calcul imprimée) sont définies en passant leurs numéros de ligne ou de colonne. Par exemple, les lignes sont définies comme \ $1 : \ $2 et les colonnes sont définies comme \ $A : \ $B.

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

Aspose.Cells.PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Defining column numbers A & B as title columns

pageSetup.PrintTitleColumns = "$A:$B";

//Defining row numbers 1 & 2 as title rows

pageSetup.PrintTitleRows = "$1:$2";

{{< /highlight >}}
## **Définir d'autres options d'impression**
**Mise en page** La classe fournit également plusieurs autres méthodes pour définir les options d'impression générales comme suit :

- **Méthode setPrintGridline** , un paramètre booléen est passé à cette méthode qui définit s'il faut imprimer ou non le quadrillage
- **Méthode setPrintHeadingssetPrintHeadings method** un paramètre booléen est passé à cette méthode qui définit s'il faut imprimer ou non les en-têtes de ligne et de colonne
- **méthode setBlackAndWhitesetBlackAndWhite method** , un paramètre booléen est passé à cette méthode qui définit s'il faut imprimer la feuille de calcul en mode noir et blanc ou non
- **Méthode setPrintCommentssetPrintComments method** , définit l'affichage des commentaires d'impression sur la feuille de calcul ou à la fin de la feuille de calcul
- **méthode setPrintDraftsetPrintDraft method** , un paramètre booléen est passé à cette méthode qui définit s'il faut imprimer la feuille de calcul en qualité brouillon ou non
- **Méthode setPrintErrorssetPrintErrors method** , définit si les erreurs de cellule doivent être imprimées telles qu'elles sont affichées, vides, tirets ou N/A

 Pour utiliser l'ensemble**ImprimerCommentaires** Et mettre**Erreurs d'impression** méthodes, Aspose.Cells fournit également deux énumérations, PrintCommentsType et PrintErrorsType qui contiennent des valeurs prédéfinies à transmettre à des paramètres pour définir respectivement les méthodes PrintComments et PrintErrors.

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Allowing to print gridlines

pageSetup.PrintGridlines = true;

//Allowing to print row/column headings

pageSetup.PrintHeadings = true;

//Allowing to print worksheet in black & white mode

pageSetup.BlackAndWhite = true;

//Allowing to print comments as displayed on worksheet

pageSetup.PrintComments = PrintCommentsType.PrintInPlace;

//Allowing to print worksheet with draft quality

pageSetup.PrintDraft = true;

//Allowing to print cell errors as N/A

pageSetup.PrintErrors = PrintErrorsType.PrintErrorsNA;

{{< /highlight >}}
## **Définir l'ordre des pages**
**Mise en page**La classe fournit la méthode set Order qui est utilisée pour ordonner l'impression de plusieurs pages de votre feuille de calcul. Il existe deux possibilités pour ordonner les pages comme suit :

Bas puis dessus ainsi il imprimera toutes les pages vers le bas avant d'imprimer les pages vers la droite
Plus puis vers le bas ainsi il imprimera les pages de gauche à droite avant d'imprimer les pages ci-dessous
Aspose.Cells fournit une énumération, PrintOrderType qui contient tous les types de commande prédéfinis à affecter à la méthode setPage Order.

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Setting the printing order of the pages to over then down

pageSetup.Order = PrintOrderType.OverThenDown;

{{< /highlight >}}
## **Télécharger l'exemple de code**
- [GithubGenericName](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Print%20Spreadsheet%20with%20Options%20%28Aspose.Cells%29.zip)
