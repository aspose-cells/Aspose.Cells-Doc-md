---
title: Особенности настройки страницы
type: docs
weight: 40
url: /ru/java/page-setup-features/
---
Иногда необходимо настроить параметры страницы для рабочих листов, чтобы управлять печатью. Эти параметры настройки страницы предлагают различные варианты.

**Параметры страницы** 

![дело:изображение_альтернативный_текст](page-setup-features_1.png)

Параметры настройки страницы полностью поддерживаются в Aspose.Cells. В этой статье объясняется, как установить параметры страницы с помощью Aspose.Cells.

## **Настройка параметров страницы**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , представляющий файл Excel Microsoft. Класс Workbook содержит коллекцию Worksheets, которая обеспечивает доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) учебный класс.

Класс Worksheet предоставляет свойство PageSetup, используемое для установки параметров настройки страницы. На самом деле свойство PageSetup является объектом класса PageSetup, который позволяет задавать параметры макета страницы для печатного листа. Класс PageSetup предоставляет различные свойства, используемые для установки параметров настройки страницы. Некоторые из этих свойств обсуждаются ниже.

### **Ориентация страницы**

 Ориентацию страницы можно установить как книжную или альбомную с помощью[**Настройка страницы**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) учебный класс'[**setOrientation (ТипОриентации Страницы)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation) метод.[**setOrientation (ТипОриентации Страницы)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation) метод принимает[**PageOrientationType**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType) перечисление в качестве параметра. Члены[**PageOrientationType**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType)перечисление приведено ниже.

|**Типы ориентации страницы**|**Описание**|
|:- |:- |
|[**ПЕЙЗАЖ**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#LANDSCAPE)|Альбомная ориентация|
|[**ПОРТРЕТ**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#PORTRAIT)|Портретная ориентация|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageOrientation-PageOrientation.java" >}}

### **Коэффициент масштабирования**

 Можно уменьшить или увеличить размер рабочего листа, отрегулировав коэффициент масштабирования с помощью[**setZoom**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Zoom) метод[**Настройка страницы**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) учебный класс.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ScalingFactor-ScalingFactor.java" >}}

### **Параметры FitToPages**

 Чтобы уместить содержимое рабочего листа в определенное количество страниц, используйте[**Настройка страницы**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) учебный класс'[**setFitToPagesTall**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall) а также[**setFitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide) методы. Эти методы также используются для масштабирования рабочих листов.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FitToPagesOptions-FitToPagesOptions.java" >}}

### **Размер бумаги**

 Установите размер бумаги, на котором рабочие листы будут напечатаны, с помощью[**Настройка страницы**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) учебный класс'[**Размер бумаги**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperSize) имущество. Свойство PaperSize принимает одно из предопределенных значений в[**PaperSizeType**](https://reference.aspose.com/cells/java/com.aspose.cells/PaperSizeType) перечисление, приведенное ниже.

|**Типы размеров бумаги**|**Описание**|
|:- |:- |
|Бумага10x14|10 дюймов х 14 дюймов|
|Бумага11x17|11 дюймов х 17 дюймов|
|БумагаA3|A3 (297 мм x 420 мм)|
|БумагаA4|А4 (210 мм х 297 мм)|
|БумагаA4Маленький|A4, малый (210 мм x 297 мм)|
|БумагаA5|A5 (148 мм x 210 мм)|
|БумагаB3|B3 (13,9 х 19,7 дюйма)|
|БумагаB4|B4 (250 мм x 354 мм)|
|БумагаB5|B5 (182 мм x 257 мм)|
|БумагаВизитная Карточка|Визитная карточка (90 мм x 55 мм)|
|БумагаCЛист|Лист размера C|
|БумагаDЛист|Лист размера D|
|БумагаКонверт10|Конверт №10 (4-1/8 дюйма x 9-1/2 дюйма)|
|БумагаКонверт11|Конверт №11 (4-1/2 дюйма x 10-3/8 дюйма)|
|БумагаКонверт12|Конверт №12 (4-1/2 дюйма x 11 дюймов)|
|БумагаКонверт14|Конверт №14 (5 дюймов x 11-1/2 дюйма)|
|БумагаКонверт9|Конверт №9 (3-7/8 дюйма x 8-7/8 дюйма)|
|БумагаКонвертB4|Конверт B4 (250 мм x 353 мм)|
|БумагаКонвертB5|Конверт B5 (176 мм x 250 мм)|
|БумагаКонвертB6|Конверт B6 (176 мм x 125 мм)|
|БумагаКонвертC3|Конверт C3 (324 мм x 458 мм)|
|БумагаКонвертC4|Конверт C4 (229 мм x 324 мм)|
|БумагаКонвертC5|Конверт C5 (162 мм x 229 мм)|
|БумагаКонвертC6|Конверт C6 (114 мм x 162 мм)|
|БумагаКонвертC65|Конверт C65 (114 мм x 229 мм)|
|PaperEnvelopeDL|Конверт DL (110 мм x 220 мм)|
|БумагаКонвертИталия|Конверт Италия (110 мм x 230 мм)|
|БумагаКонвертМонарх|Конверт Monarch (3-7/8 дюйма x 7-1/2 дюйма)|
|БумагаКонвертЛичный|Конверт (3-5/8 дюйма x 6-1/2 дюйма)|
|БумагаEЛист|лист размера Е|
|БумагаРуководитель|Представительский (7-1/2 дюйма x 10-1/2 дюйма)|
|PaperFanfoldЮридическийНемецкий|Фанфолд German Legal (8-1/2 дюйма x 13 дюймов)|
|PaperFanfoldStdНемецкий|Фальцованная немецкая стандартная складка (8-1/2 дюйма x 12 дюймов)|
|БумагаFanfoldСША|Стандартный веерообразный сгиб США (14-7/8 дюймов x 11 дюймов)|
|БумагаФолио|Фолио (8-1/2 дюйма x 13 дюймов)|
|PaperLedger|Леджер (17 дюймов x 11 дюймов)|
|БумагаПравовые|Legal (8-1/2 дюйма x 14 дюймов)|
|БумагаПисьмо|Letter (8-1/2 дюйма x 11 дюймов)|
|БумагаПисьмоМалый|Letter Small (8-1/2 дюйма x 11 дюймов)|
|БумагаПримечание|Примечание (8-1/2 дюйма x 11 дюймов)|
|БумагаКварто|Кварто (215 мм x 275 мм)|
|БумагаЗаявление|Заявление (5-1/2 дюйма x 8-1/2 дюйма)|
|БумагаТаблоид|Таблоид (11 дюймов x 17 дюймов)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ManagePaperSize-ManagePaperSize.java" >}}

### **Качество печати**

 Установите качество печати рабочих листов, которые будут напечатаны с помощью[**Настройка страницы**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) учебный класс'[**setPrintQuality**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintQuality) метод. Единицей измерения качества печати является количество точек на дюйм (DPI).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintQuality-SetPrintQuality.java" >}}

### **Номер первой страницы**

 Начните нумерацию страниц рабочего листа с помощью[**Настройка страницы**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) учебный класс'[**setFirstPageNumber**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FirstPageNumber) метод. Метод setFirstPageNumber устанавливает номер первой страницы рабочего листа, а последующие страницы нумеруются в порядке возрастания.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetFirstPageNumber-SetFirstPageNumber.java" >}}

## **Настройка полей**

Aspose.Cells полностью поддерживает параметры настройки страницы Microsoft Excel. Разработчикам может потребоваться настроить параметры страницы для рабочих листов, чтобы контролировать процесс печати. В этом разделе обсуждается, как использовать Aspose.Cells для настройки полей страницы.

**Поля страницы в Microsoft Excel**

![дело:изображение_альтернативный_текст](page-setup-features_2.png)

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)который представляет собой файл Excel Microsoft. Класс Workbook содержит коллекцию Worksheets, которая обеспечивает доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) учебный класс.

 Класс Worksheet предоставляет свойство PageSetup, используемое для установки параметров настройки страницы. Атрибут PageSetup является объектом[**Настройка страницы**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) класс, который позволяет устанавливать различные параметры макета страницы для печатного листа. Класс PageSetup предоставляет различные свойства и методы, используемые для установки параметров настройки страницы.

### **Поля страницы**

 Установите поля (левое, правое, верхнее, нижнее) страницы с помощью[**Настройка страницы**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) члены класса. Несколько методов, используемых для указания полей страницы, перечислены ниже:

- [**установитьлевое поле (целое число)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#LeftMargin)
- [**установитьRightMargin (целое)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#RightMargin)
- [**setTopMargin (целое число)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#TopMargin)
- [**setBottomMargin (целое число)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BottomMargin)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetMargins-SetMargins.java" >}}

### **Центрировать на странице**

 Можно центрировать что-то на странице по горизонтали и по вертикали.[**Настройка страницы**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) класс имеет членов для этой цели:[**setCenterГоризонтально**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterHorizontally) а также[**setCenterVertical**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterVertically).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CenterOnPage-CenterOnPage.java" >}}

### **Поля верхнего и нижнего колонтитула**

Установите поля верхнего и нижнего колонтитула с помощью[**Настройка страницы**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) члены, такие как[**setHeaderMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#HeaderMargin) а также[**setFooterMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FooterMargin).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HeaderAndFooterMargins-HeaderAndFooterMargins.java" >}}

## **Настройка верхних и нижних колонтитулов**

Верхние и нижние колонтитулы — это разделы текста и изображений над верхним полем или под нижним полем на странице. Также можно добавлять верхние и нижние колонтитулы к рабочим листам. Верхние и нижние колонтитулы можно использовать для отображения любой полезной информации, например номера страницы, имени автора, названия документа или даты и времени. Верхние и нижние колонтитулы также управляются с помощью диалогового окна «Параметры страницы».

**Диалоговое окно «Параметры страницы»** 

![дело:изображение_альтернативный_текст](page-setup-features_3.png)

Aspose.Cells позволяет добавлять верхние и нижние колонтитулы к рабочим листам во время выполнения, но рекомендуется, чтобы верхние и нижние колонтитулы устанавливались вручную в предварительно созданном файле для печати. Вы можете использовать Microsoft Excel в качестве инструмента с графическим интерфейсом, чтобы легко устанавливать верхние и нижние колонтитулы, чтобы сократить время разработки. Aspose.Cells может импортировать файл и зарезервировать эти настройки.

Чтобы добавить верхние и нижние колонтитулы во время выполнения, Aspose.Cells предоставляет специальные классы и некоторые команды сценария для управления форматированием.

### **Команды сценария**

Команды сценария — это специальные команды, предоставленные Aspose.Cells, которые позволяют разработчикам форматировать верхние и нижние колонтитулы.

|**Команды сценария**|**Описание**|
|:- |:- |
|&П|Текущий номер страницы.|
|&ГРАММ|Картинка.|
|&N|Общее количество страниц.|
|&D|Текущая дата.|
|&Т|Текущее время.|
|&А|Имя рабочего листа.|
|&F|Имя файла без пути.|
|&"\<FontName>"|Название шрифта. Например: &"Ариал"|
|&"\<FontName>, \<FontStyle>"|Имя шрифта со стилем. Например: &"Arial,Жирный"|
|&\<FontSize>|Представляет размер шрифта. Например: «&14abc». Но если за этой командой следует простое число, которое будет напечатано в заголовке, оно должно быть отделено пробелом от размера шрифта. Например: «&14 123».|

### **Установить верхние и нижние колонтитулы**

[**Настройка страницы**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) класс предоставляет метод[**setHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeader(int,%20java.lang.String) для добавления заголовка и[**setFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooter(int,%20java.lang.String)) для добавления нижнего колонтитула на лист. Скрипт используется в качестве аргумента для всех вышеперечисленных методов. Он представляет сценарий, который будет использоваться для верхнего или нижнего колонтитула. Этот сценарий содержит команды сценария для форматирования верхних или нижних колонтитулов.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetHeadersAndFooters-SetHeadersAndFooters.java" >}}

### **Вставьте графику в верхний или нижний колонтитул**

[**Настройка страницы**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) класс имеет методы[**setHeadPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeaderPicture(int,%20byte[]) ) а также[**setFooterPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooterPicture(int,%20byte[])) для добавления изображений в верхний и нижний колонтитулы листа. Эти методы принимают два параметра:

- **Раздел**, раздел верхнего или нижнего колонтитула, где будет размещено изображение. Есть три секции: левая, центральная и правая, представленные числовыми значениями 0, 1 и 2 соответственно.
- **Входной поток файла**, графические данные. Двоичные данные должны быть записаны в буфер массива байтов.

После выполнения кода и открытия файла проверьте заголовок рабочего листа в Microsoft Excel:

1.  На**Файл** меню, выберите**Настройка страницы**.
1.  В диалоговом окне «Параметры страницы» выберите**Верхний/нижний колонтитул** вкладка

**Вставка графики в верхний/нижний колонтитул** 

![дело:изображение_альтернативный_текст](page-setup-features_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertImageInHeaderFooter-InsertImageInHeaderFooter.java" >}}

### **Вставьте графику только в верхний колонтитул первой страницы**

[**Настройка страницы**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) class также имеет другие полезные методы, например[**setPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setPicture(boolean,%20boolean,%20boolean,%20int,%20byte[])), [**setFirstPageHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageHeader(int,%20java.lang.String)), [**setFirstPageFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageFooter(int,%20java.lang.String)), для добавления изображений в верхний/нижний колонтитул первой страницы листа. Первая страница — это специальная страница: обычно требуется, чтобы на ней отображалась специальная информация, например логотип компании.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertGraphicinFirstPageHeaderOnly-InsertGraphicinFirstPageHeaderOnly.java" >}}

## **Настройка параметров печати**

Microsoft Параметры настройки страницы Excel предоставляют несколько параметров печати (также называемых параметрами листа), которые позволяют пользователям управлять печатью страниц рабочего листа. Эти параметры печати позволяют пользователям:

- Выберите определенную область печати на листе.
- Печатайте заголовки.
- Распечатайте линии сетки.
- Печатать заголовки строк и столбцов
- Добейтесь чернового качества.
- Печать комментариев.
- Вывести ошибки ячеек.
- Определите порядок страниц.

Все эти варианты печати показаны ниже.

**Параметры печати (листа)** 

![дело:изображение_альтернативный_текст](page-setup-features_5.png)

### **Настройка параметров печати и листа**

 spose.Cells поддерживает все параметры печати, предлагаемые Microsoft Excel, и разработчики могут легко настроить эти параметры для рабочих листов, используя свойства, предлагаемые[**Настройка страницы**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)учебный класс. Использование этих свойств обсуждается ниже более подробно.

### **Установить область печати**

По умолчанию только область печати включает все области рабочего листа, содержащие данные. Разработчики могут установить определенную область печати рабочего листа.

 Чтобы выбрать конкретную область печати, используйте кнопку[**Настройка страницы**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) учебный класс'[**setPrintArea**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintArea) имущество. Назначьте этому свойству диапазон ячеек, определяющий область печати.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintArea-SetPrintArea.java" >}}

### **Установить заголовки для печати**

 Aspose.Cells позволяет указать, что заголовки строк и столбцов будут повторяться на всех страницах печатного листа. Для этого используйте[**Настройка страницы**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) учебный класс'[**setPrintTitleColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleColumns) а также[**setPrintTitleRows**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleRows) характеристики.

Строки или столбцы, которые будут повторяться, определяются путем передачи их номеров строк или столбцов. Например, строки определяются как $1:$2, а столбцы — как $A:$B.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintTitle-SetPrintTitle.java" >}}

### **Установите другие параметры печати**

[**Настройка страницы**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) class также предоставляет несколько других свойств для установки общих параметров печати следующим образом:

- [**setPrintGridlines**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintGridlines), логическое свойство, определяющее, печатать линии сетки или нет.
- [*setPrintHeadings*](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintHeadings), логическое свойство, определяющее, следует ли печатать заголовки строк и столбцов.
- [**установитьчерный и белый**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BlackAndWhite), логическое свойство, определяющее, следует ли печатать рабочий лист в черно-белом режиме или нет.
- [**setPrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments), определяет, отображать ли комментарии печати на рабочем листе или в конце рабочего листа.
- [**setPrintDraft**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintDraft), логическое свойство, определяющее, следует ли печатать рабочий лист в черновом качестве или нет.
- [**setPrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors), определяет, следует ли печатать ошибки ячеек как отображаемые, пустые, тире или Н/Д.

 Чтобы установить[**ПечатьКомментарии**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments) а также[**Ошибки печати**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors) properties, Aspose.Cells также предоставляет два перечисления,[**PrintCommentsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType) а также[**PrintErrorsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType) которые содержат предварительно определенные значения, которые должны быть присвоены[**setPrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments) а также[**setPrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors) свойства соответственно.

 Предустановленные значения в[**PrintCommentsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType) перечисление описано ниже.

|**Печать типов комментариев**|**Описание**|
|:- |:- |
|[**PRINT_IN_PLACE**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_IN_PLACE)|Указывает, чтобы печатать комментарии так, как они отображаются на листе.|
|[**PRINT_NO_COMMENTS**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_NO_COMMENTS)|Указывает, что комментарии не следует печатать.|
|[**PRINT_SHEET_END**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_SHEET_END)|Указывает, что комментарии следует печатать в конце рабочего листа.|

 Предустановленные значения[**PrintErrorsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType) перечисление описано ниже.

|**Типы ошибок печати**|**Описание**|
|:- |:- |
|[*PRINT_ERRORS_BLANK*](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_BLANK)|Указывает не печатать ошибки.|
|[**PRINT_ERRORS_DASH**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_DASH)|Указывает печатать ошибки как "--".|
|[**PRINT_ERRORS_DISPLAYED**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_DISPLAYED)|Задает печать ошибок в том виде, в котором они отображаются.|
|[**PRINT_ERRORS_NA**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_NA)|Указывает печатать ошибки как "#N/A".|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-OtherPrintOptions-OtherPrintOptions.java" >}}

### **Установить порядок страниц**

[**Настройка страницы**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) класс обеспечивает[**setOrder**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order) свойство, которое используется для заказа печати нескольких страниц рабочего листа. Есть две возможности упорядочить страницы следующим образом:

- **Вниз, затем над** печатает все страницы вниз перед печатью любых страниц справа.
- **Затем вниз** печатает страницы слева направо перед печатью любых страниц ниже.

 Aspose.Cells предоставляет перечисление,[**ПринтОрдерТип**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType) , который содержит все предопределенные типы заказов, которые должны быть назначены[**setOrder**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order) метод.

 Предустановленные значения[**ПринтОрдерТип**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType) перечисление описано ниже.

|**Типы заказов на печать**|**Описание**|
|:- |:- |
|[**DOWN_THEN_OVER**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#DOWN_THEN_OVER)|Распечатайте вниз, а затем снова.|
|[**OVER_THEN_DOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#OVER_THEN_DOWN)|Распечатайте сверху, затем вниз.|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPageOrder-SetPageOrder.java" >}}

## **Удалить существующие настройки принтера для рабочих листов в файле Excel**

Пожалуйста, ознакомьтесь с этой статьей, связанной с этой темой.

## **Предварительные темы**
- [Вычислить коэффициент масштабирования параметров страницы](/cells/ru/java/calculate-page-setup-scaling-factor/)
- [Скопируйте настройки параметров страницы из исходного листа в рабочий лист назначения](/cells/ru/java/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/)
- [Определите, является ли размер бумаги рабочего листа автоматическим](/cells/ru/java/determine-if-paper-size-of-worksheet-is-automatic/)
- [Получить ширину и высоту бумаги из PageSetup рабочего листа](/cells/ru/java/get-paper-width-and-height-from-pagesetup-of-worksheet/)
- [Реализовать пользовательский размер бумаги рабочего листа для рендеринга](/cells/ru/java/implement-custom-paper-size-of-worksheet-for-rendering/)
- [Параметры страницы и параметры печати](/cells/ru/java/page-setup-and-printing-options/)
- [Удалить существующие настройки принтера для рабочих листов в файле Excel](/cells/ru/java/remove-existing-printersettings-of-worksheets-in-excel-file/)
