---
title: Licensing
type: docs
weight: 120
url: /de/net/licensing/
description: Aspose.Cells for .NET bietet verschiedene Kaufpläne oder eine kostenlose Testversion und eine 30-tägige temporäre Lizenz zur Evaluierung unter Verwendung von Licensing und Abonnementrichtlinien in C#.
keywords: C# Apply License from Disk or Stream. C# Set License from Disk or Stream. Apply License in Aspose.Cells for NET.
---
##  **So beantragen Sie eine Lizenz in der Komponente Aspose.Cells**

Die Lizenz ist eine reine XML-Textdatei, die Details wie den Produktnamen, die Anzahl der Entwickler, an die sie lizenziert ist, das Ablaufdatum des Abonnements usw. enthält. Die Datei ist digital signiert. Ändern Sie sie daher nicht. Selbst das versehentliche Einfügen eines zusätzlichen Zeilenumbruchs in die Datei führt dazu, dass die Datei ungültig wird. Sie müssen vor der Verwendung von Aspose.Cells eine Lizenz festlegen, wenn Sie die Testbeschränkung vermeiden möchten. Es ist nur einmal erforderlich, eine Lizenz pro Anwendung (oder Prozess) festzulegen. Die Lizenz kann aus einer Datei, einem Stream oder einer eingebetteten Ressource geladen werden.

Aspose.Cells versucht, die Lizenz an den folgenden Orten zu finden:

- Expliziter Pfad
- Der Ordner, der Aspose.Cells.dll enthält
- Der Ordner, der die Assembly enthält, die Aspose.Cells.dll aufgerufen hat
- Der Ordner, der die Eintragsassembly enthält (Ihre EXE-Datei)
- Eine eingebettete Ressource in der Assembly mit dem Namen Aspose.Cells.dll

Es gibt zwei gängige Methoden zum Anwenden einer Lizenz: aus einer Datei oder einem Stream oder als eingebettete Ressource.

###  **So wenden Sie eine Lizenz von der Festplatte oder vom Stream an**

Der einfachste Weg, eine Lizenz festzulegen, besteht darin, die Lizenzdatei im selben Ordner wie die Datei Aspose.Cells.dll abzulegen und nur den Dateinamen ohne Pfad anzugeben.

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license file through its path

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

Wenn Sie die SetLicense-Methode aufrufen, sollte der Lizenzname mit dem Namen Ihrer Lizenzdatei identisch sein. Sie können beispielsweise den Namen der Lizenzdatei in *Aspose.Cells.lic.xml** ändern. Dann sollten Sie in Ihrem Code den geänderten Lizenznamen (**Aspose.Cells.lic.xml**) für die SetLicense-Methode verwenden.

{{% /alert %}}

Es ist auch möglich, eine Lizenz aus einem Stream zu laden.

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license through a stream

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense(myStream);

{{< /highlight >}}

###  **So wenden Sie eine gemessene Lizenz an**

Aspose.Cells ermöglicht Entwicklern die Anwendung eines gemessenen Schlüssels. Es handelt sich um einen neuen Lizenzierungsmechanismus. Der neue Lizenzierungsmechanismus wird zusammen mit der bestehenden Lizenzierungsmethode verwendet. Kunden, die eine Abrechnung auf Basis der Nutzung der API-Funktionen wünschen, können die getaktete Lizenzierung nutzen. Weitere Einzelheiten finden Sie unter[Metered Licensing FAQ](https://purchase.aspose.com/faqs/licensing/metered)Abschnitt.

Eine neue Klasse[Dosiert](https://reference.aspose.com/cells/net/aspose.cells/metered)wurde eingeführt, um einen dosierten Schlüssel anzuwenden. Im Folgenden finden Sie einen Beispielcode, der zeigt, wie ein gemessener öffentlicher und privater Schlüssel festgelegt wird.

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

###  **So verwenden Sie eine eingebettete Ressource**

Eine weitere praktische Möglichkeit, die Lizenz in Ihre Anwendung zu packen und sicherzustellen, dass sie nicht verloren geht, besteht darin, sie als eingebettete Ressource in eine der Assemblys einzubinden, die Aspose.Cells aufruft. Um die Lizenzdatei als eingebettete Ressource einzubinden, führen Sie die folgenden Schritte aus :

1.  Fügen Sie in Visual Studio .NET die Lizenzdatei (.lic) durch Auswahl in das Projekt ein**Vorhandenes Element hinzufügen** von dem**Datei** Speisekarte.
1.  Wählen Sie die Datei im Projektmappen-Explorer aus und legen Sie fest**Aktion erstellen** Zu**Eingebettete Ressource** im Eigenschaftenfenster

Um auf die in der Assembly eingebettete Lizenz (als eingebettete Ressource) zuzugreifen, ist es nicht erforderlich, die Methoden GetExecutingAssembly und GetManifestResourceStream der System.Reflection.Assembly-Klasse des Frameworks Microsoft .NET aufzurufen. Sie müssen lediglich die Lizenzdatei als eingebettete Ressource zu Ihrem Projekt hinzufügen und den Namen der Lizenzdatei an die SetLicense-Methode übergeben. Der**Aspose.Cells.License** Die Klasse findet die Lizenzdatei automatisch in den eingebetteten Ressourcen. Bitte sehen Sie sich das unten aufgeführte Beispiel an, um diese Methode zum Festlegen einer Lizenz (eingebettet) in Ihren Anwendungen zu verstehen.

{{< highlight "csharp" >}}

 //Instantiate the License class

Aspose.Cells.License license = new Aspose.Cells.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

##  **So legen Sie die Lizenz in Aspose.Cells Grid Controls fest**

In Aspose.Cells Grid Suite kann die Lizenz aus einer Datei, einem Stream oder einer eingebetteten Ressource geladen werden. Aspose.Cells.GridDesktop / Aspose.Cells.GridWeb versucht, die Lizenz an den folgenden Orten zu finden:

1. Expliziter Pfad
1. Der Ordner, der die DLL der Komponente enthält (enthalten in Aspose.Cells.GridDesktop oder Aspose.Cells.GridWeb)
1. Der Ordner, der die Assembly enthält, die die DLL der Komponente aufgerufen hat (enthalten in Aspose.Cells.GridDesktop oder Aspose.Cells.GridWeb)
1. Der Ordner, der die Eintragsassembly enthält (Ihre EXE-Datei)
1. Eine eingebettete Ressource in der Assembly, die die DLL der Komponente aufgerufen hat (enthalten in Aspose.Cells.GridDesktop oder Aspose.Cells.GridWeb)

{{% alert color="primary" %}}

Wenn Sie das Steuerelement Aspose.Cells.GridDesktop verwenden, wird die Lizenzklasse als Aspose.Cells.GridDesktop.License verwendet. Wenn Sie jedoch das Steuerelement Aspose.Cells.GridWeb verwenden, wird die Klasse Aspose.Cells.GridWeb.License zum Festlegen der Lizenz verwendet.

{{% /alert %}}

###  **So wenden Sie eine Lizenz von der Festplatte oder vom Stream an**

Der einfachste Weg, eine Lizenz festzulegen, besteht darin, die Lizenzdatei im selben Ordner wie die DLL der Komponente (in Aspose.Cells.GridWeb enthalten) abzulegen und nur den Dateinamen ohne Pfad anzugeben.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license file through its path

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense("MyLicense.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

Wenn Sie die SetLicense-Methode aufrufen, sollte der Lizenzname mit dem Namen Ihrer Lizenzdatei identisch sein. Sie können beispielsweise den Namen der Lizenzdatei in „MyLicense.lic.xml“ ändern. Dann sollten Sie in Ihrem Code den geänderten Lizenznamen (MyLicense.lic.xml) für die SetLicense-Methode verwenden.

{{% /alert %}}

Es ist auch möglich, eine Lizenz aus einem Stream zu laden.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license through a stream

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense(myStream);

{{< /highlight >}}

###  **So wenden Sie eine Lizenz als eingebettete Ressource an**

Eine weitere praktische Möglichkeit, die Lizenz mit Ihrer Anwendung zu verpacken und sicherzustellen, dass sie nicht verloren geht, besteht darin, sie als eingebettete Ressource in eine der Assemblys einzubinden, die die DLL der Komponente aufruft (enthalten in Aspose.Cells.GridDesktop). Um die Lizenzdatei als eingebettete Ressource einzubinden, führen Sie die folgenden Schritte aus:

1.  Fügen Sie in Visual Studio .NET die Lizenzdatei (.lic) mithilfe von in das Projekt ein**Vorhandenes Element hinzufügen** Option auf der**Datei** Speisekarte.
1. Wählen Sie die Datei im Projektmappen-Explorer aus und legen Sie im Eigenschaftenfenster die Build-Aktion auf „Eingebettete Ressource“ fest.
1. Um auf die in der Assembly eingebettete Lizenz (als eingebettete Ressource) zuzugreifen, ist es nicht erforderlich, die Methoden GetExecutingAssembly und GetManifestResourceStream der System.Reflection.Assembly-Klasse von Microsoft .NET Framework aufzurufen. Fügen Sie stattdessen die Lizenzdatei als eingebettete Ressource in Ihrem hinzu Projekt und übergeben Sie den Namen der Lizenzdatei an die SetLicense-Methode. Die License-Klasse findet die Lizenzdatei automatisch in den eingebetteten Ressourcen.

Bitte sehen Sie sich das unten aufgeführte Beispiel an, um diese Methode zum Anwenden einer Lizenz als eingebettete Ressource auf Ihre Anwendungen zu verstehen.

{{< highlight "csharp" >}}

 //Instantiate the License class

Aspose.Cells.GridDesktop.License license = new Aspose.Cells.GridDesktop.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Total.lic");

{{< /highlight >}}

##  **So wenden Sie eine Lizenz in Aspose.Cells.GridDesktop für eine WinForm-Anwendung an**

Es wird empfohlen, dass Sie Ihren Lizenzcode vor dem Start Ihrer Anwendung eingeben und ihn nur einmal anwenden. Geben Sie beispielsweise für eine Windows-Anwendung C# den Lizenzcode in die Main-Methode ein.

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

##  **Hinweise zur Beantragung einer Lizenz in Aspose.Cells.GridWeb**

Es wird empfohlen, den Lizenzcode in Global.asax.cs Ihrer Webanwendung abzulegen (es wird davon ausgegangen, dass diese Lizenzdatei auf dem Laufwerk „d:\“ abgelegt ist):

{{< highlight "csharp" >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(@"d:\Aspose.Cells.GridWeb.lic.xml");

}

{{< /highlight >}}

Laden einer Lizenz aus einem Stream

{{< highlight "csharp" >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(myStream);

}

{{< /highlight >}}
