---
title: Управление рабочими листами
type: docs
weight: 10
url: /ru/python-java/manage-worksheets/
---
Управлять рабочими листами с помощью Aspose.Cells for Python via Java очень просто. В этой статье мы продемонстрируем добавление, доступ и удаление рабочих листов с помощью файла Aspose.Cells API.
## **Добавление рабочих листов в новый файл Excel**
 Чтобы создать новую рабочую книгу, создайте объект[Рабочая тетрадь](https://reference.aspose.com/cells/python/asposecells.api/Workbook) учебный класс.[Рабочая тетрадь](https://reference.aspose.com/cells/python/asposecells.api/Workbook) класс представляет файл Excel. Затем с помощью[Добавлять](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#add\(\) ) метод[Рабочий листКоллекция](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection) , в файл Excel добавляются новые рабочие листы. Наконец, чтобы сохранить только что созданный файл Excel, вызовите метод[спасти](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String\) ) метод[Рабочая тетрадь](https://reference.aspose.com/cells/python/asposecells.api/Workbook)учебный класс.

В следующем фрагменте кода показано создание нового файла Excel и добавление в него рабочего листа.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToNewExcelFile.py" >}}
## **Добавление рабочих листов в электронную таблицу конструктора**
Добавление рабочих листов в электронную таблицу конструктора точно такое же, как добавление рабочего листа в новый файл Excel. Единственное отличие состоит в том, что вместо создания нового файла Excel мы открываем существующий файл по[Рабочая тетрадь](https://reference.aspose.com/cells/python/asposecells.api/Workbook)учебный класс.

В следующем фрагменте кода показано добавление рабочего листа в электронную таблицу конструктора.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToDesignerSpreadsheet.py" >}}
## **Доступ к рабочим листам с использованием имени листа**
После загрузки рабочей книги разработчики могут получить доступ к любому рабочему листу, используя его индекс или имя. Следующий фрагмент кода демонстрирует доступ к рабочему листу по его имени.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AccessingWorksheetsUsingSheetName.py" >}}
## **Удаление рабочих листов**
Могут быть случаи, когда некоторые листы встречаются, чтобы быть удаленными из книги. Для этого API предоставляет[WorksheetCollection.removeAt](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#removeAt\(int\)) метод. Вы можете передать ему индекс листа или имя листа, который нужно удалить. В следующих примерах показано удаление рабочих листов с использованием индекса и имени листа.
### **Удаление рабочих листов с помощью индекса листов**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetIndex.py" >}}
### **Удаление рабочих листов с использованием имени листа**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetName.py" >}}
