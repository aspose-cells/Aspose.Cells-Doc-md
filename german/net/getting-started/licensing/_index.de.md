---
title: Lizenzierung
type: docs
weight: 120
url: /de/net/licensing/
description: Aspose.Cells for .NET bietet verschiedene Pläne zum Kauf oder bietet eine kostenlose Testversion und eine 30 tägige temporäre Lizenz zur Evaluierung mithilfe von Lizenzierungs und Abonnementrichtlinien in C#.
keywords: C# Lizenz von Festplatte oder Stream anwenden. C# Lizenz von Festplatte oder Stream setzen. Lizenz in Aspose.Cells for NET anwenden.
---

## **Wie man eine Lizenz in Aspose.Cells-Komponente anwendet**

Die Lizenz ist eine einfache XML-Textdatei, die Details wie den Produktnamen, die Anzahl der lizenzierten Entwickler, das Ablaufdatum des Abonnements usw. enthält. Die Datei ist digital signiert, daher dürfen Sie die Datei nicht ändern. Auch das versehentliche Hinzufügen eines zusätzlichen Zeilenumbruchs in die Datei macht sie ungültig. Sie müssen eine Lizenz setzen, bevor Sie Aspose.Cells verwenden, wenn Sie die Evaluierungseinschränkung vermeiden möchten. Es ist nur einmal pro Anwendung (oder Prozess) erforderlich, eine Lizenz zu setzen. Die Lizenz kann aus einer Datei, einem Stream oder einem eingebetteten Ressourcen geladen werden.

Aspose.Cells versucht, die Lizenz an folgenden Orten zu finden:

- Expliziter Pfad
- Der Ordner, der Aspose.Cells.dll enthält
- Der Ordner, der das Assembly enthält, das Aspose.Cells.dll aufgerufen hat
- Der Ordner, der die Einstiegsanwendung enthält (Ihre .exe)
- Eine eingebettete Ressource in der Assembly, die Aspose.Cells.dll aufgerufen hat

Es gibt zwei gängige Methoden, um eine Lizenz anzuwenden, von Datei oder Stream, oder als eingebettete Ressource.

### **So wenden Sie eine Lizenz von Disk oder Stream an**

Der einfachste Weg, eine Lizenz festzulegen, besteht darin, die Lizenzdatei im selben Ordner wie die Aspose.Cells.dll zu platzieren und nur den Dateinamen ohne Pfad anzugeben.

{{< highlight csharp >}}

 //Instantiate an instance of license and set the license file through its path

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

Wenn Sie die SetLicense-Methode aufrufen, sollte der Lizenzname mit dem Namen Ihrer Lizenzdatei übereinstimmen. Sie können beispielsweise den Lizenzdateinamen in **Aspose.Cells.lic.xml** ändern. Dann sollten Sie im Code den modifizierten Lizenznamen (**Aspose.Cells.lic.xml**) für die SetLicense-Methode verwenden.

{{% /alert %}}

Es ist auch möglich, eine Lizenz von einem Stream zu laden.

{{< highlight csharp >}}

 //Instantiate an instance of license and set the license through a stream

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense(myStream);

{{< /highlight >}}

### **Wie man eine abgemessene Lizenz anwendet**

Aspose.Cells ermöglicht Entwicklern die Verwendung eines abgemessenen Schlüssels. Es handelt sich um einen neuen Lizenzierungsmechanismus. Der neue Lizenzierungsmechanismus wird zusammen mit der bestehenden Lizenzierungsmethode verwendet. Kunden, die nach der Nutzung der API-Funktionen abgerechnet werden möchten, können die abgemessene Lizenzierung verwenden. Weitere Details finden Sie im Abschnitt [FAQ zur abgemessenen Lizenzierung](https://purchase.aspose.com/faqs/licensing/metered).  

Eine neue Klasse [Metered](https://reference.aspose.com/cells/net/aspose.cells/metered) wurde eingeführt, um einen abgemessenen Schlüssel anzuwenden. Im Folgenden finden Sie den Beispielcode, der zeigt, wie man öffentlichen und privaten abgemessenen Schlüssel setzt.

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

### **Wie man eine eingebettete Ressource verwendet**

Eine weitere elegante Möglichkeit, die Lizenz mit Ihrer Anwendung zu verpacken und sicherzustellen, dass sie nicht verloren geht, besteht darin, sie als eingebettete Ressource in einer der Assemblys einzuschließen, die Aspose.Cells aufrufen. Führen Sie die folgenden Schritte aus, um die Lizenzdatei als eingebettete Ressource einzuschließen:

1. In Visual Studio .NET die Lizenz (.lic)-Datei in das Projekt einschließen, indem Sie **Vorhandenes Element hinzufügen** aus dem **Datei**-Menü auswählen.
1. Wählen Sie die Datei im Lösungs-Explorer aus und setzen Sie **Build-Aktion** auf **Eingebettete Ressource** im Eigenschaftenfenster

Um auf die in der Assembly eingebettete Lizenz (als eingebettete Ressource) zuzugreifen, ist es nicht erforderlich, die Methoden GetExecutingAssembly und GetManifestResourceStream der System.Reflection.Assembly-Klasse des Microsoft .NET Framework aufzurufen. Es genügt, die Lizenzdatei als eingebettete Ressource Ihrem Projekt hinzuzufügen und den Namen der Lizenzdatei an die SetLicense-Methode zu übergeben. Die Klasse **Aspose.Cells.License** findet automatisch die Lizenzdatei in den eingebetteten Ressourcen. Bitte sehen Sie sich das folgende Beispiel an, um diese Methode zum Festlegen der Lizenz (eingebettet) in Ihren Anwendungen zu verstehen.

{{< highlight csharp >}}

 //Instantiate the License class

Aspose.Cells.License license = new Aspose.Cells.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

## **Wie man eine Lizenz in Aspose.Cells Grid Controls setzt**

In Aspose.Cells Grid Suite kann die Lizenz aus einer Datei, einem Stream oder einer eingebetteten Ressource geladen werden. Aspose.Cells.GridDesktop / Aspose.Cells.GridWeb versuchen, die Lizenz in folgenden Speicherorten zu finden:

1. Expliziter Pfad
1. Der Ordner, der die dll des Komponenten enthält (in Aspose.Cells.GridDesktop oder Aspose.Cells.GridWeb enthalten)
1. Der Ordner, der die Assembly enthält, die die dll des Komponenten aufgerufen hat (in Aspose.Cells.GridDesktop oder Aspose.Cells.GridWeb enthalten)
1. Der Ordner, der die Einstiegsassembly enthält (Ihre .exe)
1. Eine eingebettete Ressource in der Assembly, die die DLL der Komponente aufgerufen hat (in Aspose.Cells.GridDesktop oder Aspose.Cells.GridWeb enthalten)

{{% alert color="primary" %}}

Wenn Sie das Aspose.Cells.GridDesktop-Control verwenden, wird die Lizenzklasse als Aspose.Cells.GridDesktop.License verwendet, wenn Sie jedoch das Aspose.Cells.GridWeb-Control verwenden, wird die Aspose.Cells.GridWeb.License-Klasse verwendet, um die Lizenz festzulegen.

{{% /alert %}}

### **So wenden Sie eine Lizenz von Disk oder Stream an**

Der einfachste Weg, um eine Lizenz festzulegen, besteht darin, die Lizenzdatei in denselben Ordner wie die DLL der Komponente (in Aspose.Cells.GridWeb enthalten) zu legen und nur den Dateinamen ohne Pfad anzugeben.

{{< highlight csharp >}}

//Instantiate an instance of license and set the license file through its path

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense("MyLicense.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

Wenn Sie die SetLicense-Methode aufrufen, sollte der Lizenzname mit dem Namen Ihrer Lizenzdatei übereinstimmen. Sie können beispielsweise den Namen der Lizenzdatei in "MyLicense.lic.xml" ändern. Dann sollten Sie im Code den modifizierten Lizenznamen verwenden (das ist MyLicense.lic.xml) für die SetLicense-Methode.

{{% /alert %}}

Es ist auch möglich, eine Lizenz von einem Stream zu laden.

{{< highlight csharp >}}

//Instantiate an instance of license and set the license through a stream

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense(myStream);

{{< /highlight >}}

### **So wenden Sie eine Lizenz als eingebettete Ressource an**

Ein weiterer eleganter Weg, die Lizenz mit Ihrer Anwendung zu bündeln und sicherzustellen, dass sie nicht verloren geht, besteht darin, sie als eingebettete Ressource in eine der Assemblys aufzunehmen, die die DLL der Komponente aufruft (in Aspose.Cells.GridDesktop enthalten). Um die Lizenzdatei als eingebettete Ressource aufzunehmen, führen Sie die folgenden Schritte durch:

1. In Visual Studio .NET die Lizenzdatei (.lic) mit der Option **Existierendes Element hinzufügen** im **Datei**-Menü dem Projekt hinzufügen.
1. Wählen Sie die Datei im Lösungsexplorer aus und setzen Sie im Eigenschaftenfenster die Buildaktion auf Eingebettete Ressource.
1. Um auf die eingebettete Lizenz in der Assembly (als eingebettete Ressource) zuzugreifen, ist es nicht erforderlich, die Methoden GetExecutingAssembly und GetManifestResourceStream der System.Reflection.Assembly-Klasse des Microsoft .NET Framework aufzurufen. Fügen Sie stattdessen die Lizenzdatei als eingebettete Ressource in Ihr Projekt ein und geben Sie den Namen der Lizenzdatei an die SetLicense-Methode weiter. Die Lizenzklasse findet die Lizenzdatei automatisch in den eingebetteten Ressourcen.

Bitte überprüfen Sie das untenstehende Beispiel, um dieses Verfahren zum Anwenden einer Lizenz als eingebettete Ressource auf Ihre Anwendungen zu verstehen.

{{< highlight csharp >}}

 //Instantiate the License class

Aspose.Cells.GridDesktop.License license = new Aspose.Cells.GridDesktop.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Total.lic");

{{< /highlight >}}

## **So wenden Sie eine Lizenz in Aspose.Cells.GridDesktop für eine WinForm-Anwendung an**

Es wird empfohlen, Ihren Lizenzcode vor dem Start Ihrer Anwendung einzufügen und ihn nur einmal anzuwenden. Setzen Sie beispielsweise für eine Windows C#-Anwendung den Lizenzcode in die Main-Methode.

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

## **Anmerkungen zur Anwendung einer Lizenz in Aspose.Cells.GridWeb**

Es wird empfohlen, den Lizenzcode in die Global.asax.cs Ihrer Webanwendung einzufügen (diese Lizenzdatei wird auf dem Laufwerk "d:\" angenommen):

{{< highlight csharp >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(@"d:\Aspose.Cells.GridWeb.lic.xml");

}

{{< /highlight >}}

Laden einer Lizenz von einem Stream

{{< highlight csharp >}}

 protected void Application_Start(Object sender, EventArgs e)

{

    Aspose.Cells.GridWeb.License lic = new Aspose.Cells.GridWeb.License();

    lic.SetLicense(myStream);

}

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
