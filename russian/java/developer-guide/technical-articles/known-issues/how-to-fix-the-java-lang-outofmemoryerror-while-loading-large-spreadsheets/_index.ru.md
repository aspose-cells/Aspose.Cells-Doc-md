---
title: Как исправить ошибку java.lang.OutOfMemoryError при загрузке больших электронных таблиц
type: docs
weight: 20
url: /ru/java/how-to-fix-the-java-lang-outofmemoryerror-while-loading-large-spreadsheets/
---

{{% alert color="primary" %}} 

Есть справедливые шансы того, что конструктор Workbook может вызвать java.lang.OutOfMemoryError при загрузке больших электронных таблиц. Это исключение указывает на то, что доступной памяти недостаточно для полной загрузки электронной таблицы в память, поэтому электронная таблица должна быть загружена с включенными [Предпочтениями памяти](/cells/ru/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}} 
## **Как исправить ошибку java.lang.OutOfMemoryError при загрузке больших электронных таблиц**
API Aspose.Cells предоставляют настройки памяти для оптимизации потребления памяти при загрузке и обработке электронных таблиц. Эти опции также полезны для эффективной загрузки больших электронных таблиц с огромными наборами данных в объект Workbook, как показано ниже. 

**Java**

{{< highlight csharp >}}

 //Specify the LoadOptions

LoadOptions options = new LoadOptions();

//Set the memory preferences

options.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Instantiate the Workbook

//Load the Big Excel file having large Data set in it

Workbook book = new Workbook("sample.xlsx", options);

{{< /highlight >}}
