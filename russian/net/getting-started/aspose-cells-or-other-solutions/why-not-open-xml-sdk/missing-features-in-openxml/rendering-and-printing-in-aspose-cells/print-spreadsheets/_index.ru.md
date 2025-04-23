---
title: Печать таблиц
type: docs
weight: 20
url: /ru/net/print-spreadsheets/
---

Настройки страницы также предоставляют несколько параметров печати (также называемых параметрами листа), которые позволяют пользователям управлять распечатываемыми страницами листов. Эти параметры печати позволяют пользователям:

- Выбрать конкретную область печати на листе
- Печатать заголовки
- Печатать сетку
- Печатать заголовки строк/столбцов
- Достигнуть чернового качества
- Печатать комментарии
- Печатать ошибки ячеек
- Определить порядок страниц
  **Установка параметров печати/листа**

Aspose.Cells поддерживает все эти параметры печати, и разработчики могут легко настраивать эти параметры для своих желаемых листов с помощью нескольких предлагаемых свойств класса PageSetup. Использование этих свойств класса PageSetup обсуждается ниже более подробно.
## **Установка области печати**
По умолчанию выбирается только та область печати, которая включает всю область листа, содержащую данные, но разработчики также могут установить конкретную область печати на листе по своему усмотрению.

Для выбора конкретной области печати разработчики могут использовать метод **PrintArea** класса **PageSetup**. Вы можете передать этому методу диапазон ячеек области печати в качестве аргумента.

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Specifying the cells range (from A1 cell to T35 cell) of the print area

pageSetup.PrintArea = "A1:T35";


{{< /highlight >}}
## **Установка заголовков для печати**
Aspose.Cells позволяет указать строки и столбцы заголовков, которые вы хотите повторить на всех страницах своего распечатанного листа. Для этого разработчики могут использовать методы **setPrintTitleColumns** и **setPrintTitleRows** класса **PageSetup**.

Строки или столбцы (для повторения на всех страницах отпечатанного листа) определяются путем передачи их номеров строки или столбца. Например, строки определяются как \ $1: \ $2, а столбцы определяются как \ $A: \ $B.

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

Aspose.Cells.PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Defining column numbers A & B as title columns

pageSetup.PrintTitleColumns = "$A:$B";

//Defining row numbers 1 & 2 as title rows

pageSetup.PrintTitleRows = "$1:$2";

{{< /highlight >}}
## **Настройка Других Опций Печати**
Класс **PageSetup** также предоставляет несколько других методов для настройки общих параметров печати следующим образом:

- Метод **setPrintGridlines**, этому методу передается логический параметр, который определяет, печатать или не печатать линии сетки
- Метод **setPrintHeadings**, этому методу передается логический параметр, который определяет, печатать или не печатать заголовки строк и столбцов
- Метод **setBlackAndWhite**, этому методу передается логический параметр, который определяет, печатать ли лист в черно-белом режиме или нет
- Метод **setPrintComments**, определяет, следует ли отображать комментарии для печати на листе или в конце листа
- Метод **setPrintDraft**, этому методу передается логический параметр, который определяет, печатать ли лист в черновом качестве или нет
- Метод **setPrintErrors**, определяет, печатать ли ошибки ячеек как отображаемые, пустые, тире или N/A

Для использования методов **setPrintComments** и **setPrintErrors**, Aspose.Cells также предоставляет два перечисления, PrintCommentsType и PrintErrorsType, содержащие предопределенные значения для передачи параметров в соответствующие методы.

{{< highlight csharp >}}

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
Класс **PageSetup** предоставляет метод установки порядка страниц, который используется для упорядочивания нескольких страниц вашего листа для печати. Есть две возможности упорядочивания страниц, как следует:

Спуститься, затем вправо - таким образом, все страницы будут печататься сверху вниз перед печатью страниц справа налево
Вправо, затем вниз - таким образом, страницы будут печататься слева направо перед печатью страниц сверху вниз
Aspose.Cells предоставляет перечисление PrintOrderType, содержащее все предопределенные типы порядка, которые могут быть назначены методу setPageOrder.

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Setting the printing order of the pages to over then down

pageSetup.Order = PrintOrderType.OverThenDown;

{{< /highlight >}}
## **Загрузить образец кода**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Print%20Spreadsheet%20with%20Options%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
