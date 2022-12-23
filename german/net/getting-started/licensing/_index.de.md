---
title: Lizenzierung
type: docs
weight: 120
url: /de/net/licensing/
---
{{% alert color="primary" %}}

 Sie können ganz einfach eine Testversion von Aspose.Cells von herunterladen[Download-Seite](https://www.nuget.org/packages/Aspose.Cells) @ NuGet repos. Die Evaluierungsversion bietet absolut dieselben Funktionen wie die lizenzierte Version der Komponente. Darüber hinaus wird die Evaluierungsversion einfach lizenziert, wenn Sie eine Lizenz erwerben und ein paar Codezeilen hinzufügen, um die Lizenz anzuwenden.

{{% /alert %}}

## **Einschränkungen der Evaluierungsversion**

Die Evaluierungsversion des Produkts Aspose.Cells (ohne Angabe einer Lizenz) bietet die volle Produktfunktionalität, ist jedoch auf das Öffnen von 100 Dateien in einem Programm und einem zusätzlichen Arbeitsblatt mit Evaluierungswasserzeichen beschränkt.

Die Einschränkungen sind unten aufgeführt:

- **Anzahl der geöffneten Dateien** (Aspose.Cells)
Wenn Sie Ihr Programm ausführen, können Sie nur 100 Excel-Dateien mit der Bibliothek Aspose.Cells öffnen. Wenn Ihre Anwendung diese Zahl überschreitet, wird eine Ausnahme ausgelöst.
- **Einstellungen der Konfigurationsdatei** (Aspose.Cells.GridWeb)
 Sie können den Skriptpfad nicht neu angeben, indem Sie die folgenden Codezeilen in den Konfigurationsabschnitt einfügen (z. B. in die Datei web.config). Der acw_client ist ein Ordner, der Dateien enthält, und Aspose.Cells. GridWeb verwendet diesen Ordner, um seine interne Konfiguration zu verwalten, er enthält Skriptdateien, Bilddateien und andere Dateien, um das Verhalten von GridWeb festzulegen und andere Operationen festzulegen. Die Konfigurationsdatei wird verwendet, um zu verhindern, dass das Steuerelement die eingebetteten Client-Ressourcen (Bilder, Skripte usw.) verwendet, was in einigen Fällen / Szenarien nützlich ist. Darüber hinaus werden diese Konfigurationseinstellungen in der Datei web.config nur mit der LIZENZIERTEN Version des Steuerelements wirksam.

**XML**

{{< highlight "csharp" >}}

 <appSettings>

<add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

<add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>

{{< /highlight >}}

{{% alert color="primary" %}}

Diese Einstellungen können in einigen Fällen/Szenarien obligatorisch sein, wenn Sie die Aspose.Cells.GridWeb-Steuerung in Dateisystem-Websites oder MS Ajax-Erweiterungen usw. verwenden.

{{% /alert %}}

Darüber hinaus wird ein Arbeitsblatt mit Bewertungswasserzeichen immer als aktives Arbeitsblatt in der generierten Excel-Datei angezeigt, die die Bibliothek Aspose.Cells verwendet. Nur in der lizenzierten Version können Sie das aktive Arbeitsblatt auf andere Arbeitsblätter setzen. In der Ausgabe PDF oder der Bilddatei von Aspose.Cells würde ein Bewertungswasserzeichen am oberen Rand des Dokuments/Bilds eingefügt. Sie können die Bewertungs-Copyright-Warnung (das zusätzliche Arbeitsblatt) auch im GridWeb-Steuerelement nicht ausblenden, sie wird immer hinzugefügt (am Ende in den Arbeitsblattregistern) im Steuerelement.

{{% alert color="primary" %}}

 Wenn Sie Aspose.Cells ohne Einschränkungen der Evaluierungsversion testen möchten, können Sie auch a[30 Tage temporäre Lizenz](https://purchase.aspose.com/temporary-license).

{{% /alert %}}

## **Anwenden einer Lizenz in Aspose.Cells Komponente**

Die Lizenz ist eine reine Text-XML-Datei, die Details wie den Produktnamen, die Anzahl der lizenzierten Entwickler, das Ablaufdatum des Abonnements usw. enthält. Die Datei ist digital signiert, ändern Sie die Datei also nicht. Selbst das versehentliche Hinzufügen eines zusätzlichen Zeilenumbruchs in die Datei macht sie ungültig. Sie müssen eine Lizenz festlegen, bevor Sie Aspose.Cells verwenden, wenn Sie die Evaluierungseinschränkung vermeiden möchten. Es ist nur einmal pro Anwendung (oder Prozess) erforderlich, eine Lizenz festzulegen. Die Lizenz kann aus einer Datei, einem Stream oder einer eingebetteten Ressource geladen werden.

Aspose.Cells versucht, die Lizenz an den folgenden Orten zu finden:

- Explizite Pfad
- Der Ordner, der Aspose.Cells.dll enthält
- Der Ordner, der die Assembly mit dem Namen Aspose.Cells.dll enthält
- Der Ordner, der den Eintrag Assembly enthält (Ihre .exe)
- Eine eingebettete Ressource in der Assembly, die Aspose.Cells.dll aufgerufen hat

Es gibt zwei gängige Methoden zum Anwenden einer Lizenz, aus einer Datei oder einem Stream oder als eingebettete Ressource.

### **Anwenden einer Lizenz von Disk oder Stream**

Der einfachste Weg, eine Lizenz festzulegen, besteht darin, die Lizenzdatei in denselben Ordner wie die Aspose.Cells.dll zu legen und nur den Dateinamen ohne Pfad anzugeben.

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license file through its path

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

 Wenn Sie die SetLicense-Methode aufrufen, sollte der Lizenzname mit dem Namen Ihrer Lizenzdatei identisch sein. Beispielsweise können Sie den Namen der Lizenzdatei ändern in**Aspose.Cells.lic.xml**. Dann sollten Sie in Ihrem Code den geänderten Lizenznamen verwenden (**Aspose.Cells.lic.xml**) für die SetLicense-Methode.

{{% /alert %}}

Es ist auch möglich, eine Lizenz aus einem Stream zu laden.

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license through a stream

Aspose.Cells.License license = new Aspose.Cells.License();

license.SetLicense(myStream);

{{< /highlight >}}

### **Gemessene Lizenz anwenden**

Aspose.Cells ermöglicht es Entwicklern, gemessene Schlüssel anzuwenden. Es ist ein neuer Lizenzierungsmechanismus. Der neue Lizenzierungsmechanismus wird zusammen mit der bestehenden Lizenzierungsmethode verwendet. Diejenigen Kunden, die basierend auf der Nutzung der API-Funktionen abgerechnet werden möchten, können die gebührenpflichtige Lizenzierung verwenden. Weitere Einzelheiten finden Sie unter[Häufig gestellte Fragen zur getakteten Lizenzierung](https://purchase.aspose.com/faqs/licensing/metered)Sektion.

Eine neue Klasse[Gemessen](https://reference.aspose.com/cells/net/aspose.cells/metered)wurde eingeführt, um einen gemessenen Schlüssel anzuwenden. Im Folgenden finden Sie den Beispielcode, der zeigt, wie der gemessene öffentliche und private Schlüssel festgelegt wird.

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

### **Verwenden einer eingebetteten Ressource**

Eine andere nette Möglichkeit, die Lizenz mit Ihrer Anwendung zu verpacken und sicherzustellen, dass sie nicht verloren geht, besteht darin, sie als eingebettete Ressource in eine der Assemblys einzuschließen, die Aspose.Cells aufruft. Führen Sie die folgenden Schritte aus, um die Lizenzdatei als eingebettete Ressource einzuschließen :

1.  Fügen Sie in Visual Studio .NET die Lizenzdatei (.lic) durch Auswahl in das Projekt ein**Vorhandenes Element hinzufügen** von dem**Datei** Speisekarte.
1. Wählen Sie die Datei im Projektmappen-Explorer aus und stellen Sie sie ein**Aktion erstellen** zu**Eingebettete Ressource** im Eigenschaftenfenster

 Um auf die in die Assembly eingebettete Lizenz (als eingebettete Ressource) zuzugreifen, ist es nicht erforderlich, die Methoden GetExecutingAssembly und GetManifestResourceStream der System.Reflection.Assembly-Klasse von Microsoft .NET Framework aufzurufen. Sie müssen lediglich die Lizenzdatei als eingebettete Ressource zu Ihrem Projekt hinzufügen und den Namen der Lizenzdatei an die SetLicense-Methode übergeben. Das**Aspose.Cells.License** class findet die Lizenzdatei automatisch in den eingebetteten Ressourcen. Bitte sehen Sie sich das unten angegebene Beispiel an, um diese Methode zum Festlegen von Lizenzen (eingebettet) in Ihren Anwendungen zu verstehen.

{{< highlight "csharp" >}}

 //Instantiate the License class

Aspose.Cells.License license = new Aspose.Cells.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Cells.lic");

{{< /highlight >}}

## **Einstellen der Lizenz in Aspose.Cells Grid Controls**

In Aspose.Cells Grid Suite kann die Lizenz aus einer Datei, einem Stream oder einer eingebetteten Ressource geladen werden. Aspose.Cells.GridDesktop / Aspose.Cells.GridWeb versucht, die Lizenz an den folgenden Orten zu finden:

1. Explizite Pfad
1. Der Ordner, der die DLL der Komponente enthält (enthalten in Aspose.Cells.GridDesktop oder Aspose.Cells.GridWeb)
1. Der Ordner, der die Assembly enthält, die die DLL der Komponente aufgerufen hat (enthalten in Aspose.Cells.GridDesktop oder Aspose.Cells.GridWeb)
1. Der Ordner, der den Eintrag Assembly enthält (Ihre .exe)
1. Eine eingebettete Ressource in der Assembly, die die DLL der Komponente aufgerufen hat (enthalten in Aspose.Cells.GridDesktop oder Aspose.Cells.GridWeb)

{{% alert color="primary" %}}

Wenn Sie das Aspose.Cells.GridDesktop-Steuerelement verwenden, wird die Lizenzklasse als Aspose.Cells.GridDesktop.License verwendet. Wenn Sie jedoch das Aspose.Cells.GridWeb-Steuerelement verwenden, wird die Klasse Aspose.Cells.GridWeb.License zum Festlegen der Lizenz verwendet.

{{% /alert %}}

### **Anwenden einer Lizenz von Disk oder Stream**

Der einfachste Weg, eine Lizenz festzulegen, besteht darin, die Lizenzdatei in denselben Ordner wie die DLL der Komponente (in Aspose.Cells.GridWeb enthalten) zu legen und nur den Dateinamen ohne Pfad anzugeben.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license file through its path

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense("MyLicense.lic");

{{< /highlight >}}

{{% alert color="primary" %}}

Wenn Sie die SetLicense-Methode aufrufen, sollte der Lizenzname mit dem Namen Ihrer Lizenzdatei identisch sein. Beispielsweise können Sie den Namen der Lizenzdatei in „MyLicense.lic.xml“ ändern. Dann sollten Sie in Ihrem Code den geänderten Lizenznamen (d. h. MyLicense.lic.xml) für die SetLicense-Methode verwenden.

{{% /alert %}}

Es ist auch möglich, eine Lizenz aus einem Stream zu laden.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license through a stream

Aspose.Cells.GridWeb.License license = new Aspose.Cells.GridWeb.License();

license.SetLicense(myStream);

{{< /highlight >}}

### **Anwenden einer Lizenz als eingebettete Ressource**

Eine weitere nette Möglichkeit, die Lizenz mit Ihrer Anwendung zu verpacken und sicherzustellen, dass sie nicht verloren geht, besteht darin, sie als eingebettete Ressource in eine der Assemblys einzufügen, die die DLL der Komponente aufruft (in Aspose.Cells.GridDesktop enthalten). Führen Sie die folgenden Schritte aus, um die Lizenzdatei als eingebettete Ressource einzuschließen:

1.  Fügen Sie in Visual Studio .NET die Lizenzdatei (.lic) in das Projekt ein, indem Sie die**Vorhandenes Element hinzufügen** Option auf der**Datei** Speisekarte.
1. Wählen Sie die Datei im Projektmappen-Explorer aus und setzen Sie Build Action im Fenster Properties auf Embedded Resource.
1. Um auf die in die Assembly eingebettete Lizenz (als eingebettete Ressource) zuzugreifen, ist es nicht erforderlich, die Methoden GetExecutingAssembly und GetManifestResourceStream der System.Reflection.Assembly-Klasse von Microsoft .NET Framework aufzurufen. Fügen Sie stattdessen die Lizenzdatei als eingebettete Ressource in Ihrer project und übergeben Sie den Namen der Lizenzdatei an die SetLicense-Methode. Die Lizenzklasse findet automatisch die Lizenzdatei in den eingebetteten Ressourcen.

Bitte sehen Sie sich das unten angegebene Beispiel an, um diese Methode zum Anwenden einer Lizenz als eingebettete Ressource auf Ihre Anwendungen zu verstehen.

{{< highlight "csharp" >}}

 //Instantiate the License class

Aspose.Cells.GridDesktop.License license = new Aspose.Cells.GridDesktop.License();

//Pass only the name of the license file embedded in the assembly

license.SetLicense("Aspose.Total.lic");

{{< /highlight >}}

## **Anwenden einer Lizenz in Aspose.Cells.GridDesktop für eine WinForm-Anwendung**

Es wird empfohlen, dass Sie Ihren Lizenzcode eingeben, bevor Ihre Anwendung startet, und ihn nur einmal anwenden. Geben Sie beispielsweise für eine Windows C#-Anwendung den Lizenzcode in die Main-Methode ein.

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

## **Hinweise zum Anwenden einer Lizenz in Aspose.Cells.GridWeb**

Es wird empfohlen, den Lizenzcode in Global.asax.cs Ihrer Webanwendung abzulegen (es wird davon ausgegangen, dass diese Lizenzdatei auf dem Laufwerk „d:\“ abgelegt wird):

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
