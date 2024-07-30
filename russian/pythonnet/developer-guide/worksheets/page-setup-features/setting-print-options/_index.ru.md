---
title: Настройка параметров печати
type: docs
weight: 40
url: /ru/python-net/setting-print-options/
description: В этой статье показано, как программно настроить параметры печати функции настройки страниц Excel Worksheet с использованием API Aspose.Cells для Python via .NET. Вы можете установить область печати, заголовки печати и порядок страниц.
keywords: Библиотека Excel для Python, Установка области печати Excel в Python, Установка заголовков печати Excel в Python, Как настроить порядок страниц в Excel в Python, Как установить параметры печати в Python, Как установить область печати в Python, Как установить заголовки печати в Python. 
---

{{% alert color="primary" %}}

Настройки страницы установки Microsoft Excel предоставляют несколько параметров печати (также называемых параметрами листа), которые позволяют пользователям контролировать порядок печати листов рабочей книги.

{{% /alert %}}

## **Как настроить параметры печати**

Эти параметры печати позволяют пользователям:

- Выбрать конкретную область печати на рабочем листе.
- Напечатать заголовки.
- Напечатать сетку.
- Печать верхних заголовков строк / столбцов.
- Достичь чернового качества.
- Напечатать примечания.
- Напечатать ошибки ячеек.
- Определить порядок страниц.

Aspose.Cells для Python via .NET поддерживает все параметры печати, предлагаемые Microsoft Excel, и разработчики могут легко настроить эти параметры для листов, используя свойства, предлагаемые классом [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup). Как использовать эти свойства, обсуждается далее более подробно.

## **Как установить область печати**

По умолчанию область печати включает все области листа, содержащие данные. Разработчики могут установить конкретную область печати листа.

Чтобы выбрать конкретную область печати, используйте свойство [**print_area**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_area/) класса [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup). Назначьте этому свойству диапазон ячеек, определяющий область печати.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetPrintArea-1.py" >}}

## **Как установить заголовки печати**

Aspose.Cells для Python via .NET позволяет вам обозначить строки и столбцы заголовков, которые будут повторяться на всех страницах печатаемого листа. Для этого используйте свойства [**print_title_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_title_columns/) и [**print_title_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_title_rows) класса [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup).

Строки или столбцы, которые будут повторяться, определяются путем передачи их номеров строки или столбца. Например, строки определяются как $1:$2, а столбцы определяются как $A:$B.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetPrintTitle-1.py" >}}

## **Как настроить другие параметры печати**

Класс [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) также предоставляет несколько других свойств для установки общих параметров печати:

- [**print_grid_lines**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_gridlines/): булево свойство, определяющее, печатать сетку или нет.
- [**print_headings**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_headings/): булевое свойство, определяющее, печатать заголовки строк и столбцов или нет.
- [**black_and_white**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/black_and_white/): булево свойство, определяющее, печатать лист в черно-белом режиме или нет.
- [**print_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_comments/): определяет, отображать ли примечания к печати на листе или в конце листа.
- [**print_draft**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_draft/): булево свойство, определяющее, печатать ли лист без графики.
- [**print_errors**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_errors): определяет, следует ли печатать ошибки ячейки как отображаемые, пустые, тире или N/A.

Для установки свойств [**print_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_comments/) и [**print_errors**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_errors) также Aspose.Cells предоставляет два перечисления, [**PrintCommentsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printcommentstype) и [**PrintErrorsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printerrorstype), содержащие заранее определенные значения, которые нужно присвоить свойствам [**print_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_comments/) и [**print_errors**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_errors) соответственно.

Заранее определенные значения в перечислении [**PrintCommentsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printcommentstype) перечислены ниже вместе с их описаниями.

|**Типы Примечаний к Печати**|**Описание**|
| :- | :- |
|PRINT_IN_PLACE|Указывает печатать комментарии, как отображено на листе.|
|PRINT_NO_COMMENTS|Указывает не печатать комментарии.|
|PRINT_SHEET_END|Указывает печатать комментарии в конце листа.|

Заранее определенные значения перечисления [**PrintErrorsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printerrorstype) перечислены ниже вместе с их описаниями.



|**Типы Ошибок Печати**|**Описание**|
| :- | :- |
|PRINT_ERRORS_BLANK|Указывает не печатать ошибки.|
|PRINT_ERRORS_DASH|Указывает печатать ошибки как "--".|
|PRINT_ERRORS_DISPLAYED|Указывает печатать ошибки, как отображены.|
|PRINT_ERRORS_NA|Указывает печатать ошибки как "#N/A".|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-OtherPrintOptions-1.py" >}}

## **Как настроить порядок страниц**

Класс [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) предоставляет свойство [**Order**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/order), которое используется для упорядочивания печати нескольких страниц вашей таблицы. Есть две возможности упорядочить страницы следующим образом:

- **Сначала вниз, затем вправо:** печатает все страницы вниз до печати любых страниц вправо.
- **Сначала вправо, затем вниз:** печатает страницы слева направо до печати страниц ниже.

Aspose.Cells предоставляет перечисление [**PrintOrderType**](https://reference.aspose.com/cells/python-net/aspose.cells/printordertype), содержащее все заранее определенные типы порядка.

Заранее определенные значения перечисления [**PrintOrderType**](https://reference.aspose.com/cells/python-net/aspose.cells/printordertype) перечислены ниже.

|**Типы порядка печати**|**Описание**|
| :- | :- |
|DOWN_THEN_OVER|Представляет порядок печати: сначала вниз, затем вбок.|
|OVER_THEN_DOWN|Представляет порядок печати: сначала вбок, затем вниз.|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetPageOrder-1.py" >}}
