---
title: Conserva il prefisso delle virgolette singole del valore o intervallo Cell
type: docs
weight: 310
url: /it/net/preserve-single-quote-prefix-of-cell-value-or-range/
description: Scopri come preservare il prefisso delle virgolette singole del valore o dell'intervallo Cell tramite Aspose.Cells for .NET API.
keywords: Preserve Single Quote Prefix of Cell Value or Range, Hide leading apostrophe or single quote mark, Show leading apostrophe or single quote mark
---
##  **Possibili scenari di utilizzo**

Quando inserisci un valore all'interno della cella che contiene un apostrofo iniziale o una virgoletta singola, Microsoft Excel lo nasconde, ma quando selezioni la cella, visualizza l'apostrofo iniziale o la virgoletta singola in una barra della formula come mostrato nello screenshot seguente.

![cose da fare:immagine_alt_testo](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells nasconde anche l'apostrofo iniziale o la virgoletta singola come Microsoft Excel ma imposta il[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) COME**VERO** per quella cella. Se imposti uno stile vuoto della cella, allora[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) diventa**falso** Ancora. Per far fronte a questa problematica lo Aspose.Cells mette a disposizione[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix) proprietà, quando è impostata**false**, quindi [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) non viene aggiornato affatto e il suo vecchio valore viene conservato . Significa che se il vecchio valore della proprietà [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) era **true**, rimarrà **vero** e se il vecchio valore era *false**, rimarrà *false**.

##  **Conserva il prefisso delle virgolette singole del valore o intervallo Cell**

Il seguente codice di esempio spiega l'utilizzo di[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix)proprietà come descritto in precedenza. Per ulteriore assistenza, leggere i commenti all'interno del codice e vedere l'output della console del codice fornito di seguito.

##  **Codice d'esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.cs" >}}

##  **Uscita della console**

{{< highlight "java" >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
