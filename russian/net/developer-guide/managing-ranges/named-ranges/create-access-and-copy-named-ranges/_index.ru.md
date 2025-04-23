---
title: Создание доступа и копирование именованных диапазонов
type: docs
weight: 200
url: /ru/net/create-access-and-copy-named-ranges/
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

## **Работа с именованным диапазоном с использованием Aspose.Cells**

Здесь мы используем API Aspose.Cells для выполнения этой задачи.
Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells).

### **Создание именованного диапазона**

Можно создать именованный диапазон, вызвав перегруженный метод [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) коллекции [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Типичная версия метода [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/3) принимает следующие параметры:

- Имя верхней левой ячейки, имя верхней левой ячейки в диапазоне.
- Имя нижней правой ячейки, имя нижней правой ячейки в диапазоне.

Когда вызывается метод [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/3), он возвращает только что созданный диапазон в виде экземпляра класса [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range). Используйте этот объект [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range), чтобы настроить именованный диапазон. Например, установите имя диапазона, используя свойство [**Name**](https://reference.aspose.com/cells/net/aspose.cells/range/properties/name). В следующем примере показано, как создать именованный диапазон ячеек, который простирается от B4:G14.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CreateNamedRangeofCells-1.cs" >}}

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-InputDataInCellsInRange-1.cs" >}}

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IdentifyCellsinNamedRange-1.cs" >}}

### **Доступ к именованным диапазонам**

#### **Доступ к конкретному именованному диапазону**

Вызовите метод [**GetRangeByName**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getrangebyname) коллекции [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection), чтобы получить диапазон по указанному имени. Типичный метод [**GetRangeByName**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getrangebyname) принимает имя именованного диапазона и возвращает указанный именованный диапазон как экземпляр класса [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range). В следующем примере показано, как получить доступ к указанному диапазону по его имени.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-AccessSpecificNamedRange-1.cs" >}}

#### **Доступ ко всем именованным диапазонам в электронной таблице**

Вызовите метод [**GetNamedRanges**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getnamedranges) коллекции [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection), чтобы получить все именованные диапазоны в электронной таблице. Метод [**GetNamedRanges**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/getnamedranges) возвращает массив всех именованных диапазонов в коллекции [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection).

В следующем примере показано, как получить доступ ко всем именованным диапазонам в книге.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-AccessAllNamedRanges-1.cs" >}}

### **Копировать именованные диапазоны**

Aspose.Cells предоставляет метод [**Range.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/copy/index) для копирования диапазона ячеек с форматированием в другой диапазон.

В следующем примере показано, как скопировать исходный диапазон ячеек в другой именованный диапазон.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CopyNamedRanges-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
