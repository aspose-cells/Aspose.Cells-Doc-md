---
title: Общедоступный API Изменения в Aspose.Cells 8.4.0
type: docs
weight: 140
url: /ru/java/public-api-changes-in-aspose-cells-8-4-0/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 8.3.2 до 8.4.0, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные публичные методы,[добавлены классы и т.д.](/cells/ru/java/public-api-changes-in-aspose-cells-8-4-0/) а также[удалены классы и т.д.](/cells/ru/java/public-api-changes-in-aspose-cells-8-4-0/), но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Механизм изменения кода VBA/макро в электронных таблицах**
 Для обеспечения возможности[Манипуляции с кодом VBA/макро](/cells/ru/java/modifying-vba-or-macro-code-using-aspose-cells/), Aspose.Cells for Java 8.4.0 представил ряд новых классов и свойств в пакете com.aspose.cells.Vba. Вот несколько важных деталей этих новых классов.

- Класс VbaProject можно использовать для извлечения проекта VBA из данной электронной таблицы.
- Класс VbaModuleCollection представляет коллекцию модулей VBA, которые являются частью данного VbaProject.
- Класс VbaModule представляет один модуль из коллекции VbaModuleCollection.

В следующем фрагменте кода показано, как динамически изменять сегменты кода VBA.

**Java**

{{< highlight "csharp" >}}

 Рабочая книга рабочая книга = новая рабочая книга ("source.xlsm");

//Изменить код модуля VBA

Модули VbaModuleCollection = workbook.getVbaProject().getModules();

 для (целое я = 0; я< modules.getCount(); i++)

{

	VbaModule module = modules.get(i);

    String code = module.getCodes();

    //Replace the original message with the modified message

    if (code.contains("This is test message."))

    {

        code = code.replace("This is test message.", "This is Aspose.Cells message.");

        module.setCodes(code);

    }

}

//Save the output Excel file

workbook.save("output.xlsm");

{{< /highlight >}}
### **Возможность удалить сводную таблицу**
Aspose.Cells for Java 8.4.0 предоставляет два метода для PivotTableCollection, чтобы обеспечить функцию удаления сводной таблицы из данной электронной таблицы. Детали вышеупомянутых способов следующие.

- Метод PivotTableCollection.remove принимает объект сводной таблицы и удаляет его из коллекции.
- Метод PivotTableCollection.removeAt принимает целочисленное значение на основе нулевого индекса и удаляет конкретную сводную таблицу из коллекции.

В следующем фрагменте кода показано, как удалить сводную таблицу, используя оба вышеупомянутых метода.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the first pivot table object

PivotTable pivotTable = worksheet.getPivotTables().get(0);

//Remove pivot table using pivot table object

worksheet.getPivotTables().remove(pivotTable);

//Remove pivot table using pivot table position

worksheet.getPivotTables().removeAt(0);

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **Поддержка различных макетов сводных таблиц**
Aspose.Cells for Java 8.4.0 обеспечивает поддержку различных предопределенных макетов для сводных таблиц. Чтобы обеспечить эту функцию, API-интерфейсы Aspose.Cells предоставили три метода для класса сводной таблицы, как подробно описано ниже.

- Метод PivotTable.showInCompactForm отображает сводную таблицу в компактном макете.
- Метод PivotTable.showInOutlineForm отображает сводную таблицу в макете Outline.
- Метод PivotTable.showInTabularForm отображает сводную таблицу в виде таблицы.

{{% alert color="primary" %}} 

 Важно вызывать PivotTable.refreshData и PivotTable.calculateData после установки любого из вышеупомянутых макетов.

{{% /alert %}} 

Следующий пример кода задает различные макеты для сводной таблицы и сохраняет результат на диске.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first pivot table

PivotTable pivotTable = worksheet.getPivotTables().get(0);

//1 - Show the pivot table in compact form

pivotTable.showInCompactForm();

//Refresh the pivot table

pivotTable.refreshData();

pivotTable.calculateData();

//Save the output

workbook.save("CompactForm.xlsx");

//2 - Show the pivot table in outline form

pivotTable.showInOutlineForm();

//Refresh the pivot table

pivotTable.refreshData();

pivotTable.calculateData();

//Save the output

workbook.save("OutlineForm.xlsx");

//3 - Show the pivot table in tabular form

pivotTable.showInTabularForm();

//Refresh the pivot table

pivotTable.refreshData();

pivotTable.calculateData();

//Save the output

workbook.save("TabularForm.xlsx");

{{< /highlight >}}
### **Добавлен класс TxtLoadStyleStrategy и свойство TxtLoadOptions.LoadStyleStrategy.**
Aspose.Cells for Java 8.4.0 предоставляет класс TxtLoadStyleStrategy и свойство TxtLoadOptions.LoadStyleStrategy для указания стратегии форматирования проанализированных значений при преобразовании строкового значения в число или дату и время.
### **Добавлен метод DataBar.ToImage**
С выпуском v8.4.0 Aspose.Cells API предоставил метод DataBar.toImage для сохранения условно отформатированного DataBar в формате изображения. Метод {DataBar.toImage}} принимает два параметра, как описано ниже.

- Первый параметр имеет тип com.aspose.cells.Cell, к которому применено условное форматирование.
- Второй параметр имеет тип com.aspose.cells.rendering.ImageOrPrintOptions для установки различных параметров результирующего изображения.

В следующем примере кода показано использование метода DataBar.toImage для отображения панели данных в формате изображения.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the cell which contains conditional formatting databar

Cell cell = worksheet.getCells().get("C1");

//Get the conditional formatting of the cell

FormatConditionCollection fcc = cell.getFormatConditions();

//Access the conditional formatting databar

DataBar dbar = fcc.get(0).getDataBar();

//Create image or print options

ImageOrPrintOptions opts = new ImageOrPrintOptions();

opts.setImageFormat(ImageFormat.getPng());

//Get the image bytes of the databar

byte[]imgBytes = dbar.toImage(cell, opts);

//Write image bytes on the disk

FileOutputStream out = new FileOutputStream("databar.png");

out.write(imgBytes);

out.close();

{{< /highlight >}}
### **Добавлено свойство Border.ThemeColor**
Aspose.Cells API позволяют извлекать данные, относящиеся к темам, из электронных таблиц. В выпуске Aspose.Cells for Java 8.4.0 API предоставил свойство Border.ThemeColor, которое можно использовать для получения атрибутов цвета темы границ Cell.
### **Добавлено свойство DrawObject.ImageBytes**
Aspose.Cells for Java 8.4.0 предоставляет свойство DrawObject.ImageBytes для получения данных изображения из диаграммы или формы.
### **Добавлено свойство HtmlSaveOptions.ExportBogusRowData.**
 Aspose.Cells for Java 8.4.0 предоставляет свойство {HtmlSaveOptions.ExportBogusRowData}}. Свойство логического типа определяет, будет ли API вводить фиктивные данные нижней строки при экспорте электронной таблицы в формат HTML.

{{% alert color="primary" %}} 

Значение по умолчанию верно.

{{% /alert %}} 

Следующий пример кода иллюстрирует использование вышеупомянутого свойства.

**Java**

{{< highlight "csharp" >}}

 //Create an object of HtmlSaveOptions class

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the ExportBogusRowData to true

options.ExportBogusRowData = true;

//Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **Добавлено свойство HtmlSaveOptions.CellCssPrefix.**
Недавно добавленное свойство HtmlSaveOptions.CellCssPrefix позволяет устанавливать префикс для файлов CSS при экспорте электронных таблиц в формат HTML.

{{% alert color="primary" %}} 

Значение по умолчанию — "" (пустая строка).

{{% /alert %}}
## **Устаревшие API**
### **Методы Cells.getCellByIndex и Row.getCellByIndex устарели**
Вместо этого используйте метод getEnumerator для перебора всех ячеек.
### **Свойство DrawObject.Image устарело**
Вместо этого используйте свойство DrawObject.ImageBytes для получения данных изображения.
