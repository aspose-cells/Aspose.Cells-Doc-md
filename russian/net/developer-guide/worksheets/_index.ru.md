---
title: Управление листами рабочих книг Microsoft Excel.
linktitle: Рабочие листы
type: docs
weight: 90
url: /ru/net/manage-worksheets/
description: Добавление листа, удаление листа и активный лист с помощью Aspose.Cells.
---


{{% alert color="primary" %}}

Разработчики могут легко создавать и управлять листами в файлах Microsoft Excel программно, используя гибкий API Aspose.Cells. В этой теме описываются подходы к добавлению и удалению листов в файлах Microsoft Excel.

{{% /alert %}}

Aspose.Cells предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), который представляет файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets), которая позволяет получить доступ к каждому листу в файле Excel.

Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) предоставляет широкий спектр свойств и методов для управления листами.

## **Добавление рабочих листов в новый файл Excel**

Для создания нового файла Excel программно:

1. Создайте объект класса [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Вызовите метод [**Add**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/add) класса [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection). Пустой лист автоматически добавляется в файл Excel. Его можно ссылаться, передавая индекс листа нового листа в коллекцию [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets).
3. Получите ссылку на рабочий лист.
1. Выполнение работы с рабочими листами.
1. Сохраните новый файл Excel с новыми листами, вызвав метод [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) класса [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToNewExcelFile-1.cs" >}}

## **Добавление листов в дизайнерскую электронную таблицу**

Процесс добавления листов в дизайнерскую электронную таблицу такой же, как добавление нового листа, за исключением того, что файл Excel уже существует, поэтому должен быть открыт перед добавлением листов. Дизайнерскую электронную таблицу можно открыть с помощью класса [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToDesignerSpreadSheet-1.cs" >}}

## **Доступ к листам с использованием имени листа**

Получите доступ к любому листу, указав его имя или индекс.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AccessingWorksheetsusingSheetName-1.cs" >}}

## **Удаление листов с использованием имени листа**

Чтобы удалить листы из файла, вызовите метод [**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat/index) класса [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection). Передайте имя листа методу [**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells.worksheetcollection/removeat/methods/1), чтобы удалить конкретный лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetName-1.cs" >}}

## **Удаление рабочих листов с использованием индекса листа.**

Удаление листов по имени хорошо работает, когда известно имя листа. Если вы не знаете имя листа, используйте перегруженную версию метода [**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat), который принимает индекс листа вместо его имени.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetIndex-1.cs" >}}

## **Активация листов и установка активной ячейки на листе**

Иногда вам может понадобиться, чтобы определенный лист был активным и отображался, когда пользователь открывает файл Microsoft Excel в Excel. Точно так же вы можете активировать определенную ячейку и установить полосы прокрутки, чтобы показать активную ячейку.
Aspose.Cells способен выполнить все эти задачи.

Активный лист - это лист, над которым вы работаете: имя активного листа на вкладке жирным шрифтом по умолчанию.

Активная ячейка - это выбранная ячейка, в которую вводятся данные при начале набора текста. Одновременно может быть активна только одна ячейка. Активная ячейка выделяется толстой границей.

### **Активация листов и установка активной ячейки**

Aspose.Cells предоставляет конкретные вызовы API для активации листа и ячейки. Например, свойство [**Aspose.Cells.WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/activesheetindex) полезно для установки активного листа в книге.
Точно так же свойство [**Aspose.Cells.Worksheet.ActiveCell**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/activecell) используется для установки и получения активной ячейки на листе.

Чтобы убедиться, что горизонтальные или вертикальные полосы прокрутки находятся в позиции строки и столбца, которую вы хотите показать, используйте свойства [**Aspose.Cells.Worksheet.FirstVisibleRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblerow) и [**Aspose.Cells.Worksheet.FirstVisibleColumn**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblecolumn).

В следующем примере показано, как активировать лист и сделать активной ячейку. В сгенерированном выводе полосы прокрутки будут прокручены, чтобы сделать 2-ю строку и 2-й столбец первой видимой строкой и столбцом.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-MakeCellActive-1.cs" >}}

## **Продвинутые темы**
- [Копирование и перемещение листов](/cells/ru/net/copying-and-moving-worksheets/)
- [Посчитать количество ячеек в листе](/cells/ru/net/count-number-of-cells-in-the-worksheet/)
- [Обнаружение пустых листов](/cells/ru/net/detecting-empty-worksheets/)
- [Определить, является ли рабочий лист диалоговым листом](/cells/ru/net/find-if-the-worksheet-is-dialog-sheet/)
- [Получить уникальный идентификатор листа](/cells/ru/net/get-worksheet-unique-id/)
- [Создание, изменение или удаление сценариев из листов](/cells/ru/net/create-manipulate-or-remove-scenarios-from-worksheets/)
- [Управление разрывами страницы](/cells/ru/net/managing-page-breaks/)
- [Возможности настройки страницы](/cells/ru/net/page-setup-features/)
- [Печать нескольких копий листа книги Excel](/cells/ru/net/print-multiple-copies-of-a-worksheet/)
- [Использование свойства Sheet.SheetId из OpenXml с помощью Aspose.Cells](/cells/ru/net/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [Просмотр листов](/cells/ru/net/worksheet-views/)

{{< app/cells/assistant language="csharp" >}}
