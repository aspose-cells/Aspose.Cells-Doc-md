---
title: Изменения в общедоступном API в Aspose.Cells 8.0.1
type: docs
weight: 20
url: /ru/net/public-api-changes-in-aspose-cells-8-0-1/
---

{{% alert color="primary" %}} 

Эти страницы перечисляют общедоступные изменения в API, которые были введены в Aspose.Cells 8.0.1. Здесь описаны не только новые и устаревшие общедоступные методы, но также изменения в поведении за кулисами в Aspose.Cells, которые могут повлиять на существующий код. Любое изменение поведения, которое могло бы быть рассмотрено как регрессия и изменяет существующее поведение, особенно важно, и здесь документировано.

{{% /alert %}} 
## **Добавлено свойство MemorySetting в класс Cells**
Класс Cells теперь содержит свойство MemorySetting, которое может использоваться для оптимизации использования памяти для данных ячеек и уменьшения общего объема памяти. В следующем примере показано, как записать большой объем данных на лист в оптимизированном режиме.

**C#**

{{< highlight csharp >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences

book.Settings.MemorySetting = MemorySetting.MemoryPreference;

//To change the memory setting of existing sheets, please change memory setting for them manually:

Cells cells = book.Worksheets[0].Cells;

cells.MemorySetting = MemorySetting.MemoryPreference;

//Input large dataset into the cells of the worksheet

//Your code goes here

{{< /highlight >}}

Настройки памяти не будут работать для листа, созданного автоматически объектом Workbook. Чтобы изменить настройки памяти существующих листов, примените настройки памяти вручную перед выполнением любых манипуляций с данными.

{{% alert color="primary" %}} 

Пожалуйста, ознакомьтесь со статьей [Оптимизация использования памяти при работе с большими наборами данных](/cells/ru/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
