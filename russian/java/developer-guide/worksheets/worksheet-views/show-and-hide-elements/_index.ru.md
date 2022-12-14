---
title: Показать и скрыть элементы
type: docs
weight: 60
url: /ru/java/show-and-hide-elements/
---
{{% alert color="primary" %}}

Aspose.Cells позволяет пользователю отображать и скрывать элементы книги, включая рабочие листы, строки, столбцы, вкладки, полосы прокрутки, линии сетки,

{{% /alert %}}

## **Показать и скрыть рабочий лист**

 Файл Excel может иметь один или несколько рабочих листов. Всякий раз, когда мы создаем файл Excel, мы добавляем рабочие листы в файл Excel, в котором мы работаем. Каждый рабочий лист в файле Excel независим от другого рабочего листа, поскольку имеет свои собственные данные, настройки форматирования и т. д. Иногда разработчикам может потребоваться сделать несколько рабочих листов скрытыми, а другие видимыми в файле Excel для их собственных интересов. Так,**Aspose.Cells** позволяет разработчикам контролировать видимость рабочих листов в своих файлах Excel.

**Управление видимостью рабочих листов:**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) который представляет файл Excel.[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) класс содержит[**Рабочий листКоллекция**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)что позволяет получить доступ к каждому рабочему листу в файле Excel.

 Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Класс предоставляет широкий спектр свойств и методов для управления рабочим листом. Но для управления видимостью рабочего листа разработчики могут использовать[**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) метод[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) учебный класс.

### **Делаем рабочий лист видимым**

 Разработчики могут сделать рабочий лист видимым, передав**истинный** как параметр к[**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) метод[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) учебный класс.

### **Скрытие рабочего листа**

 Разработчики могут скрыть рабочий лист, передав**ЛОЖЬ** как параметр к[**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) метод[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) учебный класс.

**Пример:**

 Ниже приведен полный пример, демонстрирующий использование[**setVisible (ложь)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) метод[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) класс, чтобы скрыть первый рабочий лист файла Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-HideUnhideWorksheet-1.java" >}}

**Рабочий лист - до изменения:**

 На скриншоте ниже вы можете видеть, что**Книга1.xls** файл содержит три рабочих листа:**Лист1** , **Лист2** а также**Лист3** .

![дело:изображение_альтернативный_текст](show-and-hide-elements_1.png)

**Фигура:** Просмотр рабочего листа до внесения каких-либо изменений

**Рабочий лист — после выполнения примера кода:**

**Книга1.xls** файл открывается с помощью[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) класс, а затем первый рабочий лист**Книга1.xls** файл сделан скрытым. Измененный файл сохраняется как**вывод.xls**файл, графический вид которого показан ниже:

![дело:изображение_альтернативный_текст](show-and-hide-elements_2.png)

**Фигура:** Вид рабочего листа после модификации

**Установка типа видимости**

 Вы также можете скрыть рабочие листы особым образом. Эта функция может скрыть рабочий лист, так что единственный способ снова сделать его видимым — дать[**Тип видимости.VERY_HIDDEN**](https://reference.aspose.com/cells/java/com.aspose.cells/visibilitytype#VERY_HIDDEN) как значение параметра для[**setVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType) метод в коде (здесь следует отметить, что пользователь не может сделать объект видимым в MS Excel напрямую, используя его пункты меню). Пользователи также могут использовать[**getVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType) метод, чтобы проверить, помечен ли лист как VeryHidden или нет.

## **Показать или скрыть вкладки**

Если вы внимательно посмотрите в конец файла Excel Microsoft, вы увидите ряд элементов управления. Это включает:

- Вкладки листа.
- Кнопки прокрутки вкладок.

Вкладки листов представляют рабочие листы в файле Excel. Щелкните любую вкладку, чтобы переключиться на этот рабочий лист. Чем больше рабочих листов в рабочей книге, тем больше вкладок листов. Если в файле Excel много рабочих листов, вам нужны кнопки для навигации по ним. Итак, Microsoft Excel предоставляет кнопки прокрутки вкладок для прокрутки вкладок листа.

**Вкладки листов и кнопки прокрутки вкладок**

![дело:изображение_альтернативный_текст](show-and-hide-elements_3.png)

Используя Aspose.Cells, разработчики могут контролировать видимость вкладок листа и кнопок прокрутки вкладок в файлах Excel.

**Управление видимостью вкладок:**
 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , представляющий файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Класс предоставляет широкий спектр свойств и методов для управления файлом Excel.

### **Скрытие вкладок**

 Скрыть вкладки в файле Excel, установив[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) учебный класс'[**getSettings().setShowTabs(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs) метод.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

### **Делаем вкладки видимыми**

 Сделайте вкладки видимыми с помощью[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) учебный класс'[**getSettings().setShowTabs(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs) метод.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayTab-1.java" >}}

**Полный пример кода:**

Ниже приведен полный пример, который открывает файл Excel (book1.xls), скрывает его вкладки и сохраняет измененный файл как output.xls.

Вы можете видеть, что файл Book1.xls содержит вкладки на рисунке ниже. После выполнения кода примера вкладки скрыты, как видно из скриншота файла output.xls ниже.

**book1.xls: файл Excel до каких-либо изменений**

![дело:изображение_альтернативный_текст](show-and-hide-elements_4.png)

**output.xls: файл Excel после модификации**

![дело:изображение_альтернативный_текст](show-and-hide-elements_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

## **Показать и скрыть строки и столбцы**

Все рабочие листы в файле Excel состоят из ячеек, расположенных в строках и столбцах. Все строки и столбцы имеют уникальные значения, которые используются для их идентификации и идентификации отдельных ячеек. Например, строки пронумерованы — 1, 2, 3, 4 и т. д. — а столбцы упорядочены в алфавитном порядке — A, B, C, D и т. д. Значения строк и столбцов отображаются в заголовках. Используя Aspose.Cells, разработчики могут контролировать видимость этих заголовков строк и столбцов.

**Управление видимостью рабочих листов:**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), представляющий файл Excel Microsoft. Класс Workbook содержит коллекцию WorksheetCollection, которая обеспечивает доступ к каждому рабочему листу в файле Excel.

 Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)учебный класс. Класс Worksheet предоставляет широкий набор свойств и методов для управления рабочими листами. Чтобы управлять видимостью заголовков строк и столбцов, используйте класс Worksheet.[**setRowColumnHeadersVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) метод.

### **Скрытие заголовков строк/столбцов**

 Скрыть заголовки строк и столбцов с помощью[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) учебный класс'[**setRowColumnHeadersVisible (ложь)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) метод.

### **Отображение заголовков строк/столбцов**

 Сделайте заголовки строк и столбцов видимыми с помощью[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) учебный класс'[**setRowColumnHeadersVisible (истина)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) метод.

 Ниже приведен полный пример, демонстрирующий, как использовать[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) учебный класс'[**setRowColumnHeadersVisible (ложь)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) способ скрыть заголовки строк и столбцов первого рабочего листа файла Excel.

На приведенном ниже снимке экрана показано, что Book1.xls содержит три рабочих листа: Sheet1, Sheet2 и Sheet3. Каждый рабочий лист показывает заголовки строк и столбцов.

**Book1.xls: рабочий лист до изменения**

![дело:изображение_альтернативный_текст](show-and-hide-elements_6.png)

 Book1.xls открывается с помощью[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class», а заголовки строк и столбцов на первом листе скрыты. Измененный файл сохраняется как output.xls.

**Вид рабочего листа после модификации**

![дело:изображение_альтернативный_текст](show-and-hide-elements_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideUnhideWorksheet-1.java" >}}

## **Показать и скрыть полосы прокрутки**

Полосы прокрутки очень часто используются для навигации по содержимому любого файла. Обычно существует два вида полос прокрутки:

- Вертикальные полосы прокрутки
- Горизонтальные полосы прокрутки

Microsoft Excel также предоставляет горизонтальные и вертикальные полосы прокрутки, чтобы пользователи могли прокручивать содержимое рабочего листа. Используя Aspose.Cells, разработчики могут управлять видимостью обоих типов полос прокрутки в файлах Excel.

**Управление видимостью полос прокрутки:**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) который представляет файл Excel.[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Класс предоставляет широкий спектр свойств и методов для управления файлом Excel. Но для управления видимостью полос прокрутки в файле Excel разработчики могут использовать[**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) & [**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) методы[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) учебный класс.

### **Скрытие полос прокрутки**

 Скройте полосы прокрутки, установив[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) учебный класс'[**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) или же[**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) методы**ЛОЖЬ**.

### **Делаем полосы прокрутки видимыми**

 Сделайте полосы прокрутки видимыми, установив класс Workbook.[**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) или же[**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) методы**истинный**.

**Полный пример кода:**

Ниже приведен полный код, который открывает файл Excel, book1.xls, скрывает обе полосы прокрутки, а затем сохраняет измененный файл как output.xls.

На снимке экрана ниже показан файл Book1.xls, содержащий обе полосы прокрутки. Измененный файл сохраняется как файл output.xls, также показанный ниже.

**Book1.xls: файл Excel до каких-либо изменений**

![дело:изображение_альтернативный_текст](show-and-hide-elements_8.png)

**output.xls: файл Excel после модификации**

![дело:изображение_альтернативный_текст](show-and-hide-elements_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-DisplayHideScrollBars-1.java" >}}

## **Показать и скрыть линии сетки**

Все рабочие листы Excel Microsoft имеют линии сетки по умолчанию. Они помогают разграничить ячейки, чтобы было легко вводить данные в определенные ячейки. Линии сетки позволяют нам рассматривать рабочий лист как набор ячеек, где каждую ячейку легко идентифицировать.

Aspose.Cells также позволяет контролировать видимость линий сетки.

### **Управление видимостью линий сетки**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) который представляет собой файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) класс содержит[**Рабочий листКоллекция**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) который позволяет получить доступ к каждому рабочему листу в файле.

 Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Класс предоставляет широкий спектр свойств и методов для управления рабочими листами. Для управления видимостью линий сетки используйте[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) учебный класс'[**setGridlinesVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) метод.

#### **Делаем линии сетки видимыми**

 Чтобы сделать линии сетки видимыми, используйте кнопку[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) учебный класс'[**setGridlinesVisible (истина)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) метод.

#### **Скрытие линий сетки**

 Скрыть линии сетки с помощью[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) учебный класс'[**setGridlinesVisible (ложь)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) метод.

{{% alert color="primary" %}}

Линии сетки применяются ко всему листу. Чтобы «скрыть» линии сетки в разделе рабочего листа, используйте[форматирование границ](/cells/ru/java/create-table-by-using-border-lines-for-a-range/) чтобы установить для границ цвет, который сочетается с цветовой схемой листа.

{{% /alert %}}

**Пример: скрытие линий сетки на определенном рабочем листе**

 Пример ниже демонстрирует использование[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) учебный класс'[**setGridlinesVisible (ложь)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) способ скрыть линии сетки первого рабочего листа файла Excel.

На приведенном ниже снимке экрана показано, что файл Book1.xls содержит три рабочих листа: Sheet1, Sheet2 и Sheet3. Все эти рабочие листы имеют линии сетки.

**Вид рабочего листа до изменения**

![дело:изображение_альтернативный_текст](show-and-hide-elements_10.png)

 Файл Book1.xls открывается с помощью[**Рабочая тетрадь**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class, а затем линии сетки первого рабочего листа скрываются. Измененный файл сохраняется как файл output.xls.

**Вид рабочего листа после модификации**

![дело:изображение_альтернативный_текст](show-and-hide-elements_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayHideGridlines-DisplayHideGridlines.java" >}}

### **Статьи по Теме**

{{% alert color="primary" %}}

- [Особенности настройки страницы](/cells/ru/java/page-setup-features/).
- [Добавление границ к ячейкам для создания таблицы](/cells/ru/java/create-table-by-using-border-lines-for-a-range/).

{{% /alert %}}
