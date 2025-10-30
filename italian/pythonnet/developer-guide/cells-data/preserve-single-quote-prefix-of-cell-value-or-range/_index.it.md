---
title: Conserva il prefisso apice singolo del valore della cella o dell intervallo
type: docs
weight: 310
url: /it/python-net/preserve-single-quote-prefix-of-cell-value-or-range/
description: Scopri come Conservare il Prefisso Apice Singolo del Valore della Cella o dell Intervallo tramite l API Aspose.Cells per Python via .NET.
keywords: Libreria Excel Python, Python Conserva il Prefisso Apice Singolo del Valore della Cella o dell Intervallo, Python Nascondi il simbolo apostrofo o apice iniziale, Python Mostra il simbolo apostrofo o apice iniziale
---

## **Possibili Scenari di Utilizzo**

Quando si inserisce un valore dentro la cella che ha un apice iniziale o un simbolo di apice singolo, Microsoft Excel lo nasconde, ma quando si seleziona la cella, visualizza il prefisso apice in un formula bar come mostrato nella seguente schermata.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Anche Aspose.Cells per Python via .NET nasconde il prefisso apice o l'apice singolo come Microsoft Excel ma imposta il [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) come **vero** per quella cella. Se si imposta uno stile vuoto della cella, allora [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) diventa di nuovo **falso**. Per risolvere questo problema, Aspose.Cells per Python via .NET fornisce la proprietà [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix), quando è impostata a **falso**, quindi [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) non viene affatto aggiornato e il suo vecchio valore è preservato. Significa che se il vecchio valore della proprietà [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) era **vero**, rimarrà **vero** e se il vecchio valore era **falso**, rimarrà **falso**.

## **Conserva il prefisso apice singolo del valore della cella o dell'intervallo**

Il seguente codice di esempio spiega l'uso della proprietà [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) come descritto in precedenza. Si prega di leggere i commenti all'interno del codice e di vedere l'output della console del codice sottostante per ulteriore aiuto.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-PreserveSingleQuotePrefixOfCellValueOrRange.py" >}}

## **Output della console**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.quote_prefix is False, it means, do not update the value of Cell.Style.quote_prefix.

Similarly, when StyleFlag.quote_prefix is True, it means, update the value of Cell.Style.quote_prefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
