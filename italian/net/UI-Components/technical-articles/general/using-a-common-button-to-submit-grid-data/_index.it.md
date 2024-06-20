---
title: Utilizzo di un pulsante comune per inviare dati della griglia
type: docs
weight: 20
url: /it/net/aspose-cells-gridweb/using-a-common-button-to-submit-grid-data/
keywords: GridWeb, invia, pulsante, personalizzato
description: Questo articolo descrive l uso del pulsante di invio in GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb fornisce alcuni pulsanti di comando integrati come **Invia** e **Salva**. Utilizza questi pulsanti per eseguire compiti correlati.

Questo articolo mostra come inviare dati a un server non solo facendo clic sul pulsante di comando integrato **Salva** di GridWeb, ma facendo clic su un comune pulsante ASP.NET (Controllo Web). Lo scopo di questo articolo è mostrare la flessibilità di Aspose.Cells.GridWeb. Inoltre, questo articolo utilizza anche funzioni speciali esposte da Aspose.Cells.GridWeb da utilizzare nello script lato client.

{{% /alert %}} 
## **Invio dati della griglia utilizzando un pulsante ASP.NET**
Aspose.Cells.GridWeb fornisce tre pulsanti integrati (**Invia**, **Salva** e **Annulla**). Dopo la modifica in GridWeb, un utente può fare clic sul pulsante **Invia** o **Salva** nella barra delle schede per consentire a GridWeb di inviare i dati al server. Se l'utente fa clic su una scheda di foglio, il controllo GridWeb esegue la stessa operazione dei pulsanti di comando integrati. Aspose.Cells.GridWeb supporta anche l'aggiunta di questa funzionalità a un comune controllo Button ASP.NET, ma è necessario aggiungere del codice aggiuntivo all'applicazione.
### **1. Creare un'applicazione di prova**
Apri il tuo IDE Visual Studio.NET e crea un nuovo progetto di applicazione Web ASP.NET. Una volta creato l'applicazione, verrà aggiunta una pagina WebForm1.aspx predefinita al tuo progetto. Trascina e rilascia il controllo GridWeb dalla tua casella degli strumenti sulla Web Form. Se non riesci a trovare il controllo GridWeb nella tua casella degli strumenti, consulta questa pagina: [Integra i controlli della griglia Aspose.Cells con Visual Studio.NET](/cells/it/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/) per saperne di più. Dopo aver aggiunto il controllo GridWeb alla tua Web Form, aggiungi anche un controllo web Button dalla casella degli strumenti alla tua Web Form.
### **2. Aggiunta della codifica all'evento Page_Load**
Ora è il momento di aggiungere del codice all'evento Page_Load della Web Form. Puoi fare doppio clic sulla Web Form nella vista di progettazione e l'IDE di VS.NET ti porterà automaticamente all'handle dell'evento Page_Load dove dovrai utilizzare la raccolta di attributi del pulsante per sovrascrivere il suo evento OnClick.

{{% alert color="primary" %}} 

Il controllo pulsante ASP.NET è un controllo lato server. Ogni volta che viene premuto, viene attivato un evento lato server ma se desideri utilizzare questo controllo Button per eseguire del codice lato client (normalmente utilizzando JavaScript) allora devi modificare il suo attributo onclick nell'evento Page_Load. Aspose.Cells.GridWeb fornisce alcune funzioni che possono essere invocate in JavaScript per gestire il controllo GridWeb dal lato client. Nell'esempio sottostante, abbiamo utilizzato le funzioni updateData e validateAll (che sono funzioni del lato client) di GridWeb per aggiornare e convalidare i dati della griglia.

{{% /alert %}} 
#### **Esempio di codice**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-UsingCommonSubmitButton.aspx-UsingCommonSubmitButton.cs" >}}
### **3. Esecuzione dell'applicazione**
Ora puoi compilare ed eseguire la tua applicazione premendo Ctrl+F5 e la pagina verrà aperta in una nuova finestra del browser. Aggiungi alcuni valori a GridWeb e premi il pulsante Invia dati della griglia al server e vedrai che avviene un postback per aggiornare e convalidare i dati di GridWeb.
## **Conclusioni**
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb offre grande flessibilità per lavorare con i controlli GridWeb dal lato server o dal lato client. Gli sviluppatori hanno un ampio numero di opzioni per utilizzare il controllo GridWeb in differenti tipi di scenari per fornire migliori soluzioni ai propri clienti.

{{% /alert %}}
