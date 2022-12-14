---
title: Lägga till nya kalkylblad i arbetsboken och aktivera ett arbetsblad i VSTO och Aspose.Cells
type: docs
weight: 30
url: /sv/net/adding-new-worksheets-to-workbook-and-activating-a-sheet-in-vsto-and-aspose-cells/
---
## **Migreringstips:**
1. Lägg till nya kalkylblad till en befintlig Microsoft Excel-fil.
1. Fyll i data i cellerna i varje nytt kalkylblad.
1. Aktivera ett ark i arbetsboken.
1. Spara som Microsoft Excel-fil.

Nedan finns parallella kodavsnitt för VSTO (C#) och Aspose.Cells för .NET (C#), som visar hur man utför dessa uppgifter.

**VSTO**

{{< highlight "csharp" >}}

 //initiera applikationsobjekt

Excel.Application excelApp = Application;

//Ange sökvägen till mallens excel-fil.

string myPath = "Book1.xls";

//Öppna excel-filen.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Saknas.Värde, Saknas.Värde,

Saknas.Värde, Saknas.Värde,

Saknas.Värde, Saknas.Värde,

Saknas.Värde, Saknas.Värde,

Saknas.Värde, Saknas.Värde,

Missing.Value, Missing.Value);

//Deklarera ett kalkylbladsobjekt.

Excel.Worksheet newWorksheet;

//Lägg till 5 nya kalkylblad i arbetsboken och fyll i lite data

//in i cellerna.

 för (int i = 1; i< 6; i++){

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

 //Instantera en instans av licens och ställ in licensfilen

//genom dess väg

Aspose.Cells.Licenslicens = ny Aspose.Cells.License();

license.SetLicense("Aspose.Total.lic");

//Ange sökvägen till mallens excel-fil.

string myPath = "Book1.xls";

//Instantiera en ny arbetsbok.

//Öppna excel-filen.

Workbook workbook = new Workbook(myPath);

//Deklarera ett kalkylbladsobjekt.

Arbetsblad newWorksheet;

//Lägg till 5 nya kalkylblad i arbetsboken och fyll i lite data

//in i cellerna.

 för (int i = 0; i< 5; i++){

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
## **Ladda ner exempelkod**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Adding.New.Worksheets.to.Workbook.and.Activating.a.Sheet.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Adding%20New%20Worksheets%20to%20Workbook%20and%20Activating%20a%20Sheet%20\(Aspose.Cells\).zip/download)
- [Bit hink](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Adding%20New%20Worksheets%20to%20Workbook%20and%20Activating%20a%20Sheet%20\(Aspose.Cells\).blixtlås)
