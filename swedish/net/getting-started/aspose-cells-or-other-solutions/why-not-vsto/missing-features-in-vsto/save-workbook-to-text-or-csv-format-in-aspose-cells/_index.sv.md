---
title: Spara arbetsbok i text eller CSV format i Aspose.Cells
type: docs
weight: 110
url: /sv/net/save-workbook-to-text-or-csv-format-in-aspose-cells/
---

{{% alert color="primary" %}} 

Ibland vill du konvertera eller spara en arbetsbok med flera kalkylblad i textformat. För textformat (till exempel TXT, TabDelim, CSV etc.) sparar både Microsoft Excel och Aspose.Cells innehållet i endast det aktiva kalkylbladet som standard.

{{% /alert %}} 

Följande kodexempel förklarar hur du sparar en hel arbetsbok i textformat. Ladda den källarbetsbok som kan vara vilken Microsoft Excel- eller OpenOffice-kalkylarksfil som helst (t.ex. XLS, XLSX, XLSM, XLSB, ODS osv.) med vilket antal arbetsblad som helst.

När koden körs konverterar den data från alla kalkylblad i arbetsboken till TXT-format.

Du kan ändra samma exempel för att spara din fil till CSV. Som standard är TxtSaveOptions.Separator kommatecken, så ange inte ett avgränsare om du sparar i CSV-format.

**C#**

{{< highlight csharp >}}

 string filePath = "source.xlsx";

//Load your source workbook

Workbook workbook = new Workbook(filePath);

//0-byte array

byte[] workbookData = new byte[0];

//Text save options. You can use any type of separator

TxtSaveOptions opts = new TxtSaveOptions();

opts.Separator = '\t';

//Copy each worksheet data in text format inside workbook data array

for (int idx = 0; idx < workbook.Worksheets.Count; idx++)

{

    //Save the active worksheet into text format

    MemoryStream ms = new MemoryStream();

    workbook.Worksheets.ActiveSheetIndex = idx;

    workbook.Save(ms, opts);

    //Save the worksheet data into sheet data array

    ms.Position = 0;

    byte[] sheetData = ms.ToArray();

    //Combine this worksheet data into workbook data array

    byte[] combinedArray = new byte[workbookData.Length + sheetData.Length];

    Array.Copy(workbookData, 0, combinedArray, 0, workbookData.Length);

    Array.Copy(sheetData, 0, combinedArray, workbookData.Length, sheetData.Length);

    workbookData = combinedArray;

}

//Save entire workbook data into file

File.WriteAllBytes(filePath + ".out.txt", workbookData);


{{< /highlight >}}
## **Ladda ned körbar kod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Save%20Workbook%20to%20Text%20or%20CSV%20Format)
## **Ladda ned provkoden**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
{{< app/cells/assistant language="csharp" >}}
