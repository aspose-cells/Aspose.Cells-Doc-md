---
title: Добавление новых рабочих листов в рабочую книгу и активация листа в VSTO и Aspose.Cells
type: docs
weight: 30
url: /ru/net/adding-new-worksheets-to-workbook-and-activating-a-sheet-in-vsto-and-aspose-cells/
---
## **Совет по миграции:**
1. Добавьте новые рабочие листы в существующий файл Excel Microsoft.
1. Заполните данные в ячейки каждого нового рабочего листа.
1. Активируйте лист в книге.
1. Сохранить как файл Excel Microsoft.

Ниже приведены параллельные фрагменты кода для VSTO (C#) и Aspose.Cells for .NET (C#), которые показывают, как выполнить эти задачи.

**ВСТО**

{{< highlight "csharp" >}}

// инициировать объект приложения

Excel.Приложение excelApp = Приложение;

// Указываем путь к файлу excel шаблона.

строка myPath = "Book1.xls";

//Открываем файл excel.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Отсутствует.Значение, Отсутствует.Значение,

Отсутствует.Значение, Отсутствует.Значение,

Отсутствует.Значение, Отсутствует.Значение,

Отсутствует.Значение, Отсутствует.Значение,

Отсутствует.Значение, Отсутствует.Значение,

Отсутствующее.Значение, Отсутствующее.Значение);

// Объявить объект Worksheet.

Excel.Worksheet newWorksheet;

//Добавить 5 новых рабочих листов в рабочую книгу и заполнить некоторые данные

//в ячейки.

 для (целое я = 1; я< 6; i++){

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

 //Создаем экземпляр лицензии и устанавливаем файл лицензии

//по своему пути

Aspose.Cells.License license = new Aspose.Cells.License();

лицензия.SetLicense("Aspose.Total.lic");

// Указываем путь к файлу excel шаблона.

строка myPath = "Book1.xls";

//Создание новой книги.

//Открываем файл excel.

Книга рабочей книги = новая рабочая книга (мой путь);

// Объявить объект Worksheet.

Рабочий лист новыйРабочий лист;

//Добавить 5 новых рабочих листов в рабочую книгу и заполнить некоторые данные

//в ячейки.

 для (целое я = 0; я< 5; i++){

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
## **Скачать пример кода**
- [Гитхаб](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Adding.New.Worksheets.to.Workbook.and.Activating.a.Sheet.Aspose.Cells.zip)
- [Источникфорж](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Adding%20New%20Worksheets%20to%20Workbook%20and%20Activating%20a%20Sheet%20\(Aspose.Cells\).zip/скачать)
- [Битбакет](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Adding%20New%20Worksheets%20to%20Workbook%20and%20Activating%20a%20Sheet%20\(Aspose.Cells\).zip)
