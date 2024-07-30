---
title: Congela la prima colonna(o) del foglio di lavoro di Excel
linktitle: Congelare le colonne
type: docs
weight: 190
url: /it/python-net/how-to-freeze-columns-of-excel-worksheet
description: In questo articolo, imparerai come bloccare le colonne sinistre di Fogli di calcolo di Excel in modo programmatico utilizzando le API Aspose.Cells per Python via .NET.
keywords: Libreria Excel Python, Congelare colonne a sinistra in Python, Congelare prime colonne in Python, Bloccare le colonne in Python.
---

## **Introduzione**

In questo articolo, impareremo come bloccare (freezare) colonne a sinistra. Quando hai una grande quantità di dati in una riga, e non riesci a vedere le colonne a sinistra quando scorri orizzontalmente, puoi bloccare e fissare la prima colonna in modo da poter vedere quella parte fissa anche quando si scorrono il resto dei dati. In questo modo, puoi vedere facilmente le intestazioni nelle colonne a sinistra.


## **Come Congelare Colonne In Excel**

**![Congelare la/e colonna/e di sinistra in Excel](freeze-columns.png)**


1. Se vuoi congelare la/e colonna/e di sinistra, seleziona prima la colonna sotto la colonna che deve essere congelata
2. Fare clic su Visualizza > Blocca riquadri.
3. Nel menu a discesa, fare clic su Congela la prima colonna.
4. Se si scorre verso il basso, la prima colonna è sempre nella vista sinistra.

**![Colonna congelata](frozen-columns.png)**

Come si può vedere, la prima colonna è congelata, è sempre bloccata in alto nella vista quando si scorre orizzontalmente.

Le colonne fisse ti consentono di visualizzare i tuoi dati lunghi senza tenere traccia della prima colonna.




## **Come Congelare Colonne con Aspose.Cells per la Libreria Excel Python**
È semplice congelare la prima o più colonne con Aspose.Cells per Python via .NET. Utilizza il metodo [**Worksheet.freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#str-int-int) per congelare la/e colonna/e selezionata/e.
1. Costruire un libro di lavoro per aprire il file o creare un file vuoto.
2. Congelare la prima colonna con il metodo Worksheet.FreezePanes().
3. Salvare il file.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Freeze-Column.py" >}}

File Excel di esempio allegato (Freeze.xlsx).
