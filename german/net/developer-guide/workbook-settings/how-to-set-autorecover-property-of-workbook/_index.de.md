---
title: So legen Sie die Eigenschaft AutoRecover einer Arbeitsmappe fest
type: docs
weight: 220
url: /de/net/how-to-set-autorecover-property-of-workbook/
---

{{% alert color="primary" %}}

Mit Aspose.Cells können Sie die AutoRecover-Eigenschaft der Arbeitsmappe festlegen. Der Standardwert dieser Eigenschaft ist **true**. Wenn Sie sie auf einer Arbeitsmappe auf **false** setzen, deaktiviert Microsoft Excel die AutoRecover (Autosave)-Funktion für diese Excel-Datei.

Aspose.Cells bietet die [**Workbook.Settings.AutoRecover**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover)-Eigenschaft, um diese Option zu aktivieren oder zu deaktivieren.

{{% /alert %}}

Der folgende Code erklärt, wie man die [**Workbook.Settings.AutoRecover**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover)-Eigenschaft der Arbeitsmappe verwendet. Der Code liest zuerst den Standardwert dieser Eigenschaft, der **true** ist, dann setzt er ihn auf **false** und speichert die Arbeitsmappe. Dann liest er die Arbeitsmappe erneut und liest den Wert dieser Eigenschaft, der zu diesem Zeitpunkt **false** ist.

## C# Code zur Festlegung der AutoRecover-Eigenschaft der Arbeitsmappe

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SetAutoRecovery-SetAutoRecovery.cs" >}}

## **Ergebnis**

Hier ist die Konsolenausgabe des obigen Beispielcodes.

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
