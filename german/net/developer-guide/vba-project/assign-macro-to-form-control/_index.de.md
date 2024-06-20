---
title: Weisen Sie einem Formularsteuerelement einen Makrocode zu.
type: docs
weight: 60
url: /de/net/assign-macro-to-form-control/
---

{{% alert color="primary" %}}

Mit Aspose.Cells können Sie einem Formularsteuerelement wie einer Schaltfläche einen Makrocode zuweisen. Verwenden Sie die Eigenschaft [**Shape.MarcoName**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/macroname), um einem Formularsteuerelement in der Arbeitsmappe einen neuen Makrocode zuzuweisen.

{{% /alert %}}

Der folgende Beispielcode erstellt eine neue Arbeitsmappe, weist einer Schaltfläche ein Makro zu und speichert die Ausgabe im XLSM-Format. Wenn Sie die Ausgabedatei in Microsoft Excel öffnen, wird der folgende Makrocode angezeigt.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Makro einem Formularsteuerelement in C# zuweisen**

Hier ist der Beispielcode zum Generieren der Ausgabedatei XLSM mit Makrocode.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AssignMacroToFormControl-1.cs" >}}
