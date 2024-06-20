---
title: Aggiungi Formule Cellula
type: docs
weight: 30
url: /it/net/aspose-cells-gridweb/add-cell-formula/
keywords: GridWeb, formula
description: Questo articolo introduce come aggiungere una formula in una cella in GridWeb.
---

{{% alert color="primary" %}} 

La funzionalità più preziosa offerta da Aspose.Cells.GridWeb è il supporto per formule o funzioni. Aspose.Cells.GridWeb ha il suo motore di formule che calcola le formule nei fogli di lavoro. Aspose.Cells.GridWeb supporta sia funzioni o formule integrate che definite dall'utente. Questo argomento discute l'aggiunta di formule alle celle utilizzando l'API Aspose.Cells.GridWeb in dettaglio.

{{% /alert %}} 
## **Aggiunta Formule alle Celle**
### **Come aggiungere e calcolare una formula?**
È possibile aggiungere, accedere e modificare formule nelle celle utilizzando la proprietà Formula di una cella. Aspose.Cells.GridWeb supporta formule definite dall'utente che vanno da semplici a complesse. Tuttavia, un gran numero di funzioni o formule integrate (simili a Microsoft Excel) sono anche fornite con Aspose.Cells.GridWeb. Per visualizzare l'elenco completo delle funzioni integrate, consulta questa [lista di funzioni supportate.](/cells/it/net/aspose-cells-gridweb/list-of-supported-functions/)

{{% alert color="primary" %}} 

La sintassi della formula dovrebbe essere compatibile con la sintassi di Microsoft Excel. Ad esempio, tutte le formule devono iniziare con un segno uguale (=).

Per aggiungere una formula dinamicamente, Aspose.Cells.GridWeb la riconoscerà come formula anche se non si utilizza il segno **=**, ma se gli utenti finali lavorano nell'interfaccia grafica, devono utilizzare il segno "=".

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-AddFormulas.cs" >}}



**Formula aggiunta alla cella B3 ma non calcolata da GridWeb** 

![todo:image_alt_text](add-cell-formulas_1.png)

Nella schermata precedente, puoi vedere che è stata aggiunta una formula a B3 ma non è stata ancora calcolata. Per calcolare tutte le formule, chiamare il metodo CalculateFormula della classe GridWorksheetCollection del controllo GridWeb dopo aver aggiunto le formule ai fogli di lavoro come mostrato di seguito.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-CalculateFormulas.cs" >}}

{{% alert color="primary" %}} 

Gli utenti possono anche calcolare le formule cliccando su **Invia**.

**Cliccando sul pulsante Invia di GridWeb** 

![todo:image_alt_text](add-cell-formulas_2.png)

**IMPORTANTE**: Se un utente clicca sui pulsanti **Salva** o **Annulla**, o sulle schede dei fogli, tutte le formule vengono calcolate automaticamente da GridWeb.

**Risultato della formula dopo il calcolo** 

![todo:image_alt_text](add-cell-formulas_3.png)

{{% /alert %}} 
### **Riferimento a celle da altri fogli di lavoro**
Utilizzando Aspose.Cells.GridWeb, è possibile fare riferimento ai valori memorizzati in fogli di lavoro diversi nelle loro formule, creando formule complesse.

La sintassi per fare riferimento a un valore di cella da un foglio di lavoro diverso è NomeFoglio!NomeCella.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-AddComplexFormulas.cs" >}}
