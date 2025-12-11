---
title: Open Text Files as Workbooks
type: docs
weight: 180
url: /net/open-text-files-as-workbooks/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Below are comparison code examples for opening a text file as workbooks:

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

    // LoadOptions to represent the options for loading the file
    LoadOptions loadOptions = new LoadOptions(LoadFormat.CSV);

    Workbook newWorkbook = new Workbook(TextFile, loadOptions);

    newWorkbook.Save(fileName);

{{< /highlight >}}

## **Download**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/OpenTextFilesAsWorkbooks.Aspose.Cells.zip)

{{< app/cells/assistant language="csharp" >}}
