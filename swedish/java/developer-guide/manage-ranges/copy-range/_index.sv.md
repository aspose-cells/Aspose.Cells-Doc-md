---
title: Kopiera intervall för Excel
linktitle: Kopiera intervall
type: docs
weight: 30
url: /sv/java/copy-ranges-of-Excel/
---
## **Introduktion**

I Excel kan du välja ett intervall, kopiera intervallet och sedan klistra in det med specifika alternativ i samma kalkylblad, andra kalkylblad eller andra filer.

## **Kopiera intervall med Aspose.Cells**

 Aspose.Cells ger viss överbelastning[Range.Copy](https://reference.aspose.com/cells/java/com.aspose.cells/range) metoder för att kopiera intervallet.
## **Kopiera intervall**

Skapa två intervall: källintervallet, målintervallet, kopiera sedan källintervallet till målintervallet med metoden Range.Copy.

Se följande kod:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Copy-Range.java" >}}

## **Klistra in intervall med alternativ**

Aspose.Cells stöder inklistring av intervallet med specifik typ.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Paste-Range.java" >}}

## **Kopiera endast data från intervallet.**
Du kan också kopiera data med Range.CopyData-metoden som följande koder:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Copy-Range-Data.java" >}}


