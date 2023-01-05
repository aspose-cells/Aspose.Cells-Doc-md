---
title: So legen Sie die AutoRecover-Eigenschaft von Workbook fest
type: docs
weight: 220
url: /de/net/how-to-set-autorecover-property-of-workbook/
---
{{% alert color="primary" %}}

Sie können Aspose.Cells verwenden, um die AutoRecover-Eigenschaft der Arbeitsmappe festzulegen. Der Standardwert dieser Eigenschaft ist**wahr** . Wenn Sie es einstellen**FALSCH** In einer Arbeitsmappe deaktiviert Microsoft Excel die automatische Wiederherstellung (automatisches Speichern) für diese Excel-Datei.

 Aspose.Cells bietet[**Arbeitsmappe.Einstellungen.AutoWiederherstellen**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover) -Eigenschaft, um diese Option zu aktivieren oder zu deaktivieren.

{{% /alert %}}

 Der folgende Code erklärt die Verwendung[**Arbeitsmappe.Einstellungen.AutoWiederherstellen**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover) Eigentum der Arbeitsmappe. Der Code liest zuerst den Standardwert dieser Eigenschaft, der ist**wahr** , dann setzt es es als**FALSCH** und speichert die Arbeitsmappe. Dann liest es die Arbeitsmappe erneut und liest den Wert dieser Eigenschaft, der lautet**FALSCH** in diesem Moment.

## C#-Code zum Festlegen der AutoRecover-Eigenschaft von Workbook

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SetAutoRecovery-SetAutoRecovery.cs" >}}

## **Ausgabe**

Hier ist die Konsolenausgabe des obigen Beispielcodes.

{{< highlight "java" >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}
