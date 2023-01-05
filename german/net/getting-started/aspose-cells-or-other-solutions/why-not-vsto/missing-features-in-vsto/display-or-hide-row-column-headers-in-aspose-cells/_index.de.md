---
title: Anzeigen oder Ausblenden von Zeilen-Spalten-Überschriften in Aspose.Cells
type: docs
weight: 60
url: /de/net/display-or-hide-row-column-headers-in-aspose-cells/
---
{{% alert color="primary" %}}

Alle Arbeitsblätter in einer Excel-Datei bestehen aus Zellen, die in Zeilen und Spalten angeordnet sind. Alle Zeilen und Spalten haben eindeutige Werte, die zu ihrer Identifizierung und zur Identifizierung einzelner Zellen verwendet werden. Beispielsweise werden Zeilen nummeriert – 1, 2, 3, 4 usw. – und Spalten alphabetisch geordnet – A, B, C, D usw. Die Zeilen- und Spaltenwerte werden in den Kopfzeilen angezeigt. Mit Aspose.Cells können Entwickler die Sichtbarkeit dieser Zeilen- und Spaltenüberschriften steuern.

{{% /alert %}}

## **Steuern der Sichtbarkeit der Arbeitsblätter**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , die eine Microsoft Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

 Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) -Klasse bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten von Arbeitsblättern. Um die Sichtbarkeit von Zeilen- und Spaltenüberschriften zu steuern, verwenden Sie die[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse'[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) Eigentum.[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) ist eine boolesche Eigenschaft, was bedeutet, dass sie nur a speichern kann**wahr** oder**FALSCH** Wert.

 Nachfolgend finden Sie ein vollständiges Beispiel, das die Verwendung von zeigt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse'[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) -Eigenschaft zum Ausblenden von Zeilen- und Spaltenüberschriften auf dem ersten Arbeitsblatt in einer Datei.

Der Screenshot zeigt Book1.xls, die Eingabedatei. Es enthält drei Arbeitsblätter: Sheet1, Sheet2 und Sheet3. Jedes Arbeitsblatt zeigt Zeilen- und Spaltenüberschriften.

**Book1.xls: Arbeitsblatt vor der Änderung**

![todo: Bild_alt_Text](display-or-hide-row-column-headers-in-aspose-cells_1.png)

Book1.xls wird geöffnet, indem die Open-Methode der Workbook-Klasse aufgerufen wird, und die Zeilen- und Spaltenüberschriften auf dem ersten Arbeitsblatt werden ausgeblendet. Die geänderte Datei wird als output.xls gespeichert.

**Output.xls: Arbeitsblatt nach der Änderung** 

![todo: Bild_alt_Text](display-or-hide-row-column-headers-in-aspose-cells_2.png)

**C#**

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Hiding the headers of rows and columns

worksheet.IsRowColumnHeadersVisible = false;

//Saving the modified Excel file

workbook.Save("output.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **Laufcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Row%20Column%20Headers)

## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
