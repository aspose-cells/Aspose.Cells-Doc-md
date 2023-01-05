---
title: Informationen zum Arbeitsblatt erhalten
type: docs
weight: 50
url: /de/net/get-worksheet-information/
---
## **OpenXML-Excel**
{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\..\Beispieldateien\";

string FileName = FilePath + "Get worksheet information.xlsx";

GetSheetInfo(Dateiname);

Console.ReadKey();

}

public static void GetSheetInfo(string fileName)

{  // Datei schreibgeschützt öffnen.  using (SpreadsheetDocument mySpreadsheet = SpreadsheetDocument.Open(fileName, false))  {  Ssheets = mySpreadsheet.WorkbookPart.Workbook.Sheets; _x0 each0.0 // Blatt, zeigt die Blattinformationen an.  foreach (E Blatt in Blättern)  {  foreach (A attr in Blatt.GetAttributes())  {  Console.WriteLine("{0}: {1}" , attr.LocalName, attr.Value); _ x000d_ }  }  } x000d_ {{< /highlight >}} # # # # # # x000dx000d_ x000d_ @| Files\";  string FileName = FilePath + "Arbeitsblattinformationen abrufen.xlsx";  GetSheetInfo(FileName);  Console.ReadKey();  }

private statische void GetSheetInfo(string fileName)

{  //Instanziieren eines Arbeitsmappenobjekts  Arbeitsmappe workbook = new Workbook(fileName);  //Alle Blätter in der Arbeitsmappe durchlaufen  foreach (Worksheet Sheet in workbook.Worksheets)  {_x0 Name und //.00d_ {_x0 Index von Sheet  Console.WriteLine("Blattname: {0}", Sheet.Name);  Console.WriteLine("Blattindex: {0}", Sheet.Index);  //Durchlaufe alle benutzerdefinierten Eigenschaften  foreach (CustomProperty -Eigenschaft in Blatt **Beispielcode herunterladen** - [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/AsposeCellsVsOpenXMLv1.1) - [Sourceforge](https://sourceforge .net/projects/asposeopenxml/files/Aspose.Cells%20Vs%20OpenXML/Get%20worksheet%20information%20\(Aspose.Cells \).zip/download) - [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Get%20worksheet%20information%20\(Aspose.Cells\).zip)