---
title: FAQ
type: docs
weight: 100
url: /de/net/faq/
---

## **So beheben Sie die System.StackOverflowException bei Workbook.CalculateFormula?**
Manchmal treten Benutzer auf die System.StackOverflowException bei der Methode Workbook.CalculateFormula. Diese Ausnahme tritt in der Regel auf, weil die Standard-Stackgröße des IIS zu klein ist (nur 265k). Sie können diesen Fehler beheben, indem Sie einen anderen Thread mit erhöhter Stapelgröße erstellen und dann Ihren Workbook.CalculateFormula-Code darin verschieben.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Controllers-GridWebFAQController-FixStackOverflowException.cs" >}}
## **Dicke von Linienproblem beim Rendern von Excel zu PDF**
Manchmal, wenn eine Excel-Datei in PDF konvertiert wird, ist die Dicke der Linien im Ausgabe-PDF unterschiedlich. Dieses Problem wird nicht von Aspose.Cells verursacht. Es wird durch **Adobe Reader** verursacht, wenn seine Einstellungen **"Glätten von Linien Kunst"** und **"Verstärken von dünnen Linien"** aktiviert sind. Das Deaktivieren dieser Optionen zeigt das PDF gut an.

Wenn **"Glätten von Linien Kunst"** und **"Verstärken von dünnen Linien"** aktiviert sind, ist die Dicke der Linien unterschiedlich. Sehen Sie sich die folgenden Schritte an, wie dies gemacht wird:

- Gehe zu **Bearbeiten**
- Wählen Sie **Einstellungen**
- In der Kategorie **Seitenanzeige** aktivieren Sie **"Glätten von Linien Kunst"** und **"Verstärken von dünnen Linien"**

Wenn **"Glätten von Linien Kunst"** und **"Verstärken von dünnen Linien"** deaktiviert sind, ist die Dicke der Linien gleich. Befolgen Sie dazu einfach die folgenden Schritte:

- Gehe zu **Bearbeiten**
- Wählen Sie **Einstellungen**
- In der Kategorie **Seitenanzeige** deaktivieren Sie **"Glätten von Linien Kunst"** und **"Verstärken von dünnen Linien"**
## **So beheben Sie die System.OutOfMemoryException beim Laden großer Tabellenkalkulationen?**
Es besteht eine hohe Wahrscheinlichkeit, dass der Workbook-Konstruktor eine System.OutOfMemoryException beim Laden großer Tabellenkalkulationen wirft. Diese Ausnahme deutet darauf hin, dass der verfügbare Speicher nicht ausreicht, um die Tabelle komplett in den Speicher zu laden, daher muss die Tabelle geladen werden, während die [Speichereinstellungen](/cells/de/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/) aktiviert sind.

Aspose.Cells APIs bieten Speicherpräferenzen zur Optimierung des Speicherverbrauchs beim Laden und Verarbeiten von Tabellenkalkulationen. Diese Optionen sind auch hilfreich beim effizienten Laden großer Tabellenkalkulationen mit riesigen Datensätzen im Workbook-Objekt, wie unten demonstriert.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-KnowledgeBase-FAQs-FixOutOfMemoryException-1.cs" >}}

## **Bestimmen Sie, welche Stapelgröße für eine bestimmte Arbeitsmappe benötigt wird**
Obwohl wir den Aspose.Cells Formelberechnungs-Engine verbessert haben und in den meisten Fällen sollten alle Formeln erfolgreich für eine bestimmte Vorlagendatei berechnet werden können, ohne eine kleinere Stapelgröße anzugeben. Aber manchmal ist die System.StackOverflowException bei der Methode Workbook.CalculateFormula unvermeidlich. Wir bieten neue APIs für die Benutzer, um die Formelberechnungen zu verfolgen. Wir haben eine Klasse namens "AbstractCalculationMonitor" hinzugefügt und eine Eigenschaft bereitgestellt, d.h., *CalculationOptions.CalculationMonitor* um mit dem Problem umzugehen/zu verfolgen.

Benutzer können die Stapelgröße selbst mithilfe der APIs nachverfolgen. Bitte beachten Sie, dass das Überprüfen des Stapels für jede Zelle die Leistung erheblich beeinträchtigen wird. Sehen Sie sich das Beispielcode-Segment zur Referenz an:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "CalculationMonitor-CustomStackTrace.cs" >}}

{{% alert color="primary" %}} 

Es gibt keinen besseren Weg, um die zur Laufzeit verwendete Stapelgröße zu erhalten. Der obige Code, den wir bereitgestellt haben, dient nur als Beispiel. Die Leistung wird sich mit Sicherheit erheblich verschlechtern. Daher denken wir, dass der Code von den Benutzern (die ihn wirklich verwenden möchten) entsprechend ihren verschiedenen Szenarien und Anforderungen optimiert werden kann. Zum Beispiel durch das Überprüfen des Stapels, wenn die Anzahl der rekursiven Zellen eine bestimmte Anzahl erreicht, das Sammeln des durchschnittlichen Anstiegs des Stapels für eine rekursive Zelle und die Bestimmung der Häufigkeit, den Stapel zu überprüfen, usw.

{{% /alert %}}

{{< app/cells/assistant language="csharp" >}}
