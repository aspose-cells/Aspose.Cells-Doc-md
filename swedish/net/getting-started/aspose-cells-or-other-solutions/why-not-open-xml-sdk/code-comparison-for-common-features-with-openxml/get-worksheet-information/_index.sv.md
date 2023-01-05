---
title: Få information om arbetsblad
type: docs
weight: 50
url: /sv/net/get-worksheet-information/
---
## **OpenXML Excel**
{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\..\Sample Files\";

string FileName = FilePath + "Hämta kalkylbladsinformation.xlsx";

GetSheetInfo(Filnamn);

Console.ReadKey();

}

offentligt statiskt tomrum GetSheetInfo(sträng filnamn)

{  // Öppna fil som skrivskyddad.  med (SpreadSheetDocument MySpreadSheet = SpreadsheetDocument.open (FileName, False) _ x000d_  { _x000d ark, visa arkinformationen.  foreach (E ark i ark)  {  foreach (A attr in sheet.GetAttributes())_x0000d_ _0d" _0d" _0d" _0d" _0d" _0d" _xd" _0d" _0d" _xd" _xd" _xd" , attr.LocalName, attr.Value);  }  }  }  {{< /highlight >}} ## **Aspose.Cells** {{< highlight csharp >}}  string FilePath = @"..\..\..\..\Sample Files\";  string FileName = FilePath + "Hämta kalkylbladsinformation.xlsx";  GetSheetInfo(FileName);  Console.ReadKey();_x0000d__x00d

privat statisk tomrum GetSheetInfo(sträng filnamn)

{  // Instantiera ett arbetsbok Object  Workbook Workbook = new Workbook (filnamn); _ x000d_  // loop genom alla ark i arbetsboken  foreach (arbetshus i arbetsboken. Index av Sheet  Console.WriteLine("Sheet Name: {0}", Sheet.Name);  Console.WriteLine("Sheet Index: {0}", Sheet.Index); genom alla anpassade_ /x00d_ egenskaper  foreach (anpassad egendom i ark. **Ladda ner provkod** - [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/AsposeCellsVsOpenXMLv1.1)_x0000d_x0000d [https://Sourceforge_ .net/projects/asposeopenxml/files/Aspose.Cells%20Vs%20OpenXML/Get%20worksheet%20information%20\(Aspose.Cells \).zip/download) - [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Get%20worksheet%20information%20\(Aspose.Cells\).zip)