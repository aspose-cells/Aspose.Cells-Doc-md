---
title: GridWeb im Browserfenster anpassen
type: docs
weight: 40
url: /de/net/aspose-cells-gridweb/resize-gridweb-in-the-browser-window/
keywords: GridWeb, anpassen
description: Dieser Artikel zeigt, wie man in GridWeb anpasst.
---

## **Mögliche Verwendungsszenarien**
Manchmal möchten Sie, dass Aspose.Cells.GridWeb sich entsprechend dem Browserfenster selbst anpasst. Möglicherweise müssen Sie möchten, dass GridWeb seine Größe (Höhe, Breite) anpasst und mit der Größe des Browserfensters kompatibel ist. Aspose.Cells.GridWeb bietet clientseitige *resize()*-Funktion zu diesem Zweck. Darüber hinaus können Sie sogar die GridWeb-Steuerung im Browserfenster vergrößerbar machen. Sie können beispielsweise den unteren rechten Griff (über die Maus) verwenden, um die Breite/Höhe an das Fenster anzupassen. Sie müssen auch jquery-Javascript-Dateien in Ihrer Projektquellcodedatei angeben/einschließen, um es auf Ihrer Seite zum funktionieren zu bringen.
## **Mit der resize-Methode von GridWeb**
Der folgende Code überprüft, ob eine Größenänderung alle 100 Millisekunden stattfindet. Wenn keine Größenänderung mehr stattfindet, wird angenommen, dass die Größenänderung jetzt abgeschlossen ist. Wir verwenden eine Beispielvorlagendatei, die in GridWeb importiert wird. Wir verwenden clientseitigen Code, um GridWeb anzupassen. Der Screenshot zeigt, dass GridWeb sich entsprechend anpasst, wenn das Browserfenster vergrößert wird.

![todo:image_alt_text](resize-gridweb-in-the-browser-window_1.png)
### **Beispielcode**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-ResizeGridWebUsingResizeMethod" >}}


## **GridWeb durch die vergrößerungs jquery ui-Funktion vergrößerbar machen**
Der folgende Code wird die GridWeb-Steuerung im Browserfenster vergrößerbar machen. Sie können beispielsweise den unteren rechten Griff verwenden, um die Größe von GridWeb im Browserfenster anzupassen. Wir verwenden die gleiche Vorlagendatei, die zuerst in GridWeb importiert wird. Wir verwenden jquery-Skripte, um GridWeb vergrößerbar zu machen. Der Screenshot zeigt, dass GridWeb mithilfe seines unteren rechten Griffes im Browserfenster vergrößert wurde.

![todo:image_alt_text](resize-gridweb-in-the-browser-window_2.png)
### **Beispielcode**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-MakingGridWebResizableUsingResizablejQueryUiFeature" >}}
