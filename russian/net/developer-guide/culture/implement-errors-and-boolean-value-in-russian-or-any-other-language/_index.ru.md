---
title: Реализация ошибок и логических значений на русском или на любом другом языке
type: docs
weight: 40
url: /ru/net/implement-errors-and-boolean-value-in-russian-or-any-other-language/
---

## **Возможные сценарии использования**

Если вы используете Microsoft Excel на русском языке, локали или на любом другом языке, он будет отображать ошибки и логические значения в соответствии с этой локалью или языком. Вы можете добиться похожего поведения при использовании Aspose.Cells с помощью свойства [**Workbook.Settings.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings). Вам нужно переопределить следующие методы класса [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings).

- [**GlobalizationSettings.GetErrorValueString()**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/geterrorvaluestring)
- [**GlobalizationSettings.GetBooleanValueString()**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getbooleanvaluestring)

## **Реализация ошибок и логических значений на русском или на любом другом языке**

Приведенный ниже образец кода иллюстрирует, как реализовать ошибки и логические значения на русском или на любом другом языке. Пожалуйста, проверьте [используемый образец файл Excel](73990159.xlsx) в этом коде и его [выходной PDF](73990160.pdf). На скриншоте показано различие между образцом файла Excel и выходным PDF для справки.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.cs" >}}
{{< app/cells/assistant language="csharp" >}}
