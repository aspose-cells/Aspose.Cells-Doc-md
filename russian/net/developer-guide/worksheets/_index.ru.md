---
title: Управление рабочими листами Microsoft файлов Excel.
linktitle: Рабочие листы
type: docs
weight: 90
url: /ru/net/manage-worksheets/
description: Добавить рабочий лист, удалить рабочий лист и активный лист, используя Aspose.Cells.
---
{{% alert color="primary" %}}

Разработчики могут легко создавать рабочие листы в файлах Excel Microsoft и управлять ими программно, используя Aspose.Cells' гибкий API. В этом разделе описываются подходы к добавлению и удалению рабочих листов в файлах Excel Microsoft.

{{% /alert %}}

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) который представляет файл Excel.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook)класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel.

 Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)Класс предоставляет широкий спектр свойств и методов для управления рабочими листами.

## **Добавление рабочих листов в новый файл Excel**

Чтобы создать новый файл Excel программно:

1.  Создайте объект из[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook)учебный класс.
1.  Позвоните[**Добавлять**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/add) метод[**Рабочий листКоллекция**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) учебный класс. Пустой рабочий лист автоматически добавляется в файл Excel. На него можно сослаться, передав индекс листа нового рабочего листа в[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) коллекция.
1. Получите ссылку на рабочий лист.
1. Выполнить работу с рабочими листами.
1.  Сохраните новый файл Excel с новыми рабочими листами, вызвав[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) учебный класс'[**Сохранять**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)метод.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToNewExcelFile-1.cs" >}}

## **Добавление рабочих листов в электронную таблицу конструктора**

 Процесс добавления рабочих листов в электронную таблицу конструктора такой же, как и добавление нового рабочего листа, за исключением того, что файл Excel уже существует, поэтому его следует открыть перед добавлением рабочих листов. Таблицу конструктора можно открыть с помощью[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook)учебный класс.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToDesignerSpreadSheet-1.cs" >}}

## **Доступ к рабочим листам с использованием имени листа**

Получите доступ к любому рабочему листу, указав его имя или индекс.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AccessingWorksheetsusingSheetName-1.cs" >}}

## **Удаление рабочих листов с использованием имени листа**

Чтобы удалить рабочие листы из файла, вызовите метод[**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat/index) метод[**Рабочий листКоллекция**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) учебный класс. Передайте имя листа в[**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells.worksheetcollection/removeat/methods/1)способ удаления определенного рабочего листа.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetName-1.cs" >}}

## **Удаление рабочих листов с помощью индекса листов**

 Удаление рабочих листов по имени хорошо работает, когда известно имя рабочего листа. Если вы не знаете имя рабочего листа, используйте перегруженную версию[**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat)метод, который принимает индекс листа рабочего листа вместо его имени листа.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetIndex-1.cs" >}}

## **Активация листов и создание активного Cell на рабочем листе**

Иногда вам нужно, чтобы определенный рабочий лист был активным и отображался, когда пользователь открывает файл Excel Microsoft в Excel. Точно так же вы можете захотеть активировать определенную ячейку и настроить полосы прокрутки для отображения активной ячейки.
Aspose.Cells способен выполнять все эти задачи.

 Ан**активный лист** — это лист, над которым вы работаете: имя активного листа на вкладке по умолчанию выделено полужирным шрифтом.

 Ан**активная ячейка** — это выбранная ячейка, ячейка, в которую вводятся данные, когда вы начинаете печатать. Одновременно активна только одна ячейка. Активная ячейка выделена жирной рамкой.

### **Активация листов и активация Cell**

Aspose.Cells предоставляет специальные вызовы API для активации листа и ячейки. Например,[**Aspose.Cells.WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/activesheetindex)Свойство полезно для установки активного листа в книге.
Сходным образом,[**Aspose.Cells.Worksheet.ActiveCell**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/activecell)Свойство используется для установки и получения активной ячейки на листе.

Чтобы убедиться, что горизонтальные или вертикальные полосы прокрутки находятся в позиции индекса строки и столбца, в которой вы хотите отобразить определенные данные, используйте[**Aspose.Cells.Worksheet.FirstVisibleRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblerow) а также[**Aspose.Cells.Worksheet.FirstVisibleColumn**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblecolumn)характеристики.

В следующем примере показано, как активировать рабочий лист и сделать в нем активную ячейку. В сгенерированном выводе полосы прокрутки будут прокручиваться, чтобы сделать 2-ю строку и 2-й столбец их первой видимой строкой и столбцом.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-MakeCellActive-1.cs" >}}

## **Предварительные темы**
- [Копирование и перемещение рабочих листов](/cells/ru/net/copying-and-moving-worksheets/)
- [Подсчитать количество ячеек на рабочем листе](/cells/ru/net/count-number-of-cells-in-the-worksheet/)
- [Обнаружение пустых листов](/cells/ru/net/detecting-empty-worksheets/)
- [Найдите, является ли рабочий лист диалоговым листом](/cells/ru/net/find-if-the-worksheet-is-dialog-sheet/)
- [Получить уникальный идентификатор рабочего листа](/cells/ru/net/get-worksheet-unique-id/)
- [Создавайте, манипулируйте или удаляйте сценарии из рабочих листов](/cells/ru/net/create-manipulate-or-remove-scenarios-from-worksheets/)
- [Управление разрывами страниц](/cells/ru/net/managing-page-breaks/)
- [Особенности настройки страницы](/cells/ru/net/page-setup-features/)
- [Печать нескольких копий рабочего листа](/cells/ru/net/print-multiple-copies-of-a-worksheet/)
- [Используйте свойство Sheet.SheetId OpenXml, используя Aspose.Cells](/cells/ru/net/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [Представления рабочего листа](/cells/ru/net/worksheet-views/)

