---
title: Применить условное форматирование на листе
type: docs
weight: 40
url: /ru/cpp/apply-conditional-formatting-in-worksheet/
---
## **Возможный сценарий использования**
 Aspose.Cells позволяет добавлять все виды условного форматирования, например формулу, выше среднего, цветовую шкалу, панель данных, набор значков, Top10 и т. д. Он предоставляет[IFormatCondition](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition)класс, который имеет все необходимые методы для применения условного форматирования по вашему выбору. Вот список нескольких методов Get.

- [ПолучитьIAboveAverage()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#aff550fd834cd78967ec440492ff012d5)
- [ПолучитьIColorScale()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a3348a7c447dc564ceabc22c9c89bd6f5)
- [ПолучитьIDataBar()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a4415a87833c41386ed1595e742485e07)
- [ПолучитьIIconSet()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a011b2c7dbaaf671819d09f5d1df865e3)
- [ПолучитьITop10()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a64388aaf1b43811f5ee1ee3090c9bd4a)
## **Применить условное форматирование на листе**
 В следующем примере кода показано, как добавить условное форматирование Cell Value в ячейки A1 и B2. Пожалуйста, смотрите[выходной файл excel](23167004.xlsx) сгенерированный кодом, и следующий снимок экрана, объясняющий влияние кода на[выходной файл excel](23167004.xlsx). Если вы поместите значение больше 100 в ячейки A2 и B2, красный цвет заливки ячеек A1 и B2 исчезнет.

![дело:изображение_альтернативный_текст](apply-conditional-formatting-in-worksheet_1.png)
## **Образец кода**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ApplyConditionalFormattingInWorksheet.cpp" >}}
