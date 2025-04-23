---
title: HTML in Excel mit StreamProvider laden
type: docs
weight: 80
url: /de/java/convert-html-to-excel-with-streamprovider/
---

{{% alert color="primary" %}} 

Beim Laden von HTML, das externe Ressourcen enthält, stoßen wir oft auf die folgenden zwei Probleme:
1. Wenn der HTML-Stream geladen wird, können die Bilder und externen Ressourcen, auf die die HTML-Datei verweist, nicht über relative Pfade erhalten werden.
1. Externe Ressourcenpfade, auf die in HTML-Dateien verwiesen wird, müssen zugeordnet werden.

In diesem Artikel wird erklärt, wie das [**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)-Interface für die Einstellung der [**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider)-Eigenschaft implementiert wird. Durch die Implementierung dieses Interfaces können externe Ressourcen beim Laden von HTML-Streams geladen werden oder diese externen Ressourcen sind relativ.

{{% /alert %}} 

Dies ist der Hauptcode, der die Verwendung von  [**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider) zeigt



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Load-Html-With-StreamProvider.java" >}}
{{< app/cells/assistant language="java" >}}
