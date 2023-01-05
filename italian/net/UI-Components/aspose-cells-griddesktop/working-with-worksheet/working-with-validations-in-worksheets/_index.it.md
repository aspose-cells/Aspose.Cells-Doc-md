---
title: Utilizzo delle convalide nei fogli di lavoro
type: docs
weight: 70
url: /it/net/working-with-validations-in-worksheets/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop supporta anche l'aggiunta di convalide (o regole di convalida) alle celle di un foglio di lavoro. Applicando le regole di convalida alle celle, gli sviluppatori possono limitare agli utenti l'immissione di dati in Grid in un formato specifico. Diverse modalità di convalida sono supportate da Aspose.Cells.GridDesktop. In questo argomento, non discuteremo solo di queste modalità di convalida, ma spiegheremo anche la manipolazione di queste convalide.

{{% /alert %}} 
## **Modalità di convalida**
Esistono tre modalità di convalida supportate da Aspose.Cells.GridDesktop come segue:

- È richiesta la modalità di convalida
- Modalità di convalida delle espressioni regolari
- Modalità di convalida personalizzata
### **È richiesta la modalità di convalida**
 In questa modalità di convalida, gli utenti sono limitati a immettere valori nelle celle specificate. Una volta**È richiesta la convalida** viene applicato su una cella del foglio di lavoro, diventa obbligatorio per un utente inserire il valore in quella cella.
### **Modalità di convalida delle espressioni regolari**
 In questa modalità, le restrizioni vengono applicate alle celle del foglio di lavoro per consentire agli utenti di inviare i dati nelle celle in un formato specifico. Il modello del formato dei dati è fornito sotto forma di a**Espressione regolare**.
### **Modalità di convalida personalizzata**
 Usare**Convalida personalizzata** , È necessario che gli sviluppatori implementino l'interfaccia Aspose.Cells.GridDesktop.ICustomValidation. L'interfaccia fornisce un**Convalidare** metodo. Questo metodo restituisce true se i dati sono validi altrimenti restituisce false.
## **Utilizzo delle convalide in Aspose.Cells.GridDesktop**
### **Aggiunta di convalida**
Per aggiungere qualsiasi tipo di convalida a una cella del foglio di lavoro, procedi nel seguente modo:

-  Aggiungi il controllo Aspose.Cells.GridDesktop al tuo**Modulo**
-  Accedi a qualsiasi desiderato**Foglio di lavoro**
-  Aggiungi una convalida desiderata al file**Convalide** raccolta del**Foglio di lavoro** per specificare quale convalida verrebbe applicata su quale cella.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-AddingValidation.cs" >}}

{{% alert color="primary" %}} 

 Nella figura sopra, abbiamo anche menzionato le regole di convalida davanti alle celle in cui vengono applicate queste regole di convalida. Se viene immesso un valore non valido (che non è valido secondo la regola di convalida definita per quella cella), a**Casella dei messaggi** sembrerebbe notificare all'utente la voce non valida.

{{% /alert %}} 
### **Implementazione di ICustomValidation**
 Nello snippet di codice sopra, abbiamo aggiunto una convalida personalizzata in**A8**cell ma non abbiamo ancora implementato quella convalida personalizzata. Come abbiamo spiegato all'inizio di questo argomento, per applicare la convalida personalizzata, dobbiamo implementare**ICustomValidation** interfaccia. Quindi, proviamo a creare una classe da implementare**ICustomValidation** interfaccia.

Nello snippet di codice riportato di seguito, abbiamo implementato una convalida personalizzata per eseguire i seguenti controlli:

- Controlla se l'indirizzo della cella è accurato in cui viene aggiunta la convalida
- Controlla se il tipo di dati del valore della cella è double
- Controlla se il valore della cella è maggiore di 100



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-ImplementingICustomInterface.cs" >}}
### **Accesso alla convalida**
Una volta aggiunta una convalida a una specifica cella del foglio di lavoro, gli sviluppatori potrebbero richiedere di accedere e modificare gli attributi di una specifica convalida in fase di esecuzione. Quindi, Aspose.Cells.GridDesktop ha reso semplice per gli sviluppatori svolgere questa attività.

Per accedere a una validazione specifica, procedi nel seguente modo:

-  Accedi a un file desiderato**Foglio di lavoro**
-  Accedi a uno specifico**Convalida**nel foglio di lavoro specificando il nome della cella su cui è stata applicata la convalida
-  Modificare**Convalida** attributi, se lo si desidera



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-AccessingValidation.cs" >}}

{{% alert color="primary" %}} 

**Convalide** collection ha due indicizzatori. Un indicizzatore (utilizzato nell'esempio seguente) consente di accedere a un file**Convalida** oggetto prendendo un nome di cella come indice mentre l'altro indicizzatore prende due parametri (ovvero numeri di riga e colonna) per eseguire la stessa attività.

{{% /alert %}} 
### **Rimozione della convalida**
Per rimuovere una convalida specifica dal foglio di lavoro, procedi nel seguente modo:

-  Accedi a un file desiderato**Foglio di lavoro**
-  Rimuovi un file specifico**Convalida** dal**Foglio di lavoro** specificando il nome della cella su cui è stata applicata la validazione



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-RemoveValidation.cs" >}}
