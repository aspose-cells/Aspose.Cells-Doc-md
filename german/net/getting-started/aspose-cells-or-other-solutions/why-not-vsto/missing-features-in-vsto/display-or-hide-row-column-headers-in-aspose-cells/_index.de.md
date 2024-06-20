---
title: Zeigen oder Ausblenden von Zeilen und Spaltenüberschriften in Aspose.Cells
type: docs
weight: 60
url: /de/net/display-or-hide-row-column-headers-in-aspose-cells/
---

{{% alert color="primary" %}}

Alle Arbeitsblätter in einer Excel-Datei bestehen aus Zellen, die in Zeilen und Spalten angeordnet sind. Alle Zeilen und Spalten haben eindeutige Werte, die zur Identifizierung und zur Identifizierung einzelner Zellen verwendet werden. Beispielsweise sind Zeilen nummeriert - 1, 2, 3, 4 usw. - und Spalten sind alphabetisch geordnet - A, B, C, D usw. Die Zeilen- und Spaltenwerte werden in den Überschriften angezeigt. Mit Aspose.Cells können Entwickler die Sichtbarkeit dieser Zeilen- und Spaltenüberschriften steuern.

{{% /alert %}}

## **Steuerung der Sichtbarkeit der Arbeitsblätter**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) enthält eine [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung von Arbeitsblättern. Um die Sichtbarkeit von Zeilen- und Spaltenüberschriften zu steuern, verwenden Sie die Eigenschaft [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) der Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) ist eine boolesche Eigenschaft, was bedeutet, dass sie nur einen **true** oder **false** Wert speichern kann.

Ein vollständiges Beispiel unten zeigt, wie die Eigenschaft [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) der Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) verwendet wird, um Zeilen- und Spaltenüberschriften auf dem ersten Arbeitsblatt in einer Datei zu verbergen.

Der Screenshot zeigt Book1.xls, die Eingabedatei. Sie enthält drei Arbeitsblätter: Sheet1, Sheet2 und Sheet3. Jedes Arbeitsblatt zeigt Zeilen- und Spaltenüberschriften.

**Book1.xls: Arbeitsblatt vor der Änderung**

![todo:image_alt_text](display-or-hide-row-column-headers-in-aspose-cells_1.png)

Book1.xls wird durch Aufrufen der Open-Methode der Workbook-Klasse geöffnet und die Zeilen- und Spaltenüberschriften auf dem ersten Arbeitsblatt werden ausgeblendet. Die geänderte Datei wird als output.xls gespeichert.

**Output.xls: Arbeitsblatt nach der Änderung** 

![todo:image_alt_text](display-or-hide-row-column-headers-in-aspose-cells_2.png)

**C#**

{{< highlight csharp >}}

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

## **Laufenden Code herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Row%20Column%20Headers)

## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
