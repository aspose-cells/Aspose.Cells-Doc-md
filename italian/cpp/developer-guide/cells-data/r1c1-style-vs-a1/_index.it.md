---  
title: Excel – Stile di riferimento R1C1 vs. A1 con C++  
linktitle: Excel – Stile di riferimento R1C1 vs. A1  
type: docs  
weight: 30  
url: /it/cpp/r1c1-reference-style-vs-a1/  
description: Stile di riferimento R1C1 VS. stile A1 utilizzando Aspose.Cells con C++.  
keywords: Stile di riferimento R1C1 VS. Stile A1, Stile di riferimento R1C1, Come passare da uno stile di riferimento R1C1 a uno stile di riferimento A1, Stile di riferimento A1.  
---  

## **Introduzione**

In Excel, R1C1 e A1 sono due diversi stili di riferimento utilizzati per identificare le celle in un foglio di lavoro. Si noti che la scelta tra A1 e R1C1 è principalmente una questione di preferenza personale. La maggior parte degli utenti è più familiare con lo stile A1, ma R1C1 può essere utile in determinate situazioni, specialmente quando si lavora con formule e calcoli.

## **Stile di riferimento A1**

Questo è lo stile di riferimento predefinito in Excel. In stile A1, le colonne sono identificate da lettere (A, B, C, ..., Z, AA, AB, ..., ZZ, AAA, AAB, ...), e le righe sono identificate da numeri (1, 2, 3, ...). Per esempio, la cella nella prima colonna e seconda riga si riferisce come A2.

## **Stile di Riferimento R1C1**

In stile R1C1, sia le righe che le colonne sono identificate da numeri. La lettera "R" rappresenta il numero di riga, e la lettera "C" rappresenta il numero di colonna. Ad esempio, R2C1 si riferisce alla cella nella seconda riga e prima colonna.

Qualsiasi numero tra parentesi quadre si riferisce alla distanza relativa dalla cella corrente. A differenza di A1 che si riferisce alle colonne seguite dal numero di riga, R1C1 fa l'opposto: righe seguite dalle colonne (cosa che richiede un po' di pratica). I numeri positivi faranno riferimento alle celle sotto e/o a destra. I numeri negativi faranno riferimento alle celle sopra e/o a sinistra.

Ad esempio, R[2]C[3] è una cella 2 righe sotto e 3 colonne a destra. R[-1]C[-4] è una cella 1 riga sopra e 4 colonne a sinistra. Se non viene mostrato nessun numero tra parentesi, allora ci si riferisce alla stessa riga o colonna, cioè R[3]C sarà una cella 3 righe sotto la cella corrente nella stessa colonna.  
<br>  
<image src="2.png" width="70%" />  

## **Confronto per lo stile di riferimento R1C1 e stile di riferimento A1**  
Ecco un rapido confronto:  
|**Stile A1**|**Stile R1C1**|  
| :- | :- |  
|A1|R1C1  
|B3|R3C2  
|G10|R10C7  
|AA25|R25C27  

## **Come passare da R1C1 Stile di Riferimento a A1 Stile di Riferimento**  
È possibile passare tra questi stili di riferimento nelle impostazioni di Excel. Per cambiare lo stile di riferimento:

1. Vai alla scheda "File".  
1. Seleziona "Opzioni" in basso.  
1. Nella finestra di dialogo Opzioni di Excel, vai alla categoria "Formule".  
1. Sotto la sezione "Lavorare con le formule", seleziona o deseleziona l'opzione "Stile di riferimento R1C1".  
1. Fai clic su "OK" per applicare le modifiche.  
<br>  
<image src="1.png" width="70%" />  

## **Come utilizzare lo Stile di Riferimento R1C1 e lo Stile di Riferimento A1 in Excel**  
L'esempio seguente mostra come calcolare la somma di due valori di cella in due stili.  
<br>  
Stile di Riferimento A1:  
<br>  
<image src="4.png" width="70%" />  

Stile di Riferimento R1C1:  
<br>  
<image src="3.png" width="70%" />  
