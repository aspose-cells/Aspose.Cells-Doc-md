---
title: Изменения в общедоступном API в Aspose.Cells 8.0.0
type: docs
weight: 20
url: /ru/java/public-api-changes-in-aspose-cells-8-0-0/
---

{{% alert color="primary" %}} 

Эта страница перечисляет изменения в общедоступном API, которые были внесены в Aspose.Cells 8.0.0. Она включает не только новые и устаревшие общедоступные методы, но и описание любых изменений в поведении внутри Aspose.Cells, которые могут повлиять на существующий код.

{{% /alert %}} 
## **Добавлено свойство MemorySetting для LoadOptions и WorkbookSettings.**
Начиная с версии v8.0.0 Aspose.Cells for Java, мы предоставили параметры использования памяти для улучшения производительности. Теперь свойство MemorySetting доступно в классах LoadOptions и WorkbookSettings.
### **Пример**
Демонстрирует, как читать файл Excel (большого размера) в оптимизированном режиме.

**Java**

{{< highlight csharp >}}

 //Initialize LoadOptions

LoadOptions options = new LoadOptions();

//Set memory preferences

options.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Instantiate the Workbook with an object of LoadOptions

Workbook book = new Workbook(myDir + "large.xlsx", options);

{{< /highlight >}}

Демонстрирует, как записать большой набор данных на лист в оптимизированном режиме.

**Java**

{{< highlight csharp >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences for WorkbookSettings

book.getSettings().setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Input large data into the cells

//.........

{{< /highlight >}}

{{% alert color="primary" %}} 

Пожалуйста, ознакомьтесь с подробной статьей по [Оптимизации использования памяти при работе с большими файлами, содержащими большие наборы данных](/cells/ru/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)

{{% /alert %}}
## **Изменилась реализации классов Row и Cell**
В предыдущих версиях объекты Row и Cell хранились в памяти для представления соответствующих строки и ячейки в рабочем листе. Тот же экземпляр возвращался, когда извлекался **RowCollection[int index]** или **Cells[int row, int column]**. В целях оптимизации памяти теперь в памяти будут храниться только свойства и данные Row и Cell. Следовательно, объекты Row и Cell стали оболочкой вышеперечисленных свойств.
### **Пример**
Демонстрирует, как сравнивать объекты Cell и Row отныне.

**Java**

{{< highlight csharp >}}

 //..

row1.equals(row2);


cell1.equals(cell2);

//..

{{< /highlight >}}

Поскольку объекты Row и Cell создаются в зависимости от вызова, они не будут храниться и управляться в памяти компонентом Cells. Поэтому после некоторых операций вставки и удаления индексы Row и Column могут не обновляться, или эти объекты могут стать недействительными.
### **Пример**
Например, следующий фрагмент кода будет возвращать недействительные результаты при использовании версии 8.0.0 и выше.

**Java**

{{< highlight csharp >}}

 Cell cell = cells.get("A2");

System.out.println(cell.getName() + ":" + cell.getValue());

cells.insertRange(CellArea.createCellArea("A1", "A1"), ShiftType.DOWN);

System.out.println(cell.getName() + ":" + cell.getValue());

{{< /highlight >}}

В новой версии объект Cell станет недействительным или будет ссылаться на ячейку A2 с нежелательным значением. Чтобы избежать такой ситуации, необходимо снова получить объекты Row или Cell из коллекции ячеек, чтобы получить правильный результат.

**Java**

{{< highlight csharp >}}

 Cell cell = cells.get("A2");

System.out.println(cell.getName() + ":" + cell.getValue());

cells.insertRange(CellArea.createCellArea("A1", "A1"), ShiftType.DOWN);

//Fetch the cell reference again

Cell cell = cells.get("A3");

System.out.println(cell.getName() + ":" + cell.getValue());

{{< /highlight >}}

{{% alert color="primary" %}} 

RowCollection больше не наследует CollectionBase, поскольку в его внутреннем списке нет объекта Row.

{{% /alert %}}
## **Изменено поведение метода Cell.StringValue**
В предыдущих версиях специальный шаблон _ игнорировался при форматировании значений ячеек, в то время как специальный символ * всегда давал один символ в отформатированном результате. С этой версии мы изменили логику обработки специальных символов _ и *, чтобы отформатированный результат соответствовал результату, полученному в приложении Excel. Например, пользовательский формат ячейки "_(\$* #,##0.00_)" для значения 123 ранее давал результат "$ 123.00". В новых версиях Cell.StringValue будет содержать результат "$123.00", что соответствует поведению приложения Excel при копировании ячейки в текст или экспорте в CSV.
## **Добавлено поле CreatedTime в PdfSaveOptions**
Теперь пользователи могут получить или установить время создания PDF при сохранении электронной таблицы в PDF с использованием класса PdfSaveOptions.
## **Добавлено свойство ShowFormulas для Worksheet**
Отныне пользователи могут использовать булево свойство ShowFormulas, предлагаемое классом Worksheet, для переключения между отображением формулы и значения на заданном рабочем листе.
## **Добавлена константа Ooxml к классу FileFormatType**
В класс FileFormatType добавлена новая константа Ooxml для представления зашифрованного файла Office Open XML, такого как XLSX, DOCX, PPTX и других.
## **Устарел класс FilterColumnCollection AutoFilter**
С Aspose.Cells for Java метод getFilterColumnCollection был помечен как устаревший. Рекомендуется использовать метод AuotFilter.getFilterColumns вместо него.
## **Заменено SeriesCollection.SecondCatergoryData на SeriesCollection.SecondCategoryData**
Мы исправили опечатку в имени метода SeriesCollection.getSecondCatergoryData. Теперь следует использовать метод SeriesCollection.getSecondCategoryData, а исходный метод SeriesCollection.getSecondCatergoryData помечен как устаревший.
{{< app/cells/assistant language="java" >}}
