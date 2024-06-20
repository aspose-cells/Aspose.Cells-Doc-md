---
title: Sortieren von Arbeitsblattdaten
type: docs
weight: 80
url: /de/net/aspose-cells-griddesktop/sorting-worksheet-data/
keywords: GridDesktop,sortieren,sortieren von Daten,Datensortierung
description: Dieser Artikel zeigt, wie Daten in einem Arbeitsblatt in GridDesktop sortiert werden.
---

{{% alert color="primary" %}} 

Sortieren ist eine wichtige Routineaufgabe, die wir hauptsächlich beim Verarbeiten von Daten verwenden. In diesem Thema werden wir anhand eines einfachen Beispiels diskutieren, wie Daten in einem Arbeitsblatt sortiert werden können.

{{% /alert %}} 
## **Daten im Arbeitsblatt sortieren**
Um Daten in einem Arbeitsblatt mithilfe der API von Aspose.Cells.GridDesktop zu sortieren, befolgen Sie bitte die folgenden Schritte:

- Erstellen Sie zunächst ein globales Objekt von **CellRange**, damit es überall im Umfang Ihrer Klasse zugänglich ist
- Erstellen Sie einen Ereignisbehandler für das Ereignis **SelectedCellRangeChanged** von **GridDesktop**. Das Ereignis **SelectedCellRangeChanged** wird jedes Mal ausgelöst, wenn ein vom Benutzer ausgewählter Zellenbereich geändert wird. Beispielsweise, wenn ein Benutzer Zellen (die Daten zur Sortierung enthalten) auswählt, wird jedes Mal, wenn sich sein Auswahlbereich ändert, dieses Ereignis ausgelöst.
- Der Ereignisbehandler liefert das Argument **CellRangeEventArgs**, das weiterhin den aktualisierten Bereich von Zellen (vom Benutzer ausgewählt) in Form eines **CellRange**-Objekts bereitstellt. In diesem Ereignisbehandler weisen wir dieses **CellRange**-Objekt (das den aktualisierten Bereich von Zellen enthält) dem globalen **CellRange**-Objekt zu, sodass es auch in anderen Teilen des Codes verwendet werden kann. Um sicherzustellen, dass wir den Zellenbereich nicht verlieren, schreiben wir den Ereignisbehandlercode innerhalb einer Bedingung
- Jetzt können wir einige Codezeilen schreiben, um Daten im Arbeitsblatt zu sortieren. Greifen Sie zunächst auf ein gewünschtes Arbeitsblatt zu
- Erstellen Sie ein **SortRange**-Objekt, das den Bereich von Zellen enthält, deren Daten sortiert werden sollen. Im Konstruktor von **SortRange** können wir das Arbeitsblatt, die Indizes der Startzeile und -spalte, die Anzahl der Zeilen und Spalten zur Sortierung, die Orientierung der Sortierung (wie von oben nach unten oder von links nach rechts) usw. angeben.
- Nun können wir die Methode **Sort** des **SortRange**-Objekts aufrufen, um die Daten zu sortieren. In der **Sort**-Methode können wir den Index der Spalte oder Zeile angeben, die sortiert werden soll, und die Sortierreihenfolge (die **Aufsteigend** oder **Absteigend** sein kann, je nach Ihren Anforderungen)
- Schließlich können wir die Methode **Invalidate** des **GridDesktop** aufrufen, um Zellen neu zu zeichnen.

Im unten stehenden Beispiel haben wir gezeigt, wie Daten in einer Spalte sortiert werden können.

Erstellen Sie ein globales Objekt von CellRange und das Ereignis **SelectedCellRangeChanged** von GridDesktop. Schreiben Sie nun den Code wie unten angegeben:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-CheckingCellRange.cs" >}}


Nun schreiben wir die Methode für **Aufsteigende Sortierung**. Sie können eine Schaltfläche für **Aufsteigende Sortierung** erstellen und den unten stehenden Code in ihr **Klick**-Ereignis schreiben.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-AscendingSort.cs" >}}


Schließlich schreiben wir einige Codezeilen, um die Funktionalität der **Absteigenden Sortierung** zu erreichen. Erstellen Sie eine Schaltfläche für **Absteigende Sortierung** und schreiben Sie den unten stehenden Code in ihr **Klick**-Ereignis.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-DescendingSort.cs" >}}
