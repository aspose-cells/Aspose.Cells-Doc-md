---
title: Blocca riquadri del foglio di lavoro di Excel
linktitle: Blocca riquadri
type: docs
weight: 190
url: /it/net/how-to-freeze-panes-of-excel-worksheet
description: In questo articolo imparerai come bloccare riquadri dei fogli di lavoro di Excel in modo programmato utilizzando la libreria C# con API .NET.
keywords: Blocca riquadri, Blocca finestra.
---

## **Introduzione**

In questo articolo impareremo come bloccare i riquadri. Quando si ha una grande quantità di dati sotto un'intestazione comune, non è possibile vedere l'intestazione scorrendo il foglio di lavoro. E ciascun record contiene molti dati. È possibile bloccare i riquadri in modo da poter vedere quella porzione bloccata anche quando il resto dei dati viene scorruto. È possibile vedere facilmente gli intestazioni nelle righe superiori o nelle prime colonne. Bloccare e sbloccare i riquadri cambia solo la visualizzazione dei dati senza modificare i dati stessi.

## **In Excel**

**![Blocca riquadri in Excel](Freeze-panes.png)**


1. Se si desidera bloccare riquadri, congelare righe e colonne, selezionare prima una cella (come ad esempio B2)
2. Fare clic su Visualizza > Blocca riquadri.
3. Nel menu a discesa, fare clic su Blocca riquadri.
4. Se si scorre verso il basso o verso destra, la prima riga e la colonna sono bloccate.

**![Blocchi congelati](Frozen-Panes.png)**

Come si può vedere, la prima riga e la colonna A sono bloccate, la seconda riga è 32 e la seconda colonna visibile è D. 

I blocchi congelati ti permettono di visualizzare i tuoi dati senza dover tenere traccia delle etichette di riga o colonna.




## **Congelare Riquadri con Aspose.Cells per .Net**
È semplice bloccare i riquadri con Aspose.Cells per .Net. Si prega di utilizzare il metodo [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/freezepanes/) per bloccare i riquadri nella cella selezionata.
1. Costruire un libro di lavoro per aprire il file o creare un file vuoto.
2. Blocchi congelati con il metodo Worksheet.FreezePanes().
3. Salvare il file.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Freeze-Pane.cs" >}}

File Excel di esempio allegato (Freeze.xlsx).
