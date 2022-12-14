---
title: Gitternetzlinien anzeigen oder ausblenden in Aspose.Cells
type: docs
weight: 50
url: /de/net/display-or-hide-gridlines-in-aspose-cells/
---
{{% alert color="primary" %}}

Alle Excel-Arbeitsblätter haben standardmäßig Gitternetzlinien. Sie helfen dabei, Zellen abzugrenzen, sodass es einfach ist, Daten in bestimmte Zellen einzugeben. Gitternetzlinien ermöglichen es uns, ein Arbeitsblatt als eine Sammlung von Zellen anzuzeigen, wobei jede Zelle leicht identifizierbar ist.

{{% /alert %}}

## **Steuern der Sichtbarkeit der Gitternetzlinien**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , die eine Microsoft Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

 Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) -Klasse bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten eines Arbeitsblatts. Um die Sichtbarkeit von Gitternetzlinien zu steuern, verwenden Sie die[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse'[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) Eigentum.[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) ist eine boolesche Eigenschaft, was bedeutet, dass sie nur a speichern kann**Stimmt** oder**FALSCH** Wert.

 Nachfolgend finden Sie ein vollständiges Beispiel, das die Verwendung von demonstriert[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) Eigentum der[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse, um die Gitternetzlinien des ersten Arbeitsblatts der Excel-Datei auszublenden.

Im Screenshot unten sehen Sie, dass die Datei Book1.xls drei Arbeitsblätter enthält: Sheet1, Sheet2 und Sheet3. Alle Arbeitsblätter haben Gitterlinien.

**Book1.xls: Arbeitsblattansicht vor der Änderung** 

![todo: Bild_alt_Text](display-or-hide-gridlines-in-aspose-cells_1.png)

Die Datei Book1.xls wird mithilfe der Workbook-Klasse geöffnet, und die Gitternetzlinien auf dem ersten Arbeitsblatt werden ausgeblendet. Die geänderte Datei wird als output.xls gespeichert.

**Output.xls: Arbeitsblatt nach der Änderung** 

![todo: Bild_alt_Text](display-or-hide-gridlines-in-aspose-cells_2.png)

**C#**

{{< highlight "csharp" >}}

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

## **Laufcode herunterladen**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Gridlines)

## **Beispielcode herunterladen**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
