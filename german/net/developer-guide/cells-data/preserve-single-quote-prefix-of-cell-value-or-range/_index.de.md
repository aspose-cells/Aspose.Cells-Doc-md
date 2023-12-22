---
title: Behalten Sie das einfache Anführungszeichen-Präfix des Werts oder Bereichs Cell bei
type: docs
weight: 310
url: /de/net/preserve-single-quote-prefix-of-cell-value-or-range/
description: Erfahren Sie, wie Sie das einfache Anführungszeichen-Präfix des Werts oder Bereichs Cell über Aspose.Cells for .NET API beibehalten.
keywords: Preserve Single Quote Prefix of Cell Value or Range, Hide leading apostrophe or single quote mark, Show leading apostrophe or single quote mark
---
##  **Mögliche Nutzungsszenarien**

Wenn Sie einen Wert in die Zelle einfügen, der ein Apostroph oder ein einfaches Anführungszeichen am Anfang hat, wird er von Microsoft in Excel ausgeblendet. Wenn Sie jedoch die Zelle auswählen, wird das Apostroph oder das einfache Anführungszeichen am Anfang in einer Bearbeitungsleiste angezeigt, wie im folgenden Screenshot gezeigt.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells verbirgt auch das führende Apostroph oder einfache Anführungszeichen wie Microsoft Excel, legt aber das fest[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) als**WAHR** für diese Zelle. Wenn Sie einen leeren Stil für die Zelle festlegen, dann[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) wird**FALSCH** wieder. Um dieses Problem zu lösen, bietet Aspose.Cells[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix) Eigenschaft, wenn sie festgelegt ist**false**, dann wird [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) überhaupt nicht aktualisiert und sein alter Wert bleibt erhalten . Das heißt, wenn der alte Wert der Eigenschaft [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) **wahr** war, dann wird **wahr bleiben** und wenn der alte Wert *falsch** war, bleibt er *falsch**.

##  **Behalten Sie das einfache Anführungszeichen-Präfix des Werts oder Bereichs Cell bei**

Der folgende Beispielcode erläutert die Verwendung von[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix)Eigentum wie zuvor beschrieben. Bitte lesen Sie die Kommentare im Code und sehen Sie sich die Konsolenausgabe des unten angegebenen Codes an, um weitere Hilfe zu erhalten.

##  **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.cs" >}}

##  **Konsolenausgabe**

{{< highlight "java" >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
