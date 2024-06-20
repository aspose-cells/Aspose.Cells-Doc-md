---
title: Настройка параметров печати
type: docs
weight: 40
url: /ru/net/setting-print-options/
description: В этой статье показано, как программно установить параметры печати функции Настройка страницы листа Excel с использованием API и библиотеки .NET C#. Вы можете установить область печати, заголовки страниц и порядок страниц.
keywords: установить область печати Excel c#, установить заголовки печати Excel c#, установить порядок страниц Excel c#
---

{{% alert color="primary" %}}

Настройки страницы установки Microsoft Excel предоставляют несколько параметров печати (также называемых параметрами листа), которые позволяют пользователям контролировать порядок печати листов рабочей книги.

{{% /alert %}}

## **Установка параметров печати**

Эти параметры печати позволяют пользователям:

- Выбрать конкретную область печати на рабочем листе.
- Напечатать заголовки.
- Напечатать сетку.
- Печать верхних заголовков строк / столбцов.
- Достичь чернового качества.
- Напечатать примечания.
- Напечатать ошибки ячеек.
- Определить порядок страниц.

Aspose.Cells поддерживает все параметры печати, предлагаемые Microsoft Excel, и разработчики могут легко настраивать эти параметры для листов с помощью предлагаемых свойств класса [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup). Как использовать эти свойства, подробно обсуждается ниже.

### **Установка области печати**

По умолчанию область печати включает все области листа, содержащие данные. Разработчики могут установить конкретную область печати листа.

Чтобы выбрать конкретную область печати, используйте свойство [**PrintArea**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printarea) класса [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup). Назначьте этому свойству диапазон ячеек, определяющий область печати.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintArea-1.cs" >}}

### **Установка заголовков для печати**

Aspose.Cells позволяет определить повторение заголовков строк и столбцов на всех страницах напечатанного листа. Для этого используйте свойства [**PrintTitleColumns**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlecolumns) и [**PrintTitleRows**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlerows) класса [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup).

Строки или столбцы, которые будут повторяться, определяются путем передачи их номеров строки или столбца. Например, строки определяются как $1:$2, а столбцы определяются как $A:$B.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintTitle-1.cs" >}}

### **Настройка Других Опций Печати**

Класс [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) также предоставляет несколько других свойств для установки общих параметров печати:

- [**PrintGridlines**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printgridlines): булево свойство, определяющее, печатать сетку или нет.
- [**PrintHeadings**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printheadings): булевое свойство, определяющее, печатать заголовки строк и столбцов или нет.
- [**BlackAndWhite**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/blackandwhite): булево свойство, определяющее, печатать лист в черно-белом режиме или нет.
- [**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments): определяет, отображать ли примечания к печати на листе или в конце листа.
- [**PrintDraft**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printdraft): булево свойство, определяющее, печатать ли лист без графики.
- [**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors): определяет, следует ли печатать ошибки ячейки как отображаемые, пустые, тире или N/A.

Для установки свойств [**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) и [**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors) также Aspose.Cells предоставляет два перечисления, [**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype) и [**PrintErrorsType**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype), содержащие заранее определенные значения, которые нужно присвоить свойствам [**PrintComments**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) и [**PrintErrors**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors) соответственно.

Заранее определенные значения в перечислении [**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype) перечислены ниже вместе с их описаниями.

|**Типы Примечаний к Печати**|**Описание**|
| :- | :- |
|PrintInPlace|Указывает на печать комментариев как отображаемых в таблице.|
|PrintNoComments|Указывает, что комментарии не нужно печатать.|
|PrintSheetEnd|Указывает на печать комментариев в конце таблицы.|

Заранее определенные значения перечисления [**PrintErrorsType**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype) перечислены ниже вместе с их описаниями.



|**Типы Ошибок Печати**|**Описание**|
| :- | :- |
|PrintErrorsBlank|Указывает, что ошибки не нужно печатать.|
|PrintErrorsDash|Указывает на печать ошибок как "--".|
|PrintErrorsDisplayed|Указывает на печать ошибок как отображаемых.|
|PrintErrorsNA|Указывает на печать ошибок как "#N/A".|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-OtherPrintOptions-1.cs" >}}

### **Установить порядок страниц**

Класс [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) предоставляет свойство [**Order**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/order), которое используется для упорядочивания печати нескольких страниц вашей таблицы. Есть две возможности упорядочить страницы следующим образом:

- **Сначала вниз, затем вправо:** печатает все страницы вниз до печати любых страниц вправо.
- **Сначала вправо, затем вниз:** печатает страницы слева направо до печати страниц ниже.

Aspose.Cells предоставляет перечисление [**PrintOrderType**](https://reference.aspose.com/cells/net/aspose.cells/printordertype), содержащее все заранее определенные типы порядка.

Заранее определенные значения перечисления [**PrintOrderType**](https://reference.aspose.com/cells/net/aspose.cells/printordertype) перечислены ниже.

|**Типы порядка печати**|**Описание**|
| :- | :- |
|DownThenOver|Представляет порядок печати как сначала вниз, затем вправо.|
|OverThenDown|Представляет порядок печати как сначала вправо, затем вниз.|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPageOrder-1.cs" >}}
