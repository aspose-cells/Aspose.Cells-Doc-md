---
title: Arbeitsmappe in Text oder CSV Format in Aspose.Cells speichern
type: docs
weight: 110
url: /de/net/save-workbook-to-text-or-csv-format-in-aspose-cells/
---

{{% alert color="primary" %}} 

Manchmal möchten Sie eine Arbeitsmappe mit mehreren Arbeitsblättern im Textformat konvertieren oder speichern. Für Textformate (z.B. TXT, TabDelim, CSV etc.) speichern sowohl Microsoft Excel als auch Aspose.Cells standardmäßig nur den Inhalt des aktiven Arbeitsblatts.

{{% /alert %}} 

Das folgende Codebeispiel erläutert, wie eine gesamte Arbeitsmappe in Textformat gespeichert werden kann. Laden Sie die Quellarbeitsmappe, die eine beliebige Microsoft Excel- oder OpenOffice-Tabellendatei sein kann (also XLS, XLSX, XLSM, XLSB, ODS usw.) mit einer beliebigen Anzahl von Tabellenblättern.

Wenn der Code ausgeführt wird, konvertiert er die Daten aller Blätter in der Arbeitsmappe in das TXT-Format.

Sie können das gleiche Beispiel ändern, um Ihre Datei in CSV zu speichern. Standardmäßig ist bei TxtSaveOptions.Separator ein Komma angegeben. Geben Sie also keinen Separator an, wenn Sie im CSV-Format speichern.

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
## **Laufenden Code herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Save%20Workbook%20to%20Text%20or%20CSV%20Format)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
