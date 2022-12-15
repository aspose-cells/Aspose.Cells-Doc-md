---
title: Aggiungi Cell Formule
type: docs
weight: 30
url: /it/net/add-cell-formulas/
---
{{% alert color="primary" %}} 

La caratteristica più preziosa offerta da Aspose.Cells.GridWeb è il supporto per formule o funzioni. Aspose.Cells.GridWeb ha il proprio Formula Engine che calcola le formule nei fogli di lavoro. Aspose.Cells.GridWeb supporta funzioni o formule sia integrate che definite dall'utente. Questo argomento illustra in dettaglio l'aggiunta di formule alle celle utilizzando l'API Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Aggiunta di formule a Cells**
### **Come aggiungere e calcolare una formula?**
 È possibile aggiungere, accedere e modificare le formule nelle celle utilizzando la proprietà Formula di una cella. Aspose.Cells.GridWeb supporta formule definite dall'utente che vanno dal semplice al complesso. Tuttavia, con Aspose.Cells.GridWeb viene fornito anche un gran numero di funzioni o formule incorporate (simili a Microsoft Excel). Per vedere l'elenco completo delle funzioni integrate, fare riferimento a questo[elenco delle funzioni supportate.](/cells/it/net/list-of-supported-functions/)

{{% alert color="primary" %}} 

La sintassi della formula deve essere compatibile con la sintassi di Microsoft Excel. Ad esempio, tutte le formule devono iniziare con un segno di uguale (=).

Per aggiungere dinamicamente una formula, Aspose.Cells.GridWeb la riconoscerà come formula anche se non si utilizza un segno **=**, ma se gli utenti finali lavorano nella GUI, deve utilizzare il segno "=".

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-AddFormulas.cs" >}}



**Formula aggiunta alla cella B3 ma non calcolata da GridWeb** 

![cose da fare:immagine_alt_testo](add-cell-formulas_1.png)

Nello screenshot sopra, puoi vedere che una formula è stata aggiunta a B3 ma non è stata ancora calcolata. Per calcolare tutte le formule, chiama il metodo CalculateFormula del controllo GridWeb GridWorksheetCollection dopo aver aggiunto le formule ai fogli di lavoro come mostrato di seguito.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-CalculateFormulas.cs" >}}

{{% alert color="primary" %}} 

 Gli utenti possono anche calcolare le formule facendo clic**Invia**.

**Facendo clic sul pulsante Invia di GridWeb** 

![cose da fare:immagine_alt_testo](add-cell-formulas_2.png)

**IMPORTANTE** : se un utente fa clic su**Salva** o**Annullare** pulsanti o le schede dei fogli, tutte le formule vengono calcolate automaticamente da GridWeb.

**Risultato della formula dopo il calcolo** 

![cose da fare:immagine_alt_testo](add-cell-formulas_3.png)

{{% /alert %}} 
### **Riferimento a Cells da Altri fogli di lavoro**
Utilizzando Aspose.Cells.GridWeb, è possibile fare riferimento a valori memorizzati in diversi fogli di lavoro nelle loro formule, creando formule complesse.

La sintassi per fare riferimento a un valore di cella da un foglio di lavoro diverso è SheetName!CellName.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-AddComplexFormulas.cs" >}}
