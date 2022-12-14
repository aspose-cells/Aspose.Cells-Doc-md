---
title: Agregar nuevas hojas de trabajo al libro de trabajo y activar una hoja en VSTO y Aspose.Cells
type: docs
weight: 30
url: /es/net/adding-new-worksheets-to-workbook-and-activating-a-sheet-in-vsto-and-aspose-cells/
---
## **Consejo de migración:**
1. Agregue nuevas hojas de trabajo a un archivo de Excel Microsoft existente.
1. Complete los datos en las celdas de cada nueva hoja de trabajo.
1. Activar una hoja en el libro de trabajo.
1. Guardar como archivo de Excel Microsoft.

A continuación, se encuentran fragmentos de código paralelo para VSTO (C#) y Aspose.Cells for .NET (C#), que muestran cómo lograr estas tareas.

**VSTO**

{{< highlight "csharp" >}}

//iniciar objeto de aplicación

Excel.Aplicación excelApp = Aplicación;

//Especifique la ruta del archivo de Excel de la plantilla.

string myPath = "Libro1.xls";

//Abrir el archivo de Excel.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Valor perdido, Valor perdido,

Valor perdido, Valor perdido,

Valor perdido, Valor perdido,

Valor perdido, Valor perdido,

Valor perdido, Valor perdido,

Valor perdido, Valor perdido);

//Declarar un objeto de hoja de trabajo.

Excel.Hoja de trabajo nuevaHoja de trabajo;

//Agregue 5 nuevas hojas de trabajo al libro de trabajo y complete algunos datos

//a las celdas.

 para (int i = 1; i< 6; i++){

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

 //Crear una instancia de licencia y configurar el archivo de licencia

//a traves de su camino

Aspose.Cells.Licencia licencia = nuevo Aspose.Cells.Licencia();

licencia.SetLicense("Aspose.Total.lic");

//Especifique la ruta del archivo de Excel de la plantilla.

string myPath = "Libro1.xls";

//Crear una instancia de un nuevo libro de trabajo.

//Abrir el archivo de Excel.

Libro de trabajo libro de trabajo = nuevo libro de trabajo (myPath);

//Declarar un objeto de hoja de trabajo.

Hoja de trabajo nuevaHoja de trabajo;

//Agregue 5 nuevas hojas de trabajo al libro de trabajo y complete algunos datos

//a las celdas.

 para (int i = 0; i< 5; i++){

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
## **Descargar código de muestra**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Adding.New.Worksheets.to.Workbook.and.Activating.a.Sheet.Aspose.Cells.zip)
- [forjafuente](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Adding%20New%20Worksheets%20to%20Workbook%20and%20Activating%20a%20Sheet%20\(Aspose.Cells\).zip/descargar)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Adding%20New%20Worksheets%20to%20Workbook%20and%20Activating%20a%20Sheet%20\(Aspose.Cells\).Código Postal)
