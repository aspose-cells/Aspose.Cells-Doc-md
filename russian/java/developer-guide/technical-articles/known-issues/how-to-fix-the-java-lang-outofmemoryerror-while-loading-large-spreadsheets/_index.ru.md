---
title: Как исправить ошибку java.lang.OutOfMemoryError при загрузке больших электронных таблиц
type: docs
weight: 20
url: /ru/java/how-to-fix-the-java-lang-outofmemoryerror-while-loading-large-spreadsheets/
---
{{% alert color="primary" %}} 

 Есть большая вероятность, что конструктор Workbook может выдать ошибку java.lang.OutOfMemoryError при загрузке больших электронных таблиц. Это исключение говорит о том, что доступной памяти недостаточно для полной загрузки электронной таблицы в память, поэтому электронную таблицу необходимо загрузить, включив[Настройки памяти](/cells/ru/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}} 
## **Как исправить ошибку java.lang.OutOfMemoryError при загрузке большой электронной таблицы**
Aspose.Cells API-интерфейсы предоставляют настройки памяти для оптимизации потребления памяти при загрузке и обработке электронных таблиц. Эти параметры также полезны для эффективной загрузки больших электронных таблиц, содержащих огромные наборы данных, в объект Workbook, как показано ниже.

**Java**

{{< highlight "csharp" >}}

 //Specify the LoadOptions

LoadOptions options = new LoadOptions();

//Set the memory preferences

options.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Instantiate the Workbook

//Load the Big Excel file having large Data set in it

Workbook book = new Workbook("sample.xlsx", options);

{{< /highlight >}}
