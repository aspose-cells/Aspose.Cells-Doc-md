---
title: Lizenzierung
type: docs
weight: 21
url: /de/python-net/licensing/
---
{{% alert color="primary" %}}

 Sie können eine Evaluierungsversion von Aspose.Cells Python einfach über .Net von herunterladen[Download-Seite](https://pypi.org/project/aspose-cells-python/) Pypi-Repos. Die Evaluierungsversion bietet absolut dieselben Funktionen wie die lizenzierte Version der Komponente. Darüber hinaus wird die Evaluierungsversion einfach lizenziert, wenn Sie eine Lizenz erwerben und ein paar Codezeilen hinzufügen, um die Lizenz anzuwenden.

{{% /alert %}}

## **Einschränkungen der Evaluierungsversion**

Die Evaluierungsversion von Aspose.Cells Python über das .Net-Produkt (ohne Angabe einer Lizenz) bietet die volle Produktfunktionalität, ist jedoch auf das Öffnen von 100 Dateien in einem Programm und einem zusätzlichen Arbeitsblatt mit Evaluierungswasserzeichen beschränkt.

Die Einschränkungen sind unten aufgeführt:

- **Anzahl der geöffneten Dateien** (Aspose.Cells Python über .Net)
 Wenn Sie Ihr Programm ausführen, können Sie nur 100 Excel-Dateien mit Aspose.Cells Python über die .Net-Bibliothek öffnen. Wenn Ihre Anwendung diese Zahl überschreitet, wird eine Ausnahme ausgelöst.


Darüber hinaus wird ein Arbeitsblatt mit Bewertungswasserzeichen immer als aktives Arbeitsblatt in der generierten Excel-Datei mit Aspose.Cells Python über die Bibliothek angezeigt. Nur in der lizenzierten Version können Sie das aktive Arbeitsblatt auf andere Arbeitsblätter setzen. In der Ausgabe-PDF- oder Bilddatei von Aspose.Cells Python über würde ein Bewertungswasserzeichen am oberen Rand des Dokuments/Bilds eingefügt.

{{% alert color="primary" %}}

 Wenn Sie Aspose.Cells Python ohne Einschränkungen der Evaluierungsversion testen möchten, können Sie auch eine anfordern[30 Tage temporäre Lizenz](https://purchase.aspose.com/temporary-license).

{{% /alert %}}

## **Anwenden einer Lizenz in Aspose.Cells Python über Komponente**

Die Lizenz ist eine reine Text-XML-Datei, die Details wie den Produktnamen, die Anzahl der lizenzierten Entwickler, das Ablaufdatum des Abonnements usw. enthält. Die Datei ist digital signiert, ändern Sie die Datei also nicht. Selbst das versehentliche Hinzufügen eines zusätzlichen Zeilenumbruchs in der Datei macht sie ungültig. Sie müssen eine Lizenz festlegen, bevor Sie Aspose.Cells Python über verwenden, wenn Sie die Evaluierungseinschränkung vermeiden möchten. Es ist nur einmal pro Anwendung (oder Prozess) erforderlich, eine Lizenz festzulegen. Die Lizenz kann aus einer Datei geladen werden.

Aspose.Cells Python via versucht, die Lizenz in expliziten Pfadpositionen zu finden.

Es gibt zwei gängige Methoden, um eine Lizenz aus einer Datei anzuwenden.

### **Anwenden einer Lizenz von der Festplatte**

Der einfachste Weg, eine Lizenz festzulegen, besteht darin, die Lizenzdatei im expliziten Pfad abzulegen.

{{< highlight "csharp" >}}

 //Instantiate an instance of license and set the license file through its path

license = License();
 //For Windows
license.set_license("D:\Aspose.Cells.lic");
 //For Linux or MacOS
license.set_license("/home/yourusername/Aspose.Cells.lic"); 
{{< /highlight >}}

{{% alert color="primary" %}}

Wenn Sie das Set anrufen_Lizenzmethode verwenden, sollte der Lizenzname mit dem Namen Ihrer Lizenzdatei identisch sein. Beispielsweise können Sie den Namen der Lizenzdatei in **Aspose.Cells.lic.xml** ändern. Dann sollten Sie in Ihrem Code den geänderten Lizenznamen (**Aspose.Cells.lic.xml**) für das Set verwenden_Lizenzmethode.

{{% /alert %}}


