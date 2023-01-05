---
title: Общедоступный API Изменения в Aspose.Cells 8.0.1
type: docs
weight: 20
url: /ru/net/public-api-changes-in-aspose-cells-8-0-1/
---
{{% alert color="primary" %}} 

На этой странице перечислены общедоступные API изменения, внесенные в Aspose.Cells 8.0.1. Он включает в себя не только новые и устаревшие общедоступные методы, но и описание любых изменений в поведении за кулисами в Aspose.Cells, которые могут повлиять на существующий код. Любое введенное поведение, которое можно рассматривать как регрессию и которое изменяет существующее поведение, особенно важно и задокументировано здесь.

{{% /alert %}} 
## **Свойство MemorySetting добавлено в класс Cells**
Класс Cells предоставляет свойство MemorySetting, которое можно использовать для оптимизации использования памяти для данных ячеек и, следовательно, для снижения общей стоимости памяти. В следующем примере показано, как записать большие данные на лист в оптимизированном режиме.

**C#**

{{< highlight "csharp" >}}

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

Параметры памяти не будут работать для листа по умолчанию, автоматически созданного объектом Workbook. Чтобы изменить настройки памяти существующих листов, примените настройку памяти вручную, прежде чем выполнять какие-либо манипуляции с данными.

{{% alert color="primary" %}} 

 Пожалуйста, ознакомьтесь с подробной статьей о[Оптимизация памяти при работе с большими наборами данных](/cells/ru/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)

{{% /alert %}}
