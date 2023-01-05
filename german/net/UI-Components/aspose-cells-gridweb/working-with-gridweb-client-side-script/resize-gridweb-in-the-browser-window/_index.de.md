---
title: Ändern Sie die Größe von GridWeb im Browserfenster
type: docs
weight: 40
url: /de/net/resize-gridweb-in-the-browser-window/
---
## **Mögliche Nutzungsszenarien**
Manchmal möchten Sie, dass Aspose.Cells.GridWeb die Größe selbst in Übereinstimmung mit dem Browserfenster ändert. GridWeb sollte immer seine Größe (Höhe, Breite) anpassen und mit der Größe des Browserfensters kompatibel sein. Aspose.Cells.GridWeb bietet clientseitig*Größe ändern ()* Funktion für den Zweck. Darüber hinaus können Sie die Größe des GridWeb-Steuerelements sogar im Browserfenster ändern. Beispielsweise können Sie den unteren rechten Ziehpunkt (mit der Maus) verwenden, um seine Breite/Höhe im Fenster anzupassen. Sie müssen auch JQuery-JavaScript-Dateien einschließen/angeben, damit sie in der Seitenquelle in Ihrem Projekt funktionieren.
## **Verwenden der Größenänderungsmethode von GridWeb**
Der folgende Code prüft, ob alle 100 Millisekunden eine Größenänderungsaktion stattfindet. Wenn es keine weitere Größenänderungsaktion gibt, dann denkt es, dass die Größenänderungsoperation jetzt beendet ist. Wir verwenden eine Beispielvorlagendatei, die in GridWeb importiert wird. Wir verwenden clientseitigen Code zur Größenänderung des GridWeb. Der Screenshot zeigt, dass sich GridWeb bei der Größenänderung des Browserfensters entsprechend anpasst.

![todo: Bild_alt_Text](resize-gridweb-in-the-browser-window_1.png)
### **Beispielcode**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-ResizeGridWebUsingResizeMethod" >}}


## **Ändern der Größe von GridWeb mithilfe der anpassbaren Jquery-UI-Funktion**
Der folgende Code macht das GridWeb-Steuerelement im Browserfenster in der Größe veränderbar. Beispielsweise können Sie den Griff unten rechts verwenden, um die Größe von GridWeb im Fenster anzupassen. Wir verwenden dieselbe Vorlagendatei, die zuerst in GridWeb importiert wird. Wir verwenden jquery-Skripte, um das GridWeb in der Größe veränderbar zu machen. Der Screenshot zeigt, dass die Größe von GridWeb mit dem unteren rechten Ziehpunkt im Browserfenster geändert wurde.

![todo: Bild_alt_Text](resize-gridweb-in-the-browser-window_2.png)
### **Beispielcode**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-MakingGridWebResizableUsingResizablejQueryUiFeature" >}}
