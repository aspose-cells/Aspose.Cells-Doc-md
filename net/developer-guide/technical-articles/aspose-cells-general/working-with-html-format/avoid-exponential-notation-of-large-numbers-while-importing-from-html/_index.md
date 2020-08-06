---
title: Avoid exponential notation of large numbers while importing from Html
type: docs
weight: 10
url: /net/avoid-exponential-notation-of-large-numbers-while-importing-from-html/
---

{{% alert color="primary" %}} 

Sometimes your Html contains numbers like 1234567890123456 which are longer than 15 digits and when you import your HTML to excel file, these numbers convert to exponential notation like 1.23457E+15. If you want, your number should be imported as it is and not converted to exponential notation, then please use [HTMLLoadOptions.KeepPrecision](https://apireference.aspose.com/net/cells/aspose.cells/abstracttextloadoptions/properties/keepprecision) property and set it **true** while loading your HTML.

{{% /alert %}} 

The following sample code explains the usage of [HTMLLoadOptions.KeepPrecision](https://apireference.aspose.com/net/cells/aspose.cells/abstracttextloadoptions/properties/keepprecision) property. The API will import the number as it is without converting it to exponential notation.



{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-AvoidExponentialNotationWhileImportingFromHtml-1.cs" >}}
