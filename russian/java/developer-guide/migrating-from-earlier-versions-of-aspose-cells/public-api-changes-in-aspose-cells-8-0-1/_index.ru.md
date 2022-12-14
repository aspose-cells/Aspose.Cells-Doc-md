---
title: Общедоступный API Изменения в Aspose.Cells 8.0.1
type: docs
weight: 30
url: /ru/java/public-api-changes-in-aspose-cells-8-0-1/
---
{{% alert color="primary" %}} 

На этой странице перечислены общедоступные API изменения, внесенные в Aspose.Cells 8.0.1. Он включает в себя не только новые и устаревшие общедоступные методы, но и описание любых изменений в поведении за кулисами в Aspose.Cells, которые могут повлиять на существующий код. Любое введенное поведение, которое можно рассматривать как регрессию и которое изменяет существующее поведение, особенно важно и задокументировано здесь.

{{% /alert %}} 
## **Свойство MemorySetting добавлено в класс Cells**
Класс Cells предоставляет методы setMemorySetting и getMemorySetting, которые можно использовать для оптимизации использования памяти для данных ячеек и, следовательно, для снижения общей стоимости памяти. В следующем примере показано, как записать большие данные на лист в оптимизированном режиме.

**Java**

{{< highlight "csharp" >}}

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

 Параметры памяти не будут работать для листа по умолчанию, автоматически созданного рабочей книгой. Чтобы изменить настройки памяти существующих листов, примените настройки памяти вручную, прежде чем выполнять какие-либо манипуляции с данными.

{{% /alert %}} {{% alert color="primary" %}} 

 Пожалуйста, ознакомьтесь с подробной статьей о[Оптимизация памяти при работе с большими наборами данных](/cells/ru/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)

{{% /alert %}}
