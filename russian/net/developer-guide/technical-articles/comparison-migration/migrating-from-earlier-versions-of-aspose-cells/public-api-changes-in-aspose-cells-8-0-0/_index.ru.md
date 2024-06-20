---
title: Изменения в общедоступном API в Aspose.Cells 8.0.0
type: docs
weight: 10
url: /ru/net/public-api-changes-in-aspose-cells-8-0-0/
---

{{% alert color="primary" %}} 

Эта страница перечисляет изменения в общедоступном API, которые были внесены в Aspose.Cells 8.0.0. Она включает не только новые и устаревшие общедоступные методы, но и описание любых изменений в поведении внутри Aspose.Cells, которые могут повлиять на существующий код.

{{% /alert %}} 
## **Добавлено свойство MemorySetting для LoadOptions и WorkbookSettings.**
Начиная с v8.0.0 Aspose.Cells for .NET мы предоставили параметры использования памяти для улучшения производительности. Свойство MemorySetting теперь доступно в классах LoadOptions и WorkbookSettings.
##### **Пример**
Демонстрирует, как читать файл Excel (большого размера) в оптимизированном режиме.

**C#**

{{< highlight csharp >}}

 //Initialize LoadOptions

LoadOptions options = new LoadOptions();

//Set memory preferences

options.MemorySetting = MemorySetting.MEMORY_PREFERENCE;

//Instantiate the Workbook with an object of LoadOptions

Workbook book = new Workbook(myDir + "large.xlsx", options);

{{< /highlight >}}

Демонстрирует, как записать большой набор данных на лист в оптимизированном режиме.

**C#**

{{< highlight csharp >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences for WorkbookSettings

book.Settings.MemorySetting = MemorySetting.MEMORY_PREFERENCE;

//Input large data into the cells

//.........

{{< /highlight >}}

{{% alert color="primary" %}} 

Пожалуйста, ознакомьтесь с подробной статьей по [Оптимизации использования памяти при работе с большими файлами с большими наборами данных](/cells/ru/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}}
## **Изменилась реализации классов Row и Cell**
В предыдущих версиях объекты Row и Cell хранились в памяти для представления соответствующих строки и ячейки в рабочем листе. Тот же экземпляр возвращался, когда извлекался **RowCollection[int index]** или **Cells[int row, int column]**. В целях оптимизации памяти теперь в памяти будут храниться только свойства и данные Row и Cell. Следовательно, объекты Row и Cell стали оболочкой вышеперечисленных свойств.
### **Пример**
Демонстрирует, как сравнивать объекты Cell и Row отныне.

**C#**

{{< highlight csharp >}}

 //..

row1.Equals(row2);


cell1.Equals(cell2);

//..

{{< /highlight >}}

Поскольку объекты Row и Cell создаются в зависимости от вызова, они не будут храниться и управляться в памяти компонентом Cells. Поэтому после некоторых операций вставки и удаления индексы Row и Column могут не обновляться, или эти объекты могут стать недействительными.
### **Пример**
Например, следующий фрагмент кода будет возвращать недействительные результаты при использовании версии 8.0.0 и выше.

**C#**

{{< highlight csharp >}}

 Cell cell = cells["A2"];

Console.WriteLine(cell.Name + ":" + cell.Value);

cells.InsertRange(CellArea.CreateCellArea("A1", "A1"), ShiftType.DOWN);

Console.WriteLine(cell.Name + ":" + cell.Value);

{{< /highlight >}}



В новой версии объект Cell станет недействительным или будет ссылаться на ячейку A2 с нежелательным значением. Чтобы избежать такой ситуации, необходимо снова получить объекты Row или Cell из коллекции ячеек, чтобы получить правильный результат.

**C#**

{{< highlight csharp >}}

 Cell cell = cells["A2"];

Console.WriteLine(cell.Name + ":" + cell.Value);

cells.InsertRange(CellArea.CreateCellArea("A1", "A1"), ShiftType.DOWN);

//Fetch the cell reference again

Cell cell = cells["A3"];

Console.WriteLine(cell.Name + ":" + cell.Value);

{{< /highlight >}}

{{% alert color="primary" %}} 

RowCollection больше не наследует CollectionBase, поскольку в его внутреннем списке нет объекта Row.

{{% /alert %}}
## **Изменено поведение метода Cell.StringValue**
В предыдущих версиях специальный шаблон _ игнорировался при форматировании значений ячеек, в то время как специальный символ * всегда приводил к одному символу в отформатированном результате. С этой версии мы изменили логику обработки специальных символов _ и * для того, чтобы сформированный результат совпадал с поведением приложения Excel. Например, пользовательский формат ячейки "_(\$* #,##0.00_)" использовался для представления значения 123 и давал результат "$ 123.00". В новых версиях Cell.StringValue будет содержать результат "$123.00", что соответствует поведению приложения Excel при копировании ячейки в текст или экспорте в CSV.
## **Добавлено поле CreatedTime в PdfSaveOptions**
Теперь пользователи могут получить или установить время создания PDF при сохранении электронной таблицы в PDF с использованием класса PdfSaveOptions.
## **Добавлено свойство ShowFormulas для Worksheet**
Отныне пользователи могут использовать логическое свойство ShowFormulas, предлагаемое Worksheet, для изменения отображения формул на значения в заданном листе Excel.
## **Добавлена константа Ooxml к классу FileFormatType**
В класс FileFormatType добавлена новая константа Ooxml для представления зашифрованного файла Office Open XML, такого как XLSX, DOCX, PPTX и других.
## **Устарел класс FilterColumnCollection AutoFilter**
С версии Aspose.Cells for Java, свойство FilterColumnCollection помечено как устаревшее, рекомендуется использовать свойство AuotFilter.FilterColumns вместо него.
## **Заменено SeriesCollection.SecondCatergoryData на SeriesCollection.SecondCategoryData**
Мы исправили опечатку в названии свойства SeriesCollection.SecondCatergoryData. Теперь вы можете использовать свойство SeriesCollection.SecondCategoryData, в то время как исходное свойство SeriesCollection.SecondCatergoryData помечено как устаревшее.
