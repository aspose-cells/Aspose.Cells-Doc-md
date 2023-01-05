---
title: Bir elektronik tablo belgesindeki tüm adlandırılmış aralıkların sözlüğünü alın
type: docs
weight: 120
url: /tr/net/retrieve-a-dictionary-of-all-named-ranges-in-a-spreadsheet-document/
---
## **OpenXML Excel'i aç**
{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\..\Sample Files\";

string FileName = FilePath + "Retrieve a dictionary of all named ranges.xlsx";

Dictionary<String, String> ranges = GetDefinedNames(FileName);

public static Dictionary<String, String> GetDefinedNames(String fileName)

{

    // Given a workbook name, return a dictionary of defined names.

    // The pairs include the range name and a string representing the range.

    var returnValue = new Dictionary<String, String>();

    // Open the spreadsheet document for read-only access.

    using (SpreadsheetDocument document =

        SpreadsheetDocument.Open(fileName, false))

    {

        // Retrieve a reference to the workbook part.

        var wbPart = document.WorkbookPart;

        // Retrieve a reference to the defined names collection.

        DefinedNames definedNames = wbPart.Workbook.DefinedNames;

        // If there are defined names, add them to the dictionary.

        if (definedNames != null)

        {

            foreach (DefinedName dn in definedNames)

                returnValue.Add(dn.Name.Value, dn.Text);

        }

    }

    return returnValue;

}

{{< /highlight >}}
## **Aspose.Cells**
{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\..\Sample Files\";

string FileName = FilePath + "Retrieve a dictionary of all named ranges.xlsx";

Dictionary<String, String> ranges = GetDefinedNames(FileName);

public static Dictionary<String, String> GetDefinedNames(String fileName)

{

    // Given a workbook name, return a dictionary of defined names.

    // The pairs include the range name and a string representing the range.

    var returnValue = new Dictionary<String, String>();



    // Open a SpreadsheetDocument based on a filepath.

    Workbook workbook = new Workbook(fileName);



    //Getting all named ranges

    Range[] range = workbook.Worksheets.GetNamedRanges();



    // If there are items in Ranges, add them to the dictionary.

    if (range != null)

    {

        foreach (Range rn in range)

            returnValue.Add(rn.Name, rn.Value.ToString());

    }

    return returnValue;

}

{{< /highlight >}}
## **Çalışan Kod Örneği İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/AsposeCellsVsOpenXMLv1.1)
## **Basit kod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/Aspose.Cells%20VS%20OpenXML/Retrieve%20a%20dictionary%20of%20all%20named%20ranges)
