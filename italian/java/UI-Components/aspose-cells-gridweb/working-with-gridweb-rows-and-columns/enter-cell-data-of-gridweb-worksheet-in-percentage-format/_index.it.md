---
title: Inserisci Cell Dati del foglio di lavoro GridWeb in formato percentuale
type: docs
weight: 1010
url: /it/java/enter-cell-data-of-gridweb-worksheet-in-percentage-format/
---
##  **Possibili scenari di utilizzo**
GridWeb ora supporta gli utenti a inserire i dati della cella in formato percentuale come 3% e i dati nella cella verranno automaticamente formattati come 3,00%. Tuttavia, dovrai impostare lo stile della cella su Formato percentuale, ovvero GridTableItemStyle.NumberType a 9 o 10. Il numero 9 formatterà 3% come 3%, ma il numero 10 formatterà 3% come 3,00%.

{{% alert color="primary" %}} 

Se non hai impostato lo stile della cella su Formato percentuale, i dati di input 3% verranno visualizzati come 0,03.

{{% /alert %}} 
##  **Inserisci Cell Dati del foglio di lavoro GridWeb in formato percentuale**
Il codice di esempio seguente imposta la cella A1 GridTableItemStyle.NumberType come 10, pertanto i dati di input 3% verranno formattati automaticamente come 3,00% come mostrato nello screenshot.

![cose da fare:immagine_alt_testo](enter-cell-data-of-gridweb-worksheet-in-percentage-format_1.png)
##  **Codice d'esempio**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}






