---
title: Licensing
type: docs
weight: 120
url: /it/net/licensing/
description: Aspose.Cells for .NET fornisce diversi piani di acquisto o offre una prova gratuita e una licenza temporanea di 30 giorni per la valutazione utilizzando Licensing e le politiche di abbonamento in C#.
keywords: C# Apply License from Disk or Stream. C# Set License from Disk or Stream. Apply License in Aspose.Cells for NET.
---
##  **Come applicare una licenza nel componente Aspose.Cells**

La licenza è un file XML di testo semplice che contiene dettagli come il nome del prodotto, il numero di sviluppatori a cui è concessa la licenza, la data di scadenza dell'abbonamento e così via. Il file è firmato digitalmente, quindi non modificare il file. Anche l'aggiunta involontaria di un'interruzione di riga aggiuntiva nel file lo invaliderà. È necessario impostare una licenza prima di utilizzare Aspose.Cells se si desidera evitare la limitazione della valutazione. È necessario impostare una licenza solo una volta per applicazione (o processo). La licenza può essere caricata da un file, un flusso o una risorsa incorporata.

Aspose.Cells tenta di trovare la licenza nelle seguenti posizioni:

- Percorso esplicito
- La cartella che contiene Aspose.Cells.dll
- La cartella che contiene l'assembly che ha chiamato Aspose.Cells.dll
- La cartella che contiene l'assembly della voce (il tuo .exe)
- Una risorsa incorporata nell'assembly che ha chiamato Aspose.Cells.dll

Esistono due metodi comuni per applicare una licenza: da file o flusso o come risorsa incorporata.

###  **Come applicare una licenza da disco o flusso**

Il modo più semplice per impostare una licenza è inserire il file di licenza nella stessa cartella di Aspose.Cells.dll e specificare solo il nome del file senza il percorso.

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license file through its path

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

Quando chiami il metodo SetLicense, il nome della licenza deve essere uguale a quello del file di licenza. Ad esempio, puoi modificare il nome del file di licenza in *Aspose.Cells.lic.xml**. Quindi nel codice dovresti utilizzare il nome della licenza modificata (**Aspose.Cells.lic.xml**) per il metodo SetLicense.

{{% /alert %}}

È anche possibile caricare una licenza da uno stream.

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license through a stream

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense(myStream);

{{< /highlight >}}

###  **Come applicare la licenza a consumo**

Aspose.Cells consente agli sviluppatori di applicare la chiave a consumo. Si tratta di un nuovo meccanismo di concessione delle licenze. Il nuovo meccanismo di licenza verrà utilizzato insieme al metodo di licenza esistente. I clienti che desiderano ricevere una fattura in base all'utilizzo delle funzionalità API possono utilizzare la licenza a consumo. Per ulteriori dettagli, fare riferimento a[Con tassametro Licensing FAQ](https://purchase.aspose.com/faqs/licensing/metered)sezione.

Una nuova classe[Misurato](https://reference.aspose.com/cells/net/aspose.cells/metered)è stato introdotto per applicare la chiave misurata. Di seguito è riportato il codice di esempio che mostra come impostare la chiave pubblica e privata misurata.

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

###  **Come utilizzare una risorsa incorporata**

Un altro modo efficace per comprimere la licenza con l'applicazione e assicurarsi che non vada persa è includerla come risorsa incorporata in uno degli assembly che chiama Aspose.Cells. Per includere il file di licenza come risorsa incorporata, eseguire i seguenti passaggi :

1.  In Visual Studio .NET includere il file di licenza (.lic) nel progetto selezionandolo**Aggiungi elemento esistente** dal**File** menù.
1.  Selezionare il file in Solution Explorer e impostare**Costruisci azione** A**Risorsa incorporata** nella finestra Proprietà

Per accedere alla licenza incorporata nell'assembly (come risorsa incorporata), non è necessario chiamare i metodi GetExecutingAssembly e GetManifestResourceStream della classe System.Reflection.Assembly di Microsoft .NET Framework. Tutto quello che devi fare è semplicemente aggiungere il file di licenza come risorsa incorporata al tuo progetto e passare il nome del file di licenza nel metodo SetLicense. IL**Aspose.Cells.License** class troverà automaticamente il file di licenza nelle risorse incorporate. Si prega di rivedere l'esempio fornito di seguito per comprendere questo metodo di impostazione della licenza (incorporata) nelle proprie applicazioni.

{{< highlight "csharp" >}}

 //Instantiate the License class

Aspose.Cells.License license = new Aspose.Cells.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

##  **Come impostare la licenza nei controlli della griglia Aspose.Cells**

In Aspose.Cells Grid Suite, la licenza può essere caricata da un file, stream o una risorsa incorporata. Aspose.Cells.GridDesktop / Aspose.Cells.GridWeb tenta di trovare la licenza nelle seguenti posizioni:

1. Percorso esplicito
1. La cartella che contiene la dll del componente (compresa in Aspose.Cells.GridDesktop o Aspose.Cells.GridWeb)
1. La cartella che contiene l'assembly che ha chiamato la dll del componente (incluso in Aspose.Cells.GridDesktop o Aspose.Cells.GridWeb)
1. La cartella che contiene l'assembly della voce (il tuo .exe)
1. Una risorsa incorporata nell'assembly che ha chiamato la dll del componente (inclusa in Aspose.Cells.GridDesktop o Aspose.Cells.GridWeb)

{{% alert color="primary" %}}

Se si utilizza il controllo Aspose.Cells.GridDesktop, la classe di licenza verrà utilizzata come Aspose.Cells.GridDesktop.License, ma se si utilizza il controllo Aspose.Cells.GridWeb, per impostare la licenza verrà utilizzata la classe Aspose.Cells.GridWeb.License.

{{% /alert %}}

###  **Come applicare una licenza da disco o flusso**

Il modo più semplice per impostare una licenza è mettere il file di licenza nella stessa cartella della dll del componente (inclusa in Aspose.Cells.GridWeb) e specificare solo il nome del file senza il suo percorso.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license file through its path

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense("MyLicense.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

Quando chiami il metodo SetLicense, il nome della licenza deve essere uguale a quello del file di licenza. Ad esempio, puoi modificare il nome del file di licenza in "MyLicense.lic.xml". Quindi nel tuo codice dovresti utilizzare il nome della licenza modificata (ovvero MyLicense.lic.xml) per il metodo SetLicense.

{{% /alert %}}

È anche possibile caricare una licenza da uno stream.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license through a stream

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense(myStream);

{{< /highlight >}}

###  **Come applicare una licenza come risorsa incorporata**

Un altro modo accurato per confezionare la licenza con la tua applicazione e assicurarti che non vada persa, è includerla come risorsa incorporata in uno degli assembly che chiama la dll del componente (incluso in Aspose.Cells.GridDesktop). Per includere il file di licenza come risorsa incorporata, effettuare le seguenti operazioni:

1.  In Visual Studio .NET includere il file di licenza (.lic) nel progetto utilizzando l'estensione**Aggiungi elemento esistente** opzione su**File** menù.
1. Selezionare il file in Esplora soluzioni e impostare Azione di compilazione su Risorsa incorporata nella finestra Proprietà.
1. Per accedere alla licenza incorporata nell'assembly (come risorsa incorporata), non è necessario chiamare i metodi GetExecutingAssembly e GetManifestResourceStream della classe System.Reflection.Assembly di Microsoft .NET Framework. Aggiungi invece il file di licenza come risorsa incorporata nel tuo project e passare il nome del file di licenza nel metodo SetLicense. La classe License trova automaticamente il file di licenza nelle risorse incorporate.

Ti preghiamo di rivedere l'esempio fornito di seguito per comprendere questo metodo di applicazione di una licenza come risorsa incorporata alle tue applicazioni.

{{< highlight "csharp" >}}

 //Instantiate the License class

Aspose.Cells.GridDesktop.License license = new Aspose.Cells.GridDesktop.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Total.lic");

{{< /highlight >}}

##  **Come applicare una licenza in Aspose.Cells.GridDesktop per un'applicazione WinForm**

Si consiglia di inserire il codice di licenza prima dell'avvio dell'applicazione e di applicarlo solo una volta. Ad esempio, per un'applicazione Windows C#, inserisci il codice di licenza nel metodo Main.

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

##  **Note sull'applicazione di una licenza in Aspose.Cells.GridWeb**

Si consiglia di inserire il codice di licenza nel Global.asax.cs della tua applicazione web (si presuppone che questo file di licenza sia inserito nell'unità " d:\ "):

{{< highlight "csharp" >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(@"d:\Aspose.Cells.GridWeb.lic.xml");

}

{{< /highlight >}}

Caricamento di una licenza da uno stream

{{< highlight "csharp" >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(myStream);

}

{{< /highlight >}}
