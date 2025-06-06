---
title: Добавить гиперссылки в ячейки в VSTO и Aspose.Cells
type: docs
weight: 20
url: /ru/net/add-hyperlinks-to-cells-in-vsto-and-aspose-cells/
---

Чтобы добавить гиперссылки в ячейки электронной таблицы, выполните следующие шаги:

1. Настройте лист: 
   1. Создать объект приложения.(только VSTO.)
   1. Добавить книгу.
   1. Получить первый лист.
   1. Добавьте текст в ячейки, к которым хотите добавить гиперссылку.
1. Добавьте гиперссылку.
1. Сохраните документ.

Эти шаги показаны в приведенных ниже примерах кода. Первый пример показывает, как использовать VSTO с C# для добавления гиперссылки в ячейку. Последующие примеры показывают, как сделать то же самое с использованием Aspose.Cells for .NET, также с помощью C#.

Образцы кода генерируют файл Excel с гиперссылкой в ячейке A1 на первом рабочем листе.

![todo:image_alt_text](picture1.png)

Гиперссылка добавлена в ячейку A1.

## **VSTO**

{{< highlight csharp >}}

 //Instantiate the Application object.

Excel.Application ExcelApp = Application;

//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);

//Get the First sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];

//Define a range object(A1).

Excel.Range _range;

_range = objSheet.get_Range("A1", "A1");

//Add a hyperlink to it.

objSheet.Hyperlinks.Add(_range, "http://www.aspose.com/", Type.Missing, "Click to go to Aspose site", "Aspose Site!");

//Save the excel file.

objBook.SaveCopyAs("Hyperlink_test.xls");

//Quit the Application.

ExcelApp.Quit();

{{< /highlight >}}

## **Aspose.Cells**

{{< highlight csharp >}}

 //Instantiate a new Workbook object.

Workbook workbook = new Workbook();

//Get the First sheet.

Worksheet worksheet = workbook.Worksheets[0];

//Define A1 Cell.

Aspose.Cells.Cell cell = worksheet.Cells["A1"];

//Add a hyperlink to it.

int index = worksheet.Hyperlinks.Add("A1", 1, 1, "http://www.aspose.com/");

worksheet.Hyperlinks[index].TextToDisplay = "Aspose Site!";

worksheet.Hyperlinks[index].ScreenTip = "Click to go to Aspose site";

//Save the excel file.

workbook.Save("Hyperlink_test.xls");

{{< /highlight >}}

## **Загрузить образец кода**

- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Add.Hyperlinks.to.Cells.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Add%20Hyperlinks%20to%20Cells%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Add%20Hyperlinks%20to%20Cells%20\(Aspose.Cells\).zip)
{{< app/cells/assistant language="csharp" >}}
