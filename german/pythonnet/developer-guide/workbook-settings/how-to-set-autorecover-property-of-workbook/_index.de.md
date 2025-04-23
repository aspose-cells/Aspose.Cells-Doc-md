---
title: So legen Sie die Eigenschaft AutoRecover einer Arbeitsmappe fest
type: docs
weight: 220
url: /de/python-net/how-to-set-autorecover-property-of-workbook/
---

{{% alert color="primary" %}}

Sie können Aspose.Cells für Python via .NET verwenden, um die AutoWiederherstellungs-Eigenschaft der Arbeitsmappe zu setzen. Der Standardwert dieser Eigenschaft ist **true**. Wenn Sie ihn auf **false** setzen, deaktiviert Microsoft Excel die AutoWiederherstellung (Autospeichern) bei dieser Excel-Datei.

Aspose.Cells für Python via .NET bietet die [**Workbook.settings.auto_recover**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/auto_recover)-Eigenschaft, um diese Option zu aktivieren oder zu deaktivieren.

{{% /alert %}}

Der folgende Code erklärt, wie man die [**Workbook.settings.auto_recover**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/auto_recover)-Eigenschaft der Arbeitsmappe verwendet. Der Code liest zunächst den Standardwert dieser Eigenschaft, der **true** ist, setzt sie dann auf **false** und speichert die Arbeitsmappe. Anschließend liest er die Arbeitsmappe erneut und liest den Wert dieser Eigenschaft, der zu diesem Zeitpunkt **false** ist.

## C# Code zur Festlegung der AutoRecover-Eigenschaft der Arbeitsmappe

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "WorkbookSettings-SetAutoRecovery.py" >}}

## **Ergebnis**

Hier ist die Konsolenausgabe des obigen Beispielcodes.

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}

