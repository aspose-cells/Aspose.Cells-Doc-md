---
title: Настройки границы с Golang через C++
linktitle: Настройки границ
description: Как использовать библиотеку Aspose.Cells на C++ для установки стиля и цвета границы ячеек. Регулируя ширину, стиль и цвет границы, вы получаете больше контроля над внешним видом ячеек.
keywords: Aspose.Cells, Настройки границы ячейки, C++, Ширина границы, Стиль границы, Цвет границы
type: docs
weight: 40
url: /ru/go-cpp/cells-border-settings/
---

## **Добавление границ в ячейки**

Microsoft Excel позволяет пользователям форматировать ячейки, добавляя границы. Тип границы зависит от её расположения. Например, верхняя граница добавляется к верхней стороне ячейки. Также можно изменить стиль линии и цвет границы.

С помощью Aspose.Cells разработчики могут добавлять границы и настраивать их внешний вид таким же гибким способом, как в Microsoft Excel.

### **Добавление границ в ячейки**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), позволяющую получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Класс [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) обеспечивает коллекцию [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Каждый элемент коллекции [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) представляет объект класса [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Aspose.Cells предоставляет метод [**GetStyle**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/) в классе [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/). Метод [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) используется для установки стиля форматирования ячейки. Класс [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) предоставляет свойства для добавления границ к ячейкам.

#### **Добавление границ к ячейке**

Разработчики могут добавлять границы к ячейке, используя коллекцию [**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/) объекта [**Style**](https://reference.aspose.com/cells/go-cpp/style/). Тип границы передается как индекс в коллекцию [**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/). Все типы границ предопределены в перечислении [**BorderType**](https://reference.aspose.com/cells/cpp/aspose.cells/bordertype/).

Перечисление границ

| **Типы границ** | **Описание** |
|------------------|-----------------|
| BottomBorder     | Линия нижней границы |
| DiagonalDown     | Диагональная линия снизу слева вверх направо |
| DiagonalUp       | Диагональная линия сверху слева вниз направо |
| LeftBorder       | Левая грань |
| RightBorder      | Правая грань |
| TopBorder        | Верхняя грань |

Коллекция [**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/) хранит все границы. Каждая граница в коллекции [**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/) представлена объектом [**Border**](https://reference.aspose.com/cells/cpp/aspose.cells/border/), который обеспечивает два свойства: [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/border/getcolor/) и [**GetLineStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/border/getlinestyle/) для установки цвета линии границы и стиля соответственно.

Чтобы установить цвет линии границы, выберите цвет с помощью перечисления Color и присвойте его свойству Color объекта Border.

Стиль линии границы устанавливается выбором стиля линии из перечисления [**CellBorderType**](https://reference.aspose.com/cells/go-cpp/cellbordertype/).

**Перечисление типов границ ячейки**

| **Типы линий**       | **Описание**               |
|------------------------|-------------------------------|
| DashDot               | Тонкая пунктирно-штриховая линия |
| DashDotDot            | Тонкая штрихпунктирная линия |
| Dashed                | Пунктирная линия |
| Dotted                | Точечная линия |
| Double                | Двойная линия |
| Hair                  | Тонкая линия |
| MediumDashDot         | Средняя штрихпунктирная линия |
| MediumDashDotDot      | Средняя штрихпунктирная точка |
| MediumDashed          | Средняя пунктирная линия |
| None                  | Нет линии |
| Medium                | Средняя линия |
| SlantedDashDot        | Наклонная средняя штрихпунктирная линия |
| Thick                 | Толстая линия |
| Thin                  | Тонкая линия |

Выберите один из стилей линий и затем присвойте его свойству [**GetLineStyle()**](https://reference.aspose.com/cells/go-cpp/border/getlinestyle/) объекта [**Border**](https://reference.aspose.com/cells/go-cpp/border/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-BorderSettings.go" >}}
{{% alert color="primary" %}}

Следует одновременно устанавливать как стиль линии, так и цвет. Две диагональные линии границы должны иметь одинаковый стиль линии и цвет.

{{% /alert %}}

#### **Добавление границ для диапазона ячеек**

Также возможно добавлять границы к диапазону ячеек, а не только к одной ячейке. Для этого сначала создайте диапазон ячеек, вызвав метод [**CreateRange**](https://reference.aspose.com/cells/go-cpp/cells/createrange/) коллекции [**Cells**](https://reference.aspose.com/cells/go-cpp/cells/). Он принимает следующие параметры:

- Первая строка, первая строка диапазона.
- Первый столбец, представляет первый столбец диапазона.
- Количество строк, количество строк в диапазоне.
- Количество столбцов, количество столбцов в диапазоне.

Метод [**CreateRange**](https://reference.aspose.com/cells/go-cpp/cells/createrange_string_string/) возвращает объект [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/), который содержит указанный диапазон ячеек. Объект [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) предоставляет метод [**SetOutlineBorder**](https://reference.aspose.com/cells/cpp/aspose.cells/range/setoutlineborder/), который принимает следующие параметры для добавления границы к диапазону ячеек:

- **Тип границы**, тип границы, выбранный из перечисления [**BorderType**](https://reference.aspose.com/cells/go-cpp/bordertype/).
- **Стиль линии**, стиль линии границы, выбранный из перечисления [**CellBorderType**](https://reference.aspose.com/cells/go-cpp/cellbordertype/).
- **Цвет**, цвет линии, выбранный из перечисления Color.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-BorderSettings-1.go" >}}
