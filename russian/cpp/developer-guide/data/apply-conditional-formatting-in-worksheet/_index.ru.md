---
title: Применение Условного Форматирования в Листе
type: docs
weight: 40
url: /ru/cpp/apply-conditional-formatting-in-worksheet/
---

## **Возможные сценарии использования**
Aspose.Cells позволяет добавлять все виды условного форматирования, например Формула, Выше среднего, Цветовая шкала, Полоса данных, Набор значков, Топ-10 и т. д. Он предоставляет класс [FormatCondition](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/), который имеет все необходимые методы для применения выбранного условного форматирования. Вот список нескольких методов Get.

- [GetAboveAverage()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getaboveaverage/)
- [GetColorScale()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getcolorscale)
- [GetDataBar()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getdatabar)
- [GetIconSet()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/geticonset)
- [GetTop10()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/gettop10)
## **Применить условное форматирование в листе**
В следующем образце кода показано, как добавить условное форматирование значения ячейки на ячейках A1 и B2. Пожалуйста, посмотрите [файл Excel-вывода](23167004.xlsx), созданный кодом, а также следующий скриншот, который объясняет эффект кода на [файл Excel-вывода](23167004.xlsx). Если вы введете значение больше 100 в ячейку A2 и B2, красный цвет заливки из ячеек A1 и B2 исчезнет.

![todo:image_alt_text](apply-conditional-formatting-in-worksheet_1.png)
## **Образец кода**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ApplyConditionalFormattingInWorksheet-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
