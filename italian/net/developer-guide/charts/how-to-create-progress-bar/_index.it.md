---
title: Come creare una barra di avanzamento
description: Impara come creare una barra di avanzamento usando Aspose.Cells for .NET. 
keywords: Aspose.Cells for .NET, Barra di avanzamento, crea una barra di avanzamento, aggiungi una barra di avanzamento, inserisci una barra di avanzamento.
type: docs
weight: 73
url: /it/net/how-to-create-a-progress-bar/
---

## **Possibili Scenari di Utilizzo**
Il motivo principale per creare una barra di avanzamento in Excel è trasformare numeri grezzi in una metrica visiva immediatamente comprensibile, rendendo i dati complessi semplici da afferrare al volo.

1. Maggiore chiarezza visiva e intuizione immediata: Una tabella con numeri come "75%", "8/10" o "15000/20000" richiede uno sforzo cognitivo per essere interpretata. Una barra di avanzamento permette a chiunque, da un dirigente senior a un membro del team, di capire lo stato, le prestazioni o il livello di completamento immediatamente senza leggere e processare i numeri.

2. Identificazione rapida dello stato e delle tendenze: Il nostro cervello è programmato per elaborare informazioni visive come lunghezza e colore più velocemente rispetto al testo. Puoi vedere rapidamente: Cosa è in corsa? (barre lunghe e verdi), Cosa è in ritardo? (barre corte e rosse) e Cosa è quasi completo? (barre quasi piene). Questo consente decisioni più rapide e priorità.

3. Miglioramento di cruscotti e report: Le barre di avanzamento sono fondamentali per cruscotti efficaci. Rendono i report più coinvolgenti, professionali e più facili da presentare. Un cruscotto con barre di avanzamento per gli indicatori chiave di prestazione (KPI) è molto più efficace di un foglio pieno di numeri.

4. Motivazione e monitoraggio delle prestazioni: Per i team di vendita, i tracciatori di progetto o gli obiettivi personali, vedere una rappresentazione visiva dei progressi può essere molto motivante. Fornisce un senso di realizzazione chiaro e soddisfacente man mano che la barra si riempie.

5. Comunicazione efficiente: Durante riunioni o presentazioni, una barra di avanzamento trasmette il messaggio molto più efficacemente che dire "Siamo al 72,5% del nostro obiettivo trimestrale." La parte visiva parla da sola, risparmiando tempo e prevenendo fraintendimenti.


## **Come creare una barra di progresso in Excel**

Creare una barra di progresso in Excel è un ottimo modo per visualizzare il completamento delle attività, il progresso del progetto o le tendenze dei dati. Ecco una guida su come crearne una utilizzando diversi metodi, insieme a qualche suggerimento per la personalizzazione.

### **Utilizzo della formattazione condizionale (Barre dei dati)**
1. Prepara i tuoi dati: Avere almeno una colonna di valori rappresentanti il progresso, idealmente in percentuale (ad esempio, 0,5 per il 50%). Puoi calcolarlo usando una formula come =Valore_Attuale/Valore_Target.
2. Seleziona le celle: Evidenzia le celle contenenti i tuoi valori percentuali.
3. Applica le Barre dei dati: Vai sulla scheda Home > Formattazione condizionale > Barre dei dati. Scegli tra Riempimento sfumato o Riempimento solido.
4. Personalizza (Opzionale): Per un maggiore controllo, vai su Formattazione condizionale > Gestisci regole > Modifica regola.
5. Imposta i tipi Minimo e Massimo su Numero, con valori 0 e 1 rispettivamente, per garantire una visualizzazione accurata dal 0% al 100%.
6. Regola i colori e lo stile del bordo qui. Per visualizzare sia il numero che la barra, modifica la regola e assicurati che "Mostra solo barra" sia deselezionato.

### **Utilizzo della funzione REPT (barra basata su testo)**
1. Inserisci la formula: In una cella, usa una formula come =REPT("█", B2*10) & REPT("░", 10 - B2*10), dove B2 contiene la percentuale di progresso. Questo esempio crea una barra di 10 caratteri: quadrati pieni (█) per il completamento e quadrati leggeri (░) per il resto.
2. Regola e formatta: Modifica il moltiplicatore (ad esempio, *20 per una barra di 20 caratteri) in base alla lunghezza desiderata. Usa un font a larghezza fissa come Courier New per un allineamento corretto.

### **Utilizzo di un grafico (per dashboard)**
1. Struttura i dati: Crea una tabella per calcolare i valori:
|**Numero**|**A**|**B**|
| :- | :- | :- |
|1|Progresso|Rimanente|
|2|=Valore_Attuale/Valore_Target|=1-A2|
<br>
2. Inserisci il grafico: Seleziona i dati > scheda Inserisci > Grafici > Grafico a barre impilate 2-D.
3. Formatizza il grafico: Rimuovi il titolo del grafico, la legenda e le linee della griglia per un aspetto pulito. Fai clic con il tasto destro sulla serie di dati "Rimanente" > Formatta serie dati > Riempimento > Nessun riempimento. Fai clic con il tasto destro sulla serie di "Progresso" > Formatta serie dati > Regola la sovrapposizione delle serie al 100% e la larghezza dello spazio tra le colonne a 0%. Formatizza l'asse orizzontale: imposta Limiti > Minimo a 0 e Massimo a 1.

## **Come creare una barra di progresso in Aspose.Cells**

### **Utilizza la funzione REPT (Barra basata su testo) per creare una barra di progresso**
Si prega di vedere il seguente esempio di codice. Crea un nuovo foglio di lavoro e aggiunge alcuni dati di esempio. Successivamente, aggiunge la funzione REPT (Barra basata su testo) in base ai dati iniziali. Infine, salva il foglio di lavoro in un file xlsx. La schermata seguente mostra la formattazione condizionale (Barre di dati) creata da Aspose.Cells nel file Excel di output.
<br>
<img src="formula.png" width=70% />

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Progress-Bar-Using-Formula.cs" >}}

### **Utilizza la formattazione condizionale (Barre di dati) per creare una barra di progresso**
Si prega di vedere il seguente esempio di codice. Crea un nuovo foglio di lavoro e aggiunge alcuni dati di esempio. Successivamente, applica una formattazione condizionale (Barre di dati) in base ai dati iniziali e imposta le proprietà pertinenti. Infine, salva il foglio di lavoro in un file xlsx. La schermata seguente mostra le barre di dati create da Aspose.Cells nel file Excel di output.
<br>
<img src="databar.png" width=70% />

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Progress-Bar-Using-ConditionalFormats.cs" >}}


### **Utilizza il grafico a barre impilate (BarStacked) per creare una barra di progresso**
Si prega di vedere il seguente esempio di codice. Carica il [file Excel di esempio](sample.xlsx) che contiene alcuni dati di esempio. Successivamente, crea un grafico a barre impilate basato sui dati iniziali e imposta le proprietà pertinenti. Infine, salva il foglio di lavoro nel formato XLSX di output. La schermata seguente mostra la barra di progresso creata da Aspose.Cells nel file Excel di output.

<br>
<img src="barchart.png" width=70% />

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Progress-Bar-Use-BarStacked-Chart.cs" >}}
