---
title: Impostazione di diversi intestazioni e piè di pagina per pagine diverse
type: docs
weight: 35
url: /it/python-net/setting-different-headers-and-footers-for-pages-to-Excel/
description: Questo articolo fornisce un codice di esempio che mostra come impostare in modo programmato vari intestazioni e piè di pagina delle impostazioni di Impostazione Pagina del foglio di Excel utilizzando l API Aspose.Cells per Python. È possibile impostare le intestazioni e i piè di pagina per la prima pagina, pagine dispari e pagine pari.
keywords: Libreria Python Excel, Imposta intestazioni e piè di pagina excel prima pagina, imposta intestazioni e piè di pagina excel pagine dispari in Python, imposta intestazioni e piè di pagina excel pagine pari in Python.
---

{{% alert color="primary" %}}

MS Excel supporta l'impostazione di intestazioni e piè di pagina diversi per la prima pagina, le pagine dispari e pari dal 2007.
Aspose.Cells per Python via .NET supporta la stessa funzionalità.

{{% /alert %}}

## **Come impostare intestazioni e piè di pagina diversi in MS Excel**

**![Impostazione di Intestazioni e piè di pagina diversi](difpage.png)**

1. Fare clic su **Layout di pagina > Titoli di stampa > Intestazione/piè di pagina**.
1. Seleziona **Pagine pari e dispari diverse** o **Prima pagina diversa**.
1. Inserisci intestazioni e piè di pagina diversi.

## **Come impostare intestazioni e piè di pagina diversi con la libreria Excel Aspose.Cells per Python**

Aspose.Cells per Python via .NET si comporta allo stesso modo di Excel.
1. Imposta i flag [PageSetup.is_hf_diff_odd_even](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_hf_diff_odd_even/) e [PageSetup.is_hf_diff_first](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_hf_diff_first/) 
1. Inserisci intestazioni e piè di pagina diversi.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-DiffHeaderFooter.py" >}}
