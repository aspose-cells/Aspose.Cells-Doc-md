---
title: Abilita GridWeb EditBox
type: docs
weight: 110
url: /it/net/enable-gridweb-editbox/
---
{{% alert color="primary" %}} 

La casella di modifica di GridWeb è una barra degli strumenti visualizzata nella parte superiore del controllo che è possibile utilizzare per visualizzare/inserire o copiare dati/formula nelle celle. Mostra anche il nome della cella che stai modificando. Dopo aver fatto clic sulla cornice o quando si inizia a scrivere dati o si digita un simbolo di uguale (=), verrà attivata la casella di modifica.

{{% /alert %}} 
## **Impostazione della casella di modifica di Aspose.Cells.GridWeb**
Il controllo GridWeb fornisce la proprietà ShowCellEditBox a cui gli sviluppatori possono assegnarla su "True" per attivare la barra degli strumenti. Il valore predefinito dell'attributo è False. Quando ne imposti il valore su "True", la casella di modifica verrà visualizzata nella parte superiore del controllo GridWeb.

{{% alert color="primary" %}} 

 Per abilitare questa funzione, devi importare il file "jquery.js" nel tuo progetto e farvi riferimento nelle tue pagine .aspx per farlo funzionare. È possibile scaricare l'archivio jQuery da<https://jqueryui.com/download/all/> e inserisci i file della libreria in una cartella del progetto e aggiungi un riferimento al file della libreria tramite<script> tag nel tuo modulo web .aspx come segue. Tutte le ultime versioni di jQuery sono OK.

{{< highlight "csharp" >}}

 <head id="Head1" runat="server">

  <title>Untitled Page</title>

  <script type="text/javascript" src="/jquery/jquery.js"></script>

</head>



{{< /highlight >}}

{{% /alert %}} 

**Controllo GridWeb con casella di modifica** 

![cose da fare:immagine_alt_testo](enable-gridweb-editbox_1.png)
### **Esempio**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-DisplayCellEditBox.aspx-DisplayCellEditBox.cs" >}}
