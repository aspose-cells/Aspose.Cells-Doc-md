---
title: Blocca riquadri del foglio di lavoro di Excel
linktitle: Blocca riquadri
type: docs
weight: 190
url: /it/python-net/how-to-freeze-panes-of-excel-worksheet
description: In questo articolo imparerai come bloccare i riquadri dei fogli di lavoro di Excel automaticamente usando le API di Aspose.Cells per Python via .NET.
keywords: Libreria Python per Excel, blocco riquadri, blocca finestra in Python.
---

## **Introduzione**

In questo articolo impareremo come bloccare i riquadri. Quando si ha una grande quantità di dati sotto un'intestazione comune, non è possibile vedere l'intestazione scorrendo il foglio di lavoro. E ciascun record contiene molti dati. È possibile bloccare i riquadri in modo da poter vedere quella porzione bloccata anche quando il resto dei dati viene scorruto. È possibile vedere facilmente gli intestazioni nelle righe superiori o nelle prime colonne. Bloccare e sbloccare i riquadri cambia solo la visualizzazione dei dati senza modificare i dati stessi.

## ***Come bloccare i riquadri in Excel**

**![Blocca riquadri in Excel](Freeze-panes.png)**


1. Se si desidera bloccare riquadri, congelare righe e colonne, selezionare prima una cella (come ad esempio B2)
2. Fare clic su Visualizza > Blocca riquadri.
3. Nel menu a discesa, fare clic su Blocca riquadri.
4. Se si scorre verso il basso o verso destra, la prima riga e la colonna sono bloccate.

**![Blocchi congelati](Frozen-Panes.png)**

Come si può vedere, la prima riga e la colonna A sono bloccate, la seconda riga è 32 e la seconda colonna visibile è D. 

I blocchi congelati ti permettono di visualizzare i tuoi dati senza dover tenere traccia delle etichette di riga o colonna.




## **Come bloccare i riquadri con Aspose.Cells per Python Libreria Excel**
 È semplice bloccare i riquadri con Aspose.Cells per Python via .NET. Utilizza il metodo [**Worksheet.freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#str-int-int) per bloccare i riquadri alla cella selezionata.
1. Costruire un libro di lavoro per aprire il file o creare un file vuoto.
2. Blocchi congelati con il metodo Worksheet.FreezePanes().
3. Salvare il file.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Freeze-Pane.py" >}}

File Excel di esempio allegato (Freeze.xlsx).
{{< app/cells/assistant language="python-net" >}}
