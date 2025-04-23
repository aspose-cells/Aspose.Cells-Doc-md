---
title: Impostazione di Formule Array Dinamiche
description: Come utilizzare la libreria Aspose.Cells per calcolare formule array dinamiche in Microsoft Excel. Caricando un file Excel esistente o creandone uno nuovo, possiamo utilizzare il metodo fornito da Aspose.Cells per calcolare la formula array dinamica e ottenere il risultato. Infine, salviamo il file Excel modificato su disco.
keywords: Formule Array Dinamiche, Formule Array Dinamiche in Excel, Impostazione di formule array dinamiche, Calcolo di formule array dinamiche, utilizzo di formule array dinamiche di Excel.
type: docs
weight: 70
url: /it/net/calculation-of-dynamic-array-formulas/
---
## **Cos'è la Formula Array di Excel**
In Excel, una formula array è un tipo speciale di formula che ti consente di eseguire calcoli su array di dati anziché su singole celle. Le formule array possono essere utilizzate per eseguire calcoli complessi, manipolare dati e risolvere problemi specifici in modo efficiente. Sono inserite in modo diverso rispetto alle formule regolari e spesso richiedono l'uso di Ctrl + Maiusc + Invio.

Ecco alcuni punti chiave sulle formule array in Excel:
1. Sintassi:
<br>
Le formule array sono scritte come formule regolari ma coinvolgono operazioni su array di valori. Sono racchiuse tra parentesi graffe { } per indicare che sono formule array. Tuttavia, non è necessario digitare queste parentesi graffe manualmente; Excel le aggiunge automaticamente quando si inserisce correttamente la formula.
1. Inserimento di Formule Array:
<br>
Per inserire una formula array, digitare la formula nella barra della formula. anziché premere Invio per finire, premere Ctrl + Maiusc + Invio. Questo dice a Excel che si tratta di una formula array. Quando inserita correttamente, Excel visualizza la formula tra parentesi graffe nella barra della formula per indicare che si tratta di una formula array.
1. Casi d'Uso:
<br>
Le formule array sono utili per eseguire calcoli su più celle o intervalli contemporaneamente. Possono essere utilizzati per calcoli matematici avanzati, operazioni condizionali, filtraggio dati e altro ancora.
1. Vantaggi:
<br>
Le formule array ti permettono di eseguire calcoli complessi in una singola formula, il che può migliorare l'efficienza e semplificare i fogli di lavoro. Possono gestire grandi set di dati ed eseguire calcoli che altrimenti richiederebbero più passaggi intermedi.
1. Limitazioni:
<br>
Le formule array possono essere più difficili da capire e risolvere rispetto alle formule regolari. Possono rallentare le prestazioni del foglio di lavoro, specialmente se utilizzate ampiamente o con grandi set di dati.
1. Esempi:
<br>
Sommare i valori in un intervallo: **{=SUMMA(A1:A5*B1:B5)}**
<br>
Trova il valore massimo in un intervallo: **{=MAX(A1:A5+B1:B5)}**
<br>
<image src="1.png" width="70%" />
<br>

Ricorda che le formule di matrice dovrebbero essere usate con prudenza ed è importante capire come funzionano prima di implementarle nei fogli di calcolo. Possono essere strumenti potenti per l'analisi e la manipolazione dei dati in Excel.

## **Cos'è la Formula di Matrice Dinamica in Excel**
Le formule di matrice dinamica sono una nuova funzionalità introdotta in Excel 365 ed Excel 2021. Ti consentono di lavorare con matrici di dati in modo più semplice ed efficiente rispetto alle formule di matrice tradizionali. Le formule di matrice dinamica spargono automaticamente i risultati nelle celle adiacenti, eliminando la necessità di Ctrl + Maiusc + Invio e consentendo una manipolazione più semplice dei dati.

Punti chiave sulle formule di matrice dinamica in Excel:
1. Spillaggio Automatico:
<br>
Le formule di matrice dinamica spargono automaticamente i risultati nelle celle adiacenti in base alla dimensione dei dati in uscita. Ciò significa che non è necessario selezionare un intervallo di celle prima di inserire la formula o utilizzare Ctrl + Maiusc + Invio per confermare la formula.
1. Inserimento in una singola cella:
<br>
Le formule di matrice dinamica vengono inserite in una singola cella, ed Excel popola automaticamente le celle adiacenti con i risultati. Ciò rende più facile gestire e comprendere le formule, in quanto è necessario inserire la formula una sola volta.
1. Nuove Funzioni:
<br>
Le formule di array dinamico introducono nuove funzioni che possono gestire array in modo nativo, come **FILTRO**, **ORDINA**, **UNICO**, **SEQUENZA**, **ORDINAPER**, e **ARRAYALEATORIO**. Queste funzioni possono restituire valori multipli o manipolare array direttamente, semplificando calcoli complessi.
1. Gestione flessibile dei range:
<br>
Le formule di array dinamico regolano dinamicamente le dimensioni del range ricaduto in base alle dimensioni dei dati di input o ai calcoli eseguiti. Questa flessibilità consente un uso più efficiente dello spazio del foglio di lavoro e semplifica la creazione di formule.
1. Miglioramento delle prestazioni:
<br>
Le formule di array dinamico possono migliorare le prestazioni rispetto alle formule di array tradizionali, specialmente quando si lavora con grandi set di dati o calcoli complessi.
1. Compatibilità:
<br>
Le formule di array dinamico sono disponibili in Excel 365 ed Excel 2021. Potrebbe non essere supportato nelle versioni precedenti di Excel.
1. Esempi di formule di array dinamico:
<br>
**FILTRO**: Restituisce un array di valori che soddisfano i criteri specificati.
<br>
**ORDINA**: Ordina i valori in un intervallo o array.
<br>
**UNICO**: Restituisce valori unici da un elenco o intervallo.
<br>
**SEQUENZA**: Genera una sequenza di numeri o date.
<br>
**ARRAYALEATORIO**: Genera un array di numeri casuali.
<br>
<image src="2.png" width="70%" />
<br>

Le formule di array dinamico offrono capacità potenti per la manipolazione e l'analisi dei dati in Excel, rendendo più semplice lavorare con array di dati e svolgere calcoli complessi in modo efficiente.

## **Qual è la differenza tra formule di array e formule di array dinamico in Excel**
In Excel, sia le formule di array che le formule di array dinamico vengono utilizzate per eseguire calcoli su valori multipli contemporaneamente, ma presentano alcune differenze in termini di funzionalità e modalità di implementazione.

### **Caratteristiche delle formule di array**
1. Le formule di array sono formule tradizionali in Excel che possono eseguire calcoli su array di dati.
1. Vengono inserite premendo Ctrl + Maiusc + Invio dopo aver digitato la formula, che informa Excel che si tratta di una formula di array.
1. Le formule di array presentano limitazioni nella capacità di riversare i risultati nelle celle adiacenti. Tipicamente restituiscono un singolo risultato, anche se quel risultato potrebbe essere un array di celle.
1. Sono stati presenti per molto tempo e sono supportati in tutte le versioni di Excel.

### **Caratteristiche delle formule ad array dinamico**
1. Le formule ad array dinamico sono una nuova funzionalità introdotta in Excel 365 (abbonamento a Office 365) e Excel 2021.
1. Spillano automaticamente i risultati nelle celle adiacenti in base alle dimensioni dei dati di input o al calcolo della formula.
1. Le formule ad array dinamico non richiedono di premere Ctrl + Maiusc + Invio; basta digitare la formula in una cella e Excel popola automaticamente le celle adiacenti con i risultati.
1. Queste formule hanno la capacità di restituire risultati multipli (una serie di celle) direttamente senza la necessità di una formula di matrice o Ctrl + Maiusc + Invio.
1. Hanno nuove funzioni come **FILTRO**, **ORDINA**, **UNICO**, ecc., che possono gestire le matrici in modo nativo e restituire i risultati in un formato di array dinamico.
In sintesi, le formule ad array dinamico sono un modo più moderno e conveniente per lavorare con le matrici in Excel, fornendo uno spill automatico dei risultati e semplificando il processo di lavoro con le matrici rispetto alle formule di matrice tradizionali. Tuttavia, sono disponibili solo nelle versioni più recenti di Excel che supportano gli array dinamici.

## **Come impostare e calcolare le formule ad array dinamico in Excel**
Impostare le formule ad array dinamico in Excel comporta l'uso di funzioni specifiche progettate per lavorare con matrici di dati e consentire ai risultati di spillare automaticamente nelle celle circostanti. 

Ecco una guida passo dopo passo per impostare le formule ad array dinamico:
1. Seleziona la cella:
<br>
Scegli la cella in cui desideri visualizzare i risultati della formula ad array dinamico. Le formule ad array dinamico fanno spillare i risultati nelle celle adiacenti, quindi assicurati che ci sia abbastanza spazio per l'output spillato.
1. Inserisci la formula:
<br>
Digita la formula ad array dinamico nella barra delle formule della cella selezionata. Utilizza una delle funzioni ad array dinamico disponibili in Excel 365 e Excel 2021, come **FILTRO**, **ORDINA**, **UNICO**, **SEQUENZA**, **ORDINAPER**, o **MATR.CASUALE**. 
<br>
Ad esempio, potresti utilizzare la funzione FILTRO per filtrare un elenco di dati in base a criteri specifici: **=FILTRO(A2:C15,(A2:A15=F4)*(C2:C15=G4),"")**.
<br>
<image src="3.png" width="70%" />
<br>
1. Premi Invio:
<br>
Dopo aver digitato la formula, premi semplicemente Invio sulla tastiera. A differenza delle formule di matrice tradizionali, non è necessario premere Ctrl + Maiusc + Invio.
1. Osserva la gamma spillata:
<br>
Excel spillare automaticamente i risultati della formula nelle celle circostanti. La gamma spillata si regola dinamicamente in base alle dimensioni dei dati di output o al calcolo eseguito dalla formula. Excel evidenzia la gamma spillata con un bordo e un'icona a freccia diagonale per indicare che contiene dati spillati.
1. Interagire con l'intervallo spillato:
<br>
Puoi interagire con l'intervallo spillato come con qualsiasi altro intervallo di celle in Excel. Utilizza l'intervallo spillato in altre formule, esegui calcoli su di esso, formattalo o fai riferimento ad esso in grafici o tabelle.
1. Aggiornare la Formula:
<br>
Se devi modificare la formula di array dinamico, modificala semplicemente nella cella originale in cui è stata inserita.
Dopo la modifica, premi nuovamente Invio per confermare le modifiche. Excel aggiornerà automaticamente l'intervallo spillato se necessario.
1. Cancellare l'intervallo spillato:
<br>
Se desideri cancellare i dati spillati, puoi eliminare la formula dalla cella originale. Excel cancellerà anche l'intervallo spillato. In alternativa, puoi eliminare direttamente l'intervallo spillato selezionandolo e premendo il tasto Canc.
<br>

Seguendo questi passaggi, puoi configurare formule di array dinamico in Excel per analizzare e manipolare in modo efficiente array di dati, consentendo un'analisi e una segnalazione più facili dei dati.

## **Come impostare e aggiornare formule di array dinamico utilizzando Aspose.Cells**
Si prega di vedere il seguente codice di esempio che carica il [file Excel di esempio](dynamicArrayFormula.xlsx) che contiene alcuni dati di esempio. Dopo aver caricato il file, chiamare la funzione [Cell.SetDynamicArrayFormula](https://reference.aspose.com/cells/net/aspose.cells/cell/setdynamicarrayformula/#setdynamicarrayformula) per impostare la formula di array dinamico e la funzione [Workbook.RefreshDynamicArrayFormulas](https://reference.aspose.com/cells/net/aspose.cells/workbook/refreshdynamicarrayformulas/#refreshdynamicarrayformulas) per aggiornare le formule di array dinamico prima di chiamare il calcolo delle formule, e infine salvare il workbook come [file Excel di output](out.xlsx). 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Formulas-dynamic-array-formulas.cs" >}}

La snapshot di output:
<br>
<image src="4.png" width="70%" />
{{< app/cells/assistant language="csharp" >}}
