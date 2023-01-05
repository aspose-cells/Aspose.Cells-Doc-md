---
title: ワークシート情報を取得する
type: docs
weight: 50
url: /ja/net/get-worksheet-information/
---
## **OpenXML エクセル**
{{< highlight "csharp" >}}

string FilePath = @"..\..\..\..\Sample Files\";

string FileName = FilePath + "ワークシート情報を取得.xlsx";

GetSheetInfo(ファイル名);

Console.ReadKey();

}

public static void GetSheetInfo(文字列ファイル名)

{  // ファイルを読み取り専用で開きます。シート、シート情報を表示する、attr.localname、attr.value）; _ x000d_ }  }  }   {{< /highlight >}} ## ** 07611481__x000 .. Files\";  string FileName = FilePath + "ワークシート情報を取得.xlsx";  GetSheetInfo(ファイル名);  Console.ReadKey();  }

private static void GetSheetInfo(string fileName)

{  //Workbook オブジェクトのインスタンス化  Workbook workbook = new Workbook(fileName);  //workbook 内のすべてのシートをループする  foreach (workbook.Worksheets 内の Worksheet Sheet)0  //Get _x00d_0 Index of Sheet  Console.WriteLine("Sheet Name: {0}", Sheet.Name);  Console.WriteLine("Sheet Index: {0}", Sheet.Index);  //すべてのカスタムをループProperties  foreach（sheet.customporteriesのカスタムプロパティプロパティ）  {  console.writeLine（ "{0}：{1}"、property.name）; **サンプル コードのダウンロード** - [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/AsposeCellsVsOpenXMLv1.1) - [Sourceforge](https://sourceforge .net/projects/asposeopenxml/files/Aspose.Cells%20Vs%20OpenXML/Get%20worksheet%20information%20\(Aspose.Cells \).zip/download) - [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Get%20worksheet%20information%20\(Aspose.Cells\).zip)