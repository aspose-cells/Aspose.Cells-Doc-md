---
title: Proteggi le celle
type: docs
weight: 50
url: /it/net/aspose-cells-gridweb/protect-cells/
keywords: GridWeb, proteggi, di sola lettura, modificabile
description: Questo articolo presenta come proteggere le celle in GridWeb.
---

{{% alert color="primary" %}} 

Questo argomento descrive alcune tecniche per proteggere le celle. Utilizzando queste tecniche, i programmatori possono limitare agli utenti la modifica di tutte o di un'area selezionata di celle in un foglio di lavoro.

{{% /alert %}} 
## **Protezione delle celle**
Aspose.Cells.GridWeb fornisce alcune tecniche diverse per controllare il livello di protezione sulle celle quando il controllo è in [modalità di modifica](/cells/it/net/aspose-cells-gridweb/enable-different-gridweb-modes/#edit-mode) (modalità predefinita). Questo protegge le celle dalla modifica da parte degli utenti finali.
### **Rendere tutte le celle di sola lettura**
Per impostare tutte le celle in un foglio di lavoro come di sola lettura, chiamare il metodo SetAllCellsReadonly del foglio di lavoro.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsReadOnly.cs" >}}
### **Rendere tutte le celle modificabili**
Per rimuovere la protezione da tutte le celle, chiamare il metodo SetAllCellsEditable del foglio di lavoro. Questo metodo ha l'effetto opposto al metodo SetAllCellsReadonly.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsEditable.cs" >}}
### **Rendere selezionate le celle di sola lettura**
Per proteggere solo un'area di celle:

1. Prima rendere tutte le celle modificabili chiamando il metodo SetAllCellsEditable.
2. Specificare l'area di celle da proteggere chiamando il metodo SetReadonlyRange del foglio di lavoro. Questo metodo richiede il numero di righe e colonne per specificare l'area delle celle.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsReadOnly.cs" >}}
### **Rendere selezionate le celle modificabili**
Per rimuovere la protezione da un'area di celle:

1. Rendere tutte le celle di sola lettura chiamando il metodo SetAllCellsReadonly.
2. Specificare l'area di celle da rendere modificabili chiamando il metodo SetEditableRange del foglio di lavoro. Questo metodo richiede il numero di righe e colonne per specificare l'area delle celle.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsEditable.cs" >}}
