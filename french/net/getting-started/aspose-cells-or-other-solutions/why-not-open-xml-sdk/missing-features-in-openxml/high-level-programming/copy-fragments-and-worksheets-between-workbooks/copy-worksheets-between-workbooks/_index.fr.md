---
title: Copier des feuilles de calcul entre des classeurs
type: docs
weight: 10
url: /fr/net/copy-worksheets-between-workbooks/
---
Aspose.Cells fournit une méthode, Aspose.Cells.Worksheet.Copy(), utilisée pour copier les données et la mise en forme d'une feuille de calcul source vers une autre feuille de calcul dans ou entre des classeurs. La méthode prend l'objet feuille de calcul source comme paramètre.

L'exemple suivant montre comment copier une feuille de calcul d'un classeur vers un autre classeur.

{{< highlight "csharp" >}}

chaîne FilePath = @"..\..\..\Sample Files\" ;

string FileName = FilePath + "Copier la feuille entre Workbook.xlsx" ;

//Créer un nouveau classeur.

Classeur excelWorkbook0 = nouveau classeur();

// Récupère la première feuille de calcul du livre.

Feuille de calcul ws0 = excelWorkbook0.Worksheets[0] ;

//Mettez des données dans les lignes d'en-tête (A1:A4)

 pour (int je = 0; je< 5; i++)

{

    ws0.Cells[i, 0].PutValue(string.Format("Header Row {0}", i));

}

//Put some detail data (A5:A999)

for (int i = 5; i < 1000; i++)

{

    ws0.Cells[i, 0].PutValue(string.Format("Detail Row {0}", i));

}

//Define a pagesetup object based on the first worksheet.

PageSetup pagesetup = ws0.PageSetup;

//The first five rows are repeated in each page...

//It can be seen in print preview.

pagesetup.PrintTitleRows = "$1:$5";

//Create another Workbook.

Workbook excelWorkbook1 = new Workbook();

//Get the first worksheet in the book.

Worksheet ws1 = excelWorkbook1.Worksheets[0];

//Name the worksheet.

ws1.Name = "MySheet";

//Copy data from the first worksheet of the first workbook into the

//first worksheet of the second workbook.

ws1.Copy(ws0);

//Save the excel file.

excelWorkbook1.Save(FileName);

{{< /highlight >}}
## **Télécharger l'exemple de code**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Copy%20between%20Workbooks%20%28Aspose.Cells%29.zip)

L'exemple suivant montre comment copier une feuille de calcul d'un classeur vers un autre classeur.

{{< highlight "csharp" >}}

 //Créer un nouveau classeur.

Classeur excelWorkbook0 = nouveau classeur();

// Récupère la première feuille de calcul du livre.

Feuille de calcul ws0 = excelWorkbook0.Worksheets[0] ;

//Mettez des données dans les lignes d'en-tête (A1:A4)

 pour (int je = 0; je< 5; i++)

{

	ws0.Cells[i, 0].PutValue(string.Format("Header Row {0}", i));

}

//Put some detail data (A5:A999)

for (int i = 5; i < 1000; i++)

{

	ws0.Cells[i, 0].PutValue(string.Format("Detail Row {0}", i));

}

//Define a pagesetup object based on the first worksheet.

PageSetup pagesetup = ws0.PageSetup;

//The first five rows are repeated in each page...

//It can be seen in print preview.

pagesetup.PrintTitleRows = "$1:$5";

//Create another Workbook.

Workbook excelWorkbook1 = new Workbook();

//Get the first worksheet in the book.

Worksheet ws1 = excelWorkbook1.Worksheets[0];

//Name the worksheet.

ws1.Name = "MySheet";

//Copy data from the first worksheet of the first workbook into the

//first worksheet of the second workbook.

ws1.Copy(ws0);

//Save the excel file.

excelWorkbook1.Save("copyworksheet.xls");


{{< /highlight >}}
## **Télécharger l'exemple de code**
- [GithubGenericName](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Copy%20Sheet%20between%20Workbook%20%28Aspose.Cells%29.zip)
