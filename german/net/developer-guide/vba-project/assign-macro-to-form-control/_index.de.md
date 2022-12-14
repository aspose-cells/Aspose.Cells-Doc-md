---
title: Makro dem Formularsteuerelement zuweisen
type: docs
weight: 60
url: /de/net/assign-macro-to-form-control/
---
{{% alert color="primary" %}}

 Aspose.Cells ermöglicht es Ihnen, einem Formularsteuerelement wie einem Button einen Makrocode zuzuweisen. Bitte verwenden Sie die[**Shape.MarcoName**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/macroname) -Eigenschaft, um einem Formularsteuerelement in der Arbeitsmappe einen neuen Makrocode zuzuweisen.

{{% /alert %}}

Der folgende Beispielcode erstellt eine neue Arbeitsmappe, weist einer Formularschaltfläche einen Makrocode zu und speichert die Ausgabe im XLSM-Format. Sobald Sie die XLSM-Ausgabedatei in Microsoft Excel öffnen, sehen Sie den folgenden Makrocode.

{{< highlight "java" >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Weisen Sie dem Formularsteuerelement in C# ein Makro zu**

Hier ist der Beispielcode zum Generieren der XLSM-Ausgabedatei mit Makrocode.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AssignMacroToFormControl-1.cs" >}}
