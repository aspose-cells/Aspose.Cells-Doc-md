---
title: Lizenzierung
type: docs
weight: 50
url: /de/java/licensing/
---
{{% alert color="primary" %}} 

 Sie können eine Evaluierungsversion von herunterladen**Aspose.Cells** for Java ab[seine Download-Seite](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-cells) @ Maven repos. Die Evaluierungsversion bietet absolut dieselben Funktionen wie die lizenzierte Version des Produkts. Darüber hinaus wird die Evaluierungsversion einfach lizenziert, wenn Sie eine Lizenz erwerben und ein paar Codezeilen hinzufügen, um die Lizenz anzuwenden.

 Sobald Sie mit Ihrer Bewertung zufrieden sind**Aspose.Cells** , du kannst[eine Lizenz kaufen](https://purchase.aspose.com)auf der Website Aspose. Machen Sie sich mit den verschiedenen angebotenen Abonnementarten vertraut. Bei Fragen steht Ihnen das Verkaufsteam unter Aspose gerne zur Verfügung.

Jede Aspose-Lizenz enthält ein einjähriges Abonnement für kostenlose Upgrades auf alle neuen Versionen oder Fixes, die während dieser Zeit herauskommen. Der technische Support ist kostenlos und unbegrenzt und wird sowohl lizenzierten als auch Testbenutzern zur Verfügung gestellt.

{{% /alert %}} {{% alert color="primary" %}} 

 Wenn Sie testen möchten**Aspose.Cells** ohne Einschränkungen der Testversion, fordern Sie eine temporäre 30-Tage-Lizenz an. Bitte beziehen Sie sich auf[Wie erhalte ich eine temporäre Lizenz?](https://purchase.aspose.com/temporary-license) für mehr Informationen.

{{% /alert %}}

## **Einschränkungen der Evaluierungsversion**

 Evaluierungsversion von**Aspose.Cells** Das Produkt (ohne angegebene Lizenz) bietet die volle Produktfunktionalität, ist jedoch auf das Öffnen von 100 Dateien in einem Programm und einem zusätzlichen Arbeitsblatt mit Wasserzeichen für die Evaluierung beschränkt.

Die Einschränkungen sind unten aufgeführt:

### **1. Einschränkung: Anzahl der geöffneten Dateien**

Wenn Sie Ihr Programm ausführen, können Sie nur 100 Excel-Dateien öffnen. Wenn Ihre Anwendung diese Zahl überschreitet, wird eine Ausnahme ausgelöst.

### **2. Einschränkung: Arbeitsblatt mit Bewertungswasserzeichen**

![todo: Bild_alt_Text](licensing_1.png)

Dieses Arbeitsblatt wird immer als aktives Arbeitsblatt angezeigt. Nur in der lizenzierten Version können Sie das aktive Arbeitsblatt auf andere Arbeitsblätter setzen.

## **Einstellen einer Lizenz**

Die Lizenz ist eine reine Text-XML-Datei, die Details wie den Produktnamen, die Anzahl der lizenzierten Entwickler, das Ablaufdatum des Abonnements usw. enthält. Die Datei ist digital signiert, ändern Sie die Datei also nicht; selbst das versehentliche Hinzufügen eines zusätzlichen Zeilenumbruchs in der Datei macht sie ungültig.

Sie müssen eine Lizenz festlegen, bevor Sie Aspose.Cells verwenden, wenn Sie die Evaluierungseinschränkungen vermeiden möchten. Sie müssen nur einmal pro Anwendung oder Prozess eine Lizenz festlegen.

Die Lizenz kann aus einem Stream oder einer Datei an den folgenden Orten geladen werden:

1. Explizite Pfad.
1. Der Ordner, der die Datei Aspose.Cells.jar enthält.

 Verwenden Sie die[Lizenz.setLizenz](https://reference.aspose.com/cells/java/com.aspose.cells/license#setLicense(java.io.InputStream))-Methode zum Lizenzieren der Komponente. Der einfachste Weg, eine Lizenz festzulegen, besteht oft darin, die Lizenzdatei in denselben Ordner wie Aspose.Cells.jar zu legen und nur den Dateinamen ohne Pfad anzugeben, wie im folgenden Beispiel gezeigt:

### **Beispiel 1**

 In diesem Beispiel**Aspose.Cells** versucht, die Lizenzdatei in dem Ordner zu finden, der die JARs Ihrer Anwendung enthält.

{{< highlight "csharp" >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense("Aspose.Cells.Java.lic");

{{< /highlight >}}

### **Beispiel 2**

Initialisiert eine Lizenz aus einem Stream.

{{< highlight "csharp" >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense(new java.io.FileInputStream("Aspose.Cells.Java.lic"));

{{< /highlight >}}

### **Hinweise zum Anwenden einer Lizenz in Aspose.Cells.GridWeb**

Es wird empfohlen, den Lizenzcode an einer Stelle in Ihrer Webanwendung zu platzieren, an der er zuerst verarbeitet werden soll.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license file through its path

com.aspose.gridweb.License lic = new com.aspose.gridweb.License();

lic.setLicense("Aspose.Cells.lic");

{{< /highlight >}}

## **Gemessene Lizenz anwenden**

Aspose.Cells ermöglicht es Entwicklern, gemessene Schlüssel anzuwenden. Es ist ein neuer Lizenzierungsmechanismus. Der neue Lizenzierungsmechanismus wird zusammen mit der bestehenden Lizenzierungsmethode verwendet. Diejenigen Kunden, die basierend auf der Nutzung der API-Funktionen abgerechnet werden möchten, können die gebührenpflichtige Lizenzierung verwenden. Weitere Einzelheiten finden Sie unter[Häufig gestellte Fragen zur getakteten Lizenzierung](https://purchase.aspose.com/faqs/licensing/metered)Sektion.

Eine neue Klasse[Gemessen](https://reference.aspose.com/cells/java/com.aspose.cells/Metered)wurde eingeführt, um einen gemessenen Schlüssel anzuwenden. Im Folgenden finden Sie den Beispielcode, der zeigt, wie der gemessene öffentliche und private Schlüssel festgelegt wird.

{{< highlight "java" >}}

//Set metered public and private keys

Metered metered = new Metered();

//Access the setMeteredKey property and pass public and private keys as parameters

metered.setMeteredKey("************", "************");

//Instantiate a new Workbook

Workbook workbook = new Workbook();

//Check if the license is set

System.out.println(workbook.isLicensed());

//Get the Consumption quantity

double amountBefore = Metered.getConsumptionQuantity();

System.out.println(amountBefore);

Workbook workbook2 = new Workbook("Book1.xlsx");

workbook2.save("out1.xlsx");

//Get the Consumption quantity again which should be greater a bit

double amountAfter = Metered.getConsumptionQuantity();

System.out.println(amountAfter);

{{< /highlight >}}
