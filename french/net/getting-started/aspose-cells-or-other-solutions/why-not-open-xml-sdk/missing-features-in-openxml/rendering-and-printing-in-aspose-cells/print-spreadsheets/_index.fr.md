---
title: Imprimer des feuilles de calcul
type: docs
weight: 20
url: /fr/net/print-spreadsheets/
---

Les paramètres de mise en page offrent également plusieurs options d'impression (également appelées options de feuille) qui permettent aux utilisateurs de contrôler leurs pages imprimées de feuille de calcul. Ces options d'impression permettent aux utilisateurs de :

- Sélectionner une zone d'impression spécifique de la feuille de calcul
- Imprimer les titres
- Imprimer les quadrillages
- Imprimer les en-têtes de ligne/colonne
- Obtenir une qualité brouillon
- Imprimer les commentaires
- Imprimer les erreurs de cellule
- Définir l'ordre des pages
  **Paramètres d'impression/d'onglet**

Aspose.Cells prend en charge toutes ces options d'impression et les développeurs peuvent facilement configurer ces options pour leurs feuilles de calcul souhaitées à l'aide des plusieurs propriétés offertes par la classe PageSetup. L'utilisation de ces propriétés de la classe PageSetup est discutée ci-dessous de manière plus détaillée.
## **Définir la zone d'impression**
Par défaut, seule cette zone d'impression est sélectionnée qui incorpore toute la zone de la feuille de calcul contenant des données, mais les développeurs peuvent également établir une zone d'impression spécifique de la feuille de calcul selon leur souhait.

Pour sélectionner une zone d'impression spécifique, les développeurs peuvent utiliser la méthode **setPrintArea** de la classe **PageSetup**. Vous pouvez fournir la plage de cellules de la zone d'impression à cette méthode en argument.

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Specifying the cells range (from A1 cell to T35 cell) of the print area

pageSetup.PrintArea = "A1:T35";


{{< /highlight >}}
## **Définir les titres d'impression**
Aspose.Cells vous permet de spécifier les en-têtes de lignes et de colonnes que vous voulez avoir répétés sur toutes les pages de votre feuille de calcul imprimée. Pour ce faire, les développeurs peuvent utiliser les méthodes **setPrintTitleColumns** et **setPrintTitleRows** de la classe **PageSetup**.

Les lignes ou colonnes (à répéter sur toutes les pages de la feuille de calcul imprimée) sont définies en passant leurs numéros de ligne ou de colonne. Par exemple, les lignes sont définies comme \ $1: \ $2 et les colonnes sont définies comme \ $A: \ $B.

{{< highlight csharp >}}

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
La classe **PageSetup** fournit également plusieurs autres méthodes pour définir des options générales d'impression comme suit :

- méthode **setPrintGridlines**, un paramètre booléen est passé à cette méthode qui définit s'il faut imprimer ou non les quadrillages
- méthode **setPrintHeadings**, un paramètre booléen est passé à cette méthode qui définit s'il faut imprimer ou non les en-têtes de lignes et de colonnes
- méthode **setBlackAndWhite**, un paramètre booléen est passé à cette méthode qui définit s'il faut imprimer la feuille de calcul en mode noir et blanc ou non
- méthode **setPrintComments**, définit s'il faut afficher les commentaires d'impression sur la feuille de calcul ou à la fin de la feuille de calcul
- méthode **setPrintDraft**, un paramètre booléen est passé à cette méthode qui définit s'il faut imprimer la feuille de calcul en qualité brouillon ou non
- méthode **setPrintErrors**, définit s'il faut imprimer les erreurs de cellule telles qu'affichées, vides, traits d'union ou N/A

Pour utiliser les méthodes **setPrintComments** et **setPrintErrors**, Aspose.Cells fournit également deux énumérations, PrintCommentsType & PrintErrorsType qui contiennent des valeurs prédéfinies à passer en paramètres pour définir les méthodes setPrintComments et setPrintErrors respectivement.

{{< highlight csharp >}}

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
La classe **PageSetup** fournit la méthode setOrder qui est utilisée pour ordonner l'impression de plusieurs pages de votre feuille de calcul. Il existe deux possibilités d'ordonner les pages comme suit :

En bas puis à droite, ainsi toutes les pages en bas seront imprimées avant d'imprimer les pages à droite
À droite puis en bas, ainsi toutes les pages seront imprimées de gauche à droite avant d'imprimer les pages en dessous
Aspose.Cells fournit une énumération, PrintOrderType qui contient tous les types d'ordre prédéfinis à assigner à la méthode setPageOrder.

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Setting the printing order of the pages to over then down

pageSetup.Order = PrintOrderType.OverThenDown;

{{< /highlight >}}
## **Télécharger le code source d'exemple**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Print%20Spreadsheet%20with%20Options%20%28Aspose.Cells%29.zip)
