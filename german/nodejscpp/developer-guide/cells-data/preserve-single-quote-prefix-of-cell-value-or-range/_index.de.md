---
title: Behalten Sie das einfache Anführungszeichenpräfix des Zellwerts oder bereichs bei
type: docs
weight: 310
url: /de/nodejs-cpp/preserve-single-quote-prefix-of-cell-value-or-range/
description: Lernen Sie, wie Sie die Einzelzitat Präfix eines Zellwerts oder Bereichs über die API Aspose.Cells for Node.js via C++ bewahren.
keywords: Einzelzitat Präfix des Zellwerts oder Bereichs in Node.js via C++, führendes Apostroph oder einzelnes Anführungszeichen in Node.js via C++ ausblenden, führendes Apostroph oder einzelnes Anführungszeichen in Node.js via C++ anzeigen
---

## **Mögliche Verwendungsszenarien**

Wenn Sie einen Wert in die Zelle einsetzen, der ein führendes Apostroph oder einfach Anführungszeichen hat, verbirgt es Microsoft Excel, aber wenn Sie die Zelle auswählen, zeigt es das führende Apostroph oder Anführungszeichen in einer Formelleiste an, wie im folgenden Screenshot gezeigt.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells for Node.js via C++ versteckt auch das führende Apostroph oder einzelne Anführungszeichen wie Microsoft Excel, setzt aber [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-) auf **wahr** für diese Zelle. Wenn Sie einen leeren Stil für die Zelle setzen, wird [**Style.getQuotePrefix()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getQuotePrefix--) wieder auf **falsch** gesetzt. Um dieses Problem zu lösen, bietet Aspose.Cells for Node.js via C++ die [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-)-Methode, bei der, wenn sie auf **falsch** gesetzt ist, [**Style.getQuotePrefix()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getQuotePrefix--) überhaupt nicht aktualisiert wird und sein alter Wert beibehalten wird. Das bedeutet, wenn der alte Wert von [**Style.getQuotePrefix()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getQuotePrefix--) **wahr** war, bleibt er **wahr**, und wenn der alte Wert **falsch** war, bleibt er **falsch**.

## **Einzelnes Anführungszeichen-Prefix des Zellenwerts oder -bereichs beibehalten**

Der folgende Beispielcode erklärt die Verwendung der [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-)-Methode, wie zuvor beschrieben. Lesen Sie die Kommentare im Code und sehen Sie sich die unten angegebene Konsolenausgabe für weitere Hilfe an.

## **Beispielcode**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-preserve-single-quote-prefix-of-cell-value-or-range.js" >}}



## **Konsolenausgabe**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.quotePrefix is False, it means, do not update the value of Cell.Style.quotePrefix.

Similarly, when StyleFlag.quotePrefix is True, it means, update the value of Cell.Style.quotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
