---
title: Metin Dosyalarını Çalışma Kitabı Olarak Açma
type: docs
weight: 180
url: /tr/net/open-text-files-as-workbooks/
---

Aşağıdaki, metin dosyasını çalışma kitabı olarak açma için karşılaştırmalı kod örneğidir:
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
##**İndir**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/OpenTextFilesAsWorkbooks.Aspose.Cells.zip)
{{< app/cells/assistant language="csharp" >}}
