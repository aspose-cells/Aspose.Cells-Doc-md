---
title: Impostazione di intestazioni e piè di pagina diversi per pagine diverse
type: docs
weight: 35
url: /it/net/setting-different-headers-and-footers-for-pages-to-Excel/
description: In questo articolo viene fornito un codice di esempio che mostra come impostare a livello di codice varie intestazioni e piè di pagina delle impostazioni di Imposta pagina del foglio di lavoro di Excel utilizzando la libreria .NET e API. È possibile impostare le intestazioni e i piè di pagina per la prima pagina, le pagine dispari e le pagine pari.
keywords: set excel header footer first page c#, set excel header footer odd pages c#, set excel header footer even pages c#
---
{{% alert color="primary" %}}

MS Excel supporta l'impostazione di intestazioni e piè di pagina diversi per la prima pagina, le pagine dispari e le pagine pari da Excel 2007.
Aspose.Cells supporta la stessa funzione.

{{% /alert %}}

##  **Impostazione di intestazioni e piè di pagina diversi in MS Excel**

**![Impostazione di intestazioni e piè di pagina diversi](difpage.png)**

1. Fare clic su *Layout pagina > Stampa titoli > Intestazione/piè di pagina**.
1.  Controllo**Diverse pagine pari e dispari** o *Pagina di abete diversa**.
1. Inserisci intestazioni e piè di pagina diversi.

##  **Impostazione di intestazioni e piè di pagina diversi con Aspose.Cells**

Aspose.Cells si comporta come Excel.
1.  Imposta i flag[PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/ishfdiffoddeven/) E[PageSetup.IsHFDiffFirst](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/IsHFDiffFirst/) 
1. Inserisci intestazioni e piè di pagina diversi.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DiffHeaderFooter.cs" >}}
