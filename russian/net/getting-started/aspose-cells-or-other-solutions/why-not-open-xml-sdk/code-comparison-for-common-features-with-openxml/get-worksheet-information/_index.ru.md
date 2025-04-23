---
title: Получить информацию о листе
type: docs
weight: 50
url: /ru/net/get-worksheet-information/
---

## **OpenXML Excel**
{{< highlight csharp >}}

 string FilePath = @"..\..\..\..\Sample Files\";

string FileName = FilePath + "Get worksheet information.xlsx";

GetSheetInfo(FileName);

Console.ReadKey();

}

public static void GetSheetInfo(string fileName)

{

// Open file as read-only.

using (SpreadsheetDocument mySpreadsheet = SpreadsheetDocument.Open(fileName, false))

{

    S sheets = mySpreadsheet.WorkbookPart.Workbook.Sheets;

    // For each sheet, display the sheet information.

    foreach (E sheet in sheets)

    {

        foreach (A attr in sheet.GetAttributes())

        {

            Console.WriteLine("{0}: {1}", attr.LocalName, attr.Value);

        }

    }

}

{{< /highlight >}}
## **Aspose.Cells**
{{< highlight csharp >}}

 string FilePath = @"..\..\..\..\Sample Files\";

string FileName = FilePath + "Get worksheet information.xlsx";

GetSheetInfo(FileName);

Console.ReadKey();

}

private static void GetSheetInfo(string fileName)

{

//Instantiating a Workbook object

Workbook workbook = new Workbook(fileName);

//Loop through all Sheets in the workbook

foreach (Worksheet Sheet in workbook.Worksheets)

{

    //Get Name and Index of Sheet

    Console.WriteLine("Sheet Name: {0}", Sheet.Name);

    Console.WriteLine("Sheet Index: {0}", Sheet.Index);

    //Loop through all custom properties

    foreach (CustomProperty Property in Sheet.CustomProperties)

    {

        Console.WriteLine("{0}: {1}", Property.Name, Property.Value);

    }

}

{{< /highlight >}}
## **Загрузить образец кода**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/AsposeCellsVsOpenXMLv1.1)
- [Sourceforge](https://sourceforge.net/projects/asposeopenxml/files/Aspose.Cells%20Vs%20OpenXML/Get%20worksheet%20information%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Get%20worksheet%20information%20\(Aspose.Cells\).zip)
{{< app/cells/assistant language="csharp" >}}
