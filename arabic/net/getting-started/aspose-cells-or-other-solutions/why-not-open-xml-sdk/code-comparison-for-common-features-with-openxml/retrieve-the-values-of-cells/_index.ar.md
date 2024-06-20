---
title: استرجاع قيم الخلايا
type: docs
weight: 130
url: /ar/net/retrieve-the-values-of-cells/
---

## **OpenXML SDK**
{{< highlight csharp >}}

 string FilePath = @"..\..\..\..\Sample Files\";

string FileName = FilePath + "Retrieve the values of cells.xlsx";

// Retrieve the value in cell A1.

string value = GetCellValue(FileName, "Sheet1", "A1");

Console.WriteLine(value);

// Retrieve the value of a cell, given a file name, sheet name, 

// and address name.

public static string GetCellValue(string fileName,

string sheetName,

string addressName)

{

string value = null;

// Open the spreadsheet document for read-only access.

using (SpreadsheetDocument document =

    SpreadsheetDocument.Open(fileName, false))

{

    // Retrieve a reference to the workbook part.

    WorkbookPart wbPart = document.WorkbookPart;

    // Find the sheet with the supplied name, and then use that 

    // Sheet object to retrieve a reference to the first worksheet.

    Sheet theSheet = wbPart.Workbook.Descendants<Sheet>().

      Where(s => s.Name == sheetName).FirstOrDefault();

    // Throw an exception if there is no sheet.

    if (theSheet == null)

    {

        throw new ArgumentException("sheetName");

    }

    // Retrieve a reference to the worksheet part.

    WorksheetPart wsPart =

        (WorksheetPart)(wbPart.GetPartById(theSheet.Id));

    // Use its Worksheet property to get a reference to the cell 

    // whose address matches the address you supplied.

    Cell theCell = wsPart.Worksheet.Descendants<Cell>().

      Where(c => c.CellReference == addressName).FirstOrDefault();

    // If the cell does not exist, return an empty string.

    if (theCell != null)

    {

        value = theCell.InnerText;

        // If the cell represents an integer number, you are done. 

        // For dates, this code returns the serialized value that 

        // represents the date. The code handles strings and 

        // Booleans individually. For shared strings, the code 

        // looks up the corresponding value in the shared string 

        // table. For Booleans, the code converts the value into 

        // the words TRUE or FALSE.

        if (theCell.DataType != null)

        {

            switch (theCell.DataType.Value)

            {

                case CellValues.SharedString:

                    // For shared strings, look up the value in the

                    // shared strings table.

                    var stringTable =

                        wbPart.GetPartsOfType<SharedStringTablePart>()

                        .FirstOrDefault();

                    // If the shared string table is missing, something 

                    // is wrong. Return the index that is in

                    // the cell. Otherwise, look up the correct text in 

                    // the table.

                    if (stringTable != null)

                    {

                        value =

                            stringTable.SharedStringTable

                            .ElementAt(int.Parse(value)).InnerText;

                    }

                    break;

                case CellValues.Boolean:

                    switch (value)

                    {

                        case "0":

                            value = "FALSE";

                            break;

                        default:

                            value = "TRUE";

                            break;

                    }

                    break;

            }

        }

    }

}

return value;

}

{{< /highlight >}}
## **Aspose.Cells**
{{< highlight csharp >}}

 string FilePath = @"..\..\..\..\Sample Files\";

string FileName = FilePath + "Retrieve the values of cells.xlsx";

// Retrieve the value in cell A1.

string value = GetCellValue(FileName, "Sheet1", "A1");

Console.WriteLine(value);

Console.ReadKey();



// Retrieve the value of a cell, given a file name, sheet name, 

// and address name.

public static string GetCellValue(string fileName,

    string sheetName,

    string addressName)

{

    //Instantiating a Workbook object

    Workbook workbook = new Workbook(fileName);

    //Obtaining the reference of the Active worksheet

    Worksheet worksheet = workbook.Worksheets.GetSheetByCodeName(sheetName);

    //retrieve value from cell

    string returnValue = worksheet.Cells[addressName].Value.ToString();

    return returnValue;

}

{{< /highlight >}}
## **تحميل رمز عينة**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/AsposeCellsVsOpenXMLv1.1)
- [Sourceforge](https://sourceforge.net/projects/asposeopenxml/files/Aspose.Cells%20Vs%20OpenXML/Retrieve%20the%20values%20of%20cells%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Retrieve%20the%20values%20of%20cells%20\(Aspose.Cells\).zip)
