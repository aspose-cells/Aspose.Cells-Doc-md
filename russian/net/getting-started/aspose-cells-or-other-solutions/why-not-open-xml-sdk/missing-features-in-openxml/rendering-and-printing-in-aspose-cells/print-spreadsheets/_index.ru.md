---
title: Печать электронных таблиц
type: docs
weight: 20
url: /ru/net/print-spreadsheets/
---
Параметры настройки страницы также предоставляют несколько параметров печати (также называемых параметрами листа), которые позволяют пользователям управлять распечатываемыми страницами рабочих листов. Эти параметры печати позволяют пользователям:

- Выберите определенную область печати рабочего листа
- Печать заголовков
- Печать линий сетки
- Печать заголовков строк/столбцов
- Достичь чернового качества
- Печать комментариев
- Печать Cell Ошибки
- Определить порядок страниц
  **Настройка параметров печати/листа**

Aspose.Cells поддерживает все эти параметры печати, и разработчики могут легко настроить эти параметры для нужных им рабочих листов, используя несколько свойств, предлагаемых классом PageSetup. Использование этих свойств класса PageSetup обсуждается ниже более подробно.
## **Установить область печати**
По умолчанию выбирается только та область печати, которая включает всю область рабочего листа, содержащую данные, но разработчики также могут установить конкретную область печати рабочего листа по своему желанию.

 Чтобы выбрать конкретную область печати, разработчики могут использовать set**Область печати** метод**Настройка страницы** учебный класс. Вы можете указать диапазон ячеек области печати этому методу в качестве аргумента.

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Specifying the cells range (from A1 cell to T35 cell) of the print area

pageSetup.PrintArea = "A1:T35";


{{< /highlight >}}
## **Установить заголовки для печати**
 Aspose.Cells позволяет указать заголовки строк и столбцов, которые должны повторяться на всех страницах печатного листа. Для этого разработчики могут использовать набор**PrintTitleColumns** а также**setPrintTitleRows** методы**Настройка страницы** учебный класс.

Строки или столбцы (которые должны повторяться на всех страницах печатного листа) определяются путем передачи их номеров строк или столбцов. Например, строки определяются как \$1:\$2, а столбцы определяются как \$A:\$B.

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

Aspose.Cells.PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Defining column numbers A & B as title columns

pageSetup.PrintTitleColumns = "$A:$B";

//Defining row numbers 1 & 2 as title rows

pageSetup.PrintTitleRows = "$1:$2";

{{< /highlight >}}
## **Установите другие параметры печати**
**Настройка страницы** Класс также предоставляет несколько других методов для установки общих параметров печати:

- **Метод setPrintGridline s** , этому методу передается логический параметр, который определяет, печатать или не печатать линии сетки.
- **метод setPrintHeadings** этому методу передается логический параметр, который определяет, печатать заголовки строк и столбцов или нет.
- **setBlackAndWhite метод** , этому методу передается логический параметр, который определяет, печатать ли лист в черно-белом режиме или нет.
- **метод setPrintComments** , определяет, отображать ли комментарии печати на рабочем листе или в конце рабочего листа
- **метод setPrintDraft** , этому методу передается логический параметр, который определяет, печатать лист в черновом качестве или нет.
- **метод setPrintErrors** , определяет, следует ли печатать ошибки ячеек как отображаемые, пустые, тире или Н/Д

 Чтобы использовать набор**ПечатьКомментарии** и установить**Ошибки печати** методы, Aspose.Cells также предоставляет два перечисления, PrintCommentsType и PrintErrorsType, которые содержат предварительно определенные значения, которые должны быть переданы как параметры для установки методов PrintComments и PrintErrors соответственно.

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Allowing to print gridlines

pageSetup.PrintGridlines = true;

//Allowing to print row/column headings

pageSetup.PrintHeadings = true;

//Allowing to print worksheet in black & white mode

pageSetup.BlackAndWhite = true;

//Allowing to print comments as displayed on worksheet

pageSetup.PrintComments = PrintCommentsType.PrintInPlace;

//Allowing to print worksheet with draft quality

pageSetup.PrintDraft = true;

//Allowing to print cell errors as N/A

pageSetup.PrintErrors = PrintErrorsType.PrintErrorsNA;

{{< /highlight >}}
## **Установить порядок страниц**
**Настройка страницы**Класс предоставляет метод set Order, который используется для заказа печати нескольких страниц вашего рабочего листа. Есть две возможности упорядочить страницы следующим образом:

Вниз, затем вверх, таким образом, он будет печатать все страницы вниз, прежде чем печатать страницы справа
Затем вниз, таким образом, он будет печатать страницы слева направо, прежде чем печатать страницы ниже.
Aspose.Cells предоставляет перечисление PrintOrderType, которое содержит все предварительно определенные типы заказов, которые должны быть назначены методу заказа setPage.

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Setting the printing order of the pages to over then down

pageSetup.Order = PrintOrderType.OverThenDown;

{{< /highlight >}}
## **Скачать пример кода**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Битбакет](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Print%20Spreadsheet%20with%20Options%20%28Aspose.Cells%29.zip)
