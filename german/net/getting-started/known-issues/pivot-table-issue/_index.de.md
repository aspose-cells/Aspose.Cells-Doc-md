---
title: Pivot-Tabellenproblem
type: docs
weight: 50
url: /de/net/pivot-table-issue/
---
## **Symptom**
"Ich habe versucht, die generierte Excel-Datei über die Schaltfläche "Öffnen" des IE zu öffnen. Die Excel-Datei wurde durch Lesen einer Excel-Vorlage generiert. Während ich auf die Schaltfläche "Öffnen" klicke, wird sie geöffnet und gleichzeitig erscheint sie Fehlermeldung "Kann Pivot-Tabellen-Quelldatei nicht öffnen.....".

Aber wenn ich die generierte Excel-Datei mit der Schaltfläche "Speichern" speichere und sie aus der Datei aus dem gespeicherten Pfad öffne, wird sie ohne Fehler ordnungsgemäß geöffnet. "
### **Lösung**
Aspose.Cells legt das Pivot-Datenformat fest und zwingt MS Excel, Pivot-Tabellenberichte und andere Berechnungsaufgaben basierend auf der Datenquelle zu erstellen, wenn die Arbeitsmappe in MS Excel geöffnet wird. Also sollte man verwenden**SaveType.OpenInBrowser** anstatt zu verwenden**SaveType.OpenInExcel**Einer der vielen Gründe ist, dass MS Excel die Arbeitsmappendaten nicht parsen konnte, um einen Pivot-Tabellenbericht zu erstellen, wenn Sie die OpenInExcel-Option verwenden, während Sie die generierte Ausgabedatei zur Laufzeit in MS Excel speichern, indem Sie die Schaltfläche „Öffnen“ des Download-Dialogfelds verwenden. Dies wird durch das Dateinamenproblem verursacht. Es ist die Routine von IE, da es so etwas wie "[1]" anhängt, um es als "Dateiname" + "[1]" + ".xls" an den ursprünglichen Namen und somit nichts zu machen tun mit Aspose.Cells. (dh ... es fügt immer "[1]" hinzu, um "Dateiname" + "[1]" + ".xls" zu machen und nicht wie Dateiname.xls). Kurz gesagt, wenn eine Datei eine Pivot-Tabelle enthält, kann sie nicht mit der OpenInExcel SaveType-Option geöffnet werden, und dies gilt für beide, dh wenn Sie die Datei von Grund auf neu erstellen oder eine Vorlagendatei für Quelldaten verwenden, um einen Pivot-Tabellenbericht zu erstellen. Sie sollten also die OpenInBrowser SaveType-Option verwenden, wenn die Datei Pivot-Tabellendaten enthält, um einen Pivot-Tabellenbericht zu erstellen.

Sie sollten Ihren Code ändern und auf SaveType.OpenInBrowser aktualisieren, wenn Sie die Methode Workbook.Save() verwenden

Oder bearbeiten Sie Ihren Code so, dass er „inline“ verwendet, wenn Sie die Option „Anhang“ in Ihrem Code verwenden. dh



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-PivotTableIssue.aspx-PivotTableIssue.cs" >}}
