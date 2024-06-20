---
title: Управление рабочими листами
type: docs
weight: 10
url: /ru/python-java/manage-worksheets/
---

Управление листами с использованием Aspose.Cells для Python via Java очень просто. В этой статье мы продемонстрируем добавление, доступ и удаление листов с использованием API Aspose.Cells.
## **Добавление рабочих листов в новый файл Excel**
Чтобы создать новую книгу, создайте объект класса [Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workbook). Класс [Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workbook) представляет файл Excel. Затем, используя метод [add](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#add\(\)) класса [WorksheetCollection](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection), добавьте новые листы в файл Excel. Наконец, чтобы сохранить вновь созданный файл Excel, вызовите метод [save](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String\)) класса [Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workbook).

В следующем фрагменте кода показано, как создать новый файл Excel и добавить в него лист.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToNewExcelFile.py" >}}
## **Добавление листов в дизайнерскую электронную таблицу**
Добавление листов в дизайнерскую электронную таблицу точно такое же, как добавление листа в новый файл Excel. Единственное отличие заключается в том, что вместо создания нового файла Excel мы открываем существующий файл с помощью класса [Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workbook).

В следующем фрагменте кода показано, как добавить лист в дизайнерскую электронную таблицу.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToDesignerSpreadsheet.py" >}}
## **Доступ к листам с использованием имени листа**
После загрузки книги разработчики могут получить доступ к любому листу, используя его индекс или имя. В следующем фрагменте кода показан доступ к листу с использованием его имени.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AccessingWorksheetsUsingSheetName.py" >}}
## **Удаление листов**
Могут возникнуть ситуации, когда некоторые листы нужно удалить из книги. Для этого API предоставляет метод [WorksheetCollection.removeAt](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#removeAt\(int\)). Вы можете передать индекс листа или имя листа, который нужно удалить. В следующих примерах показано удаление листов с использованием индекса листа и имени листа.
### **Удаление листов с использованием индекса листа**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetIndex.py" >}}
### **Удаление листов с использованием имени листа**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetName.py" >}}
