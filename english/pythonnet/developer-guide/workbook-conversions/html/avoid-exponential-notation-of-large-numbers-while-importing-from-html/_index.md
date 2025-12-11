---
title: Avoid exponential notation of large numbers while importing from HTML
type: docs
weight: 10
url: /python-net/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: This topic shows you how to avoid exponential notation of large numbers while importing from HTML using Aspose.Cells for Python via .NET.
keywords: Avoid exponential notation of large numbers while importing from HTML, keep precision when importing html.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes your HTML contains numbers like 1234567890123456 which are longer than 15 digits, and when you import your HTML to an Excel file, these numbers are converted to exponential notation like 1.23457E+15. If you want your number to be imported as it is and not converted to exponential notation, then please use the [**HTMLLoadOptions.keep_precision**](https://reference.aspose.com/cells/python-net/aspose.cells/abstracttextloadoptions/keep_precision/) property and set it to **true** while loading your HTML.

{{% /alert %}}

The following sample code explains the usage of [**HTMLLoadOptions.keep_precision**](https://reference.aspose.com/cells/python-net/aspose.cells/abstracttextloadoptions/keep_precision/) property. The API will import the number as it is without converting it to exponential notation.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-AvoidExponentialNotationWhileImportingFromHtml-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
