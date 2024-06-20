---
title: Aspose.Cells in Ruby herunterladen und konfigurieren
type: docs
weight: 10
url: /de/java/download-and-configure-aspose-cells-in-ruby/
---

## **Erforderliche Bibliotheken herunterladen**
Laden Sie die unten genannten erforderlichen Bibliotheken herunter. Diese sind erforderlich, um die Aspose.Cells Java für Ruby Beispiele auszuführen.

- [Aspose.Cell für Java Komponente](https://downloads.aspose.com/cells/java/)
## **Beispiele von Social Coding Sites herunterladen**
Folgende Versionen von laufenden Beispielen können auf den unten genannten Social Coding Sites heruntergeladen werden:

**GitHub**

- [Aspose.Cells Java for Ruby](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Ruby)
## **Installation**
Es ist sehr einfach und leicht, das Aspose.cells Java für Ruby Gem zu installieren. Bitte befolgen Sie diese einfachen Schritte:

1. Fügen Sie diese Zeile zur Gemfile Ihrer Anwendung hinzu. 

{{< highlight java >}}

 gem 'aspose-cellsjava'

{{< /highlight >}}

1. Und dann ausführen 

{{< highlight java >}}

 $ bundle

{{< /highlight >}}

**ODER**

1. Führen Sie den folgenden Befehl aus. 

{{< highlight java >}}

 $ gem install aspose-cellsjava

{{< /highlight >}}
## **Verwendung**
Fügen Sie die erforderlichen Dateien hinzu, um mit dem helloworld Beispiel zu arbeiten.

{{< highlight java >}}

 require require File.dirname(File.dirname(File.dirname(__FILE__))) + '/lib/aspose-cellsjava'

include Asposecellsjava

include Asposecellsjava::HelloWorld

initialize_aspose_cells

{{< /highlight >}}

Lassen Sie uns den obigen Code verstehen.

1. Die erste Zeile stellt sicher, dass Aspose Cells geladen und verfügbar ist.
1. Fügen Sie die Dateien hinzu, die erforderlich sind, um auf Aspose Cells zuzugreifen.
1. Initialisieren Sie die Bibliotheken. Die Aspose JAVA-Klassen werden aus dem im aspose.yml-Datei bereitgestellten Pfad geladen/
