---
title: Aggiungi Validazione Dati Cellula
type: docs
weight: 90
url: /it/net/aspose-cells-gridweb/add-cell-data-validations/
keywords: GridWeb,validazione,validazione dati,GridValidation
description: Questo articolo introduce come aggiungere la validazione dei dati (GridValidation) in GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb ti consente di aggiungere **Validazione Dati** utilizzando il metodo GridWorksheet.Validations.Add(). Utilizzando questo metodo, devi specificare il **Intervallo Celle**. Ma se vuoi creare una Validazione Dati in una singola GridCell, puoi farlo direttamente utilizzando il metodo GridCell.CreateValidation(). Allo stesso modo, puoi rimuovere la **Validazione Dati** da una GridCell utilizzando il metodo GridCell.RemoveValidation().

{{% /alert %}} 
## **Creare una convalida dei dati in una GridCell di GridWeb**
Il seguente codice di esempio crea una **Convalida dei dati** in una cella B3. Se inserisci un valore che non è compreso tra 20 e 40, la cella B3 mostrerà un **Errore di convalida** sotto forma di **XXXX rosso** come mostrato in questo screenshot.

![todo:image_alt_text](add-cell-data-validations_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddDataValidation.aspx-AddDataValidation.cs" >}}
