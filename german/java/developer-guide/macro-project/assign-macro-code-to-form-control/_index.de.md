---
title: Makrocode einer Steuerelementform zuweisen
type: docs
weight: 400
url: /de/java/assign-macro-code-to-form-control/
---

{{% alert color="primary" %}} 

Aspose.Cells erlaubt die Zuordnung eines Makro-Codes zu einem Formularsteuerungselement wie einem Button. Verwenden Sie die Methode [ShapeCollection.addShape()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape-int-int-int-int-int-int-int-) um einen neuen Makro-Code einem Formularsteuerungselement im Arbeitsbuch zuzuordnen.

{{% /alert %}} 
## **Makrocode einer Steuerelementform zuweisen mit Aspose.Cells**
Der folgende Beispielcode erstellt eine neue Arbeitsmappe, weist einem Steuerelement wie einer Schaltfläche Makrocode zu und speichert die Ausgabe im XLSM-Format. Wenn Sie die Ausgabedatei XLSM in Microsoft Excel öffnen, werden Sie den folgenden Makrocode sehen.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Hier ist ein Beispielcode, um die Ausgabedatei XLSM mit Makrocode zu generieren.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AssignMacroToFormControl-AssignMacroToFormControl.java" >}}
{{< app/cells/assistant language="java" >}}
