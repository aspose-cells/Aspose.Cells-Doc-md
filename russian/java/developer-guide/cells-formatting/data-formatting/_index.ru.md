---
title: Форматирование данных
type: docs
weight: 80
url: /ru/java/data-formatting/
---
## **Подходы к форматированию данных в Cells**
Общеизвестно, что если ячейки рабочего листа отформатированы правильно, пользователям становится легче читать содержимое (данные) ячейки. Существует множество способов форматирования ячеек и их содержимого. Самый простой способ — отформатировать ячейки с помощью Microsoft Excel в среде WYSIWYG при создании электронной таблицы конструктора. После того, как электронная таблица конструктора создана, вы можете открыть электронную таблицу, используя Aspose.Cells, сохраняя все настройки формата, сохраненные вместе с электронной таблицей. Другой способ форматирования ячеек и их содержимого — использование Aspose.Cells API. В этом разделе мы опишем два подхода к форматированию ячеек и их содержимого с использованием Aspose.Cells API.
### **Форматирование Cells**
 Разработчики могут форматировать ячейки и их содержимое, используя гибкий API из Aspose.Cells. Aspose.Cells предоставляет класс,[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , представляющий файл Excel Microsoft.[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) класс содержит[Рабочий листКоллекция](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) который позволяет получить доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) учебный класс.[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) класс предоставляет коллекцию Cells. Каждый элемент в[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells)коллекция представляет собой объект**Cell** учебный класс.

 Aspose.Cells обеспечивает[Стиль](https://reference.aspose.com/cells/java/com.aspose.cells/style) имущество в[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) класс, используемый для установки стиля форматирования ячейки. Кроме того, Aspose.Cells также обеспечивает[Стиль](https://reference.aspose.com/cells/java/com.aspose.cells/style) класс, который используется для той же цели. Применяйте к ячейкам различные стили форматирования, чтобы задать цвета фона или переднего плана, границы, шрифты, горизонтальное и вертикальное выравнивание, уровень отступа, направление текста, угол поворота и многое другое.
#### **Использование метода setStyle**
 При применении разных стилей форматирования к разным ячейкам лучше использовать метод setStyle класса[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) учебный класс. Ниже приведен пример, демонстрирующий использование метода setStyle для применения различных параметров форматирования к ячейке.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formatting-FormattingCellsUsingsetStyleMethod-1.java" >}}




#### **Использование объекта стиля**
 Применяя один и тот же стиль форматирования к разным ячейкам, используйте[Стиль](https://reference.aspose.com/cells/java/com.aspose.cells/style) объект.

1.  Добавить[Стиль](https://reference.aspose.com/cells/java/com.aspose.cells/style) объект коллекции стилей[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) класса, вызвав метод createStyle класса Workbook.
1. Получите доступ к недавно добавленному объекту Style из коллекции Styles.
1. Задайте нужные свойства объекта «Стиль», чтобы применить нужные параметры форматирования.
1. Назначьте настроенный объект Style свойству Style любой нужной ячейки.

Такой подход может значительно повысить эффективность ваших приложений и сэкономить память.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingCellsUsingStyleObject-FormattingCellsUsingStyleObject.java" >}}




#### **Применение эффектов градиентной заливки**
Чтобы применить нужные эффекты градиентной заливки к ячейке, используйте метод setTwoColorGradient объекта Style соответствующим образом.
#### **Пример кода**
 Следующий вывод достигается путем выполнения приведенного ниже кода.

**Применение эффектов градиентной заливки** 

![дело:изображение_альтернативный_текст](data-formatting_1.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ApplyGradientFillEffects-ApplyGradientFillEffects.java" >}}




## **Настройка параметров выравнивания**
Любой, кто использовал Microsoft Excel для форматирования ячеек, будет знаком с настройками выравнивания в Microsoft Excel.

**Настройки выравнивания в Microsoft Excel** 

![дело:изображение_альтернативный_текст](data-formatting_2.png)

Как видно из рисунка выше, существуют различные варианты выравнивания:

- [Выравнивание текста](/cells/ru/java/data-formatting/) (горизонтальное вертикальное)
- [Отступ](/cells/ru/java/data-formatting/).
- [Ориентация](/cells/ru/java/data-formatting/).
- [Текстовое управление](/cells/ru/java/data-formatting/).
- [Направление текста](/cells/ru/java/data-formatting/).

Все эти настройки выравнивания полностью поддерживаются Aspose.Cells и более подробно обсуждаются ниже.
### **Настройка параметров выравнивания**
 Aspose.Cells предоставляет класс,[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , который представляет файл Excel. Класс Workbook содержит коллекцию WorksheetCollection, которая обеспечивает доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) учебный класс.

 Класс Worksheet предоставляет коллекцию Cells. Каждый элемент в коллекции Cells представляет собой объект[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) учебный класс.

Aspose.Cells предоставляет метод setStyle в[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) класс, который используется для форматирования ячейки.[Стиль](https://reference.aspose.com/cells/java/com.aspose.cells/style) класс предоставляет полезные свойства для настройки параметров шрифта.

Выберите любой тип выравнивания текста, используя перечисление TextAlignmentType. Предопределенные типы выравнивания текста в перечислении TextAlignmentType:

|**Типы выравнивания текста**|**Описание**|
|:- |:- |
|Нижний|Представляет выравнивание текста по нижнему краю|
|Центр|Представляет выравнивание текста по центру|
|CenterAcross|Представляет центр по выравниванию текста|
|Распределенный|Представляет распределенное выравнивание текста|
|Наполнять|Представляет выравнивание заливки текста|
|Общий|Представляет общее выравнивание текста|
|Оправдывать|Представляет выравнивание текста по ширине|
|Оставил|Представляет выравнивание текста по левому краю|
|Верно|Представляет выравнивание текста по правому краю|
|верхний|Представляет выравнивание текста по верхнему краю|
{{% alert color="primary" %}} 

Вы также можете применить настройку распределенного выравнивания с помощью метода Style.setJustifyDistributed().

{{% /alert %}} 
#### **Горизонтальное выравнивание**
 Использовать[Стиль](https://reference.aspose.com/cells/java/com.aspose.cells/style) метод setHorizontalAlignment объекта для выравнивания текста по горизонтали.

Следующий результат достигается путем выполнения приведенного ниже примера кода:

**Выравнивание текста по горизонтали** 

![дело:изображение_альтернативный_текст](data-formatting_3.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentHorizontal-TextAlignmentHorizontal.java" >}}




#### **Вертикальное выравнивание**
 Использовать[Стиль](https://reference.aspose.com/cells/java/com.aspose.cells/style) метод setVerticalAlignment объекта для выравнивания текста по вертикали.

Следующий вывод достигается, когда для параметра VerticalAlignment установлено значение center.

**Выравнивание текста по вертикали** 

![дело:изображение_альтернативный_текст](data-formatting_4.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentVertical-TextAlignmentVertical.java" >}}




### **Отступ**
 Можно установить уровень отступа текста в ячейке с помощью[Стиль](https://reference.aspose.com/cells/java/com.aspose.cells/style) метод setIndentLevel объекта.

Следующий вывод достигается, когда для IndentLevel установлено значение 2.

**Уровень отступа изменен на 2** 

![дело:изображение_альтернативный_текст](data-formatting_5.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Indentation-ImportingfromResultSet.java" >}}




### **Ориентация**
 Задайте ориентацию (поворот) текста в ячейке кнопкой[Стиль](https://reference.aspose.com/cells/java/com.aspose.cells/style) метод setRotationAngle объекта.

Следующий вывод достигается, когда угол поворота установлен на 25.

**Угол поворота установлен на 25** 

![дело:изображение_альтернативный_текст](data-formatting_6.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Orientation-Orientation.java" >}}




### **Текстовое управление**
В следующем разделе обсуждается, как управлять текстом, устанавливая обтекание текстом, уменьшая размер и другие параметры форматирования.
#### **Обтекание текста**
Обтекание текста в ячейке облегчает чтение: высота ячейки подстраивается под весь текст, вместо того, чтобы обрезать его или распространяться на соседние ячейки.

 Включите или выключите обтекание текстом с помощью[Стиль](https://reference.aspose.com/cells/java/com.aspose.cells/style) метод setTextWrapped объекта.

Следующий вывод достигается, когда включен перенос текста.

**Текст, заключенный внутри ячейки** 

![дело:изображение_альтернативный_текст](data-formatting_7.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WrapText-WrapText.java" >}}




#### **Уменьшение размера**
 Вариант переноса текста в поле — уменьшить размер текста, чтобы он соответствовал размерам ячейки. Это делается путем установки[Стиль](https://reference.aspose.com/cells/java/com.aspose.cells/style) свойство объекта IsTextWrapped для**истинный**.

Следующий вывод достигается, когда текст сжимается, чтобы соответствовать ячейке.

**Текст сжат, чтобы соответствовать границам ячейки** 

![дело:изображение_альтернативный_текст](data-formatting_8.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ShrinkingToFit-ShrinkingToFit.java" >}}




#### **Объединение Cells**
Как и Microsoft Excel, Aspose.Cells поддерживает объединение нескольких ячеек в одну.

Следующий результат достигается, если три ячейки в первой строке объединяются для создания большой одиночной ячейки.

**Три ячейки объединились, чтобы создать большую ячейку** 

![дело:изображение_альтернативный_текст](data-formatting_9.png)

 Использовать[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells) Метод Merge коллекции для объединения ячеек. Метод Merge принимает следующие параметры:

- Первая строка, первая строка, с которой нужно начать слияние.
- Первый столбец, первый столбец, с которого следует начать слияние.
- Количество строк, количество строк для объединения.
- Количество столбцов, количество столбцов для объединения.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MergingCellsInWorksheet-MergingCellsInWorksheet.java" >}}




### **Направление текста**
Можно задать порядок чтения текста в ячейках. Порядок чтения — это визуальный порядок, в котором отображаются символы, слова и т. д. Например, английский — язык с письмом слева направо, а арабский — язык с письмом справа налево.

 Порядок чтения устанавливается с помощью[Стиль](https://reference.aspose.com/cells/java/com.aspose.cells/style) свойство TextDirection объекта. Aspose.Cells предоставляет предварительно определенные типы направления текста в перечислении TextDirectionType.

|**Типы направления текста**|**Описание**|
|:- |:- |
|Контекст|Порядок чтения соответствует языку первого введенного символа|
|Слева направо|Порядок чтения слева направо|
|Справа налево|Порядок чтения справа налево|






{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ChangeTextDirection-ChangeTextDirection.java" >}}





Следующий вывод достигается, если порядок чтения текста установлен справа налево.

**Установка порядка чтения текста справа налево** 

![дело:изображение_альтернативный_текст](data-formatting_10.png)
## **Форматирование выбранных символов в Cell**
[Работа с настройками шрифта](/cells/ru/java/dealing-with-font-settings/)объяснил, как форматировать ячейки, но только как форматировать содержимое всех ячеек. Что делать, если вы хотите отформатировать только выбранные символы?

Aspose.Cells поддерживает эту функцию. В этом разделе объясняется, как использовать эту функцию.
### **Форматирование выбранных символов**
 Aspose.Cells предоставляет класс,[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , представляющий файл Excel Microsoft. Класс Workbook содержит коллекцию Worksheets, которая обеспечивает доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) учебный класс. Класс Worksheet предоставляет коллекцию Cells. Каждый элемент в коллекции Cells представляет собой объект[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) учебный класс.

Класс Cell предоставляет метод символов, который принимает следующие параметры для выбора диапазона символов в ячейке:

- **Начальный индекс**, индекс символа, с которого начинается выбор.
- **Количество символов**, количество символов для выбора.

В выходном файле в ячейке A1 слово «Посетить» отформатировано шрифтом по умолчанию, но «Aspose!» жирный и синий.

**Форматирование выбранных символов** 

![дело:изображение_альтернативный_текст](data-formatting_11.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}







{{% alert color="primary" %}} 

 Если вы заинтересованы в[форматирование части форматированного текста в [ячейке]](/cells/ru/java/access-and-update-the-portions-of-rich-text-of-cell/) , рассмотрите возможность использования методов Cell.getCharacters и Cell.setCharacters. Метод Cell.getCharacters должен использоваться для доступа к частям текста, а затем можно вносить поправки с помощью метода Cell.setCharacters, тогда как метод**получить** Метод возвращает массив объектов FontSetting, которыми можно манипулировать, чтобы установить различные свойства: имя шрифта, цвет шрифта, жирность и т. д.**установлен** можно использовать для применения изменений.

{{% /alert %}} 
## **Активация листов и создание активного Cell или выбор диапазона Cells на рабочем листе**
Иногда вам может потребоваться активировать определенный рабочий лист, чтобы он отображался первым, когда кто-то открывает файл в Microsoft Excel. Вам также может понадобиться активировать определенную ячейку таким образом, чтобы полосы прокрутки прокручивались до активной ячейки, чтобы она была хорошо видна. Aspose.Cells способен выполнять все вышеперечисленные задачи.

Активный лист — это лист, над которым вы работаете в книге. Имя на вкладке активного листа по умолчанию выделено полужирным шрифтом. Между тем, активная ячейка — это выбранная ячейка, в которую вводятся данные, когда вы начинаете печатать. Одновременно активна только одна ячейка. Активная ячейка окружена толстой рамкой, чтобы она выделялась на фоне других ячеек. Aspose.Cells также позволяет выбрать диапазон ячеек на листе.
### **Активация листа и активация Cell**
Aspose.Cells предоставляет специальный номер API для этих задач. Например, метод WorksheetCollection.setActiveSheetIndex полезен для установки активного листа. Точно так же метод Worksheet.setActiveCell используется для установки и получения активной ячейки на листе.

Если вы хотите, чтобы горизонтальные и вертикальные полосы прокрутки прокручивались до позиции индекса строки и столбца, чтобы обеспечить хороший обзор выбранных данных при открытии файла в Microsoft Excel, используйте свойства Worksheet.setFirstVisibleRow и Worksheet.setFirstVisibleColumn.

В следующем примере показано, как активировать рабочий лист и сделать ячейку в нем активной. Полосы прокрутки прокручиваются, чтобы сделать 2-ю строку и 2-й столбец их первой видимой строкой и столбцом.

**Установка ячейки B2 в качестве активной ячейки** 

![дело:изображение_альтернативный_текст](data-formatting_12.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MakeCellActive-MakeCellActive.java" >}}




#### **Выбор диапазона Cells на рабочем листе**
Aspose.Cells предоставляет метод Worksheet.selectRange(int startRow, int startColumn, int totalRows, int totalColumns, bool removeOthers). При установке последнего параметра — removeOthers — в значение true другие выбранные ячейки или диапазоны ячеек на листе удаляются.

В следующем примере показано, как выбрать диапазон ячеек на активном листе.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SelectRangeofCellsinWorksheet-SelectRangeofCellsinWorksheet.java" >}}







{{% alert color="primary" %}} 

Все вышеперечисленные классы и методы доступны в лицензионной версии Aspose.Cells.

{{% /alert %}} 
## **Форматирование строк и столбцов**
Форматирование строк и столбцов в электронной таблице для придания отчету вида, возможно, является наиболее широко используемой функцией приложения Excel. Aspose.Cells API-интерфейсы также предоставляют эту функциональность через свою модель данных, предоставляя класс Style, который в основном обрабатывает все функции, связанные со стилем, такие как шрифт и его атрибуты, выравнивание текста, цвета фона/переднего плана, границы, формат отображения для литералов чисел и дат и т. д. . Другим полезным классом, предоставляемым API Aspose.Cells, является StyleFlag, который позволяет повторно использовать объект Style.

В этой статье мы попытаемся объяснить, как использовать Aspose.Cells for Java API для форматирования строк и столбцов.
### **Форматирование строк и столбцов**
 Aspose.Cells предоставляет класс,[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) который представляет собой файл Excel Microsoft.[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) содержит коллекцию WorksheetCollection, которая обеспечивает доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен классом Worksheet.[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) класс предоставляет коллекцию Cells. Коллекция Cells содержит коллекцию строк.
#### **Форматирование строки**
Каждый элемент в коллекции Rows представляет объект Row. Объект Row предлагает метод applyStyle, используемый для применения форматирования к строке.

Чтобы применить такое же форматирование к строке, используйте объект Style:

1. Добавьте объект Style в класс Workbook, вызвав его метод createStyle.
1. Задайте свойства объекта Style, чтобы применить настройки форматирования.
1. Назначьте настроенный объект Style методу applyStyle объекта Row.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingARow-FormattingARow.java" >}}




#### **Форматирование столбца**
Коллекция Cells содержит коллекцию Columns. Каждый элемент в коллекции Columns представляет объект Column. Подобно объекту Row, объект Column предлагает метод applyStyle, используемый для установки форматирования столбца. Используйте метод applyStyle объекта Column, чтобы отформатировать столбец так же, как и строку.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingAColumn-FormattingAColumn.java" >}}




#### **Настройка формата отображения чисел и дат для строк и столбцов**
Если требуется установить формат отображения чисел и дат для полной строки или столбца, то процесс более или менее такой же, как описано выше, однако вместо установки параметров для текстового содержимого вы будете устанавливать форматирование для чисел и даты, используя Style.Number или Style.Custom. Обратите внимание, что свойство Style.Number имеет целочисленный тип и относится к встроенным форматам чисел и дат, тогда как свойство Style.Custom имеет строковый тип и принимает допустимые шаблоны.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingDisplayFormat-SettingDisplayFormat.java" >}}







{{% alert color="primary" %}} 

 Пожалуйста, ознакомьтесь с подробной статьей о[Настройка форматов отображения чисел и [дат]](/cells/ru/java/data-formatting/).

{{% /alert %}}
