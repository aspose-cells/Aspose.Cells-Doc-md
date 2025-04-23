---
title: Infoga ett nytt kalkylblad
type: docs
weight: 70
url: /sv/net/insert-a-new-worksheet/
---

## **OpenXML Excel**
{{< highlight csharp >}}

 string FilePath = @"..\..\..\..\Sample Files\";

string FileName = FilePath + "Insert a new worksheet.xlsx";

InsertWorksheet(FileName);

}

private static void InsertWorksheet(string docName)

{

// Open the document for editing.

using (SpreadsheetDocument spreadSheet = SpreadsheetDocument.Open(docName, true))

{

    // Add a blank WorksheetPart.

    WorksheetPart newWorksheetPart = spreadSheet.WorkbookPart.AddNewPart<WorksheetPart>();

    newWorksheetPart.Worksheet = new Worksheet(new SheetData());

    Sheets sheets = spreadSheet.WorkbookPart.Workbook.GetFirstChild<Sheets>();

    string relationshipId = spreadSheet.WorkbookPart.GetIdOfPart(newWorksheetPart);

    // Get a unique ID for the new worksheet.

    uint sheetId = 1;

    if (sheets.Elements<Sheet>().Count() > 0)

    {

        sheetId = sheets.Elements<Sheet>().Select(s => s.SheetId.Value).Max() + 1;

    }

    // Give the new worksheet a name.

    string sheetName = "Sheet" + sheetId;

    // Append the new worksheet and associate it with the workbook.

    Sheet sheet = new Sheet() { Id = relationshipId, SheetId = sheetId, Name = sheetName };

    sheets.Append(sheet);

}

}

{{< /highlight >}}
## **Aspose.Cells**
{{< highlight csharp >}}



string FilePath = @"..\..\..\..\Sample Files\";

string FileName = FilePath + "Insert a new worksheet.xlsx";

InsertWorksheet(FileName);

private static void InsertWorksheet(string docName)

{

  //Instantiating a Workbook object

  Workbook workbook = new Workbook(docName);

  //Adding a new worksheet to the Excel object

  int SheetIndex = workbook.Worksheets.Add();

  //Saving the Excel file

  workbook.Save(docName);

}


{{< /highlight >}}
## **Ladda ned provkoden**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/AsposeCellsVsOpenXMLv1.1)
- [Sourceforge](https://sourceforge.net/projects/asposeopenxml/files/Aspose.Cells%20Vs%20OpenXML/Insert%20a%20new%20worksheet%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Insert%20a%20new%20worksheet%20\(Aspose.Cells\).zip)
{{< app/cells/assistant language="csharp" >}}
