---
title: Laden Sie Aspose.Cells in Ruby herunter und konfigurieren Sie es
type: docs
weight: 10
url: /de/java/download-and-configure-aspose-cells-in-ruby/
---
## **Erforderliche Bibliotheken herunterladen**
Laden Sie die unten aufgeführten erforderlichen Bibliotheken herunter. Diese sind für die Ausführung von Aspose.Cells Java für Ruby-Beispiele erforderlich.

- [Aspose.Cell for Java Komponente](https://downloads.aspose.com/cells/java/)
## **Laden Sie Beispiele von Social-Coding-Sites herunter**
Die folgenden Versionen von Laufbeispielen stehen auf den unten genannten Social-Coding-Sites zum Download zur Verfügung:

**GitHub**

- [Aspose.Cells Java für Rubin](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Ruby)
## **Installieren**
Es ist sehr einfach und leicht, Aspose.cells Java für Ruby Gem zu installieren, bitte folgen Sie diesen einfachen Schritten:

1.  Fügen Sie diese Zeile dem Gemfile Ihrer Anwendung hinzu.

{{< highlight "java" >}}

 gem 'aspose-cellsjava'

{{< /highlight >}}

1.  Und dann ausführen

{{< highlight "java" >}}

 $ bundle

{{< /highlight >}}

**ODER**

1.  Führen Sie folgenden Befehl aus.

{{< highlight "java" >}}

 $ gem install aspose-cellsjava

{{< /highlight >}}
## **Verwenden**
Fügen Sie die erforderlichen Dateien für die Arbeit mit dem helloworld-Beispiel hinzu.

{{< highlight "java" >}}

 require require File.dirname(File.dirname(File.dirname(__FILE__))) + '/lib/aspose-cellsjava'

include Asposecellsjava

include Asposecellsjava::HelloWorld

initialize_aspose_cells

{{< /highlight >}}

Lassen Sie uns den obigen Code verstehen.

1. Die erste Zeile stellt sicher, dass die Aspose-Zellen geladen und verfügbar sind.
1. Schließen Sie die Dateien ein, die für den Zugriff auf die Aspose-Zellen erforderlich sind.
1. Initialisieren Sie die Bibliotheken. Die aspose-JAVA-Klassen werden aus dem Pfad geladen, der in der Datei aspose.yml angegeben ist/
