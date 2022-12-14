---
title: Verwenden von Format Painter
type: docs
weight: 80
url: /de/net/using-format-painter/
---
{{% alert color="primary" %}} 

Format Painter ist die Funktion von MS Excel, die in Aspose.Cells.GridDesktop angepasst wurde. Es ist eine sehr nette Funktion. Für diejenigen, die diese Funktion noch nicht verwendet haben, ermöglicht Format Painter Benutzern, die Formatierungseinstellungen einer beliebigen fokussierten Zelle auf eine andere Zelle anzuwenden. Die Implementierung dieser Funktion ist sehr einfach. In diesem Thema werden wir auch darauf eingehen.

{{% /alert %}} 
## **Verwenden von Format Painter**
 Das Merkmal von**Format Maler** erfordert, dass Benutzer eine Zelle auswählen, deren Formatierungseinstellungen Sie auf andere Zellen anwenden möchten, und dann aufrufen**FormatPainter starten** Methode**GridDesktop**. Es gibt zwei Format-Painter-Modi:

- **Format Painter einmal verwenden**
- **Format Painter immer verwenden**
### **Format Painter einmal verwenden**
 Wenn Entwickler die Funktion von Format Painter nur einmal verwenden möchten, um die Formatierungseinstellungen einer fokussierten Zelle auf eine einzelne Zelle anzuwenden, können sie dies durch Aufrufen tun**FormatPainter starten** Methode und Bestehen a**FALSCH** Wert dazu. Dies**FALSCH** value verbietet dem Formatmaler für immer, zu malen.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseOnce.cs" >}}
### **Format Painter immer verwenden**
Die Verwendung von Format Painter ist immer eine nützliche Funktion, wenn wir die Formatierungseinstellungen auf mehr als eine Zelle anwenden müssen. Entwickler können diese Funktion durch einen einfachen Aufruf erreichen**FormatPainter starten** Methode und Bestehen a**Stimmt** Wert dazu.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseAlways.cs" >}}


 Diese Art von Formatmaler malt ewig weiter, es sei denn, wir stoppen sie. Um Formatmaler also immer vom Malen abzuhalten, können wir einfach anrufen**EndFormatPainter** Methode von**GridDesktop**.

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-EndUse.cs" >}}
