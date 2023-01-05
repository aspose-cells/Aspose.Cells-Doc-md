---
title: Laden Sie HTML mit StreamProvider in Excel
type: docs
weight: 80
url: /de/net/convert-html-to-excel-with-streamprovider/
---
{{% alert color="primary" %}} 

Beim Laden von HTML-Feldern, die externe Ressourcen enthalten, treten häufig die folgenden zwei Probleme auf:
1. Wenn der HTML-Stream geladen wird, können die Bilder und externen Ressourcen, auf die von der HTML-Datei verwiesen wird, nicht über relative Pfade abgerufen werden.
1. Externe Ressourcenpfade, auf die in HTML-Dateien verwiesen wird, müssen zugeordnet werden

 In diesem Artikel wird die Implementierung erläutert[IStreamProvider](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) Schnittstelle zum Einstellen der[HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/) Eigentum. Durch Implementieren dieser Schnittstelle können Sie externe Ressourcen während des Ladens von HTML-Streams laden oder diese externen Ressourcen sind relativ.

{{% /alert %}} 

 Dies ist der Hauptcode, der die Verwendung von zeigt[HtmlLoadOptions.StreamProvider](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/streamprovider/)Eigentum



{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Load-Html-With-StreamProvider.cs" >}}
