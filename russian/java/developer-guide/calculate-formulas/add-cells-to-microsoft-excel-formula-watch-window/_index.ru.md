---
title: Добавить Cells в Microsoft Окно просмотра формулы Excel
type: docs
weight: 20
url: /ru/java/add-cells-to-microsoft-excel-formula-watch-window/
---
## **Возможные сценарии использования**

Microsoft Excel Watch Window — это полезный инструмент для удобного просмотра значений ячеек и их формул в окне. Вы можете открыть*Окно просмотра*с помощью Microsoft Excel, нажав кнопку*Формулы > Смотреть* *Окно*. Он имеет*Добавить часы*Кнопка, которую можно использовать для добавления ячеек для проверки. Точно так же вы можете использовать[**Рабочий лист.getCellWatches().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/cellwatchcollection#add(int,%20int)) метод добавления ячеек в*Окно просмотра*используя Aspose.Cells API.

## **Добавить Cells в Microsoft Окно просмотра формулы Excel**

 В следующем примере кода задается формула ячеек C1 и E1, и обе они добавляются к*Окно просмотра*. Затем он сохраняет книгу как[выходной файл Excel](67338509.xlsx). Если вы откроете выходной файл Excel и просмотрите*Окно просмотра*, вы увидите обе ячейки, как показано на этом снимке экрана.

![дело:изображение_альтернативный_текст](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Formulas-AddCellsToMicrosoftExcelFormulaWatchWindow.java" >}}
