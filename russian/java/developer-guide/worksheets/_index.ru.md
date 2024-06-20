---
title: Управление рабочими листами
linktitle: Рабочие листы
type: docs
weight: 60
url: /ru/java/manage-worksheets/
---

{{% alert color="primary" %}}

Разработчики могут легко создавать и управлять листами в своих файлах Excel программным образом, используя гибкий API Aspose.Cells. В этой теме мы обсудим некоторые подходы к добавлению и удалению листов в файлах Excel.

{{% /alert %}}

Управление листами с использованием Aspose.Cells так же просто, как раз, два. В этом разделе мы опишем, как мы можем:

1. Создать новый файл Excel с нуля и добавить в него лист
1. Добавить листы к дизайнерским электронным таблицам
1. Обращение к листам по имени листа
1. Удалить лист из файла Excel, используя его имя листа
1. Удалить лист из файла Excel, используя его индекс листа

Aspose.Cells предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), который представляет собой файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) содержит [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection), позволяющий получить доступ к каждому листу в файле Excel.

Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) предоставляет широкий спектр свойств и методов для управления листом. Давайте посмотрим, как мы можем использовать этот базовый набор API.

## **Добавление рабочих листов в новый файл Excel**

Для создания нового файла Excel программно разработчикам потребуется создать объект класса [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), представляющий файл Excel. Затем разработчики могут вызвать метод [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add--) объекта [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection). При вызове метода [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add--) в файл Excel автоматически добавляется пустой лист, на который можно сослаться, передав индекс листа вновь добавленного листа объекту [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection). После получения ссылки на лист разработчики могут работать с их листами в соответствии с их требованиями. После завершения работы с листами, разработчики могут сохранить созданный ими файл Excel с новыми листами, вызвав метод [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) объекта [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoNewExcelFile-AddingWorksheetstoNewExcelFile.java" >}}

## **Добавление листов в дизайнерскую электронную таблицу**

Процесс добавления листов в дизайнерскую таблицу тот же самый, что и в вышеуказанном подходе, за исключением того, что файл Excel уже создан, и перед добавлением листа в него сначала нужно открыть этот файл Excel. Дизайнерскую таблицу можно открыть, передавая путь к файлу или поток при инициализации класса [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoDesignerSpreadsheet-AddingWorksheetstoDesignerSpreadsheet.java" >}}

## **Доступ к листам с использованием имени листа**

Разработчики могут получить доступ к любому листу, указав его имя или индекс.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AccessingWorksheetsusingSheetName-AccessingWorksheetsusingSheetName.java" >}}

## **Удаление листов с использованием имени листа**

Иногда разработчикам может потребоваться удалить листы из существующих файлов Excel, и эту задачу можно выполнить, вызвав метод [**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(java.lang.String)) коллекции [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection). Мы можем передать имя листа методу [**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(java.lang.String)) для удаления конкретного листа.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetName-RemovingWorksheetsusingSheetName.java" >}}

## **Удаление рабочих листов с использованием индекса листа.**

Вышеуказанный подход к удалению листов работает хорошо, если разработчики уже знают имена листов, которые нужно удалить. Но что, если вы не знаете имени листа, который вы хотите удалить из своего файла Excel?

Ну, в таких случаях разработчики могут использовать перегруженную версию метода [**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(int)), которая принимает индекс листа вместо его имени листа.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetIndex-RemovingWorksheetsusingSheetIndex.java" >}}

## **Продвинутые темы**
- [Активация листов и активация ячейки в листе](/cells/ru/java/activating-sheets-and-activating-a-cell-in-worksheet/)
- [Копирование и перемещение листов внутри и между книгами](/cells/ru/java/copy-and-move-worksheets-within-and-between-workbooks/)
- [Копирование и перемещение листов](/cells/ru/java/copying-and-moving-worksheets/)
- [Посчитать количество ячеек в листе](/cells/ru/java/count-number-of-cells-in-the-worksheet/)
- [Обнаружение пустых листов](/cells/ru/java/detecting-empty-worksheets/)
- [Определить, является ли рабочий лист диалоговым листом](/cells/ru/java/find-if-the-worksheet-is-dialog-sheet/)
- [Получить уникальный идентификатор листа](/cells/ru/java/get-worksheet-unique-id/)
- [Добавление фонового изображения в Excel](/cells/ru/java/insert-background-image-to-excel/)
- [Создание, изменение или удаление сценариев из листов](/cells/ru/java/create-manipulate-or-remove-scenarios-from-worksheets/)
- [Управление разрывами страницы](/cells/ru/java/managing-page-breaks/)
- [Возможности настройки страницы](/cells/ru/java/page-setup-features/)
- [Обновление ссылок в других листах при удалении пустых столбцов и строк на листе](/cells/ru/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
- [Использование свойства Sheet.SheetId из OpenXml с помощью Aspose.Cells](/cells/ru/java/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [Работа с фоном в файлах ODS](/cells/ru/java/working-with-background-in-ods-files/)
- [Просмотр листов](/cells/ru/java/worksheet-views/)
