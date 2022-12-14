---
title: Создание и сохранение новых рабочих книг
type: docs
weight: 70
url: /ru/net/create-and-save-new-workbooks/
---
## **Советы по миграции:**
\1. Создать объект рабочей книги
\2. Получить текущий рабочий лист.
\3. Вставьте текст в любую ячейку.
\4. Сохраните рабочую книгу.
### **ВСТО**
Ниже приведен пример кода для VSTO.

{{< highlight "csharp" >}}

  Excel.Workbook newWorkbook = this.Application.Workbooks.Add();

 Excel.Worksheet worksheet = newWorkbook.ActiveSheet;

 Excel.Range cells = worksheet.Cells;

 cells.set_Item(1,1,"Some Text");

 newWorkbook.Save();

{{< /highlight >}}
### **Aspose.Cells**
Ниже приведен пример кода для Aspose.Cells.

{{< highlight "csharp" >}}

  Workbook newWorkbook = new Workbook();

 Worksheet worksheet = newWorkbook.Worksheets.Add("New Sheet");

 Cells cells = worksheet.Cells;

 cells[0,0].PutValue("Some Text");

 newWorkbook.Save(fileName);

{{< /highlight >}}
## **Скачать**
- [Гитхаб](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Create_SaveNewWorkbooks.Aspose.Cells.zip)
