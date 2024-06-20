---
title: Behalten Sie das einfache Anführungszeichenpräfix des Zellwerts oder bereichs bei
type: docs
weight: 1900
url: /de/java/preserve-single-quote-prefix-of-cell-value-or-range/
---

## **Mögliche Verwendungsszenarien**

Wenn Sie einen Wert in die Zelle einsetzen, der ein führendes Apostroph oder einfach Anführungszeichen hat, verbirgt es Microsoft Excel, aber wenn Sie die Zelle auswählen, zeigt es das führende Apostroph oder Anführungszeichen in einer Formelleiste an, wie im folgenden Screenshot gezeigt.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells blendet auch das führende Apostroph oder Anführungszeichen wie Microsoft Excel aus, aber es setzt das [**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) als **true** für diese Zelle. Wenn Sie einen leeren Stil der Zelle festlegen, wird [**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) wieder **false**. Um dieses Problem zu lösen, bietet Aspose.Cells die Eigenschaft [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix). Wenn sie auf **false** gesetzt wird, wird [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix) gar nicht aktualisiert und ihr alter Wert wird beibehalten. Das bedeutet, wenn der alte Wert der [**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix)-Eigenschaft **true** war, bleibt er wahr, und wenn der alte Wert falsch war, bleibt er falsch.

## **Einzelnes Anführungszeichen-Prefix des Zellenwerts oder -bereichs beibehalten**

Der folgende Beispielcode erläutert die Verwendung der [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix)-Eigenschaft, wie zuvor beschrieben. Bitte lesen Sie die Kommentare im Code und sehen Sie die Konsolenausgabe des unten gegebenen Codes für weitere Hilfe.

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.java" >}}

## **Konsolenausgabe**

{{< highlight java >}}

Quote Prefix of Cell A1: false

Quote Prefix of Cell A1: true

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: true

Quote Prefix of Cell A1: false

{{< /highlight >}}
