---
title: Makro einer Formularsteuerung mit Golang via C++ zuweisen
linktitle: Weisen Sie einem Formularsteuerelement einen Makrocode zu.
type: docs
weight: 60
url: /de/go-cpp/assign-macro-to-form-control/
description: Erfahren Sie, wie Sie einen Makro Code einer Formularsteuerung wie einer Schaltfläche mit Aspose.Cells for C++ zuweisen.
---

{{% alert color="primary" %}}

Mit Aspose.Cells können Sie einem Formularsteuerelement wie einer Schaltfläche einen Makrocode zuweisen. Verwenden Sie die Eigenschaft [**Shape.GetMacroName()**](https://reference.aspose.com/cells/go-cpp/shape/getmacroname/), um einem Formularsteuerelement in der Arbeitsmappe einen neuen Makrocode zuzuweisen.

{{% /alert %}}

Der folgende Beispielcode erstellt eine neue Arbeitsmappe, weist einer Formularschaltfläche einen Makro-Code zu und speichert die Ausgabe im XLSM-Format. Sobald Sie die ausgegebene XLSM-Datei in Microsoft Excel öffnen, sehen Sie den folgenden Makro-Code.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Makro zu Formularsteuerung in C++ zuweisen**

Hier ist der Beispielcode zum Generieren der Ausgabedatei XLSM mit Makrocode.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AssignMacroToFormControl.go" >}}
