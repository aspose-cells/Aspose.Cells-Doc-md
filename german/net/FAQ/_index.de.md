---
title: FAQ
type: docs
weight: 100
url: /de/net/faq/
---
## **Wie behebt man die System.StackOverFlowException auf Workbook.CalculateFormula?**
Manchmal sehen sich Benutzer System.StackOverFlowException in der Workbook.CalculateFormula-Methode gegenüber. Diese Ausnahme tritt normalerweise auf, weil die Standardstapelgröße des IIS zu klein ist (nur 265 KB). Sie können diesen Fehler beheben, indem Sie einen weiteren Thread mit erhöhter Stapelgröße erstellen und dann Ihren Workbook.CalculateFormula-bezogenen Code darin verschieben.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Controllers-GridWebFAQController-FixStackOverflowException.cs" >}}
## **Problem mit der Linienstärke beim Rendern von Excel in PDF**
Manchmal, wenn eine Excel-Datei in PDF konvertiert wird, ist die Dicke der Linien in der Ausgabe-PDF unterschiedlich. Dieses Problem wird nicht durch Aspose.Cells verursacht. Es wird verursacht durch**Adobe Reader** wenn seine Einstellungen**"Glatte Strichzeichnungen"** und**"Dünne Linien verstärken"** werden geprüft. Wenn Sie diese Optionen deaktivieren, wird PDF fein angezeigt.

 Wenn prüfen**"Glatte Strichzeichnungen"** und**"Dünne Linien verstärken"**, die Dicke der Linien ist unterschiedlich. Sehen Sie sich die folgenden Schritte an, wie es gemacht wird:

-  Gehe zu**Bearbeiten**
-  Auswählen**Einstellungen**
-  In dem**Seitenanzeige** Kategorie Überprüfen Sie die**"Glatte Strichzeichnungen"** und**"Dünne Linien verstärken"**

 Wenn deaktiviert**"Glatte Strichzeichnungen"** und**"Dünne Linien verstärken"**, die Dicke der Linien ist gleich. Um dies zu erreichen, befolgen Sie einfach die folgenden Schritte:

-  Gehe zu**Bearbeiten**
-  Auswählen**Einstellungen**
-  In dem**Seitenanzeige** Kategorie Deaktivieren Sie die**"Glatte Strichzeichnungen"** und**"Dünne Linien verstärken"**
## **Wie behebt man die System.OutOfMemoryException beim Laden großer Tabellenkalkulationen?**
Es besteht die Möglichkeit, dass der Workbook-Konstruktor beim Laden großer Tabellenkalkulationen System.OutOfMemoryException auslöst. Diese Ausnahme deutet darauf hin, dass der verfügbare Speicher nicht ausreicht, um die Tabelle vollständig in den Speicher zu laden, daher muss die Tabelle geladen werden, während die aktiviert wird[Speichereinstellungen](/cells/de/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

Aspose.Cells APIs bieten Speichereinstellungen, um den Speicherverbrauch beim Laden und Verarbeiten von Tabellenkalkulationen zu optimieren. Diese Optionen sind auch hilfreich beim effizienten Laden der großen Tabellenkalkulationen mit riesigen Datensätzen im Workbook-Objekt, wie unten gezeigt.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-KnowledgeBase-FAQs-FixOutOfMemoryException-1.cs" >}}

## **Bestimmen Sie, welche Stapelgröße für eine bestimmte Arbeitsmappe benötigt wird**
Obwohl wir die Formelberechnungs-Engine Aspose.Cells verbessert haben, sollten Sie in den meisten Fällen in der Lage sein, alle Formeln erfolgreich für eine bestimmte Vorlagendatei berechnet zu bekommen, ohne eine kleinere Stapelgröße anzugeben. Trotzdem kann StackOverFlowException für die Workbook.CalculateFormula-Methode manchmal unvermeidlich sein. Wir stellen den Benutzern neue APIs zur Verfügung, um die Formelberechnungen zu verfolgen. Wir haben eine Klasse namens "AbstractCalculationMonitor" hinzugefügt und eine Eigenschaft bereitgestellt, dh*Berechnungsoptionen.Berechnungsmonitor*um das Problem zu lösen/zu verfolgen.

Benutzer können die Stapelgröße mithilfe der APIs selbst verfolgen. Bitte beachten Sie, dass die Überprüfung des Stapels für jede Zelle die Leistung sicherlich stärker beeinträchtigt. Sehen Sie sich das Beispielcodesegment als Referenz an:

`     `öffentliche Klasse MyCalculationMonitor : AbstractCalculationMonitor
" Stoppen Sie die Formelberechnung wegen StackOverflowException-Risikos");  ` `}  ` `}  ` `} 



{{% alert color="primary" %}} 

Es gibt keinen besseren Weg, um die zur Laufzeit verwendete Stapelgröße zu erhalten. Der obige Code, den wir bereitgestellt haben, ist nur ein Beispiel. Die Leistung wird mit Sicherheit erheblich beeinträchtigt. Wir glauben also, dass der Code von Benutzern (die ihn wirklich verwenden wollen) entsprechend ihren unterschiedlichen Szenarien und Anforderungen optimiert werden kann. Beispielsweise das Überprüfen des Stacks, wenn die Anzahl der rekursiven Zellen eine bestimmte Zahl erreicht, das Erfassen der durchschnittlichen Steigerungsrate des Stacks für eine rekursive Zelle und das Bestimmen der Häufigkeit zum Überprüfen des Stacks usw.

{{% /alert %}}

