---
title: Speichern Sie die Arbeitsmappe im Text- oder CSV-Format unter Aspose.Cells
type: docs
weight: 110
url: /de/net/save-workbook-to-text-or-csv-format-in-aspose-cells/
---
{{% alert color="primary" %}} 

Manchmal möchten Sie eine Arbeitsmappe mit mehreren Arbeitsblättern in das Textformat konvertieren oder speichern. Bei Textformaten (z. B. TXT, TabDelim, CSV usw.) speichern sowohl Microsoft Excel als auch Aspose.Cells standardmäßig nur den Inhalt des aktiven Arbeitsblatts.

{{% /alert %}} 

Im folgenden Codebeispiel wird erläutert, wie eine gesamte Arbeitsmappe im Textformat gespeichert wird. Laden Sie die Quellarbeitsmappe, bei der es sich um eine beliebige Microsoft Excel- oder OpenOffice-Tabellendatei (also XLS, XLSX, XLSM, XLSB, ODS usw.) mit einer beliebigen Anzahl von Arbeitsblättern handeln kann.

Wenn der Code ausgeführt wird, konvertiert er die Daten aller Blätter in der Arbeitsmappe in das TXT-Format.

Sie können dasselbe Beispiel ändern, um Ihre Datei im CSV-Format zu speichern. Standardmäßig ist TxtSaveOptions.Separator ein Komma, geben Sie also kein Trennzeichen an, wenn Sie im CSV-Format speichern.

**C#**

{{< highlight "csharp" >}}

 string filePath = "source.xlsx";

//Laden Sie Ihre Quellarbeitsmappe

Arbeitsmappe Arbeitsmappe = neue Arbeitsmappe (Dateipfad);

//0-Byte-Array

byte[]workbookData = new byte[0];

//Optionen zum Speichern von Text. Sie können jede Art von Trennzeichen verwenden

TxtSaveOptions opts = neue TxtSaveOptions();

opts.Trennzeichen = '\t';

// Alle Arbeitsblattdaten im Textformat in das Datenarray der Arbeitsmappe kopieren

 für (int idx = 0; idx< workbook.Worksheets.Count; idx++)

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
## **Laufcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Save%20Workbook%20to%20Text%20or%20CSV%20Format)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
