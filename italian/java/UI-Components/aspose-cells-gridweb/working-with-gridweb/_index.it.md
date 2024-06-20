---
title: Lavorare con GridWeb
type: docs
weight: 20
url: /it/java/working-with-gridweb/
---

## **Apertura di un file Microsoft Excel**

Il controllo Aspose.Cells.GridWeb può aprire e caricare file Microsoft Excel - completi di dati, formattazione, grafici, immagini, ecc. Questo argomento spiega come.

Per aprire un file Excel utilizzando il controllo GridWeb:

1. Aggiungi il controllo Aspose.Cells.GridWeb a un modulo web o a una pagina.
1. Importa il file Excel specificando il percorso del file.
1. Esegui l'applicazione o apri la pagina.

Per caricare i contenuti da un file Excel nel controllo Aspose.Cells.GridWeb, devi chiamare il metodo importExcelFile per specificare il percorso del file Excel. Dopo di che, il controllo GridWeb troverà automaticamente il file dal percorso specificato e ne visualizzerà i contenuti. Di seguito è fornito un frammento di codice che carica i contenuti di un file Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-OpeningfromFile-OpeningfromFile.jsp" >}}

Il frammento di codice sopra può essere utilizzato in qualsiasi modo desideri. Ad esempio, per caricare automaticamente un file Excel quando un modulo web si carica, aggiungi questo codice all'evento Page_Load del modulo che hai specificato tu stesso.

**Un file Excel viene caricato in GridWeb**

![todo:image_alt_text](working-with-gridweb_1.png)

## **Salvataggio di un file Excel Microsoft**

È possibile creare nuovi o manipolare file Microsoft Excel esistenti, su siti web in modalità GUI utilizzando il controllo Aspose.Cells.GridWeb. I file possono poi essere salvati come file Excel. Aspose.Cells.GridWeb funziona efficacemente come un editor di fogli elettronici online. Questo argomento descrive come salvare i contenuti della griglia come file Excel.

### **Salvataggio come file**

Per salvare il contenuto del controllo Aspose.Cells.GridWeb come file Excel:

1. Aggiungi il controllo Aspose.Cells.GridWeb a un modulo web o a una pagina.
1. Salva il tuo lavoro come file Excel in un percorso specificato.
1. Esegui l'applicazione o apri la pagina.

L'esempio di codice sottostante illustra come salvare i contenuti della griglia in un file Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-SavingasFile-SavingasFile.jsp" >}}

Il frammento di codice sopra può essere utilizzato in diversi modi. Un modo comune è aggiungere un pulsante che salva i contenuti della griglia in un file Excel quando viene cliccato. Aspose.Cells.GridWeb offre un approccio più semplice per il compito. Aspose.Cells.GridWeb ha un evento chiamato SaveCommand. Il frammento di codice sopra può essere aggiunto all'gestore eventi dell'evento SaveCommand che consente agli utenti di salvare il proprio lavoro cliccando sul pulsante **Salva** integrato in Aspose.Cells.GridWeb.

## **Ridimensionamento di Aspose.Cells.GridWeb e della barra degli header**

Questo articolo spiega come ridimensionare GridWeb durante l'esecuzione utilizzando l'API di Aspose.Cells.GridWeb. Spiega anche come ridimensionare le barre degli header del controllo Aspose.Cells.GridWeb per rendere i dati più facili da leggere.

### **Modifica della larghezza e dell'altezza di Aspose.Cells.GridWeb**

La modifica della larghezza e altezza del controllo Aspose.Cells.GridWeb è una caratteristica semplice ma importante. Il controllo Aspose.Cells.GridWeb è rappresentato dalla classe GridWeb nell'API. Per ridimensionare la larghezza e altezza del controllo GridWeb, utilizzare semplicemente le proprietà di larghezza e altezza.

{{% alert color="primary" %}}

La larghezza e l'altezza del controllo possono essere definite in pixel o punti.

{{% /alert %}}

L'output del frammento di codice che segue è mostrato di seguito.

**Modificata larghezza e altezza del controllo GridWeb**

![todo:image_alt_text](working-with-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangedwidthheightofGridWebcontrol-ChangedwidthheightofGridWebcontrol.jsp" >}}

### **Modifica larghezza e altezza della barra dell'intestazione**

Il controllo Aspose.Cells.GridWeb contiene due barre dell'intestazione come segue:

- Barra dell'intestazione superiore, questa barra dell'intestazione rappresenta le colonne come A, B, C, D, ecc.
- Barra dell'intestazione sinistra, questa barra dell'intestazione rappresenta le righe come 1, 2, 3, 4, ecc.

Entrambe queste barre dell'intestazione sono mostrate di seguito.

**Barre dell'intestazione**

![todo:image_alt_text](working-with-gridweb_3.png)

Modificare l'altezza della barra dell'intestazione superiore e la larghezza della barra dell'intestazione sinistra utilizzando rispettivamente le proprietà HeaderBarHeight e HeaderBarWidth del controllo GridWeb. La figura seguente mostra l'output dell'esempio di codice che segue.

**Modificata larghezza e altezza della barra dell'intestazione**

![todo:image_alt_text](working-with-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangingWidthandHeightofHeaderBar-ChangingWidthandHeightofHeaderBar.jsp" >}}

## **Lavorare con gli eventi Aspose.Cells.GridWeb**

Tutti gli sviluppatori devono essere familiarità con gli eventi e il loro scopo. Gli eventi vengono utilizzati per inviare notifiche di modifiche che possono verificarsi in un controllo o una classe. Aspose.Cells.GridWeb ha diversi eventi che possono essere utilizzati per eseguire attività specifiche quando si verificano determinate modifiche nel controllo.

Questo argomento fornisce un'introduzione a tutti gli eventi supportati dal controllo Aspose.Cells.GridWeb insieme ad alcuni dettagli su come gestire questi eventi.

### **Introduzione agli eventi della griglia**

Il controllo Aspose.Cells.GridWeb supporta diversi eventi che forniscono maggior controllo per eseguire operazioni quando vengono attivati eventi specifici nel controllo. Di seguito è possibile trovare un elenco completo degli eventi supportati dal controllo Aspose.Cells.GridWeb.

|**Eventi**|**Descrizione**|
| :- | :- |
|CellCommand|Si verifica quando il collegamento ipertestuale del cella viene cliccato. Quando questo evento viene generato, il suo parametro e.Argument fornisce il nome del comando.|
|CellDoubleClick|Si verifica quando la cella viene doppio-cliccata.|
|ColumnDeleted|Si verifica quando un utente elimina una colonna da un foglio di lavoro utilizzando il menu lato client.|
|ColumnDeleting|Si verifica quando un utente cerca di eliminare una colonna da un foglio di lavoro utilizzando il menu lato client.|
|ColumnDoubleClick|Si verifica quando l'intestazione della colonna viene selezionata due volte.|
|ColumnInserted|Si verifica quando un utente inserisce una colonna in un foglio di lavoro utilizzando il menu lato client.|
|CustomCommand|Si verifica quando un utente fa clic su un pulsante di comando personalizzato.|
|LoadCustomData|Si verifica quando la proprietà EnableSession del controllo è impostata su false e è necessario caricare i dati del foglio di lavoro. È possibile gestire questo evento in modalità senza sessione per caricare i dati del foglio di lavoro da un file o un database.|
|PageIndexChanged|Si verifica quando l'indice della pagina del foglio del controllo cambia.|
|RowDeleted|Si verifica quando un utente elimina una riga dal foglio di lavoro utilizzando il menu lato client.|
|RowDeleting|Si verifica quando un utente cerca di eliminare una riga da un foglio di lavoro utilizzando il menu lato client.|
|RowDoubleClick|Si verifica quando l'intestazione della riga viene selezionata due volte.|
|RowInserted|Si verifica quando un utente inserisce una riga nel foglio di lavoro utilizzando il menu lato client.|
|SaveCommand|Si verifica quando viene cliccato il pulsante **Salva**.|
|SheetTabClick|Si verifica quando viene selezionata una scheda del foglio.|
|SubmitCommand|Si verifica quando viene cliccato il pulsante **Invia**.|
|UndoCommand|Si verifica quando viene cliccato il pulsante **Annulla**.|
|AjaxCallFinished|Viene attivato quando l'aggiornamento AJAX del controllo è completato. (l'EnableAJAX deve essere impostato su true).|
|CellModifiedOnAjax|Viene attivato quando la cella viene modificata nella chiamata AJAX.|
|AfterColumnFilter|Si verifica quando il filtro viene applicato su una colonna.|

### **Gestione degli eventi della griglia**

Per eseguire una specifica operazione in seguito all'attivazione di un evento specifico, è necessario creare un gestore di eventi. Un gestore di eventi esegue l'operazione desiderata quando si verifica un determinato evento. L'esempio che segue mostra come gestire un evento semplice della griglia.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HandlingGridEvents-HandlingGridEvents.jsp" >}}

## **Lavorare con eventi di doppio clic**

Aspose.Cells.GridWeb contiene tre tipi di eventi di doppio clic:

- CellDoubleClick, attivato quando viene effettuato un doppio clic su una cella.
- ColumnDoubleClick, attivato quando viene effettuato un doppio clic sull'intestazione di una colonna.
- RowDoubleClick, attivato quando viene effettuato un doppio clic sull'intestazione di una riga.

Questo argomento tratta su come abilitare eventi di doppio clic in Aspose.Cells.GridWeb. Tratta anche la creazione di gestori di eventi per questi eventi.

### **Abilita eventi di doppio clic**

Tutti i tipi di eventi di doppio clic possono essere abilitati lato client impostando la proprietà EnableDoubleClickEvent del controllo GridWeb su true.

{{% alert color="primary" %}}

Per impostazione predefinita, la proprietà EnableDoubleClickEvent è impostata su false. Ciò significa che gli eventi di doppio clic non sono abilitati per impostazione predefinita. Per implementare tali eventi, abilitare prima la funzionalità.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-EnablingDoubleClickEvents-EnablingDoubleClickEvents.jsp" >}}

Una volta abilitati gli eventi di doppio clic, è possibile creare gestori di eventi per qualsiasi evento di doppio clic. Questi gestori di eventi eseguono attività specifiche quando un dato evento di doppio clic viene attivato.

### **Gestione degli eventi di doppio clic**

#### **Doppio clic cella**

Il gestore di eventi per l'evento CellDoubleClick fornisce un argomento del tipo CellEventArgs, che fornisce le informazioni complete della cella su cui è stato effettuato il doppio clic.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickCell-DoubleClickCell.jsp" >}}

#### **Doppio clic su intestazione colonna**

Il gestore di eventi per l'evento ColumnDoubleClick fornisce un argomento del tipo RowColumnEventArgs che fornisce il numero di indice della colonna dell'intestazione su cui è stato effettuato il doppio clic e altre informazioni.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickColumnHeader-DoubleClickColumnHeader.jsp" >}}

#### **Doppio clic su intestazione riga**

Il gestore di eventi per l'evento RowDoubleClick fornisce un argomento del tipo RowColumnEventArgs che fornisce il numero di indice della riga dell'intestazione su cui è stato effettuato il doppio clic e altre informazioni correlate.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickRowHeader-DoubleClickRowHeader.jsp" >}}

## **Impostazione dello stile o dell'aspetto di Aspose.Cells.GridWeb**

Aspose.Cells.GridWeb ha il suo aspetto predefinito ma è possibile cambiarne l'aspetto. Aspose.Cells.GridWeb fornisce diverse proprietà per consentire agli sviluppatori di controllarne completamente l'aspetto. Questo argomento tratta alcune di quelle proprietà.

### **Impostazione dello stile o dell'aspetto di Aspose.Cells.GridWeb**

#### **Stili preimpostati**

Per risparmiare gli sforzi degli sviluppatori, Aspose.Cells.GridWeb offre alcuni stili preimpostati. Seleziona semplicemente uno stile dalla lista per applicarlo.

|**Stili**|**Schema colore**|
| :- | :- |
|Standard|Silver|
|Colorful1|Rose|
|Colorful2|Blue|
|Professional1|Cyan|
|Professional2|Cyan again|
|Traditional1|Dark|
|Traditional2|Gray|
|Custom|Customized|
Quando viene selezionato uno stile particolare, cambia l'intera apparenza del controllo GridWeb. Gli sviluppatori possono selezionare uno Stile predefinito da applicare in fase di esecuzione utilizzando l'API flessibile di Aspose.Cells.GridWeb.

Il controllo GridWeb fornisce la proprietà PresetStyle a cui gli sviluppatori possono assegnare qualsiasi stile predefinito desiderato.

L'output dell'estratto di codice seguente è mostrato di seguito.

**Controllo GridWeb con lo stile Colorful1 applicato ad esso**

![todo:image_alt_text](working-with-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

#### **Stile della barra dell'intestazione**

Se dai un'occhiata al controllo GridWeb, noterai due barre dell'intestazione. Una per le colonne (cioè A, B, C, D, ecc.) e l'altra per le righe (cioè 1, 2, 3, 4, ecc.). Aspose.Cells.GridWeb consente agli sviluppatori di controllare l'aspetto di queste barre dell'intestazione. Gli sviluppatori possono impostare lo stile delle barre dell'intestazione in fase di esecuzione.

{{% alert color="primary" %}}

Il controllo GridWeb fornisce la proprietà HeaderBarStyle che applica uno stile a entrambe le barre dell'intestazione del controllo.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

#### **Stile della barra delle schede**

È possibile impostare anche lo stile della barra delle schede. Consulta il seguente codice

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HeaderBarStyle-HeaderBarStyle.jsp" >}}

#### **Caricamento del file di stile**

Per applicare le impostazioni di stile da un file di stile esistente al controllo GridWeb, gli sviluppatori possono impostare il percorso del file di stile sulla proprietà CustomStyleFileName del controllo. Ma, prima di fare ciò, è necessario impostare la proprietà PresetStyle del controllo su Personalizzato. Questo perché il file di stile contiene informazioni di stile personalizzate già definite da uno sviluppatore.

Consulta l'immagine seguente che mostra GridWeb con lo stile personalizzato applicato ad esso.

![todo:image_alt_text](working-with-gridweb_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-CustomStyleSheet-CustomStyleSheet.jsp" >}}

{{% alert color="primary" %}}

IMPORTANTE: Il caricamento del file di stile nel controllo GridWeb non influisce sulle impostazioni di formattazione delle celle del controllo.

{{% /alert %}}

#### **Modello di stile personalizzato di esempio**

Ecco il modello di stile personalizzato di esempio. Puoi modificarlo secondo le tue esigenze.

{{< highlight java >}}

 <aspose.excel.web.viewerStyletemplate runat="server" HeaderBarWidth="30pt" ScrollBarBaseColor="#AFEEEE" SelectCellBgColor="#FFFAF0" ActiveHeaderBgColor="#DAA520" ActiveCellBgColor="#DDDDFF" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LeftBorderStyle-BorderWidth="" FrameTableStyle-LeftBorderStyle-BorderColor="" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-RightBorderStyle-BorderWidth="" FrameTableStyle-RightBorderStyle-BorderColor="" FrameTableStyle-BorderWidth="1px" FrameTableStyle-CellSpacing="0" FrameTableStyle-BorderColor="#C0FFC0" FrameTableStyle-CellPadding="0" FrameTableStyle-TopBorderStyle-BorderWidth="" FrameTableStyle-TopBorderStyle-BorderColor="" FrameTableStyle-BackColor="#FFFFCC" FrameTableStyle-BottomBorderStyle-BorderWidth="" FrameTableStyle-BottomBorderStyle-BorderColor="" HeaderBarStyle-LeftBorderStyle-BorderWidth="" HeaderBarStyle-LeftBorderStyle-BorderColor="" HeaderBarStyle-verticalalign="Middle" HeaderBarStyle-RightBorderStyle-BorderWidth="" HeaderBarStyle-RightBorderStyle-BorderColor="" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-font-size="10pt" HeaderBarStyle-BorderColor="#00C0C0" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-horizontalalign="Center" HeaderBarStyle-ForeColor="Red" HeaderBarStyle-TopBorderStyle-BorderWidth="" HeaderBarStyle-TopBorderStyle-BorderColor="" HeaderBarStyle-BackColor="#D8BFD8" HeaderBarStyle-BottomBorderStyle-BorderWidth="" HeaderBarStyle-BottomBorderStyle-BorderColor="" ViewTableStyle-LeftBorderStyle-BorderWidth="" ViewTableStyle-LeftBorderStyle-BorderColor="" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-RightBorderStyle-BorderWidth="" ViewTableStyle-RightBorderStyle-BorderColor="" ViewTableStyle-BorderWidth="0px" ViewTableStyle-CellSpacing="0" ViewTableStyle-CellPadding="0" ViewTableStyle-TopBorderStyle-BorderWidth="" ViewTableStyle-TopBorderStyle-BorderColor="" ViewTableStyle-BottomBorderStyle-BorderWidth="" ViewTableStyle-BottomBorderStyle-BorderColor="" BottomTableStyle-LeftBorderStyle-BorderWidth="" BottomTableStyle-LeftBorderStyle-BorderColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-RightBorderStyle-BorderWidth="" BottomTableStyle-RightBorderStyle-BorderColor="" BottomTableStyle-Height="32pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-CellSpacing="0" BottomTableStyle-BorderColor="#80FF80" BottomTableStyle-CellPadding="0" BottomTableStyle-ForeColor="#FFE0C0" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="#FF69B4" BottomTableStyle-BottomBorderStyle-BorderWidth="" BottomTableStyle-BottomBorderStyle-BorderColor="" HeaderBarHeight="15pt" ActiveTabStyle-LeftBorderStyle-BorderWidth="" ActiveTabStyle-LeftBorderStyle-BorderColor="" ActiveTabStyle-RightBorderStyle-BorderWidth="" ActiveTabStyle-RightBorderStyle-BorderColor="" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-font-size="10pt" ActiveTabStyle-BorderColor="#00C0C0" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="#FF00FF" ActiveTabStyle-TopBorderStyle-BorderWidth="" ActiveTabStyle-TopBorderStyle-BorderColor="" ActiveTabStyle-BackColor="#80FFFF" ActiveTabStyle-BottomBorderStyle-BorderWidth="" ActiveTabStyle-BottomBorderStyle-BorderColor="" HeaderBarTableStyle-LeftBorderStyle-BorderWidth="" HeaderBarTableStyle-LeftBorderStyle-BorderColor="" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-RightBorderStyle-BorderWidth="" HeaderBarTableStyle-RightBorderStyle-BorderColor="" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-CellSpacing="0" HeaderBarTableStyle-CellPadding="0" HeaderBarTableStyle-TopBorderStyle-BorderWidth="" HeaderBarTableStyle-TopBorderStyle-BorderColor="" HeaderBarTableStyle-BackColor="#C0FFC0" HeaderBarTableStyle-BottomBorderStyle-BorderWidth="" HeaderBarTableStyle-BottomBorderStyle-BorderColor="" DefaultGridLineColor="#228B22" TabStyle-LeftBorderStyle-BorderWidth="" TabStyle-LeftBorderStyle-BorderColor="" TabStyle-RightBorderStyle-BorderWidth="" TabStyle-RightBorderStyle-BorderColor="" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-font-size="8pt" TabStyle-BorderColor="#8080FF" TabStyle-BorderStyle="Groove" TabStyle-ForeColor="#FFFFCC" TabStyle-TopBorderStyle-BorderWidth="" TabStyle-TopBorderStyle-BorderColor="" TabStyle-BackColor="#C0C0FF" TabStyle-BottomBorderStyle-BorderWidth="" TabStyle-BottomBorderStyle-BorderColor="" scrollbararrowColor="#778899"/>

{{< /highlight >}}

## **Creazione del controllo su un modulo web**

Questo articolo ti guiderà su come creare un semplice modulo web JSP (Java Server Page) con il controllo GridWeb.

**Passo 1 - Creare la struttura delle directory**

È necessario creare la seguente struttura delle directory nella directory **webapps** del server Tomcat

![todo:image_alt_text](working-with-gridweb_7.png)

Queste sono le directory e i file da creare. Si prega di leggere i commenti e seguirli. È possibile ottenere gli archivi dell'ultima versione di Aspose.Cells.GridWeb for Java da [questo link](https://downloads.aspose.com/cells/java).

{{< highlight java >}}

 SamplePageGridWebJava

SamplePageGridWebJava\grid

//Get acwclient directory from GridWeb latest release archive from Downloads section

SamplePageGridWebJava\acwclient

SamplePageGridWebJava\WEB-INF

SamplePageGridWebJava\WEB-INF\lib

//Get aspose-gridweb-x.x.x.jar file from GridWeb latest release archive from Downloads section

SamplePageGridWebJava\WEB-INF\aspose-gridweb-x.x.x.jar

SamplePageGridWebJava\WEB-INF\web.xml

SamplePageGridWebJava\head.jsp

//Create this excel file using Microsoft Excel or you can use any excel file and rename it SampleExcel.xlsx

SamplePageGridWebJava\SampleExcel.xlsx

SamplePageGridWebJava\SamplePage.jsp

{{< /highlight >}}

**Passo 2 - Aggiungere codici nei file creati**

Questa sezione mostra il codice per vari file creati nella struttura delle directory sopra. Si prega di prendere questi codici e aggiungerli nei file aprendoli in Blocco note e copiandoli/incollandoli.

**Web.xml**

{{< highlight java >}}

 <?xml version="1.0" encoding="UTF-8"?>

<web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://java.sun.com/xml/ns/javaee" xmlns:web="http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd" xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd" id="WebApp_ID" version="2.5">

  <display-name>testGridWeb</display-name>

  <welcome-file-list>

    <welcome-file>SamplePage.jsp</welcome-file>

  </welcome-file-list>

  <servlet>

    <display-name>GridWebServlet</display-name>

    <servlet-name>GridWebServlet</servlet-name>

    <servlet-class>com.aspose.gridweb.GridWebServlet</servlet-class>

  </servlet>

  <servlet-mapping>

    <servlet-name>GridWebServlet</servlet-name>

    <url-pattern>/GridWebServlet</url-pattern>

  </servlet-mapping>

</web-app>

{{< /highlight >}}

**head.jsp**

{{< highlight java >}}

 <%

String path = request.getContextPath();

String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";

%>

<meta http-equiv="X-UA-Compatible" content="IE=EmulateIE9"/>

<base href="<%=basePath%>">

<script type="text/javascript" language="javascript"

	src="grid/acw_client/acwmain.js"></script>

<script type="text/javascript" language="javascript"

	src="grid/acw_client/lang_en.js"></script>

<link href="grid/acw_client/menu.css" rel="stylesheet" type="text/css" />

<style>

span.acwxc {

	overflow: hidden;

	border: none;

	display: block;

	white-space: pre;

}

</style>

<style>

span.rotation90 {

	width: 100%;

	height: 100%;

	border: none;

	-webkit-transform: rotate(-90deg);

	-moz-transform: rotate(-90deg);

	filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=3 );

	display: block

}

</style>

<style>

span.rotation-90 {

	filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=1 );

	width: 100%;

	height: 100%;

	border: none;

	-webkit-transform: rotate(90deg);

	-moz-transform: rotate(90deg);

	display: block

}

</style>

<style>

span.wrap {

	white-space: pre-wrap;

	white-space: -moz-pre-wrap;

	white-space: -pre-wrap;

	white-space: -o-pre-wrap;

	word-wrap: break-word;

	-ms-word-break: break-all;

}

</style>

{{< /highlight >}}

**SamplePage.jsp**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-SamplePage-SamplePage.jsp" >}}

**Passo 3 - Esecuzione della tua Pagina Web JSP di Esempio**

Ora hai fatto tutto. È il momento di eseguire la pagina web. Si prega di avviare il server Tomcat e quindi incollare l'URL seguente nel browser web.

{{< highlight java >}}

 http://localhost:8080/SamplePageGridWebJava/SamplePage.jsp

{{< /highlight >}}

Vedrai qualcosa di simile alla seguente schermata. Congratulazioni, hai usato con successo il controllo GridWeb sulla tua pagina JSP.

![todo:image_alt_text](working-with-gridweb_8.png)

## **Stampa di GridWeb**

A volte i programmatori devono stampare il contenuto di GridWeb incluso da una pagina web senza salvare un file Microsoft Excel. Il controllo Aspose.Cells.GridWeb supporta questa funzionalità.

### **Stampa di GridWeb**

Per stampare senza salvare un file separato, chiamare il metodo print() della classe GridWeb lato client per stampare la griglia. È possibile scegliere un evento appropriato anche.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-PrintingGridWeb-PrintingGridWeb.jsp" >}}

Poiché lo si chiama lato client, è necessario prima ottenere l'id client di gridweb. È possibile ottenere l'id client utilizzando il metodo gridweb.getClientID().

### **Codice di Esempio Lato Client**

Si prega di consultare il seguente link che chiama il metodo gridweb.print() lato client.

**HTML**

{{< highlight java >}}

 <a href="#" onclick='<%=gridweb.getClientID()%>.print(); '>Print Function of GridWeb</a>

{{< /highlight >}}

## **Introduzione alle Diverse Modalità di Griglia**

Questo articolo descrive le diverse modalità di Aspose.Cells.GridWeb. Queste modalità sono differenziate logicamente a causa delle loro diverse funzionalità e comportamenti. Abbiamo identificato diversi tipi di modalità come:

- Modalità di modifica
- Modalità di visualizzazione

Tutte queste modalità hanno le proprie caratteristiche. Gli sviluppatori possono lavorare con Aspose.Cells.GridWeb in qualsiasi modalità in base alle loro esigenze. Vedremo ciascuna modalità di seguito.

### **Modalità di modifica**

Per impostazione predefinita, il controllo Aspose.Cells.GridWeb è in modalità di modifica. In modalità di modifica, è possibile modificare completamente il contenuto della griglia utilizzando tutte le funzionalità offerte dal controllo Aspose.Cells.GridWeb. Queste funzionalità includono:

- Salvataggio del contenuto della griglia nei file di Microsoft Excel.
- Invio dei dati a un server.
- Calcolo delle formule.
- Annullamento o eliminazione delle azioni precedenti.
- Gestione delle righe e delle colonne.
- Taglio, copia o incolla dei dati.
- Formattazione delle celle, ecc.

**Controllo GridWeb in modalità di modifica**

![todo:image_alt_text](working-with-gridweb_9.png)

Gli sviluppatori possono anche passare alla modalità di modifica tramite programmazione impostando la proprietà EditMode del controllo GridWeb su true.

### **Esempio di codice**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebEditMode-GridWebEditMode.jsp" >}}

### **Modalità di visualizzazione**

Quando il controllo GridWeb si trova in modalità di visualizzazione, gli utenti non possono modificare il contenuto della griglia, il che significa che gli utenti possono solo visualizzare il contenuto della griglia. Ecco perché questa modalità si chiama modalità di visualizzazione. In modalità di visualizzazione, alcuni pulsanti (**Invia**, **Salva** e **Annulla**) sono nascosti e il menu che appare quando si fa clic con il pulsante destro del mouse contiene solo l'opzione **Copia** e **Trova**.

**Controllo GridWeb in modalità di visualizzazione** 

![todo:image_alt_text](working-with-gridweb_10.png)

Se gli sviluppatori desiderano che i loro utenti visualizzino solo i dati, possono passare alla modalità di visualizzazione tramite programmazione impostando la proprietà EditMode del controllo GridWeb su **false**.

### **Esempio di codice**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebViewMode-GridWebViewMode.jsp" >}}

{{% alert color="primary" %}}

Anche in modalità di visualizzazione, gli utenti possono modificare l'altezza e la larghezza delle righe e delle colonne.

{{% /alert %}}
