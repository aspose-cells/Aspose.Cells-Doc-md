---
title: Реализация ошибок и логических значений на русском или на любом другом языке
type: docs
weight: 30
url: /ru/java/implement-errors-and-boolean-value-in-russian-or-any-other-language/
---

## **Возможные сценарии использования**
Если вы используете Microsoft Excel на русской локали или языке или на любой другой локали или языке, он будет отображать ошибки и логические значения в соответствии с этой локалью или языком. Вы можете добиться аналогичного поведения, используя метод или свойство [Workbook.getSettings().setGlobalizationSettings()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) класса Aspose.Cells. Вам нужно будет переопределить следующие методы класса [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings).

- [GlobalizationSettings.getErrorValueString()](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getErrorValueString\(java.lang.String\))
- [GlobalizationSettings.getBooleanValueString()](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getBooleanValueString\(boolean\))
## **Реализация ошибок и логических значений на русском или на любом другом языке**
В следующем образце кода показано, как реализовать ошибки и логические значения на русском или на любом другом языке. Пожалуйста, проверьте образец Excel-файла, использованный в этом коде, и его выходной PDF. На скриншоте показано различие между [образцом Excel-файла](48496697.xlsx) и [выходным PDF](48496696.pdf) для справки.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)
## **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookSettings-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.java" >}}
