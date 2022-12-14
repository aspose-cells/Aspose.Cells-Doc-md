---
title: Arbeiten mit Aspose.Cells.GridDesktop-Ereignissen
type: docs
weight: 30
url: /de/net/working-with-aspose-cells-griddesktop-events/
---
{{% alert color="primary" %}} 

Ereignisse werden verwendet, um Benachrichtigungen zu senden, wenn eine Änderung in einem Steuerelement oder einer Klasse auftritt. Aspose.Cells.GridDesktop verfügt über mehrere Ereignisse, die verwendet werden, um bestimmte Aufgaben auszuführen, wenn bestimmte Änderungen im Steuerelement auftreten. Dieses Thema bietet eine Einführung in alle Ereignisse, die vom Aspose.Cells.GridDesktop-Steuerelement unterstützt werden, und erläutert, wie diese Ereignisse behandelt werden können.

{{% /alert %}} 
## **Einführung**
Das Aspose.Cells.GridDesktop-Steuerelement unterstützt mehrere Ereignisse, die mehr Kontrolle für die Ausführung von Vorgängen bieten, wenn bestimmte Ereignisse ausgelöst werden. Nachfolgend finden Sie eine vollständige Liste der Ereignisse, die vom Aspose.Cells.GridDesktop-Steuerelement unterstützt werden.

{{% alert color="primary" %}} 

Diese Liste enthält nicht die Ereignisse, die von Aspose.Cells.GridDesktop von der Control-Klasse geerbt werden.

{{% /alert %}} 

|**Veranstaltungen**|**Beschreibung**|
|:- |:- |
|VorBerechnen|Tritt vor der Berechnungsformel in der Arbeitsmappe auf.|
|BeforeLoadFile|Tritt auf, bevor die Arbeitsmappe aus der Datei geladen wird.|
|SpaltenüberschriftKlick|Tritt auf, wenn auf die Spaltenüberschrift geklickt wird.|
|ColumnHeaderDoubleClick|Tritt auf, wenn auf die Spaltenüberschrift doppelgeklickt wird.|
|CellDataChanged|Tritt auf, wenn die Daten oder Werte in einer Rasterzelle geändert werden. Dieses Ereignis kann auch ausgelöst werden, wenn der Wert einer Zelle programmgesteuert mithilfe der Value-Eigenschaft oder der SetCellValue-Methode einer GridCell geändert wird.|
|CellButtonClick|Tritt auf, wenn auf die Zellenschaltfläche geklickt wird.|
|CellCheckedChanged|Tritt auf, wenn die Checked-Eigenschaft des Kontrollkästchens der Zelle geändert wird.|
|CellSelectedIndexChanged|Tritt auf, wenn die SelectedIndex-Eigenschaft des Zellenkombinationsfelds geändert wird.|
|CellClick|Tritt auf, wenn auf eine Rasterzelle geklickt wird.|
|CellDoubleClick|Tritt auf, wenn auf eine Rasterzelle doppelgeklickt wird.|
|CellKeyPressed|Tritt auf, wenn eine Taste gedrückt wird, während eine Zelle den Fokus hat. Wenn Sie einen Ereignishandler für das CellKeyPressed-Ereignis erstellen möchten, legen Sie die Handled-Eigenschaft des CellKeyEventArgs-Arguments auf „true“ fest, um zu verhindern, dass das GridDesktop-Steuerelement das Tastenereignis verarbeitet.|
|AfterInsertColumns|Tritt auf, wenn eine Spalte eingefügt wird. Sie können den Spaltenindex abrufen, indem Sie die Index-Eigenschaft des Arguments Aspose.Cells.GridDesktop.WorksheetEventArgs verwenden.|
|AfterInsertRows|Tritt auf, wenn eine Zeile eingefügt wird. Sie können den Zeilenindex abrufen, indem Sie die Index-Eigenschaft des Arguments Aspose.Cells.GridDesktop.WorksheetEventArgs verwenden.|
|FailLoadFile|Tritt auf, wenn die Arbeitsmappe nicht geladen werden kann.|
|BeendenBerechnen|Tritt nach der Berechnungsformel in der Arbeitsmappe auf.|
|FinishLoadFile|Tritt auf, wenn die Arbeitsmappe geladen wird.|
|FocusedCellChanged|Tritt auf, wenn der Fokus einer Zelle geändert wird.|
|RowHeaderKlick|Tritt auf, wenn auf die Zeilenüberschrift geklickt wird.|
|RowHeaderDoubleClick|Tritt auf, wenn auf den Zeilenkopf doppelgeklickt wird.|
|RowColumnHiddenChanged|Tritt auf, wenn der ausgeblendete Zeilen- oder Spaltenstatus geändert wird.|
|SelectedSheetIndexChanged|Tritt auf, wenn ein Benutzer ein neues Arbeitsblatt auswählt, d. h. wenn das ausgewählte Blatt von einem Arbeitsblatt zu einem anderen wechselt. Dieses Ereignis kann auch programmgesteuert ausgelöst werden, wenn sich die ActiveSheetIndex-Eigenschaft des GridDesktop-Steuerelements ändert.|
## **Umgang mit Grid-Ereignissen**
Erstellen Sie einen Ereignishandler, um eine bestimmte Operation auszuführen, wenn ein bestimmtes Ereignis ausgelöst wird. Ein Ereignishandler führt eine bestimmte Aufgabe aus, wenn ein bestimmtes Ereignis ausgelöst wird. Unten wird ein Ereignishandler eingerichtet, um ein einfaches Grid-Ereignis mit Visual Studio.NET zu behandeln.

**Schritt 1: Auswählen eines Ereignisses von Aspose.Cells.GridDesktop Control**

1. Wählen Sie in Visual Studio das Aspose.Cells.GridDesktop-Steuerelement aus und öffnen Sie es**Eigenschaften**Dialog.
1.  Drücke den**Veranstaltungen** Tab.
1.  Wählen Sie eine Veranstaltung aus. (für dieses Beispiel die**CellClick** Veranstaltung ausgewählt ist).

**Schritt 2: Erstellen eines Ereignishandlers**

1.  Doppelklicken Sie auf ein ausgewähltes Ereignis in der**Eigenschaften**Dialog.
1. Wenn auf das Ereignis doppelgeklickt wird, wird von Visual Studio.NET ein Ereignishandler erstellt. Es folgt ein vom Designer generierter Code, der zeigt, dass ein Ereignis für das GridControl-Steuerelement erstellt wird.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents.Designer-DesignerGeneratedCode.cs" >}}


 Fügen Sie nun Code hinzu, um die gewünschte Operation innerhalb des Ereignishandlers auszuführen. Für dieses Beispiel haben wir eine Codezeile hinzugefügt, die ein Meldungsfeld für Benachrichtigungen anzeigt.
Sehen Sie sich den Ereignishandler an, den Visual Studio dem CellClick-Ereignis des GridDesktop-Steuerelements hinzugefügt hat. Es sieht ungefähr so aus wie im folgenden Code.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents-ClickEvent.cs" >}}


**Schritt 3: Ausführen der Anwendung**

1. Erstellen Sie die Anwendung und führen Sie sie aus.
1. Immer wenn auf eine Rasterzelle geklickt wird, erscheint ein Meldungsfeld mit der Meldung „Cell wird angeklickt“.
