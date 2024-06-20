---
title: Lavorare con le Validazioni nei Fogli di Lavoro
type: docs
weight: 70
url: /it/net/aspose-cells-griddesktop/work-with-validations-in-worksheets/
keywords: GridDesktop,validazioni,validazione
description: Questo articolo introduce come lavorare con la validazione in GridDesktop.
---

{{% alert color="primary" %}} 

Anche Aspose.Cells.GridDesktop supporta l'aggiunta di validazioni (o regole di validazione) alle celle di un foglio di lavoro. Applicando delle regole di validazione alle celle, gli sviluppatori possono limitare gli utenti nell'inserire dati nel Grid in un determinato formato. Sono supportati diversi modi di validazione da Aspose.Cells.GridDesktop. In questo argomento, non solo discuteremo su quei modi di validazione ma spiegheremo anche la manipolazione di queste validazioni.

{{% /alert %}} 
## **Modalità di Validazione**
Sono supportate tre modalità di validazione da Aspose.Cells.GridDesktop come segue:

- Modalità di Validazione Is Required
- Modalità di Validazione delle Espressioni Regolari
- Modalità di Validazione Personalizzata
### **Modalità di Validazione Is Required**
In questa modalità di validazione, agli utenti è vietato inserire valori nelle celle specificate. Una volta che la **Validazione Is Required** è applicata a una cella del foglio di calcolo, diventa obbligatorio per un utente inserire un valore in quella cella.
### **Modalità di Validazione delle Espressioni Regolari**
In questa modalità, vengono applicate restrizioni alle celle del foglio di lavoro affinché gli utenti possano inserire dati nelle celle in un formato specifico. Il modello del formato dei dati è fornito sotto forma di **Espressione Regolare**.
### **Modalità di Validazione Personalizzata**
Per utilizzare la **Validazione Personazzata**, i developer devono implementare l'interfaccia Aspose.Cells.GridDesktop.ICustomValidation. L'interfaccia fornisce un metodo **Validate**. Questo metodo restituisce true se i dati sono validi altrimenti restituisce false.
## **Lavorare con le Validazioni in Aspose.Cells.GridDesktop**
### **Aggiunta di Validazione**
Per aggiungere qualsiasi tipo di validazione a una cella del foglio di lavoro, seguire i passaggi seguenti:

- Aggiungi il controllo Aspose.Cells.GridDesktop al tuo **Form**
- Accedere a qualsiasi **Foglio di lavoro** desiderato
- Aggiungi una validazione desiderata alla collezione **Validations** del **Foglio di lavoro** per specificare quale validazione verrà applicata su quale cella.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-AddingValidation.cs" >}}

{{% alert color="primary" %}} 

Nella figura precedente, abbiamo anche menzionato le regole di validazione di fronte alle celle in cui queste regole di validazione vengono applicate. Se viene inserito un valore non valido (che non è valido secondo la regola di validazione definita per quella cella), verrà visualizzata una **MessageBox** per notificare l'utente dell'ingresso non valido.

{{% /alert %}} 
### **Implementazione di ICustomValidation**
Nello snippet di codice precedente, abbiamo aggiunto una validazione personalizzata nella cella **A8** ma non abbiamo ancora implementato tale validazione personalizzata. Come abbiamo spiegato all'inizio di questo argomento, per applicare una validazione personalizzata, dobbiamo implementare l'interfaccia **ICustomValidation**. Quindi, proviamo a creare una classe per implementare l'interfaccia **ICustomValidation**.

Nello snippet di codice sottostante, abbiamo implementato una validazione personalizzata per effettuare i seguenti controlli:

- Verifica se l'indirizzo della cella è accurato in cui è stata aggiunta la validazione
- Controlla se il tipo di dati del valore della cella è doppio
- Controlla se il valore della cella è maggiore di 100



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-ImplementingICustomInterface.cs" >}}
### **Accesso alla Validazione**
Dopo che una validazione è stata aggiunta a una specifica cella del foglio di lavoro, potrebbe essere necessario per i developer accedere e modificare gli attributi di una specifica validazione durante l'esecuzione. Quindi, Aspose.Cells.GridDesktop ha reso semplice per i developer raggiungere questo obiettivo.

Per accedere a una specifica validazione, seguire i passaggi seguenti:

- Accedi a un **Foglio di lavoro** desiderato
- Accedere a una specifica **Validazione** nel foglio di lavoro specificando il nome della cella su cui è stata applicata la validazione
- Modifica gli attributi di **Validazione**, se desiderato



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-AccessingValidation.cs" >}}

{{% alert color="primary" %}} 

La raccolta di **Validazioni** ha due indicizzatori. Un indicizzatore (che viene utilizzato nell'esempio qui sotto) consente di accedere a un oggetto **Validazione** tramite il nome della cella come indice, mentre l'altro indicizzatore richiede due parametri (cioè numeri di riga e colonna) per svolgere la stessa operazione.

{{% /alert %}} 
### **Rimozione della Validazione**
Per rimuovere una specifica validazione dal foglio di lavoro, seguire i seguenti passaggi:

- Accedi a un **Foglio di lavoro** desiderato
- Rimuovi una specifica **Validazione** dal **Foglio di lavoro** specificando il nome della cella su cui è stata applicata la validazione



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-RemoveValidation.cs" >}}
