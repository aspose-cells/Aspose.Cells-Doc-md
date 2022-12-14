---
title: Именованные диапазоны
type: docs
weight: 40
url: /ru/java/named-ranges/
---
{{% alert color="primary" %}} 

Обычно метки столбцов и строк используются для обозначения отдельных ячеек. Можно создавать описательные имена для представления ячеек, диапазонов ячеек, формул или постоянных значений. Слово**имя** может относиться к строке символов, представляющей ячейку, диапазон ячеек, формулу или постоянное значение. Присвоение имени диапазону означает, что на этот диапазон ячеек можно ссылаться по его имени. Используйте простые для понимания названия, например «Продукты», для обозначения труднопонятных диапазонов, например «Продажи!C20:C30». Метки можно использовать в формулах, которые ссылаются на данные на одном листе; если вы хотите представить диапазон на другом листе, вы можете использовать имя. * Именованные диапазоны являются одними из самых мощных функций Microsoft Excel, особенно когда они используются в качестве исходного диапазона для элементов управления списками, сводных таблиц, диаграмм и т. д.

{{% /alert %}} 
## **Создание именованного диапазона**
### **Использование Microsoft Excel**
Следующие шаги описывают, как назвать ячейку или диапазон ячеек с помощью Microsoft Excel. Этот метод применим к Microsoft Office Excel 2003, Microsoft Excel 97, 2000 и 2002.

1. Выберите ячейку, диапазон ячеек, которые вы хотите назвать.
1. Щелкните поле имени в левом конце строки формул.
1. Введите имя для ячеек.
1. Нажмите Ввод.

{{% alert color="primary" %}} 

Вы не можете назвать ячейку, пока вы меняете содержимое ячейки.

{{% /alert %}} 
### **Использование Aspose.Cells**
Здесь мы используем Aspose.Cells API для выполнения задачи.

 Aspose.Cells предоставляет класс,[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , представляющий файл Excel Microsoft.[Рабочая тетрадь](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) класс содержит[Рабочий листКоллекция](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) который позволяет получить доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) учебный класс.[Рабочий лист](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) класс предоставляет[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)коллекция.

 Можно создать именованный диапазон, вызвав перегруженный[createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\) ) метод[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) коллекция. Типичная версия этого[createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\)) принимает следующие параметры:

- Имя верхней левой ячейки, имя верхней левой ячейки в диапазоне.
- Имя нижней правой ячейки, имя нижней правой ячейки в диапазоне.

 Когда[createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\) ), он возвращает только что созданный именованный диапазон как экземпляр[Диапазон](https://reference.aspose.com/cells/java/com.aspose.cells/range) учебный класс.

В следующем примере показано, как создать именованный диапазон ячеек, охватывающий B4:G14.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreateNamedRangeofCells-CreateNamedRangeofCells.java" >}}
#### **Доступ ко всем именованным диапазонам в электронной таблице**
 Позвоните[getNamedRange](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges\(\) ) метод[Рабочий листКоллекция](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) чтобы получить все именованные диапазоны в электронной таблице.[getNamedRange](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges\(\) ) возвращает массив всех именованных диапазонов в[Рабочий листКоллекция](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection).

В следующем примере показано, как получить доступ ко всем именованным диапазонам в книге.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessAllNamedRanges-AccessAllNamedRanges.java" >}}
#### **Доступ к определенному именованному диапазону**
 Позвоните[Рабочий листКоллекция](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) коллекция[getRangeByName](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName\(java.lang.String\) ) для получения указанного диапазона по имени. Типичный[getRangeByName](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName\(java.lang.String\) ) принимает имя именованного диапазона и возвращает указанный именованный диапазон как экземпляр[Диапазон](https://reference.aspose.com/cells/java/com.aspose.cells/range)учебный класс.

В следующем примере показано, как получить доступ к указанному диапазону по его имени.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessSpecificNamedRange-AccessSpecificNamedRange.java" >}}
#### **Определить Cells в именованном диапазоне**
Используя Aspose.Cells, вы можете вставлять данные в отдельные ячейки диапазона. Предположим, у вас есть именованный диапазон ячеек, то есть A1:C4. Таким образом, матрица будет состоять из 4 * 3 = 12 ячеек, а отдельные ячейки диапазона расположены последовательно. Aspose.Cells предоставляет вам некоторые полезные свойства класса [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) для доступа к отдельным ячейкам в диапазоне. Вы можете использовать следующие методы для идентификации ячеек в диапазоне:

- [getFirstRow](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow) возвращает индекс первой строки в именованном диапазоне.
- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn)возвращает индекс первого столбца в именованном диапазоне.

В следующем примере показано, как ввести некоторые значения в ячейки указанного диапазона.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-IdentifyCellsinNamedRange-IdentifyCellsinNamedRange.java" >}}
#### **Введите данные в Cells в именованном диапазоне**
Используя Aspose.Cells, вы можете вставлять данные в отдельные ячейки диапазона. Предположим, у вас есть именованный диапазон ячеек, например, H1:J4. Таким образом, матрица будет состоять из 4 * 3 = 12 ячеек, а отдельные ячейки диапазона расположены последовательно. Aspose.Cells предоставляет вам некоторые полезные свойства класса [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) для доступа к отдельным ячейкам в диапазоне. Вы можете использовать следующие свойства для идентификации ячеек в диапазоне:

- [getFirstRow](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow)возвращает индекс первой строки в именованном диапазоне.
- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn)возвращает индекс первого столбца в именованном диапазоне.

В следующем примере показано, как ввести некоторые значения в ячейки указанного диапазона.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-InputDataInCellsInRange-InputDataInCellsInRange.java" >}}
#### **Диапазоны форматов... Установка цвета фона и атрибутов шрифта для именованного диапазона**
 Чтобы применить форматирование, определите[Стиль](https://reference.aspose.com/cells/java/com.aspose.cells/style) объекта, чтобы указать настройки стиля и применить их к[Диапазон](https://reference.aspose.com/cells/java/com.aspose.cells/range)объект.

В следующем примере показано, как установить сплошной цвет заливки (цвет заливки) с настройками шрифта в диапазоне.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges1-FormatRanges1.java" >}}
#### **Форматирование диапазонов... Добавление границ к именованному диапазону**
 Можно добавить границы к диапазону ячеек, а не только к одной ячейке.[Диапазон](https://reference.aspose.com/cells/java/com.aspose.cells/range) объект обеспечивает[setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders\(int,%20com.aspose.cells.Color\)), который принимает следующие параметры для добавления границы к диапазону ячеек:

-  borderStyle: тип границы, выбранный из[CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)перечисление.
-  borderColor: цвет линии границы, выбранный из[Цвет](https://reference.aspose.com/cells/java/com.aspose.cells/Color) перечисление.

В следующем примере показано, как установить границу контура для диапазона.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges2-FormatRanges2.java" >}}


 После выполнения приведенного выше кода будет сгенерирован следующий вывод:

![дело:изображение_альтернативный_текст](named-ranges_1.png)
#### **Применение стиля к ячейкам в диапазоне**
Иногда вы хотите применить стиль к ячейкам в[Диапазон](https://reference.aspose.com/cells/java/com.aspose.cells/range) . Для этого вы можете перебирать ячейки в диапазоне и использовать[Cell.setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) для применения стиля к ячейке.

В следующем примере показано, как применять стили к ячейкам в диапазоне.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ConvertCellsAddresstoRangeorCellArea-ConvertCellsAddresstoRangeorCellArea.java" >}}
#### **Удалить именованный диапазон**
 Aspose.Cells обеспечивает[Коллекция Имен. Удалить В ()](https://reference.aspose.com/cells/java/com.aspose.cells/namecollection#removeAt\(int\) ) способ стереть имя диапазона. Чтобы очистить содержимое диапазона, используйте[Cells.ClearRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#clearRange\(com.aspose.cells.CellArea\)) метод.
В следующем примере показано, как удалить именованный диапазон вместе с его содержимым.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RemoveANamedRange-RemoveANamedRange.java" >}}


границаЦвета
