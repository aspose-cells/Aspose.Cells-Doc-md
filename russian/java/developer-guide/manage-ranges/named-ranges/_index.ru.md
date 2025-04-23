---
title: Именованные диапазоны
type: docs
weight: 40
url: /ru/java/named-ranges/
---

{{% alert color="primary" %}} 

Обычно для ссылки на отдельные ячейки используются метки столбцов и строк. Возможно создать понятные названия, чтобы представить ячейки, диапазоны ячеек, формулы или константные значения. Слово **имя** может относиться к строке символов, которая представляет ячейку, диапазон ячеек, формулу или константное значение. Присвоение имени диапазону означает, что на этот диапазон ячеек можно ссылаться по его имени. Используйте понятные имена, такие как Продукты, для ссылки на труднопонимаемые диапазоны, такие как Продажи!C20:C30. Метки можно использовать в формулах, относящихся к данным на том же рабочем листе; если вы хотите представить диапазон на другом рабочем листе, вы можете использовать имя. *Именованные диапазоны являются одной из самых мощных функций Microsoft Excel, особенно при использовании в качестве исходного диапазона для элементов управления списками, сводными таблицами, диаграммами и т. д.

{{% /alert %}} 
## **Создание именованного диапазона**
### **Использование Microsoft Excel**
Следующие шаги описывают, как создать имя ячейки или диапазона ячеек с использованием Microsoft Excel. Данный метод применим к Microsoft Office Excel 2003, Microsoft Excel 97, 2000 и 2002.

1. Выберите ячейку или диапазон ячеек, которые вы хотите именовать.
1. Нажмите на поле с именем слева от строки формул.
1. Введите имя для ячеек.
1. Нажмите ENTER.

{{% alert color="primary" %}} 

Вы не можете называть ячейку, когда вы изменяете содержимое ячейки.

{{% /alert %}} 
### **Использование Aspose.Cells**
Здесь мы используем API Aspose.Cells для выполнения этой задачи.

Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) содержит [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection), позволяющий получить доступ к каждому листу Excel-файла. Лист представлен классом [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). Класс [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) предоставляет коллекцию [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells).

Можно создать именованный диапазон, вызвав перегруженный метод [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-java.lang.String-java.lang.String-) коллекции [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Стандартная версия метода [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-java.lang.String-java.lang.String-) принимает следующие параметры:

- Имя верхней левой ячейки, имя верхней левой ячейки в диапазоне.
- Имя нижней правой ячейки, имя нижней правой ячейки в диапазоне.

При вызове метода [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-java.lang.String-java.lang.String-) он возвращает созданный именованный диапазон как экземпляр класса [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range).

В следующем примере показано, как создать именованный диапазон ячеек, который расширяется от B4 до G14.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreateNamedRangeofCells-CreateNamedRangeofCells.java" >}}
#### **Доступ ко всем именованным диапазонам в электронной таблице**
Вызовите метод [getNamedRanges](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges--) коллекции [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection), чтобы получить все именованные диапазоны. Метод [getNamedRanges](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges--) возвращает массив всех именованных диапазонов коллекции [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection).

В следующем примере показано, как получить доступ ко всем именованным диапазонам в книге.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessAllNamedRanges-AccessAllNamedRanges.java" >}}
#### **Доступ к конкретному именованному диапазону**
Вызовите метод [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) [getRangeByName](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName-java.lang.String-) для получения диапазона по имени. Обычный метод [getRangeByName](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName-java.lang.String-) принимает имя именованного диапазона и возвращает указанный диапазон как экземпляр класса [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range).

В следующем примере показано, как получить доступ к указанному диапазону по его имени.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessSpecificNamedRange-AccessSpecificNamedRange.java" >}}
#### **Определение ячеек в именованном диапазоне**
С помощью Aspose.Cells вы можете вставлять данные в отдельные ячейки диапазона. Предположим, у вас есть именованный диапазон ячеек, т.е. A1:C4. Таким образом, матрица будет состоять из 4 * 3 = 12 ячеек, и отдельные ячейки диапазона упорядочены последовательно. Aspose.Cells предоставляет вам несколько полезных свойств класса [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) для доступа к отдельным ячейкам в диапазоне. Вы можете использовать следующие методы для определения ячеек в диапазоне:

- [getFirstRow](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow) возвращает индекс первой строки в именованном диапазоне.
- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn) возвращает индекс первого столбца в именованном диапазоне.

В следующем примере показано, как ввести некоторые значения в ячейки указанного диапазона.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-IdentifyCellsinNamedRange-IdentifyCellsinNamedRange.java" >}}
#### **Ввод данных в ячейки именованного диапазона**
С использованием Aspose.Cells, вы можете вставлять данные в отдельные ячейки диапазона. Предположим, у вас есть именованный диапазон ячеек, например, H1:J4. Таким образом, матрица создает 4 * 3 = 12 ячеек, и индивидуальные ячейки диапазона располагаются последовательно. Aspose.Cells предоставляет некоторые полезные свойства класса [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) для доступа к отдельным ячейкам в диапазоне. Вы можете использовать следующие свойства для идентификации ячеек в диапазоне:

- [getFirstRow](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow) возвращает индекс первой строки в именованном диапазоне.
- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn) возвращает индекс первого столбца в именованном диапазоне.

В следующем примере показано, как ввести некоторые значения в ячейки указанного диапазона.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-InputDataInCellsInRange-InputDataInCellsInRange.java" >}}
#### **Настройка диапазонов... Установка цвета фона и атрибутов шрифта в именованный диапазон**
Для применения форматирования определите объект [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style), чтобы указать настройки стиля, и примените его к объекту [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range).

В следующем примере показано, как установить сплошной цвет заливки (цвет заливки) с настройками шрифта для диапазона.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges1-FormatRanges1.java" >}}
#### **Настройка диапазонов... Добавление границ в именованный диапазон**
Можно добавить границы диапазону ячеек, а не только одной ячейке. Объект [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) предоставляет метод [setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders-int-com.aspose.cells.Color-) с параметрами, необходимыми для добавления границы к диапазону ячеек:

- borderStyle: тип границы, выбранный из перечисления [CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType).
- borderColor: цвет линии границы, выбранный из перечисления [Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color).

В следующем примере показано, как установить контурную границу для диапазона.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges2-FormatRanges2.java" >}}


После выполнения вышеуказанного кода будет сгенерирован следующий вывод: 

![todo:image_alt_text](named-ranges_1.png)
#### **Применить стиль к ячейкам в диапазоне**
Иногда необходимо применить стиль к ячейкам в [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range). Для этого можно пройтись по ячейкам диапазона и использовать метод [Cell.setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle-com.aspose.cells.Style-) для применения стиля к ячейке.

В следующем примере показано, как применить стили к ячейкам в диапазоне.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ConvertCellsAddresstoRangeorCellArea-ConvertCellsAddresstoRangeorCellArea.java" >}}
#### **Удалить именованный диапазон**
Aspose.Cells предоставляет метод [NameCollection.RemoveAt()](https://reference.aspose.com/cells/java/com.aspose.cells/namecollection#removeAt-int-) для удаления имени диапазона. Чтобы очистить содержимое диапазона, используйте метод [Cells.ClearRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#clearRange-com.aspose.cells.CellArea-)
В следующем примере показано, как удалить именованный диапазон со всем его содержимым.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RemoveANamedRange-RemoveANamedRange.java" >}}


borderColors 
{{< app/cells/assistant language="java" >}}
