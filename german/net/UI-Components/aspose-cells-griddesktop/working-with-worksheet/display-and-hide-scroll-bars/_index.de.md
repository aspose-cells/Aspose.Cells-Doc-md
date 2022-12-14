---
title: Bildlaufleisten anzeigen und ausblenden
type: docs
weight: 140
url: /de/net/display-and-hide-scroll-bars/
---
{{% alert color="primary" %}}

Bildlaufleisten sind nützlich, um durch den Inhalt von Tabellenkalkulationen zu navigieren, die breit und tief sind, d. h. die viele Zeilen und Spalten haben. Die meisten Anwendungen unterstützen zwei Arten von Bildlaufleisten:

- Vertikale Bildlaufleiste
- Horizontale Bildlaufleiste

Beide sind in Microsoft Excel zu finden.

GridDesktop API von Aspose.Cell bietet horizontale und vertikale Bildlaufleisten zum Scrollen durch den Inhalt eines Arbeitsblatts. Mit den Aspose.Cells.GridDesktop-APIs können Entwickler die Sichtbarkeit dieser beiden Bildlaufleisten steuern.

{{% /alert %}}

## **Steuern der Sichtbarkeit der Bildlaufleiste**

Um die Sichtbarkeit der Bildlaufleiste im GridDesktop zu steuern, verwenden Sie die Eigenschaften IsVerticalScrollBarVisible und IsHorizontalScrollBarVisible. Die folgenden Beispiele zeigen, wie Bildlaufleisten ein- und ausgeblendet werden.

### **Programmierbeispiele: Bildlaufleisten ausblenden**

Um Bildlaufleisten auszublenden, setzen Sie die Eigenschaften, die die Sichtbarkeit steuern, auf „false“.

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-DisplayHideScrolBars-HideScrollbars.cs" >}}

### **Programmierbeispiele: Bildlaufleisten sichtbar machen**

Um Bildlaufleisten sichtbar zu machen, setzen Sie die Eigenschaften, die die Sichtbarkeit steuern, auf true.

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-DisplayHideScrolBars-ShowScrollbars.cs" >}}
