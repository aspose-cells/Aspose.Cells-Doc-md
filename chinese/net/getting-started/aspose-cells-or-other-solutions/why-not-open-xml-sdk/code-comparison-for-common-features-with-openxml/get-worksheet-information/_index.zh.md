---
title: 获取工作表信息
type: docs
weight: 50
url: /zh/net/get-worksheet-information/
---
## **OpenXML Excel**
{{< highlight "csharp" >}}

string FilePath = @"..\..\..\..\示例文件\";

string FileName = FilePath + "获取工作表信息.xlsx";

GetSheetInfo(文件名);

控制台.ReadKey();

}

公共静态无效 GetSheetInfo（字符串文件名）

{  // 以只读方式打开文件。  使用 (SpreadsheetDocument mySpreadsheet = SpreadsheetDocument.Open(fileName, false))  {  S sheets = mySpreadsheet.WorkbookPart.Workbook.Sheets;  For each sheet,显示sheet信息.  foreach(E sheet in sheets)  {  foreach(A attr in sheet.GetAttributes())  {  Console.WriteLine("{0}: {1}" ，atter.localname，attr.value）; _ x000d_} _} __}  {{< /highlight >}}_x0003481 ## 000 __00 _000 _000 _10.11 pramest y.andy x.11 pr Files\";  string FileName = FilePath + "获取工作表信息.xlsx";  GetSheetInfo(FileName);  Console.ReadKey();  }

私有静态无效 GetSheetInfo（字符串文件名）

{  //实例化一个Workbook对象  Workbook workbook = new Workbook(fileName);  //循环遍历workbook中的所有Sheet  foreach(Worksheet Sheet in workbook.Worksheets)  name //Get0d {  Index of Sheet  Console.WriteLine("Sheet Name: {0}", Sheet.Name);  Console.WriteLine("Sheet Index: {0}", Sheet.Index);  //遍历所有自定义properties foreach（sheet.customproperties中的customProperty属性）_ {_x000d console.writeline（“ {0}）（0}：{1}：{1} **下载示例代码** - [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/AsposeCellsVsOpenXMLv1.1) - [Sourceforge](https://sourceforge .net/projects/asposeopenxml/files/Aspose.Cells%20Vs%20OpenXML/Get%20worksheet%20information%20\(Aspose.Cells \).zip/download) - [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Get%20worksheet%20information%20\(Aspose.Cells\).zip)