---
title: Настройка параметров страницы
type: docs
weight: 10
url: /ru/net/setting-page-options/
description: В этой статье представлен пример кода для программной установки параметров страницы листов Excel с использованием библиотеки C#, API и .NET. Вы сможете установить ориентацию страницы, коэффициент масштабирования, параметры FitToPages, размер бумаги, качество печати, номер первой страницы.
keywords: set excel page orientation c#, set excel scaling factor c#, set excel worksheets paper size c#
---
{{% alert color="primary" %}}

Иногда необходимо настроить параметры страницы для рабочих листов, чтобы управлять печатью. Эти параметры настройки страницы предлагают различные варианты.

{{% /alert %}}

##  **Настройка параметров страницы**

Параметры настройки страницы полностью поддерживаются в Aspose.Cells. В этой статье объясняется, как установить параметры страницы с помощью Aspose.Cells, и показаны примеры кода для настройки:

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) представляющий файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)сорт.

[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс обеспечивает[**Настройка страницы**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) свойство, которое используется для установки параметров настройки страницы рабочего листа. На самом деле это[**Настройка страницы**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) имущество – это объект[**Настройка страницы**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) класс, используемый для установки различных параметров макета страницы для печатного листа.[**Настройка страницы**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)класс предоставляет различные свойства, используемые для установки параметров настройки страницы. Некоторые из этих свойств обсуждаются ниже.

###  **Ориентация страницы**

 Ориентацию страницы можно установить как книжную или альбомную с помощью[**Настройка страницы**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) сорт'[**Ориентация**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/orientation) свойство.[**Ориентация**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/orientation) свойство принимает одно из предопределенных значений в[**PageOrientationType**](https://reference.aspose.com/cells/net/aspose.cells/pageorientationtype)перечисление, приведенное ниже.

|**Типы ориентации страницы**|**Описание**|
| :- | :- |
|Пейзаж|Альбомная ориентация|
|Портрет|Портретная ориентация|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-PageOrientation-1.cs" >}}

###  **Коэффициент масштабирования**

 Можно уменьшить или увеличить размер рабочего листа, отрегулировав коэффициент масштабирования с помощью[**PageSetup.Zoom**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/zoom)свойство.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ScalingFactor-1.cs" >}}

###  **Параметры FitToPages**

 Чтобы уместить содержимое рабочего листа в определенное количество страниц, используйте[**Настройка страницы**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) сорт'[**FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall) и[**FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide)характеристики. Эти свойства также используются для масштабирования рабочих листов.

{{% alert color="primary" %}}

 Вы можете либо выбрать[**FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall)/[**FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide) или[**Увеличить**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/zoom) свойство, но не то и другое одновременно.

{{% /alert %}}

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-FitToPagesOptions-1.cs" >}}

###  **Размер бумаги**

 Установите размер бумаги, на котором рабочие листы будут напечатаны, с помощью[**Настройка страницы**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) сорт'[**Размер бумаги**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/papersize) свойство.[**Размер бумаги**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/papersize) свойство принимает одно из предопределенных значений в[**PaperSizeType**](https://reference.aspose.com/cells/net/aspose.cells/papersizetype)перечисление, приведенное ниже.

|**Типы размеров бумаги**|**Описание**|
| :- | :- |
|БумагаПисьмо|Letter (8-1/2 дюйма x 11 дюймов)|
|БумагаПисьмоМалый|Letter Small (8-1/2 дюйма x 11 дюймов)|
|БумагаТаблоид|Таблоид (11 дюймов x 17 дюймов)|
|PaperLedger|Леджер (17 дюймов x 11 дюймов)|
|БумагаПравовые|Legal (8-1/2 дюйма x 14 дюймов)|
|БумагаЗаявление|Заявление (5-1/2 дюйма x 8-1/2 дюйма)|
|БумагаРуководитель|Представительский (7-1/4 дюйма x 10-1/2 дюйма)|
|БумагаA3|A3 (297 мм x 420 мм)|
|БумагаA4|А4 (210 мм х 297 мм)|
|БумагаA4Маленький|A4, малый (210 мм x 297 мм)|
|БумагаA5|A5 (148 мм x 210 мм)|
|БумагаB4|JIS B4 (257 мм x 364 мм)|
|БумагаB5|JIS B5 (182 мм x 257 мм)|
|БумагаФолио|Фолио (8-1/2 дюйма x 13 дюймов)|
|БумагаКварто|Кварто (215 мм x 275 мм)|
|Бумага10x14|10 дюймов х 14 дюймов|
|Бумага11x17|11 дюймов х 17 дюймов|
|БумагаПримечание|Примечание (8-1/2 дюйма x 11 дюймов)|
|БумагаКонверт9|Конверт №9 (3-7/8 дюйма x 8-7/8 дюйма)|
|БумагаКонверт10|Конверт №10 (4-1/8 дюйма x 9-1/2 дюйма)|
|БумагаКонверт11|Конверт №11 (4-1/2 дюйма x 10-3/8 дюйма)|
|БумагаКонверт12|Конверт №12 (4-1/2 дюйма x 11 дюймов)|
|БумагаКонверт14|Конверт №14 (5 дюймов x 11-1/2 дюйма)|
|БумагаCЛист|Лист размера С|
|БумагаDЛист|Лист размера D|
|БумагаEЛист|лист размера Е|
|PaperEnvelopeDL|Конверт DL (110 мм x 220 мм)|
|БумагаКонвертC5|Конверт C5 (162 мм x 229 мм)|
|БумагаКонвертC3|Конверт C3 (324 мм x 458 мм)|
|БумагаКонвертC4|Конверт C4 (229 мм x 324 мм)|
|БумагаКонвертC6|Конверт C6 (114 мм x 162 мм)|
|БумагаКонвертC65|Конверт C65 (114 мм x 229 мм)|
|БумагаКонвертB4|Конверт B4 (250 мм x 353 мм|
|БумагаКонвертB5|Конверт B5 (176 мм x 250 мм)|
|БумагаКонвертB6|Конверт B6 (176 мм x 125 мм)|
|БумагаКонвертИталия|Конверт Италия (110 мм x 230 мм)|
|БумагаКонвертМонарх|Конверт Monarch (3-7/8 дюйма x 7-1/2 дюйма)|
|БумагаКонвертЛичный|Конверт (3-5/8 дюйма x 6-1/2 дюйма)|
|БумагаFanfoldСША|Стандартный веерообразный сгиб США (14-7/8 дюймов x 11 дюймов)|
|PaperFanfoldStdНемецкий|Немецкий стандартный фальцованный фальц (8-1/2 дюйма x 12 дюймов)|
|PaperFanfoldЮридическийНемецкий|Фанфолд German Legal (8-1/2 дюйма x 13 дюймов)|
|БумагаISOB4|B4 (ISO) 250 х 353 мм|
|БумагаЯпонскийОткрытка|Японская открытка (100 мм x 148 мм)|
|Бумага9x11|9 дюймов х 11 дюймов|
|Бумага10x11|10 дюймов x 11 дюймов|
|Бумага15x11|15 дюймов х 11 дюймов|
|БумагаКонвертПригласить|Пригласительный конверт (220 мм x 220 мм)|
|БумагаПисьмоДополнительно|Письмо США Extra 9 \ 275 x 12 дюймов|
|БумагаЮридическаяЭкстра|US Legal Extra 9 \275 x 15 дюймов|
|БумагаТаблоидЭкстра|US Tabloid Extra 11,69 x 18 дюймов|
|БумагаA4Extra|A4 Extra 9,27 x 12,69 дюйма|
|БумагаПисьмоПоперечный|Письмо поперечное 8 \ 275 x 11 дюймов|
|БумагаA4Поперечный|A4 Поперечное 210 х 297 мм|
|БумагиПисьмоДополнительно|Letter Extra Transverse 9\275 x 12 дюймов|
|БумагаSuperA|SuperA/SuperA/A4 227 x 356 мм|
|БумагаSuperB|SuperB/SuperB/A3 305 x 487 мм|
|БумагаПисьмоПлюс|Письмо США плюс 8,5 x 12,69 дюйма|
|БумагаA4Plus|А4 плюс 210 х 330 мм|
|БумагаA5Поперечный|A5 Поперечное 148 х 210 мм|
|БумагаJISB5Поперечный|B5 (JIS) Поперечное 182 x 257 мм|
|БумагаA3Extra|А3 Экстра 322 х 445 мм|
|БумагаA5Extra|А5 экстра 174 х 235 мм|
|БумагаISOB5Extra|B5 (ISO) Экстра 201 x 276 мм|
|БумагаA2|А2 420 х 594 мм|
|БумагаA3Поперечный|A3 Поперечное 297 x 420 мм|
|БумагаA3ЭкстраПоперечный|A3 Экстра поперечный 322 x 445 мм|
|БумагаЯпонскийДвойнойОткрытка|Японская двойная открытка 200 x 148 мм|
|БумагаA6|А6 105 х 148 мм|
|БумагаЯпонскийКонвертКаку2|Японский конверт Каку #2|
|БумагаЯпонскийКонвертКаку3|Японский конверт Каку #3|
|БумагаЯпонскийКонвертЧоу3|Японский конверт Chou #3|
|БумагаЯпонскийКонвертЧоу4|Японский конверт Chou #4|
|БумагаПисьмо|11 х 8,5 дюймов|
|БумагаA3Поворот|420 мм х 297 мм|
|БумагаA4Поворот|297 мм х 210 мм|
|БумагаA5Поворот|210 мм х 148 мм|
|БумагаJISB4Rotated|B4 (JIS) Повернутый 364 x 257 мм|
|БумагаJISB5Rotated|B5 (JIS) Повернутый 257 x 182 мм|
|БумагаЯпонскийОткрыткаПовернутый|Японская открытка Повернутая 148 x 100 мм|
|БумагаЯпонскийДвойнойОткрыткаПовернутый|Двойная японская открытка повернутая 148 x 200 мм|
|БумагаA6Поворот|A6 Повернутый 148 x 105 мм|
|БумагаЯпонскийКонвертКаку2Rotated|Японский конверт Kaku # 2 повернут|
|БумагаЯпонскийКонвертKaku3Rotated|Японский конверт Kaku # 3 повернут|
|БумагаЯпонскийКонвертChou3Rotated|Японский конверт Chou # 3 повернут|
|БумагаЯпонскийКонвертChou4Rotated|Японский конверт Chou # 4 повернут|
|БумагаJISB6|B6 (JIS) 128 x 182 мм|
|БумагаJISB6Rotated|B6 (JIS) Повернутый 182 x 128 мм|
|Бумага12x11|12 х 11 дюймов|
|БумагаЯпонскийКонвертYou4|Японский конверт №4|
|БумагаЯпонскийКонвертYou4Rotated|Японский конверт, который вы # 4 повернули|
|БумагаPRC16K|КНР 16К 146 х 215 мм|
|БумагаPRC32K|КНР 32К 97 х 151 мм|
|БумагаPRCBig32K|PRC 32K (большой) 97 x 151 мм|
|БумагаPRCКонверт1|Конверт PRC #1 102 x 165 мм|
|БумагаPRCEnvelope2|Конверт PRC #2 102 x 176 мм|
|БумагаPRCEnvelope3|Конверт PRC #3 125 x 176 мм|
|БумагаPRCКонверт4|Конверт PRC #4 110 x 208 мм|
|БумагаPRCКонверт5|Конверт PRC #5 110 x 220 мм|
|БумагаPRCКонверт6|Конверт PRC #6 120 x 230 мм|
|БумагаPRCКонверт7|Конверт PRC #7 160 x 230 мм|
|БумагаPRCКонверт8|Конверт PRC #8 120 x 309 мм|
|БумагаPRCКонверт9|Конверт PRC #9 229 x 324 мм|
|БумагаPRCКонверт10|Конверт PRC #10 324 x 458 мм|
|БумагаPRC16KПовернутый|PRC 16K повернуто|
|БумагаPRC32KПовернутый|PRC 32K Повернутый|
|БумагаPRCBig32KRotated|PRC 32K (большой) повернутый|
|БумагаPRCEnvelope1Rotated|Конверт PRC #1, повернутый 165 x 102 мм|
|БумагаPRCEnvelope2Rotated|Конверт PRC #2, повернутый 176 x 102 мм|
|БумагаPRCEnvelope3Rotated|Конверт PRC #3, повернутый 176 x 125 мм|
|БумагаPRCEnvelope4Rotated|Конверт PRC № 4 повернутый 208 x 110 мм|
|БумагаPRCEnvelope5Rotated|Конверт PRC #5, повернутый 220 x 110 мм|
|БумагаPRCEnvelope6Rotated|Конверт PRC #6, повернутый 230 x 120 мм|
|БумагаPRCEnvelope7Rotated|Конверт PRC #7, повернутый 230 x 160 мм|
|БумагаPRCEnvelope8Rotated|PRC Envelope #8 Повернутый 309 x 120 мм|
|БумагаPRCEnvelope9Rotated|Конверт PRC #9, повернутый 324 x 229 мм|
|БумагаPRCEnvelope10Rotated|PRC Envelope #10 Повернутый 458 x 324 мм|
|БумагаB3|обычный B3 (13,9 x 19,7 дюйма)|
|БумагаВизитная Карточка|Визитная карточка (90 мм x 55 мм)|
|БумагаТермо|Термальный (3 x 11 дюймов)|
|Обычай|Представляет нестандартный размер бумаги.|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ManagePaperSize-1.cs" >}}

###  **Качество печати**

 Установите качество печати рабочих листов, которые будут напечатаны с помощью[**Настройка страницы**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) сорт'[**Качество печати**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printquality)свойство. Единицей измерения качества печати является число точек на дюйм (DPI).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintQuality-1.cs" >}}

###  **Номер первой страницы**

 Начните нумерацию страниц рабочего листа с помощью[**Настройка страницы**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) сорт'[**номер первой страницы**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/firstpagenumber) свойство.[**номер первой страницы**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/firstpagenumber)Свойство задает номер первой страницы рабочего листа, а последующие страницы нумеруются в порядке возрастания.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetFirstPageNumber-1.cs" >}}
