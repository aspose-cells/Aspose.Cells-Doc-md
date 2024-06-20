---
title: Lizenzierung
type: docs
weight: 21
url: /de/python-net/licensing/
---

{{% alert color="primary" %}}

Sie können ganz einfach eine Evaluierungsversion von Aspose.Cells Python via .Net von seiner [Download-Seite](https://pypi.org/project/aspose-cells-python/) bei Pypi-Repos herunterladen. Die Evaluierungsversion bietet absolut dieselben Funktionen wie die lizenzierte Version des Komponenten. Darüber hinaus wird die Evaluierungsversion einfach lizenziert, wenn Sie eine Lizenz erwerben und einige Zeilen Code hinzufügen, um die Lizenz anzuwenden.

{{% /alert %}}

## **Evaluierungsversion-Beschränkungen**

Die Evaluierungsversion des Aspose.Cells Python via .NET-Produkts (ohne spezifizierte Lizenz) bietet volle Produktfunktionalität, ist jedoch auf das Öffnen von 100 Dateien in einem Programm und ein zusätzliches Arbeitsblatt mit Evaluierungswasserzeichen beschränkt.

Die Beschränkungen werden unten angezeigt:

- **Anzahl der geöffneten Dateien** (Aspose.Cells Python über .Net)
  Beim Ausführen Ihres Programms können Sie nur 100 Excel-Dateien mit der Aspose.Cells Python über .Net-Bibliothek öffnen. Wenn Ihre Anwendung diese Anzahl überschreitet, wird eine Ausnahme ausgelöst.


Darüber hinaus wird in der generierten Excel-Datei mit der Aspose.Cells Python über Bibliothek stets ein Arbeitsblatt mit Evaluierungswasserzeichen als aktives Arbeitsblatt angezeigt. Nur in der lizenzierten Version können Sie das aktive Arbeitsblatt auf andere Arbeitsblätter festlegen. In der Ausgabe-PDF- oder Bilddatei von Aspose.Cells Python via wird ein Evaluierungswasserzeichen oben im Dokument/Bild eingefügt.

{{% alert color="primary" %}}

Wenn Sie die Aspose.Cells Python via ohne Evaluierungsversionseinschränkungen testen möchten, können Sie auch eine [30-tägige temporäre Lizenz](https://purchase.aspose.com/temporary-license) anfordern.

{{% /alert %}}

## **Lizenzierung in Aspose.Cells Python über Komponente**

Die Lizenz ist eine einfache Text-XML-Datei, die Details wie den Produktnamen, die Anzahl der lizenzierten Entwickler, das Ablaufdatum des Abonnements usw. enthält. Die Datei ist digital signiert, daher darf sie nicht geändert werden. Selbst das unbeabsichtigte Hinzufügen eines zusätzlichen Zeilenumbruchs in die Datei macht sie ungültig. Sie müssen eine Lizenz setzen, um die Evaluierungseinschränkung von Aspose.Cells Python via zu vermeiden. Es ist nur einmal pro Anwendung (oder Prozess) erforderlich, eine Lizenz festzulegen. Die Lizenz kann aus einer Datei geladen werden.

Aspose.Cells Python via versucht, die Lizenz an expliziten Pfadstandorten zu finden.

Es gibt zwei gängige Methoden, um eine Lizenz aus einer Datei anzuwenden.

### **Lizenzierung von der Festplatte**

Der einfachste Weg, um eine Lizenz festzulegen, besteht darin, die Lizenzdatei an den expliziten Pfad zu legen.

{{< highlight csharp >}}

# Instantiate an instance of license and set the license file through its path

license = License();
# For Windows
license.set_license("D:\Aspose.Cells.lic");
# For Linux or MacOS
license.set_license("/home/yourusername/Aspose.Cells.lic"); 
{{< /highlight >}}

{{% alert color="primary" %}}

Wenn Sie die set_license-Methode aufrufen, sollte der Lizenzname dem Namen Ihrer Lizenzdatei entsprechen. Sie können beispielsweise den Namen der Lizenzdatei in **Aspose.Cells.lic.xml** ändern. Dann sollten Sie in Ihrem Code den modifizierten Lizenznamen (**Aspose.Cells.lic.xml**) für die set_license-Methode verwenden.

{{% /alert %}}


