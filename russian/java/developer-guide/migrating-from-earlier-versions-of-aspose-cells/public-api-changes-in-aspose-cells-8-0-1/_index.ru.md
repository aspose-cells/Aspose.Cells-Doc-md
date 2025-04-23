---
title: Изменения в общедоступном API в Aspose.Cells 8.0.1
type: docs
weight: 30
url: /ru/java/public-api-changes-in-aspose-cells-8-0-1/
---

{{% alert color="primary" %}} 

Эти страницы перечисляют общедоступные изменения в API, которые были введены в Aspose.Cells 8.0.1. Здесь описаны не только новые и устаревшие общедоступные методы, но также изменения в поведении за кулисами в Aspose.Cells, которые могут повлиять на существующий код. Любое изменение поведения, которое могло бы быть рассмотрено как регрессия и изменяет существующее поведение, особенно важно, и здесь документировано.

{{% /alert %}} 
## **Добавлено свойство MemorySetting в класс Cells**
В классе Cells появились методы setMemorySetting и getMemorySetting, которые могут использоваться для оптимизации использования памяти для данных ячеек, и, следовательно, снижения общей стоимости памяти. В следующем примере показано, как записать большие данные на лист в оптимизированном режиме.

**Java**

{{< highlight csharp >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences

book.getSettings().setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//To change the memory setting of existing sheets, please change memory setting for them manually:

Cells cells = book.getWorksheets().get(0).getCells();

cells.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Input large dataset into the cells of the worksheet.

//Your code goes here

{{< /highlight >}}

{{% alert color="primary" %}} 

Настройки памяти не будут работать для листа по умолчанию, автоматически созданного Workbook. Для изменения настроек памяти существующих листов, примените настройки памяти вручную перед выполнением любой манипуляции с данными. 

{{% /alert %}} {{% alert color="primary" %}} 

Пожалуйста, ознакомьтесь со подробной статьей по теме [Оптимизация памяти при работе с большими наборами данных](/cells/ru/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
