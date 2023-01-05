---
title: Arbeitsblattdaten sortieren
type: docs
weight: 80
url: /de/net/sorting-worksheet-data/
---
{{% alert color="primary" %}} 

Das Sortieren ist eine wichtige Routineaufgabe, die wir meistens bei der Verarbeitung von Daten anwenden. In diesem Thema werden wir anhand eines einfachen Beispiels diskutieren, wie wir Daten in einem Arbeitsblatt sortieren können.

{{% /alert %}} 
## **Arbeitsblattdaten sortieren**
Um Daten in einem Arbeitsblatt mit API von Aspose.Cells.GridDesktop zu sortieren, führen Sie bitte die folgenden Schritte aus:

-  Erstellen Sie zunächst ein globales Objekt von**CellRange** sodass überall im Bereich Ihrer Klasse darauf zugegriffen werden kann
-  Erstellen Sie einen Ereignishandler für**SelectedCellRangeChanged** Veranstaltung von**GridDesktop**. **SelectedCellRangeChanged** -Ereignis wird jedes Mal ausgelöst, wenn ein von einem Benutzer ausgewählter Zellbereich geändert wird. Wenn ein Benutzer beispielsweise Zellen auswählt (die zu sortierende Daten enthalten), wird dieses Ereignis jedes Mal ausgelöst, wenn sich sein Auswahlbereich ändert.
-  Der Event-Handler bietet**CellRangeEventArgs** Argument, das außerdem den Aktualisierungsbereich von Zellen (vom Benutzer ausgewählt) in Form von a bereitstellt**CellRange** Objekt. In diesem Event-Handler werden wir dies also zuweisen**CellRange** Objekt (enthält den aktualisierten Zellbereich) zum globalen**CellRange**-Objekt, sodass es auch in anderen Teilen des Codes verwendet werden kann. Um sicherzustellen, dass wir den Zellbereich nicht verlieren, schreiben wir Event-Handler-Code in eine Bedingung
- Jetzt können wir Code schreiben, um Worksheet-Daten zu sortieren. Greifen Sie zunächst auf ein gewünschtes Arbeitsblatt zu
-  Ein ... kreieren**Sortierbereich** Objekt, das den Bereich der Zellen behält, deren Daten sortiert werden sollen. In**Sortierbereich** Konstruktor können wir das Arbeitsblatt, die Indizes der Startzeile und -spalte, die Anzahl der zu sortierenden Zeilen und Spalten, die Sortierrichtung (wie von oben nach unten oder von links nach rechts) usw. angeben.
-  Jetzt können wir anrufen**Sortieren** Methode von**Sortierbereich** Objekt, um die Sortierung der Daten durchzuführen. In**Sortieren** Methode können wir den Index der zu sortierenden Spalte oder Zeile und die Sortierreihenfolge angeben (das kann sein**Aufsteigend** oder**Absteigend** nach Ihren Wünschen)
-  Endlich können wir anrufen**Ungültig machen** Methode von**GridDesktop** Zellen neu zeichnen.

Im folgenden Beispiel haben wir gezeigt, wie Daten in einer Spalte sortiert werden.

 Erstellen Sie ein globales Objekt von CellRange und**SelectedCellRangeChanged**Ereignis von GridDesktop. Schreiben Sie nun den Code wie unten angegeben:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-CheckingCellRange.cs" >}}


 Jetzt schreiben wir eine Methode für**Aufsteigende Sortierung** . Sie können eine Schaltfläche für erstellen**Aufsteigende Sortierung** und schreiben Sie den folgenden Code hinein**Klicken** Vorfall.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-AscendingSort.cs" >}}


 Schließlich schreiben wir etwas Code, um das zu erreichen**Absteigende Sortierung** Funktionalität. Ein ... kreieren**Absteigende Sortierung** Schaltfläche und schreiben Sie den folgenden Code hinein**Klicken** Vorfall.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-DescendingSort.cs" >}}
