---
title: Licenza
type: docs
weight: 120
url: /it/net/licensing/
description: Aspose.Cells for .NET fornisce diversi piani di acquisto o offre una prova gratuita e una licenza temporanea di 30 giorni per la valutazione utilizzando le politiche di licenza e abbonamento in C#.
keywords: C# Applicare Licenza da Disco o Stream. C# Impostare Licenza da Disco o Stream. Applicare Licenza in Aspose.Cells for NET.
---

## **Come applicare una licenza nel componente Aspose.Cells**

La licenza è un file XML in testo semplice che contiene dettagli come il nome del prodotto, il numero di sviluppatori a cui è concessa la licenza, la data di scadenza dell'abbonamento e così via. Il file è firmato digitalmente, quindi non modificarlo. Anche l'aggiunta accidentale di un'interruzione di riga extra nel file lo renderà non valido. È necessario impostare una licenza prima di utilizzare Aspose.Cells se si desidera evitare le limitazioni della valutazione. È necessario impostare una licenza solo una volta per applicazione (o processo). La licenza può essere caricata da un file, da uno stream o da una risorsa incorporata.

Aspose.Cells cerca la licenza nei seguenti luoghi:

- Percorso esplicito
- La cartella che contiene Aspose.Cells.dll
- La cartella che contiene l'assembly che ha chiamato Aspose.Cells.dll
- La cartella che contiene l'assembly di ingresso (il tuo .exe)
- Una risorsa integrata nell'assembly che ha chiamato Aspose.Cells.dll

Ci sono due metodi comuni per applicare una licenza, da file o stream, o come risorsa integrata.

### **Come applicare una licenza da disco o stream**

Il modo più semplice per impostare una licenza è mettere il file di licenza nella stessa cartella dell'Aspose.Cells.dll e specificare solo il nome del file senza il percorso.

{{< highlight csharp >}}

 //Instantiate an instance of license and set the license file through its path

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

Quando si chiama il metodo SetLicense, il nome della licenza dovrebbe essere lo stesso del tuo file di licenza. Ad esempio, è possibile modificare il nome del file di licenza in **Aspose.Cells.lic.xml**. Quindi nel codice, si dovrebbe utilizzare il nome della licenza modificato (**Aspose.Cells.lic.xml**) per il metodo SetLicense.

{{% /alert %}}

È anche possibile caricare una licenza da uno stream.

{{< highlight csharp >}}

 //Instantiate an instance of license and set the license through a stream

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense(myStream);

{{< /highlight >}}

### **Come Applicare una Licenza Metered**

Aspose.Cells consente ai developer di applicare una chiave metered. Si tratta di un nuovo meccanismo di licenza. Il nuovo meccanismo di licenza sarà utilizzato insieme al metodo di licenza esistente. I clienti che desiderano essere fatturati in base all'uso delle funzionalità API possono utilizzare la licenza metered. Per ulteriori dettagli, consulta la sezione [FAQ sulla Licenza Metered](https://purchase.aspose.com/faqs/licensing/metered).  

Una nuova classe [Metered](https://reference.aspose.com/cells/net/aspose.cells/metered) è stata introdotta per applicare la chiave misurata. Di seguito è riportato il codice di esempio che mostra come impostare la chiave pubblica e privata misurata.

{{< highlight csharp >}}

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

### **Come usare una risorsa integrata**

Un altro modo intelligente di includere la licenza con la tua applicazione e assicurarti che non venga persa, è includerla come risorsa integrata in uno degli assembly che chiama Aspose.Cells. Per includere il file di licenza come risorsa integrata, eseguire i seguenti passaggi:

1. In Visual Studio .NET, includere il file di licenza (.lic) nel progetto selezionando **Aggiungi elemento esistente** dal menu **File**.
1. Selezionare il file in Esplora soluzioni e impostare **Azione di compilazione** su **Risorsa integrata** nella finestra delle Proprietà

Per accedere alla licenza incorporata nell'assembly (come risorsa integrata), non è necessario chiamare i metodi GetExecutingAssembly e GetManifestResourceStream della classe System.Reflection.Assembly di Microsoft .NET Framework. Tutto ciò che è necessario fare è solo aggiungere il file di licenza come risorsa integrata al tuo progetto e passare il nome del file di licenza al metodo SetLicense. La classe **Aspose.Cells.License** troverà automaticamente il file di licenza nelle risorse incorporate. Si prega di esaminare l'esempio riportato di seguito per comprendere questo metodo di impostazione della licenza (incorporata) nelle tue applicazioni.

{{< highlight csharp >}}

 //Instantiate the License class

Aspose.Cells.License license = new Aspose.Cells.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

## **Come impostare la licenza nei controlli griglia di Aspose.Cells**

Nella suite di griglie Aspose.Cells, la licenza può essere caricata da un file, uno stream o una risorsa integrata. Aspose.Cells.GridDesktop / Aspose.Cells.GridWeb cerca la licenza nei seguenti percorsi:

1. Percorso esplicito
1. La cartella che contiene il dll del componente (inclusa in Aspose.Cells.GridDesktop o Aspose.Cells.GridWeb)
1. La cartella che contiene l'assembly che ha chiamato il dll del componente (inclusa in Aspose.Cells.GridDesktop o Aspose.Cells.GridWeb)
1. La cartella che contiene l'assembly di ingresso (il tuo .exe)
1. Una risorsa integrata nell'assembly che ha chiamato il dll del componente (inclusa in Aspose.Cells.GridDesktop o Aspose.Cells.GridWeb)

{{% alert color="primary" %}}

Se stai utilizzando il controllo Aspose.Cells.GridDesktop, la classe di licenza utilizzata sarà Aspose.Cells.GridDesktop.License, ma se stai utilizzando il controllo Aspose.Cells.GridWeb, verrà utilizzata la classe Aspose.Cells.GridWeb.License per impostare la licenza.

{{% /alert %}}

### **Come applicare una licenza da disco o stream**

Il modo più semplice per impostare una licenza è mettere il file di licenza nella stessa cartella del dll del componente (incluso in Aspose.Cells.GridWeb) e specificare solo il nome del file senza il percorso.

{{< highlight csharp >}}

//Instantiate an instance of license and set the license file through its path

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense("MyLicense.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

Quando si chiama il metodo SetLicense, il nome della licenza deve essere lo stesso del tuo file di licenza. Ad esempio, è possibile modificare il nome del file di licenza in "MyLicense.lic.xml". Quindi nel tuo codice, dovresti usare il nome della licenza modificata (cioè MyLicense.lic.xml) per il metodo SetLicense.

{{% /alert %}}

È anche possibile caricare una licenza da uno stream.

{{< highlight csharp >}}

//Instantiate an instance of license and set the license through a stream

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense(myStream);

{{< /highlight >}}

### **Come Applicare una Licenza come Risorsa Incorporata**

Un altro metodo pratico per incapsulare la licenza con la tua applicazione e assicurarti che non venga persa, è includerla come risorsa incorporata in uno dei moduli che richiama il dll del componente (incluso in Aspose.Cells.GridDesktop). Per includere il file di licenza come risorsa incorporata, esegui i seguenti passaggi:

1. In Visual Studio .NET, includi il file di licenza (.lic) nel progetto utilizzando l'opzione **Aggiungi Elemento Esistente** nel menu **File**.
1. Seleziona il file nell'Esplora soluzioni e imposta l'azione di compilazione su Risorsa Incorporata nella finestra delle Proprietà.
1. Per accedere alla licenza incorporata nel modulo (come risorsa incorporata), non è necessario richiamare i metodi GetExecutingAssembly e GetManifestResourceStream della classe System.Reflection.Assembly di Microsoft .NET Framework. Invece, aggiungi il file di licenza come risorsa incorporata nel tuo progetto e passa il nome del file di licenza al metodo SetLicense. La classe License trova automaticamente il file di licenza nelle risorse incorporate.

Si prega di esaminare l'esempio riportato di seguito per comprendere questo metodo di applicazione di una licenza come risorsa incorporata alle tue applicazioni.

{{< highlight csharp >}}

 //Instantiate the License class

Aspose.Cells.GridDesktop.License license = new Aspose.Cells.GridDesktop.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Total.lic");

{{< /highlight >}}

## **Come Applicare una Licenza in Aspose.Cells.GridDesktop per un'applicazione WinForm**

Si consiglia di inserire il codice di licenza prima dell'avvio dell'applicazione e applicarlo solo una volta. Ad esempio, per un'applicazione Windows in C#, inserire il codice di licenza nel metodo Main.

{{< highlight csharp >}}

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

## **Note sull'Applicazione di una Licenza in Aspose.Cells.GridWeb**

Si consiglia di inserire il codice di licenza nel file Global.asax.cs della tua applicazione web (il file di licenza è presumibilmente situato sul drive " d:\ ").

{{< highlight csharp >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(@"d:\Aspose.Cells.GridWeb.lic.xml");

}

{{< /highlight >}}

Caricamento di una Licenza da uno Stream

{{< highlight csharp >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(myStream);

}

{{< /highlight >}}
