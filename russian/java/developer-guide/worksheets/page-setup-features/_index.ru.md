---
title: Функции настройки страницы
type: docs
weight: 40
url: /ru/java/page-setup-features/
---

Иногда необходимо настроить параметры настройки страницы для листов, чтобы контролировать печать. Эти параметры настройки страницы предлагают различные варианты.

**Опции страницы** 

![todo:image_alt_text](page-setup-features_1.png)

Опции настройки страницы полностью поддерживаются в Aspose.Cells. В этой статье объясняется, как установить опции страницы с помощью Aspose.Cells.

## **Настройка параметров страницы**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), который представляет файл Microsoft Excel. Класс Workbook содержит коллекцию Worksheets, которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

Класс Worksheet предоставляет свойство PageSetup, используемое для установки параметров настройки страницы. Фактически, свойство PageSetup является объектом класса PageSetup, что позволяет устанавливать параметры макета страницы для печатного листа. Класс PageSetup предоставляет различные свойства, используемые для установки параметров настройки страницы. Некоторые из этих свойств обсуждаются ниже.

### **Ориентация страницы**

Ориентацию страницы можно установить в книжный или альбомный вид с помощью метода [**setOrientation(PageOrientationType)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation) класса [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). Метод [**setOrientation(PageOrientationType)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation) принимает перечисление [**PageOrientationType**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType) в качестве параметра. Члены перечисления [**PageOrientationType**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType) перечислены ниже.

|**Типы ориентации страницы**|**Описание**|
| :- | :- |
|[**LANDSCAPE**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#LANDSCAPE)|Альбомная ориентация|
|[**PORTRAIT**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#PORTRAIT)|Книжная ориентация|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageOrientation-PageOrientation.java" >}}

### **Фактор масштабирования**

Размер листа можно уменьшить или увеличить, отрегулировав фактор масштабирования с помощью метода [**setZoom**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Zoom) класса [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ScalingFactor-ScalingFactor.java" >}}

### **Опции FitToPages**

Чтобы подогнать содержимое листа под определенное количество страниц, используйте методы [**setFitToPagesTall**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall) и [**setFitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide) класса [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). Эти методы также используются для масштабирования листов.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FitToPagesOptions-FitToPagesOptions.java" >}}

### **Размер бумаги**

Установите размер бумаги, на который будут напечатаны листы, с помощью свойства [**PaperSize**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperSize) класса [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). Свойство PaperSize принимает одно из предопределенных значений в перечислении [**PaperSizeType**](https://reference.aspose.com/cells/java/com.aspose.cells/PaperSizeType), перечисленных ниже.

|**Типы размеров бумаги**|**Описание**|
| :- | :- |
|Paper10x14|10 in. x 14 in.|
|Paper11x17|11 in. x 17 in.|
|PaperA3|A3 (297 mm x 420 mm)|
|PaperA4|A4 (210 mm x 297 mm)|
|PaperA4Small|A4 Small (210 mm x 297 mm)|
|PaperA5|A5 (148 mm x 210 mm)|
|PaperB3|B3 (13.9 x 19.7 inches)|
|PaperB4|B4 (250 mm x 354 mm)|
|PaperB5|B5 (182 mm x 257 mm)|
|PaperBusinessCard|Business Card (90 mm x 55 mm)|
|PaperCSheet|C size sheet|
|PaperDSheet|D size sheet|
|PaperEnvelope10|Envelope #10 (4-1/8 in. x 9-1/2 in.)|
|PaperEnvelope11|Envelope #11 (4-1/2 in. x 10-3/8 in.)|
|PaperEnvelope12|Envelope #12 (4-1/2 in. x 11 in.)|
|PaperEnvelope14|Envelope #14 (5 in. x 11-1/2 in.)|
|PaperEnvelope9|Envelope #9 (3-7/8 in. x 8-7/8 in.)|
|PaperEnvelopeB4|Envelope B4 (250 mm x 353 mm)|
|PaperEnvelopeB5|Envelope B5 (176 mm x 250 mm)|
|PaperEnvelopeB6|Envelope B6 (176 mm x 125 mm)|
|PaperEnvelopeC3|Envelope C3 (324 mm x 458 mm)|
|PaperEnvelopeC4|Envelope C4 (229 mm x 324 mm)|
|PaperEnvelopeC5|Envelope C5 (162 mm x 229 mm)|
|PaperEnvelopeC6|Envelope C6 (114 mm x 162 mm)|
|PaperEnvelopeC65|Envelope C65 (114 mm x 229 mm)|
|PaperEnvelopeDL|Envelope DL (110 mm x 220 mm)|
|PaperEnvelopeItaly|Envelope Italy (110 mm x 230 mm)|
|PaperEnvelopeMonarch|Envelope Monarch (3-7/8 in. x 7-1/2 in.)|
|PaperEnvelopePersonal|Envelope (3-5/8 in. x 6-1/2 in.)|
|PaperESheet|E size sheet|
|PaperExecutive|Executive (7-1/2 in. x 10-1/2 in.)|
|PaperFanfoldLegalGerman|German Legal Fanfold (8-1/2 in. x 13 in.)|
|PaperFanfoldStdGerman|German Standard Fanfold (8-1/2 in. x 12 in.)|
|PaperFanfoldUS|U.S. Standard Fanfold (14-7/8 in. x 11 in.)|
|PaperFolio|Folio (8-1/2 in. x 13 in.)|
|PaperLedger|Ledger (17 in. x 11 in.)|
|PaperLegal|Legal (8-1/2 in. x 14 in.)|
|PaperLetter|Letter (8-1/2 in. x 11 in.)|
|PaperLetterSmall|Letter Small (8-1/2 in. x 11 in.)|
|PaperNote|Note (8-1/2 in. x 11 in.)|
|PaperQuarto|Quarto (215 mm x 275 mm)|
|PaperStatement|Statement (5-1/2 in. x 8-1/2 in.)|
|PaperTabloid|Tabloid (11 in. x 17 in.)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ManagePaperSize-ManagePaperSize.java" >}}

### **Качество печати**

Установите качество печати листов, которые будут напечатаны с помощью метода [**setPrintQuality**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintQuality) класса [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). Единица измерения качества печати - точки на дюйм (DPI).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintQuality-SetPrintQuality.java" >}}

### **Номер первой страницы**

Начните нумерацию страниц листа с использованием метода [**setFirstPageNumber**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FirstPageNumber) класса [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). Метод setFirstPageNumber устанавливает номер страницы первой страницы листа, и следующие страницы нумеруются по возрастанию.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetFirstPageNumber-SetFirstPageNumber.java" >}}

## **Установка полей**

Aspose.Cells полностью поддерживает параметры настройки страниц Microsoft Excel. Разработчики могут настраивать параметры страницы для листов, чтобы контролировать процесс печати. В данном разделе рассматривается, как использовать Aspose.Cells для настройки полей страницы.

**Поля страниц в Microsoft Excel**

![todo:image_alt_text](page-setup-features_2.png)

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), который представляет собой файл Microsoft Excel. Класс Workbook содержит коллекцию листов, позволяющую получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

Класс Worksheet предоставляет свойство PageSetup, используемое для установки параметров настройки страницы. Атрибут PageSetup представляет объект класса [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup), который позволяет установить различные параметры макета страницы для напечатанного листа. Класс PageSetup предоставляет различные свойства и методы, используемые для установки параметров страницы.

### **Поля страницы**

Установите поля (левое, правое, верхнее, нижнее) страницы с помощью членов класса [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). Ниже приведены некоторые методы, используемые для указания полей страницы:

- [**setLeftMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#LeftMargin)
- [**setRightMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#RightMargin)
- [**setTopMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#TopMargin)
- [**setBottomMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BottomMargin)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetMargins-SetMargins.java" >}}

### **Центрирование на странице**

Возможно центрирование чего-либо на странице горизонтально и вертикально. У класса [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) есть члены для этой цели: [**setCenterHorizontally**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterHorizontally) и [**setCenterVertically**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterVertically).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CenterOnPage-CenterOnPage.java" >}}

### **Поля верхнего и нижнего колонтитулов**

Установите поля верхних и нижних колонтитулов с помощью членов класса [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup), таких как [**setHeaderMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#HeaderMargin) и [**setFooterMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FooterMargin).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HeaderAndFooterMargins-HeaderAndFooterMargins.java" >}}

## **Настройка колонтитулов и подвалов**

Верхние и нижние колонтитулы - это разделы текста и изображений над верхним полем или под нижним полем страницы. Также возможно добавление верхних и нижних колонтитулов к листам. Верхние и нижние колонтитулы могут использоваться для отображения любой полезной информации, например номера страницы, имени автора, заголовка документа или даты и времени. Верхние и нижние колонтитулы также управляются с помощью диалогового окна настройки страницы.

**Диалоговое окно настройки страницы** 

![todo:image_alt_text](page-setup-features_3.png)

Aspose.Cells позволяет добавлять верхние и нижние колонтитулы к листам во время выполнения, но рекомендуется устанавливать верхние и нижние колонтитулы вручную в предварительно разработанном файле для печати. Вы можете использовать Microsoft Excel в качестве инструмента с графическим интерфейсом пользователя для удобной установки верхних и нижних колонтитулов, чтобы уменьшить время разработки. Aspose.Cells может импортировать файл и сохранить эти настройки.

Чтобы добавлять верхние и нижние колонтитулы во время выполнения, Aspose.Cells предоставляет специальные классы и некоторые команды для управления форматированием.

### **Скриптовые команды**

Сценарные команды - это специальные команды, предоставляемые Aspose.Cells, позволяющие разработчикам форматировать заголовки и нижние колонтитулы.

|**Сценарные команды**|**Описание**|
| :- | :- |
|&P|Текущий номер страницы.
|&G|Изображение.
|&N|Общее количество страниц.
|&D|Текущая дата.
|&T|Текущее время.
|&A|Имя листа.
|&F|Имя файла без пути.
|&&Text|Показывает &Text. Например: &&WO будет отображаться как &WO|
|&"\<FontName>"|Имя шрифта. Например: &"Arial"
|&"\<FontName>, \<FontStyle>"|Имя шрифта с начертанием. Например: &"Arial,Bold"
|&\<FontSize>|Представляет размер шрифта. Например: “&14abc”. Однако, если за этой командой следует обычное число для печати в заголовке, его следует отделить пробелом от размера шрифта. Например: “&14 123”.

### **Установить заголовки и нижние колонтитулы**

Класс [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) предоставляет метод [**setHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeader-int-java.lang.String-) для добавления заголовка и [**setFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooter-int-java.lang.String-) для добавления нижнего колонтитула на лист. Этот сценарий используется в качестве аргумента для всех вышеупомянутых методов. Он представляет сценарий, используемый для заголовка или нижнего колонтитула. Этот скрипт содержит команды скрипта для форматирования заголовков или колонтитулов.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetHeadersAndFooters-SetHeadersAndFooters.java" >}}

### **Вставить графику в заголовок или нижний колонтитул**

Класс [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) имеет методы [**setHeadPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeaderPicture-int-byte[]-) и [**setFooterPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooterPicture-int-byte[]-) для добавления изображений в заголовок и нижний колонтитул листа. Эти методы принимают два параметра:

- **Секция**, секция заголовка или нижнего колонтитула, куда будет размещено изображение. Есть три секции: слева, центр и справа, представленные числовыми значениями 0, 1 и 2 соответственно.
- **Поток файла**, графические данные. Бинарные данные должны быть записаны в буфер байтового массива.

После выполнения кода и открытия файла проверьте заголовок листа в Microsoft Excel:

1. В меню **Файл** выберите **Настройка страницы**.
1. В диалоговом окне настройки страницы выберите вкладку **Верхний колонтитул/нижний колонтитул**.

**Вставка графики в верхний/нижний колонтитул** 

![todo:image_alt_text](page-setup-features_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertImageInHeaderFooter-InsertImageInHeaderFooter.java" >}}

### **Вставка графики только вверхний колонтитул первой страницы**

Класс [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) также имеет другие полезные методы, например [**setPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setPicture-boolean-boolean-boolean-int-byte[]-), [**setFirstPageHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageHeader-int-java.lang.String-), [**setFirstPageFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageFooter-int-java.lang.String-), для добавления изображений в верхний и нижний колонтитул первой страницы листа. Первая страница является особой страницей: часто требуется, чтобы она показывала специальную информацию, например логотип компании.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertGraphicinFirstPageHeaderOnly-InsertGraphicinFirstPageHeaderOnly.java" >}}

## **Установка параметров печати**

Настройки страницы в Microsoft Excel предоставляют несколько параметров печати (также называемых параметры листа), которые позволяют пользователям контролировать, как будут напечатаны страницы рабочего листа. Эти параметры печати позволяют пользователям:

- Выбрать конкретную область печати на рабочем листе.
- Напечатать заголовки.
- Напечатать сетку.
- Напечатать заголовки строк и столбцов.
- Достичь чернового качества.
- Напечатать примечания.
- Напечатать ошибки ячеек.
- Определить порядок страниц.

Ниже показаны все эти параметры печати.

**Параметры печати (листа)** 

![todo:image_alt_text](page-setup-features_5.png)

### **Настройка параметров печати и листа**

spose.Cells поддерживает все параметры печати, предлагаемые Microsoft Excel, и разработчики могут легко настроить эти параметры для рабочих листов, используя свойства, предлагаемые классом [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). О том, как используются эти свойства, обсуждается ниже более подробно.

### **Установка области печати**

По умолчанию область печати включает все области рабочего листа, содержащие данные. Разработчики могут определить конкретную область печати для рабочего листа.

Чтобы выбрать конкретную область печати, используйте свойство [**setPrintArea**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintArea) класса [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). Назначьте этому свойству диапазон ячеек, определяющий область печати.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintArea-SetPrintArea.java" >}}

### **Установка заголовков для печати**

Aspose.Cells позволяет назначить заголовки строк и столбцов для повторения на всех страницах напечатанного листа. Для этого используйте свойства [**setPrintTitleColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleColumns) и [**setPrintTitleRows**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleRows) класса [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup).

Строки или столбцы, которые будут повторяться, определяются путем передачи их номеров строки или столбца. Например, строки определяются как $1:$2, а столбцы определяются как $A:$B.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintTitle-SetPrintTitle.java" >}}

### **Настройка Других Опций Печати**

Класс [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) также предоставляет несколько других свойств для установки общих параметров печати следующим образом:

- [**setPrintGridlines**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintGridlines), логическое свойство, определяющее, следует ли печатать сетку или нет.
- [*setPrintHeadings*](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintHeadings), логическое свойство, определяющее, следует ли печатать заголовки строк и столбцов или нет.
- [**setBlackAndWhite**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BlackAndWhite), логическое свойство, определяющее, следует ли печатать лист в черно-белом режиме или нет.
- [**setPrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments), определяет, следует ли отображать примечания к печати на листе или в конце листа.
- [**setPrintDraft**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintDraft), логическое свойство, определяющее, следует ли печатать лист в черновом режиме или нет.
- [**setPrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors), определяет, следует ли печатать ошибки ячеек так, как они отображаются, в виде пустоты, тире или N/A.

Для установки свойств [**PrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments) и [**PrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors), Aspose.Cells также предоставляет два перечисления, [**PrintCommentsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType) и [**PrintErrorsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType), которые содержат предопределенные значения для назначения свойствам [**setPrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments) и [**setPrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors) соответственно.

Предопределенные значения в перечислении [**PrintCommentsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType) описаны ниже.

|**Типы Примечаний к Печати**|**Описание**|
| :- | :- |
|[**PRINT_IN_PLACE**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT-IN-PLACE)|Задает печать комментариев так, как они отображаются на листе.|
|[**PRINT_NO_COMMENTS**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT-NO-COMMENTS)|Задает не печатать комментарии.|
|[**PRINT_SHEET_END**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT-SHEET-END)|Задает печать комментариев в конце листа.|

Предопределенные значения перечисления [**PrintErrorsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType) описаны ниже.

|**Типы Ошибок Печати**|**Описание**|
| :- | :- |
|[**PRINT_ERRORS_BLANK**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT-ERRORS-BLANK)|Задает не печатать ошибки.|
|[**PRINT_ERRORS_DASH**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT-ERRORS-DASH)|Задает печать ошибок как "--".|
|[**PRINT_ERRORS_DISPLAYED**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT-ERRORS-DISPLAYED)|Задает печать ошибок так, как они отображаются.|
|[**PRINT_ERRORS_NA**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT-ERRORS-NA)|Задает печать ошибок как "#N/A".|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-OtherPrintOptions-OtherPrintOptions.java" >}}

### **Установить порядок страниц**

Класс [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) предоставляет свойство [**setOrder**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order), которое используется для упорядочения печати нескольких страниц вашей рабочей книги. Существует два варианта упорядочивания страниц, как показано ниже:

- **Сначала вниз, затем вправо** печатает все страницы внизу перед печатью страниц справа.
- **Сначала вправо, затем вниз** печатает страницы слева направо перед печатью страниц снизу.

Aspose.Cells предоставляет перечисление [**PrintOrderType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType), которое содержит все заранее определенные типы порядка для назначения методу [**setOrder**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order).

Заранее определенные значения перечисления [**PrintOrderType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType) описаны ниже.

|**Типы порядка печати**|**Описание**|
| :- | :- |
|[**DOWN_THEN_OVER**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#DOWN-THEN-OVER)|Печать вниз, затем по горизонтали.|
|[**OVER_THEN_DOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#OVER-THEN-DOWN)|Печать по горизонтали, затем вниз.|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPageOrder-SetPageOrder.java" >}}

## **Удаление текущих настроек принтера на листах Excel**

Пожалуйста, ознакомьтесь с этой статьей по этой теме.

## **Продвинутые темы**
- [Вычислить масштабирование настройки страницы](/cells/ru/java/calculate-page-setup-scaling-factor/)
- [Копирование настроек страницы с исходного листа на целевой лист](/cells/ru/java/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/)
- [Определение автоматического размера бумаги листа](/cells/ru/java/determine-if-paper-size-of-worksheet-is-automatic/)
- [Получение ширины и высоты бумаги из настройки страницы листа](/cells/ru/java/get-paper-width-and-height-from-pagesetup-of-worksheet/)
- [Настройка пользовательского размера бумаги для отображения на листе](/cells/ru/java/implement-custom-paper-size-of-worksheet-for-rendering/)
- [Настройки страницы и опции печати](/cells/ru/java/page-setup-and-printing-options/)
- [Удаление текущих настроек принтера на листах Excel](/cells/ru/java/remove-existing-printersettings-of-worksheets-in-excel-file/)
{{< app/cells/assistant language="java" >}}
