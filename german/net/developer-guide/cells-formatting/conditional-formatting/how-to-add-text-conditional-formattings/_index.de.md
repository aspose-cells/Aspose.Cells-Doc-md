---
title: Wie man Text Bedingte Formatierung hinzufügt
description: Wie man die Aspose.Cells Bibliothek in C# verwendet, um Text Bedingte Formatierung anzuwenden. Durch die Anpassung dieser Kriterien haben Sie mehr Kontrolle darüber, wie Zellen aussehen und erscheinen.
keywords: Aspose.Cells, Text Bedingte Formatierung, C#, Bedingung, Formatierung
type: docs
weight: 70
url: /de/net/how-to-add-text-conditional-formatting/
---

## **Mögliche Verwendungsszenarien**
Die textbasierte bedingte Formatierung in Tabellenkalkulationen ist nützlich, um Zellen hervorzuheben, die bestimmte textuelle Kriterien erfüllen. Dies kann die Datenanalyse verbessern und es erleichtern, wichtige Informationen in einem großen Datensatz zu finden. Hier sind einige Gründe für die Verwendung von Text-Bedingter Formatierung:

1. Spezifischen Text hervorheben: Sie können Formatierungen basierend auf bestimmten Wörtern, Phrasen oder Zeichen anwenden. Zum Beispiel möchten Sie alle Zellen hervorheben, die das Wort "Urgent" oder "Completed" enthalten, um Aufgaben in einem Projekt leicht zu unterscheiden.
1. Muster oder Trends erkennen: Wenn Sie mit Kategorien oder Status arbeiten (wie "Hoch", "Mittel", "Niedrig"), kann die textbasierte bedingte Formatierung diese visuell unterscheiden, was die Fortschrittsverfolgung oder Priorisierung erleichtert.
1. Fehler- oder Dateneingabenwarnungen: Textformatierungen können inkonsistente oder fehlerhafte Eingaben kennzeichnen, wie falsch geschriebene Wörter, unvollständiger Text oder falsche Werte. Dies ist besonders in Datensätzen mit viel Texteingaben nützlich.
1. Verbesserte Lesbarkeit: Farbcodierung von Text oder Änderung seines Stils (fett, kursiv usw.) hilft, wichtige Informationen hervorzuheben und verbessert die Gesamtlesbarkeit Ihres Blattes.
1. Dynamisches Feedback: Sie können Regeln einrichten, die die Formatierung automatisch anpassen, wenn Text bestimmte Bedingungen erfüllt. Das bedeutet, dass Sie die Formatierung nicht manuell aktualisieren müssen, wenn sich die Daten ändern.

Kurz gesagt, hilft Ihnen die bedingte Textformatierung schnell relevante Informationen, Fehler und Trends zu erkennen und ist ein leistungsstarkes Werkzeug für das Management und die Interpretation von Textdaten.

## **Wie man Text-Bedingte Formatierung mit Excel hinzufügt**
Um die textbasierte bedingte Formatierung in Excel hinzuzufügen, folgen Sie diesen Schritten:

1. Zellenbereich auswählen: Markieren Sie die Zellen, auf die Sie die bedingte Formatierung anwenden möchten.
1. Öffnen Sie das Menü für bedingte Formatierung: Gehen Sie zum Start-Tab im Excel-Ribbons. Klicken Sie auf „Bedingte Formatierung“ in der Gruppe „Stile“.
1. Wählen Sie „Neue Regel“: Wählen Sie im Dropdown-Menü „Neue Regel“.
1. Wählen Sie „Nur Zellen formatieren, die enthalten“: Im Dialogfeld für Neue Formatierungsregel wählen Sie „Nur Zellen formatieren, die enthalten“ unter dem Abschnitt „Regeltyp auswählen“.
1. Legen Sie die Regelkriterien fest: Im Abschnitt "Formatieren Sie Zellen mit" wählen Sie aus dem Dropdown "Bestimmter Text". Wählen Sie entweder "enthalten", "beginnen mit" oder "enden mit", je nach Bedingung, die Sie anwenden möchten. Geben Sie den Text ein, den Sie formatieren möchten (z.B. ein bestimmtes Wort wie "Dringend" oder "Abgeschlossen").
1. Format auswählen: Klicken Sie auf die Schaltfläche Format. Im Dialogfeld Zellen formatieren können Sie die Schriftfarbe, Füllfarbe oder andere Formatierungsoptionen nach Wunsch auswählen.
1. Regel anwenden: Sobald Sie das gewünschte Format eingestellt haben, klicken Sie auf OK, um die Regel anzuwenden. Klicken Sie erneut auf OK im Dialogfeld Neue Formatierungsregel, um es zu schließen.
1. Ergebnisse anzeigen: Die Zellen, die den angegebenen Text enthalten, werden jetzt entsprechend formatiert, was das Erkennen relevanter Informationen erleichtert.


## **So fügen Sie bedingte Textformatierung mit Aspose.Cells for .NET hinzu**

Aspose.Cells unterstützt vollständig die bedingte Formatierung, die von Microsoft Excel 2007 und neueren Versionen im XLSX-Format auf Zellen während der Laufzeit bereitgestellt wird. Dieses Beispiel zeigt eine Übung für fortgeschrittene bedingte Formatierungstypen, einschließlich BeginsWith, ContainsBlank, ContainsText und mehr.

### **Zelle formatieren, wenn der Wert mit bestimmtem Text beginnt**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-BeginsWith.cs" >}}

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text.cs" >}}
### **Zelle formatieren, wenn der Wert Leer enthält**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-ContainsBlank.cs" >}}

### **Zelle formatieren, wenn der Wert Fehler enthält**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-ContainsErrors.cs" >}}

### **Zelle formatieren, wenn der Wert bestimmten Text enthält**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-ContainsText.cs" >}}

### **Zelle formatieren, wenn der Wert doppelte Werte enthält**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-DuplicateValues.cs" >}}

### **Zelle formatieren, wenn der Wert mit bestimmtem Text endet**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-EndsWith.cs" >}}

### **Zelle formatieren, wenn der Wert Leer nicht enthält**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-NotContainsBlank.cs" >}}

### **Zelle formatieren, wenn der Wert Fehler nicht enthält**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-NotContainsErrors.cs" >}}

### **Zelle formatieren, wenn der Wert bestimmten Text nicht enthält**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-NotContainsText.cs" >}}

### **Zelle formatieren, wenn der Wert eindeutige Werte enthält**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-UniqueValues.cs" >}}

{{< app/cells/assistant language="csharp" >}}
