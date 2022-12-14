---
title: Kopiera intervalldata med stil
type: docs
weight: 340
url: /sv/java/copy-range-data-with-style/
---
{{% alert color="primary" %}} 

[Kopiera endast intervalldata](/cells/sv/java/copy-range-data-only/) förklarade hur man kopierar data från ett cellområde till ett annat område. Aspose.Cells kan också kopiera ett intervall komplett med formatering. Den här artikeln förklarar hur.

{{% /alert %}} 
## **Kopiera intervalldata med stil**
Aspose.Cells tillhandahåller en rad klasser och metoder för att arbeta med intervall, till exempel,[createRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)), [StilFlagga](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag), [appliceraStyle()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#applyStyle\(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag\)), etc.

Detta exempel:

1. Skapar en arbetsbok.
1. Fyller ett antal celler i det första kalkylbladet med data.
1. Skapar ett intervall.
1. Skapar ett stilobjekt med specificerade formateringsattribut.
1. Tillämpar stilen på dataintervallet.
1. Skapar ett andra cellområde.
1. Kopierar data med formateringen från det första intervallet till det andra intervallet.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRangeDataWithStyle-CopyRangeDataWithStyle.java" >}}

