---
title: Реализовать ошибки и булевы значения на русском или любом другом языке с помощью Golang через C++
linktitle: Реализовать ошибки и булевы значения
type: docs
weight: 40
url: /ru/go-cpp/implement-errors-and-boolean-value-in-russian-or-any-other-language/
description: Изучить, как реализовать ошибки и булевы значения на русском или другом языке с помощью Aspose.Cells и Golang через C++.
---

## **Возможные сценарии использования**

Если вы используете Microsoft Excel на русском языке или другом языке/локали, ошибки и булевы значения будут отображаться согласно выбранной локали или языку. Это можно реализовать с помощью Aspose.Cells, используя свойство [**Workbook.GetGlobalizationSettings()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getglobalizationsettings/). Для этого необходимо переопределить методы класса [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/).

- [**GlobalizationSettings.GetErrorValueString()**](https://reference.aspose.com/cells/go-cpp/globalizationsettings/geterrorvaluestring/)
- [**GlobalizationSettings.GetBooleanValueString()**](https://reference.aspose.com/cells/go-cpp/globalizationsettings/getbooleanvaluestring/)

## **Реализация ошибок и логических значений на русском или на любом другом языке**

Приведенный ниже образец кода иллюстрирует, как реализовать ошибки и логические значения на русском или на любом другом языке. Пожалуйста, проверьте [используемый образец файл Excel](73990159.xlsx) в этом коде и его [выходной PDF](73990160.pdf). На скриншоте показано различие между образцом файла Excel и выходным PDF для справки.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage.go" >}}
