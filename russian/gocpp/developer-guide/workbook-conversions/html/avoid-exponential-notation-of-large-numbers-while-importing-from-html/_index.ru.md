---
title: Избегайте экспоненциального отображения больших чисел при импорте из HTML с помощью Golang через C++
linktitle: Избегайте экспоненциальной нотации больших чисел при импорте из HTML
type: docs
weight: 10
url: /ru/go-cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: Узнайте, как избежать экспоненциального отображения больших чисел при импорте из HTML с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Иногда ваши HTML содержит числа вроде 1234567890123456, длиной более 15 цифр, и при импорте в файл Excel эти числа преобразуются в экспоненциальное отображение, например 1.23457E+15. Чтобы импортировать число как есть и не преобразовывать его в экспоненциальное отображение, используйте свойство [**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/go-cpp/abstracttextloadoptions/getkeepprecision/) и установите его в **true** при загрузке HTML.

{{% /alert %}}

Следующий пример кода объясняет использование свойства [**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/go-cpp/abstracttextloadoptions/getkeepprecision/). API импортирует число как есть без преобразования в экспоненциальное отображение.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AvoidExponentialNotationOfLargeNumbersWhileImportingFromHtml.go" >}}
