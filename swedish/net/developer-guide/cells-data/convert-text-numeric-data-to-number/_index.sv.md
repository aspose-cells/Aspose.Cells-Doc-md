---
title: Konvertera numeriska textdata till nummer
type: docs
weight: 900
url: /sv/net/convert-text-numeric-data-to-number/
description: Lär dig hur du konverterar siffror lagrade som text i Excel till siffror genom att använda Aspose.Cells for .NET API.
keywords: excel convert text to number, excel convert text to number c#, excel convert text numeric data to number, excel convert text numeric data to number c#, excel convert numeric text to number, excel convert numeric text to number c#, excel convert numeric text to number with c#, convert numeric text to number in excel with c#, convert numeric text to number in excel with c#, convert numeric string to number in excel with c#, excel convert text numeric data to number c#, excel convert numeric string to number c#
---
{{% alert color="primary" %}}

 Ibland vill du konvertera numerisk data som skrivits in som text till siffror. Du kan ange siffror som text i Microsoft Excel genom att sätta en apostrof före en siffra, till exempel**'12345**. Excel behandlar sedan numret som en sträng. Aspose.Cells låter dig konvertera strängar till tal.

{{% /alert %}}

Aspose.Cells tillhandahåller[**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue)metod som kan användas för att konvertera alla numeriska sträng- eller textdata till siffror.

 Följande skärmdump visar strängnummer i celler**A1:A17**. Strängnummer är justerade till vänster.

|**Indatafil: siffror som anges som textsträngar**|
|:- |
|![todo:image_alt_text](convert-text-numeric-data-to-number_1.png)|

Dessa strängnummer har konverterats till tal med hjälp av[**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue)i följande skärmdump. Som du kan se är de nu högerjusterade.

|**Utdatafil: strängarna har konverterats till tal**|
|:- |
|![todo:image_alt_text](convert-text-numeric-data-to-number_2.png)|

## C# kod för att konvertera sträng numeriska data till faktiska tal

Följande exempelkod illustrerar hur du konverterar alla numeriska strängdata till faktiska tal i alla kalkylblad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ConvertStringToNumericValue-ConvertTextNumericDatatoNumber.cs" >}}
