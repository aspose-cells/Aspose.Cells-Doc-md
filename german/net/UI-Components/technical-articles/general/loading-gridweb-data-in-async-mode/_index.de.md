---
title: Laden von GridWeb Daten im asynchronen Modus
type: docs
weight: 40
url: /de/net/aspose-cells-gridweb/loading-data-in-async-mode/
description: Dieser Artikel beschreibt, wie man den asynchronen Modus verwendet, um eine bessere Leistung in GridWeb zu erzielen.
keywords: GridWeb, Leistung, asynchron, asynchroner Modus
---

{{% alert color="primary" %}} 

Beim Erstellen eines Arbeitsblatts mit großen Datensätzen oder beim Lesen einer großen Microsoft Excel-Datei dauert es sicherlich länger und benötigt mehr Ressourcen. Der Gesamtspeicherbedarf des Prozesses ist immer von Bedenken. Es gibt Maßnahmen, die zur Bewältigung dieser Herausforderung ergriffen werden können. Aspose.Cells.GridWeb bietet einige relevante Optionen und APIs zur Senkung, Reduzierung und Optimierung des Speicherverbrauchs. Außerdem kann es dazu beitragen, dass der Prozess effizienter arbeitet und schneller läuft. Für ein Arbeitsblatt, das große Zelldatensätze enthält, können Sie den Datensatz asynchron laden, was die Gesamtleistung der Benutzererfahrung verbessern kann.

{{% /alert %}} 

Verwenden Sie die Option GridWeb.EnableAsync, um Speicher und Leistung für Zelldaten zu optimieren. Beim Erstellen eines großen Datensatzes für Zellen. Wenn Sie die Option auf true setzen, wird das Laden der Daten nur auf dem aktuellen sichtbaren Fensterbereich basieren. Kurz gesagt, wenn Sie im Zelldatensatz des Arbeitsblatts in GridWeb scrollen, werden neue Fensterdaten basierend auf der aktuellen Scrollposition geladen.

Das folgende Beispiel zeigt, wie der Async-Modus von GridWeb aktiviert wird.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-EnableAsyncMode.aspx-EnableAsync.cs" >}}
