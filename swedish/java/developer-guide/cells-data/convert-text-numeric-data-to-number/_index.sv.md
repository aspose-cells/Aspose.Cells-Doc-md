---
title: Konvertera numeriska textdata till nummer
type: docs
weight: 150
url: /sv/java/convert-text-numeric-data-to-number/
description: Lär dig hur du konverterar siffror som lagrats som text till siffror genom att använda Aspose.Cells for Java API.
keywords: excel convert text to number, excel convert text to number java, excel convert text numeric data to number, excel convert text numeric data to number java, excel convert numeric text to number, excel convert numeric text to number java, excel convert numeric text to number with java, convert numeric text to number in excel with java, convert numeric text to number in excel with java, convert numeric string to number in excel with java, excel convert text numeric data to number java, excel convert numeric string to number java
---
{{% alert color="primary" %}}

 Ibland vill du konvertera numerisk data som skrivits in som text till siffror. Du kan ange siffror som text i Microsoft Excel genom att sätta en apostrof före en siffra, till exempel**'12345**. Excel behandlar sedan numret som en sträng. Aspose.Cells låter dig konvertera strängar till tal.

{{% /alert %}}

Aspose.Cells for Java API tillhandahåller[**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#convertStringToNumericValue()) metod som kan användas för att konvertera alla numeriska sträng- eller textdata till siffror.

 Följande skärmdump visar strängnummer i celler**A1:A17**. Strängnummer är justerade till vänster.

**Indatafil: siffror som anges som textsträngar** 

![todo:image_alt_text](convert-text-numeric-data-to-number_1.png)

Dessa strängnummer har konverterats till tal med hjälp av[**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#convertStringToNumericValue()) i följande skärmdump. Som du kan se är de nu högerjusterade.

**Utdatafil: strängarna har konverterats till tal** 

![todo:image_alt_text](convert-text-numeric-data-to-number_2.png)

Följande exempelkod illustrerar hur du konverterar alla numeriska strängdata till faktiska tal i alla kalkylblad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConvertTextNumericDatatoNumber-ConvertTextNumericDatatoNumber.java" >}}
