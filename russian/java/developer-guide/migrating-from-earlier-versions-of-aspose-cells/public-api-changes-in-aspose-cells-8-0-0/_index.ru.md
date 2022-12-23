---
title: Общедоступный API Изменения в Aspose.Cells 8.0.0
type: docs
weight: 20
url: /ru/java/public-api-changes-in-aspose-cells-8-0-0/
---
{{% alert color="primary" %}} 

На этой странице перечислены общедоступные API изменения, внесенные в Aspose.Cells 8.0.0. Он включает в себя не только новые и устаревшие публичные методы, но и описание любых изменений поведения за кулисами в Aspose.Cells, которые могут повлиять на существующий код.

{{% /alert %}} 
## **Добавлен MemorySetting в LoadOptions и WorkbookSettings**
Начиная с версии 8.0.0 версии Aspose.Cells for Java мы предоставили параметры использования памяти для повышения производительности. Свойство MemorySetting теперь доступно в классах LoadOptions и WorkbookSettings.
### **Пример**
Демонстрирует, как читать файл Excel (имеющий большой размер) в оптимизированном режиме.

**Java**

{{< highlight "csharp" >}}

 //Initialize LoadOptions

LoadOptions options = new LoadOptions();

//Set memory preferences

options.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Instantiate the Workbook with an object of LoadOptions

Workbook book = new Workbook(myDir + "large.xlsx", options);

{{< /highlight >}}

Демонстрирует, как записать большой набор данных на лист в оптимизированном режиме.

**Java**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences for WorkbookSettings

book.getSettings().setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Input large data into the cells

//.........

{{< /highlight >}}

{{% alert color="primary" %}} 

 Пожалуйста, ознакомьтесь с подробной статьей о[Оптимизация памяти при работе с большими файлами](/cells/ru/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)с.

{{% /alert %}}
## **Реализации Row & Cell изменились**
 В предыдущих версиях объекты Row и Cell хранились в памяти для представления соответствующей строки и ячейки на рабочем листе. Тот же экземпляр возвращался всякий раз, когда**RowCollection[целый индекс]** или же**Cells [целая строка, целая колонка]** были извлечены. Из соображений производительности памяти теперь в памяти будут храниться только свойства и данные строки и Cell. Следовательно, объект Row & Cell стал оболочкой вышеупомянутых свойств.
### **Пример**
Демонстрирует, как теперь сравнивать объекты Cell и Row.

**Java**

{{< highlight "csharp" >}}

 //..

row1.equals(row2);


cell1.equals(cell2);

//..

{{< /highlight >}}

Поскольку экземпляры объектов Row и Cell создаются в соответствии с вызовом, они не будут храниться и управляться в памяти компонентом Cells. Поэтому после некоторых операций вставки и удаления индексы строк и столбцов могут не обновляться или, что еще хуже, эти объекты становятся недействительными.
### **Пример**
Например, следующий фрагмент кода вернет неверные результаты при использовании версии 8.0.0 и выше.

**Java**

{{< highlight "csharp" >}}

 Cell cell = cells.get("A2");

System.out.println(cell.getName() + ":" + cell.getValue());

cells.insertRange(CellArea.createCellArea("A1", "A1"), ShiftType.DOWN);

System.out.println(cell.getName() + ":" + cell.getValue());

{{< /highlight >}}

В новой версии объект Cell станет недействительным или будет ссылаться на A2 с каким-то нежелательным значением. Чтобы избежать такой ситуации, снова получите объекты Row или Cell из коллекции ячеек, чтобы получить правильный результат.

**Java**

{{< highlight "csharp" >}}

 Cell cell = cells.get("A2");

System.out.println(cell.getName() + ":" + cell.getValue());

cells.insertRange(CellArea.createCellArea("A1", "A1"), ShiftType.DOWN);

//Fetch the cell reference again

Cell cell = cells.get("A3");

System.out.println(cell.getName() + ":" + cell.getValue());

{{< /highlight >}}

{{% alert color="primary" %}} 

RowCollection больше не наследует CollectionBase, потому что в его внутреннем списке нет объекта Row.

{{% /alert %}}
## **Cell. Поведение StringValue изменено**
 В предыдущих версиях специальный шаблон_игнорировался при форматировании значений ячеек, где специальный символ * всегда приводил к одному символу в отформатированном результате. Начиная с этой версии, мы изменили логику обработки специальных символов._ и* чтобы отформатированный результат был таким же, как в приложении Excel. Например, пользовательский формат ячейки "_(\$* #,##0.00_)", используемое для представления значения 123, дало результат как "123,00 долларов США". В новых версиях Cell.StringValue будет содержать результат как "123,00 долларов США", что является тем же поведением, что и приложение Excel при копировании ячейки. в текст или экспортировать на номер CSV.
## **Добавлено CreatedTime в PdfSaveOptions**
Теперь пользователи могут получить или установить время создания PDF при сохранении электронной таблицы в PDF при использовании класса PdfSaveOptions.
## **Добавлен ShowFormulas на рабочий лист**
Отныне пользователи могут использовать логическое свойство ShowFormulas, предлагаемое Worksheet, для переключения представления между формулой и значением данного рабочего листа.
## **Добавлен Ooxml в FileFormatType**
В класс FileFormatType добавлена новая константа Ooxml для представления зашифрованного открытого XML-файла Office, например XLSX, DOCX, PPTX и других.
## **Устаревшая коллекция FilterColumnCollection для AutoFilter**
С номером Aspose.Cells for Java метод getFilterColumnCollection помечен как устаревший. Вместо этого предлагается использовать метод AuotFilter.getFilterColumns.
## **Заменен SeriesCollection.SecondCategoryData на SeriesCollection.SecondCategoryData.**
Мы в основном исправили опечатку в имени метода для SeriesCollection.getSecondCategoryData. Теперь вы можете использовать метод SeriesCollection.getSecondCategoryData, тогда как исходный метод SeriesCollection.getSecondCategoryData был помечен как устаревший.
