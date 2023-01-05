---
title: Управление рабочими листами
linktitle: Рабочие листы
type: docs
weight: 60
url: /ru/java/manage-worksheets/
---
{{% alert color="primary" %}}

Разработчики могут легко создавать рабочие листы в своих файлах Excel и управлять ими программно, используя гибкий API из Aspose.Cells. В этом разделе мы обсудим некоторые подходы к добавлению и удалению рабочих листов в файлах Excel.

{{% /alert %}}

Управление рабочими листами с использованием Aspose.Cells так же просто, как ABC. В этом разделе мы опишем, как мы можем:

1. Создайте новый файл Excel с нуля и добавьте в него рабочий лист.
1. Добавление рабочих листов в электронные таблицы конструктора
1. Доступ к рабочим листам с использованием имени листа
1. Удалить рабочий лист из файла Excel, используя его имя листа
1. Удалить рабочий лист из файла Excel, используя его индекс листа

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) который представляет файл Excel.[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) класс содержит[**Рабочий листКоллекция**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)который позволяет получить доступ к каждому рабочему листу в файле Excel.

 Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)Класс предоставляет широкий спектр свойств и методов для управления рабочим листом. Давайте посмотрим, как мы можем использовать этот базовый набор API.

## **Добавление рабочих листов в новый файл Excel**

 Чтобы программно создать новый файл Excel, разработчикам потребуется создать объект[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) класс, представляющий файл Excel. Затем разработчики могут позвонить[**Добавлять**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add() ) метод[**Рабочий листКоллекция**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) . Когда мы звоним[**Добавлять**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add() ) пустой рабочий лист автоматически добавляется в файл Excel, на который можно сослаться, передав индекс листа вновь добавленного рабочего листа в[**Рабочий листКоллекция**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) . После получения ссылки на рабочий лист разработчики могут работать со своими рабочими листами в соответствии со своими требованиями. После того, как работа над рабочими листами завершена, разработчики могут сохранить свой вновь созданный файл Excel с новыми рабочими листами, вызвав метод[**спасти**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions) ) метод[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)учебный класс.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoNewExcelFile-AddingWorksheetstoNewExcelFile.java" >}}

## **Добавление рабочих листов в электронную таблицу конструктора**

Процесс добавления рабочих листов в электронную таблицу дизайнера полностью аналогичен описанному выше подходу, за исключением того, что файл Excel уже создан, и нам нужно сначала открыть этот файл Excel, прежде чем добавлять в него рабочий лист. Таблицу дизайнера можно открыть, передав путь к файлу или поток при инициализации[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)учебный класс.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoDesignerSpreadsheet-AddingWorksheetstoDesignerSpreadsheet.java" >}}

## **Доступ к рабочим листам с использованием имени листа**

Разработчики могут получить доступ или получить любой рабочий лист, указав его имя или индекс.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AccessingWorksheetsusingSheetName-AccessingWorksheetsusingSheetName.java" >}}

## **Удаление рабочих листов с использованием имени листа**

 Иногда разработчикам может потребоваться удалить рабочие листы из существующих файлов Excel, и эту задачу можно выполнить, вызвав метод[**удалить в**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(java.lang.String) ) метод[**Рабочий листКоллекция**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) коллекция. Мы можем передать имя листа в[**удалить в**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(java.lang.String)) для удаления определенного рабочего листа.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetName-RemovingWorksheetsusingSheetName.java" >}}

## **Удаление рабочих листов с помощью индекса листов**

Приведенный выше подход к удалению рабочих листов хорошо работает, если разработчики уже знают имена листов, подлежащих удалению. Но что, если вы не знаете имя рабочего листа, который хотите удалить из файла Excel?

 Что ж, в таких условиях разработчики могут использовать перегруженную версию[**удалить в**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(int)), который принимает индекс рабочего листа вместо имени листа.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetIndex-RemovingWorksheetsusingSheetIndex.java" >}}

## **Предварительные темы**
- [Активация листов и активация Cell в рабочем листе](/cells/ru/java/activating-sheets-and-activating-a-cell-in-worksheet/)
- [Копировать и перемещать рабочие листы внутри и между рабочими книгами](/cells/ru/java/copy-and-move-worksheets-within-and-between-workbooks/)
- [Копирование и перемещение рабочих листов](/cells/ru/java/copying-and-moving-worksheets/)
- [Подсчитать количество ячеек на рабочем листе](/cells/ru/java/count-number-of-cells-in-the-worksheet/)
- [Обнаружение пустых листов](/cells/ru/java/detecting-empty-worksheets/)
- [Найдите, является ли рабочий лист диалоговым листом](/cells/ru/java/find-if-the-worksheet-is-dialog-sheet/)
- [Получить уникальный идентификатор рабочего листа](/cells/ru/java/get-worksheet-unique-id/)
- [Вставить фоновое изображение в Excel](/cells/ru/java/insert-background-image-to-excel/)
- [Создавайте, манипулируйте или удаляйте сценарии из рабочих листов](/cells/ru/java/create-manipulate-or-remove-scenarios-from-worksheets/)
- [Управление разрывами страниц](/cells/ru/java/managing-page-breaks/)
- [Особенности настройки страницы](/cells/ru/java/page-setup-features/)
- [Обновлять ссылки на других листах при удалении пустых столбцов и строк на листе](/cells/ru/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
- [Используйте свойство Sheet.SheetId OpenXml, используя Aspose.Cells](/cells/ru/java/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [Работа с фоном в файлах ODS](/cells/ru/java/working-with-background-in-ods-files/)
- [Представления рабочего листа](/cells/ru/java/worksheet-views/)
