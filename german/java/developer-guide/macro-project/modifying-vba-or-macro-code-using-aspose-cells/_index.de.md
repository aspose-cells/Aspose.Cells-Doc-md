---
title: VBA oder Makrocode mit Aspose.Cells ändern
type: docs
weight: 90
url: /de/java/modifying-vba-or-macro-code-using-aspose-cells/
---

{{% alert color="primary" %}} 

Sie können VBA- oder Makrocode mit Aspose.Cells ändern. Aspose.Cells hat die folgenden Klassen hinzugefügt, um das VBA-Projekt in der Excel-Datei zu lesen und zu ändern.

- VbaProject
- VbaModuleCollection
- VbaModule

Dieser Artikel zeigt Ihnen, wie Sie den VBA- oder Makrocode in der Quell-Excel-Datei mithilfe von Aspose.Cells ändern können.

{{% /alert %}} 
## **Beispiel**
Der folgende Beispielcode lädt die Quell-Excel-Datei, die den folgenden VBA- oder Makrocode enthält

{{< highlight java >}}

 Sub Button1_Click()

MsgBox "This is test message."

End Sub

{{< /highlight >}}

Nach der Ausführung des Beispielcodes von Aspose.Cells wird der VBA- oder Makrocode wie folgt modifiziert sein

{{< highlight java >}}

 Sub Button1_Click()

MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

Sie können die [Quell-Excel-Datei](5472596.xlsm) und die [Ausgabedatei](5472597.xlsm) über die angegebenen Links herunterladen.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ModifyVBAorMacroCode-ModifyVBAorMacroCode.java" >}}






