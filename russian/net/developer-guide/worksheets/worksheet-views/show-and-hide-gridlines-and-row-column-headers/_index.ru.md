---
title: Показать и скрыть линии сетки и заголовки столбцов строк
type: docs
weight: 30
url: /ru/net/show-and-hide-gridlines-and-row-column-headers/
description: В этой статье представлен пример кода для использования библиотеки C# API или .NET для программного скрытия или отображения линий сетки, заголовков строк и столбцов листа Excel.
---
{{% alert color="primary" %}}

Aspose.Cells поддерживает скрытие и отображение линий сетки рабочего листа, которые видны по умолчанию. Он также обеспечивает контроль видимости заголовков столбцов строк рабочего листа.

{{% /alert %}}

## **Показать и скрыть линии сетки**

Все рабочие листы Excel имеют линии сетки по умолчанию. Они помогают разграничить ячейки, чтобы было легко вводить данные в определенные ячейки. Линии сетки позволяют нам рассматривать рабочий лист как набор ячеек, где каждую ячейку легко идентифицировать.

### **Управление видимостью линий сетки**

Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook), представляющий файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook)класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)коллекция, которая позволяет разработчикам получать доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Класс предоставляет широкий спектр свойств и методов для управления рабочим листом. Для управления видимостью линий сетки используйте[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) имущество.[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) является логическим свойством, что означает, что оно может хранить только**истинный** или же**ЛОЖЬ** стоимость.

#### **Делаем линии сетки видимыми**

 Сделайте линии сетки видимыми, установив[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) собственность на**истинный**.

#### **Скрытие линий сетки**

 Скройте линии сетки, установив[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) собственность на**ЛОЖЬ**.

 Ниже приведен полный пример, демонстрирующий использование[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible)свойство, открыв файл Excel (book1.xls), скрыв линии сетки на первом листе и сохранив измененный файл как output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideGridlines-1.cs" >}}

## **Показать и скрыть заголовки столбцов строк**

Все рабочие листы в файле Excel состоят из ячеек, расположенных в строках и столбцах. Все строки и столбцы имеют уникальные значения, которые используются для их идентификации и идентификации отдельных ячеек. Например, строки пронумерованы — 1, 2, 3, 4 и т. д. — а столбцы упорядочены в алфавитном порядке — A, B, C, D и т. д. Значения строк и столбцов отображаются в заголовках. Используя Aspose.Cells, разработчики могут контролировать видимость этих заголовков строк и столбцов.

### **Управление видимостью рабочих листов**

Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook), представляющий файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook)класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)коллекция, которая позволяет разработчикам получать доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Класс предоставляет широкий спектр свойств и методов для управления рабочим листом. Чтобы управлять видимостью заголовков строк и столбцов, используйте[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс[**Исровколумнхедерсвидибле**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) имущество.[**Исровколумнхедерсвидибле**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) является логическим свойством, что означает, что оно может хранить только**истинный** или же**ЛОЖЬ**стоимость.

#### **Отображение заголовков строк/столбцов**

 Сделайте заголовки строк и столбцов видимыми, установив[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс[**Исровколумнхедерсвидибле**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) собственность на**истинный**.

#### **Скрытие заголовков строк/столбцов**

 Скройте заголовки строк и столбцов, установив[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс[**Исровколумнхедерсвидибле**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) собственность на**ЛОЖЬ**.

Ниже приведен полный пример, который показывает, как использовать[**Исровколумнхедерсвидибле**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible)свойство, открыв файл Excel (book1.xls), скрыв заголовки строк и столбцов на первом рабочем листе и сохранив измененный файл как output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideRowColumnHeaders-1.cs" >}}

{{% alert color="primary" %}}

 Также можно использовать[**UnhideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows) и[**Показать столбцы**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns) методы[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) класс, чтобы сделать несколько строк и столбцов видимыми.

{{% /alert %}}
