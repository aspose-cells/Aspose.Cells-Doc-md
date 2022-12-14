---
title: Laden von GridWeb-Daten im Async-Modus
type: docs
weight: 40
url: /de/net/loading-gridweb-data-in-async-mode/
---
{{% alert color="primary" %}} 

Wenn Sie eine Arbeitsmappe mit großen Datensätzen erstellen oder eine große Microsoft-Excel-Datei lesen, wird dies sicherlich mehr Zeit und Ressourcen in Anspruch nehmen. Der Gesamtspeicher, den der Prozess benötigt, ist immer ein Problem. Es gibt Maßnahmen, die zur Bewältigung der Herausforderung ergriffen werden können. Aspose.Cells.GridWeb bietet einige relevante Optionen und APIs zum Senken, Reduzieren und Optimieren der Speichernutzung. Außerdem kann es dazu beitragen, dass der Prozess effizienter arbeitet und schneller abläuft. Für ein Arbeitsblatt, das Daten aus großen Zellen enthält, können Sie das Dataset asynchron laden, was die Gesamtleistung für die Benutzererfahrung verbessern kann.

{{% /alert %}} 

Verwenden Sie die GridWeb.EnableAsync-Option, um Speicher und Leistung für Zellendaten zu optimieren. Beim Erstellen eines großen Datensatzes für Zellen. Wenn Sie die Option auf „true“ setzen, basiert das Laden der Daten nur auf dem aktuell sichtbaren Windows-Bereich. Kurz gesagt, wenn Sie in den Zellendaten des Arbeitsblatts in GridWeb scrollen, werden neue Windows-Daten nur basierend auf der aktuellen Scrollposition geladen.

Das folgende Beispiel zeigt, wie der asynchrone Modus von GridWeb aktiviert wird.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-EnableAsyncMode.aspx-EnableAsync.cs" >}}
