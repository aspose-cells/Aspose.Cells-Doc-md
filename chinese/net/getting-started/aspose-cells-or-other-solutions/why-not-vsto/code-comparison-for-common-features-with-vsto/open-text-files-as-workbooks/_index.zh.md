---
title: 打开文本文件作为工作簿
type: docs
weight: 180
url: /zh/net/open-text-files-as-workbooks/
---

以下是比较代码示例，用于将文本文件作为工作簿打开：
## **VSTO**
{{< highlight csharp >}}

     this.Application.Workbooks.OpenText(@"OpenTextFilesAsWorkbooks.txt",

    missing, 3,

    Excel.XlTextParsingType.xlDelimited,

    Excel.XlTextQualifier.xlTextQualifierNone,

    missing, missing, missing, true, missing, missing, missing,

    missing, missing, missing, missing, missing, missing);

{{< /highlight >}}
## **Aspose.Cells**
{{< highlight csharp >}}

    private static string fileName = "OpenTextFilesAsWorkbooks.xlsx";

   private static string TextFile = "OpenTextFilesAsWorkbooks.txt";

   //loadoption to represent the option of load file

   LoadOptions loadOptions = new LoadOptions(LoadFormat.CSV);

   Workbook newWorkbook = new Workbook(TextFile, loadOptions);

   newWorkbook.Save(fileName);

{{< /highlight >}}
##**下载**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/OpenTextFilesAsWorkbooks.Aspose.Cells.zip)
