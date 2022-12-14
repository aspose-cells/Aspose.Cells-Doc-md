---
title: Weisen Sie dem Formularsteuerelement Makrocode zu
type: docs
weight: 400
url: /de/java/assign-macro-code-to-form-control/
---
{{% alert color="primary" %}} 

 Aspose.Cells ermöglicht es Ihnen, einem Formularsteuerelement wie einem Button einen Makrocode zuzuweisen. Bitte verwenden Sie die[ShapeCollection.addShape()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape\(int,%20int,%20int,%20int,%20int,%20int,%20int\))-Methode, um einem Formularsteuerelement innerhalb der Arbeitsmappe einen neuen Makrocode zuzuweisen.

{{% /alert %}} 
## **Makrocode der Formularsteuerung mit Aspose.Cells zuweisen**
Der folgende Beispielcode erstellt eine neue Arbeitsmappe, weist einem Formular einen Makrocode zu und speichert die Ausgabe im XLSM-Format. Sobald Sie die XLSM-Ausgabedatei in Microsoft Excel öffnen, sehen Sie den folgenden Makrocode.

{{< highlight "java" >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Hier ist ein Beispielcode zum Generieren der XLSM-Ausgabedatei mit Makrocode.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AssignMacroToFormControl-AssignMacroToFormControl.java" >}}
