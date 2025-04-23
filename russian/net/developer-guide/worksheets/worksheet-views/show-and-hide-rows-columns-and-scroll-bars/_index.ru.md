---
title: Показать и скрыть строки, столбцы и полосы прокрутки
type: docs
weight: 20
url: /ru/net/show-and-hide-rows-columns-and-scroll-bars/
description: Эта статья демонстрирует, как программно отображать и скрывать строки и столбцы листа Excel с использованием языка C# и .NET API или библиотеки. Видимость полос прокрутки может быть отрегулирована, и несколько строк и столбцов могут быть скрыты.
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет способы управления видимостью строк, столбцов и полос прокрутки листа.

{{% /alert %}}

## **Показ и скрытие строк и столбцов**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets), позволяющую разработчикам получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells), представляющую все ячейки на листе. Коллекция [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) предоставляет несколько методов для управления строками или столбцами на листе. Некоторые из них обсуждаются ниже.

### **Показать строки и столбцы**

Разработчики могут показать любую скрытую строку или столбец, вызвав методы [**UnhideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow) и [**UnhideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn) из коллекции [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Оба метода принимают два параметра:

- **Индекс строки или столбца** - индекс строки или столбца, который используется для отображения конкретной строки или столбца.
- **Высота строки или ширина столбца** - высота строки или ширина столбца, назначенные строке или столбцу после отображения.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

При восстановлении ширины скрытого столбца до ранее назначенной ширины или до его исходной ширины рекомендуется отобразить столбец с отрицательной шириной. Например: worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **Скрыть строки и столбцы**

Разработчики могут скрыть строку или столбец, вызвав методы [**HideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow) и [**HideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn) соответственно из коллекции [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Оба метода принимают индекс строки и столбца в качестве параметра для скрытия конкретной строки или столбца.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Также можно скрыть строку или столбец, установив высоту строки или ширину столбца равным 0 соответственно.

{{% /alert %}}

### **Скрыть несколько строк и столбцов**

Разработчики могут скрыть сразу несколько строк или столбцов, вызвав методы [**HideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows) и [**HideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns) из коллекции [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Оба метода принимают начальный индекс строки или столбца и количество строк или столбцов, которые должны быть скрыты.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

## **Показывать и скрывать полосы прокрутки**

Полосы прокрутки используются для навигации по содержимому любого файла. Обычно существует два типа полос прокрутки:

- Вертикальные полосы прокрутки
- Горизонтальные полосы прокрутки

Microsoft Excel также предоставляет горизонтальные и вертикальные полосы прокрутки, чтобы пользователи могли пролистывать содержимое листа Excel. Используя Aspose.Cells, разработчики могут контролировать видимость обоих типов полос прокрутки в файлах Excel.

### **Управление видимостью полос прокрутки**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), который представляет файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) предоставляет широкий набор свойств и методов для управления файлом Excel. Чтобы контролировать видимость полос прокрутки, используйте свойства класса [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) и [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible). [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) и [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) - это логические свойства, что означает, что эти свойства могут хранить только значения **true** или **false**.

#### **Отображение полос прокрутки**

Сделать полосы прокрутки видимыми, установив свойство [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) или [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) класса [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) в **true**.

#### **Скрытие полос прокрутки**

Скрыть полосы прокрутки, установив свойство [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) или [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) класса [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) в **false**.

**Пример кода**

Ниже приведен полный код, который открывает файл Excel, book1.xls, скрывает оба ползунка прокрутки, а затем сохраняет измененный файл как output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideScrollBars-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
