---
title: Представления рабочего листа
type: docs
weight: 40
url: /ru/net/worksheet-views/
---
## **Предварительный просмотр разрыва страницы**

Все рабочие листы можно просматривать в двух режимах:

- Нормальный вид.
- Предварительный просмотр разрыва страницы.

Обычный вид — это вид рабочего листа по умолчанию. Предварительный просмотр разрыва страницы — это режим редактирования, в котором рабочий лист отображается в том виде, в котором он будет напечатан. Предварительный просмотр разрыва страницы показывает, какие данные будут размещены на каждой странице, поэтому вы можете настроить область печати и разрывы страниц. Используя Aspose.Cells, разработчики могут включить режимы обычного просмотра или предварительного просмотра с разрывом страницы.

### **Управление режимами просмотра**

Aspose.Cells предоставляет[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс, представляющий файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel.

 Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Класс предоставляет широкий спектр свойств и методов для управления рабочими листами. Чтобы включить обычный режим или режим предварительного просмотра с разрывом страницы, используйте кнопку[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс[**Испажебреакпревью**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) имущество.[**Испажебреакпревью**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) является логическим свойством, что означает, что оно может хранить только**истинный** или**ЛОЖЬ** ценность.

#### **Включение обычного просмотра**

 Установите рабочий лист в обычный вид, установив[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс[**Испажебреакпревью**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) собственность на**ЛОЖЬ**.

#### **Включение предварительного просмотра разрыва страницы**

 Установите любой рабочий лист для предварительного просмотра разрыва страницы, установив[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс[**Испажебреакпревью**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) собственность на**истинный**При этом рабочий лист переключается с обычного вида на предварительный просмотр разрыва страницы.

 Ниже приведен полный пример, демонстрирующий, как использовать[**Испажебреакпревью**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)чтобы включить режим предварительного просмотра разрыва страницы для первого рабочего листа файла Excel.

Файл book1.xls открывается путем создания экземпляра[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) учебный класс. Представление переключается на предварительный просмотр разрыва страницы для первого рабочего листа путем установки параметра[**Испажебреакпревью**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)собственность на**истинный**. Измененный файл сохраняется как output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-PageBreakPreview-1.cs" >}}

## **Коэффициент масштабирования**

### **Использование Microsoft Excel**

Microsoft Excel предоставляет функцию, которая позволяет пользователям устанавливать масштаб рабочего листа или коэффициент масштабирования. Эта функция помогает пользователям просматривать содержимое рабочего листа в уменьшенном или увеличенном виде. Пользователи могут установить коэффициент масштабирования на любое значение.

### **Aspose.Cells и коэффициент масштабирования**

Aspose.Cells позволяет разработчикам устанавливать коэффициент масштабирования рабочего листа.
Aspose.Cells предоставляет[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс, представляющий файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel.

 Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Класс предоставляет широкий спектр свойств и методов для управления рабочими листами. Чтобы установить коэффициент масштабирования рабочего листа, используйте кнопку[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс'[**Увеличить**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom)имущество. Коэффициент масштабирования задается путем присвоения числового (целочисленного) значения[**Увеличить**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom) имущество.

Ниже приведен полный пример, демонстрирующий, как использовать[**Увеличить**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom) Свойство для установки коэффициента масштабирования первого рабочего листа файла Excel.

Файл book1.xls открывается путем создания экземпляра[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook)учебный класс. Коэффициент масштабирования первого листа устанавливается равным 75, а измененный файл сохраняется как output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-ZoomFactor-1.cs" >}}

## **Замерзшие оконные стекла**

### **Использование Microsoft Excel**

Закрепить области — это функция, предоставляемая Microsoft Excel. Замораживание панелей позволяет выбрать данные, которые будут оставаться видимыми при прокрутке рабочего листа.

### **Aspose.Cells и стопорные панели**

Aspose.Cells позволяет разработчикам применять области закрепления к рабочим листам во время выполнения.

Aspose.Cells предоставляет[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook)класс, представляющий файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook)класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel.

Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Класс предоставляет широкий спектр свойств и методов для управления рабочими листами. Чтобы настроить области закрепления, вызовите класс Worksheet.[**Замерзшие оконные стекла**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index)метод.[**Замерзшие оконные стекла**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index)метод принимает следующие параметры:

- **Строка**, индекс строки ячейки, с которой начнется замораживание.
- **Столбец**, индекс столбца ячейки, с которой начнется замораживание.
- **Замороженные строки**, количество видимых строк в верхней панели.
- **Замороженные столбцы**, количество видимых столбцов на левой панели

Файл book1.xls открывается вызовом[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook)class' при создании его экземпляра, а несколько строк и столбцов заморожены на первом листе. Измененный файл сохраняется как output.xls.

 Ниже приведен полный пример, который показывает, как использовать[**Замерзшие оконные стекла**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index)метод для замораживания строк и столбцов (начиная с C4, представленного 4-й строкой и 3-м столбцом, где строки и столбцы начинаются с индекса 0) первого рабочего листа файла Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-FreezePanes-1.cs" >}}

## **Разделить панели**

Если вам нужно разделить экран, чтобы получить два разных представления на одном листе, разделите панели. Microsoft Excel предлагает очень удобную функцию, позволяющую просматривать несколько копий рабочего листа и иметь возможность независимо прокручивать каждую панель рабочего листа: разделение панелей.

Панели работают одновременно. Если вы вносите изменения в один, это изменение одновременно появляется и в другом. Aspose.Cells предоставляет пользователям функцию разделения панелей.

### **Применение и удаление разделенных панелей**

#### **Разделение панелей**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) который представляет собой файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Класс предоставляет широкий спектр свойств и методов для управления файлом Excel. Чтобы реализовать разделенные представления, используйте[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс'[**Расколоть**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/split) . Чтобы удалить разделенные панели, используйте[**УдалитьСплит**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/removesplit)метод.

В этом примере мы используем простой файл шаблона, который загружается, а затем к ячейке на первом рабочем листе применяется функция установки разделенных панелей. Обновленный файл сохраняется.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-SplitPanes-1.cs" >}}

После запуска приведенного выше кода сгенерированный файл будет иметь разделенное представление.

#### **Удаление панелей**

 Удалите разделенные панели с помощью[**УдалитьСплит**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/removesplit)метод.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-RemovePanes-1.cs" >}}

## **Предварительные темы**
- [Скрытие отображения нулевых значений на рабочем листе](/cells/ru/net/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Установить цвет вкладки рабочего листа](/cells/ru/net/set-worksheet-tab-color/)
- [Показать и скрыть линии сетки и заголовки столбцов строк](/cells/ru/net/show-and-hide-gridlines-and-row-column-headers/)
- [Показать и скрыть столбцы строк и полосы прокрутки](/cells/ru/net/show-and-hide-rows-columns-and-scroll-bars/)
- [Показать и скрыть рабочие листы и вкладки](/cells/ru/net/show-and-hide-worksheets-and-tabs/)
- [Показывать формулы вместо значений на листе](/cells/ru/net/show-formulas-instead-of-values-in-a-worksheet/)
- [Используйте параметры проверки ошибок](/cells/ru/net/use-error-checking-options/)

