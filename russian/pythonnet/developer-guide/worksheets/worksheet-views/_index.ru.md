---
title: Представления листа
type: docs
weight: 40
url: /ru/python-net/worksheet-views/
description: В этой статье будет описано, как использовать API Aspose.Cells для Python via .NET для взаимодействия с предпросмотром разрывов страниц в рабочей книге и листах Excel. Работайте со SplitPane, замороженными панелями и масштабом. 
keywords: Библиотека Excel для Python, Как установить режим предварительного просмотра разрывов страниц, Как включить нормальный режим, Как установить масштаб, Как заморозить панели, Как разбить панели, Как удалить панели.
---

## **Предпросмотр разрывов страниц**

Все листы могут быть просмотрены в двух режимах:

- Обычный вид.
- Предварительный просмотр разрыва страницы.

Нормальный режим — это режим просмотра по умолчанию для рабочего листа. Предпросмотр разрывов страниц — это режим редактирования, который отображает лист так, как он будет напечатан. Предпросмотр показывает, какие данные попадут на каждую страницу, чтобы вы могли настроить область печати и разрывы страниц. Используя Aspose.Cells для Python via .NET, разработчики могут включать режим нормального просмотра или предпросмотр разрывов страниц.

### **Управление режимами просмотра**

Aspose.Cells для Python via .NET предоставляет класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), который представляет собой файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets), которая позволяет получать доступ к каждому листу в файле Excel.

Таблица представлена классом. Класс предоставляет широкий спектр свойств и методов для управления таблицами. Чтобы включить обычный или режим предварительного просмотра разрыва страницы, используйте свойство класса. Это логическое свойство, которое может хранить только значение **true** или **false**.

#### **Включение нормального режима**

Установите таблицу в обычный вид, установив свойство класса в **false**.

#### **Включение предварительного просмотра разрывов страниц**

Установите любую таблицу в режим предварительного просмотра разрыва страницы, установив свойство класса в **true**. Таким образом, таблица переключится из обычного вида в режим предварительного просмотра разрыва страницы.

Приведен полный пример ниже, демонстрирующий, как использовать свойство для включения режима просмотра предварительного просмотра разрыва страницы для первой таблицы файла Excel.

Файл book1.xls открывается созданием экземпляра класса. Просмотр переключается на предварительный просмотр разрыва страницы для первой таблицы, установив свойство в **true**. Измененный файл сохраняется как output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-PageBreakPreview-1.py" >}}

## **Коэффициент масштабирования**

### **Использование Microsoft Excel**

Microsoft Excel предоставляет возможность установить коэффициент масштабирования листа. Эта функция помогает пользователям просматривать содержимое листа в уменьшенном или увеличенном виде. Пользователи могут установить коэффициент масштабирования на любое значение.

### **Aspose.Cells и коэффициент увеличения**

Aspose.Cells позволяет разработчикам установить коэффициент увеличения таблицы.
Aspose.Cells предоставляет класс, который представляет файл Microsoft Excel. Класс содержит коллекцию, которая позволяет получить доступ к каждой таблице в файле Excel.

Таблица представлена классом. Класс предоставляет широкий спектр свойств и методов для управления таблицами. Чтобы установить коэффициент увеличения таблицы, используйте свойство класса. Коэффициент увеличения устанавливается путем назначения числового (целочисленного) значения свойству.

Ниже приведен полный пример, демонстрирующий, как использовать свойство [**zoom**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/zoom) для установки коэффициента масштабирования первого листа файла Excel.

Файл book1.xls открывается путем создания экземпляра класса [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook). Коэффициент масштабирования первого листа устанавливается на 75, и измененный файл сохраняется как output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-ZoomFactor-1.py" >}}

## **Закрепить области**

### **Использование Microsoft Excel**

Закрепление области экрана - это функция, предоставляемая Microsoft Excel. Закрепление области экрана позволяет выбрать данные, которые останутся видимыми при прокрутке на листе.

### **Aspose.Cells и заморозка панелей**

Aspose.Cells позволяет разработчикам применять замороженные панели к листам во время выполнения.

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets), которая позволяет получить доступ к каждому листу в файле Excel.

Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) предоставляет широкий спектр свойств и методов для управления листами. Чтобы настроить заморозку панелей, вызовите метод [**freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#int-int-int-int) класса Worksheet. Метод [**freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#int-int-int-int) принимает следующие параметры:

- **row**, индекс строки ячейки, с которой начнется закрепление.
- **column**, индекс столбца ячейки, с которой начнется закрепление.
- **frozen_rows**, количество видимых строк в верхней панели.
- **frozen_columns**, количество видимых столбцов в левой панели

Файл book1.xls открывается путем вызова конструктора класса [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) при его создании, и в первом листе замораживается несколько строк и столбцов. Измененный файл сохраняется как output.xls.

Ниже приведен полный пример, показывающий, как использовать метод [**freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#str-int-int) для замораживания строк и столбцов (начиная с C4, представленного 4-й строкой и 3-й колонкой, где строки и столбцы начинаются с индекса 0) первого листа файла Excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-FreezePanes-1.py" >}}

## **Разделение областей экрана**

Если вам нужно разделить экран для получения двух разных представлений на одном листе, используйте разделение областей экрана. Microsoft Excel предлагает очень удобную функцию, которая позволяет просматривать более одной копии вашего листа и прокручивать каждую область листа независимо: разделение областей экрана.

Разделы работают одновременно. Если вы внесете изменение в один, изменение одновременно появится в другом. Aspose.Cells предоставляет функцию разделения панелей для пользователей.

### **Применение и удаление разделенных панелей**

#### **Разделение панелей**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) , который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) предоставляет широкий спектр свойств и методов для управления файлом Excel. Чтобы реализовать разделенные виды, используйте метод [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) класса [**split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split). Чтобы удалить разделение панелей, используйте метод [**remove_split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/remove_split).

В примере мы используем простой шаблонный файл, который загружается, затем устанавливается функция разделенных панелей для ячейки на первом листе. Обновленный файл сохраняется.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-SplitPanes-1.py" >}}

После выполнения вышеуказанного кода сгенерированный файл будет иметь разделенный вид.

#### **Удаление панелей**

Удаление разделенных панелей с использованием метода [**remove_split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/remove_split).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-RemovePanes-1.py" >}}

## **Продвинутые темы**
- [Скрытие отображения нулевых значений в таблице](/cells/ru/python-net/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Установить цвет вкладки листа](/cells/ru/python-net/set-worksheet-tab-color/)
- [Показывать и скрывать линии сетки и заголовки строк и столбцов](/cells/ru/python-net/show-and-hide-gridlines-and-row-column-headers/)
- [Показывать и скрывать строки, столбцы и полосы прокрутки](/cells/ru/python-net/show-and-hide-rows-columns-and-scroll-bars/)
- [Показать и скрыть листы и вкладки](/cells/ru/python-net/show-and-hide-worksheets-and-tabs/)
- [Показывать формулы вместо значений в листе](/cells/ru/python-net/show-formulas-instead-of-values-in-a-worksheet/)
- [Использовать параметры проверки ошибок](/cells/ru/python-net/use-error-checking-options/)

{{< app/cells/assistant language="python-net" >}}
