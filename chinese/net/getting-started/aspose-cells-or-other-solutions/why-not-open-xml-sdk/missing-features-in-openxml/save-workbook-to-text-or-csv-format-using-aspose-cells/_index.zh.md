---
title: 使用 Aspose.Cells 将工作簿保存为文本或 CSV 格式
type: docs
weight: 80
url: /zh/net/save-workbook-to-text-or-csv-format-using-aspose-cells/
---
{{% alert color="primary" %}} 

有时，您希望将包含多个工作表的工作簿转换或保存为文本格式。对于文本格式（例如 TXT、TabDelim、CSV 等），默认情况下 Microsoft Excel 和 Aspose.Cells 都只保存活动工作表的内容。

{{% /alert %}} 

下面的代码示例说明了如何将整个工作簿保存为文本格式。加载源工作簿，它可以是任何 Microsoft Excel 或 OpenOffice 电子表格文件（如 XLS、XLSX、XLSM、XLSB、ODS 等）和任意数量的工作表。

代码执行时，将工作簿中所有工作表的数据转换为TXT格式。

您可以修改同一示例以将文件保存为 CSV。默认情况下，TxtSaveOptions.Separator 为逗号，因此如果保存为 CSV 格式，请不要指定分隔符。

**C#**

{{< highlight "csharp" >}}

string FilePath = @"..\..\..\示例文件\";

string FileName = FilePath + "将工作簿保存为文本或 CSV 格式.xlsx";

string destFileName = FilePath + "将工作簿保存为文本或 CSV 格式.txt";

//加载源工作簿

工作簿 workbook = new Workbook(FileName);

//0字节数组

byte[]workbookData = new byte[0];

//文本保存选项。您可以使用任何类型的分隔符

TxtSaveOptions opts = new TxtSaveOptions();

opts.Separator = '\t';

//在工作簿数据数组中以文本格式复制每个工作表数据

对于 (int idx = 0; idx< workbook.Worksheets.Count; idx++)

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

File.WriteAllBytes(destFileName, workbookData);

{{< /highlight >}}
## **下载示例代码**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Save%20Workbook%20to%20Text%20or%20CSV%20Format)

## **下载运行示例**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
