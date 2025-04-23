---
title: Rastlinien anzeigen oder ausblenden in Aspose.Cells
type: docs
weight: 50
url: /de/net/display-or-hide-gridlines-in-aspose-cells/
---

{{% alert color="primary" %}}

Alle Excel-Arbeitsblätter haben standardmäßig Rastlinien. Sie helfen dabei, Zellen abzugrenzen, sodass es einfach ist, Daten in bestimmte Zellen einzugeben. Rastlinien ermöglichen es uns, ein Arbeitsblatt als Sammlung von Zellen zu betrachten, in der jede Zelle leicht identifizierbar ist.

{{% /alert %}}

## **Steuerung der Sichtbarkeit der Rastlinien**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), die eine Microsoft Excel-Datei darstellt. Die Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) enthält eine [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung eines Arbeitsblatts. Um die Sichtbarkeit von Gitternetzlinien zu steuern, verwenden Sie die Eigenschaft [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) der Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) ist eine boolesche Eigenschaft, was bedeutet, dass sie nur einen **true** oder **false** Wert speichern kann.

Ein vollständiges Beispiel unten zeigt die Verwendung der Eigenschaft [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) der Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet), um die Gitternetzlinien des ersten Arbeitsblatts der Excel-Datei zu verbergen.

Im folgenden Screenshot ist zu sehen, dass die Datei Book1.xls drei Arbeitsblätter enthält: Sheet1, Sheet2 und Sheet3. Alle Arbeitsblätter haben Gitternetzlinien.

**Book1.xls: Arbeitsblattansicht vor der Änderung** 

![todo:image_alt_text](display-or-hide-gridlines-in-aspose-cells_1.png)

Die Datei Book1.xls wird mithilfe der Workbook-Klasse geöffnet und die Gitternetzlinien auf dem ersten Arbeitsblatt werden ausgeblendet. Die geänderte Datei wird als output.xls gespeichert.

**Output.xls: Arbeitsblatt nach der Änderung** 

![todo:image_alt_text](display-or-hide-gridlines-in-aspose-cells_2.png)

**C#**

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Hiding the gridlines of the first worksheet of the Excel file

worksheet.IsGridlinesVisible = false;

//Saving the modified Excel file

workbook.Save("output.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **Laufenden Code herunterladen**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Gridlines)

## **Beispielcode herunterladen**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
{{< app/cells/assistant language="csharp" >}}
