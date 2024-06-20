---
title: Показ и скрытие элементов
type: docs
weight: 60
url: /ru/java/show-and-hide-elements/
---

{{% alert color="primary" %}}

Aspose.Cells позволяет пользователю показывать и скрывать элементы книги, включая листы, строки, столбцы, вкладки, полосы прокрутки, линии сетки.

{{% /alert %}}

## **Показать и скрыть лист**

Файл Excel может содержать один или более листов. Всякий раз, когда мы создаем файл Excel, мы добавляем листы в файл Excel, в котором работаем. Каждый лист в файле Excel независим от другого листа и имеет свои собственные данные и настройки форматирования и т. д. Иногда разработчики могут захотеть скрыть несколько листов и сделать другие видимыми в файле Excel по своему усмотрению. Таким образом, **Aspose.Cells** позволяет разработчикам контролировать видимость листов в их файлах Excel.

**Контроль видимости листов:**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), который представляет собой файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) содержит [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection), позволяющий получить доступ к каждому листу в файле Excel.

Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) предоставляет широкий спектр свойств и методов для управления листом. Однако для управления видимостью листа разработчики могут использовать метод [**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) класса [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

### **Сделать лист видимым**

Разработчики могут сделать лист видимым, передавая **true** в качестве параметра в метод [**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) класса [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

### **Скрыть лист**

Разработчики могут скрыть лист, передавая **false** в качестве параметра в метод [**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) класса [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

**Пример:**

Ниже приведен полный пример, демонстрирующий использование метода [**setVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) класса [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) для скрытия первого листа файла Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-HideUnhideWorksheet-1.java" >}}

**Лист - Перед изменением:**

На скриншоте ниже вы можете увидеть, что файл **Book1.xls** содержит три листа: **Sheet1**, **Sheet2** и **Sheet3**.

![todo:image_alt_text](show-and-hide-elements_1.png)

**Рисунок:** Вид листа перед любыми изменениями

**Лист - После выполнения примера кода:**

Файл **Book1.xls** открыт с помощью класса [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), а затем первый лист файла **Book1.xls** скрыт. Измененный файл сохранен как **output.xls**, визуальное представление которого показано ниже:

![todo:image_alt_text](show-and-hide-elements_2.png)

**Рисунок:** Вид листа после изменения

**Установка VisibilityType**

Вы также можете скрыть листы специальным образом. Эта функция может скрыть лист так, чтобы единственный способ снова сделать его видимым - передать значение [**VisibilityType.VERY_HIDDEN**](https://reference.aspose.com/cells/java/com.aspose.cells/visibilitytype#VERY_HIDDEN) в качестве параметра для метода [**setVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType) в коде (здесь следует отметить, что пользователи не могут сделать объект видимым в MS Excel непосредственно, используя его меню). Пользователи также могут использовать метод [**getVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType), чтобы проверить, помечен ли лист как "Очень скрыт" или нет.

## **Показать или скрыть вкладки**

Если вы внимательно посмотрите внизу файла Microsoft Excel, вы увидите ряд элементов управления. Среди них:

- Вкладки листов.
- Кнопки прокрутки вкладок.

Вкладки представляют листы Excel-файла. Щелкните на любой вкладке, чтобы переключиться на этот лист. Чем больше листов в книге Excel, тем больше вкладок. Если в Excel-файле большое количество листов, вам понадобятся кнопки для перемещения по ним. Поэтому Microsoft Excel предоставляет кнопки прокрутки вкладок для прокрутки по вкладкам.

**Вкладки листов и кнопки прокрутки вкладок**

![todo:image_alt_text](show-and-hide-elements_3.png)

С помощью Aspose.Cells разработчики могут контролировать видимость вкладок листов и кнопок прокрутки в файле Excel.

**Контроль видимости вкладок:**
Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), представляющий файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) предоставляет широкий спектр свойств и методов для управления файлом Excel.

### **Скрытие вкладок**

Скрыть вкладки в файле Excel, установив метод [**getSettings().setShowTabs(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs) класса [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

### **Отображение вкладок**

Отобразить вкладки с помощью метода [**getSettings().setShowTabs(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs) класса [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayTab-1.java" >}}

**Полный пример кода:**

Ниже приведен полный пример, который открывает файл Excel (book1.xls), скрывает его вкладки и сохраняет измененный файл с именем output.xls.

Вы можете увидеть, что файл Book1.xls содержит вкладки на рисунке ниже. После выполнения примерного кода вкладки скрыты, как видно на скриншоте файла output.xls ниже.

**book1.xls: Файл Excel перед любыми модификациями**

![todo:image_alt_text](show-and-hide-elements_4.png)

**output.xls: Файл Excel после изменений**

![todo:image_alt_text](show-and-hide-elements_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

## **Показ и скрытие строк и столбцов**

Все листы в файле Excel состоят из ячеек, которые располагаются в строках и столбцах. Все строки и столбцы имеют уникальные значения, которые используются для их идентификации и для идентификации отдельных ячеек. Например, строки пронумерованы – 1, 2, 3, 4 и т. д., а столбцы упорядочены по алфавиту – A, B, C, D и т. д. Значения строк и столбцов отображаются в заголовках. С помощью Aspose.Cells разработчики могут контролировать видимость этих заголовков строк и столбцов.

**Контроль видимости листов:**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), представляющий файл Microsoft Excel. Класс Workbook содержит WorksheetCollection, которая позволяет получить доступ к каждому листу в файле Excel.

Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). Класс Worksheet предоставляет широкий спектр свойств и методов для управления листами. Для контроля видимости заголовков строк и столбцов используйте метод класса Worksheet [**setRowColumnHeadersVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible).

### **Скрытие заголовков строк/столбцов**

Скрыть заголовки строк и столбцов, используя метод класса [**setRowColumnHeadersVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) класса [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

### **Отображение заголовков строк/столбцов**

Сделать заголовки строк и столбцов видимыми, используя метод класса [**setRowColumnHeadersVisible(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) класса [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

Приведен полный пример ниже, демонстрирующий, как использовать метод класса [**setRowColumnHeadersVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) класса [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) для скрытия заголовков строк и столбцов первого листа Excel.

На снимке экрана ниже показано, что в файле Book1.xls содержатся три листа Excel: Лист1, Лист2 и Лист3. Каждый лист отображает заголовки строк и столбцов.

**Book1.xls: лист перед внесением изменений**

![todo:image_alt_text](show-and-hide-elements_6.png)

Файл Book1.xls открыт с использованием класса [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), и заголовки строк и столбцов на первом листе скрыты. Измененный файл сохраняется как output.xls.

**Просмотр листа после изменений**

![todo:image_alt_text](show-and-hide-elements_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideUnhideWorksheet-1.java" >}}

## **Показывать и скрывать полосы прокрутки**

Полосы прокрутки широко используются для навигации по содержимому любого файла. Обычно существует два типа полос прокрутки:

- Вертикальные полосы прокрутки
- Горизонтальные полосы прокрутки

Microsoft Excel также предоставляет горизонтальные и вертикальные полосы прокрутки, чтобы пользователи могли пролистывать содержимое листа Excel. Используя Aspose.Cells, разработчики могут контролировать видимость обоих типов полос прокрутки в файлах Excel.

**Управление видимостью полос прокрутки:**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), представляющий файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) предоставляет широкий спектр свойств и методов для управления файлом Excel. Однако для управления видимостью полос прокрутки в файле Excel разработчики могут использовать методы [**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) и [**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) класса [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook).

### **Скрытие полос прокрутки**

Скрыть полосы прокрутки, установив методы [**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) или [**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) класса [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) в **false**.

### **Отображение полос прокрутки**

Сделать полосы прокрутки видимыми, установив методы [**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) класса Workbook в **true**.

**Полный пример кода:**

Ниже приведен полный код, который открывает файл Excel, book1.xls, скрывает оба ползунка прокрутки, а затем сохраняет измененный файл как output.xls.

На скриншоте ниже показан файл Book1.xls, содержащий оба ползунка прокрутки. Измененный файл сохранен как файл output.xls, также показан ниже.

**Book1.xls: Файл Excel до любых изменений**

![todo:image_alt_text](show-and-hide-elements_8.png)

**output.xls: Файл Excel после изменений**

![todo:image_alt_text](show-and-hide-elements_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-DisplayHideScrollBars-1.java" >}}

## **Отображение и скрытие линий сетки**

Все листы Microsoft Excel по умолчанию имеют линии сетки. Они помогают выделить ячейки, поэтому легко вводить данные в конкретные ячейки. Линии сетки позволяют нам видеть лист как совокупность ячеек, где каждая ячейка легко идентифицируема.

Aspose.Cells также позволяет вам контролировать видимость линий сетки.

### **Управление видимостью линий сетки**

Aspose.Cells предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) содержит объект [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection), который позволяет получить доступ к каждому листу в файле.

Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) предоставляет широкий спектр свойств и методов для управления листами. Чтобы контролировать видимость линий сетки, используйте метод класса [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) объекта [**setGridlinesVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible).

#### **Отображение линий сетки**

Чтобы отобразить линии сетки, используйте метод [**setGridlinesVisible(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) класса [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

#### **Скрытие линий сетки**

Скрыть линии сетки, используя метод [**setGridlinesVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) класса [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

{{% alert color="primary" %}}

Линии сетки применяются ко всему листу. Чтобы 'скрыть' линии сетки на части листа, используйте [форматирование границ](/cells/ru/java/create-table-by-using-border-lines-for-a-range/) для установки границ определенного цвета, который сочетается с цветовой схемой листа.

{{% /alert %}}

**Пример: Скрытие линий сетки на конкретном листе**

Приведенный ниже пример демонстрирует использование метода [**setGridlinesVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) класса [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) для скрытия линий сетки первого листа файла Excel.

На скриншоте ниже показано, что файл Book1.xls содержит три листа: Лист1, Лист2 и Лист3. У всех этих листов есть линии сетки.

**Вид листа перед изменениями**

![todo:image_alt_text](show-and-hide-elements_10.png)

Файл Book1.xls открывается с использованием класса [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), а затем линии сетки первого листа скрываются. Измененный файл сохраняется как файл output.xls.

**Просмотр листа после изменений**

![todo:image_alt_text](show-and-hide-elements_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayHideGridlines-DisplayHideGridlines.java" >}}

### **Связанные статьи**

{{% alert color="primary" %}}

- [Функции настройки страницы](/cells/ru/java/page-setup-features/).
- [Добавление границ ячеек для создания таблицы](/cells/ru/java/create-table-by-using-border-lines-for-a-range/).

{{% /alert %}}
