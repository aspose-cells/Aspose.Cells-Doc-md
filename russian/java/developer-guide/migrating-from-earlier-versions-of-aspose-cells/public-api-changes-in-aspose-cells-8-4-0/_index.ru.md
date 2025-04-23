---
title: Изменения в общедоступном API в Aspose.Cells 8.4.0
type: docs
weight: 140
url: /ru/java/public-api-changes-in-aspose-cells-8-4-0/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 8.3.2 до 8.4.0, которые могут быть интересны разработчикам модулей/приложений. Он включает не только новые и обновленные общедоступные методы, [добавленные классы и т. д.](/cells/ru/java/public-api-changes-in-aspose-cells-8-4-0/) и [удаленные классы и т. д.](/cells/ru/java/public-api-changes-in-aspose-cells-8-4-0/), но также описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Механизм изменения кода VBA/Macro в электронных таблицах**
Для предоставления функции [Манипулирования кодом VBA/Macro](/cells/ru/java/modifying-vba-or-macro-code-using-aspose-cells/), Aspose.Cells for Java 8.4.0 представил ряд новых классов и свойств в пакете com.aspose.cells.Vba. Некоторые важные детали этих новых классов приведены ниже.

- Класс VbaProject может быть использован для извлечения проекта VBA из заданной электронной таблицы.
- Класс VbaModuleCollection представляет коллекцию VBA-модулей, которые являются частью заданного VbaProject.
- Класс VbaModule представляет один модуль из VbaModuleCollection.

Далее приведен фрагмент кода, показывающий, как динамически изменить сегменты кода VBA.

**Java**

{{< highlight csharp >}}

 Workbook workbook = new Workbook("source.xlsm");

//Change the VBA Module Code

VbaModuleCollection modules = workbook.getVbaProject().getModules();

for(int i=0; i < modules.getCount(); i++)

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
Aspose.Cells for Java 8.4.0 предоставляет два метода для PivotTableCollection для удаления сводной таблицы из заданной электронной таблицы. Подробности указанных методов приведены ниже.

- Метод PivotTableCollection.remove принимает объект PivotTable и удаляет его из коллекции.
- Метод PivotTableCollection.removeAt принимает целочисленное значение, основанное на нуле, и удаляет определенную сводную таблицу из коллекции.

Далее показан фрагмент кода, показывающий, как удалить сводную таблицу с использованием обоих вышеупомянутых методов.

**Java**

{{< highlight csharp >}}

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
Aspose.Cells for Java 8.4.0 предоставляет поддержку различных предварительно определенных макетов для сводных таблиц. Для обеспечения этой функции API Aspose.Cells представил три метода для класса PivotTable, подробно описанных ниже.

- Метод PivotTable.showInCompactForm отображает сводную таблицу в компактном макете.
- Метод PivotTable.showInOutlineForm отображает сводную таблицу в макете контурной формы.
- Метод PivotTable.showInTabularForm отображает сводную таблицу в табличном макете.

{{% alert color="primary" %}} 

Важно вызвать PivotTable.refreshData и PivotTable.calculateData после установки любой из вышеупомянутых компоновок. 

{{% /alert %}} 

В следующем примере кода устанавливаются различные компоновки для сводной таблицы и результат сохраняется на диск.

**Java**

{{< highlight csharp >}}

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
### **Добавлены класс TxtLoadStyleStrategy и свойство TxtLoadOptions.LoadStyleStrategy.**
Версия Aspose.Cells for Java 8.4.0 предоставляет класс TxtLoadStyleStrategy и свойство TxtLoadOptions.LoadStyleStrategy для указания стратегии форматирования обработанных значений при преобразовании строки в число или дату.
### **Добавлен метод DataBar.ToImage.**
С выпуском версии 8.4.0 API Aspose.Cells предоставил метод DataBar.toImage для сохранения условно отформатированной панели данных в формате изображения. Метод {DataBar.toImage}} принимает два параметра, описанных ниже.

- Первый параметр имеет тип com.aspose.cells.Cell, на котором применено условное форматирование.
- Второй параметр имеет тип com.aspose.cells.rendering.ImageOrPrintOptions для установки различных параметров результирующего изображения.

В следующем образце кода демонстрируется использование метода DataBar.toImage для отображения панели данных в формате изображения.

**Java**

{{< highlight csharp >}}

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

byte[] imgBytes = dbar.toImage(cell, opts);

//Write image bytes on the disk

FileOutputStream out = new FileOutputStream("databar.png");

out.write(imgBytes);

out.close();

{{< /highlight >}}
### **Добавлено свойство Border.ThemeColor.**
API Aspose.Cells позволяет извлекать данные, связанные с темами, из таблиц. С выпуском Aspose.Cells for Java 8.4.0 API предоставил свойство Border.ThemeColor, которое можно использовать для извлечения атрибутов цветов темы границ ячеек.
### **Добавлено свойство DrawObject.ImageBytes.**
В версии Aspose.Cells for Java 8.4.0 было добавлено свойство DrawObject.ImageBytes для получения данных изображения из диаграммы или формы.
### **Добавлено свойство HtmlSaveOptions.ExportBogusRowData.**
В версии Aspose.Cells for Java 8.4.0 было добавлено свойство {HtmlSaveOptions.ExportBogusRowData}}. Это свойство типа Boolean определяет, будет ли API внедрять фиктивные данные нижней строки при экспорте таблицы в формат HTML. 

{{% alert color="primary" %}} 

Значение по умолчанию - true.

{{% /alert %}} 

В следующем примере кода иллюстрируется использование вышеупомянутого свойства.

**Java**

{{< highlight csharp >}}

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
Новое свойство HtmlSaveOptions.CellCssPrefix позволяет установить префикс для CSS-файлов при экспорте таблиц в формат HTML.

{{% alert color="primary" %}} 

Значение по умолчанию - "" (пустая строка).

{{% /alert %}}
## **Устаревшие API**
### **Устаревшие методы Cells.getCellByIndex и Row.getCellByIndex**
Используйте метод getEnumerator для итерации всех ячеек вместо этого.
### **Свойство DrawObject.Image устарело**
Используйте свойство DrawObject.ImageBytes для получения данных изображения вместо этого.
{{< app/cells/assistant language="java" >}}
