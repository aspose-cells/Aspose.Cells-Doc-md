---
title: Daten filtern
type: docs
weight: 100
url: /de/net/aspose-cells-griddesktop/filtering-data/
keywords: GridDesktop, Filter, Daten filtern, AutoFilter, RowFilter
description: Dieser Artikel zeigt, wie Daten im Arbeitsblatt in GridDesktop gefiltert werden.
---

{{% alert color="primary" %}} 

**Aspose.Cells.GridDesktop** bietet Auto-Filter und benutzerdefinierte Datenfilterfunktionen für die Benutzer. Mit diesen Funktionen können Sie nur die Elemente aus dem Arbeitsblatt auswählen, die Sie in einer Liste anzeigen möchten. Außerdem können Sie Elemente in einer Liste nach bestimmten Kriterien filtern. Sie können Texte, Zahlen oder Datumsangaben mit der Auto-Filter- / benutzerdefinierten Datenfilterfunktion filtern.

Sie können das boolesche Attribut **EnableAutoFilter** der Klasse **RowFilterSettings** verwenden, um die Auto-Filterfunktion für die GridDesktop-Steuerung zu aktivieren. Es gibt einige andere Eigenschaften der Klasse, die Sie verwenden können, z.B. **HeaderRow**, **StartRow** und **EndRow**, um die Kopfzeile sowie den Start- und Endzeilenindex anzugeben. Die Eigenschaft **Criteria** wird verwendet, um die benutzerdefinierten Filterkriterien festzulegen. Die Klasse hat auch eine Methode namens **FilterRows**, um die gefilterten Zeilen auf der Grundlage der angegebenen Kriterien zu erhalten.

Die Suche nach dem Typ "enthält" (ohne Beachtung der Groß- und Kleinschreibung) im Attribut RowFilter wird ebenfalls von GridDesktop unterstützt. Sie können das Eigenschaft **IgnoreCase** der Klasse **GridColumn** verwenden, um das Attribut für die Groß- und Kleinschreibung zu spezifizieren, das Ihren Anforderungen entspricht. Sie können auch eine Eigenschaft namens **IsStartWithCriteria** der Klasse **GridColumn** verwenden, um anzuzeigen, ob der RowFilter das StartWith-Kriterium in einer Spalte verwendet. Der Standardwert der Eigenschaft ist auf false gesetzt.

{{% /alert %}} 
## **Daten filtern**
Wir implementieren in diesem Beispiel sowohl die Auto-Filter- als auch die benutzerdefinierten Datenfilterfunktionen. Wir füllen eine Datenliste in der GridDesktop ein, aktivieren die Auto-Filterfunktion und suchen dann gefilterte Zeilen basierend auf bestimmten Kriterien.
### **Auto-Filter**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FilteringData-AutoFilter.cs" >}}
### **Benutzerdefinierter Datenfilter**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FilteringData-CustomFilter.cs" >}}
