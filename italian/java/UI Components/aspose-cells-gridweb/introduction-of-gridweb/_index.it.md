---
title: Introduzione di GridWeb
type: docs
weight: 10
url: /it/java/introduction-of-gridweb/
---
## **Come eseguire Aspose.Cells per GridWeb Java Demo**
{{% alert color="primary" %}} 

 Aspose.Cells per GridWeb Java le demo sono facili da eseguire. Devi solo schierare**gridwebdemo.war** nel tuo server web. Si prega di scaricare le demo da questo[collegamento](https://forum.aspose.com/uploads/discourse_instance3/22292).

Questo articolo descrive come eseguire Aspose.Cells per GridWeb Java demo in Apache Tomcat Server.

{{% /alert %}} 
### **Guida passo passo per eseguire le demo di GridWeb Java**
1.  Estratto**apache-tomcat-7.0.52.zip** in qualsiasi directory, ad esempio C:\Tomcat

![cose da fare:immagine_alt_testo](introduction-of-gridweb_1.png)



 Lo snapshot seguente mostra le directory e i file estratti del server Apache Tomcat

![cose da fare:immagine_alt_testo](introduction-of-gridweb_2.png)



 Potrebbe anche essere necessario impostare la variabile di ambiente**CATALINA_HOME** 

![cose da fare:immagine_alt_testo](introduction-of-gridweb_3.png)

1. Apri il**tomcat-users.xml** file.

![cose da fare:immagine_alt_testo](introduction-of-gridweb_4.png)

1. Aggiungi questo utente:

{{< highlight "java" >}}

   <role rolename="manager-gui"/>

  <user username="tomcat" password="secret" roles="manager-gui"/>

{{< /highlight >}}



**Qui il nome utente è tomcat e la password è segreta** 

![cose da fare:immagine_alt_testo](introduction-of-gridweb_5.png)

1.  Corri il**avvio.bat** file.
 Eseguirà Apache Tomcat Server.

![cose da fare:immagine_alt_testo](introduction-of-gridweb_6.png)



**Server Tomcat in esecuzione in una finestra di comando** 

![cose da fare:immagine_alt_testo](introduction-of-gridweb_7.png)

1.  Ora apri il browser e digita**host locale:8080**.
 Viene visualizzata la pagina web di Apache Tomcat.

   **La pagina web di Apache Tomcat** 

![cose da fare:immagine_alt_testo](introduction-of-gridweb_8.png)

1.  Clic**App Manager** e digitare nome utente e password. (Come sopra: gatto, segreto)

![cose da fare:immagine_alt_testo](introduction-of-gridweb_9.png)

1.  Scorri verso il basso fino alla sezione**File WAR da distribuire** e sfoglia il**gridwebdemo.war** file.
1.  Clic**Distribuisci**. 

![cose da fare:immagine_alt_testo](introduction-of-gridweb_10.png)

1.  Navigare**gridwebdemo.war** file.

![cose da fare:immagine_alt_testo](introduction-of-gridweb_11.png)

1.  Clic**Distribuisci**. 

![cose da fare:immagine_alt_testo](introduction-of-gridweb_12.png)

1.  Una volta distribuito, fare clic su**/gridwebdemo** e inizia a eseguire demo.

![cose da fare:immagine_alt_testo](introduction-of-gridweb_13.png)


 Viene visualizzata la pagina Demo di GridWeb.

**La pagina dimostrativa di GridWeb** 

![cose da fare:immagine_alt_testo](introduction-of-gridweb_14.png)

1.  Fai clic su qualsiasi demo ed eseguila.

   **Creazione di contenuti demo in esecuzione** 

![cose da fare:immagine_alt_testo](introduction-of-gridweb_15.png)



**Demo dei fogli di lavoro in esecuzione** 

![cose da fare:immagine_alt_testo](introduction-of-gridweb_16.png)



**Demo di HeaderBar e CommandButton in esecuzione** 

![cose da fare:immagine_alt_testo](introduction-of-gridweb_17.png)
## **Aspose.Cells.GridWeb - Demo**
{{% alert color="primary" %}} 

Per metterti in funzione rapidamente, forniamo una serie di esempi di codice e demo che mostrano come utilizzare Aspose.Cells.GridWeb API.

Si prega di scaricare le demo dal link sottostante:
[Aspose.Cells.GridWeb Demo](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb)

{{% /alert %}} 
## **Funzionalità dei browser e Aspose.Cells.GridWeb**
Aspose.Cells.GridWeb è un controllo Web basato su GUI che può essere incorporato nelle pagine Web JSP come altri controlli Web. La cosa più importante del controllo web è fornire supporto cross-browser. Aspose.Cells.GridWeb fornisce supporto cross-browser.
### **Confronto**
Aspose.Cells.GridWeb è completamente supportato su Internet Explorer (IE) di Microsoft. Tuttavia, su altri browser, presenta limitazioni minori. Questo argomento fornisce un confronto dettagliato delle funzionalità supportate da diversi browser.

|**Funzionalità lato client**|**Microsoft Internet Explorer**|**Google Cromo**|**Mozilla Firefox**|**musica lirica**|
|:- |:- |:- |:- |:- |
|Menu contestuale di Cell|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/cross >}}|
|Convalida lato client|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Evento doppio clic|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| Menu `A tendina (*Modalità casella combinata* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| Menu `A tendina (*Modalità menu a comparsa* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Immissione/modifica formule|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Blocca o sblocca righe/colonne|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| Collegamenti ipertestuali (*Modalità CellCommand* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| Collegamenti ipertestuali (*Modalità URL* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Unisci o Separa Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Multiplo Cells Copia/Incolla|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Multiplo Cells Input/Modifica, postback singolo|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Formato numerico|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Paginazione del foglio|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Sola lettura Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Righe/colonne di sola lettura|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Convalida dei dati mediante espressioni regolari|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Ridimensiona la larghezza della colonna|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Ridimensiona l'altezza della riga|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Inserisci/Elimina righe e colonne|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Scorri il contenuto|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Scorri le schede dei fogli|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Imposta i bordi di Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Impostare le impostazioni dei caratteri di Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
{{< emoticons/cross >}} Il menu contestuale di una cella può essere attivato solo facendo clic sul pulsante Menu lato client.
