---
title: Lizenzierung
type: docs
weight: 50
url: /de/python-java/licensing/
---

{{% alert color="primary" %}} 

Sie können eine Evaluierungsversion von **Aspose.Cells** für Python via Java mit `pip install aspose-cells` installieren. Die Evaluierungsversion bietet genau die gleichen Funktionen wie die lizenzierte Version des Produkts. Außerdem wird die Evaluierungsversion einfach lizenziert, wenn Sie eine Lizenz erwerben und ein paar Zeilen Code hinzufügen, um die Lizenz anzuwenden.

Wenn Sie mit Ihrer Evaluierung von **Aspose.Cells** zufrieden sind, können Sie [eine Lizenz erwerben](https://purchase.aspose.com) auf der Aspose-Website. Machen Sie sich mit den verschiedenen angebotenen Abonnementtypen vertraut. Bei Fragen zögern Sie nicht, das Aspose-Verkaufsteam zu kontaktieren.

Jede Aspose-Lizenz beinhaltet ein einjähriges Abonnement für kostenlose Upgrades auf alle neuen Versionen oder Fixes, die während dieser Zeit veröffentlicht werden. Der technische Support ist kostenlos und unbegrenzt und wird sowohl für lizenzierte als auch für Evaluierungsnutzer bereitgestellt.

{{% /alert %}} {{% alert color="primary" %}} 

Wenn Sie **Aspose.Cells** ohne Einschränkungen der Evaluierungsversion testen möchten, fordern Sie eine 30-tägige temporäre Lizenz an. Bitte beachten Sie [Wie man eine temporäre Lizenz erhält](https://purchase.aspose.com/temporary-license) für weitere Informationen.

{{% /alert %}}

## **Evaluierungsversion-Beschränkungen**

Die Evaluierungsversion des **Aspose.Cells**-Produkts (ohne spezifizierte Lizenz) bietet die volle Funktionalität des Produkts, ist jedoch auf das Öffnen von 100 Dateien in einem Programm und ein zusätzliches Arbeitsblatt mit Evaluierungswasserzeichen beschränkt.

Die Beschränkungen werden unten angezeigt:

### **1. Beschränkung: Anzahl der geöffneten Dateien**

Beim Ausführen Ihres Programms können Sie nur 100 Excel-Dateien öffnen. Wenn Ihre Anwendung diese Anzahl überschreitet, wird eine Ausnahme ausgelöst.

### **2. Beschränkung: Arbeitsblatt mit Evaluierungswasserzeichen**

![todo:image_alt_text](licensing_1.png)

Dieses Arbeitsblatt wird immer als aktives Arbeitsblatt angezeigt. Nur in der lizenzierten Version können Sie das aktive Arbeitsblatt auf andere Arbeitsblätter festlegen.

## **Lizenz festlegen**

Die Lizenz ist eine einfache Text-XML-Datei, die Details wie den Produktnamen, die Anzahl der lizenzierten Entwickler, das Ablaufdatum des Abonnements usw. enthält. Die Datei ist digital signiert, also ändern Sie die Datei nicht; selbst das versehentliche Hinzufügen eines zusätzlichen Zeilenumbruchs in die Datei macht sie ungültig.

Sie müssen eine Lizenz setzen, bevor Sie Aspose.Cells verwenden, wenn Sie dessen Evaluierungsbeschränkungen vermeiden möchten. Sie müssen die Lizenz nur einmal pro Anwendung oder Prozess setzen.

Die Lizenz kann aus einer Datei an den folgenden Orten geladen werden:

1. Ausdrücklicher Pfad.
1. Arbeitsordner.

Verwenden Sie die [License.setLicense](https://reference.aspose.com/cells/python-java/asposecells.api/License)-Methode, um das Komponente zu lizenzieren. Oft ist der einfachste Weg, eine Lizenz zu setzen, die Lizenzdatei in denselben Ordner wie Aspose.Cells.jar zu legen und nur den Dateinamen ohne Pfad anzugeben, wie im folgenden Beispiel gezeigt:

### **Beispiel**

In diesem Beispiel wird **Aspose.Cells** versuchen, die Lizenzdatei in Ihrem Arbeitsordner zu finden.

{{< highlight python >}}

from asposecells.api import License

lic = License()
lic.setLicense("Aspose.Cells.lic")

{{< /highlight >}}
