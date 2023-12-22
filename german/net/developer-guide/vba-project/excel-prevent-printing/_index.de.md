---
title: So verhindern Sie, dass Benutzer eine Excel-Datei drucken
type: docs
weight: 600
url: /de/net/how-to-prevent-printing-excel/
description: Erfahren Sie, wie Sie Benutzer daran hindern, Excel über Aspose.Cells for .NET API zu drucken.
keywords: excel printing, prevent printing excel, how to prevent users from printing excel, excel prevent printing, prevent printing workbook, Prevent users from printing the whole workbook with VBA. 
---
##  **Mögliche Nutzungsszenarien**
Bei unserer täglichen Arbeit kann es sein, dass die Excel-Datei einige wichtige Informationen enthält. Um die interne Datenweitergabe zu schützen, erlaubt uns das Unternehmen nicht, diese auszudrucken. In diesem Dokument erfahren Sie, wie Sie andere am Drucken von Excel-Dateien hindern.

##  **So verhindern Sie, dass Benutzer Dateien in MS-Excel drucken**
Sie können den folgenden VBA-Code anwenden, um Ihre spezifische zu druckende Datei zu schützen.
1. Öffnen Sie Ihre Arbeitsmappe, deren Drucken Sie anderen nicht erlauben.
1. Wählen Sie im Excel-Menüband die Registerkarte „Entwickler“ aus und klicken Sie im Abschnitt „Steuerelemente“ auf die Schaltfläche „Code anzeigen“. Alternativ können Sie die Tasten ALT + F11 gedrückt halten, um das Fenster Microsoft Visual Basic für Applikationen zu öffnen.
<br>
<img src="1.png" width=70% />
1. Doppelklicken Sie dann im linken Projekt-Explorer auf „DieseArbeitsmappe“, um das Modul zu öffnen, und fügen Sie einige VBA-Codes hinzu.
<br>
<img src="2.png" width=70% />
1. Speichern und schließen Sie dann diesen Code und gehen Sie zur Arbeitsmappe zurück. Wenn Sie nun die Beispieldatei drucken, ist das Drucken nicht zulässig und Sie erhalten die folgende Warnmeldung:
<br>
<img src="3.png" width=70% />

##  **So verhindern Sie, dass Benutzer Excel-Dateien mit Aspose.Cells for .NET drucken**

Der folgende Beispielcode veranschaulicht, wie Benutzer daran gehindert werden, eine Excel-Datei zu drucken:

1.  Laden Sie die[Beispieldatei](sample.xlsx).
1. Rufen Sie das VbaModuleCollection-Objekt aus der VbaProject-Eigenschaft von Workbook ab.
1. Rufen Sie das VbaModule-Objekt über den Namen „ThisWorkbook“ ab.
1. Legen Sie die codes-Eigenschaft von VbaModule fest.
1.  Speichern Sie die Beispieldatei unter[XLSM-Format](out.xlsm).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "VBA-Prevent-printing-excel.cs" >}}