---
title: Форматирование данных
type: docs
weight: 80
url: /ru/java/data-formatting/
---

## **Подходы к форматированию данных в ячейках**
Общеизвестный факт, что если ячейки листа отформатированы правильно, то пользователям становится проще читать содержимое (данные) ячейки. Существует множество способов форматирования ячеек и их содержимого. Самый простой способ - отформатировать ячейки с помощью Microsoft Excel в среде WYSIWYG при создании дизайнерской таблицы. После создания дизайнерской таблицы вы можете открыть таблицу с помощью Aspose.Cells, сохранив все настройки формата вместе с таблицей. Другой способ отформатировать ячейки и их содержимое - использовать API Aspose.Cells. В этой теме мы опишем два подхода к форматированию ячеек и их содержимого с использованием API Aspose.Cells.
### **Форматирование ячеек**
Разработчики могут форматировать ячейки и их содержимое с использованием гибкого API Aspose.Cells. Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), который представляет собой файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) содержит коллекцию [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection), позволяющую получить доступ к каждому листу в файле Excel. Лист представлен классом [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). Класс [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) предоставляет коллекцию Cells. Каждый элемент коллекции [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells) представляет объект класса **Cell**.

Aspose.Cells предоставляет свойство [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) в классе [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell), используемое для задания стиля форматирования ячейки. Кроме того, Aspose.Cells также предоставляет класс [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style), который используется для того же целя. Применяйте различные виды стилей форматирования для ячеек, устанавливая их фоновые или передние цвета, границы, шрифты, горизонтальное и вертикальное выравнивание, отступ, направление текста, угол поворота и многое другое.
#### **Использование метода setStyle**
При применении различных стилей форматирования к разным ячейкам лучше использовать метод setStyle класса [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell). Ниже приведен пример использования метода setStyle для применения различных настроек форматирования к ячейке.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formatting-FormattingCellsUsingsetStyleMethod-1.java" >}}




#### **Использование объекта Style**
При применении одного и того же стиля форматирования к разным ячейкам используйте объект [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style).

1. Добавьте объект [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) в коллекцию Styles класса [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), вызвав метод createStyle класса Workbook.
1. Получите только что добавленный объект Style из коллекции Styles.
1. Установите желаемые свойства объекта Style, чтобы применить необходимые настройки форматирования.
1. Присвойте настроенный объект Style свойству Style любой желаемой ячейки.

Этот подход может значительно повысить эффективность ваших приложений и сэкономить память.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingCellsUsingStyleObject-FormattingCellsUsingStyleObject.java" >}}




#### **Применение эффектов градиентного заливки**
Чтобы применить желаемые эффекты градиентного заливки к ячейке, используйте метод setTwoColorGradient объекта стиля соответственно.
#### **Пример кода**
Нижеприведенный вывод достигается выполнением кода ниже. 

**Применение эффектов градиентного заливки** 

![todo:image_alt_text](data-formatting_1.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ApplyGradientFillEffects-ApplyGradientFillEffects.java" >}}




## **Настройка настроек выравнивания**
Любой, кто использовал Microsoft Excel для форматирования ячеек, будет знаком с настройками выравнивания в Microsoft Excel.

**Параметры выравнивания в Microsoft Excel** 

![todo:image_alt_text](data-formatting_2.png)

Как видно на приведенной выше фигуре, существуют различные варианты выравнивания:

- [Выравнивание текста](/cells/ru/java/data-formatting/) (горизонтальное и вертикальное)
- [Отступ](/cells/ru/java/data-formatting/).
- [Ориентация](/cells/ru/java/data-formatting/).
- [Управление текстом](/cells/ru/java/data-formatting/).
- [Направление текста](/cells/ru/java/data-formatting/).

Все эти настройки выравнивания полностью поддерживаются Aspose.Cells и обсуждаются более подробно ниже.
### **Настройка настроек выравнивания**
Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), который представляет собой файл Excel. Класс Workbook содержит коллекцию Worksheet, которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

Класс Worksheet предоставляет коллекцию Cells. Каждый элемент в коллекции Cells представляет объект класса [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

Aspose.Cells предоставляет метод setStyle в классе [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell), который используется для форматирования ячейки. Класс [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) предоставляет полезные свойства для настройки параметров шрифта.

Выберите любой тип выравнивания текста, используя перечисление TextAlignmentType. Предопределенные типы выравнивания текста в перечислении TextAlignmentType:

|**Типы выравнивания текста**|**Описание**|
| :- | :- |
|Bottom|Представляет выравнивание текста по нижнему краю|
|Center|Представляет выравнивание текста по центру|
|CenterAcross|Представляет выравнивание текста по центру с наложением|
|Distributed|Представляет распределенное выравнивание текста|
|Fill|Представляет выравнивание текста по заливке|
|General|Представляет общее выравнивание текста|
|Justify|Представляет выравнивание текста по ширине|
|Left|Представляет выравнивание текста влево|
|Right|Представляет выравнивание текста вправо|
|Top|Представляет верхнее выравнивание текста|
{{% alert color="primary" %}} 

Также можно применить настройку равномерного распределения с помощью метода Style.setJustifyDistributed().

{{% /alert %}} 
#### **Горизонтальное выравнивание**
Используйте метод setHorizontalAlignment объекта [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style), чтобы выровнять текст горизонтально.

Следующий результат достигается при выполнении приведенного ниже примера кода:

**Выравнивание текста горизонтально** 

![todo:image_alt_text](data-formatting_3.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentHorizontal-TextAlignmentHorizontal.java" >}}




#### **Вертикальное выравнивание**
Используйте метод setVerticalAlignment объекта [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style), чтобы выровнять текст вертикально.

Следующий результат достигается, когда VerticalAlignment установлено в центр.

**Выравнивание текста вертикально** 

![todo:image_alt_text](data-formatting_4.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentVertical-TextAlignmentVertical.java" >}}




### **Отступ**
Возможно установить уровень отступа текста в ячейке, используя метод setIndentLevel объекта [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style).

Следующий вывод получается при установке уровня отступа равным 2.

**Уровень отступа установлен на 2** 

![todo:image_alt_text](data-formatting_5.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Indentation-ImportingfromResultSet.java" >}}




### **Ориентация**
Установка ориентации (поворота) текста в ячейке с помощью метода setRotationAngle объекта [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style).

Следующий вывод получается при установке угла поворота равным 25.

**Угол поворота установлен на 25** 

![todo:image_alt_text](data-formatting_6.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Orientation-Orientation.java" >}}




### **Управление текстом**
В следующем разделе рассматривается управление текстом с помощью установки переноса текста, уменьшения для подгонки и других параметров форматирования.
#### **Перенос текста**
Перенос текста в ячейке упрощает его чтение: высота ячейки автоматически ajusts для размещения всего текста вместо его обрезания или переполнения смежными ячейками.

Установите перенос текста включенным или выключенным с помощью метода setTextWrapped объекта [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style).

Следующий вывод получается при включении переноса текста.

**Текст перенесен внутри ячейки** 

![todo:image_alt_text](data-formatting_7.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WrapText-WrapText.java" >}}




#### **Уменьшение для подгонки**
Опция переноса текста в ячейке состоит в уменьшении размера текста для соответствия размерам ячейки. Это делается путем установки свойства IsTextWrapped объекта [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) в **true**.

Следующий вывод получается при уменьшении текста для соответствия ячейке.

**Текст уменьшен для соответствия границам ячейки** 

![todo:image_alt_text](data-formatting_8.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ShrinkingToFit-ShrinkingToFit.java" >}}




#### **Объединение ячеек**
Как и Microsoft Excel, Aspose.Cells поддерживает объединение нескольких ячеек в одну.

Следующий результат достигается, если объединить три ячейки в первой строке, чтобы создать большую одиночную ячейку.

**Три ячейки объединены для создания большой ячейки** 

![todo:image_alt_text](data-formatting_9.png)

Используйте метод Merge коллекции [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells) для объединения ячеек. Метод Merge принимает следующие параметры:

- Первая строка, первая строка, с которой начинается объединение.
- Первая колонка, первая колонка, с которой начинается объединение.
- Количество строк, количество строк для объединения.
- Количество столбцов, количество столбцов для объединения.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MergingCellsInWorksheet-MergingCellsInWorksheet.java" >}}




### **Направление текста**
Возможно установить порядок чтения текста в ячейках. Порядок чтения - это визуальный порядок, в котором отображаются символы, слова и т.д. Например, английский - это язык с направлением слева направо, в то время как арабский - справа налево.

Порядок чтения устанавливается с помощью свойства TextDirection объекта [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style). Aspose.Cells предоставляет предопределенные типы направления текста в перечислении TextDirectionType.

|** Типы направления текста **| ** Описание ** |
| :- | :- |
|Context|Порядок чтения согласуется с языком первого введенного символа|
|LeftToRight|Порядок чтения слева направо|
|RightToLeft|Порядок чтения справа налево|






{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ChangeTextDirection-ChangeTextDirection.java" >}}





Следующий результат достигается, если направление чтения текста установлено справа налево.

**Установка направления чтения текста справа налево** 

![todo:image_alt_text](data-formatting_10.png)
## **Форматирование выбранных символов в ячейке**
[Работа с настройками шрифта](/cells/ru/java/dealing-with-font-settings/) объяснил, как форматировать ячейки, но только как форматировать содержимое всей ячейки. Что если вы хотите отформатировать только выбранные символы?

Aspose.Cells поддерживает эту функцию. В этой теме объясняется, как использовать эту функцию.
### **Форматирование выбранных символов**
Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), который представляет файл Microsoft Excel. Класс Workbook содержит коллекцию Worksheets, которая позволяет получить доступ к каждому листу в файл Excel. Лист представлен классом [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). Класс Worksheet предоставляет коллекцию Cells. Каждый элемент в коллекции Cells представляет объект класса [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

Класс Cell предоставляет метод characters, который принимает следующие параметры для выбора диапазона символов в ячейке:

- **Индекс начала**, индекс начального символа для выбора.
- **Количество символов**, количество выбираемых символов.

В выходном файле, в ячейке A1, слово 'Visit' форматируется стандартным шрифтом, но 'Aspose!' выделено жирным и синим.

**Форматирование выбранных символов** 

![todo:image_alt_text](data-formatting_11.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}







{{% alert color="primary" %}} 

Если вас интересует [форматирование части Rich Text в [ячейке](/cells/ru/java/access-and-update-the-portions-of-rich-text-of-cell/), рассмотрите использование методов Cell.getCharacters & Cell.setCharacters. Метод Cell.getCharacters используется для доступа к частям текста, и затем изменения могут быть сделаны с использованием метода Cell.setCharacters, тогда как метод **get** возвращает массив объектов FontSetting, которые могут быть изменены для установки различных свойств, таких как название шрифта, цвет шрифта, жирность и т. д., и метод **set** может быть использован для применения изменений.

{{% /alert %}} 
## **Активация листов и установка активной ячейки или выбор диапазона ячеек на листе**
Иногда вам может потребоваться активировать определенный лист, чтобы он был первым, который отображается, когда кто-то открывает файл в Microsoft Excel. Вам также может понадобиться активировать определенную ячейку таким образом, чтобы полосы прокрутки прокручивались к активной ячейке, чтобы она была четко видна. Aspose.Cells способен выполнить все вышеупомянутые задачи.

Активным листом является лист, над которым вы работаете в книге. По умолчанию имя на вкладке активного листа выделено жирным. Активная ячейка, между тем, - это выбранная ячейка, в которую вводятся данные при начале ввода. Одновременно активной ячейкой является только одна ячейка. Активная ячейка окружена тяжелой рамкой, чтобы она выделялась среди других ячеек. Aspose.Cells также позволяет выбирать диапазон ячеек на листе.
### **Активация листа и установка активной ячейки**
Aspose.Cells предоставляет специальный API для этих задач. Например, метод WorksheetCollection.setActiveSheetIndex полезен для установки активного листа. Аналогично, метод Worksheet.setActiveCell используется для установки и получения активной ячейки на листе.

Если вы хотите, чтобы горизонтальные и вертикальные полосы прокрутки прокручивались к позиции индекса строки и столбца для обеспечения хорошего вида выбранных данных при открытии файла в Microsoft Excel, используйте свойства Worksheet.setFirstVisibleRow и Worksheet.setFirstVisibleColumn.

В следующем примере показано, как активировать лист и сделать в нем активной ячейку. Полосы прокрутки прокручиваются, чтобы сделать 2-й ряд и 2-й столбец их первым видимым рядом и столбцом.

**Установить ячейку B2 в качестве активной ячейки** 

![todo:image_alt_text](data-formatting_12.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MakeCellActive-MakeCellActive.java" >}}




#### **Выбор диапазона ячеек на листе**
Aspose.Cells предоставляет метод Worksheet.selectRange(int startRow, int startColumn, int totalRows, int totalColumns, bool removeOthers). Используя последний параметр - removeOthers - true, выбор других ячеек или диапазонов ячеек на листе удаляется.

В следующем примере показано, как выбрать диапазон ячеек на активном листе.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SelectRangeofCellsinWorksheet-SelectRangeofCellsinWorksheet.java" >}}







{{% alert color="primary" %}} 

Все вышеперечисленные классы и методы доступны в лицензированной версии Aspose.Cells.

{{% /alert %}} 
## **Форматирование строк и столбцов**
Форматирование строк и столбцов в таблице для создания отчета —, вероятно, наиболее широко используемая функция приложения Excel.There is an introductory phrase fragment. Consider revising. Экспоненты.Aspose.Cells API-интерфейсы также предоставляют эту функциональность через свою модель данных, путем открытия класса Style, который в основном обрабатывает все связанные с оформлением функции, такие как шрифт и его атрибуты, выравнивание текста, цвета фона/переднего плана, границы, формат отображения для чисел и литералов даты и так далее. Еще один полезный класс, который предоставляют API Aspose.Cells-это StyleFlag, который позволяет повторное использование объекта Style. 

В данной статье мы постараемся объяснить, как использовать Aspose.Cells for Java API для применения форматирования к строкам и столбцам. 
### **Форматирование строк и столбцов**
Aspose.Cells предоставляет класс, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), который представляет собой файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) содержит коллекцию рабочих листов, что позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом Worksheet. Класс [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) предоставляет коллекцию Cells. Коллекция Cells предоставляет коллекцию Rows.
#### **Форматирование строки**
Каждый элемент в коллекции Rows представляет объект Row. Объект Row предлагает метод applyStyle, используемый для применения форматирования к строке.

Чтобы применить одно и то же форматирование к строке, используйте объект Style:

1. Добавьте объект Style к классу Workbook, вызвав его метод createStyle.
1. Установите свойства объекта Style для применения параметров форматирования.
1. Назначьте настроенный объект Style методу applyStyle объекта Row.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingARow-FormattingARow.java" >}}




#### **Форматирование столбца**
Коллекция Cells предоставляет коллекцию столбцов. Каждый элемент в коллекции Columns представляет объект Column. Аналогично объекту Row, объект Column предлагает метод applyStyle, используемый для установки форматирования столбца. Используйте метод applyStyle объекта Column для форматирования столбца также, как и строку.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingAColumn-FormattingAColumn.java" >}}




#### **Установка формата отображения чисел и дат для строк и столбцов**
Если требуется установить формат отображения чисел и дат для целой строки или столбца, то процесс примерно тот же, что и обсуждался выше, однако вместо установки параметров для текстового содержимого, вы будете устанавливать форматирование для чисел и дат с использованием Style.Number или Style.Custom. Обратите внимание, что свойство Style.Number имеет тип integer и относится к встроенным числовым и датам форматам, тогда как свойство Style.Custom имеет тип string и принимает допустимые шаблоны.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingDisplayFormat-SettingDisplayFormat.java" >}}







{{% alert color="primary" %}} 

Пожалуйста, ознакомьтесь с подробной статьей по [Установке форматов отображения чисел и [дат](/cells/ru/java/data-formatting/).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
