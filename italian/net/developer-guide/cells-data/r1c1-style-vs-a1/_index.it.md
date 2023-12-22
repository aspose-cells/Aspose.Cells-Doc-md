---
title: "Excel: stile di riferimento R1C1 rispetto a A1"
type: docs
weight: 30
url: /it/net/r1c1-reference-style-vs-a1/
description: Stile di riferimento R1C1 VS. Stile A1 utilizzando Aspose.Cells for Python via .NET API.
keywords: R1C1 Reference Style VS. A1 style, R1C1 Reference Style, How to switch between R1C1 Reference Style and A1 Reference Style, A1 Reference style.
---
{{% alert color="primary" %}}

In Excel, R1C1 e A1 sono due diversi stili di riferimento utilizzati per identificare le celle in un foglio di lavoro. Si noti che la scelta tra A1 e R1C1 è in gran parte una questione di preferenze personali. La maggior parte degli utenti ha più familiarità con lo stile A1, ma R1C1 può essere utile in determinate situazioni, soprattutto quando si lavora con formule e calcoli.

{{% /alert %}}

##  **Stile di riferimento A1**

Questo è lo stile di riferimento predefinito in Excel. Nello stile A1, le colonne sono identificate da lettere (A, B, C, ..., Z, AA, AB, ..., ZZ, AAA, AAB, ...) e le righe sono identificate da numeri (1, 2, 3, ...).
Ad esempio, la cella nella prima colonna e nella seconda riga viene denominata A2.

##  **Stile di riferimento R1C1**

Nello stile R1C1, sia le righe che le colonne sono identificate da numeri. La lettera "R" rappresenta il numero di riga e la lettera "C" rappresenta il numero di colonna. Ad esempio, R2C1 si riferisce alla cella nella seconda riga e nella prima colonna.

Tutti i numeri tra parentesi quadre si riferiscono alla distanza relativa dalla cella corrente. A differenza di A1 che si riferisce alle colonne seguite dal numero di riga, R1C1 fa il contrario: righe seguite da colonne (a cui occorre un po' di tempo per abituarsi). I numeri positivi si riferiranno alle celle in basso e/o a destra. I numeri negativi si riferiranno alle celle sopra e/o a sinistra.

Ad esempio R[2]C[3] è una cella 2 righe in basso e 3 colonne a destra. R[-1]C[-4] è una cella 1 riga in alto e 4 colonne a sinistra. Se non viene mostrato alcun numero tra parentesi, ti riferisci alla stessa riga o colonna, ovvero R[3]C sarà una cella 3 righe sotto la cella corrente nella stessa colonna.
<br>
<image src="2.png" width="70%" />

##  **Confronto tra lo stile di riferimento R1C1 e lo stile di riferimento A1**
Ecco un rapido confronto:
|**Stile A1**|**Stile R1C1**|
| :- | :- |
|A1|
|B3|
|G10|
|AA25|

##  **Come passare dallo stile di riferimento R1C1 allo stile di riferimento A1**
Puoi passare da uno stile di riferimento all'altro nelle impostazioni di Excel. Per modificare lo stile di riferimento:

1. Vai alla scheda "File".
1. Seleziona "Opzioni" in basso.
1. Nella finestra di dialogo Opzioni di Excel, vai alla categoria "Formule".
1. Nella sezione "Lavorare con le formule", seleziona o deseleziona l'opzione "Stile di riferimento R1C1".
1. Fare clic su "OK" per applicare le modifiche.
<br>
<image src="1.png" width="70%" />

##  **Come utilizzare lo stile di riferimento R1C1 e lo stile di riferimento A1 in Excel**
L'esempio seguente mostra come calcolare la somma di due valori di cella in due stili.
<br>
Stile di riferimento A1:
<br>
<image src="4.png" width="70%" />

Stile di riferimento R1C1:
<br>
<image src="3.png" width="70%" />
