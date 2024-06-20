---
title: Форматы ячеек
type: docs
weight: 100
url: /ru/java/cells-formatting/
---

## **Добавление границ в ячейки**
Microsoft Excel позволяет пользователям форматировать ячейки, добавляя границы.

**Настройки границ в Microsoft Excel** 

![todo:image_alt_text](cells-formatting_1.png)

Тип границы зависит от того, куда она добавлена. Например, верхняя граница - это граница, добавленная в верхнюю позицию ячейки. Пользователи также могут изменить стиль линии и цвет границ.

С помощью Aspose.Cells разработчики могут добавлять границы и настраивать их в том же гибком формате, что и в Microsoft Excel.
### **Добавление границ в ячейки**
Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), представляющий файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) содержит коллекцию [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). Класс [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) содержит коллекцию [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Каждый элемент в коллекции [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) представляет объект класса [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

Aspose.Cells предоставляет метод [setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) в классе [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell), используемый для установки стиля форматирования ячейки. Также используется объект класса [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style), предоставляющий свойства для настройки параметров шрифта.
#### **Добавление границ к ячейке**
Добавление границы в ячейку с помощью метода [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\)) объекта [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style). Тип границы передается в качестве параметра. Все типы границ заранее определены в перечислении [BorderType](https://reference.aspose.com/cells/java/com.aspose.cells/BorderType).

|**Типы границ**|**Описание**|
| :- | :- |
|[BOTTOM_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#BOTTOM_BORDER)|Линия нижней границы|
|[DIAGONAL_DOWN](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_DOWN)|Диагональная линия от верхнего левого до правого нижнего|
|[DIAGONAL_UP](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_UP)|Диагональная линия от нижнего левого до правого верхнего|
|[LEFT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#LEFT_BORDER)|Левая граничная линия|
|[RIGHT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#RIGHT_BORDER)|Правая граничная линия|
|[TOP_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#TOP_BORDER)|Верхняя граничная линия|
|[HORIZONTAL](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#HORIZONTAL)|Только для динамического стиля, такого как условное форматирование.|
|[VERTICAL](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#VERTICAL)|Только для динамического стиля, такого как условное форматирование.|
Для установки цвета линии выберите цвет, используя перечисление [Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color) и передайте его в метод [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\)) объекта [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) через параметр Color. Стили линии предопределены в перечислении [CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType).

|**Стили линий**|**Описание**|
| :- | :- |
|[DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT)|Представляет тонкую пунктирно-точечную линию|
|[DASH_DOT_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT_DOT)|Представляет тонкую пунктирно-точечно-пунктирную линию|
|[DASHED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASHED)|Представляет пунктирную линию|
|[DOTTED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOTTED)|Представляет пунктирную линию|
|[DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOUBLE)|Представляет двойную линию|
|[HAIR](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#HAIR)|Представляет линию волосковой толщины|
|[MEDIUM_DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT)|Представляет среднюю пунктирно-точечную линию|
|[MEDIUM_DASH_DOT_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT_DOT)|Представляет среднюю пунктирно-точечно-пунктирную линию|
|[MEDIUM_DASHED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASHED)|Представляет среднюю пунктирную линию|
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#NONE)|Представляет отсутствие линии|
|[MEDIUM](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM)|Представляет среднюю линию|
|[SLANTED_DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#SLANTED_DASH_DOT)|Представляет наклонную среднюю пунктирно-точечную линию|
|[THICK](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THICK)|Представляет толстую линию|
|[THIN](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THIN)|Представляет тонкую линию|
Выберите один из вышеперечисленных стилей линий, а затем назначьте его методу [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\)) объекта [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style).

Следующий вывод генерируется при выполнении приведенного ниже кода.

**Границы применяются со всех сторон ячейки** 

![todo:image_alt_text](cells-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBordersToCells-AddingBordersToCells.java" >}}
#### **Добавление границ для диапазона ячеек**
Можно добавить границы для диапазона ячеек, а не только для одной ячейки. Сначала создайте диапазон ячеек, вызвав метод [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)) коллекции [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), который принимает следующие параметры:

- **Первая строка**, первая строка диапазона.
- **Первый столбец**, первый столбец диапазона.
- **Количество строк**, количество строк в диапазоне.
- **Количество столбцов**, количество столбцов в диапазоне.

Метод [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)) возвращает объект [Range](https://reference.aspose.com/cells/java/com.aspose.cells/Range), который содержит указанный диапазон. Объект [Range](https://reference.aspose.com/cells/java/com.aspose.cells/Range) предоставляет метод [setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders\(int,%20com.aspose.cells.Color\)), который принимает следующие параметры:

- **CellBorderType**, стиль линии границы, выбранный из перечисления [CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType).
- **Color**, цвет линии границы, выбранный из перечисления [Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color).

Следующий вывод генерируется при выполнении приведенного ниже кода.

**Границы применяются к диапазону ячеек** 

![todo:image_alt_text](cells-formatting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBorderstoRange-AddingBorderstoRange.java" >}}
## **Цвета и палитра**
Палитра - это количество цветов, доступных для использования при создании изображения. Использование стандартной палитры в презентации позволяет пользователю создавать однородный вид. Каждый файл Microsoft Excel (97-2003) имеет палитру из 56 цветов, которые могут быть применены к ячейкам, шрифтам, сеткам, графическим объектам, заливкам и линиям в диаграмме.

**Настройки палитры в Microsoft Excel** 

![todo:image_alt_text](cells-formatting_4.png)

С помощью Aspose.Cells можно не только использовать существующие цвета, но и создавать пользовательские цвета. Перед использованием пользовательского цвета добавьте его в палитру. В этой теме объясняется, как добавить пользовательские цвета в палитру.
### **Добавление пользовательских цветов в палитру**
Aspose.Cells также поддерживает палитру из 56 цветов. Стандартная палитра цветов показана выше. Если вы хотите использовать пользовательский цвет, который не определен в палитре, вам нужно добавить этот цвет в палитру перед использованием.

{{% alert color="primary" %}} 

Палитра вмещает только 56 цветов. Когда вы добавляете пользовательский цвет в палитру, палитра изменяется, и любой элемент в файле, отформатированный предыдущим цветом, изменяется. Поэтому, когда вы меняете палитру, будьте очень осторожны. Более того, это ограничение применимо только к формату файла XLS (Excel 97 - 2003), поскольку для форматов файлов XLSX или других более новых форматов MS Excel (2007/2010) такого ограничения нет.

{{% /alert %}} 

Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), который представляет файл Microsoft Excel. Класс предоставляет метод [changePalette](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#changePalette\(com.aspose.cells.Color,%20int\)), который принимает следующие параметры для добавления пользовательского цвета для изменения палитры:

- **Пользовательский цвет**, пользовательский цвет, который будет добавлен в палитру.
- **Индекс**, индекс цвета, который будет заменен пользовательским цветом. Должен быть от 0 до 55.

Приведенный ниже пример добавляет пользовательский цвет в палитру перед его применением к шрифту.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndPalette-ColorsAndPalette.java" >}}
## **Цвета и фоновые узоры**
Microsoft Excel может устанавливать передний (контур) и задний (заливка) цвета ячеек и фоновые узоры, как показано ниже.

**Установка цветов и фоновых узоров в Microsoft Excel** 

![todo:image_alt_text](cells-formatting_5.png)

Aspose.Cells также поддерживает эти функции гибким образом. В этой теме мы узнаем, как использовать эти функции с использованием Aspose.Cells.
### **Установка цветов и фоновых узоров**
Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), который представляет файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) содержит [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). Класс [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) предоставляет коллекцию [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Каждый элемент в коллекции [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) представляет объект класса [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

Aspose.Cells предоставляет метод [setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) в классе [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell), который используется для установки форматирования ячейки. Также объект класса [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) можно использовать для настройки параметров шрифта.

{{% alert color="primary" %}} 

Чтобы установить передний или задний цвет ячейки, используйте свойства объекта [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) [setBackgroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor) или [setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor). Эти свойства вступают в силу только в том случае, если свойство объекта [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) [setPattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) настроено.

{{% /alert %}} 

Свойство [setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) устанавливает цвет затемнения ячейки.

Свойство [setPattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) указывает фоновый узор, используемый для переднего или заднего цвета. Aspose.Cells предоставляет перечисление [BackgroundType](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType), которое содержит набор предопределенных типов фоновых узоров.

|**Тип узора**|**Описание**|
| :- | :- |
|[DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_CROSSHATCH)|Представляет диагональный крестовый узор|
|[DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_STRIPE)|Представляет диагональный узор в полоску|
|[GRAY_6](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_6)|Представляет узор 6.25% серого цвета|
|[GRAY_12](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_12)|Представляет собой 12,5% серый узор|
|[GRAY_25](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_25)|Представляет собой 25% серый узор|
|[GRAY_50](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_50)|Представляет собой 50% серый узор|
|[GRAY_75](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_75)|Представляет собой 75% серый узор|
|[HORIZONTAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#HORIZONTAL_STRIPE)|Представляет горизонтальный полосатый узор|
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)|Представляет отсутствие фона|
|[REVERSE_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#REVERSE_DIAGONAL_STRIPE)|Представляет перевернутый диагональный полосатый узор|
|[SOLID](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID)|Представляет сплошной узор|
|[THICK_DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THICK_DIAGONAL_CROSSHATCH)|Представляет толстый диагональный клетчатый узор|
|[THIN_DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_CROSSHATCH)|Представляет тонкий диагональный клетчатый узор|
|[THIN_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_STRIPE)|Представляет тонкий диагональный полосатый узор|
|[THIN_HORIZONTAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_CROSSHATCH)|Представляет тонкий горизонтальный клетчатый узор|
|[THIN_HORIZONTAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_STRIPE)|Представляет тонкий горизонтальный полосатый узор|
|[THIN_REVERSE_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_REVERSE_DIAGONAL_STRIPE)|Представляет тонкий перевернутый диагональный полосатый узор|
|[THIN_VERTICAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_VERTICAL_STRIPE)|Представляет тонкий вертикальный полосатый узор|
|[VERTICAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#VERTICAL_STRIPE)|Представляет вертикальный полосатый узор|
В приведенном ниже примере цвет переднего плана ячейки A1 установлен, но ячейка A2 настроена иметь как передний, так и фоновый цвета с фоновым узором вертикальных полос.

Следующий вывод генерируется при выполнении кода.

Применены **цвета переднего плана и фона на ячейках с фоновыми узорами** 

![todo:image_alt_text](cells-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndBackground-ColorsAndBackground.java" >}}
### **Важно знать**
{{% alert color="primary" %}} 

- Чтобы установить передний или задний фон ячейки, используйте свойство [ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) или [BackgroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor) объекта [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style). Оба свойства вступят в силу только если свойство [Pattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) объекта [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) настроено.
- Свойство [ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) устанавливает оттенок цвета ячейки.
  Свойство [Pattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) определяет тип используемого фонового узора для переднего или заднего цвета. Aspose.Cells предоставляет перечисление, [BackgroundType](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType), которое содержит набор предопределенных типов фоновых узоров.
- Если выбрать значение [BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE) из перечисления [BackgroundType](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType), передний цвет не применяется.
  Точно так же, задний цвет не применяется, если выбраны значения [BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE) или [BackgroundType.SOLID](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID).
- При извлечении заливки ячейки, если [Style.Pattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) равно [BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE), [Style.ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) вернет *Color.Empty*.

{{% /alert %}} 
## **Форматирование выбранных символов в ячейке**
[Working with Font Settings](/cells/ru/java/dealing-with-font-settings/) объясняет, как форматировать ячейки, но только как форматировать содержимое всей ячейки. Что делать, если вы хотите отформатировать только выбранные символы?

Aspose.Cells поддерживает эту функцию. В этой теме объясняется, как использовать эту функцию.
### **Форматирование выбранных символов**
Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), который представляет файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) содержит [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). Класс [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) предоставляет коллекцию [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Каждый элемент в коллекции [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) представляет объект класса [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

Класс [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) предоставляет метод [characters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#characters(int,%20int)) который принимает следующие параметры для выбора диапазона символов в ячейке:

- **Индекс начала**, индекс начального символа для выбора.
- **Количество символов**, количество выбираемых символов.

В выходном файле, в ячейке A1, слово 'Visit' форматируется стандартным шрифтом, но 'Aspose!' выделено жирным и синим.

**Форматирование выбранных символов** 

![todo:image_alt_text](cells-formatting_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}

{{% alert color="primary" %}} 

Если вас интересует [форматирование части форматированного текста в ячейке](/cells/ru/java/access-and-update-the-portions-of-rich-text-of-cell/), рассмотрите использование методов [Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters()) и Cell.setCharacters. Метод [Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters()) позволяет получить доступ к частям текста, а затем изменения можно внести с помощью метода Cell.setCharacters, в то время как **get** метод возвращает массив объектов [FontSetting](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting), которые можно изменять для установки различных свойств, таких как имя шрифта, цвет шрифта, жирность и т. д., а метод **set** можно использовать для применения изменений.

{{% /alert %}}

## **Продвинутые темы**
- [Настройки выравнивания](/cells/ru/java/cells-alignment-settings/)
- [Условное форматирование](/cells/ru/java/conditional-formatting/)
- [Форматирование данных](/cells/ru/java/data-formatting/)
- [Темы и цвета Excel](/cells/ru/java/excel-2007-themes-and-colors/)
- [Работа с настройками шрифта](/cells/ru/java/dealing-with-font-settings/)
- [Форматирование ячеек листа в книге Excel](/cells/ru/java/format-worksheet-cells-in-a-workbook/)
- [Реализация системы дат 1904 года](/cells/ru/java/implement-1904-date-system/)
- [Объединение и разъединение ячеек](/cells/ru/java/merging-and-unmerging-cells/)
- [Настройки чисел](/cells/ru/java/cells-number-settings/)
- [Сохранить префикс одинарной кавычки значения ячейки или диапазона](/cells/ru/java/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Стилизация и форматирование данных](/cells/ru/java/styling-and-data-formatting/)
