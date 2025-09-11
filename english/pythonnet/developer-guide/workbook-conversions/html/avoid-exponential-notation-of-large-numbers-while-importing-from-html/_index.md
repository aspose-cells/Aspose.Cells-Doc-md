---
title: Avoid exponential notation of large numbers while importing from HTML
type: docs
weight: 10
url: /python-net/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: This topic show you how to Avoid exponential notation of large numbers while importing from HTML using Aspose.Cells for Python via NET.
keywords: Avoid exponential notation of large numbers while importing from HTML, keep precision when importing html.
---

{{% alert color="primary" %}}

Sometimes your Html contains numbers like 1234567890123456 which are longer than 15 digits and when you import your HTML to excel file, these numbers convert to exponential notation like 1.23457E+15. If you want, your number should be imported as it is and not converted to exponential notation, then please use [**HTMLLoadOptions.keep_precision**](https://reference.aspose.com/cells/python-net/aspose.cells/abstracttextloadoptions/keep_precision/) property and set it **true** while loading your HTML.

{{% /alert %}}

The following sample code explains the usage of [**HTMLLoadOptions.keep_precision**](https://reference.aspose.com/cells/python-net/aspose.cells/abstracttextloadoptions/keep_precision/) property. The API will import the number as it is without converting it to exponential notation.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-AvoidExponentialNotationWhileImportingFromHtml-1.py" >}}
{{< app/cells/assistant language="python-net" >}}