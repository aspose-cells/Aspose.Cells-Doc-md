---
title: Wie man Zahlen im lokalen Sprachformat formatiert
type: docs
weight: 10
url: /de/net/how-to-format-number-to-local-language-format/
description: Dieser Artikel führt in die Formatierung von Zahlen im lokalen Sprachformat mit der Aspose.Cells for .NET API ein.
keywords: Wandle eine Zahl in ein lokales Sprachformat um, Transformiere eine Ziffer in ihr lokales Sprachformat, Ändere eine Zahl in ihr entsprechendes Sprachformat, Formatiere einen numerischen Wert in ein lokales Sprachformat, Drücke eine Zahl als lokales Sprachformat aus, Formatiere Zahl in das lokale Sprachformat.
---

## **Mögliche Verwendungsszenarien**

Das Formatieren von Zahlen in lokalen Formaten in Excel ist unerlässlich, um sicherzustellen, dass Daten klar verstanden, genau interpretiert und professionell präsentiert werden, über verschiedene Regionen und Kulturen hinweg.

1. **Kulturelle und regionale Anpassung**: Verschiedene Regionen verwenden unterschiedliche Zahlenformate für Dezimalzahlen, Tausendertrennzeichen, Währungen und Daten. 
1. **Professionalität und Klarheit**: Die Verwendung lokaler Formate verbessert das professionelle Erscheinungsbild Ihrer Tabellen. Es zeigt Aufmerksamkeit fürs Detail und Rücksichtnahme auf das Publikum, was bei Berichten, Finanzabschlüssen und mit Stakeholdern geteilten Daten entscheidend ist.
1. **Konsistenz bei der Datenanzeige**: Lokale Formatierung sorgt für Konsistenz bei der Zusammenarbeit mit Teams oder Kunden aus verschiedenen Regionen. Sie verhindert Fehler, die durch missverständliche Dateninterpretation entstehen können, wie Verwirrung bei Dezimaltrennzeichen.
1. **Kompatibilität mit externen Systemen**: Beim Exportieren von Daten in andere Formate (z. B. CSV) kann die lokale Formatierung helfen, die Datenintegrität zu erhalten.
1. **Zugänglichkeit und Benutzerfreundlichkeit**: Lokale Formatierung macht Daten für Benutzer zugänglicher, die mit ausländischen Formaten nicht vertraut sind. Beispielsweise hilft die Anzeige von Daten im Format "TT/MM/JJJJ" (häufig im UK) versus "MM/TT/JJJJ" (häufig in den USA) Verwirrung zu vermeiden.
1. **Datenvalidierung und Genauigkeit**: Falsche Formatierung kann zu Berechnungsfehlern führen. Wenn eine Zahl aufgrund von Dezimaltrennzeichen falsch interpretiert wird, könnten Formeln falsche Ergebnisse liefern. Die Verwendung lokaler Formate stellt sicher, dass von Benutzern eingegebene Daten den regionalen Standards entsprechen, was das Risiko von Fehlern bei der Dateneingabe oder -analyse reduziert.

## **Wie man Zahlen in Excel im lokalen Sprachformat formatiert**

Um Zahlen in Excel im lokalen Sprachformat zu formatieren, können Sie verschiedene integrierte Funktionen und Features nutzen, die sich an die regionalen Einstellungen anpassen. 

1. **Verwenden Sie die integrierten Regionaleinstellungen von Excel**: Gehen Sie zu Datei > Optionen > Regionaleinstellungen (oder ähnlich, je nach Excel-Version). Wählen Sie Ihre gewünschte Sprache/Region (z. B. Deutsch für Dezimaltrennzeichen mit Komma, Englisch für Punkt). Bereits bestehende Werte und Formeln werden automatisch in das neue Format umgewandelt.
1. **Verwenden Sie die TEXT-Funktion für benutzerdefinierte, lokal angepasste Formatierung**: Die TEXT-Funktion kann die Zahlenformatierung anhand regional spezifischer Muster erzwingen, was nützlich ist, um Zahlen wie Telefonnummern oder Währungen ohne Änderung der globalen Einstellungen anzuzeigen. Syntax: =TEXT(Wert, "Formatcode")
1. **Programmgesteuerte Handhabung (VBA/APIs)**: Für Entwickler, die VBA verwenden, können Sie NumberFormat mit US-Englisch-Formatstrings verwenden (z. B. "#.##"). Excel passt sich automatisch an die Ländereinstellungen des Benutzers an. Vermeiden Sie NumberFormatLocal, es sei denn, Sie benötigen explizit länderspezifische Formatstrings.
1. **Überschreiben der Systemtrenner für spezielle Fälle**: Wenn das lokalisierte Format unerwartet verhält (z. B. durch Windows-Updates, die Trennzeichen beeinflussen), überschreiben Sie die Standardwerte manuell: Deaktivieren Sie in den Excel-Optionen "Systemtrenner verwenden" und definieren Sie benutzerdefinierte Dezimal- und Tausendertrennzeichen.
1. **Zahl mit benutzerdefiniertem Format formatieren**: Klicken Sie mit der rechten Maustaste auf die Zelle, wählen Sie 'Zellen formatieren', dann finden Sie 'Zahl'->'Benutzerdefiniert' und setzen Sie den gewünschten benutzerdefinierten Zahlentyp. Als Beispiel nehmen wir die Einstellung benutzerdefinierter Zahlenformate in einem chinesischen Umfeld.
<br>
<img src="1.png" width=60% />


## **Wie man Nummern im lokalen Sprachformat in Aspose.Cells for .NET formatiert**

Um Nummern im lokalen Sprachformat in Aspose.Cells for .NET zu formatieren, können Sie das `Style`-Objekt verwenden, das mit einer Zelle oder Zellbereich verbunden ist. Das `Style`-Objekt ermöglicht es, verschiedene Formatierungsoptionen festzulegen, einschließlich benutzerdefinierter Zahlenformate. 

Hier ist ein einfaches Beispiel, wie man ein lokales Sprachzahlformat auf eine Zelle in Aspose.Cells for .NET anwendet:

1. **Verwenden Sie Aspose.Cells**: Stellen Sie sicher, dass Aspose.Cells for .NET in Ihr Projekt eingebunden ist. Sie können es aus NuGet oder von der Aspose-Website beziehen.

2. **Erstellen oder öffnen Sie eine Arbeitsmappe**: Beginnen Sie mit der Erstellung einer neuen Arbeitsmappe oder dem Öffnen einer bestehenden.

3. **Zugriff auf die gewünschte Zelle**: Identifizieren und greifen Sie auf die Zelle oder den Zellbereich zu, den Sie formatieren möchten.

4. **Benutzerdefiniertes Zahlenformat anwenden**: Setzen Sie das Zahlenformat des Zellstils auf ein chinesisches Sprachzahlenformat.

4. **Beispielcode**: Hier ein Codeausschnitt, der diese Schritte demonstriert.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-FormatNumber-To-LocalLanguageFormat.cs" >}}

## **Ausgabe, die durch den Beispielcode generiert wurde**
Hier ist das PDF-Ergebnis des oben genannten Beispielcodes.
<br>
<img src="2.png" width=60% />

{{< app/cells/assistant language="csharp" >}}
