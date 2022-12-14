---
title: Aggiungi Cell Convalide dati
type: docs
weight: 90
url: /it/net/add-cell-data-validations/
---
{{% alert color="primary" %}} 

 Aspose.Cells.GridWeb consente di aggiungere**Convalida dei dati** utilizzando il metodo GridWorksheet.Validations.Add(). Usando questo metodo, devi specificare il file**Cell Gamma** Ma se vuoi creare una convalida dei dati in un singolo GridCell, puoi farlo direttamente usando il metodo GridCell.CreateValidation (). Allo stesso modo, puoi rimuovere**Convalida dei dati** da un GridCell utilizzando il metodo GridCell.RemoveValidation().

{{% /alert %}} 
## **Creare la convalida dei dati in una GridCell di GridWeb**
 Il codice di esempio seguente crea a**Convalida dei dati** in una cella B3. Se inserisci un valore che non è compreso tra 20 e 40, verrà visualizzata la cella B3**errore di convalida** nella forma di**Rosso XXXX** come mostrato in questo screenshot.

![cose da fare:immagine_alt_testo](add-cell-data-validations_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddDataValidation.aspx-AddDataValidation.cs" >}}
