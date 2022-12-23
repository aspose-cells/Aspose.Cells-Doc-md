---
title: Utilizzo di un pulsante comune per inviare i dati della griglia
type: docs
weight: 20
url: /it/net/using-a-common-button-to-submit-grid-data/
---
{{% alert color="primary" %}} 

 Aspose.Cells.GridWeb fornisce alcuni pulsanti di comando integrati come**Invia** e**Salva**. Utilizzare questi pulsanti per eseguire attività correlate.

Questo articolo mostra come inviare dati a un server non solo facendo clic sull'opzione integrata di GridWeb**Salva** pulsante di comando, ma facendo clic su un comune pulsante ASP.NET (controllo Web). Lo scopo di questo articolo è mostrare la flessibilità di Aspose.Cells.GridWeb. Inoltre, questo articolo utilizza anche funzioni speciali esposte da Aspose.Cells.GridWeb da utilizzare nello script lato client.

{{% /alert %}} 
## **Invio dei dati della griglia utilizzando un pulsante ASP.NET**
Aspose.Cells.GridWeb fornisce tre pulsanti integrati (**Invia**, **Salva** e**Annullare** ). Dopo la modifica in GridWeb, un utente può fare clic su**Invia** o**Salva** pulsante nella barra delle schede per consentire a GridWeb di inviare i dati al server. Se l'utente fa clic su una scheda Foglio, il controllo GridWeb esegue la stessa attività dei pulsanti di comando incorporati. Aspose.Cells.GridWeb supporta anche l'aggiunta di questa funzionalità a un comune controllo Button ASP.NET, ma è necessario aggiungere del codice aggiuntivo all'applicazione.
### **1. Creazione di un'applicazione di prova**
Apri il tuo IDE di Visual Studio.NET e crea un nuovo progetto di applicazione Web ASP.NET. Una volta creata l'applicazione, al progetto verrà aggiunta una pagina WebForm1.aspx predefinita. Trascina e rilascia il controllo GridWeb dalla Toolbox al Web Form . Se non riesci a trovare il controllo GridWeb nella tua casella degli strumenti, fai riferimento a questa pagina:[Integra i controlli griglia Aspose.Cells con Visual Studio.NET](/cells/it/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/) per saperne di più. Dopo che il controllo GridWeb è stato aggiunto al tuo Web Form, aggiungi anche un controllo Web Button da Toolbox al tuo Web Form.
### **2. Aggiunta di codice all'evento Page_Load**
Ora è il momento di aggiungere del codice a Page_Carica l'evento del Web Form. Puoi fare doppio clic sul modulo Web in visualizzazione struttura e l'IDE VS.NET ti porterà automaticamente alla pagina_Carica il gestore dell'evento dove dovresti usare la raccolta Attributes del Button per sovrascrivere il suo evento OnClick.

{{% alert color="primary" %}} 

ASP.NET Il controllo pulsante è un controllo lato server. Ogni volta che viene cliccato, viene attivato un evento lato server, ma se si desidera utilizzare questo controllo Button per eseguire del codice sul lato client (normalmente utilizzando javascript), è necessario modificare il suo attributo onclick nell'evento Page_Load. Aspose.Cells.GridWeb fornisce alcune funzioni che possono essere richiamate in javascript per gestire il controllo GridWeb dal lato client. Nell'esempio seguente, abbiamo utilizzato le funzioni updateData e validateAll (che sono funzioni lato client) di GridWeb per aggiornare e convalidare i dati Grid.

{{% /alert %}} 
#### **Esempio di codice**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-UsingCommonSubmitButton.aspx-UsingCommonSubmitButton.cs" >}}
### **3. Esecuzione dell'applicazione**
Ora puoi compilare ed eseguire la tua applicazione premendo Ctrl+F5 e la pagina verrà aperta in una nuova finestra del browser. Aggiungiamo alcuni valori a GridWeb e premiamo il pulsante Submit Grid Data to Server e vedresti verificarsi un postback per aggiornare e convalidare i dati di GridWeb.
## **Conclusione**
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb offre una grande flessibilità per lavorare con i controlli GridWeb dal lato server o client. Gli sviluppatori hanno un ampio numero di opzioni per utilizzare il controllo GridWeb in diversi tipi di scenari per fornire soluzioni migliori ai propri clienti.

{{% /alert %}}
