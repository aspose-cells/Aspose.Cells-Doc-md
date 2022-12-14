---
title: Laden Sie HTML mit StreamProvider in Excel
type: docs
weight: 80
url: /de/java/convert-html-to-excel-with-streamprovider/
---
{{% alert color="primary" %}} 

Beim Laden von HTML, das externe Ressourcen enthält, treten häufig die folgenden zwei Probleme auf:
1. Wenn der HTML-Stream geladen wird, können die Bilder und externen Ressourcen, auf die von der HTML-Datei verwiesen wird, nicht über relative Pfade abgerufen werden.
1. Externe Ressourcenpfade, auf die in HTML-Dateien verwiesen wird, müssen zugeordnet werden.

 In diesem Artikel wird die Implementierung erläutert[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) Schnittstelle zum Einstellen der[**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider) Eigentum. Durch Implementieren dieser Schnittstelle können Sie externe Ressourcen während des Ladens von HTML-Streams laden oder diese externen Ressourcen sind relativ.

{{% /alert %}} 

 Dies ist der Hauptcode, der die Verwendung von zeigt[**HtmlLoadOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#StreamProvider)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Load-Html-With-StreamProvider.java" >}}
