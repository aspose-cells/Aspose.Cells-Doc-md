---
title: Работа с настройками шрифта
linktitle: Настройки шрифта
type: docs
weight: 20
url: /ru/java/dealing-with-font-settings/
---

{{% alert color="primary" %}} 

Внешний вид текста можно контролировать, изменяя его настройки шрифта. Эти настройки шрифта могут включать имя, стиль, размер, цвет и другие эффекты шрифтов, как показано ниже на рисунке:

**Настройки шрифта в Microsoft Excel** 

![todo:image_alt_text](dealing-with-font-settings_1.png)

Как и Microsoft Excel, Aspose.Cells также поддерживает настройку настроек шрифта ячеек.

{{% /alert %}} 
## **Настройка настроек шрифта**
Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), который представляет файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) содержит [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). Класс [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) предоставляет коллекцию [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Каждый элемент в коллекции [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) представляет объект класса [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

Aspose.Cells предоставляет метод [setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle-com.aspose.cells.Style-) класса [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell), используемый для установки форматирования ячейки. Также объект класса [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) содержит свойства для настройки шрифтов.

В этой статье показано, как:

- [Применить определенный шрифт к тексту.](/cells/ru/java/dealing-with-font-settings/)
- [Установить текст жирным](/cells/ru/java/dealing-with-font-settings/).
- [Установить размер шрифта](/cells/ru/java/dealing-with-font-settings/).
- [Установить цвет шрифта](/cells/ru/java/dealing-with-font-settings/).
- [Подчеркнуть текст](/cells/ru/java/dealing-with-font-settings/).
- [Перечеркнуть текст](/cells/ru/java/dealing-with-font-settings/).
- [Установить текст нижним индексом](/cells/ru/java/dealing-with-font-settings/).
- [Установить текст верхним индексом](/cells/ru/java/dealing-with-font-settings/).
### **Установка названия шрифта**
Примените определенный шрифт к тексту в ячейках, используя свойство [setName](https://reference.aspose.com/cells/java/com.aspose.cells/font#Name) объекта [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontName-SettingFontName.java" >}}
### **Установка стиля шрифта на жирный**
Установите текст жирным путем установки свойства [setBold](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsBold) объекта [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) на **true**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SettingFontStyle-1.java" >}}
### **Установка размера шрифта**
Установите размер шрифта, используя свойство [setSize](https://reference.aspose.com/cells/java/com.aspose.cells/font#Size) объекта [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontSize-SetFontSize.java" >}}
### **Установка типа подчеркивания шрифта**
Подчеркните текст с помощью свойства [setUnderline](https://reference.aspose.com/cells/java/com.aspose.cells/font#Underline) объекта [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) . Aspose.Cells предлагает различные предопределенные типы подчеркивания шрифта в перечислении [FontUnderlineType](https://reference.aspose.com/cells/java/com.aspose.cells/FontUnderlineType)

|**Типы подчеркивания шрифта**|**Описание**|
| :- | :- |
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#NONE)| Без подчеркивания|
|[SINGLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#SINGLE)| Одиночное подчеркивание|
|[DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE)| Двойное подчеркивание|
|[ACCOUNTING](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#ACCOUNTING)| Одиночное подчеркивание в учетной записи|
|[DOUBLE_ACCOUNTING](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE-ACCOUNTING)|Двойное подчеркивание•
|[DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH)| Пунктирное подчеркивание|
|[DASH_DOT_DOT_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH-DOT-DOT-HEAVY)|Толстое тире через точку, точку, точку|
|[DASH_DOT_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH-DOT-HEAVY)|Толстая тире через точку|
|[DASHED_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASHED-HEAVY)|Толстая пунктирная линия|
|[DASH_LONG](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH-LONG)|Длинная пунктирная линия|
|[DASH_LONG_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH-LONG-HEAVY)|Толстая длинная пунктирная линия|
|[DOT_DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT-DASH)|Тире с точкой|
|[DOT_DOT_DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT-DOT-DASH)|Двойной тире с точками|
|[DOTTED](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED)| Пунктирное подчеркивание|
|[DOTTED_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED-HEAVY)|Толстая точечная подчеркивание|
|[HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#HEAVY)| Толстое подчеркивание|
|[WAVE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVE)| Волнообразное подчеркивание|
|[WAVY_DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY-DOUBLE)|Двойная волнистая линия|
|[WAVY_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY-HEAVY)|Толстая волнистая линия|
|[WORDS](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WORDS)|Подчеркнуть только символы без пробелов|
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontUnderlineType-SettingFontUnderlineType.java" >}}



### **Установка цвета шрифта**
Установите цвет шрифта с помощью свойства [setColor](https://reference.aspose.com/cells/java/com.aspose.cells/Font) объекта [Font](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color) . Выберите любой цвет из перечисления [Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color) и присвойте выбранный цвет объекту [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) через свойство [setColor](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontColor-SetFontColor.java" >}}



### **Установка зачеркивания текста**
Зачеркните текст с помощью свойства [setStrikeout](https://reference.aspose.com/cells/java/com.aspose.cells/Font) объекта [Font](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsStrikeout) .

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingStrikeOutEffect-SettingStrikeOutEffect.java" >}}



### **Установка нижнего индекса**
Используйте свойство [setSubscript](https://reference.aspose.com/cells/java/com.aspose.cells/Font) объекта [Font](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSubscript) , чтобы сделать текст нижним индексом.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSubscript-SetSubscript.java" >}}



### **Настройка верхнего индекса**
Примените верхний индекс к тексту с помощью свойства [setSuperscript](https://reference.aspose.com/cells/java/com.aspose.cells/Font) объекта [Font](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSuperscript) .

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSuperscript-SetSuperscript.java" >}}

## **Продвинутые темы**
- [Применить эффект верхнего и нижнего индекса к шрифтам](/cells/ru/java/apply-superscript-and-subscript-effects-on-fonts/)
- [Получение списка используемых шрифтов в электронной таблице или книге](/cells/ru/java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
{{< app/cells/assistant language="java" >}}
