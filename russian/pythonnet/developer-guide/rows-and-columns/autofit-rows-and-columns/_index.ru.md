---
title: Автоподбор строк и столбцов
type: docs
weight: 20
url: /ru/python-net/autofit-rows-and-columns/
description: Эта статья показывает, как автоматически подгонять строки, столбцы, строки объединенных ячеек и строку в диапазоне ячеек с помощью API Aspose.Cells для Python via .NET.
keywords: Библиотека Python Excel, Python Автоподгонка строк, Python автоподгонка столбцов, Python автоподгонка строки в диапазоне ячеек, Python автоподгонка строк объединенных ячеек.
---

{{% alert color="primary" %}}

Microsoft Excel позволяет пользователям автоматически подгонять ширину и высоту ячеек в соответствии с их содержимым. Эта функция также доступна через Aspose.Cells для Python via .NET, поэтому разработчики могут автоматически подгонять размеры ячейки во время выполнения.

{{% /alert %}}

## **Автоматическая подгонка размера**

Aspose.Cells для Python via .NET предоставляет класс, который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) предоставляет широкий спектр свойств и методов для управления листом. В этой статье рассматривается использование класса [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) для автоматической подгонки строк или столбцов.

### **Автоматическая подгонка строки - простой**

Наиболее простой способ автоматического изменения ширины и высоты строки - вызвать метод класса. Метод принимает индекс строки (строки, которую нужно изменить в размере) в качестве параметра.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowsandColumns-1.py" >}}

### **Как автоматически подогнать строку в диапазоне ячеек**

Строка состоит из многих столбцов. Aspose.Cells для Python via .NET позволяет разработчикам автоматически подогнать строку в зависимости от содержимого в диапазоне ячеек внутри строки, вызвав перегруженную версию метода [**auto_fit_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_row/#int-int-int). Он принимает следующие параметры:

- Индекс строки, индекс строки, которую нужно автоматически подогнать.
- Индекс первого столбца, индекс первого столбца строки.
- Индекс последнего столбца, индекс последнего столбца строки.

Метод проверяет содержимое всех столбцов в строке, а затем автоматически подгоняет строку.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowinSpecificRange-1.py" >}}

### **Как автоматически подогнать столбец в диапазоне ячеек**

Столбец состоит из многих строк. Возможно автоматически подогнать столбец на основе содержимого диапазона ячеек в столбце, вызвав перегруженную версию метода, который принимает следующие параметры:

- Индекс столбца, индекс столбца, который нужно автоматически подогнать.
- Индекс первой строки, индекс первой строки столбца.
- Индекс последней строки, индекс последней строки столбца.

Метод проверяет содержимое всех строк в столбце, а затем автоматически подгоняет столбец.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitColumninSpecificRange-1.py" >}}

### **Как автоматически подогнать строки для объединенных ячеек**

С Aspose.Cells для Python via .NET можно автоматически подогнать строки даже для ячеек, которые были объединены с использованием API [**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions). Класс [**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) предоставляет свойство [**auto_fit_merged_cells_type**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/auto_fit_merged_cells_type/), которое можно использовать для автоматической подгонки строк для объединенных ячеек. [**auto_fit_merged_cells_type**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/auto_fit_merged_cells_type/) принимает перечисление [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitmergedcellstype), которое имеет следующие элементы:

- NONE: Игнорировать объединенные ячейки.
- FIRST_LINE: Только расширяет высоту первой строки.
- LAST_LINE: Только расширяет высоту последней строки.
- EACH_LINE: Только расширяет высоту каждой строки.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowsforMergedCells-1.py" >}}

{{% alert color="primary" %}}

Вы также можете попробовать использовать перегруженные версии методов [**auto_fit_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_rows/#int-int-aspose.cells.AutoFitterOptions) и [**auto_fit_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_columns/#int-int-aspose.cells.AutoFitterOptions), принимающие диапазон строк/столбцов и экземпляр [**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) для автоматической подгонки выбранных строк/столбцов в соответствии с вашими желаемыми [**AutoFitterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions).

Сигнатуры вышеперечисленных методов выглядят следующим образом:

1. auto_fit_rows(start_row, end_row, [**options**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions) параметры)
1. auto_fit_columns(first_column, last_column, [**options**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions))

{{% /alert %}}

## **Важно знать**

{{% alert color="primary" %}}

Если ячейка объединена, то методы AutoFit не будут применены, что соответствует тому же поведению, что и в Microsoft Excel. Вы можете обойти это, используя API автофильтра. Более того, если текст в ячейке перенесен, метод [**auto_fit_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/auto_fit_column/#int-int-int) также не будет применен. Еще одна вещь, которую нужно знать, заключается в том, что методы AutoFit занимают много времени. Поэтому вы должны вызывать эти методы как можно реже, чтобы обеспечить эффективность вашего приложения.

{{% /alert %}}

## **Продвинутые темы**
- [AutoFit строк для объединенных ячеек](/cells/ru/python-net/autofit-rows-for-merged-cells/)
{{< app/cells/assistant language="python-net" >}}
