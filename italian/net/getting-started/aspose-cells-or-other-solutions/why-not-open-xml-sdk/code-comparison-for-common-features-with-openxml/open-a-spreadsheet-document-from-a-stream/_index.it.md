---
title: Apri un foglio di lavoro da uno stream
type: docs
weight: 110
url: /it/net/open-a-spreadsheet-document-from-a-stream/
---
## **Excel OpenXML**
{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\..\Sample Files\";

string FileName = FilePath + "Open a spreadsheet document from a stream.xlsx";

Stream stream = File.Open(FileName, FileMode.Open);

OpenAndAddToSpreadsheetStream(stream);

stream.Close();

public static void OpenAndAddToSpreadsheetStream(Stream stream)

{

    // Open a SpreadsheetDocument based on a stream.

    SpreadsheetDocument spreadsheetDocument =

        SpreadsheetDocument.Open(stream, true);

    // Add a new worksheet.

    WorksheetPart newWorksheetPart = spreadsheetDocument.WorkbookPart.AddNewPart<WorksheetPart>();

    newWorksheetPart.Worksheet = new Worksheet(new SheetData());

    newWorksheetPart.Worksheet.Save();

    Sheets sheets = spreadsheetDocument.WorkbookPart.Workbook.GetFirstChild<Sheets>();

    string relationshipId = spreadsheetDocument.WorkbookPart.GetIdOfPart(newWorksheetPart);

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

    spreadsheetDocument.WorkbookPart.Workbook.Save();

    // Close the document handle.

    spreadsheetDocument.Close();

    // Caller must close the stream.

}

{{< /highlight >}}
## **Aspose.Cells**
{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\..\Sample Files\";

string FileName = FilePath + "Open a spreadsheet document from a stream.xlsx";

Stream stream = File.Open(FileName, FileMode.Open);

OpenAndAddToSpreadsheetStream(stream);

stream.Close();

public static void OpenAndAddToSpreadsheetStream(Stream stream)

{

    //Creating a Workbook object, open the file from a Stream object

    //that contains the content of file and it should support seeking

    Workbook workbook = new Workbook(stream);

}

{{< /highlight >}}
## **Scarica l'esempio di codice in esecuzione**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/AsposeCellsVsOpenXMLv1.1)
## **Codice di esempio**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/Aspose.Cells%20VS%20OpenXML/Open%20from%20a%20stream/OpenXML%20Spreadshhets)
