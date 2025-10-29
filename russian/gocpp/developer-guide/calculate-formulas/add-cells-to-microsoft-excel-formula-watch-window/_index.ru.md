---
title: Добавление ячеек в окно отслеживания формул Microsoft Excel с Golang через C++
linktitle: Добавить ячейки в окно наблюдения формул
description: Узнайте, как использовать Aspose.Cells for C++ для добавления ячеек в окно наблюдения формул в Excel. Загрузите или создайте файл Excel, манипулируйте ячейками, задавайте формулы и сохраните изменённый файл.
keywords: Aspose.Cells, Excel, окно наблюдения формул, ячейки, добавление, C++
type: docs
weight: 60
url: /ru/go-cpp/add-cells-to-microsoft-excel-formula-watch-window/
---

## **Возможные сценарии использования**

Окно наблюдения в Microsoft Excel — это полезный инструмент для удобного мониторинга значений ячеек и их формул в окне. Вы можете открыть *Окно наблюдения* в Microsoft Excel, выбрав *Формулы > Окно наблюдения*. В нем есть кнопка *Добавить наблюдение*, которая используется для добавления ячеек для проверки. Аналогично, вы можете использовать метод [**Worksheet.CellWatches.Add()**](https://reference.aspose.com/cells/go-cpp/cellwatchcollection/add_int_int/) для добавления ячеек в *Окно наблюдения* с помощью API Aspose.Cells.

## **Добавление ячеек в окно наблюдения формул Microsoft Excel**

Следующий пример кода устанавливает формулу ячеек C1 и E1 и добавляет обе ячейки в окно наблюдения. Затем он сохраняет книгу как [выходной файл Excel](67338481.xlsx). Если вы откроете выходной файл Excel и посмотрите *Окно наблюдения*, вы увидите обе ячейки, как показано на этом скриншоте.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddCellsToMicrosoftExcelFormulaWatchWindow.go" >}}
