---
title: Impostazione di intestazioni e piè di pagina diversi per pagine diverse
type: docs
weight: 35
url: /it/net/setting-different-headers-and-footers-for-pages-to-Excel/
---
{{% alert color="primary" %}}

MS Excel supporta l'impostazione di intestazioni e piè di pagina diversi per la prima pagina, le pagine dispari e le pagine pari da Excel 2007.
Aspose.Cells supporta la stessa funzione.

{{% /alert %}}

## **Impostazione di intestazioni e piè di pagina diversi in MS Excel**

**![Impostazione di intestazioni e piè di pagina diversi](difpage.png)**

1.  Clic**layout di pagina > Stampa titoli > Intestazione/Piè di pagina**.
1.  Dai un'occhiata**Diverse pagine pari e dispari** o**Pagina di abete diversa**.
1. Inserisci intestazioni e piè di pagina diversi.

## **Impostazione di intestazioni e piè di pagina diversi con Aspose.Cells**

Aspose.Cells si comporta come Excel.
1.  Imposta i flag[PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/ishfdiffoddeven/) e[PageSetup.IsHFDiffFirst](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/IsHFDiffFirst/) 
1. Inserisci intestazioni e piè di pagina diversi.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DiffHeaderFooter.cs" >}}
