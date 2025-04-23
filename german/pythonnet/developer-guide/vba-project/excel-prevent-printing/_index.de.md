---
title: Wie verhindert man, dass Benutzer eine Excel Datei drucken
type: docs
weight: 600
url: /de/python-net/how-to-prevent-printing-excel/
description: Erfahren Sie, wie man verhindert, dass Benutzer Excel drucken, mittels der Aspose.Cells for Python via .NET API.
keywords: Excel Druck, Excel Druck verhindern, wie man das Drucken von Excel verhindert, Excel Druck verhindern, das Drucken des gesamten Arbeitsmappens mit VBA verhindern 
---

## **Mögliche Verwendungsszenarien**
In unserer täglichen Arbeit kann in der Excel-Datei wichtige Informationen enthalten sein. Um ein Ausbreiten interner Daten zu verhindern, erlaubt uns das Unternehmen nicht, sie zu drucken. Dieses Dokument zeigt Ihnen, wie Sie verhindern können, dass andere Excel-Dateien drucken.

## **Wie man das Drucken einer Datei in MS-Excel verhindert**
Sie können den folgenden VBA-Code anwenden, um Ihre spezifische Datei vor dem Drucken zu schützen.
1. Öffnen Sie Ihre Arbeitsmappe, die Sie anderen nicht erlauben möchten zu drucken.
1. Wählen Sie das Register „Entwicklertools“ in der Excel-Menüleiste aus und klicken Sie auf die Schaltfläche „Code anzeigen“ im Abschnitt „Steuerlemente“. Alternativ können Sie die ALT + F11-Tasten gedrückt halten, um das Fenster „Microsoft Visual Basic for Applications“ zu öffnen.
<br>
<img src="1.png" width=70% />
1. Klicken Sie dann im linken Projekt-Explorer doppelt auf ThisWorkbook, um das Modul zu öffnen, und fügen Sie einige VBA-Codes hinzu.
<br>
<img src="2.png" width=70% />
1. Speichern Sie dann diesen Code und schließen Sie ihn, kehren Sie zur Arbeitsmappe zurück und wenn Sie die Beispieldatei drucken, wird das Drucken nicht erlaubt und Sie erhalten folgendes Warnfeld:
<br>
<img src="3.png" width=70% />

## **So verhindern Sie, dass Benutzer Excel-Dateien mit Aspose.Cells for Python via .NET drucken**

Der folgende Beispielcode veranschaulicht, wie man das Drucken von Excel-Dateien verhindert:

1. Laden Sie die [Beispieldatei](sample.xlsx).
1. Holen Sie sich das VbaModuleCollection-Objekt aus der VbaProject-Eigenschaft der Arbeitsmappe.
1. Holen Sie das VbaModule-Objekt über den Namen „ThisWorkbook“.
1. Setzen Sie die Eigenschaften des VbaModule-Codes.
1. Speichern Sie die Beispieldatei im [xlsm-Format](out.xlsm).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-Prevent-printing-excel.py" >}}

