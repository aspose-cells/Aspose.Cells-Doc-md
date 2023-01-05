---
title: Открывать текстовые файлы как рабочие книги
type: docs
weight: 180
url: /ru/net/open-text-files-as-workbooks/
---
Ниже приведен пример сравнительного кода для открытия текстового файла в качестве рабочих книг:
## **ВСТО**
{{< highlight "csharp" >}}

     this.Application.Workbooks.OpenText(@"OpenTextFilesAsWorkbooks.txt",

    missing, 3,

    Excel.XlTextParsingType.xlDelimited,

    Excel.XlTextQualifier.xlTextQualifierNone,

    missing, missing, missing, true, missing, missing, missing,

    missing, missing, missing, missing, missing, missing);

{{< /highlight >}}
## **Aspose.Cells**
{{< highlight "csharp" >}}

    private static string fileName = "OpenTextFilesAsWorkbooks.xlsx";

   private static string TextFile = "OpenTextFilesAsWorkbooks.txt";

   //loadoption to represent the option of load file

   LoadOptions loadOptions = new LoadOptions(LoadFormat.CSV);

   Workbook newWorkbook = new Workbook(TextFile, loadOptions);

   newWorkbook.Save(fileName);

{{< /highlight >}}
## **Скачать**
- [Гитхаб](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/OpenTextFilesAsWorkbooks.Aspose.Cells.zip)
