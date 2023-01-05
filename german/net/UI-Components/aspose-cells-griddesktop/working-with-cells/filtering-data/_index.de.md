---
title: Filtern von Daten
type: docs
weight: 100
url: /de/net/filtering-data/
---
{{% alert color="primary" %}} 

**Aspose.Cells.GridDesktop** bietet Autofilter- und benutzerdefinierte Datenfilterfunktionen für die Benutzer. Mithilfe dieser Funktionen finden Sie möglicherweise eine Möglichkeit, nur die Elemente aus dem Arbeitsblatt auszuwählen, die Sie in einer Liste anzeigen möchten. Darüber hinaus können Sie Elemente in einer Liste nach festgelegten Kriterien filtern. Sie können Text, Zahlen oder Datumsangaben mit der Funktion Autofilter / benutzerdefinierter Datenfilter filtern.

 Sie können verwenden**AutoFilter aktivieren** Boolesches Attribut von**Zeilenfiltereinstellungen** -Klasse, um das Autofilter-Feature für das GridDesktop-Steuerelement zu aktivieren. Es gibt einige andere Eigenschaften der Klasse, die Sie verwenden können, z**Kopfzeile** , **StartRow** und**EndRow**um die Kopf-, Anfangs- und Endzeilenindizes anzugeben. Das**Kriterien** -Eigenschaft wird verwendet, um die benutzerdefinierten Filterkriterien festzulegen. Die Klasse hat auch eine Methode namens**Filterzeilen** um die gefilterten Zeilen basierend auf den angegebenen Kriterien abzurufen.

 Das Suchattribut vom Typ „enthält“ (Groß-/Kleinschreibung beachten) in RowFilter wird auch von GridDesktop unterstützt. Sie dürfen verwenden**Fall ignorieren** Eigentum von**GridSpalte** -Klasse, um das Groß-/Kleinschreibungsattribut für Ihren Bedarf anzugeben. Sie können auch eine Eigenschaft namens verwenden**IsStartWithCriteria** von**GridSpalte** Klasse, um anzugeben, ob der RowFilter das StartWith-Kriterium für eine Spalte verwendet; der Standardwert der Eigenschaft ist auf false gesetzt.

{{% /alert %}} 
## **Filtern von Daten**
In diesem Beispiel implementieren wir sowohl Autofilter- als auch benutzerdefinierte Datenfilterfunktionen. Wir füllen einige Datenlisten im GridDesktop aus, aktivieren die Auto-Filter-Funktion und suchen dann gefilterte Zeilen basierend auf einigen Kriterien.
### **Automatischer Filter**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FilteringData-AutoFilter.cs" >}}
### **Benutzerdefinierter Datenfilter**


{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-FilteringData-CustomFilter.cs" >}}
