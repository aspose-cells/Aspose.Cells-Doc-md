---
title: Licensing
type: docs
weight: 50
url: /de/java/licensing/
description: Aspose.Cells für JAVA bietet verschiedene Kaufpläne oder eine kostenlose Testversion und eine 30-tägige temporäre Lizenz zur Evaluierung unter Verwendung von Licensing und Abonnementrichtlinien in Java.
keywords: Java Apply License from Disk or Stream. Java Set License from Disk or Stream. Apply License in Aspose.Cells for Java.
---
##  **So beantragen Sie eine Lizenz in der Komponente Aspose.Cells**

Die Lizenz ist eine reine XML-Textdatei, die Details wie den Produktnamen, die Anzahl der Entwickler, an die sie lizenziert ist, das Ablaufdatum des Abonnements usw. enthält. Die Datei ist digital signiert. Ändern Sie sie daher nicht. Selbst das versehentliche Einfügen eines zusätzlichen Zeilenumbruchs in die Datei macht sie ungültig.

Sie müssen vor der Verwendung von Aspose.Cells eine Lizenz festlegen, wenn Sie die Testeinschränkungen vermeiden möchten. Sie müssen nur einmal pro Anwendung oder Prozess eine Lizenz festlegen.

Die Lizenz kann aus einem Stream oder einer Datei an den folgenden Orten geladen werden:

1. Expliziter Pfad.
1. Der Ordner, der die Datei Aspose.Cells.jar enthält.

 Benutzen Sie die[License.setLicense](https://reference.aspose.com/cells/java/com.aspose.cells/license#setLicense(java.io.InputStream))-Methode zum Lizenzieren der Komponente. Der einfachste Weg, eine Lizenz festzulegen, besteht häufig darin, die Lizenzdatei im selben Ordner wie Aspose.Cells.jar abzulegen und nur den Dateinamen ohne Pfad anzugeben, wie im folgenden Beispiel gezeigt:

###  **So wenden Sie eine Lizenz von der Festplatte an**

 In diesem Beispiel**Aspose.Cells**wird versuchen, die Lizenzdatei in dem Ordner zu finden, der die JARs Ihrer Anwendung enthält.

{{< highlight "csharp" >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense("Aspose.Cells.Java.lic");

{{< /highlight >}}

###  **So beantragen Sie eine Lizenz aus Stream**

Initialisiert eine Lizenz aus einem Stream.

{{< highlight "csharp" >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense(new java.io.FileInputStream("Aspose.Cells.Java.lic"));

{{< /highlight >}}

###  **So beantragen Sie eine Lizenz in Aspose.Cells.GridWeb**

Es wird empfohlen, den Lizenzcode an einer Stelle in Ihrer Webanwendung zu platzieren, an der er zuerst verarbeitet werden soll.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license file through its path

com.aspose.gridweb.License lic = new com.aspose.gridweb.License();

lic.setLicense("Aspose.Cells.lic");

{{< /highlight >}}

##  **So wenden Sie eine gemessene Lizenz an**

Aspose.Cells ermöglicht Entwicklern die Anwendung eines gemessenen Schlüssels. Es handelt sich um einen neuen Lizenzierungsmechanismus. Der neue Lizenzierungsmechanismus wird zusammen mit der bestehenden Lizenzierungsmethode verwendet. Kunden, die eine Abrechnung auf Basis der Nutzung der API-Funktionen wünschen, können die getaktete Lizenzierung nutzen. Weitere Einzelheiten finden Sie unter[Metered Licensing FAQ](https://purchase.aspose.com/faqs/licensing/metered)Abschnitt.

Eine neue Klasse[Dosiert](https://reference.aspose.com/cells/java/com.aspose.cells/Metered)wurde eingeführt, um einen dosierten Schlüssel anzuwenden. Im Folgenden finden Sie einen Beispielcode, der zeigt, wie ein gemessener öffentlicher und privater Schlüssel festgelegt wird.

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
