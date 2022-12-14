---
title: Kopiera endast intervalldata
type: docs
weight: 330
url: /sv/java/copy-range-data-only/
---
{{% alert color="primary" %}} 

Ibland måste du kopiera data från ett cellområde till ett annat, bara kopiera data, inte formateringen. Aspose.Cells erbjuder denna funktion genom att tillhandahålla[Range.copyData](https://reference.aspose.com/cells/java/com.aspose.cells/range#copyData\(com.aspose.cells.Range\)) metod.

{{% /alert %}} 
## **Kopiera endast intervalldata**
Det här exemplet visar hur man:

1. Skapa en arbetsbok.
1. Lägg till data i celler i det första kalkylbladet.
1. Skapa ett intervall.
1. Skapa ett stilobjekt med specificerade formateringsattribut.
1. Använd stilformateringen på intervallet.
1. Skapa ytterligare ett cellområde.
1.  Kopiera data från det första intervallet till detta andra intervall med hjälp av[Range.copyData](https://reference.aspose.com/cells/java/com.aspose.cells/range#copyData\(com.aspose.cells.Range\)) metod.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRangeDataOnly-CopyRangeDataOnly.java" >}}
