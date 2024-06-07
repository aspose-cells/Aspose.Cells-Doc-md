---
title: 在Aspose.Cells中将工作簿保存为文本或CSV格式
type: docs
weight: 110
url: /zh/net/save-workbook-to-text-or-csv-format-in-aspose-cells/
---

{{% alert color="primary" %}} 

有时，您希望将一个包含多个工作表的工作簿转换或保存为文本格式。对于文本格式（例如TXT、TabDelim、CSV等），默认情况下Microsoft Excel和Aspose.Cells只保存活动工作表的内容。

{{% /alert %}} 

以下代码示例说明如何将整个工作簿保存为文本格式。加载源工作簿，可以是任何包含任意工作表数量的Microsoft Excel或OpenOffice电子表格文件（如XLS、XLSX、XLSM、XLSB、ODS等）。

当代码执行时，它将工作簿中所有工作表的数据转换为TXT格式。

您可以修改相同的示例，将文件保存为CSV格式。默认情况下，TxtSaveOptions.Separator是逗号，因此在保存为CSV格式时不要指定分隔符。

**C#**

{{< highlight csharp >}}

 string filePath = "source.xlsx";

//Load your source workbook

Workbook workbook = new Workbook(filePath);

//0-byte array

byte[] workbookData = new byte[0];

//Text save options. You can use any type of separator

TxtSaveOptions opts = new TxtSaveOptions();

opts.Separator = '\t';

//Copy each worksheet data in text format inside workbook data array

for (int idx = 0; idx < workbook.Worksheets.Count; idx++)

{

    //Save the active worksheet into text format

    MemoryStream ms = new MemoryStream();

    workbook.Worksheets.ActiveSheetIndex = idx;

    workbook.Save(ms, opts);

    //Save the worksheet data into sheet data array

    ms.Position = 0;

    byte[] sheetData = ms.ToArray();

    //Combine this worksheet data into workbook data array

    byte[] combinedArray = new byte[workbookData.Length + sheetData.Length];

    Array.Copy(workbookData, 0, combinedArray, 0, workbookData.Length);

    Array.Copy(sheetData, 0, combinedArray, workbookData.Length, sheetData.Length);

    workbookData = combinedArray;

}

//Save entire workbook data into file

File.WriteAllBytes(filePath + ".out.txt", workbookData);


{{< /highlight >}}
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Save%20Workbook%20to%20Text%20or%20CSV%20Format)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
