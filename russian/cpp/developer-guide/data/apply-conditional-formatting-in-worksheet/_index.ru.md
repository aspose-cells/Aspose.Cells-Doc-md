---
title: Применить условное форматирование на листе
type: docs
weight: 40
url: /ru/cpp/apply-conditional-formatting-in-worksheet/
---
##  **Возможный сценарий использования**
 Aspose.Cells позволяет добавлять все виды условного форматирования, например, «Формула», «Выше среднего», «Цветовая шкала», «Панель данных», «Набор значков», «Топ10» и т. д. Он обеспечивает[ФорматУсловие](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/)класс, который имеет все необходимые методы для применения условного форматирования по вашему выбору. Вот список нескольких методов Get.

- [GetAboveAverage()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getaboveaverage/)
- [GetColorScale()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getcolorscale)
- [GetDataBar()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getdatabar)
- [GetIconSet()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/geticonset)
- [GetTop10()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/gettop10)
##  **Применить условное форматирование на листе**
 В следующем примере кода показано, как добавить условное форматирование значения Cell к ячейкам A1 и B2. Пожалуйста, ознакомьтесь с[выходной файл Excel](23167004.xlsx) сгенерированный кодом, и следующий снимок экрана, который объясняет влияние кода на[выходной файл Excel](23167004.xlsx)Если вы поместите значение больше 100 в ячейки A2 и B2, красный цвет заливки из ячеек A1 и B2 исчезнет.

![задача: image_alt_text](apply-conditional-formatting-in-worksheet_1.png)
##  **Образец кода**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ApplyConditionalFormattingInWorksheet-new.cpp" >}}
