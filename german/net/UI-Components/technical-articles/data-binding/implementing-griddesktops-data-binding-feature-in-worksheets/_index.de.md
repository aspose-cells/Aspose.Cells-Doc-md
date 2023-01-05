---
title: Implementieren der GridDesktop-Datenbindungsfunktion in Arbeitsblättern
type: docs
weight: 10
url: /de/net/implementing-griddesktops-data-binding-feature-in-worksheets/
---
{{% alert color="primary" %}} 

Datenbindung ist eine spannende Funktion, die vom Microsoft .NET Framework angeboten wird. Wir wissen, dass das von Microsoft angebotene DataGrid-Steuerelement die Datenbindung unterstützt, was bedeutet, dass ein DataGrid an eine beliebige Datenquelle gebunden werden kann (unter Verwendung von DataSet-, DataTable- und DataView-Objekten). Diese Funktion hat das Leben der Entwickler erheblich vereinfacht. Basierend auf dem gleichen Konzept unterstützt Aspose.Cells.GridDesktop auch die Datenbindung, die es Entwicklern ermöglicht, Arbeitsblätter an jede Datenquelle zu binden. Dieser Artikel untersucht die Funktion.

{{% /alert %}} 
## **Erstellen einer Beispieldatenbank**
1.  Erstellen Sie eine Beispieldatenbank zur Verwendung mit dem Beispiel. Wir haben Microsoft Access verwendet, um eine Beispieldatenbank mit einer Produkttabelle (Schema unten) zu erstellen.

![todo: Bild_alt_Text](implementing-griddesktops-data-binding-feature-in-worksheets_1.png)

1. Der Tabelle Products werden drei Dummy-Datensätze hinzugefügt.
   **Datensätze in der Produkttabelle** 

![todo: Bild_alt_Text](implementing-griddesktops-data-binding-feature-in-worksheets_2.png)
## **Erstellen Sie eine Beispielanwendung**
Erstellen Sie nun eine einfache Desktopanwendung in Visual Studio und gehen Sie wie folgt vor.

1. Ziehen Sie das "GridControl"-Steuerelement aus der Toolbox und legen Sie es auf dem Formular ab.
1. Legen Sie vier Schaltflächen aus der Toolbox am unteren Rand des Formulars ab und legen Sie ihre Texteigenschaft auf fest**Arbeitsblatt binden**, **Zeile hinzufügen**, **Zeile löschen** und**Update auf Datenbank** beziehungsweise.
## **Namespace hinzufügen und globale Variablen deklarieren**
Da in diesem Beispiel eine Access-Datenbank Microsoft verwendet wird, fügen Sie den System.Data.OleDb-Namespace am Anfang des Codes hinzu.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingNamespaceToTheTop.cs" >}}


Sie können jetzt die unter diesem Namensraum gepackten Klassen verwenden.

1. Deklarieren Sie globale Variablen.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeclareGlobalVariable.cs" >}}
## **DataSet mit Daten aus Datenbank füllen**
Stellen Sie nun eine Verbindung mit der Beispieldatenbank her, um Daten abzurufen und in ein DataSet-Objekt zu füllen.

1. Verwenden Sie das OleDbDataAdapter-Objekt, um eine Verbindung mit unserer Beispieldatenbank herzustellen und ein DataSet mit Daten zu füllen, die aus der Products-Tabelle in der Datenbank abgerufen wurden, wie im folgenden Code gezeigt.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-FillDataSet.cs" >}}
## **Verbindliches Arbeitsblatt mit DataSet**
Binden Sie das Arbeitsblatt mit der Products-Tabelle des DataSets:

1. Greifen Sie auf ein gewünschtes Arbeitsblatt zu.
1. Binden Sie das Arbeitsblatt mit der Tabelle Products des DataSets.

 Fügen Sie den folgenden Code hinzu**Arbeitsblatt binden** Klickereignis der Schaltfläche.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-BindWorksheet.cs" >}}
## **Spaltenüberschriften des Arbeitsblatts festlegen**
Das gebundene Arbeitsblatt lädt nun erfolgreich Daten, aber die Spaltenüberschriften sind standardmäßig mit A, B und C gekennzeichnet. Besser wäre es, die Spaltenüberschriften auf die Spaltennamen in der Datenbanktabelle zu setzen.

So legen Sie die Spaltenüberschriften des Arbeitsblatts fest:

1. Rufen Sie die Beschriftungen für jede Spalte der DataTable (Produkte) im DataSet ab.
1. Weisen Sie die Überschriften den Überschriften der Arbeitsblattspalten zu.

 Fügen Sie den in der geschriebenen Code an**Arbeitsblatt binden** Klickereignis der Schaltfläche mit dem folgenden Code-Snippet. Dadurch werden die alten Spaltenüberschriften (A, B und C) durch ProductID, ProductName und ProductPrice ersetzt.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SettingColumnHeader.cs" >}}
## **Anpassen der Breite und des Stils von Spalten**
Um das Aussehen des Arbeitsblatts weiter zu verbessern, ist es möglich, die Breite und den Stil der Spalten festzulegen. Beispielsweise besteht manchmal die Spaltenüberschrift oder der Wert in der Spalte aus einer langen Anzahl von Zeichen, die nicht in die Zelle passen. Um solche Probleme zu lösen, unterstützt Aspose.Cells.GridDesktop das Ändern der Spaltenbreite.

 Fügen Sie den folgenden Code an die an**Arbeitsblatt binden** Knopf. Die Spaltenbreiten werden entsprechend den neuen Einstellungen angepasst.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-CustomizingStyle.cs" >}}


 Aspose.Cells. GridDesktop unterstützt auch das Anwenden benutzerdefinierter Stile auf Spalten. Der folgende Code, angehängt an die**Arbeitsblatt binden** Schaltfläche, passt die Spaltenstile an, um sie präsentabler zu machen.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-ApplyCustomStyle.cs" >}}


 Führen Sie nun die Anwendung aus und klicken Sie auf die**Arbeitsblatt binden** Knopf.
## **Zeilen hinzufügen**
Um einem Arbeitsblatt neue Zeilen hinzuzufügen, verwenden Sie die AddRow-Methode der Worksheet-Klasse. Dadurch wird unten eine leere Zeile angehängt, und der Datenquelle wird eine neue DataRow hinzugefügt (hier wird der DataTable des DataSet eine neue DataRow hinzugefügt). Entwickler können beliebig viele Zeilen hinzufügen, indem sie die AddRow-Methode immer wieder aufrufen. Wenn eine Zeile hinzugefügt wurde, können Benutzer Werte eingeben.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingRows.cs" >}}
## **Zeilen löschen**
Aspose.Cells. GridDesktop unterstützt auch das Löschen von Zeilen durch Aufrufen der RemoveRow-Methode der Worksheet-Klasse. Das Entfernen einer Zeile mit Aspose.Cells.GridDesktop erfordert, dass der Index der Zeile gelöscht wird.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeletingRows.cs" >}}


 Hinzufügen des obigen Codes zu der**Zeile löschen** Schaltfläche und führen Sie die Anwendung aus. Einige Datensätze werden angezeigt, bevor die Zeile entfernt wird. Wählen Sie eine Zeile aus und klicken Sie auf**Zeile löschen** Schaltfläche entfernt die ausgewählte Zeile.
## **Änderungen in der Datenbank speichern**
Um schließlich alle Änderungen, die von Benutzern am Arbeitsblatt vorgenommen wurden, wieder in der Datenbank zu speichern, verwenden Sie die Update-Methode des OleDbDataAdapter-Objekts. Die Update-Methode verwendet die Datenquelle (DataSet, DataTable usw.) des Arbeitsblatts, um die Datenbank zu aktualisieren.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SavingChangesToDatabase.cs" >}}




1.  Fügen Sie den obigen Code hinzu**Update auf Datenbank** Knopf.
1. Führen Sie die Anwendung aus.
1. Führen Sie einige Operationen an den Arbeitsblattdaten durch, fügen Sie möglicherweise neue Zeilen hinzu und bearbeiten oder entfernen Sie vorhandene Daten.
1.  Dann klick**Update auf Datenbank** um die Änderungen in der Datenbank zu speichern.
1. Überprüfen Sie die Datenbank, um festzustellen, ob die Tabellendatensätze entsprechend aktualisiert wurden.
