---
title: Wie man Zellen sperrt, um sie zu schützen
type: docs
weight: 130
url: /de/net/how-to-lock-cells-to-protect-them/
description: Dieser Artikel zeigt Ihnen den Code, der erklärt, wie man Zellen sperrt, um sie mit der Aspose.Cells Bibliothek zu schützen.
keywords: C# Zellen sperren, um sie zu schützen, Wie man Zellen in C# schützt, Zellen in C# schützen.
---

## **Mögliche Verwendungsszenarien**
Das Sperren von Zellen zum Schutz ist eine gängige Praxis in Tabellenkalkulationsanwendungen wie Microsoft Excel oder Google Sheets aus mehreren wichtigen Gründen:

1. Verhindern von unbeabsichtigten Änderungen: Durch das Sperren von Zellen können Benutzer daran gehindert werden, wichtige Daten oder Formeln versehentlich zu ändern. Dies ist besonders nützlich in komplexen Tabellenkalkulationen, wo unbeabsichtigte Änderungen zu erheblichen Fehlern führen können.

1. Aufrechterhaltung der Datenintegrität: Durch das Sperren von Zellen können Sie sicherstellen, dass kritische Daten konsistent und genau bleiben. Dies ist besonders wichtig für Finanzdokumente, Berichte und andere Dokumente, bei denen die Datenintegrität wesentlich ist.

1. Kontrollierter Zugriff: In kollaborativen Umgebungen ermöglicht das Sperren von Zellen die Kontrolle darüber, wer bestimmte Teile einer Tabelle bearbeiten kann. Zum Beispiel möchten Sie möglicherweise nur bestimmten Teammitgliedern die Bearbeitung bestimmter Zellen erlauben, während der Rest des Arbeitsblatts geschützt bleibt.

1. Schutz von Formeln: Formeln sind oft entscheidend für Berechnungen und Datenanalyse. Das Sperren von Zellen, die Formeln enthalten, stellt sicher, dass diese Formeln nicht versehentlich geändert oder gelöscht werden, was die Funktionalität des gesamten Arbeitsblatts beeinträchtigen könnte.

1. Einhaltung von Geschäftsregeln: In einigen Fällen können spezifische Geschäftsregeln oder Vorschriften erfordern, dass bestimmte Daten vor Änderungen geschützt werden. Das Sperren von Zellen hilft, diese Anforderungen zu erfüllen.

1. Benutzerführung: Durch das Sperren von Zellen und das Bereitstellen klarer Anweisungen, welche Zellen bearbeitet werden können, können Sie Benutzer anleiten, wie sie mit der Tabelle interagieren können, wodurch Verwirrung und Fehler reduziert werden.

## **Wie man Zellen in Excel sperrt, um sie zu schützen**
So können Sie Zellen in Microsoft Excel sperren:

1. Wählen Sie die zu sperrenden Zellen aus: Wählen Sie die Zellen aus, die Sie sperren möchten. Wenn Sie das gesamte Blatt sperren möchten, können Sie diesen Schritt überspringen.
1. Öffnen Sie den Dialog Zellen formatieren: Klicken Sie mit der rechten Maustaste auf die ausgewählten Zellen und wählen Sie "Zellen formatieren" oder drücken Sie Strg+1.
<br>
<img src="1.png" width=60% />
1. Sperren Sie die Zellen: Gehen Sie im Dialogfeld Zellen formatieren zum Tab "Schutz". Aktivieren Sie das Kontrollkästchen "Gesperrt". Klicken Sie auf "OK".
1. Schützen Sie das Arbeitsblatt: Gehen Sie zum Reiter "Überprüfen" im Menüband. Klicken Sie auf "Blatt schützen". Legen Sie ein Passwort fest (optional) und wählen Sie die Berechtigungen aus, die Sie zulassen möchten (z. B. Auswahl gesperrter Zellen, Zellen formatieren usw.). Klicken Sie auf "OK".
<br>
<img src="2.png" width=60% />

## **Wie man Zellen mit C# sperrt, um sie zu schützen**

Aspose.Cells ist eine leistungsstarke Bibliothek zur programmgesteuerten Arbeit mit Excel-Dateien. Um Zellen mit Aspose.Cells zu sperren, müssen Sie die folgenden Schritte befolgen: Laden Sie [Beispieldatei](sample.xlsx), entsperren Sie zuerst alle Zellen (standardmäßig sind alle Zellen gesperrt, aber nicht erzwungen, bis das Arbeitsblatt geschützt ist), sperren Sie dann die spezifischen Zellen, die Sie schützen möchten, und schützen Sie schließlich das Arbeitsblatt, um die Sperrung zu erzwingen.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "CellsData-lock-cells-to-protect-them.cs" >}}

## **Ergebnisausgabe**
Dieser Code stellt sicher, dass nur die angegebenen Zellen (A1 und B2 in diesem Beispiel) gesperrt sind, und das Arbeitsblatt ist geschützt, um diese Einstellungen zu erzwingen. Alle anderen Zellen im Arbeitsblatt bleiben entsperrt und bearbeitbar.

<br>
<img src="3.png" width=60% />


