---
title: Wie man Zellen sperrt, um sie zu schützen
type: docs
weight: 130
url: /de/nodejs-cpp/how-to-lock-cells-to-protect-them/
description: Dieser Artikel zeigt Ihnen Code, der erklärt, wie man Zellen mit Aspose.Cells for Node.js via C++ sperrt, um sie zu schützen.
keywords: Node.js Zellen sperren, um sie zu schützen, Wie man Zellen in Node.js sperrt, um sie zu schützen, Zellen in Node.js sperren.
---

## **Mögliche Verwendungsszenarien**
Das Sperren von Zellen zum Schutz ist eine gängige Praxis in Tabellenkalkulationsanwendungen wie Microsoft Excel oder Google Sheets, aus mehreren wichtigen Gründen:

1. Verhinderung unbeabsichtigter Änderungen: Das Sperren von Zellen kann verhindern, dass Benutzer versehentlich wichtige Daten oder Formeln ändern. Dies ist besonders bei komplexen Tabellen sinnvoll, bei denen unbeabsichtigte Änderungen zu erheblichen Fehlern führen können.

1. Erhaltung der Datenintegrität: Durch das Sperren von Zellen können Sie sicherstellen, dass wichtige Daten konsistent und genau bleiben. Dies ist entscheidend für Finanzdokumente, Berichte und andere Dokumente, bei denen Datenintegrität essenziell ist.

1. Kontrollierter Zugriff: In kollaborativen Umgebungen ermöglicht das Sperren von Zellen die Kontrolle darüber, wer bestimmte Teile einer Tabelle bearbeiten darf. Zum Beispiel möchten Sie nur bestimmten Teammitgliedern erlauben, bestimmte Zellen zu bearbeiten, während der Rest des Arbeitsblatts geschützt bleibt.

1. Schutz von Formeln: Formeln sind oft entscheidend für Berechnungen und Datenanalyse. Das Sperren von Zellen, die Formeln enthalten, stellt sicher, dass diese Formeln nicht versehentlich geändert oder gelöscht werden, was die Funktionalität des gesamten Arbeitsblatts stören könnte.

1. Durchsetzung von Geschäftsregeln: In manchen Fällen erfordern bestimmte Geschäftsregeln oder Vorschriften, dass bestimmte Daten vor Änderungen geschützt werden. Das Sperren von Zellen hilft, diese Anforderungen zu erfüllen.

1. Benutzeranleitung: Durch das Sperren von Zellen und das Bereitstellen klarer Anweisungen, welche Zellen bearbeitet werden dürfen, können Sie Benutzer anleiten, wie sie mit der Tabelle interagieren, und Verwirrung sowie Fehler reduzieren.

## **Wie man Zellen in Excel sperrt, um sie zu schützen**
So sperren Sie Zellen in Microsoft Excel:

1. Zellen zum Sperren auswählen: Wählen Sie die Zellen aus, die Sie sperren möchten. Wenn das gesamte Blatt gesperrt werden soll, können Sie diesen Schritt überspringen.
1. Öffnen Sie den Dialog zum Zellenformat: Klicken Sie mit der rechten Maustaste auf die ausgewählten Zellen und wählen Sie „Zellen formatieren“ oder drücken Sie Strg+1.
<br>
<img src="1.png" width=60% />
1. Zellen sperren: Gehen Sie im Dialogfeld „Zellen formatieren“ zum Tab „Schutz“. Aktivieren Sie das Kontrollkästchen „Gesperrt“. Klicken Sie auf „OK“.
1. Arbeitsblatt schützen: Gehen Sie auf die Registerkarte "Überprüfen" im Menüband. Klicken Sie auf "Blatt schützen". Legen Sie ein Passwort fest (optional) und wählen Sie die Berechtigungen, die Sie zulassen möchten (z. B. geschützte Zellen auswählen, Zellen formatieren usw.). Klicken Sie auf "OK."
<br>
<img src="2.png" width=60% />

## **Wie man Zellen in Node.js sperrt, um sie mit Node.js zu schützen**

Aspose.Cells ist eine leistungsstarke Bibliothek für die programmgesteuerte Arbeit mit Excel-Dateien. Um Zellen mit Aspose.Cells for Node.js via C++ zu sperren, müssen Sie diese Schritte befolgen: Laden Sie [Beispieldatei](sample.xlsx), entsperren Sie zuerst alle Zellen (da standardmäßig alle Zellen gesperrt sind, aber erst beim Schutz der Arbeitsmappe durchgesetzt werden), dann sperren Sie die spezifischen Zellen, die Sie schützen möchten, und schützen Sie schließlich das Arbeitsblatt, um die Sperrung durchzusetzen.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-lock-cells-to-protect-them.js" >}}


## **Ausgabeergebnis**
Dieser Code stellt sicher, dass nur die angegebenen Zellen (A1 und B2 in diesem Beispiel) gesperrt sind, und das Arbeitsblatt geschützt ist, um diese Einstellungen durchzusetzen. Alle anderen Zellen im Arbeitsblatt bleiben entsperrt und bearbeitbar.

<br>
<img src="3.png" width=60% />


