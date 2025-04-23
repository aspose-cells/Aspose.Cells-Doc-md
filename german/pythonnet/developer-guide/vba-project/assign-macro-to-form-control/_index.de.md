---
title: Weisen Sie einem Formularsteuerelement einen Makrocode zu.
type: docs
weight: 60
url: /de/python-net/assign-macro-to-form-control/
---

{{% alert color="primary" %}}

Aspose.Cells für Python via .NET ermöglicht es, einem Formularsteuerung-Element wie einem Button einen Makro-Code zuzuweisen. Bitte verwenden Sie die Eigenschaft [**Shape.macro_name**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/macro_name), um einen neuen Makro-Code einer Formularsteuerung im Arbeitsbuch zuzuweisen.

{{% /alert %}}

Der folgende Beispielcode erstellt eine neue Arbeitsmappe, weist einer Schaltfläche ein Makro zu und speichert die Ausgabe im XLSM-Format. Wenn Sie die Ausgabedatei in Microsoft Excel öffnen, wird der folgende Makrocode angezeigt.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Makro einer Formularsteuerung in Python zuweisen**

Hier ist der Beispielcode zum Generieren der Ausgabedatei XLSM mit Makrocode.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-AssignMacroToFormControl-1.py" >}}
