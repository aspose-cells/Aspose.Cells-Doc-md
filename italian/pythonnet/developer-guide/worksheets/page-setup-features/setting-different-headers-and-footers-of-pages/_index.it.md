---
title: Impostazione di diversi intestazioni e piè di pagina per pagine diverse
type: docs
weight: 35
url: /it/python-net/setting-different-headers-and-footers-for-pages-to-Excel/
description: Questo esempio di codice mostra come impostare programmaticamente vari intestazioni e piè di pagina delle impostazioni di pagina del foglio di lavoro Excel usando le API Aspose.Cells per Python. Puoi impostare intestazioni e piè di pagina per la prima pagina, pagine dispari e pagine pair.
keywords: Libreria Python Excel, impostare intestazione piè di pagina del primo foglio, impostare intestazione piè di pagina per pagine dispari in Python, impostare intestazione piè di pagina per pagine pari usando Python.
---

{{% alert color="primary" %}}

MS Excel supporta l'impostazione di intestazioni e piè di pagina diversi per la prima pagina, le pagine dispari e pari dal 2007.
Aspose.Cells per Python via .NET supporta la stessa funzione.

{{% /alert %}}

## **Come impostare intestazioni e piè di pagina diversi in MS Excel**

**![Impostazione di Intestazioni e piè di pagina diversi](difpage.png)**

1. Fare clic su **Layout di pagina > Titoli di stampa > Intestazione/piè di pagina**.
1. Seleziona **Pagine pari e dispari diverse** o **Prima pagina diversa**.
1. Inserisci intestazioni e piè di pagina diversi.

## **Come impostare intestazioni e piè di pagina diversi con Aspose.Cells per Python Excel Library**

Aspose.Cells per Python via .NET si comporta allo stesso modo di Excel.
1. Imposta i flag [PageSetup.is_hf_diff_odd_even](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_hf_diff_odd_even/) e [PageSetup.is_hf_diff_first](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_hf_diff_first/) 
1. Inserisci intestazioni e piè di pagina diversi.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-DiffHeaderFooter.py" >}}
{{< app/cells/assistant language="python-net" >}}
