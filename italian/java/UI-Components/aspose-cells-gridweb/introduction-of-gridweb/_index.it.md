---
title: Introduzione di GridWeb
type: docs
weight: 10
url: /it/java/introduction-of-gridweb/
---
## **Nozioni di base di GridWeb**
Aspose.Cells.GridWeb è un controllo web basato su GUI che può essere incorporato nelle pagine web JSP o in qualsiasi pagina html nel server Java. 

È facile e semplice da usare.

Ti aiuta a creare rapidamente un editor web online per file di fogli di calcolo.

Supporta anche l'importazione e l'esportazione di tutti i tipi di file in formato foglio di calcolo, che è compatibile al 100% con il file MS Excel.

## **Aspose.Cells.GridWeb - Demo**

Per avviarti rapidamente, forniamo alcuni esempi di codice e demo che mostrano come utilizzare l'API Aspose.Cells.GridWeb.

Si prega di scaricare le demo dal link sottostante:
[Demo Aspose.Cells.GridWeb](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/master/Examples.GridWeb)


## **Come eseguire le Demo Aspose.Cells for GridWeb Java**
{{% alert color="primary" %}} 

Le demo Aspose.Cells for GridWeb Java sono facili da eseguire. È sufficiente distribuire **gridwebdemo.war** nel proprio server web. Si prega di scaricare le demo da questo [link](https://forum.aspose.com/uploads/discourse_instance3/22292).

Questo articolo descrive come eseguire le Demo Aspose.Cells for GridWeb Java in Apache Tomcat Server.

{{% /alert %}} 
### **Guida passo passo per eseguire le Demo GridWeb Java**
1. Estrarre **apache-tomcat-7.0.52.zip** in una qualsiasi directory, ad es. C:\Tomcat 

![todo:image_alt_text](introduction-of-gridweb_1.png)



Lo snapshot seguente mostra le directory e i file estratti del server Apache Tomcat 

![todo:image_alt_text](introduction-of-gridweb_2.png)



Potresti anche dover impostare la variabile d'ambiente **CATALINA_HOME** 

![todo:image_alt_text](introduction-of-gridweb_3.png)

1. Apri il file **tomcat-users.xml** 

![todo:image_alt_text](introduction-of-gridweb_4.png)

1. Aggiungi questo utente:

{{< highlight java >}}

   <role rolename="manager-gui"/>

  <user username="tomcat" password="secret" roles="manager-gui"/>

{{< /highlight >}}



**Qui il nome utente è tomcat e la password è segreta** 

![todo:image_alt_text](introduction-of-gridweb_5.png)

1. Esegui il file **startup.bat**
   Esso avvierà il server Apache Tomcat. 

![todo:image_alt_text](introduction-of-gridweb_6.png)



**Server Tomcat in esecuzione in una finestra di comando** 

![todo:image_alt_text](introduction-of-gridweb_7.png)

1. Ora apri il browser e digita **localhost:8080**.
   Viene visualizzata la pagina web di Apache Tomcat. 

   **La pagina web di Apache Tomcat** 

![todo:image_alt_text](introduction-of-gridweb_8.png)

1. Fare clic su **App Manager** e inserire nome utente e password. (Come sopra: tomcat, segreto) 

![todo:image_alt_text](introduction-of-gridweb_9.png)

1. Scorri verso il basso nella sezione **File WAR da distribuire** e cerca il file **gridwebdemo.war**.
1. Fare clic su **Distribuisci**. 

![todo:image_alt_text](introduction-of-gridweb_10.png)

1. Sfoglia il file **gridwebdemo.war**. 

![todo:image_alt_text](introduction-of-gridweb_11.png)

1. Fare clic su **Distribuisci**. 

![todo:image_alt_text](introduction-of-gridweb_12.png)

1. Una volta distribuito, fare clic su **/gridwebdemo** e avviare le demo. 

![todo:image_alt_text](introduction-of-gridweb_13.png)


Viene visualizzata la pagina demo di GridWeb. 

**La pagina demo di GridWeb** 

![todo:image_alt_text](introduction-of-gridweb_14.png)

1. Fare clic su qualsiasi demo e eseguilo. 

   **Creazione di contenuti demo in esecuzione** 

![todo:image_alt_text](introduction-of-gridweb_15.png)



**Demo dei fogli di lavoro in esecuzione** 

![todo:image_alt_text](introduction-of-gridweb_16.png)



**Demo HeaderBar e CommandButton in esecuzione** 

![todo:image_alt_text](introduction-of-gridweb_17.png)


## **Capacità dei browser e Aspose.Cells.GridWeb**
Aspose.Cells.GridWeb è un controllo web basato su GUI che può essere incorporato nelle pagine web JSP come altri controlli web. La cosa più importante riguardo al controllo web è fornire supporto multipiattaforma. Aspose.Cells.GridWeb fornisce supporto multipiattaforma.
### **Confronto**
Aspose.Cells.GridWeb è completamente supportato da Internet Explorer di Microsoft (IE). Tuttavia, su altri browser, ha limitazioni minori. Questo argomento fornisce un confronto dettagliato di quali funzionalità sono supportate da browser diversi.

|**Funzionalità lato client**|**Microsoft Internet Explorer**|**Google Chrome**|**Mozilla Firefox**|**Opera**|
| :- | :- | :- | :- | :- |
|Menu contestuale della cella|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/cross >}}|
|Convalida lato client|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Evento doppio clic|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|DropDownList (*Modalità ComboBox*)|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|DropDownList (*Modalità Menu a comparsa*)|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Input/Modifica formula|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Congelare o scongelare righe/colonne|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Link ipertestuali (*Modalità CellCommand*)|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Link ipertestuali (*Modalità URL*)|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Unire o separare celle|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Copia/Incolla celle multiple|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Input/Modifica celle multiple, singolo postback|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Formato numero|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Paginazione foglio|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Celle in sola lettura|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Righe/Colonne in sola lettura|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Convalida dati usando espressioni regolari|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Ridimensionare larghezza colonna|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Ridimensionare altezza riga|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Inserisci/Elimina righe e colonne|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Contenuto di scorrimento|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Schede Foglio Scorrimento|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Imposta Bordi delle celle|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Imposta Impostazioni del carattere delle celle|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
{{< emoticons/cross >}} Context menu of a cell can only be activated by clicking the Client side menu button.
