---
title: Реализовать ошибки и логическое значение на русском или любом другом языке
type: docs
weight: 40
url: /ru/net/implement-errors-and-boolean-value-in-russian-or-any-other-language/
---
## **Возможные сценарии использования**

Если вы используете Microsoft Excel в русской локали или языке или любой другой локали или языке, он будет отображать ошибки и логические значения в соответствии с этой локалью или языком. Вы можете добиться аналогичного поведения, используя Aspose.Cells, используя**[Workbook.Settings.GlobalizationSettings**] (https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings). Вам придется переопределить следующие методы[**Настройки глобализации**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)учебный класс.

- [**GlobalizationSettings.GetErrorValueString()**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/geterrorvaluestring)
- [**GlobalizationSettings.GetBooleanValueString()**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getbooleanvaluestring)

## **Реализовать ошибки и логическое значение на русском или любом другом языке**

 В следующем примере кода показано, как реализовать ошибки и логическое значение на русском или любом другом языке. Пожалуйста, проверьте[Образец файла Excel](73990159.xlsx) используется в этом коде и его[Выходной PDF-файл](73990160.pdf)На снимке экрана показана разница между образцом файла Excel и выходным PDF-файлом для справки.

![дело:изображение_альтернативный_текст](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.cs" >}}
