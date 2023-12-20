---
title: Lavorare con GridWeb
type: docs
weight: 20
url: /it/java/working-with-gridweb/
---
## **Apertura di un file Excel Microsoft**

Il controllo Aspose.Cells.GridWeb può aprire e caricare Microsoft file Excel, completi di dati, formattazione, grafici, immagini e così via. Questo argomento spiega come.

Per aprire un file Excel utilizzando il controllo GridWeb:

1. Aggiungere il controllo Aspose.Cells.GridWeb a un modulo Web o una pagina.
1. Importa il file Excel specificando il percorso del file.
1. Eseguire l'applicazione o aprire la pagina.

Per caricare il contenuto da un file Excel nel controllo Aspose.Cells.GridWeb, è necessario chiamare il metodo importExcelFile per specificare il percorso del file Excel. Successivamente, il controllo GridWeb troverà automaticamente il file dal percorso specificato e ne visualizzerà il contenuto. Di seguito viene fornito uno snippet di codice che carica il contenuto di un file Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-OpeningfromFile-OpeningfromFile.jsp" >}}

Lo snippet di codice sopra può essere utilizzato come preferisci. Ad esempio, per caricare automaticamente un file Excel quando viene caricato un modulo web, aggiungi questo codice all'evento Page_Load del modulo che hai specificato tu stesso.

**Un file Excel viene caricato in GridWeb**

![cose da fare:immagine_alt_testo](working-with-gridweb_1.png)

## **Salvataggio di un file Excel Microsoft**

È possibile creare nuovi o manipolare file Excel Microsoft esistenti, su siti Web in modalità GUI utilizzando il controllo Aspose.Cells.GridWeb. I file possono quindi essere salvati in file Excel. Aspose.Cells.GridWeb funge efficacemente da editor di fogli di calcolo online. Questo argomento descrive come salvare il contenuto della griglia in file Excel.

### **Salvataggio come file**

Per salvare il contenuto del controllo Aspose.Cells.GridWeb come file Excel:

1. Aggiungere il controllo Aspose.Cells.GridWeb a un modulo Web o una pagina.
1. Salva il tuo lavoro come file Excel in un percorso specificato.
1. Eseguire l'applicazione o aprire la pagina.

L'esempio di codice seguente illustra come salvare il contenuto della griglia in un file Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-SavingasFile-SavingasFile.jsp" >}}

 Il suddetto frammento di codice può essere utilizzato in diversi modi. Un modo comune consiste nell'aggiungere un pulsante che salva il contenuto della griglia in un file Excel quando viene fatto clic. Aspose.Cells.GridWeb offre un approccio più semplice per l'attività. Aspose.Cells.GridWeb ha un evento chiamato SaveCommand. Il suddetto frammento di codice può essere aggiunto al gestore di eventi dell'evento SaveCommand che consente agli utenti di salvare il proprio lavoro facendo clic sull'opzione integrata di Aspose.Cells.GridWeb**Salva** pulsante.

## **Ridimensionamento di Aspose.Cells.GridWeb e della relativa barra dell'intestazione**

Questo articolo spiega come ridimensionare GridWeb in fase di esecuzione utilizzando Aspose.Cells.GridWeb API. Spiega inoltre come ridimensionare le barre di intestazione del controllo Aspose.Cells.GridWeb per semplificarne la lettura dei dati.

### **Modifica della larghezza e dell'altezza di Aspose.Cells.GridWeb**

Modificare la larghezza e l'altezza del controllo Aspose.Cells.GridWeb è una caratteristica semplice ma importante. Il controllo Aspose.Cells.GridWeb è rappresentato dalla classe GridWeb in API. Per ridimensionare la larghezza e l'altezza del controllo GridWeb, utilizzare semplicemente le sue proprietà width e height.

{{% alert color="primary" %}}

La larghezza e l'altezza del controllo possono essere definite in pixel o punti.

{{% /alert %}}

L'output del frammento di codice che segue è mostrato di seguito.

**Larghezza e altezza modificate del controllo GridWeb**

![cose da fare:immagine_alt_testo](working-with-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangedwidthheightofGridWebcontrol-ChangedwidthheightofGridWebcontrol.jsp" >}}

### **Modifica della larghezza e dell'altezza della barra dell'intestazione**

Aspose.Cells. Il controllo GridWeb contiene due barre di intestazione come segue:

- Barra dell'intestazione superiore, questa barra dell'intestazione rappresenta le colonne come A, B, C, D, ecc.
- Barra di intestazione sinistra, questa barra di intestazione rappresenta le righe come 1, 2, 3, 4, ecc.

Entrambe queste barre di intestazione sono mostrate di seguito.

**Barre di intestazione**

![cose da fare:immagine_alt_testo](working-with-gridweb_3.png)

Modificare l'altezza della barra dell'intestazione superiore e la larghezza della barra dell'intestazione sinistra utilizzando rispettivamente le proprietà HeaderBarHeight e HeaderBarWidth del controllo GridWeb. La figura seguente mostra l'output dell'esempio di codice che segue.

**Larghezza e altezza della barra dell'intestazione modificate**

![cose da fare:immagine_alt_testo](working-with-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-ChangingWidthandHeightofHeaderBar-ChangingWidthandHeightofHeaderBar.jsp" >}}

## **Utilizzo di Aspose.Cells.GridWeb Events**

Tutti gli sviluppatori devono avere familiarità con gli eventi e il loro scopo. Gli eventi vengono utilizzati per inviare notifiche di modifiche che possono verificarsi in un controllo o in una classe. Aspose.Cells.GridWeb ha diversi eventi che possono essere utilizzati per eseguire attività specifiche quando si verificano determinate modifiche nel controllo.

Questo argomento fornisce un'introduzione a tutti gli eventi supportati dal controllo Aspose.Cells.GridWeb insieme ad alcuni dettagli su come gestire questi eventi.

### **Introduzione agli eventi di griglia**

Aspose.Cells. Il controllo GridWeb supporta diversi eventi che forniscono un maggiore controllo per l'esecuzione di operazioni quando vengono attivati eventi specifici nel controllo. Di seguito è riportato un elenco completo degli eventi supportati dal controllo Aspose.Cells.GridWeb.

|**Eventi**|**Descrizione**|
|:- |:- |
|CellCommand|Si verifica quando si fa clic sul collegamento ipertestuale del comando di una cella. Quando questo evento viene attivato, il suo parametro e.Argument fornisce il nome del comando.|
|CellDoubleClick|Si verifica quando si fa doppio clic sulla cella.|
|Colonna eliminata|Si verifica quando un utente elimina una colonna da un foglio di lavoro utilizzando il menu lato client.|
|Eliminazione colonna|Si verifica quando un utente tenta di eliminare una colonna da un foglio di lavoro utilizzando il menu lato client.|
|ColonnaDoubleClick|Si verifica quando si fa doppio clic sull'intestazione di colonna.|
|ColonnaInserito|Si verifica quando un utente inserisce una colonna in un foglio di lavoro utilizzando il menu lato client.|
|Comando personalizzato|Si verifica quando un utente fa clic su un pulsante di comando personalizzato.|
|Carica dati personalizzati|Si verifica quando la proprietà EnableSession del controllo è impostata su false e deve caricare i dati del foglio di lavoro. È possibile gestire questo evento in modalità senza sessione per caricare i dati del foglio di lavoro da un file o da un database.|
|PageIndexModificato|Si verifica quando l'indice della pagina del foglio del controllo viene modificato.|
|Riga eliminata|Si verifica quando un utente elimina una riga dal foglio di lavoro utilizzando il menu lato client.|
|RowDeleting|Si verifica quando un utente tenta di eliminare una riga da un foglio di lavoro utilizzando il menu lato client.|
|RigaDoppio clic|Si verifica quando si fa doppio clic sull'intestazione di riga.|
|RigaInserita|Si verifica quando un utente inserisce una riga nel foglio di lavoro utilizzando il menu lato client.|
|SalvaComando| Si verifica quando il**Salva** si fa clic sul pulsante.|
|FoglioSchedaClic|Si verifica quando si fa clic su una scheda del foglio.|
|InviaComando| Si verifica quando il**Invia** si fa clic sul pulsante.|
|AnnullaComando| Si verifica quando il**Annullare** si fa clic sul pulsante.|
|Ajax CallFinished|Viene eseguito al termine dell'aggiornamento AJAX del controllo. (EnableAJAX deve essere impostato su true).|
|CellModifiedOnAjax|Si attiva quando la cella viene modificata nella chiamata AJAX.|
|DopoColumnFilter|Viene eseguito quando il filtro viene applicato a una colonna.|

### **Gestione degli eventi della griglia**

Per eseguire un'operazione specifica sull'attivazione di un evento specifico, dobbiamo creare un gestore di eventi. Un gestore di eventi esegue l'attività desiderata quando viene attivato un determinato evento. L'esempio che segue mostra come gestire un semplice evento di griglia.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HandlingGridEvents-HandlingGridEvents.jsp" >}}

## **Utilizzo degli eventi DoubleClick**

Aspose.Cells.GridWeb contiene tre tipi di eventi doppio clic:

- CellDoubleClick, attivato quando si fa doppio clic su una cella.
- ColumnDoubleClick, attivato quando si fa doppio clic sull'intestazione di una colonna.
- RowDoubleClick, attivato quando si fa doppio clic su un'intestazione di riga.

Questo argomento illustra come abilitare gli eventi di doppio clic in Aspose.Cells.GridWeb. Discute anche la creazione di gestori di eventi per questi eventi.

### **Abilitazione degli eventi doppio clic**

Tutti i tipi di eventi doppio clic possono essere abilitati sul lato client impostando la proprietà EnableDoubleClickEvent del controllo GridWeb su true.

{{% alert color="primary" %}}

Per impostazione predefinita, la proprietà EnableDoubleClickEvent è impostata su false. Ciò significa che gli eventi doppio clic non sono abilitati per impostazione predefinita. Per implementare tali eventi, abilita prima la funzione.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-EnablingDoubleClickEvents-EnablingDoubleClickEvents.jsp" >}}

Una volta abilitati gli eventi di doppio clic, è possibile creare gestori di eventi per qualsiasi evento di doppio clic. Questi gestori di eventi eseguono attività specifiche quando viene attivato un determinato evento di doppio clic.

### **Gestione degli eventi DoubleClick**

#### **Doppio clic Cell**

Il gestore eventi per l'evento CellDoubleClick fornisce un argomento del tipo CellEventArgs, che fornisce le informazioni complete della cella su cui si fa doppio clic.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickCell-DoubleClickCell.jsp" >}}

#### **Fare doppio clic sull'intestazione della colonna**

Il gestore eventi per l'evento ColumnDoubleClick fornisce un argomento del tipo RowColumnEventArgs che fornisce il numero di indice della colonna per l'intestazione su cui è stato fatto doppio clic e altre informazioni.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickColumnHeader-DoubleClickColumnHeader.jsp" >}}

#### **Fare doppio clic sull'intestazione della riga**

Il gestore eventi per l'evento RowDoubleClick fornisce un argomento del tipo RowColumnEventArgs che fornisce il numero di indice della riga per l'intestazione su cui è stato fatto doppio clic e altre informazioni correlate.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-DoubleClickRowHeader-DoubleClickRowHeader.jsp" >}}

## **Impostazione dello stile o dell'aspetto di Aspose.Cells.GridWeb**

Aspose.Cells.GridWeb ha il proprio aspetto predefinito ma è possibile modificarne l'aspetto. Aspose.Cells.GridWeb fornisce diverse proprietà per consentire agli sviluppatori di controllarne completamente l'aspetto. In questo argomento vengono illustrate alcune di queste proprietà.

### **Impostazione dello stile o dell'aspetto di Aspose.Cells.GridWeb**

#### **Stili preimpostati**

Per salvare gli sforzi degli sviluppatori, Aspose.Cells.GridWeb offre alcuni stili preimpostati. Basta selezionare uno stile dall'elenco per applicare lo stile.

|**Stili**|**Combinazione di colori**|
|:- |:- |
|Standard|Argento|
|Colorato1|Rosa|
|Colorato2|Blu|
|Professionale1|Ciano|
|Professionale2|Di nuovo ciano|
|Tradizionale1|Buio|
|Tradizionale2|Grigio|
|Costume|Personalizzato|
Quando viene selezionato uno stile particolare, cambia l'intero aspetto del controllo GridWeb. Gli sviluppatori possono selezionare uno stile preimpostato da applicare in fase di esecuzione utilizzando il flessibile API di Aspose.Cells.GridWeb.

Il controllo GridWeb fornisce la proprietà PresetStyle a cui gli sviluppatori possono assegnare qualsiasi stile preimpostato desiderato.

L'output del seguente frammento di codice è mostrato di seguito.

**Controllo GridWeb con lo stile Colorful1 applicato su di esso**

![cose da fare:immagine_alt_testo](working-with-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

#### **Stile barra di intestazione**

Se dai un'occhiata al controllo GridWeb, noterai due barre di intestazione. Uno per le colonne (ovvero A, B, C, D, ecc.) e l'altro per le righe (ovvero 1, 2, 3, 4, ecc.). Aspose.Cells.GridWeb consente agli sviluppatori di controllare l'aspetto di queste barre di intestazione. Gli sviluppatori possono impostare lo stile delle barre di intestazione in fase di esecuzione.

{{% alert color="primary" %}}

Il controllo GridWeb fornisce la proprietà HeaderBarStyle che applica uno stile a entrambe le barre di intestazione del controllo.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-Colorful1style-Colorful1style.jsp" >}}

#### **Stile barra delle schede**

È possibile impostare anche lo stile della barra delle schede. Si prega di vedere il seguente codice

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-HeaderBarStyle-HeaderBarStyle.jsp" >}}

#### **Caricamento del file di stile**

Per applicare le impostazioni di stile da un file di stile esistente al controllo GridWeb, gli sviluppatori possono impostare il percorso del file di stile sulla proprietà CustomStyleFileName del controllo. Ma, prima di farlo, è necessario impostare la proprietà PresetStyle del controllo su Custom. È perché quel file di stile contiene informazioni di stile personalizzate già definite da uno sviluppatore.

Si prega di vedere l'immagine seguente che mostra GridWeb con lo stile personalizzato applicato.

![cose da fare:immagine_alt_testo](working-with-gridweb_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-CustomStyleSheet-CustomStyleSheet.jsp" >}}

{{% alert color="primary" %}}

IMPORTANTE: il caricamento del file di stile nel controllo GridWeb non influisce sulle impostazioni di formattazione delle celle del controllo.

{{% /alert %}}

#### **Esempio di modello di stile personalizzato**

Ecco il modello di stile personalizzato di esempio. Puoi modificarlo secondo le tue esigenze.

{{< highlight "java" >}}

 <aspose.excel.web.viewerStyletemplate runat="server" HeaderBarWidth="30pt" ScrollBarBaseColor="#AFEEEE" SelectCellBgColor="#FFFAF0" ActiveHeaderBgColor="#DAA520" ActiveCellBgColor="#DDDDFF" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LeftBorderStyle-BorderWidth="" FrameTableStyle-LeftBorderStyle-BorderColor="" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-RightBorderStyle-BorderWidth="" FrameTableStyle-RightBorderStyle-BorderColor="" FrameTableStyle-BorderWidth="1px" FrameTableStyle-CellSpacing="0" FrameTableStyle-BorderColor="#C0FFC0" FrameTableStyle-CellPadding="0" FrameTableStyle-TopBorderStyle-BorderWidth="" FrameTableStyle-TopBorderStyle-BorderColor="" FrameTableStyle-BackColor="#FFFFCC" FrameTableStyle-BottomBorderStyle-BorderWidth="" FrameTableStyle-BottomBorderStyle-BorderColor="" HeaderBarStyle-LeftBorderStyle-BorderWidth="" HeaderBarStyle-LeftBorderStyle-BorderColor="" HeaderBarStyle-verticalalign="Middle" HeaderBarStyle-RightBorderStyle-BorderWidth="" HeaderBarStyle-RightBorderStyle-BorderColor="" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-font-size="10pt" HeaderBarStyle-BorderColor="#00C0C0" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-horizontalalign="Center" HeaderBarStyle-ForeColor="Red" HeaderBarStyle-TopBorderStyle-BorderWidth="" HeaderBarStyle-TopBorderStyle-BorderColor="" HeaderBarStyle-BackColor="#D8BFD8" HeaderBarStyle-BottomBorderStyle-BorderWidth="" HeaderBarStyle-BottomBorderStyle-BorderColor="" ViewTableStyle-LeftBorderStyle-BorderWidth="" ViewTableStyle-LeftBorderStyle-BorderColor="" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-RightBorderStyle-BorderWidth="" ViewTableStyle-RightBorderStyle-BorderColor="" ViewTableStyle-BorderWidth="0px" ViewTableStyle-CellSpacing="0" ViewTableStyle-CellPadding="0" ViewTableStyle-TopBorderStyle-BorderWidth="" ViewTableStyle-TopBorderStyle-BorderColor="" ViewTableStyle-BottomBorderStyle-BorderWidth="" ViewTableStyle-BottomBorderStyle-BorderColor="" BottomTableStyle-LeftBorderStyle-BorderWidth="" BottomTableStyle-LeftBorderStyle-BorderColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-RightBorderStyle-BorderWidth="" BottomTableStyle-RightBorderStyle-BorderColor="" BottomTableStyle-Height="32pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-CellSpacing="0" BottomTableStyle-BorderColor="#80FF80" BottomTableStyle-CellPadding="0" BottomTableStyle-ForeColor="#FFE0C0" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="#FF69B4" BottomTableStyle-BottomBorderStyle-BorderWidth="" BottomTableStyle-BottomBorderStyle-BorderColor="" HeaderBarHeight="15pt" ActiveTabStyle-LeftBorderStyle-BorderWidth="" ActiveTabStyle-LeftBorderStyle-BorderColor="" ActiveTabStyle-RightBorderStyle-BorderWidth="" ActiveTabStyle-RightBorderStyle-BorderColor="" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-font-size="10pt" ActiveTabStyle-BorderColor="#00C0C0" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="#FF00FF" ActiveTabStyle-TopBorderStyle-BorderWidth="" ActiveTabStyle-TopBorderStyle-BorderColor="" ActiveTabStyle-BackColor="#80FFFF" ActiveTabStyle-BottomBorderStyle-BorderWidth="" ActiveTabStyle-BottomBorderStyle-BorderColor="" HeaderBarTableStyle-LeftBorderStyle-BorderWidth="" HeaderBarTableStyle-LeftBorderStyle-BorderColor="" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-RightBorderStyle-BorderWidth="" HeaderBarTableStyle-RightBorderStyle-BorderColor="" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-CellSpacing="0" HeaderBarTableStyle-CellPadding="0" HeaderBarTableStyle-TopBorderStyle-BorderWidth="" HeaderBarTableStyle-TopBorderStyle-BorderColor="" HeaderBarTableStyle-BackColor="#C0FFC0" HeaderBarTableStyle-BottomBorderStyle-BorderWidth="" HeaderBarTableStyle-BottomBorderStyle-BorderColor="" DefaultGridLineColor="#228B22" TabStyle-LeftBorderStyle-BorderWidth="" TabStyle-LeftBorderStyle-BorderColor="" TabStyle-RightBorderStyle-BorderWidth="" TabStyle-RightBorderStyle-BorderColor="" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-font-size="8pt" TabStyle-BorderColor="#8080FF" TabStyle-BorderStyle="Groove" TabStyle-ForeColor="#FFFFCC" TabStyle-TopBorderStyle-BorderWidth="" TabStyle-TopBorderStyle-BorderColor="" TabStyle-BackColor="#C0C0FF" TabStyle-BottomBorderStyle-BorderWidth="" TabStyle-BottomBorderStyle-BorderColor="" scrollbararrowColor="#778899"/>

{{< /highlight >}}

## **Creazione di controllo su un Web Form**

Questo articolo ti guiderà su come creare un semplice modulo Web JSP (Java Server Page) con il controllo GridWeb su di esso.

**Passaggio 1: creazione di una struttura di directory**

 È necessario creare la seguente struttura di directory nel file**webapp**directory di Tomcat Server

![cose da fare:immagine_alt_testo](working-with-gridweb_7.png)

 Queste sono le directory e i file che devi creare. Si prega di leggere i commenti e seguirli. È possibile ottenere gli ultimi archivi di rilascio Aspose.Cells.GridWeb for Java da[questo link](https://downloads.aspose.com/cells/java).

{{< highlight "java" >}}

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

**Passaggio 2: aggiunta di codici nei file creati**

Questa sezione mostra il codice per vari file creati nella struttura di directory di cui sopra. Si prega di ottenere questi codici e aggiungerli nei file aprendoli in Blocco note e copiandoli/incollandoli.

**Web.xml**

{{< highlight "java" >}}

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

{{< highlight "java" >}}

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

**Passaggio 3: esecuzione della pagina Web JSP di esempio**

Ora hai fatto tutto. È tempo di eseguire la pagina web. Avvia il tuo server Tomcat e incolla il seguente URL nel browser web.

{{< highlight "java" >}}

 http://localhost:8080/SamplePageGridWebJava/SamplePage.jsp

{{< /highlight >}}

Vedrai qualcosa di simile al seguente screenshot. Congratulazioni, hai utilizzato con successo il controllo GridWeb sulla tua pagina JSP.

![cose da fare:immagine_alt_testo](working-with-gridweb_8.png)

## **Stampa GridWeb**

Ci sono momenti in cui gli sviluppatori devono stampare il contenuto GridWeb incluso da una pagina web senza salvare un file Excel Microsoft. Il controllo Aspose.Cells.GridWeb supporta questa funzionalità.

### **Stampa GridWeb**

Per stampare senza salvare un file separato, chiama il metodo print() della classe GridWeb sul lato client per stampare la griglia. Puoi anche scegliere un evento appropriato.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-PrintingGridWeb-PrintingGridWeb.jsp" >}}

Dal momento che lo stai chiamando dal lato client, dovrai prima ottenere l'ID client gridweb. È possibile ottenere l'ID client utilizzando il metodo gridweb.getClientID().

### **Codice di esempio lato client**

Si prega di vedere il seguente collegamento che chiama il metodo gridweb.print() dal lato client.

**HTML**

{{< highlight "java" >}}

 <a href="#" onclick='<%=gridweb.getClientID()%>.print(); '>Print Function of GridWeb</a>

{{< /highlight >}}

## **Introduzione alle diverse modalità di rete**

Questo articolo descrive le diverse modalità di Aspose.Cells.GridWeb. Queste modalità sono logicamente differenziate a causa delle loro diverse caratteristiche e comportamenti. Abbiamo identificato diversi tipi di modalità come:

- Modalità Modifica
- Modalità di visualizzazione

Tutte queste modalità hanno le loro caratteristiche. Gli sviluppatori possono lavorare con Aspose.Cells.GridWeb in qualsiasi modalità in base alle loro esigenze. Vedremo ciascuna modalità di seguito.

### **Modalità Modifica**

Per impostazione predefinita, il controllo Aspose.Cells.GridWeb è in modalità di modifica. In modalità Modifica è possibile modificare completamente o modificare il contenuto della griglia utilizzando tutte le funzionalità offerte dal controllo Aspose.Cells.GridWeb. Queste funzionalità includono:

- Salvataggio del contenuto della griglia nei file Excel Microsoft.
- Invio di dati a un server.
- Formule di calcolo.
- Annullamento o eliminazione di azioni precedenti.
- Gestione di righe e colonne.
- Tagliare, copiare o incollare dati.
- Formattazione delle celle ecc.

**Controllo GridWeb in modalità di modifica**

![cose da fare:immagine_alt_testo](working-with-gridweb_9.png)

Gli sviluppatori possono anche passare alla modalità di modifica a livello di codice impostando la proprietà EditMode del controllo GridWeb su true.

### **Esempio di codice**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebEditMode-GridWebEditMode.jsp" >}}

### **Modalità di visualizzazione**

Quando il controllo GridWeb è in modalità di visualizzazione, gli utenti non possono modificare o modificare il contenuto della griglia, il che significa che gli utenti possono solo visualizzare il contenuto della griglia. Ecco perché questa modalità è chiamata modalità di visualizzazione. In modalità di visualizzazione, alcuni pulsanti (**Invia**, **Salva** e**Annullare** ) sono nascosti e il menu che appare facendo clic con il pulsante destro del mouse contiene solo i file**copia** e**Trova** opzione.

**Controllo GridWeb in modalità di visualizzazione** 

![cose da fare:immagine_alt_testo](working-with-gridweb_10.png)

 Se gli sviluppatori desiderano che i propri utenti visualizzino solo i dati, possono passare alla modalità di visualizzazione a livello di codice impostando la proprietà EditMode del controllo GridWeb su**falso**.

### **Esempio di codice**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-gridweb-GridWebViewMode-GridWebViewMode.jsp" >}}

{{% alert color="primary" %}}

Anche in modalità di visualizzazione, gli utenti possono modificare l'altezza e la larghezza di righe e colonne.

{{% /alert %}}
