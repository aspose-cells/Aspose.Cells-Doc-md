---
title: Открыть документ таблицы только для чтения
type: docs
weight: 100
url: /ru/net/open-a-spreadsheet-document-for-read-only-access/
---

## **OpenXML Excel**
{{< highlight csharp >}}

 string FilePath = @"..\..\..\..\Sample Files\";

string FileName = FilePath + "Open a spreadsheet document for read-only access.xlsx";

OpenSpreadsheetDocumentReadonly(FileName);

}

public static void OpenSpreadsheetDocumentReadonly(string filepath)

{

// Open a SpreadsheetDocument based on a filepath.

using (SpreadsheetDocument spreadsheetDocument = SpreadsheetDocument.Open(filepath, false))

{

    // Attempt to add a new WorksheetPart.

    // The call to AddNewPart generates an exception because the file is read-only.

    WorksheetPart newWorksheetPart = spreadsheetDocument.WorkbookPart.AddNewPart<WorksheetPart>();

    // The rest of the code will not be called.

}

}

{{< /highlight >}}
## **Aspose.Cells**
{{< highlight csharp >}}



string FilePath = @"..\..\..\..\Sample Files\";

string FileName = FilePath + "Open a spreadsheet document for read-only access.xlsx";

OpenSpreadsheetDocumentReadonly(FileName);

public static void OpenSpreadsheetDocumentReadonly(string filepath)

{

  // Open a SpreadsheetDocument based on a filepath.

  Workbook workbook = new Workbook(filepath);

}


{{< /highlight >}}
## **Скачать пример выполнения кода**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/AsposeCellsVsOpenXMLv1.1)
## **Образец кода**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/Aspose.Cells%20VS%20OpenXML/Open%20read-only%20access)
{{< app/cells/assistant language="csharp" >}}
