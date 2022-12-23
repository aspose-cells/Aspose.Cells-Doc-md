---
title: Ottieni informazioni sul foglio di lavoro
type: docs
weight: 50
url: /it/net/get-worksheet-information/
---
## **Excel OpenXML**
{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\..\File di esempio\";

string FileName = FilePath + "Ottieni informazioni sul foglio di lavoro.xlsx";

GetFoglioInfo(NomeFile);

Console.ReadKey();

}

public static void GetSheetInfo(string fileName)

{  // Apri file in sola lettura.  using (SpreadsheetDocument mySpreadsheet = SpreadsheetDocument.Open(fileName, false))  {  S sheet = mySpreadsheet.WorkbookPart.Workbook.Sheets; _/00 For each sheet, visualizza le informazioni sul foglio.  foreach (E sheet in sheets)  {  foreach (A attr in sheet.GetAttributes())  {  Console.WriteLine("{0}: {1}" , attr.LocalName, attr.Value);  }  }  }  {{< /highlight >}} ## **Aspose.Cells** {{< highlight csharp >}}  string FilePath = @"..\..\..\..\Sample Files\";  string FileName = FilePath + "Get worksheet information.xlsx";  GetSheetInfo(FileName);  Console.ReadKey();  }

private static void GetSheetInfo(string fileName)

{  //Creazione di un'istanza di un oggetto cartella di lavoro  Workbook workbook = new Workbook(fileName);  //Scorri tutti i fogli nella cartella di lavoro  foreach (foglio del foglio di lavoro nella cartella di lavoro.Fogli di lavoro)  {__x0 con nome00 e Index of Sheet  Console.WriteLine("Sheet Name: {0}", Sheet.Name);  Console.WriteLine("Sheet Index: {0}", Sheet.Index);  //Ripeti tutte le personalizzazioni Properties  foreach (proprietà CustomProperty in foglio.CustomProperties)   {  console.writeline ({0}: {1} ", Property.name, Property.Value); _ _1000 **Scarica il codice di esempio** - [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/AsposeCellsVsOpenXMLv1.1) - [Sourceforge](https://sourceforge .net/projects/asposeopenxml/files/Aspose.Cells%20Vs%20OpenXML/Get%20worksheet%20information%20\(Aspose.Cells \).zip/download) - [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Get%20worksheet%20information%20\(Aspose.Cells\).zip)