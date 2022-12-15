---
title: Çalışma sayfası bilgilerini al
type: docs
weight: 50
url: /tr/net/get-worksheet-information/
---
## **OpenXML Excel'i aç**
{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\..\Örnek Dosyalar\";

string FileName = FilePath + "Çalışma sayfası bilgilerini al.xlsx";

GetSheetInfo(DosyaAdı);

Console.ReadKey();

}

genel statik geçersiz GetSheetInfo(dize dosyaAdı)

{  // (SpreadsheetDocument mySpreadsheet = SpreadsheetDocument.Open(fileName, false))  {  S Sheets = mySpreadsheet.WorkbookPart.Workbook.Sheets;  kullanarak dosyayı salt okunur olarak açın. sayfa, sayfa bilgilerini görüntüleyin.  foreach (sayfalarda E sayfası)  {  foreach (Sayfada bir özellik.GetAttributes())  {  Console.WriteLine("{0}: {1}") , attr.LocalName, attr.Value);  }  }  }  {{< /highlight >}} ## **Aspose.Cells** {{< highlight csharp >}}  string FilePath = @"..\..\..\..\Sample Files\";  string FileName = FilePath + "Çalışma sayfası bilgilerini al.xlsx";  GetSheetInfo(FileName);  Console.ReadKey();  }

özel statik geçersiz GetSheetInfo(dize dosyaAdı)

{  //Bir Çalışma Kitabı Oluşturma object  Workbook workbook = new Workbook(fileName);  //workbook'taki tüm Sayfalarda döngü yapın  foreach (workbook.Worksheets'teki Worksheet Sheet) _x000d /0t0 {0 Sheet  Index. Properties  foreach (sheet.customproperties içindeki CustomProperty özelliği)  _X000d_ {  console.writeline ("{0}: {1}", pruitt.name, property.value); **Örnek Kodu İndirin** - [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/AsposeCellsVsOpenXMLv1.1) - [Sourceforge](https://sourceforge .net/projects/asposeopenxml/files/Aspose.Cells%20Vs%20OpenXML/Get%20worksheet%20information%20\(Aspose.Cells \).zip/download) - [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Get%20worksheet%20information%20\(Aspose.Cells\).zip)