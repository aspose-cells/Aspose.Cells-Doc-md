---
title: Копирование листов
type: docs
weight: 60
url: /ru/net/copy-worksheets/
---

## **Совет по миграции:**
\1. Создайте объект рабочей книги и получите лист.
\2. Вставьте текст в лист.
\3. Создайте новый лист и скопируйте его на предыдущий сделанный лист.
### **VSTO**
Ошибка в рендеринге макроса 'code': Недопустимое значение для параметра lang
### **Aspose.Cells**
{{< highlight csharp >}}

  private static string fileName ="CopyWorksheets.xlsx";

 Workbook newWorkbook = new Workbook();

 Worksheet worksheet = newWorkbook.Worksheets.Add("New Sheet");

 Cells cells = worksheet.Cells;

 cells[0, 0].PutValue("Some Text");

 Worksheet worksheet2 = newWorkbook.Worksheets.Add("MySheet");

 worksheet2.Copy(worksheet);

 newWorkbook.Save(fileName);

{{< /highlight >}}
## **Загрузка**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/CopyWorksheets.Aspose.Cells.zip)
{{< app/cells/assistant language="csharp" >}}
