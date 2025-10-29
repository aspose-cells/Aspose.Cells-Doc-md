---
title: Создание доступа и копирование именованных диапазонов
type: docs
weight: 200
url: /ru/python-net/create-access-and-copy-named-ranges/
description: В этой статье показано, как создать доступ и скопировать именованные диапазоны с помощью Aspose.Cells для Python via .NET API.
keywords: Библиотека Python Excel, Создание доступа и копирование именованных диапазонов Python, Создание именованных диапазонов Python, Копирование именованных диапазонов Python, Доступ ко всем именованным диапазонам в электронной таблице Python.
---

## **Введение**

Обычно для обозначения отдельных ячеек используются метки столбцов и строк. Возможно создание описательных имен для представления ячеек, диапазонов ячеек, формул или постоянных значений. Слово **имя** может обозначать строку символов, представляющую ячейку, диапазон ячеек, формулу или постоянное значение. Присвоение имени диапазону означает, что к этому диапазону ячеек можно обращаться по его имени. Используйте понятные имена, такие как Продукты, для обращения к труднопонимаемым диапазонам, например Продажи!C20:C30. Метки могут использоваться в формулах, обращающихся к данным на той же листе; если вы хотите обозначить диапазон на другом листе, можно использовать имя. *Именованные диапазоны являются одной из самых мощных функций Microsoft Excel, особенно при использовании в качестве исходного диапазона для элементов управления списками, сводных таблиц, диаграмм и т. д.

## **Работа с именованным диапазоном с помощью Microsoft Excel**

### **Создание именованных диапазонов**

В следующих шагах описано, как назвать ячейку или диапазон ячеек в **MS Excel**. Этот метод применим к **Microsoft Office Excel 2003**, **Microsoft Excel 97**, **2000** и **2002**.

1. Выберите ячейку или диапазон ячеек, которые вы хотите именовать.
1. Нажмите **Поле с именем** в левом конце строки формул.
1. Введите имя для ячеек.
1. Нажмите ENTER.

{{% alert color="primary" %}}

Вы не можете называть ячейку, когда вы изменяете содержимое ячейки.

{{% /alert %}}

## **Работа с именованным диапазоном с использованием Aspose.Cells для библиотеки Excel Python**

Здесь мы используем API Aspose.Cells для Python via .NET, чтобы выполнить задачу.
Aspose.Cells для Python via .NET предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) предоставляет коллекцию [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells).

### **Создание именованного диапазона**

Можно создать именованный диапазон, вызвав перегруженный метод [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str-str) коллекции [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Типичная версия метода [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str-str) принимает следующие параметры:

- Имя верхней левой ячейки, имя верхней левой ячейки в диапазоне.
- Имя нижней правой ячейки, имя нижней правой ячейки в диапазоне.

Когда вызывается метод [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str-str), он возвращает только что созданный диапазон в виде экземпляра класса [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range). Используйте этот объект [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range), чтобы настроить именованный диапазон. Например, установите имя диапазона, используя свойство [**name**](https://reference.aspose.com/cells/python-net/aspose.cells/range/name). В следующем примере показано, как создать именованный диапазон ячеек, который простирается от B4:G14.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-CreateNamedRangeofCells-1.py" >}}

### **Ввод данных в ячейки именованного диапазона**

Можно вставить данные в отдельные ячейки диапазона, следуя образцу

- **C#**: Range[row,column]
- **VB**: Range(row,column)

Предположим, у вас есть именованный диапазон ячеек, который охватывает A1:C4. Матрица состоит из 4 * 3 = 12 ячеек. Отдельные ячейки диапазона упорядочены последовательно: Диапазон[0,0], Диапазон[0,1], Диапазон[0,2], Диапазон[1,0], Диапазон[1,1], Диапазон[1,2], Диапазон[2,0], Диапазон[2,1], Диапазон[2,2], Диапазон[3,0], Диапазон[3,1], Диапазон[3,2].

Используйте следующие свойства для определения ячеек в диапазоне:

- FirstRow возвращает индекс первой строки в именованном диапазоне.
- FirstColumn возвращает индекс первого столбца в именованном диапазоне.
- RowCount возвращает общее количество строк в именованном диапазоне.
- ColumnCount возвращает общее количество столбцов в именованном диапазоне.

В следующем примере показано, как ввести некоторые значения в ячейки указанного диапазона.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-InputDataInCellsInRange-1.py" >}}

### **Определение ячеек в именованном диапазоне**

Вы можете вставить данные в отдельные ячейки диапазона, следуя шаблону:

- **C#**: Range[row,column]
- **VB**: Range(row,column)

Если у вас есть именованный диапазон, который охватывает A1:C4. Матрица делает 4 * 3 = 12 ячеек. Отдельные ячейки диапазона упорядочены последовательно: Диапазон[0,0], Диапазон[0,1], Диапазон[0,2], Диапазон[1,0], Диапазон[1,1], Диапазон[1,2], Диапазон[2,0], Диапазон[2,1], Диапазон[2,2], Диапазон[3,0], Диапазон[3,1], Диапазон[3,2].

Используйте следующие свойства для определения ячеек в диапазоне:

- FirstRow возвращает индекс первой строки в именованном диапазоне.
- FirstColumn возвращает индекс первого столбца в именованном диапазоне.
- RowCount возвращает общее количество строк в именованном диапазоне.
- ColumnCount возвращает общее количество столбцов в именованном диапазоне.

В следующем примере показано, как ввести некоторые значения в ячейки указанного диапазона.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-IdentifyCellsinNamedRange-1.py" >}}

### **Доступ к именованным диапазонам**

#### **Доступ к конкретному именованному диапазону**

Вызовите метод [**get_range_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/get_range_by_name/#str) коллекции [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/), чтобы получить диапазон по указанному имени. Типичный метод [**get_range_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/get_range_by_name/#str) принимает имя именованного диапазона и возвращает указанный именованный диапазон как экземпляр класса [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range). В следующем примере показано, как получить доступ к указанному диапазону по его имени.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-AccessSpecificNamedRange-1.py" >}}

#### **Доступ ко всем именованным диапазонам в электронной таблице**

Вызовите метод [**get_named_ranges**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/get_named_ranges/#) коллекции [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/), чтобы получить все именованные диапазоны в электронной таблице. Метод [**get_named_ranges**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/get_named_ranges/#) возвращает массив всех именованных диапазонов в коллекции [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/).

В следующем примере показано, как получить доступ ко всем именованным диапазонам в книге.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-AccessAllNamedRanges-1.py" >}}

### **Копировать именованные диапазоны**

Aspose.Cells для Python via .NET предоставляет [**Range.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy/#aspose.cells.Range) метод для копирования диапазона ячеек с форматированием в другой диапазон.

В следующем примере показано, как скопировать исходный диапазон ячеек в другой именованный диапазон.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-CopyNamedRanges-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
