---
title: Aggiunta di nuovi fogli di lavoro alla cartella di lavoro e attivazione di un foglio in VSTO e Aspose.Cells
type: docs
weight: 30
url: /it/net/adding-new-worksheets-to-workbook-and-activating-a-sheet-in-vsto-and-aspose-cells/
---
## **Suggerimento per la migrazione:**
1. Aggiungi nuovi fogli di lavoro a un file Microsoft Excel esistente.
1. Inserisci i dati nelle celle di ogni nuovo foglio di lavoro.
1. Attiva un foglio nella cartella di lavoro.
1. Salva come file Microsoft Excel.

Di seguito sono riportati frammenti di codice paralleli per VSTO (C#) e Aspose.Cells for .NET (C#), che mostrano come eseguire queste attività.

**VSTO**

{{< highlight "csharp" >}}

 //inizia l'oggetto dell'applicazione

Excel.Application excelApp = Applicazione;

//Specifica il percorso del file excel del modello.

string myPath = "Libro1.xls";

//Apri il file excel.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Valore.mancante, Valore.mancante,

Valore.mancante, Valore.mancante,

Valore.mancante, Valore.mancante,

Valore.mancante, Valore.mancante,

Valore.mancante, Valore.mancante,

Valore.Mancante, Valore.Mancante);

//Dichiara un oggetto foglio di lavoro.

Excel.Foglio di lavoro nuovoFoglio di lavoro;

//Aggiungi 5 nuovi fogli di lavoro alla cartella di lavoro e inserisci alcuni dati

//nelle celle.

 per (int i = 1; i< 6; i++){

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

 //Crea un'istanza di licenza e imposta il file di licenza

//attraverso il suo percorso

Aspose.Cells.License licenza = new Aspose.Cells.License();

licenza.SetLicense("Aspose.Total.lic");

//Specifica il percorso del file excel del modello.

string myPath = "Libro1.xls";

//Crea un'istanza di una nuova cartella di lavoro.

//Apri il file excel.

Cartella di lavoro cartella di lavoro = new Cartella di lavoro(myPath);

//Dichiara un oggetto foglio di lavoro.

Foglio di lavoro nuovoFoglio di lavoro;

//Aggiungi 5 nuovi fogli di lavoro alla cartella di lavoro e inserisci alcuni dati

//nelle celle.

 per (int i = 0; i< 5; i++){

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
## **Scarica il codice di esempio**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Adding.New.Worksheets.to.Workbook.and.Activating.a.Sheet.Aspose.Cells.zip)
- [SourceForge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Adding%20New%20Worksheets%20to%20Workbook%20and%20Activating%20a%20Sheet%20\(Aspose.Cells\).zip/scarica)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Adding%20New%20Worksheets%20to%20Workbook%20and%20Activating%20a%20Sheet%20\(Aspose.Cells\).cerniera lampo)
