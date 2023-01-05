---
title: Lizenzierung
type: docs
weight: 50
url: /de/python-java/licensing/
---
{{% alert color="primary" %}} 

 Sie können eine Evaluierungsversion von installieren**Aspose.Cells** for Python via Java mit `pip install aspose-cells`. Die Evaluierungsversion bietet absolut dieselben Funktionen wie die lizenzierte Version des Produkts. Darüber hinaus wird die Evaluierungsversion einfach lizenziert, wenn Sie eine Lizenz erwerben und ein paar Codezeilen hinzufügen, um die Lizenz anzuwenden.

 Sobald Sie mit Ihrer Bewertung zufrieden sind**Aspose.Cells** , Sie können[eine Lizenz erwerben](https://purchase.aspose.com)auf der Website Aspose. Machen Sie sich mit den verschiedenen angebotenen Abonnementarten vertraut. Bei Fragen steht Ihnen das Verkaufsteam unter Aspose gerne zur Verfügung.

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

Die Lizenz kann aus einer Datei an den folgenden Orten geladen werden:

1. Explizite Pfad.
1. Arbeitsordner.

 Verwenden Sie die[Lizenz.setLizenz](https://reference.aspose.com/cells/python-java/asposecells.api/License) Methode zum Lizenzieren der Komponente. Der einfachste Weg, eine Lizenz festzulegen, besteht oft darin, die Lizenzdatei in denselben Ordner wie Aspose.Cells.jar zu legen und nur den Dateinamen ohne Pfad anzugeben, wie im folgenden Beispiel gezeigt:

### **Beispiel**

 In diesem Beispiel**Aspose.Cells** wird versuchen, die Lizenzdatei in Ihrem Arbeitsordner zu finden.

{{< highlight "python" >}}

from asposecells.api import License

lic = License()
lic.setLicense("Aspose.Cells.lic")

{{< /highlight >}}
