---
title: Conserva il prefisso apice singolo del valore della cella o dell intervallo
type: docs
weight: 310
url: /it/net/preserve-single-quote-prefix-of-cell-value-or-range/
description: Scopri come conservare il prefisso di apostrofo singolo del valore della cella o dell intervallo tramite l API Aspose.Cells for .NET.
keywords: Conserva il prefisso di apostrofo singolo del valore della cella o dell intervallo, Nascondi l apostrofo singolo iniziale, Mostra l apostrofo singolo iniziale
---

## **Possibili Scenari di Utilizzo**

Quando si inserisce un valore dentro la cella che ha un apice iniziale o un simbolo di apice singolo, Microsoft Excel lo nasconde, ma quando si seleziona la cella, visualizza il prefisso apice in un formula bar come mostrato nella seguente schermata.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Anche Aspose.Cells nasconde l'apostrofo singolo iniziale come Microsoft Excel, ma imposta il [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) come vero per quella cella. Se si imposta uno stile vuoto della cella, allora [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) diventa di nuovo falso. Per affrontare questo problema, Aspose.Cells fornisce la proprietà [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix), quando è impostata su falso, allora [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) non viene aggiornato affatto e conserva il suo vecchio valore. Ciò significa che se il vecchio valore della proprietà [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) era vero, rimarrà vero e se il vecchio valore era falso, rimarrà falso.

## **Conserva il prefisso apice singolo del valore della cella o dell'intervallo**

Il seguente codice di esempio spiega l'uso della proprietà [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix) come descritto in precedenza. Si prega di leggere i commenti all'interno del codice e di vedere l'output della console del codice sottostante per ulteriore aiuto.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.cs" >}}

## **Output della console**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
