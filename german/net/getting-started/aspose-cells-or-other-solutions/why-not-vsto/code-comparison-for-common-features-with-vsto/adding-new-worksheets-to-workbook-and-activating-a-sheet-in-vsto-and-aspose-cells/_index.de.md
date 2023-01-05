---
title: Hinzufügen neuer Arbeitsblätter zur Arbeitsmappe und Aktivieren eines Blatts in VSTO und Aspose.Cells
type: docs
weight: 30
url: /de/net/adding-new-worksheets-to-workbook-and-activating-a-sheet-in-vsto-and-aspose-cells/
---
## **Migrationstipp:**
1. Fügen Sie neue Arbeitsblätter zu einer bestehenden Microsoft Excel-Datei hinzu.
1. Füllen Sie Daten in die Zellen jedes neuen Arbeitsblatts ein.
1. Aktivieren Sie ein Blatt in der Arbeitsmappe.
1. Als Microsoft Excel-Datei speichern.

Nachfolgend finden Sie parallele Codeausschnitte für VSTO (C#) und Aspose.Cells for .NET (C#), die zeigen, wie diese Aufgaben ausgeführt werden.

**VSTO**

{{< highlight "csharp" >}}

//Anwendungsobjekt initiieren

Excel.Application excelApp = Anwendung;

//Geben Sie den Excel-Dateipfad der Vorlage an.

string myPath = "Buch1.xls";

//Excel-Datei öffnen.

excelApp.Workbooks.Open(myPath, Fehlender.Wert, Fehlender.Wert,

Fehlender.Wert, Fehlender.Wert,

Fehlender.Wert, Fehlender.Wert,

Fehlender.Wert, Fehlender.Wert,

Fehlender.Wert, Fehlender.Wert,

Fehlender.Wert, Fehlender.Wert,

Fehlender.Wert, Fehlender.Wert);

//Ein Worksheet-Objekt deklarieren.

Excel.Worksheet newWorksheet;

// Fügen Sie der Arbeitsmappe 5 neue Arbeitsblätter hinzu und füllen Sie einige Daten aus

//in die Zellen.

 für (int i = 1; i< 6; i++){

                //Add a worksheet to the workbook.

                newWorksheet = (Excel.Worksheet)excelApp.Worksheets.Add(Missing.Value, Missing.Value,

                Missing.Value, Missing.Value);

                //Name the sheet.

                newWorksheet.Name = "New_Sheet" + i.ToString();

                //Get the Cells collection.

                Excel.Range cells = newWorksheet.Cells;

                //Input a string value to a cell of the sheet.

                cells.set_Item(i, i, "New_Sheet" + i.ToString());

            }

//Activate the first worksheet by default.

((Excel.Worksheet)excelApp.ActiveWorkbook.Sheets[1]).Activate();

//Save As the excel file.

excelApp.ActiveWorkbook.SaveCopyAs("out_Book1.xls");

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}

**Aspose.Cells**

{{< highlight "csharp" >}}

 //Instanziieren Sie eine Lizenzinstanz und legen Sie die Lizenzdatei fest

//durch seinen Weg

Aspose.Cells.License Lizenz = neu Aspose.Cells.License();

lizenz.SetLicense("Aspose.Total.lic");

//Geben Sie den Excel-Dateipfad der Vorlage an.

string myPath = "Buch1.xls";

// Instanziiere eine neue Arbeitsmappe.

//Excel-Datei öffnen.

Arbeitsmappe Arbeitsmappe = neue Arbeitsmappe (myPath);

//Ein Worksheet-Objekt deklarieren.

Arbeitsblatt neuesArbeitsblatt;

// Fügen Sie der Arbeitsmappe 5 neue Arbeitsblätter hinzu und füllen Sie einige Daten aus

//in die Zellen.

 für (int i = 0; i< 5; i++){

                //Add a worksheet to the workbook.

                newWorksheet = workbook.Worksheets[workbook.Worksheets.Add()];

                //Name the sheet.

                newWorksheet.Name = "New_Sheet" + (i + 1).ToString();

                //Get the Cells collection.

                Cells cells = newWorksheet.Cells;

                //Input a string value to a cell of the sheet.

                cells[i, i].PutValue("New_Sheet" + (i + 1).ToString());

            }

//Activate the first worksheet by default.

workbook.Worksheets.ActiveSheetIndex = 0;

//Save As the excel file.

workbook.Save("out_My_Book1.xls");

{{< /highlight >}}
## **Beispielcode herunterladen**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Adding.New.Worksheets.to.Workbook.and.Activating.a.Sheet.Aspose.Cells.zip)
- [Quellenschmiede](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Adding%20New%20Worksheets%20to%20Workbook%20and%20Activating%20a%20Sheet%20\(Aspose.Cells\).zip/herunterladen)
- [Bit Bucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Adding%20New%20Worksheets%20to%20Workbook%20and%20Activating%20a%20Sheet%20\(Aspose.Cells\).Postleitzahl)
