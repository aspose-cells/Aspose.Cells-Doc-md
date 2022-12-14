---
title: Cells Форматы
type: docs
weight: 100
url: /ru/java/cells-formatting/
---
## **Добавление границ к Cells**
Microsoft Excel позволяет пользователям форматировать ячейки, добавляя границы.

**Настройки границ в Microsoft Excel** 

![дело:изображение_альтернативный_текст](cells-formatting_1.png)

Тип границы зависит от того, где она добавлена. Например, верхняя граница добавляется к верхнему положению ячейки. Пользователи также могут изменять стиль и цвет линий границ.

С помощью Aspose.Cells разработчики могут добавлять границы и настраивать их внешний вид так же гибко, как и в Microsoft Excel.
### **Добавление границ к Cells**
 Aspose.Cells предоставляет класс,[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) который представляет собой файл Excel Microsoft.[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) класс содержит[Рабочий листКоллекция](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)который позволяет получить доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) учебный класс.[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) класс предоставляет[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) коллекция. Каждый элемент в[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) коллекция представляет собой объект[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)учебный класс.

 Aspose.Cells обеспечивает[setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\) ) метод в[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) класс, используемый для установки стиля форматирования ячейки. Также объектом[Стиль](https://reference.aspose.com/cells/java/com.aspose.cells/Style)используется класс и предоставляет свойства для настройки параметров шрифта.
#### **Добавление границ к Cell**
 Добавьте границы к ячейке с помощью[Стиль](https://reference.aspose.com/cells/java/com.aspose.cells/Style) объекты[setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\) ) метод. Тип границы передается в качестве параметра. Все типы границ предварительно определены в[Тип границы](https://reference.aspose.com/cells/java/com.aspose.cells/BorderType)перечисление.

|**Типы границ**|**Описание**|
|:- |:- |
|[BOTTOM_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#BOTTOM_BORDER)|Нижняя граница|
|[ДИАГОНАЛЬНЫЙ_ВНИЗ](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_DOWN)|Диагональная линия сверху слева направо вниз|
|[ДИАГОНАЛЬ_ВВЕРХ](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_UP)|Диагональная линия снизу слева направо вверх|
|[LEFT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#LEFT_BORDER)|Левая пограничная линия|
|[RIGHT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#RIGHT_BORDER)|Правая пограничная линия|
|[TOP_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#TOP_BORDER)|Верхняя пограничная линия|
|[ГОРИЗОНТАЛЬНЫЙ](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#HORIZONTAL)|Только для динамического стиля, такого как условное форматирование.|
|[ВЕРТИКАЛЬНЫЙ](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#VERTICAL)|Только для динамического стиля, такого как условное форматирование.|
 Чтобы задать цвет линии, выберите цвет с помощью[Цвет](https://reference.aspose.com/cells/java/com.aspose.cells/Color) перечисление и передать его в[Стиль](https://reference.aspose.com/cells/java/com.aspose.cells/Style) объекты[setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\) ) параметр Color метода. Стили линий предварительно определены в[CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)перечисление.

|**Стили линий**|**Описание**|
|:- |:- |
|[DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT)|Представляет собой тонкую штрихпунктирную линию|
|[БРОСАТЬСЯ_ТОЧКА_ТОЧКА](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT_DOT)|Представляет собой тонкую штрихпунктирную линию|
|[ПУНКТИРНАЯ](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASHED)|Представляет пунктирную линию|
|[ПУНКТИРНЫЙ](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOTTED)|Представляет пунктирную линию|
|[ДВОЙНОЙ](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOUBLE)|Представляет собой двойную линию|
|[ВОЛОСЫ](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#HAIR)|Представляет линию роста волос.|
|[СРЕДНИЙ_БРОСАТЬСЯ_ТОЧКА](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT)|Представляет среднюю штрихпунктирную линию|
|[СРЕДНИЙ_БРОСАТЬСЯ_DOT_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT_DOT)|Представляет среднюю штрихпунктирную линию|
|[MEDIUM_DASHED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASHED)|Представляет среднюю пунктирную линию|
|[НИКТО](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#NONE)|Не представляет линию|
|[СРЕДНИЙ](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM)|Представляет среднюю линию|
|[НАКЛОННЫЙ_БРОСАТЬСЯ_ТОЧКА](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#SLANTED_DASH_DOT)|Представляет собой наклонную среднюю штрихпунктирную линию.|
|[ТОЛСТЫЙ](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THICK)|Представляет толстую линию|
|[ТОНКИЙ](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THIN)|Представляет собой тонкую линию|
 Выберите один из приведенных выше стилей линий, а затем назначьте его[Стиль](https://reference.aspose.com/cells/java/com.aspose.cells/Style)объекты[setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\)) метод.

Следующий вывод генерируется при выполнении кода ниже.

**Границы применяются со всех сторон ячейки** 

![дело:изображение_альтернативный_текст](cells-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBordersToCells-AddingBordersToCells.java" >}}
#### **Добавление границ к диапазону Cells**
 Можно добавить границы к диапазону ячеек, а не только к одной ячейке. Сначала создайте диапазон ячеек, вызвав метод[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) коллекция[createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)), который принимает следующие параметры:

- **Первый ряд**, первая строка диапазона.
- **Первая колонка**, первый столбец диапазона.
- **Количество рядов**, количество строк в диапазоне.
- **Число столбцов**, количество столбцов в диапазоне.

[createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\) ) метод возвращает[Диапазон](https://reference.aspose.com/cells/java/com.aspose.cells/Range) объект, который содержит указанный диапазон.[Диапазон](https://reference.aspose.com/cells/java/com.aspose.cells/Range) объект обеспечивает[setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders\(int,%20com.aspose.cells.Color\)) метод, который принимает следующие параметры:

- **CellBorderType**, стиль линии границы, выбранный из[CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)перечисление.
- **Цвет**, цвет линии границы, выбранный из[Цвет](https://reference.aspose.com/cells/java/com.aspose.cells/Color)перечисление.

Следующий вывод генерируется при выполнении кода ниже.

**Границы применяются к диапазону ячеек** 

![дело:изображение_альтернативный_текст](cells-formatting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBorderstoRange-AddingBorderstoRange.java" >}}
## **Цвета и палитра**
Палитра — это количество цветов, доступных для использования при создании изображения. Использование стандартизированной палитры в презентации позволяет пользователю создать единообразный вид. Каждый файл Excel Microsoft (97-2003) содержит палитру из 56 цветов, которые можно применять к ячейкам, шрифтам, линиям сетки, графическим объектам, заливкам и линиям диаграммы.

**Настройки палитры в Microsoft Excel** 

![дело:изображение_альтернативный_текст](cells-formatting_4.png)

С номером Aspose.Cells можно использовать не только существующие цвета, но и пользовательские цвета. Прежде чем использовать собственный цвет, добавьте его в палитру. В этом разделе объясняется, как добавить пользовательские цвета в палитру.
### **Добавление пользовательских цветов в палитру**
Aspose.Cells также поддерживает палитру из 56 цветов. Стандартная цветовая палитра показана выше. Если вы хотите использовать пользовательский цвет, который не определен в палитре, вам нужно будет добавить этот цвет в палитру перед использованием.

{{% alert color="primary" %}} 

В палитре всего 56 цветов. Когда вы добавляете пользовательский цвет в палитру, палитра изменяется, и любой элемент в файле, отформатированный с использованием предыдущего цвета, изменяется. Поэтому при смене палитры будьте очень осторожны. Более того, это ограничение касается только формата файлов XLS (Excel 97 - 2003), поскольку такого ограничения нет для XLSX или других расширенных форматов файлов MS Excel (2007/2010).

{{% /alert %}} 

Aspose.Cells предоставляет класс,[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), представляющий файл Excel Microsoft. Класс предоставляет[изменить палитру](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#changePalette\(com.aspose.cells.Color,%20int\)), который принимает следующие параметры для добавления пользовательского цвета для изменения палитры:

- **Пользовательский цвет**, пользовательский цвет, который нужно добавить в палитру.
- **Индекс**, индекс цвета, который будет заменен пользовательским цветом. Должно быть между 0-55.

В приведенном ниже примере пользовательский цвет добавляется в палитру перед его применением к шрифту.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndPalette-ColorsAndPalette.java" >}}
## **Цвета и фоновые узоры**
Microsoft Excel может устанавливать цвета переднего плана (контура) и фона (заливки) ячеек и шаблонов фона, как показано ниже.

**Настройка цветов и узоров фона в Microsoft Excel** 

![дело:изображение_альтернативный_текст](cells-formatting_5.png)

Aspose.Cells также гибко поддерживает эти функции. В этой теме мы научимся использовать эти функции, используя Aspose.Cells.
### **Настройка цветов и фоновых рисунков**
Aspose.Cells предоставляет класс,[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), представляющий файл Excel Microsoft.[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)класс содержит[Рабочий листКоллекция](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)который позволяет получить доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)учебный класс.[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)класс предоставляет[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)коллекция. Каждый элемент в[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)коллекция представляет собой объект[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)учебный класс.

Aspose.Cells обеспечивает[setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) метод в[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)класс, который используется для установки форматирования ячейки. Также объектом[Стиль](https://reference.aspose.com/cells/java/com.aspose.cells/Style)class можно использовать для настройки параметров шрифта.

{{% alert color="primary" %}} 

 Чтобы установить цвет переднего плана или фона ячейки, используйте[Стиль](https://reference.aspose.com/cells/java/com.aspose.cells/Style) объекты[setBackgroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor) или же[setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) характеристики. Эти свойства вступают в силу только в том случае, если[Стиль](https://reference.aspose.com/cells/java/com.aspose.cells/Style) объекты[установитьШаблон](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) свойство настроено.

{{% /alert %}} 

[setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor)Свойство задает цвет заливки ячейки.

[установитьШаблон](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) Свойство указывает шаблон фона, используемый для цвета переднего плана или фона. Aspose.Cells обеспечивает[Тип фона](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType)перечисление, которое содержит набор предопределенных типов фоновых узоров.

|**тип шаблона**|**Описание**|
|:- |:- |
|[DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_CROSSHATCH)|Представляет диагональную штриховку|
|[ДИАГОНАЛЬНАЯ_ПОЛОСА](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_STRIPE)|Представляет собой рисунок диагональной полосы|
|[СЕРЫЙ_6](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_6)|Представляет 6,25% серого узора|
|[СЕРЫЙ_12](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_12)|Представляет 12,5% серый узор|
|[СЕРЫЙ_25](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_25)|Представляет 25% серый узор|
|[СЕРЫЙ_50](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_50)|Представляет 50% серый шаблон|
|[СЕРЫЙ_75](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_75)|Представляет 75% серый узор|
|[ГОРИЗОНТАЛЬНАЯ_ПОЛОСА](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#HORIZONTAL_STRIPE)|Представляет собой рисунок с горизонтальной полосой|
|[НИКТО](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)|Не представляет фона|
|[ЗАДНИЙ ХОД_ДИАГОНАЛЬ_ПОЛОСКА](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#REVERSE_DIAGONAL_STRIPE)|Представляет собой узор из обратных диагональных полос.|
|[ТВЕРДЫЙ](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID)|Представляет сплошной узор|
|[ТОЛСТЫЙ_ДИАГОНАЛЬ_ПЕРЕКРЕСТОЧНОСТЬ](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THICK_DIAGONAL_CROSSHATCH)|Представляет толстую диагональную штриховку|
|[ТОНКИЙ_ДИАГОНАЛЬ_ПЕРЕКРЕСТОЧНОСТЬ](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_CROSSHATCH)|Представляет образец тонкой диагональной штриховки|
|[ТОНКИЙ_ДИАГОНАЛЬ_ПОЛОСКА](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_STRIPE)|Представляет собой узор из тонких диагональных полос.|
|[ТОНКИЙ_ГОРИЗОНТАЛЬНЫЙ_ПЕРЕКРЕСТОЧНОСТЬ](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_CROSSHATCH)|Представляет собой тонкую горизонтальную штриховку|
|[ТОНКИЙ_ГОРИЗОНТАЛЬНЫЙ_ПОЛОСКА](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_STRIPE)|Представляет собой узор из тонких горизонтальных полос.|
|[ТОНКИЙ_ЗАДНИЙ ХОД_ДИАГОНАЛЬНАЯ_ПОЛОСА](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_REVERSE_DIAGONAL_STRIPE)|Представляет собой узор из тонких обратных диагональных полос.|
|[ТОНКИЙ_ВЕРТИКАЛЬНЫЙ_ПОЛОСКА](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_VERTICAL_STRIPE)|Представляет собой узор из тонких вертикальных полос.|
|[ВЕРТИКАЛЬНАЯ_ПОЛОСА](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#VERTICAL_STRIPE)|Представляет собой рисунок с вертикальными полосами|
В приведенном ниже примере установлен цвет переднего плана ячейки A1, но ячейка A2 настроена так, чтобы иметь цвета переднего плана и фона с фоновым узором с вертикальными полосами.

При выполнении кода генерируется следующий вывод.

**Цвета переднего плана и фона, примененные к ячейкам с фоновыми узорами** 

![дело:изображение_альтернативный_текст](cells-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndBackground-ColorsAndBackground.java" >}}
### **Важно знать**
{{% alert color="primary" %}} 

-  Чтобы установить цвет переднего плана или фона ячейки, используйте кнопку[Стиль](https://reference.aspose.com/cells/java/com.aspose.cells/Style) объекты[Цвет переднего плана](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) или же[Фоновый цвет](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor) характеристики. Оба свойства вступят в силу, только если[Стиль](https://reference.aspose.com/cells/java/com.aspose.cells/Style) объекты[Шаблон](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) свойство настроено.
- [Цвет переднего плана](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) Свойство задает цвет тени ячейки.
[Шаблон](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) Свойство указывает тип фонового узора, используемого для цвета переднего плана или фона. Aspose.Cells предоставляет перечисление,[Тип фона](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType)который содержит набор предопределенных типов фоновых узоров.
-  Если вы выберете[BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE) значение из[Тип фона](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType) перечисление, цвет переднего плана не применяется.
 Аналогично, цвет фона не применяется, если вы выбираете[BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE) или же[BackgroundType.SOLID](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID) ценности.
-  При получении цвета заливки/затенения ячейки, если[Стиль.Шаблон](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) является[BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE), [Стиль.ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) вернется*Цвет.Пустой*.

{{% /alert %}} 
## **Форматирование выбранных символов в Cell**
[Работа с настройками шрифта](/cells/ru/java/dealing-with-font-settings/) объяснил, как форматировать ячейки, но только как форматировать содержимое целых ячеек. Что делать, если вы хотите отформатировать только выбранные символы?

Aspose.Cells поддерживает эту функцию. В этом разделе объясняется, как использовать эту функцию.
### **Форматирование выбранных символов**
Aspose.Cells предоставляет класс,[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), представляющий файл Excel Microsoft.[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)класс содержит[Рабочий листКоллекция](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)который позволяет получить доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)учебный класс.[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)класс предоставляет[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)коллекция. Каждый элемент в[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)коллекция представляет собой объект[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)учебный класс.

[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) класс предоставляет[персонажи](https://reference.aspose.com/cells/java/com.aspose.cells/cell#characters\(int,%20int\)), который принимает следующие параметры для выбора диапазона символов в ячейке:

- **Начальный индекс**, индекс символа, с которого начинается выбор.
- **Количество символов**, количество символов для выбора.

В выходном файле в ячейке A1 слово «Посетить» отформатировано шрифтом по умолчанию, но «Aspose!» жирный и синий.

**Форматирование выбранных символов** 

![дело:изображение_альтернативный_текст](cells-formatting_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}

{{% alert color="primary" %}} 

 Если вы заинтересованы в[форматирование части Rich Text в ячейке](/cells/ru/java/access-and-update-the-portions-of-rich-text-of-cell/) , рассмотрите возможность использования[Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters\(\) ) и методы Cell.setCharacters.[Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters\(\) ) следует использовать для доступа к частям текста, а затем можно вносить поправки с помощью метода Cell.setCharacters, тогда как метод**получить**метод возвращает массив[Настройка шрифта](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting) объекты, которыми можно манипулировать для установки различных свойств, таких как имя шрифта, цвет шрифта, жирность и т. д. и**установлен** можно использовать для применения изменений.

{{% /alert %}}

## **Предварительные темы**
- [Настройки выравнивания](/cells/ru/java/cells-alignment-settings/)
- [Условное форматирование](/cells/ru/java/conditional-formatting/)
- [Форматирование данных](/cells/ru/java/data-formatting/)
- [Темы и цвета Excel](/cells/ru/java/excel-2007-themes-and-colors/)
- [Работа с настройками шрифта](/cells/ru/java/dealing-with-font-settings/)
- [Формат рабочего листа Cells в рабочей книге](/cells/ru/java/format-worksheet-cells-in-a-workbook/)
- [Внедрить систему дат 1904 года](/cells/ru/java/implement-1904-date-system/)
- [Объединение и разделение Cells](/cells/ru/java/merging-and-unmerging-cells/)
- [Настройки номера](/cells/ru/java/cells-number-settings/)
- [Сохранить префикс одиночной кавычки для значения или диапазона Cell](/cells/ru/java/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Стилизация и форматирование данных](/cells/ru/java/styling-and-data-formatting/)
