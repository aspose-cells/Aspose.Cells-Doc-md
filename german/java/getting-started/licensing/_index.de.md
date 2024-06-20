---
title: Lizenzierung
type: docs
weight: 50
url: /de/java/licensing/
description: Aspose.Cells für JAVA bietet verschiedene Pläne zum Kauf oder bietet eine kostenlose Testversion und eine 30 tägige vorübergehende Lizenz zur Evaluation unter Verwendung von Lizenzierungs und Abonnementrichtlinien in Java.
keywords: Lizenz in Java von Diskette oder Stream anwenden. Lizenz in Java von Diskette oder Stream setzen. Lizenz in Aspose.Cells for Java anwenden.
---

## **Wie man eine Lizenz in Aspose.Cells-Komponente anwendet**

Die Lizenz ist eine einfache Text-XML-Datei, die Details wie den Produktnamen, die Anzahl der lizenzierten Entwickler, das Ablaufdatum des Abonnements usw. enthält. Die Datei ist digital signiert, also ändern Sie die Datei nicht; selbst das versehentliche Hinzufügen eines zusätzlichen Zeilenumbruchs in die Datei macht sie ungültig.

Sie müssen eine Lizenz setzen, bevor Sie Aspose.Cells verwenden, wenn Sie dessen Evaluierungsbeschränkungen vermeiden möchten. Sie müssen die Lizenz nur einmal pro Anwendung oder Prozess setzen.

Die Lizenz kann von einem Stream oder einer Datei an den folgenden Speicherorten geladen werden:

1. Ausdrücklicher Pfad.
1. Der Ordner, der die Aspose.Cells.jar enthält.

Verwenden Sie die Methode [License.setLicense](https://reference.aspose.com/cells/java/com.aspose.cells/license#setLicense(java.io.InputStream)), um die Komponente zu lizenzieren. Oft ist es am einfachsten, die Lizenzdatei in denselben Ordner wie Aspose.Cells.jar zu platzieren und nur den Dateinamen ohne Pfad anzugeben, wie im folgenden Beispiel gezeigt:

### **Wie man eine Lizenz von der Diskette anwendet**

In diesem Beispiel wird **Aspose.Cells** versuchen, die Lizenzdatei im Ordner zu finden, der die JARs Ihrer Anwendung enthält.

{{< highlight csharp >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense("Aspose.Cells.Java.lic");

{{< /highlight >}}

### **Wie man eine Lizenz von einem Stream anwendet**

Initialisiert eine Lizenz von einem Stream.

{{< highlight csharp >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense(new java.io.FileInputStream("Aspose.Cells.Java.lic"));

{{< /highlight >}}

### **Wie man eine Lizenz im Aspose.Cells.GridWeb anwendet**

Es wird empfohlen, den Lizenzierungscode an einem Ort in Ihrer Webanwendung zu platzieren, an dem er zuerst verarbeitet wird.

{{< highlight csharp >}}

//Instantiate an instance of license and set the license file through its path

com.aspose.gridweb.License lic = new com.aspose.gridweb.License();

lic.setLicense("Aspose.Cells.lic");

{{< /highlight >}}

## **Wie man eine abgemessene Lizenz anwendet**

Aspose.Cells ermöglicht Entwicklern die Verwendung eines abgemessenen Schlüssels. Es handelt sich um einen neuen Lizenzierungsmechanismus. Der neue Lizenzierungsmechanismus wird zusammen mit der bestehenden Lizenzierungsmethode verwendet. Kunden, die nach der Nutzung der API-Funktionen abgerechnet werden möchten, können die abgemessene Lizenzierung verwenden. Weitere Details finden Sie im Abschnitt [FAQ zur abgemessenen Lizenzierung](https://purchase.aspose.com/faqs/licensing/metered).

Es wurde eine neue Klasse [Metered](https://reference.aspose.com/cells/java/com.aspose.cells/Metered) eingeführt, um einen lizenzierten Schlüssel anzuwenden. Im Folgenden finden Sie den Beispielcode, der zeigt, wie ein lizenzierter öffentlicher und privater Schlüssel festgelegt wird.

{{< highlight java >}}

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
