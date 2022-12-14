---
title: Реализовать ошибки и логическое значение на русском или любом другом языке
type: docs
weight: 30
url: /ru/java/implement-errors-and-boolean-value-in-russian-or-any-other-language/
---
## **Возможные сценарии использования**
 Если вы используете Microsoft Excel в русской локали или языке или любой другой локали или языке, он будет отображать ошибки и логические значения в соответствии с этой локалью или языком. Вы можете добиться аналогичного поведения, используя Aspose.Cells[Рабочая книга.getSettings().setGlobalizationSettings()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) метод или свойство. Вам придется переопределить следующие методы[Настройки глобализации](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings)учебный класс.

- [GlobalizationSettings.getErrorValueString()](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getErrorValueString\(java.lang.String\))
- [GlobalizationSettings.getBooleanValueString()](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getBooleanValueString\(boolean\))
## **Реализовать ошибки и логическое значение на русском или любом другом языке**
 В следующем примере кода показано, как реализовать ошибки и логическое значение на русском или любом другом языке. Пожалуйста, проверьте образец файла Excel, используемый в этом коде, и его выходной PDF-файл. На скриншоте показана разница между[Образец файла Excel](48496697.xlsx) и[Выходной PDF-файл](48496696.pdf) для справки.

![дело:изображение_альтернативный_текст](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)
## **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookSettings-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.java" >}}
