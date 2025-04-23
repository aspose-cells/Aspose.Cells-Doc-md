---
title: Impostazione di diversi intestazioni e piè di pagina per pagine diverse
type: docs
weight: 35
url: /it/net/setting-different-headers-and-footers-for-pages-to-Excel/
description: Questo articolo fornisce un codice di esempio che mostra come impostare in modo programmato varie intestazioni e piè di pagina delle impostazioni della pagina del foglio di lavoro di Excel utilizzando la libreria C# e l API .NET. È possibile impostare le intestazioni e i piè di pagina per la prima pagina, le pagine dispari e pari.
keywords: imposta intestazione piè di pagina excel prima pagina c#, imposta intestazione piè di pagina excel pagine dispari c#, imposta intestazione piè di pagina excel pagine pari c#
---

{{% alert color="primary" %}}

MS Excel supporta l'impostazione di intestazioni e piè di pagina diversi per la prima pagina, le pagine dispari e pari dal 2007.
Aspose.Cells supporta la stessa funzionalità.

{{% /alert %}}

## **Impostazione di Intestazioni e piè di pagina diversi in MS Excel**

**![Impostazione di Intestazioni e piè di pagina diversi](difpage.png)**

1. Fare clic su **Layout di pagina > Titoli di stampa > Intestazione/piè di pagina**.
1. Seleziona **Pagine pari e dispari diverse** o **Prima pagina diversa**.
1. Inserisci intestazioni e piè di pagina diversi.

## **Impostazione di Intestazioni e piè di pagina diversi con Aspose.Cells**

Aspose.Cells si comporta allo stesso modo di Excel.
1. Imposta i flag [PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/ishfdiffoddeven/) e [PageSetup.IsHFDiffFirst](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/IsHFDiffFirst/) 
1. Inserisci intestazioni e piè di pagina diversi.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DiffHeaderFooter.cs" >}}
{{< app/cells/assistant language="csharp" >}}
