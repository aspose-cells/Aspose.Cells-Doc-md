---
title: Копировать рабочие листы
type: docs
weight: 60
url: /ru/net/copy-worksheets/
---
## **Совет по миграции:**
\1. Создайте объект Workbook и получите Worksheet.
\2. Вставьте текст в рабочий лист.
\3. Создайте новый рабочий лист и скопируйте его на предыдущий перед созданием рабочего листа.
### **ВСТО**
Ошибка рендеринга макроса 'code': указано недопустимое значение для параметра lang
### **Aspose.Cells**
{{< highlight "csharp" >}}

  private static string fileName ="CopyWorksheets.xlsx";

 Workbook newWorkbook = new Workbook();

 Worksheet worksheet = newWorkbook.Worksheets.Add("New Sheet");

 Cells cells = worksheet.Cells;

 cells[0, 0].PutValue("Some Text");

 Worksheet worksheet2 = newWorkbook.Worksheets.Add("MySheet");

 worksheet2.Copy(worksheet);

 newWorkbook.Save(fileName);

{{< /highlight >}}
## **Скачать**
- [Гитхаб](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/CopyWorksheets.Aspose.Cells.zip)
