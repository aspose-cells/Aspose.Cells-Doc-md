---
title: Verwenden Sie den Format Pinsel
type: docs
weight: 80
url: /de/net/aspose-cells-griddesktop/use-format-painter/
keywords: GridDesktop,format painter
description: Dieser Artikel stellt den Format Pinsel in GridDesktop vor.
---

{{% alert color="primary" %}} 

Der Format-Pinsel ist eine Funktion von MS Excel, die in Aspose.Cells.GridDesktop übernommen wurde. Es ist eine sehr nützliche Funktion. Für diejenigen, die diese Funktion noch nicht verwendet haben, ermöglicht der Format-Pinsel die Anwendung der Formatierungseinstellungen einer fokussierten Zelle auf eine andere Zelle. Die Umsetzung dieser Funktion ist sehr einfach. In diesem Thema werden wir das ebenfalls behandeln.

{{% /alert %}} 
## **Verwenden des Format-Pinsels**
Die Funktion des **Format-Pinsels** erfordert, dass Benutzer eine Zelle auswählen, deren Formatierungseinstellungen sie auf andere Zellen anwenden möchten, und dann die Methode **StartFormatPainter** von **GridDesktop** aufrufen. Es gibt zwei Modi des Format-Pinsels wie folgt:

- **Einmal Verwenden des Format-Pinsels**
- **Immer Verwenden des Format-Pinsels**
### **Einmal Verwenden des Format-Pinsels**
Wenn Entwickler die Funktion des Format-Pinsels nur einmal verwenden möchten, um die Formatierungseinstellungen einer fokussierten Zelle auf eine einzelne Zelle anzuwenden, können sie dies tun, indem sie die Methode **StartFormatPainter** aufrufen und ihr den Wert **false** übergeben. Dieser **false**-Wert verhindert, dass der Format-Pinsel für immer malt.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseOnce.cs" >}}
### **Immer Verwenden des Format-Pinsels**
Das immer Verwenden des Format-Pinsels ist eine nützliche Funktion, wenn wir die Formatierungseinstellungen auf mehr als eine Zelle anwenden müssen. Entwickler können diese Funktion einfach realisieren, indem sie die Methode **StartFormatPainter** aufrufen und ihr den Wert **true** übergeben.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseAlways.cs" >}}


Eine solche Art des Format-Pinsels malt immer, es sei denn, wir stoppen ihn. Um den Format-Pinsel vom ständigen Malen abzuhalten, können wir einfach die Methode **EndFormatPainter** von **GridDesktop** aufrufen.

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-EndUse.cs" >}}
