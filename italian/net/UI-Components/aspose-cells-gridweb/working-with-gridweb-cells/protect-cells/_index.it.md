---
title: Proteggi Cells
type: docs
weight: 50
url: /it/net/protect-cells/
---
{{% alert color="primary" %}} 

Questo argomento descrive alcune tecniche per proteggere le cellule. L'utilizzo di queste tecniche consente agli sviluppatori di impedire agli utenti di modificare tutte o un intervallo selezionato di celle in un foglio di lavoro.

{{% /alert %}} 
## **Protezione Cells**
 Aspose.Cells.GridWeb fornisce alcune tecniche diverse per controllare il livello di protezione sulle celle quando il controllo è in[Modalità Modifica](/cells/it/net/enable-different-gridweb-modes/#edit-mode) (la modalità predefinita). Questo protegge le celle dalla modifica da parte degli utenti finali.
### **Rendere tutto Cells in sola lettura**
Per impostare tutte le celle di un foglio di lavoro in sola lettura, chiamare il metodo SetAllCellsReadonly del foglio di lavoro.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsReadOnly.cs" >}}
### **Rendere tutto Cells modificabile**
Per rimuovere la protezione da tutte le celle, chiamare il metodo SetAllCellsEditable del foglio di lavoro. Questo metodo ha l'effetto opposto al metodo SetAllCellsReadonly.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeAllCellsEditable.cs" >}}
### **Rendere selezionato Cells Sola lettura**
Per proteggere solo un intervallo di celle:

1. Per prima cosa rendi modificabili tutte le celle chiamando il metodo SetAllCellsEditable.
1. Specificare l'intervallo di celle da proteggere chiamando il metodo SetReadonlyRange del foglio di lavoro. Questo metodo accetta il numero di righe e colonne per specificare l'intervallo di celle.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsReadOnly.cs" >}}
### **Rendere modificabile Cells selezionato**
Per annullare la protezione di un intervallo di celle:

1. Rendere tutte le celle di sola lettura chiamando il metodo SetAllCellsReadonly.
1. Specificare l'intervallo di celle che devono essere modificabili chiamando il metodo SetEditableRange del foglio di lavoro. Questo metodo accetta il numero di righe e colonne per specificare l'intervallo di celle.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ProtectCells.aspx-MakeSelectedCellsEditable.cs" >}}
