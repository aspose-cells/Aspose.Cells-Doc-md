---
title: Добавление ячеек в окно наблюдения формул Microsoft Excel
description: Как использовать библиотеку Aspose.Cells для добавления ячеек в окно наблюдения формул в Excel. Загрузив существующий файл Excel или создав новый, мы можем манипулировать ячейками и задавать формулы. Наконец, мы сохраняем измененный файл Excel на диск.
keywords: Aspose.Cells, Excel, Окно наблюдения формул, Ячейки, Добавление
type: docs
weight: 60
url: /ru/net/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Возможные сценарии использования**

Окно наблюдения Microsoft Excel - это удобный инструмент для отслеживания значений ячеек и их формул в окне. Вы можете открыть *Окно наблюдения* в Microsoft Excel, щелкнув *Формулы > Окно наблюдения*. В нем есть кнопка *Добавить наблюдение*, которую можно использовать для добавления ячеек для проверки. Аналогично, вы можете использовать метод [**Worksheet.CellWatches.Add()**](https://reference.aspose.com/cells/net/aspose.cells/cellwatchcollection/methods/add/index) для добавления ячеек в *Окно наблюдения* с помощью API Aspose.Cells.

## **Добавление ячеек в окно наблюдения формул Microsoft Excel**

В следующем фрагменте кода задается формула для ячеек C1 и E1, и обе из них добавляются в окно наблюдения. Затем книга сохраняется как [выходной файл Excel](67338481.xlsx). Если вы откроете выходной файл Excel и просмотрите *Окно наблюдения*, то увидите обе ячейки, как показано на скриншоте.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Formulas-AddCellsToMicrosoftExcelFormulaWatchWindow.cs" >}}
{{< app/cells/assistant language="csharp" >}}
