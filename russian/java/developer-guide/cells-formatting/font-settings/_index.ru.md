---
title: Работа с настройками шрифта
linktitle: Настройки шрифта
type: docs
weight: 20
url: /ru/java/dealing-with-font-settings/
---
{{% alert color="primary" %}} 

Внешний вид текста можно контролировать, изменяя настройки шрифта. Эти настройки шрифта могут включать имя, стиль, размер, цвет и другие эффекты шрифтов, как показано ниже на рисунке:

**Настройки шрифта в Microsoft Excel** 

![дело:изображение_альтернативный_текст](dealing-with-font-settings_1.png)

Как и Microsoft Excel, Aspose.Cells также поддерживает настройку параметров шрифта ячеек.

{{% /alert %}} 
## **Настройка параметров шрифта**
 Aspose.Cells предоставляет класс,[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) который представляет собой файл Excel Microsoft.[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) класс содержит[Рабочий листКоллекция](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) который позволяет получить доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)учебный класс.[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) класс предоставляет[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) коллекция. Каждый элемент в[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) коллекция представляет собой объект[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)учебный класс.

 Aspose.Cells обеспечивает[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) учебный класс'[setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\) ), используемый для установки форматирования ячейки. Также объектом[Стиль](https://reference.aspose.com/cells/java/com.aspose.cells/Style)класс предоставляет свойства для настройки параметров шрифта.

В этой статье показано, как:

- [Применение определенного шрифта к тексту.](/cells/ru/java/dealing-with-font-settings/)
- [Сделать текст жирным](/cells/ru/java/dealing-with-font-settings/).
- [Установите размер шрифта](/cells/ru/java/dealing-with-font-settings/).
- [Установить цвет шрифта](/cells/ru/java/dealing-with-font-settings/).
- [Подчеркнуть текст](/cells/ru/java/dealing-with-font-settings/).
- [Зачеркнутый текст](/cells/ru/java/dealing-with-font-settings/).
- [Установить текст в индекс](/cells/ru/java/dealing-with-font-settings/).
- [Сделать текст надстрочным](/cells/ru/java/dealing-with-font-settings/).
### **Настройка имени шрифта**
 Применение определенного шрифта к тексту в ячейках с помощью кнопки[Шрифт](https://reference.aspose.com/cells/java/com.aspose.cells/Font) объекты[Имя набора](https://reference.aspose.com/cells/java/com.aspose.cells/font#Name)имущество.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontName-SettingFontName.java" >}}
### **Установка стиля шрифта на полужирный**
 Выделите текст жирным шрифтом, установив[Шрифт](https://reference.aspose.com/cells/java/com.aspose.cells/Font) объекты[установить полужирный](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsBold) собственность на**истинный**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SettingFontStyle-1.java" >}}
### **Настройка размера шрифта**
 Установите размер шрифта с помощью[Шрифт](https://reference.aspose.com/cells/java/com.aspose.cells/Font) объекты[setSize](https://reference.aspose.com/cells/java/com.aspose.cells/font#Size)имущество.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontSize-SetFontSize.java" >}}
### **Настройка типа подчеркивания шрифта**
 Подчеркните текст с помощью[Шрифт](https://reference.aspose.com/cells/java/com.aspose.cells/Font) объекты[setUnderline](https://reference.aspose.com/cells/java/com.aspose.cells/font#Underline) имущество. Aspose.Cells предлагает различные предопределенные типы подчеркивания шрифта в[ШрифтПодстрочныйТип](https://reference.aspose.com/cells/java/com.aspose.cells/FontUnderlineType)перечисление.

|**Типы подчеркивания шрифта**|**Описание**|
|:- |:- |
|[НИКТО](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#NONE)|Без подчеркивания|
|[НЕ ЗАМУЖЕМ](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#SINGLE)|Одно подчеркивание|
|[ДВОЙНОЙ](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE)|Двойное подчеркивание|
|[БУХГАЛТЕРСКИЙ УЧЕТ](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#ACCOUNTING)|Единое бухгалтерское подчеркивание|
|[DOUBLE_ACCOUNTING](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE_ACCOUNTING)|Двойное бухгалтерское подчеркивание|
|[БРОСАТЬСЯ](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH)|Пунктирное подчеркивание|
|[БРОСАТЬСЯ_ТОЧКА_DOT_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_DOT_DOT_HEAVY)|Подчеркивание жирным тире-точкой-точкой|
|[БРОСАТЬСЯ_ТОЧКА_ТЯЖЕЛЫЙ](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_DOT_HEAVY)|Подчеркивание толстой штрихпунктирной линией|
|[DASHED_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASHED_HEAVY)|Подчеркивание жирным пунктиром|
|[DASH_LONG](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_LONG)|Подчеркивание длинной пунктирной линией|
|[БРОСАТЬСЯ_ДЛИННАЯ_ТЯЖЕЛЫЙ](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_LONG_HEAVY)|Подчеркивание толстой длинной пунктирной линией|
|[DOT_DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT_DASH)|Подчеркивание тире-точкой|
|[ТОЧКА_ТОЧКА_БРОСАТЬСЯ](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT_DOT_DASH)|Штрих-точка-точка подчеркивание|
|[ПУНКТИРНЫЙ](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED)|Пунктирное подчеркивание|
|[DOTTED_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED_HEAVY)|Подчеркивание жирным пунктиром|
|[ТЯЖЕЛЫЙ](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#HEAVY)|Толстое подчеркивание|
|[ВОЛНА](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVE)|Подчеркивание волны|
|[WAVY_DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY_DOUBLE)|Подчеркивание двойной волны|
|[WAVY_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY_HEAVY)|Подчеркивание тяжелой волны|
|` `[СЛОВА](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WORDS)|Подчеркивание только не пробельных символов|
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontUnderlineType-SettingFontUnderlineType.java" >}}



### **Настройка цвета шрифта**
 Установите цвет шрифта с помощью[Шрифт](https://reference.aspose.com/cells/java/com.aspose.cells/Font) объекты[setColor](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color) имущество. Выберите любой цвет из[Цвет](https://reference.aspose.com/cells/java/com.aspose.cells/Color) перечисление и присвоить выбранный цвет[Шрифт](https://reference.aspose.com/cells/java/com.aspose.cells/Font) объекты[setColor](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontColor-SetFontColor.java" >}}



### **Установка эффекта зачеркивания для текста**
 Зачеркнутый текст с[Шрифт](https://reference.aspose.com/cells/java/com.aspose.cells/Font) объекты[setStrikeout](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsStrikeout)имущество.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingStrikeOutEffect-SettingStrikeOutEffect.java" >}}



### **Установка индекса**
 Сделать текст надстрочным с помощью[Шрифт](https://reference.aspose.com/cells/java/com.aspose.cells/Font) объекты[setSubscript](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSubscript)имущество.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSubscript-SetSubscript.java" >}}



### **Установка верхнего индекса**
 Применить надстрочный индекс к тексту с помощью[Шрифт](https://reference.aspose.com/cells/java/com.aspose.cells/Font) объекты[setSuperscript](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSuperscript)имущество.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSuperscript-SetSuperscript.java" >}}

## **Предварительные темы**
- [Применение эффектов верхнего и нижнего индекса к шрифтам](/cells/ru/java/apply-superscript-and-subscript-effects-on-fonts/)
- [Получить список шрифтов, используемых в электронной таблице или книге](/cells/ru/java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
