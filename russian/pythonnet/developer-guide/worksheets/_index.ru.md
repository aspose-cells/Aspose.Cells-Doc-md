---
title: Управление листами рабочих книг Microsoft Excel.
linktitle: Рабочие листы
type: docs
weight: 90
url: /ru/python-net/manage-worksheets/
description: В этой статье показано, как управлять листами Microsoft Excel с помощью Aspose.Cells for Python via .NET API.
keywords: Библиотека Python Excel, Управление листами файлов Microsoft Excel на Python, Добавление листа на Python, Удаление листа на Python, Как добавить листы в новый файл Excel на Python, Как добавить листы в дизайнерскую электронную таблицу на Python, Как обратиться к листам по названию на Python, Как удалить листы по названию на Python, Как удалить листы по индексу на Python, Как активировать листы и сделать активной ячейку на Python.
---


{{% alert color="primary" %}}

Разработчики могут легко создавать и управлять листами в файлах Microsoft Excel программно, используя гибкий API Aspose.Cells. В этой теме описываются подходы к добавлению и удалению листов в файлах Microsoft Excel.

{{% /alert %}}

Aspose.Cells предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), который представляет файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/), которая позволяет получить доступ к каждому листу в файле Excel.

Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) предоставляет широкий спектр свойств и методов для управления листами.

## **Как добавить листы в новый файл Excel**

Для создания нового файла Excel программно:

1. Создайте объект класса [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook).
1. Вызовите метод [**add**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/add/#str) класса [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection). Пустой лист автоматически добавляется в файл Excel. Его можно ссылаться, передавая индекс листа нового листа в коллекцию [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/).
3. Получите ссылку на рабочий лист.
1. Выполнение работы с рабочими листами.
1. Сохраните новый файл Excel с новыми листами, вызвав метод [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) класса [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-AddingWorksheetsToNewExcelFile-1.py" >}}

## **Как добавить листы в дизайнерскую электронную таблицу**

Процесс добавления листов в дизайнерскую электронную таблицу такой же, как добавление нового листа, за исключением того, что файл Excel уже существует, поэтому должен быть открыт перед добавлением листов. Дизайнерскую электронную таблицу можно открыть с помощью класса [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-AddingWorksheetsToDesignerSpreadSheet-1.py" >}}

## **Как обратиться к листам по названию**

Получите доступ к любому листу, указав его имя или индекс.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-AccessingWorksheetsusingSheetName-1.py" >}}

## **Как удалить листы по названию**

Чтобы удалить листы из файла, вызовите метод [**remove_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/remove_by_name/#str) класса [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection). Передайте имя листа методу [**remove_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/remove_by_name/#str), чтобы удалить конкретный лист.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-RemovingWorksheetsUsingSheetName-1.py" >}}

## **Как удалить листы по индексу**

Удаление листов по названию хорошо работает, когда известно название листа. Если вы не знаете название листа, используйте метод [**remove_by_index**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/remove_by_index/#int), принимающий индекс листа вместо его названия.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-RemovingWorksheetsUsingSheetIndex-1.py" >}}

## **Как активировать листы и сделать активной ячейку в листе**

Иногда вам может понадобиться, чтобы определенный лист был активным и отображался, когда пользователь открывает файл Microsoft Excel в Excel. Точно так же вы можете активировать определенную ячейку и установить полосы прокрутки, чтобы показать активную ячейку.
Aspose.Cells способен выполнить все эти задачи.

Активный лист - это лист, над которым вы работаете: имя активного листа на вкладке жирным шрифтом по умолчанию.

Активная ячейка - это выбранная ячейка, в которую вводятся данные при начале набора текста. Одновременно может быть активна только одна ячейка. Активная ячейка выделяется толстой границей.

### **Как активировать листы и сделать активной ячейку**

Aspose.Cells предоставляет конкретные вызовы API для активации листа и ячейки. Например, свойство [**Aspose.Cells.WorksheetCollection.active_sheet_index**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/active_sheet_index/) полезно для установки активного листа в книге.
Точно так же свойство [**Aspose.Cells.Worksheet.active_cell**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/active_cell/) используется для установки и получения активной ячейки на листе.

Чтобы убедиться, что горизонтальные или вертикальные полосы прокрутки находятся в позиции строки и столбца, которую вы хотите показать, используйте свойства [**Aspose.Cells.Worksheet.first_visible_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/first_visible_row/) и [**Aspose.Cells.Worksheet.first_visible_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/first_visible_column/).

В следующем примере показано, как активировать лист и сделать активной ячейку. В сгенерированном выводе полосы прокрутки будут прокручены, чтобы сделать 2-ю строку и 2-й столбец первой видимой строкой и столбцом.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-MakeCellActive-1.py" >}}

