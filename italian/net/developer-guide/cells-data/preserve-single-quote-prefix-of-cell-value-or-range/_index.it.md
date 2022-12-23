---
title: Conserva il prefisso delle virgolette singole del valore o intervallo Cell
type: docs
weight: 310
url: /it/net/preserve-single-quote-prefix-of-cell-value-or-range/
---
## **Possibili scenari di utilizzo**

Quando inserisci un valore all'interno della cella che ha l'apostrofo iniziale o le virgolette singole, Microsoft Excel lo nasconde, ma quando selezioni la cella, visualizza l'apostrofo iniziale o le virgolette singole in una barra della formula come mostrato nello screenshot seguente.

![cose da fare:immagine_alt_testo](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells nasconde anche l'apostrofo iniziale o le virgolette singole come Microsoft Excel ma imposta il[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) come**VERO** per quella cella Se imposti uno stile vuoto della cella, allora[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) diventa**falso** ancora. Per far fronte a questo problema, Aspose.Cells fornisce[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix) proprietà, quando è impostata**falso** , poi[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)non viene affatto aggiornato e il suo vecchio valore viene preservato. Significa se il vecchio valore di[**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)proprietà era**VERO** , rimarrà**VERO** e se il vecchio valore era**falso** , rimarrà**falso**.

## **Conserva il prefisso delle virgolette singole del valore o intervallo Cell**

 Il seguente codice di esempio spiega l'utilizzo di[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix)proprietà come descritto in precedenza. Si prega di leggere i commenti all'interno del codice e vedere l'output della console del codice indicato di seguito per ulteriore aiuto.

## **Codice d'esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.cs" >}}

## **Uscita console**

{{< highlight "java" >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
