---
title: Behalten Sie das einfache Anführungszeichenpräfix des Zellwerts oder bereichs bei
type: docs
weight: 310
url: /de/python-net/preserve-single-quote-prefix-of-cell-value-or-range/
description: Erfahren Sie, wie Sie das einfache Anführungszeichenpräfix des Zellwerts oder bereichs durch die Aspose.Cells für Python via .NET API beibehalten.
keywords: Python Excel Bibliothek, Python Beibehaltung des einfachen Anführungszeichenpräfix des Zellwerts oder bereichs, Python Ausblenden des führenden Apostrophs oder des einfachen Anführungszeichens, Python Anzeigen des führenden Apostrophs oder einfachen Anführungszeichens
---

## **Mögliche Verwendungsszenarien**

Wenn Sie einen Wert in die Zelle einsetzen, der ein führendes Apostroph oder einfach Anführungszeichen hat, verbirgt es Microsoft Excel, aber wenn Sie die Zelle auswählen, zeigt es das führende Apostroph oder Anführungszeichen in einer Formelleiste an, wie im folgenden Screenshot gezeigt.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells für Python via .NET verbirgt auch das führende Apostroph oder Anführungszeichen wie Microsoft Excel, setzt aber die [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) für diese Zelle auf **true**. Wenn Sie einen leeren Stil der Zelle setzen, wird [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) wieder zu **false**. Um dieses Problem zu beheben, bietet Aspose.Cells für Python via .NET die Eigenschaft [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix). Wenn es auf **false** gesetzt wird, wird [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) überhaupt nicht aktualisiert, und ihr alter Wert wird beibehalten. Das bedeutet, wenn der alte Wert der [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix)-Eigenschaft **true** war, bleibt er auch **true**, und wenn der alte Wert **false** war, bleibt er auch **false**.

## **Einzelnes Anführungszeichen-Prefix des Zellenwerts oder -bereichs beibehalten**

Der folgende Beispielcode erläutert die Verwendung der [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix)-Eigenschaft, wie zuvor beschrieben. Bitte lesen Sie die Kommentare im Code und sehen Sie die Konsolenausgabe des folgenden Codes für weitere Hilfe.

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-PreserveSingleQuotePrefixOfCellValueOrRange.py" >}}

## **Konsolenausgabe**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.quote_prefix is False, it means, do not update the value of Cell.Style.quote_prefix.

Similarly, when StyleFlag.quote_prefix is True, it means, update the value of Cell.Style.quote_prefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
