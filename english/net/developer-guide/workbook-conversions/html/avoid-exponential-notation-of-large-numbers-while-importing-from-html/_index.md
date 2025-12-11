---
title: Avoid exponential notation of large numbers while importing from HTML
type: docs
weight: 10
url: /net/avoid-exponential-notation-of-large-numbers-while-importing-from/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes your HTML contains numbers like 1234567890123456 which are longer than 15 digits, and when you import your HTML to an Excel file, these numbers are converted to exponential notation such as 1.23457E+15. If you want the number to be imported exactly as it appears and not converted to exponential notation, please use the [**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision) property and set it to **true** while loading your HTML.

{{% /alert %}}

The following sample code explains the usage of [**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision) property. The API will import the number as it is without converting it to exponential notation.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AvoidExponentialNotationWhileImportingFromHtml-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
