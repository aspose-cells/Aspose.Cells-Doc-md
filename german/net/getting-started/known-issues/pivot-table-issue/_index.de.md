---
title: Pivot Tabellenproblem
type: docs
weight: 50
url: /de/net/pivot-table-issue/
---

## **Symptom**
„Ich habe versucht, die generierte Excel-Datei über die Schaltfläche „Öffnen“ des IE zu öffnen. Die Excel-Datei wurde durch das Lesen einer Excel-Vorlage generiert. Wenn ich auf die Schaltfläche Öffnen klicke, öffnet sie sich und gleichzeitig wird eine Fehlermeldung angezeigt, die besagt: „Pivot-Tabellenquellendatei kann nicht geöffnet werden.....“.

Aber wenn ich die generierte Excel-Datei mit der Schaltfläche „Speichern“ speichere und sie dann über den gespeicherten Pfad öffne, wird sie ohne Fehler ordnungsgemäß geöffnet.
### **Lösung**
Aspose.Cells setzt das Pivot-Datenformat und zwingt MS Excel, den Pivot-Tabellenbericht und andere Berechnungsaufgaben basierend auf der Datenquelle zu erstellen, wenn die Arbeitsmappe in MS Excel geöffnet wird. Daher sollte man **SaveType.OpenInBrowser** verwenden, anstatt **SaveType.OpenInExcel** zu verwenden. Einer der vielen Gründe ist, wenn Sie beim Speichern der generierten Ausgabedatei in MS Excel zur Laufzeit über die Schaltfläche "Öffnen" des Download-Dialogfelds die Option OpenInExcel verwenden, kann MS Excel die Arbeitsbuchdaten nicht parsen, um den Pivot-Tabellenbericht zu generieren. Dies wird durch das Dateinamenproblem verursacht. Es ist die Routine des IE, da er etwas wie "[1]" hinzufügt, um es als "Dateiname"+"[1]"+".xls" zum ursprünglichen Namen zu machen und somit nichts mit Aspose.Cells zu tun hat. (d.h. es fügt immer "[1]" hinzu, um "Dateiname"+"[1]"+".xls" zu machen und nicht wie dateiname.xls). Kurz gesagt, wenn eine Datei eine Pivot-Tabelle enthält, kann sie nicht mit der Option SaveType.OpenInExcel geöffnet werden, und das gilt sowohl dafür, ob Sie die Datei von Grund auf erstellen oder eine Vorlagendatei für die Quelldaten verwenden, um den Pivot-Tabellenbericht zu erstellen. Daher sollte die SaveType-Option OpenInBrowser verwendet werden, wenn die Datei Pivot-Tabellendaten enthält, um den Pivot-Tabellenbericht zu erstellen.

Sie sollten Ihren Code ändern und auf SaveType.OpenInBrowser aktualisieren, wenn Sie die Workbook.Save() Methode verwenden.

Oder bearbeiten Sie Ihren Code, um "inline" zu verwenden, wenn Sie die Option "Anhang" in Ihrem Code verwenden. d.h.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-PivotTableIssue.aspx-PivotTableIssue.cs" >}}
