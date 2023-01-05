---
title: Obtenir des informations sur la feuille de calcul
type: docs
weight: 50
url: /fr/net/get-worksheet-information/
---
## **OpenXML Excel**
{{< highlight "csharp" >}}

 chaîne FilePath = @"..\..\..\..\Sample Files\" ;

string FileName = FilePath + "Obtenir les informations de la feuille de calcul.xlsx" ;

GetSheetInfo(NomFichier);

Console.ReadKey();

}

public static void GetSheetInfo(string fileName)

{  // Ouvrir le fichier en lecture seule.  en utilisant (SpreadsheetDocument mySpreadsheet = SpreadsheetDocument.Open(fileName, false))  {  S sheets = mySpreadsheet.WorkbookPart.Workbook.Sheets; _x00 feuille, afficher les informations de la feuille.  foreach (E feuille dans feuilles)  {  foreach (A attr in sheet.GetAttributes())  {  Console.WriteLine("{0} : {1}" , att.localname, att.value); _ x000d_ }  }  }   {{< /highlight >}} ## ** Aspose.Cells ** _ x000d_ 07612348 Files\";  chaîne FileName = FilePath + "Obtenir les informations de la feuille de calcul.xlsx";  GetSheetInfo(FileName);  Console.ReadKey();  }

vide statique privé GetSheetInfo (chaîne fileName)

{  //Instanciation d'un objet Workbook  Workbook workbook = new Workbook(fileName);  //Parcourir toutes les feuilles du classeur  foreach (Worksheet Sheet in workbook.Worksheets)  { //x000d_ { Index de Sheet  Console.WriteLine("Sheet Name : {0}", Sheet.Name);  Console.WriteLine("Sheet Index : {0}", Sheet.Index);  //Parcourir tous les Properties  foreach (propriété personnalisée dans la feuille.CustomProperties)   {  console.writeline ("{0}: {1}", propriété.name, propriété.value); _ #x_x_x_x_x_x'x'xte **Télécharger un exemple de code** - [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/AsposeCellsVsOpenXMLv1.1) - [Sourceforge](https://sourceforge .net/projects/asposeopenxml/files/Aspose.Cells%20Vs%20OpenXML/Get%20worksheet%20information%20\(Aspose.Cells \).zip/download) - [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Get%20worksheet%20information%20\(Aspose.Cells\).zip)