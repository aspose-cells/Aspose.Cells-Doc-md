---
title: HTML mit StreamProvider speichern
type: docs
weight: 120
url: /de/java/convert-excel-to-html-with-streamprovider/
---

{{% alert color="primary" %}}

Beim Konvertieren von Excel-Dateien, die Bilder und Formen enthalten, in HTML-Dateien stehen wir oft vor den folgenden beiden Problemen:
1. Wo sollten wir die Bilder und Formen speichern, wenn wir die Excel-Datei in eine HTML-Streamdatei speichern.
1. Ersetzen Sie den Standardpfad durch den erwarteten Pfad.

Dieser Artikel erklärt, wie Sie die [**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)-Schnittstelle zur Festlegung der [**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider)-Eigenschaft implementieren. Durch die Implementierung dieser Schnittstelle können die erstellten Ressourcen während der HTML-Generierung an bestimmte Speicherorte oder Speicherströme gespeichert werden.

{{% /alert %}}

## Beispielcode

Dies ist der Hauptcode, der die Verwendung der [**HtmlSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#StreamProvider)-Eigenschaft zeigt

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-HtmlSaveOptions-HtmlSaveOptions.java" >}}

Hier ist der Code für die Klasse *ExportStreamProvider*, die die [**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)-Schnittstelle implementiert, die im obigen Code verwendet wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportStreamProvider-ExportStreamProvider.java" >}}

