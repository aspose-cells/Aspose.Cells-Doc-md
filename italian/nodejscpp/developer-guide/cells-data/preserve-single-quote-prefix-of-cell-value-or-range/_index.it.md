---
title: Conserva il prefisso apice singolo del valore della cella o dell intervallo
type: docs
weight: 310
url: /it/nodejs-cpp/preserve-single-quote-prefix-of-cell-value-or-range/
description: Impara come Preservare il Prefisso con Singolo Apostrofo del Valore di Cella o Intervallo tramite l API Aspose.Cells for Node.js via C++.
keywords: Preserva il Prefisso con Apostrofo Singolo di Valore di Cella o Intervallo Node.js via C++, Nascondi l apostrofo iniziale o il segno di virgoletta singola Node.js via C++, Mostra l apostrofo iniziale o il segno di virgoletta singola Node.js via C++
---

## **Possibili Scenari di Utilizzo**

Quando si inserisce un valore dentro la cella che ha un apice iniziale o un simbolo di apice singolo, Microsoft Excel lo nasconde, ma quando si seleziona la cella, visualizza il prefisso apice in un formula bar come mostrato nella seguente schermata.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells for Node.js via C++ nasconde anche l'apostrofo o la virgoletta singola iniziale come Microsoft Excel, ma imposta [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-) su **true** per quella cella. Se imposti uno stile vuoto sulla cella, allora [**Style.getQuotePrefix()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getQuotePrefix--) ritorna a essere **false**. Per gestire questa questione, Aspose.Cells for Node.js via C++ fornisce il metodo [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-), che quando impostato su **false**, [**Style.getQuotePrefix()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getQuotePrefix--) non viene aggiornato e il suo vecchio valore viene preservato. Ciò significa che se il vecchio valore di [**Style.getQuotePrefix()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getQuotePrefix--) era **true**, rimarrà **true** e se era **false**, rimarrà **false**.

## **Conserva il prefisso apice singolo del valore della cella o dell'intervallo**

Il codice di esempio seguente spiega l'uso del metodo [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-) come descritto precedentemente. Leggi i commenti nel codice e guarda l'output della console di seguito per ulteriore assistenza.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-preserve-single-quote-prefix-of-cell-value-or-range.js" >}}



## **Output della console**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.quotePrefix is False, it means, do not update the value of Cell.Style.quotePrefix.

Similarly, when StyleFlag.quotePrefix is True, it means, update the value of Cell.Style.quotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
