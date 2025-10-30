---
title: Come inserire il simbolo di spunta
type: docs
weight: 10
url: /it/net/how-to-insert-tick-symbol-to-excel/
description: Questo articolo introdurrà come inserire il simbolo di spunta API Aspose.Cells for .NET.
keywords: Copiare e incollare il simbolo di spunta, usare il menu Simbolo o Inserisci, inserire un codice Alt, usare AutoCorrezione o scorciatoie, usare il pannello emoji/simboli, aggiungere un tick in una casella / casella di scrutinio
---

## **Possibili Scenari di Utilizzo**
 Inserire un simbolo di spunta (✓) può servire a vari scopi a seconda del contesto. Ecco alcune ragioni comuni per cui qualcuno potrebbe inserire un simbolo di spunta:

1. **Indicazione di Completamento o Successo**: È comunemente usato per segnare un'attività come completata o confermare che qualcosa è stato fatto con successo. Ad esempio, in una lista di cose da fare, puoi usare una spunta per mostrare che un compito è stato portato a termine.

2. **Liste di Controllo e Sondaggi**: In sondaggi, moduli o liste di controllo, un simbolo di spunta indica le opzioni selezionate o mostra che un elemento soddisfa i criteri richiesti.

3. **Approvazione o Validazione**: Un simbolo di spunta può indicare approvazione o validazione di un'azione, decisione o documento. È spesso usato in un contesto formale o semi-formale.

4. **Estetica del Design**: In alcuni casi, il simbolo di spunta viene semplicemente usato per il suo aspetto visivo o come parte di un elemento di design, come nei loghi, infografiche o presentazioni.

5. **Risposta Positiva o Corretta**: Può essere usato nei materiali educativi per evidenziare risposte corrette o l'esito positivo di qualcosa.

6. **Indicazione di Accordo o Consenso**: Un simbolo di spunta può rappresentare l'accordo, il consenso o il riconoscimento di una dichiarazione o condizione.


## **Come Inserire il Simbolo di Spunta in Excel**
Ecco una guida chiara su come inserire un simbolo di spunta (✓ o ✔) in Excel, utilizzando diversi metodi:

### Usando il menu dei simboli

1. Clicca sulla cella dove vuoi inserire la spunta.
2. Vai alla scheda Inserisci sulla barra multifunzione.
3. Clicca su Simbolo (a destra).
4. Nella finestra di dialogo Simbolo: Scegli il carattere (Wingdings o Segoe UI Symbol), Cerca (✔ (Codice carattere 252) o ✓ (Codice carattere 2713))
5. Clicca Inserisci, poi Chiudi.

### Usando scorciatoie da tastiera
1. Codice Alt (solo Windows): Tieni premuto Alt e digita il codice usando il tastierino numerico: Alt + 0252 (✔) — Font Wingdings, Alt + 10003 (✓) — Segoe UI Symbol
2. Dopo aver digitato, rilascia Alt per inserire il simbolo.

### Copia e Incolla
Puoi copiare un simbolo di spunta e incollarlo in qualsiasi cella di Excel: ✓ (U+2713) e ✔ (U+2714). Basta copiarlo da qui e incollarlo direttamente in una cella.

### Utilizzo della formattazione condizionale con una formula
Puoi creare segni di spunta automatici con formule e formattazione condizionale:

1. Inserisci una formula come: =SE(A1="yes"; "✓"; "")
2. Personalizza dimensione carattere e allineamento per l'aspetto.

### Inserisci con funzione CHAR (Font Wingdings)
Se usi Wingdings: =CHAR(252)  →  ✔, Poi modifica il carattere della cella a Wingdings per visualizzarlo correttamente.

### Inserisci usando le caselle di controllo di Excel (Opzionale)

Per caselle di controllo interattive:
1. Vai alla scheda Sviluppatore (abilitala nelle Opzioni se nascosta).
2. Clicca Inserisci → Controlli modulo → Casella di controllo.
3. Posiziona la casella di controllo nel foglio.

## **Come inserire il simbolo di spunta in Aspose.Cells for .NET**
Per inserire un simbolo di spunta (✓) in una cella usando Aspose.Cells for .NET, puoi usare i seguenti metodi per soddisfare i requisiti.

1. Aggiungi il simbolo di spunta usando Unicode (U+2713).
2. Aggiungi il simbolo di spunta usando il font simbolo (Wingdings 2 o Webdings).
3. Aggiungi il simbolo di spunta usando un'immagine.
4. Aggiungi il simbolo di spunta usando il controllo casella di controllo.
5. Aggiungi il simbolo di spunta usando le formattazioni condizionali.
6. Aggiungi il simbolo di spunta usando una formula.

Ecco un esempio base di come inserire il simbolo di spunta in una cella in Aspose.Cells for .NET:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Shapes-insert-tick-symbol.cs" >}}

## **Risultato dell'Output**

Lo screenshot seguente mostra i simboli di spunta creati da Aspose.Cells for .NET nel file Excel di output.
<br>
<img src="tick_result.png" width=70% />

{{< app/cells/assistant language="csharp" >}}
