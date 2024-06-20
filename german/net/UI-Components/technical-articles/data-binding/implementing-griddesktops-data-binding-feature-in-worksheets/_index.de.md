---
title: Implementieren des Data Binding Features von GridDesktop in Arbeitsblättern
type: docs
weight: 10
url: /de/net/aspose-cells-griddesktop/implementing-data-binding-feature-in-worksheets/
keywords: GridDesktop, Datenbindung, Daten, binden
description: Dieser Artikel zeigt, wie die Datenbindung in GridDesktop implementiert wird.
---

{{% alert color="primary" %}} 

Datenbindung ist ein aufregendes Feature, das vom Microsoft .NET Framework angeboten wird. Wir wissen, dass die von Microsoft angebotene DataGrid-Steuerung die Datenbindung unterstützt, was bedeutet, dass ein DataGrid an jede Datenquelle (unter Verwendung von DataSet-, DataTable- und DataView-Objekten) gebunden werden kann. Dieses Feature hat das Leben der Entwickler sehr erleichtert. Basierend auf demselben Konzept unterstützt auch Aspose.Cells.GridDesktop die Datenbindung, die es Entwicklern ermöglicht, Arbeitsblätter an jede Datenquelle zu binden. Dieser Artikel erforscht das Feature.

{{% /alert %}} 
## **Erstellen einer Beispieldatenbank**
1. Erstellen einer Beispieldatenbank, die mit dem Beispiel verwendet werden soll. Wir haben Microsoft Access verwendet, um eine Beispieldatenbank mit einer Produkttabelle (Schema unten) zu erstellen. 

![todo:image_alt_text](implementing-griddesktops-data-binding-feature-in-worksheets_1.png)

1. Es wurden drei Dummy-Datensätze zur Produkttabelle hinzugefügt.
   **Datensätze in der Produkttabelle** 

![todo:image_alt_text](implementing-griddesktops-data-binding-feature-in-worksheets_2.png)
## **Erstellen einer Beispielanwendung**
Erstellen Sie jetzt eine einfache Desktop-Anwendung in Visual Studio und führen Sie die folgenden Schritte aus.

1. Ziehen Sie die Steuerung "GridControl" aus der Toolbox und platzieren Sie sie auf dem Formular.
1. Fügen Sie vier Schaltflächen aus der Toolbox am unteren Rand des Formulars hinzu und legen Sie ihren Text auf **Bind Worksheet**, **Zeile hinzufügen**, **Zeile löschen** und **Aktualisierung in Datenbank** fest.
## **Hinzufügen von Namensraum und Deklaration globaler Variablen**
Da dieses Beispiel eine Microsoft Access-Datenbank verwendet, fügen Sie das System.Data.OleDb-Namespace ganz oben im Code hinzu.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingNamespaceToTheTop.cs" >}}


Sie können jetzt die unter diesem Namespace verpackten Klassen verwenden.

1. Globale Variablen deklarieren.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeclareGlobalVariable.cs" >}}
## **Füllen des DataSet mit Daten aus der Datenbank.**
Stellen Sie nun eine Verbindung zur Beispieldatenbank her, um Daten abzurufen und in ein DataSet-Objekt zu laden.

1. Verwenden Sie das OleDbDataAdapter-Objekt, um sich mit unserer Beispieldatenbank zu verbinden und ein DataSet mit Daten aus der Products-Tabelle in der Datenbank zu füllen, wie im folgenden Code gezeigt.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-FillDataSet.cs" >}}
## **Binden des Arbeitsblatts mit dem DataSet.**
Binden Sie das Arbeitsblatt mit der Products-Tabelle des DataSet:

1. Greifen Sie auf ein gewünschtes Arbeitsblatt zu.
1. Binden Sie das Arbeitsblatt mit der Products-Tabelle des DataSet.

Fügen Sie den folgenden Code zum Klickereignis der **Arbeitsblatt binden**-Schaltfläche hinzu.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-BindWorksheet.cs" >}}
## **Festlegen von Spaltenüberschriften des Arbeitsblatts.**
Das gebundene Arbeitsblatt lädt jetzt erfolgreich Daten, aber die Spaltenüberschriften sind standardmäßig mit A, B und C beschriftet. Es wäre besser, die Spaltenüberschriften auf die Spaltennamen in der Datenbanktabelle zu setzen.

Um die Spaltenüberschriften des Arbeitsblatts zu setzen:

1. Holen Sie die Beschriftungen für jede Spalte der DataTable (Products) im DataSet.
1. Weisen Sie die Beschriftungen den Überschriften der Arbeitsblattspalten zu.

Fügen Sie den im Klickereignis der **Arbeitsblatt binden**-Schaltfläche geschriebenen Codeausschnitt hinzu. Dadurch werden die alten Spaltenüberschriften (A, B und C) durch ProductID, ProductName und ProductPrice ersetzt.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SettingColumnHeader.cs" >}}
## **Anpassen der Breite und des Stils von Spalten.**
Um das Aussehen des Arbeitsblatts weiter zu verbessern, ist es möglich, die Breite und den Stil von Spalten festzulegen. Manchmal besteht z. B. die Spaltenüberschrift oder der Wert innerhalb der Spalte aus einer großen Anzahl von Zeichen, die nicht in die Zelle passen. Um solche Probleme zu lösen, unterstützt Aspose.Cells.GridDesktop das Ändern der Spaltenbreiten.

Fügen Sie den folgenden Code zur **Arbeitsblatt binden**-Schaltfläche hinzu. Die Spaltenbreiten werden entsprechend den neuen Einstellungen angepasst.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-CustomizingStyle.cs" >}}


Aspose.Cells.GridDesktop unterstützt auch das Anwenden von benutzerdefinierten Stilen auf Spalten. Der folgende Code, der zur **Arbeitsblatt binden**-Schaltfläche hinzugefügt wird, passt die Spaltenstile an, um sie präsentabler zu gestalten.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-ApplyCustomStyle.cs" >}}


Führen Sie nun die Anwendung aus und klicken Sie auf die Schaltfläche **Arbeitsblatt binden**.
## **Zeilen hinzufügen**
Um neue Zeilen zu einem Arbeitsblatt hinzuzufügen, verwenden Sie die AddRow-Methode der Worksheet-Klasse. Dadurch wird eine leere Zeile unten angehängt und eine neue DataRow wird der Datenquelle hinzugefügt (hier wird eine neue DataRow zur DataTable des DataSet hinzugefügt). Entwickler können beliebig viele Zeilen hinzufügen, indem sie die AddRow-Methode immer wieder aufrufen. Nachdem eine Zeile hinzugefügt wurde, können Benutzer Werte eingeben.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingRows.cs" >}}
## **Zeilen löschen**
Aspose.Cells.GridDesktop unterstützt auch das Löschen von Zeilen durch Aufrufen der RemoveRow-Methode der Worksheet-Klasse. Zum Löschen einer Zeile ist der Index der zu löschenden Zeile erforderlich.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeletingRows.cs" >}}


Fügen Sie den obigen Code zur Schaltfläche **Zeile löschen** hinzu und führen Sie die Anwendung aus. Einige Datensätze werden angezeigt, bevor die Zeile entfernt wird. Durch Auswahl einer Zeile und Klicken auf die Schaltfläche **Zeile löschen** wird die ausgewählte Zeile entfernt.
## **Änderungen in der Datenbank speichern**
Schließlich können Änderungen, die Benutzer am Arbeitsblatt vorgenommen haben, zurück in die Datenbank gespeichert werden, indem die Update-Methode des OleDbDataAdapter-Objekts verwendet wird. Die Update-Methode übernimmt die Datenquelle (DataSet, DataTable usw.) des Arbeitsblatts, um die Datenbank zu aktualisieren.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SavingChangesToDatabase.cs" >}}




1. Fügen Sie den obigen Code zur Schaltfläche **Database aktualisieren** hinzu.
1. Führen Sie die Anwendung aus.
1. Führen Sie einige Operationen an den Arbeitsblattdaten aus, z. B. das Hinzufügen neuer Zeilen und das Bearbeiten oder Entfernen vorhandener Daten.
1. Klicken Sie dann auf **Database aktualisieren**, um die Änderungen in der Datenbank zu speichern.
1. Überprüfen Sie die Datenbank, um zu sehen, dass die Tabelleneinträge entsprechend aktualisiert wurden.
