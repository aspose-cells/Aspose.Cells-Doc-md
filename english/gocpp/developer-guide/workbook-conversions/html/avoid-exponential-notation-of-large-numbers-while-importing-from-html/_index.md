---
title: Avoid exponential notation of large numbers while importing from HTML with Golang via C++
linktitle: Avoid exponential notation of large numbers while importing from HTML
type: docs
weight: 10
url: /go-cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: Learn how to avoid exponential notation of large numbers while importing from HTML using Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Sometimes your HTML contains numbers like 1234567890123456 which are longer than 15 digits, and when you import your HTML to an Excel file, these numbers convert to exponential notation like 1.23457E+15. If you want your number to be imported as it is and not converted to exponential notation, then please use the [**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/go-cpp/abstracttextloadoptions/getkeepprecision/) property and set it to **true** while loading your HTML.

{{% /alert %}}

The following sample code explains the usage of the [**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/go-cpp/abstracttextloadoptions/getkeepprecision/) property. The API will import the number as it is without converting it to exponential notation.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AvoidExponentialNotationOfLargeNumbersWhileImportingFromHtml.go" >}}