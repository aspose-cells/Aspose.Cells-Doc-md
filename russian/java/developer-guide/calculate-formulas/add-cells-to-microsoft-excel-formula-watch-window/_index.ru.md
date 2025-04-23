---
title: Добавление ячеек в окно наблюдения формул Microsoft Excel
type: docs
weight: 20
url: /ru/java/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Возможные сценарии использования**

Окно наблюдения Microsoft Excel — полезный инструмент для удобного отслеживания значений ячеек и их формул. Вы можете открыть *Окно наблюдения* в Microsoft Excel, нажав *Формулы > Наблюдение* *Окно*. В нем есть кнопка *Добавить наблюдение*, которую можно использовать, чтобы добавить ячейки для проверки. Точно так же вы можете использовать метод [**Worksheet.getCellWatches().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/cellwatchcollection#add-int-int-) для добавления ячеек в *Окно наблюдения* с использованием API Aspose.Cells.

## **Добавление ячеек в окно наблюдения формул Microsoft Excel**

В следующем образце кода устанавливается формула для ячеек C1 и E1 и добавляются обе из них в *Окно наблюдения*. Затем книга сохраняется как [файл Excel](67338509.xlsx). Если вы откроете файл Excel и просмотрите *Окно наблюдения*, то увидите обе ячейки, как показано на этом скриншоте.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Formulas-AddCellsToMicrosoftExcelFormulaWatchWindow.java" >}}
{{< app/cells/assistant language="java" >}}
