+++
title = "Open Text Files as Workbooks" 
description = "" 
weight = 16806 
+++

Aspose.Cells for .NET : Open Text Files as Workbooks  

# Aspose.Cells for .NET : Open Text Files as Workbooks


Below are comparison code example for opening textfile as Workbooks:

#### VSTO

{{< code lang="cs" >}}
    this.Application.Workbooks.OpenText(@"OpenTextFilesAsWorkbooks.txt",
    missing, 3,
    Excel.XlTextParsingType.xlDelimited,
    Excel.XlTextQualifier.xlTextQualifierNone,
    missing, missing, missing, true, missing, missing, missing,
    missing, missing, missing, missing, missing, missing);
{{< /code >}}

#### Aspose.Cells

{{< code lang="cs" >}}
   private static string fileName = "OpenTextFilesAsWorkbooks.xlsx";
   private static string TextFile = "OpenTextFilesAsWorkbooks.txt";
   //loadoption to represent the option of load file
   LoadOptions loadOptions = new LoadOptions(LoadFormat.CSV);
   Workbook newWorkbook = new Workbook(TextFile, loadOptions);
   newWorkbook.Save(fileName);
{{< /code >}}

##### Download

*   [CodePlex](https://asposevsto.codeplex.com/downloads/get/1459767)
*   [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/OpenTextFilesAsWorkbooks.Aspose.Cells.zip)

