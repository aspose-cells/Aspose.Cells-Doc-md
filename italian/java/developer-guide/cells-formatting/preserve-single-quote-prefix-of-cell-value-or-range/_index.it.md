---
title: Conserva il prefisso apice singolo del valore della cella o dell intervallo
type: docs
weight: 1900
url: /it/java/preserve-single-quote-prefix-of-cell-value-or-range/
---

## **Possibili Scenari di Utilizzo**

Quando si inserisce un valore dentro la cella che ha un apice iniziale o un simbolo di apice singolo, Microsoft Excel lo nasconde, ma quando si seleziona la cella, visualizza il prefisso apice in un formula bar come mostrato nella seguente schermata.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells nasconde anche l'apostrofo iniziale o il singolo segno di citazione come Microsoft Excel ma imposta il [**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) come **true** per quella cella. Se si imposta uno stile vuoto della cella, allora [**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) diventa nuovamente **false**. Per affrontare questo problema, Aspose.Cells fornisce la proprietà [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix), quando impostata su **false**, allora [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix) non viene affatto aggiornata e il suo vecchio valore viene preservato. Significa che se il vecchio valore della proprietà [**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) era **true**, rimarrà true e se il vecchio valore era false, rimarrà false.

## **Conserva il prefisso apice singolo del valore della cella o dell'intervallo**

Il seguente codice di esempio spiega l'utilizzo della proprietà [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix) come descritto in precedenza. Si prega di leggere i commenti all'interno del codice e vedere l'output della console del codice qui sotto per ulteriori dettagli.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.java" >}}

## **Output della console**

{{< highlight java >}}

Quote Prefix of Cell A1: false

Quote Prefix of Cell A1: true

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: true

Quote Prefix of Cell A1: false

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
