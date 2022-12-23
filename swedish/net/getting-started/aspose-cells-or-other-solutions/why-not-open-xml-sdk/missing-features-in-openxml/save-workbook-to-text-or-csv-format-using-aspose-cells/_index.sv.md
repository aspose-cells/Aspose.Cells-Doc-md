---
title: Spara arbetsbok till text eller CSV Formatera med Aspose.Cells
type: docs
weight: 80
url: /sv/net/save-workbook-to-text-or-csv-format-using-aspose-cells/
---
{{% alert color="primary" %}} 

Ibland vill du konvertera eller spara en arbetsbok med flera kalkylblad till textformat. För textformat (till exempel TXT, TabDelim, CSV etc.) sparar både Microsoft Excel och Aspose.Cells endast innehållet i det aktiva kalkylbladet som standard.

{{% /alert %}} 

Följande kodexempel förklarar hur man sparar en hel arbetsbok i textformat. Ladda källarbetsboken som kan vara valfri Microsoft Excel- eller OpenOffice-kalkylarksfil (såsom XLS, XLSX, XLSM, XLSB, ODS och så vidare) med valfritt antal kalkylblad.

När koden exekveras konverterar den data från alla ark i arbetsboken till formatet TXT.

Du kan ändra samma exempel för att spara din fil till CSV. Som standard är TxtSaveOptions.Separator kommatecken, så ange inte en avgränsare om du sparar i formatet CSV.

**C#**

{{< highlight "csharp" >}}

string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Spara arbetsbok till text eller CSV Format.xlsx";

string destFileName = FilePath + "Spara arbetsbok till text eller CSV Format.txt";

//Ladda din källarbetsbok

Arbetsbok arbetsbok = ny arbetsbok(Filnamn);

//0-byte array

byte[]workbookData = ny byte[0];

//Spara alternativ för text. Du kan använda vilken typ av separator som helst

TxtSaveOptions opts = new TxtSaveOptions();

opts.Separator = '\t';

//Kopiera varje kalkylbladsdata i textformat inuti arbetsboksdatamatrisen

 för (int idx = 0; idx< workbook.Worksheets.Count; idx++)

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

File.WriteAllBytes(destFileName, workbookData);

{{< /highlight >}}
## **Ladda ner provkod**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Save%20Workbook%20to%20Text%20or%20CSV%20Format)

## **Ladda ner körningsexempel**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
