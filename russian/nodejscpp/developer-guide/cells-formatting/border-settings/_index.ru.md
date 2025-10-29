---  
title: Настройки границ
linktitle: Настройки границ  
description: Как использовать библиотеку Aspose.Cells в Node.js через C++ для установки стиля и цвета границы ячеек. Регулируя ширину, стиль и цвет границы, вы получите больше контроля над внешним видом ячеек.  
keywords: Aspose.Cells, Настройки границ ячейки, Node.js через C++, ширина границы, стиль границы, цвет границы  
type: docs  
weight: 40  
url: /ru/nodejs-cpp/cells-border-settings/  
---  

## **Добавление границ в ячейки**  

Microsoft Excel позволяет пользователям форматировать ячейки, добавляя границы. Тип границы зависит от её расположения. Например, верхняя граница добавляется к верхней стороне ячейки. Также можно изменить стиль линии и цвет границы.  

С Aspose.Cells for Node.js via C++ разработчики могут добавлять границы и настраивать их внешний вид так же гибко, как в Microsoft Excel.  

### **Добавление границ в ячейки**  

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--), позволяющую получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) обеспечивает коллекцию [**cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Каждый элемент коллекции [**cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) представляет объект класса [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).  

Aspose.Cells предоставляет метод [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) в классе [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell). Метод [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) используется для установки стиля форматирования ячейки. Класс [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) предоставляет свойства для добавления границ к ячейкам.  

#### **Добавление границ к ячейке**  

Разработчики могут добавлять границы к ячейке, используя коллекцию [**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--) объекта [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style). Тип границы передается как индекс в коллекцию [**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--). Все типы границ предопределены в перечислении [**BorderType**](https://reference.aspose.com/cells/nodejs-cpp/bordertype).  

Перечисление границ  

|**Типы границ**|**Описание**|  
| :- | :- |  
|BottomBorder|Линия нижней границы|  
|DiagonalDown|Диагональная линия от верхнего левого до нижнего правого|  
|DiagonalUp|Диагональная линия от нижнего левого до верхнего правого|  
|LeftBorder|Линия левой границы|  
|RightBorder|Линия правой границы|  
|TopBorder|Линия верхней границы|  

Коллекция [**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--) хранит все границы. Каждая граница в коллекции [**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--) представлена объектом [**Border**](https://reference.aspose.com/cells/nodejs-cpp/border), который обеспечивает два свойства: [**setColor**](https://reference.aspose.com/cells/nodejs-cpp/border/#setColor-color-) и [**setLineStyle**](https://reference.aspose.com/cells/nodejs-cpp/border/#setLineStyle-cellbordertype-) для установки цвета линии границы и стиля соответственно.  

Чтобы установить цвет линии границы, выберите цвет с помощью перечисления Color (часть Node.js) и присвойте его свойству color объекта Border.  

Стиль линии границы устанавливается выбором стиля линии из перечисления [**CellBorderType**](https://reference.aspose.com/cells/nodejs-cpp/cellbordertype).  

**Перечисление типов границ ячейки**  

|**Стили линий**|**Описание**|  
| :- | :- |  
|DashDot|Тонкая пунктирная линия|  
|DashDotDot|Тонкая штрих-пунктирная линия|  
|Dashed|Пунктирная линия|  
|Dotted|Точечная линия|  
|Double|Двойная линия|  
|Hair|Линия минимальной толщины|  
|MediumDashDot|Средняя штрих-пунктирная линия|  
|MediumDashDotDot|Средняя штрих-точечно-пунктирная линия|  
|MediumDashed|Средняя пунктирная линия|  
|None|Нет линии|  
|Medium|Средняя линия|  
|SlantedDashDot|Наклоненная средняя штрих-пунктирная линия|  
|Thick|Толстая линия|  
|Thin|Тонкая линия|  
Выберите один из стилей линий и затем присвойте его свойству [**lineStyle**](https://reference.aspose.com/cells/nodejs-cpp/border/#setLineStyle-cellbordertype-) объекта [**Border**](https://reference.aspose.com/cells/nodejs-cpp/border).  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AddBordersToCell.js" >}}

{{% alert color="primary" %}}  
Следует одновременно устанавливать как стиль линии, так и цвет. Две диагональные линии границы должны иметь одинаковый стиль линии и цвет.  
{{% /alert %}}  

#### **Добавление границ для диапазона ячеек**  

Также возможно добавлять границы к диапазону ячеек, а не только к одной ячейке. Для этого сначала создайте диапазон ячеек, вызвав метод [**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) коллекции [**cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Он принимает следующие параметры:  

- Первая строка, первая строка диапазона.  
- Первый столбец, представляет первый столбец диапазона.  
- Количество строк, количество строк в диапазоне.  
- Количество столбцов, количество столбцов в диапазоне.  

Метод [**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) возвращает объект [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range), который содержит указанный диапазон ячеек. Объект [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) предоставляет метод [**setOutlineBorder**](https://reference.aspose.com/cells/nodejs-cpp/range/#setOutlineBorder-bordertype-cellbordertype-cellscolor-), который принимает следующие параметры для добавления границы к диапазону ячеек:  

- **Тип границы**, тип границы, выбранный из перечисления [**BorderType**](https://reference.aspose.com/cells/nodejs-cpp/bordertype).  
- **Стиль линии**, стиль линии границы, выбранный из перечисления [**CellBorderType**](https://reference.aspose.com/cells/nodejs-cpp/cellbordertype).  
- **Цвет**, цвет линии, выбранный из перечисления Color.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AddBordersToRange.js" >}}


{{< app/cells/assistant language="nodejs-cpp" >}}
