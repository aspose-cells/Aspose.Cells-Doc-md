---
title: Показать и скрыть столбцы строк и полосы прокрутки
type: docs
weight: 20
url: /ru/net/show-and-hide-rows-columns-and-scroll-bars/
description: В этой статье показано, как программно отображать и скрывать строки и столбцы листа Excel с помощью языка C# и .NET API или библиотеки. Можно настроить видимость полос прокрутки, а некоторые строки и столбцы можно скрыть.
---
{{% alert color="primary" %}}

Aspose.Cells предоставляет способы управления видимостью строк, столбцов и полос прокрутки рабочего листа.

{{% /alert %}}

## **Показать и скрыть строки и столбцы**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , представляющий файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) коллекция, которая позволяет разработчикам получать доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс предоставляет[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) коллекция, представляющая все ячейки рабочего листа.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collection предоставляет несколько методов для управления строками или столбцами на листе. Некоторые из них обсуждаются ниже.

### **Показать строки и столбцы**

 Разработчики могут показать любую скрытую строку или столбец, вызвав метод[**UnhideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow) и[**Показать столбец**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn) методы[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)сборник соответственно. Оба метода принимают два параметра:

- **Индекс строки или столбца** - индекс строки или столбца, который используется для отображения конкретной строки или столбца.
- **Высота строки или ширина столбца** - высота строки или ширина столбца, назначенная строке или столбцу после отображения.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

При отображении скрытого столбца, если вам нужно восстановить его ранее заданную ширину или исходную ширину, отобразите столбец с отрицательной шириной. Например: рабочий лист.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **Скрыть строки и столбцы**

 Разработчики могут скрыть строку или столбец, вызвав метод[**HideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow) и[**СкрытьКолонку**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn) методы[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)сборник соответственно. Оба метода принимают индекс строки и столбца в качестве параметра, чтобы скрыть конкретную строку или столбец.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Также можно скрыть строку или столбец, установив для высоты строки или ширины столбца значение 0 соответственно.

{{% /alert %}}

### **Скрыть несколько строк и столбцов**

 Разработчики могут скрыть сразу несколько строк или столбцов, вызвав метод[**HideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows) и[**Скрыть столбцы**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns) методы[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)сборник соответственно. Оба метода принимают в качестве параметров начальный индекс строки или столбца и количество строк или столбцов, которые должны быть скрыты.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

## **Показать и скрыть полосы прокрутки**

Полосы прокрутки используются для навигации по содержимому любого файла. Обычно существует два вида полос прокрутки:

- Вертикальные полосы прокрутки
- Горизонтальные полосы прокрутки

Microsoft Excel также предоставляет горизонтальные и вертикальные полосы прокрутки, чтобы пользователи могли прокручивать содержимое рабочего листа. Используя Aspose.Cells, разработчики могут управлять видимостью обоих типов полос прокрутки в файлах Excel.

### **Управление видимостью полос прокрутки**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook)который представляет файл Excel.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Класс предоставляет широкий спектр свойств и методов для управления файлом Excel. Для управления видимостью полос прокрутки используйте[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) учебный класс'[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) и[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) характеристики.[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) и[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) являются логическими свойствами, что означает, что эти свойства могут хранить только**истинный** или же**ЛОЖЬ** ценности.

#### **Делаем полосы прокрутки видимыми**

 Сделайте полосы прокрутки видимыми, установив[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) учебный класс'[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) или же[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) собственность на**истинный**.

#### **Скрытие полос прокрутки**

 Скройте полосы прокрутки, установив[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) учебный класс'[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) или же[**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) собственность на**ЛОЖЬ**.

**Образец кода**

Ниже приведен полный код, который открывает файл Excel, book1.xls, скрывает обе полосы прокрутки, а затем сохраняет измененный файл как output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideScrollBars-1.cs" >}}
