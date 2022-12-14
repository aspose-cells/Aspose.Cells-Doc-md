---
title: Licenza
type: docs
weight: 120
url: /it/net/licensing/
---
{{% alert color="primary" %}}

 Puoi facilmente scaricare una versione di valutazione di Aspose.Cells dal suo[pagina di download](https://www.nuget.org/packages/Aspose.Cells) @ NuGet repos. La versione di valutazione offre assolutamente le stesse funzionalità della versione con licenza del componente. Inoltre, la versione di valutazione diventa semplicemente concessa in licenza quando acquisti una licenza e aggiungi un paio di righe di codice per applicare la licenza.

{{% /alert %}}

## **Limiti della versione di valutazione**

La versione di valutazione del prodotto Aspose.Cells (senza una licenza specificata) fornisce funzionalità complete del prodotto, ma è limitata all'apertura di 100 file in un programma e un foglio di lavoro aggiuntivo con filigrana di valutazione.

Le limitazioni sono mostrate di seguito:

- **Numero di file aperti** (Aspose.Cells)
Quando si esegue il programma, è possibile aprire solo 100 file Excel utilizzando la libreria Aspose.Cells. Se la tua applicazione supera questo numero, verrà generata un'eccezione.
- **Impostazioni del file di configurazione** (Aspose.Cells.GridWeb)
 Non è possibile specificare nuovamente il percorso dello script aggiungendo le seguenti righe di codice nella sezione di configurazione (ad esempio nel file web.config). Il acw_client è una cartella che contiene i file e Aspose.Cells.GridWeb utilizza questa cartella per gestire la sua configurazione interna, ha file di script, file immagine e altri file per specificare il comportamento di GridWeb e impostare altre operazioni. Il file di configurazione viene utilizzato per impedire al controllo di utilizzare le risorse client incorporate (immagini, script, ecc.) che è utile in alcuni casi/scenari. Inoltre, queste impostazioni di configurazione nel file web.config avranno effetto solo con la versione CON LICENZA del controllo.

**XML**

{{< highlight "csharp" >}}

 <appSettings>

<add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

<add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>

{{< /highlight >}}

{{% alert color="primary" %}}

Queste impostazioni potrebbero essere obbligatorie in alcuni casi/scenari se si utilizza il controllo Aspose.Cells.GridWeb nei siti Web del file system o nelle estensioni MS Ajax ecc.

{{% /alert %}}

Inoltre, un foglio di lavoro con filigrana di valutazione verrà sempre visualizzato come foglio di lavoro attivo nel file excel generato utilizzando la libreria Aspose.Cells. Solo nella versione con licenza, puoi impostare il foglio di lavoro attivo su altri fogli di lavoro. Nel file PDF o immagine di output di Aspose.Cells, una filigrana di valutazione verrà incollata nella parte superiore del documento/immagine. (alla fine nelle schede del foglio di lavoro) nel controllo.

{{% alert color="primary" %}}

 Se vuoi testare Aspose.Cells senza limitazioni della versione di valutazione, puoi anche richiedere a[Licenza temporanea di 30 giorni](https://purchase.aspose.com/temporary-license).

{{% /alert %}}

## **Applicazione di una licenza nel componente Aspose.Cells**

La licenza è un file XML di testo semplice che contiene dettagli come il nome del prodotto, il numero di sviluppatori a cui è concesso in licenza, la data di scadenza dell'abbonamento e così via. Il file è firmato digitalmente, quindi non modificarlo. Anche l'aggiunta involontaria di un'ulteriore interruzione di riga nel file lo invaliderà. È necessario impostare una licenza prima di utilizzare Aspose.Cells se si desidera evitare la sua limitazione di valutazione. È necessario impostare una licenza solo una volta per applicazione (o processo). La licenza può essere caricata da un file, un flusso o una risorsa incorporata.

Aspose.Cells cerca di trovare la licenza nelle seguenti posizioni:

- Percorso esplicito
- La cartella che contiene Aspose.Cells.dll
- La cartella che contiene l'assembly che ha chiamato Aspose.Cells.dll
- La cartella che contiene l'assembly della voce (il tuo .exe)
- Una risorsa incorporata nell'assembly che ha chiamato Aspose.Cells.dll

Esistono due metodi comuni per applicare una licenza, da file o flusso o come risorsa incorporata.

### **Applicazione di una licenza da disco o flusso**

Il modo più semplice per impostare una licenza è inserire il file di licenza nella stessa cartella di Aspose.Cells.dll e specificare solo il nome del file senza il relativo percorso.

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license file through its path

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

 Quando si chiama il metodo SetLicense, il nome della licenza deve essere uguale a quello del nome del file della licenza. Ad esempio, è possibile modificare il nome del file di licenza in**Aspose.Cells.lic.xml**. Quindi nel tuo codice, dovresti usare il nome della licenza modificata (**Aspose.Cells.lic.xml**) per il metodo SetLicense.

{{% /alert %}}

È anche possibile caricare una licenza da un flusso.

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license through a stream

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense(myStream);

{{< /highlight >}}

### **Applicazione della licenza misurata**

Aspose.Cells consente agli sviluppatori di applicare la chiave misurata. È un nuovo meccanismo di licenza. Il nuovo meccanismo di licenza verrà utilizzato insieme al metodo di licenza esistente. I clienti che desiderano essere fatturati in base all'utilizzo delle funzionalità API possono utilizzare le licenze a consumo. Per maggiori dettagli, fare riferimento a[Domande frequenti sulle licenze misurate](https://purchase.aspose.com/faqs/licensing/metered)sezione.

Una nuova classe[Misurato](https://reference.aspose.com/cells/net/aspose.cells/metered)è stato introdotto per applicare la chiave misurata. Di seguito è riportato il codice di esempio che illustra come impostare la chiave pubblica e privata misurata.

{{< highlight "csharp" >}}

 //Set metered public and private keys

Metered metered = new Metered();

//Access the setMeteredKey property and pass public and private keys as parameters

metered.SetMeteredKey("*************", "*************");

//Instantiate a new Workbook

Workbook workbook = new Workbook();

//Check if the license is set

Console.WriteLine(workbook.IsLicensed);

//Get the Consumption quantity

decimal amountBefore = Metered.GetConsumptionQuantity();

Console.WriteLine(amountBefore);

Workbook workbook2 = new Workbook("e:\\test2\\Book1.xlsx");

workbook2.Save("e:\\test2\\out1.xlsx");

//Since uploading data is already running on another thread, so you might need to wait for some time (optional)

System.Threading.Thread.Sleep(10000);

//Get the Consumption quantity again which should be greater a bit

decimal amountAfter = Metered.GetConsumptionQuantity();

Console.WriteLine(amountAfter);

{{< /highlight >}}

### **Utilizzo di una risorsa incorporata**

Un altro modo accurato per impacchettare la licenza con la tua applicazione e assicurarti che non vada persa, è includerla come risorsa incorporata in uno degli assembly che chiama Aspose.Cells. Per includere il file di licenza come risorsa incorporata, procedi come segue :

1.  In Visual Studio .NET includere il file di licenza (.lic) nel progetto mediante selezione**Aggiungi elemento esistente** dal**File** menù.
1. Seleziona il file in Esplora soluzioni e imposta**Costruisci Azione** a**Risorsa incorporata** nella finestra Proprietà

 Per accedere alla licenza incorporata nell'assembly (come risorsa incorporata), non è necessario chiamare i metodi GetExecutingAssembly e GetManifestResourceStream della classe System.Reflection.Assembly del Framework Microsoft .NET. Tutto quello che devi fare è semplicemente aggiungere il file di licenza come risorsa incorporata al tuo progetto e passare il nome del file di licenza nel metodo SetLicense. Il**Aspose.Cells.License** class troverà automaticamente il file di licenza nelle risorse incorporate. Si prega di rivedere l'esempio fornito di seguito per comprendere questo metodo di impostazione della licenza (incorporata) nelle applicazioni.

{{< highlight "csharp" >}}

 //Instantiate the License class

Aspose.Cells.License license = new Aspose.Cells.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

## **Impostazione della licenza in Aspose.Cells Grid Controls**

In Aspose.Cells Grid Suite, la licenza può essere caricata da un file, un flusso o una risorsa incorporata. Aspose.Cells.GridDesktop / Aspose.Cells.GridWeb tenta di trovare la licenza nelle seguenti posizioni:

1. Percorso esplicito
1. La cartella che contiene la dll del componente (contenuta in Aspose.Cells.GridDesktop o Aspose.Cells.GridWeb)
1. La cartella che contiene l'assembly che ha chiamato la dll del componente (inclusa in Aspose.Cells.GridDesktop o Aspose.Cells.GridWeb)
1. La cartella che contiene l'assembly della voce (il tuo .exe)
1. Una risorsa incorporata nell'assembly che ha chiamato la dll del componente (inclusa in Aspose.Cells.GridDesktop o Aspose.Cells.GridWeb)

{{% alert color="primary" %}}

Se si utilizza il controllo Aspose.Cells.GridDesktop, la classe di licenza verrà utilizzata come Aspose.Cells.GridDesktop.License, ma se si utilizza il controllo Aspose.Cells.GridWeb, verrà utilizzata la classe Aspose.Cells.GridWeb.License per impostare la licenza.

{{% /alert %}}

### **Applicazione di una licenza da disco o flusso**

Il modo più semplice per impostare una licenza è mettere il file della licenza nella stessa cartella della dll del componente (contenuta in Aspose.Cells.GridWeb) e specificare solo il nome del file senza il suo percorso.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license file through its path

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense("MyLicense.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

Quando si chiama il metodo SetLicense, il nome della licenza deve essere uguale a quello del nome del file della licenza. Ad esempio, è possibile modificare il nome del file di licenza in "MyLicense.lic.xml". Quindi, nel tuo codice, dovresti usare il nome della licenza modificata (ovvero MyLicense.lic.xml) per il metodo SetLicense.

{{% /alert %}}

È anche possibile caricare una licenza da un flusso.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license through a stream

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense(myStream);

{{< /highlight >}}

### **Applicazione di una licenza come risorsa incorporata**

Un altro modo accurato per impacchettare la licenza con la tua applicazione e assicurarti che non vada persa, è includerla come risorsa incorporata in uno degli assembly che chiama la dll del componente (inclusa in Aspose.Cells.GridDesktop). Per includere il file di licenza come risorsa incorporata, attenersi alla seguente procedura:

1.  In Visual Studio .NET includere il file di licenza (.lic) nel progetto utilizzando l'estensione**Aggiungi elemento esistente** opzione sul**File** menù.
1. Selezionare il file in Solution Explorer e impostare Build Action su Embedded Resource nella finestra Properties.
1. Per accedere alla licenza incorporata nell'assembly (come risorsa incorporata), non è necessario chiamare i metodi GetExecutingAssembly e GetManifestResourceStream della classe System.Reflection.Assembly del Framework Microsoft .NET. Aggiungere invece il file della licenza come risorsa incorporata nel proprio project e passare il nome del file di licenza nel metodo SetLicense. La classe License trova automaticamente il file di licenza nelle risorse incorporate.

Si prega di rivedere l'esempio fornito di seguito per comprendere questo metodo di applicazione di una licenza come risorsa incorporata alle applicazioni.

{{< highlight "csharp" >}}

 //Instantiate the License class

Aspose.Cells.GridDesktop.License license = new Aspose.Cells.GridDesktop.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Total.lic");

{{< /highlight >}}

## **Applicazione di una licenza in Aspose.Cells.GridDesktop per un'applicazione WinForm**

Si consiglia di inserire il codice di licenza prima dell'avvio dell'applicazione e di applicarlo una sola volta. Ad esempio, per un'applicazione Windows C#, inserire il codice di licenza nel metodo Main.

{{< highlight "csharp" >}}

public class Form1 : System.Windows.Forms.Form

{

private Aspose.Cells.GridDesktop.GridDesktop gridDesktop1;

/// <summary>

/// Required designer variable.

/// </summary>

private System.ComponentModel.Container components = null;

public Form1()

{

//

// Required for Windows Form Designer support

//

InitializeComponent();

//

// TODO: Add any constructor code after InitializeComponent call

//

}

/// The main entry point for the application.

/// </summary>

.

.

.

.

[STAThread]

static void Main()

{

Aspose.Cells.GridDesktop.License lic = new Aspose.Cells.GridDesktop.License();

//Use this line if you are using an explicit path for the license file.

lic.SetLicense(@"C:\MyLicense.lic");

//Or use the line below if you are using the license file as an embedded resource.

//lic.SetLicense("MyLicense.lic");

Application.Run(new Form1());

}

private void Form1_Load(object sender, System.EventArgs e)

{

Aspose.Cells.GridDesktop.Worksheet sheet = this.gridDesktop1.Worksheets.Add("MySheet");

sheet.Cells["A1"].SetCellValue("Hello");

gridDesktop1.ActiveSheetIndex = 1;

}

}

{{< /highlight >}}

## **Note sull'applicazione di una licenza in Aspose.Cells.GridWeb**

Si consiglia di inserire il codice di licenza in Global.asax.cs dell'applicazione Web (si presume che questo file di licenza sia inserito nell'unità " d:\ "):

{{< highlight "csharp" >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(@"d:\Aspose.Cells.GridWeb.lic.xml");

}

{{< /highlight >}}

Caricamento di una licenza da un flusso

{{< highlight "csharp" >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(myStream);

}

{{< /highlight >}}
