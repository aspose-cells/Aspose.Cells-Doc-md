---
title: Impostazione delle formule di matrice dinamica
description: Come utilizzare la libreria Aspose.Cells per calcolare le formule in matrice dinamica in Microsoft Excel. Caricando un file Excel esistente o creando un nuovo file Excel, possiamo utilizzare il metodo fornito da Aspose.Cells per calcolare la formula in matrice dinamica e ottenere il risultato. Infine, salviamo il file Excel modificato su disco.
keywords: Dynamic Array Formulas, Dynamic Array Formulas in Excel, Set dynamic array formulas, Calculation of dynamic array formulas, operate dynamic array formulas of Excel.
type: docs
weight: 70
url: /it/net/calculation-of-dynamic-array-formulas/
---
##  **Che cos'è la formula matriciale di Excel**
In Excel, una formula di matrice è un tipo speciale di formula che consente di eseguire calcoli su matrici di dati anziché su singole celle. Le formule di matrice possono essere utilizzate per eseguire calcoli complessi, manipolare dati e risolvere problemi specifici in modo efficiente. Vengono immesse in modo diverso dalle formule normali e spesso richiedono l'uso di Ctrl + Maiusc + Invio.

Ecco alcuni punti chiave sulle formule di matrice in Excel:
1. Sintassi:
<br>
Le formule di matrice sono scritte come formule normali ma implicano operazioni su matrici di valori. Sono racchiuse tra parentesi graffe { } per indicare che sono formule di matrice. Tuttavia, non puoi digitare tu stesso queste parentesi graffe; Excel li aggiunge automaticamente quando inserisci correttamente la formula.
1. Immissione di formule di matrice:
<br>
Per inserire una formula in forma di matrice, digita la formula nella barra della formula. Invece di premere Invio per terminare, premi Ctrl + Maiusc + Invio. Questo dice a Excel che si tratta di una formula di matrice. Se inserita correttamente, Excel visualizza la formula tra parentesi graffe nella barra della formula per indicare che si tratta di una formula in forma di matrice.
1. Casi d'uso:
<br>
Le formule di matrice sono utili per eseguire calcoli su più celle o intervalli contemporaneamente. Possono essere utilizzati per calcoli matematici avanzati, operazioni condizionali, filtraggio dei dati e altro ancora.
1. Benefici:
<br>
Le formule di matrice ti consentono di eseguire calcoli complessi in un'unica formula, il che può migliorare l'efficienza e semplificare i tuoi fogli di lavoro. Possono gestire set di dati di grandi dimensioni ed eseguire calcoli che altrimenti richiederebbero più passaggi intermedi.
1. Limitazioni:
<br>
Le formule di matrice possono essere più difficili da comprendere e risolvere i problemi rispetto alle formule normali. Possono rallentare le prestazioni del foglio di lavoro, soprattutto se utilizzati in modo estensivo o con set di dati di grandi dimensioni.
1. Esempi:
<br>
 Sommando i valori in un intervallo:**{=SOMMA(A1:A5*B1:B5)}**
<br>
 Trovare il valore massimo in un intervallo:**{=MAX(A1:A5+B1:B5)}**
<br>
<image src="1.png" width="70%" />
<br>

Ricorda che le formule di matrice devono essere utilizzate con giudizio ed è importante capire come funzionano prima di implementarle nei tuoi fogli di lavoro. Possono essere potenti strumenti per l'analisi e la manipolazione dei dati in Excel.

##  **Che cos'è la formula di matrice dinamica di Excel**
Le formule di matrice dinamica sono una nuova funzionalità introdotta in Excel 365 ed Excel 2021. Consentono di lavorare con matrici di dati in modo più fluido ed efficiente rispetto alle formule di matrice tradizionali. Le formule in matrice dinamica distribuiscono automaticamente i risultati nelle celle vicine, eliminando la necessità di Ctrl + Maiusc + Invio e consentendo una più semplice manipolazione dei dati.

Punti chiave sulle formule di matrice dinamica in Excel:
1. Versamento automatico:
<br>
Le formule in matrice dinamica distribuiscono automaticamente i risultati nelle celle adiacenti in base alla dimensione dei dati di output. Ciò significa che non è necessario selezionare un intervallo di celle prima di inserire la formula o utilizzare Ctrl + Maiusc + Invio per confermare la formula.
1. Unico-Cell Inserimento:
<br>
Le formule in matrice dinamica vengono immesse in una singola cella ed Excel popola automaticamente le celle vicine con i risultati. Ciò semplifica la gestione e la comprensione delle formule, poiché è necessario inserire la formula solo una volta.
1. Nuove funzioni:
<br>
Le formule di matrice dinamica introducono nuove funzioni in grado di gestire le matrici in modo nativo, come *FILTER**, *SORT**, *UNIQUE**, *SEQUENCE**, *SORTBY** e *RANDARRAY**. Queste funzioni possono restituire più valori o manipolare direttamente gli array, semplificando calcoli complessi.
1. Gestione flessibile della gamma:
<br>
Le formule di matrice dinamica regolano dinamicamente la dimensione dell'intervallo suddiviso in base alla dimensione dei dati di input o al calcolo eseguito. Questa flessibilità consente un utilizzo più efficiente dello spazio del foglio di lavoro e semplifica la creazione delle formule.
1. Prestazione migliorata:
<br>
Le formule di matrice dinamica possono migliorare le prestazioni rispetto alle formule di matrice tradizionali, soprattutto quando si lavora con set di dati di grandi dimensioni o calcoli complessi.
1. Compatibilità:
<br>
Le formule in matrice dinamica sono disponibili in Excel 365 ed Excel 2021. Potrebbero non essere supportate nelle versioni precedenti di Excel.
1. Esempi di formule di matrice dinamica:
<br>
*FILTER**: Restituisce un array di valori che soddisfano i criteri specificati.
<br>
*SORT**: ordina i valori in un intervallo o array.
<br>
*UNIQUE**: restituisce valori univoci da un elenco o intervallo.
<br>
*SEQUENZA**: Genera una sequenza di numeri o date.
<br>
*RANDARRAY**: Genera un array di numeri casuali.
<br>
<image src="2.png" width="70%" />
<br>

Le formule di matrice dinamica offrono potenti funzionalità per la manipolazione e l'analisi dei dati in Excel, semplificando il lavoro con matrici di dati ed esegue calcoli complessi in modo efficiente.

##  **Qual è la differenza tra le formule di matrice e le formule di matrice dinamica in Excel**
In Excel, sia le formule di matrice che le formule di matrice dinamica vengono utilizzate per eseguire calcoli su più valori contemporaneamente, ma presentano alcune differenze in termini di funzionalità e modalità di implementazione.

###  **Funzionalità delle formule di matrice**
1. Le formule di matrice sono formule tradizionali in Excel che possono eseguire calcoli su matrici di dati.
1. Vengono inseriti premendo Ctrl + Maiusc + Invio dopo aver digitato la formula, che indica a Excel che si tratta di una formula di matrice.
1. Le formule di matrice presentano limitazioni in termini di capacità di trasferire i risultati nelle celle adiacenti. In genere restituiscono un 1. singolo risultato, sebbene tale risultato possa essere un array di celle.
1. Sono in circolazione da molto tempo e sono supportati in tutte le versioni di Excel.

###  **Funzionalità delle formule di matrice dinamica**
1. Le formule di matrice dinamica sono una nuova funzionalità introdotta in Excel 365 (abbonamento a Office 365) ed Excel 2021.
1. Versano automaticamente i risultati nelle celle adiacenti in base alla dimensione dei dati di input o al calcolo della formula.
1. Le formule in matrice dinamica non richiedono la pressione di Ctrl + Maiusc + Invio; digiti semplicemente la formula in una cella ed Excel popola automaticamente le celle adiacenti con i risultati.
1. Queste formule hanno la capacità di restituire più risultati (un intervallo di celle) direttamente senza la necessità di una formula di matrice o Ctrl + Maiusc + Invio.
1. Hanno nuove funzioni come *FILTER**, *SORT**, *UNIQUE**, ecc., che possono gestire gli array in modo nativo e restituire risultati in un formato di array dinamico.
In sintesi, le formule di matrice dinamica rappresentano un modo più moderno e conveniente per lavorare con le matrici in Excel, fornendo la distribuzione automatica dei risultati e semplificando il processo di lavoro con le matrici rispetto alle formule di matrice tradizionali. Tuttavia, sono disponibili solo nelle versioni più recenti di Excel che supportano gli array dinamici.

##  **Come impostare e calcolare le formule di matrice dinamica in Excel**
 L'impostazione di formule di matrice dinamica in Excel implica l'utilizzo di funzioni specifiche progettate per funzionare con matrici di dati e consentire ai risultati di riversarsi automaticamente nelle celle vicine.

Ecco una guida passo passo per impostare le formule in matrice dinamica:
1. Seleziona lo Cell:
<br>
Scegli la cella in cui desideri che vengano visualizzati i risultati della formula in matrice dinamica. Le formule in matrice dinamica distribuiscono i risultati in celle adiacenti, quindi assicurati che ci sia spazio sufficiente per l'output distribuito.
1. Inserisci la formula:
<br>
 Digita la formula in matrice dinamica nella barra della formula della cella selezionata. Utilizzare una delle funzioni di matrice dinamica disponibili in Excel 365 ed Excel 2021, ad esempio *FILTRO**, *ORDINAMENTO**, *UNICO**, *SEQUENZA**, *ORDINAMENTO** o *RANDARRAY**.
<br>
Ad esempio, potresti utilizzare la funzione FILTRO per filtrare un elenco di dati in base a criteri specifici: *=FILTRO(A2:C15,(A2:A15=F4)*(C2:C15=G4),"")**.
<br>
<image src="3.png" width="70%" />
<br>
1. Premere Invio:
<br>
Dopo aver digitato la formula, premi semplicemente Invio sulla tastiera. A differenza delle formule matriciali tradizionali, non è necessario premere Ctrl + Maiusc + Invio.
1. Osservare l'intervallo di fuoriuscite:
<br>
Excel distribuisce automaticamente i risultati della formula nelle celle vicine. L'intervallo suddiviso si regola dinamicamente in base alla dimensione dei dati di output o al calcolo eseguito dalla formula. Excel evidenzia l'intervallo rovesciato con un bordo e un'icona con una freccia diagonale per indicare che contiene dati riversati.
1. Interagisci con la gamma rovesciata:
<br>
Puoi interagire con l'intervallo rovesciato proprio come qualsiasi altro intervallo di celle in Excel. Utilizza l'intervallo rovesciato in altre formule, esegui calcoli su di esso, formattalo o fai riferimento ad esso in grafici o tabelle.
1. Aggiorna la formula:
<br>
Se devi modificare la formula in matrice dinamica, modifica semplicemente la formula nella cella originale in cui è stata inserita.
Dopo la modifica, premere nuovamente Invio per confermare le modifiche. Excel aggiornerà automaticamente l'intervallo rovesciato, se necessario.
1. Cancellazione dell'intervallo versato:
<br>
Se desideri cancellare i dati versati, puoi eliminare la formula dalla cella originale. Excel cancellerà anche l'intervallo rovesciato. In alternativa, puoi eliminare direttamente l'intervallo rovesciato selezionandolo e premendo il tasto Elimina.
<br>

Seguendo questi passaggi, è possibile impostare formule di matrice dinamica in Excel per analizzare e manipolare in modo efficiente matrici di dati, consentendo un'analisi dei dati e attività di reporting più semplici.

##  **Come impostare e aggiornare le formule di matrice dinamica utilizzando Aspose.Cells**
 Consulta il seguente codice di esempio che carica il file[file Excel di esempio](dynamicArrayFormula.xlsx) che contiene alcuni dati fittizi. Dopo aver caricato il file, chiama il file[Cell.SetDynamicArrayFormula](https://reference.aspose.com/cells/net/aspose.cells/cell/setdynamicarrayformula/#setdynamicarrayformula) funzione per impostare la formula di matrice dinamica e[Workbook.RefreshDynamicArrayFormulas](https://reference.aspose.com/cells/net/aspose.cells/workbook/refreshdynamicarrayformulas/#refreshdynamicarrayformulas) funzione per aggiornare le formule in matrice dinamica prima di chiamare il calcolo della formula e infine salvare la cartella di lavoro con nome[file Excel di output](out.xlsx). 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Formulas-dynamic-array-formulas.cs" >}}

L'istantanea di output:
<br>
<image src="4.png" width="70%" />