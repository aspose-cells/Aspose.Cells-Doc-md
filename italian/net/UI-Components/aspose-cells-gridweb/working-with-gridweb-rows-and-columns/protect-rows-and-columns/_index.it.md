---
title: Proteggere righe e colonne
type: docs
weight: 60
url: /it/net/aspose-cells-gridweb/protect-rows-and-columns/
keywords: GridWeb, proteggere
description: Questo articolo introduce come proteggere righe e colonne in GridWeb.
---

{{% alert color="primary" %}} 

Questo argomento discute alcune tecniche per proteggere le celle nelle righe e colonne da qualsiasi tipo di azione eseguita dagli utenti finali. Gli sviluppatori possono implementare questa protezione utilizzando due tecniche: rendendo le celle nelle righe e colonne di sola lettura, o limitando le opzioni del menu contestuale di Aspose.Cells.GridWeb. Entrambe queste tecniche sono discusse di seguito con l'aiuto di esempi.

{{% /alert %}} 
## **Protezione delle celle nelle righe e colonne**
### **Rendere righe e colonne di sola lettura**
Un modo per proteggere righe e colonne in un foglio di lavoro è rendere le celle di sola lettura. Quindi non possono essere cancellate dagli utenti finali.

Per rendere righe e colonne di sola lettura:

1. Aggiungi il controllo Aspose.Cells.GridWeb a un modulo Web.
1. Accedi al GridWorksheet nella raccolta.
1. Imposta le tue celle desiderate nelle righe o colonne di sola lettura.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-MakeRowsColumnsReadOnly.aspx-MakeCellReadOnly.cs" >}}
### **Limitazione delle opzioni del menu contestuale**
Aspose.Cells.GridWeb fornisce un menu contestuale che gli utenti finali possono utilizzare per eseguire operazioni sul controllo. Il menu fornisce molte opzioni per manipolare celle, righe e colonne.

**Opzioni contestuali complete** 

![todo:image_alt_text](protect-rows-and-columns_1.png)

È possibile limitare qualsiasi tipo di operazioni lato client su righe e colonne limitando le opzioni disponibili nel menu contestuale. È possibile farlo impostando le proprietà EnableClientColumnOperations e EnableClientRowOperations del controllo GridWeb su false. È anche possibile impedire agli utenti di congelare righe e colonne impostando la proprietà EnableClientFreeze del controllo GridWeb su false.

**Menu contestuale dopo aver limitato le opzioni di riga e colonna** 

![todo:image_alt_text](protect-rows-and-columns_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-RestrictContextMenu.aspx-RestrictContextMenu.cs" >}}
