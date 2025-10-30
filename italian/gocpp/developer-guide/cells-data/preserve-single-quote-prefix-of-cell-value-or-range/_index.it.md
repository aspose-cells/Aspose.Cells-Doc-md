---
title: Preserva il prefisso di citazione singola del valore o intervallo della cella con Golang tramite C++
linktitle: Conserva il prefisso apice singolo del valore della cella o dell intervallo
type: docs
weight: 310
url: /it/go-cpp/preserve-single-quote-prefix-of-cell-value-or-range/
description: Impara come preservare il prefisso di apice singolo del valore della cella o intervallo tramite l API Aspose.Cells for C++.
keywords: Conserva il prefisso di apostrofo singolo del valore della cella o dell intervallo, Nascondi l apostrofo singolo iniziale, Mostra l apostrofo singolo iniziale
---

## **Possibili Scenari di Utilizzo**

Quando si inserisce un valore all'interno della cella che ha un apostrofo o un segno di singolo apice all'inizio, allora Microsoft Excel lo nasconde, ma quando si seleziona la cella, visualizza l'apostrofo o il singolo apice nella barra della formula come mostrato nello screenshot seguente.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells nasconde anche l'apostrofo o il singolo apice all'inizio come Microsoft Excel, ma imposta [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) come **true** per quella cella. Se si imposta uno stile vuoto della cella, allora [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) diventa di nuovo **false**. Per gestire questo problema, Aspose.Cells fornisce la proprietà [**StyleFlag.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/getquoteprefix/), quando viene impostata su **false**, allora [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) non viene aggiornato affatto e il suo vecchio valore viene preservato. Ciò significa che se il vecchio valore della proprietà [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) era **true**, rimarrà **true** e se il vecchio valore era **false**, rimarrà **false**.

## **Conserva il prefisso apice singolo del valore della cella o dell'intervallo**

Il codice di esempio seguente spiega l'uso della proprietà [**StyleFlag.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/styleflag/getquoteprefix/) come descritto in precedenza. Si prega di leggere i commenti all'interno del codice e vedere l'output della console del codice di seguito per ulteriore assistenza.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PreserveSingleQuotePrefixOfCellValueOrRange.go" >}}
## **Output della console**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
