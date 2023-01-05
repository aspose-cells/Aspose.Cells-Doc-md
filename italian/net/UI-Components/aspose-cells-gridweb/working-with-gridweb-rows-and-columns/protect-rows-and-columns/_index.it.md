---
title: Proteggi righe e colonne
type: docs
weight: 60
url: /it/net/protect-rows-and-columns/
---
{{% alert color="primary" %}} 

In questo argomento vengono illustrate alcune tecniche per proteggere le celle in righe e colonne da qualsiasi tipo di azione eseguita dagli utenti finali. Gli sviluppatori possono implementare questa protezione utilizzando due tecniche: rendendo le celle in righe e colonne di sola lettura o limitando le opzioni del menu contestuale di Aspose.Cells.GridWeb. Entrambe queste tecniche sono discusse di seguito con l'aiuto di esempi.

{{% /alert %}} 
## **Protezione Cells in righe e colonne**
### **Rendere righe e colonne di sola lettura**
Un modo per proteggere righe e colonne in un foglio di lavoro consiste nel rendere le celle di sola lettura. Quindi non possono essere eliminati dagli utenti finali.

Per rendere righe e colonne di sola lettura:

1. Aggiungere il controllo Aspose.Cells.GridWeb a un Web Form.
1. Accedi a GridWorksheet nella raccolta.
1. Imposta le celle desiderate in righe o colonne in sola lettura.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-MakeRowsColumnsReadOnly.aspx-MakeCellReadOnly.cs" >}}
### **Limitazione delle opzioni del menu contestuale**
Aspose.Cells.GridWeb fornisce un menu contestuale che gli utenti finali possono utilizzare per eseguire operazioni sul controllo. Il menu offre molte opzioni per manipolare celle, righe e colonne.

**Opzioni contestuali complete** 

![cose da fare:immagine_alt_testo](protect-rows-and-columns_1.png)

È possibile limitare qualsiasi tipo di operazione lato client su righe e colonne restringendo le opzioni disponibili nel menu contestuale. Può essere eseguito impostando le proprietà EnableClientColumnOperations e EnableClientRowOperations del controllo GridWeb su false. È anche possibile impedire agli utenti di bloccare righe e colonne impostando la proprietà EnableClientFreeze del controllo GridWeb su false.

**Menu contestuale dopo aver limitato le opzioni di riga e colonna** 

![cose da fare:immagine_alt_testo](protect-rows-and-columns_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-RestrictContextMenu.aspx-RestrictContextMenu.cs" >}}
