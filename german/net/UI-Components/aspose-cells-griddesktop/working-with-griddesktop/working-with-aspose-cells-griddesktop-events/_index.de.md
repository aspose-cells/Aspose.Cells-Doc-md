---
title: Arbeiten mit Aspose.Cells.GridDesktop Ereignissen
type: docs
weight: 30
url: /de/net/aspose-cells-griddesktop/work-with-aspose-cells-griddesktop-events/
keywords: GridDesktop, Ereignis, Ereignisse
description: Dieser Artikel zeigt, wie Ereignisse in GridDesktop verwendet werden können.
---

{{% alert color="primary" %}} 

Ereignisse dienen dazu, Benachrichtigungen zu senden, wenn eine Änderung in einem Steuerelement oder einer Klasse auftritt. Aspose.Cells.GridDesktop verfügt über mehrere Ereignisse, die spezielle Aufgaben ausführen, wenn bestimmte Änderungen im Steuerelement auftreten. Dieses Thema bietet eine Einführung in alle von der Aspose.Cells.GridDesktop-Steuerung unterstützten Ereignisse und erklärt, wie diese Ereignisse behandelt werden können.

{{% /alert %}} 
## **Einführung**
Die Aspose.Cells.GridDesktop-Steuerung unterstützt mehrere Ereignisse, die mehr Kontrolle bieten, um Operationen auszuführen, wenn bestimmte Ereignisse ausgelöst werden. Nachfolgend finden Sie eine vollständige Liste der von der Aspose.Cells.GridDesktop-Steuerung unterstützten Ereignisse.

{{% alert color="primary" %}} 

Diese Liste enthält nicht die Ereignisse, die von der Control-Klasse in Aspose.Cells.GridDesktop geerbt werden.

{{% /alert %}} 

|**Ereignisse**|**Beschreibung**|
| :- | :- |
|BeforeCalculate|Tritt auf, bevor eine Formel in der Arbeitsmappe berechnet wird.|
|BeforeLoadFile| Tritt auf, bevor die Arbeitsmappe aus einer Datei geladen wird.|
|ColumnHeaderClick|Tritt auf, wenn auf die Spaltenüberschrift geklickt wird.|
|ColumnHeaderDoubleClick|Tritt auf, wenn auf die Spaltenüberschrift doppelgeklickt wird.|
|CellDataChanged|Tritt auf, wenn die Daten oder der Wert in einer Rasterzelle geändert werden. Dieses Ereignis kann auch ausgelöst werden, wenn der Wert einer Zelle programmgesteuert mithilfe der Value-Eigenschaft oder der SetCellValue-Methode einer GridCell geändert wird.|
|CellButtonClick|Tritt auf, wenn auf die Zellenschaltfläche geklickt wird.|
|CellCheckedChanged|Tritt auf, wenn die Checked-Eigenschaft des Zellenkontrollkästchens geändert wird.|
|CellSelectedIndexChanged|Tritt auf, wenn die SelectedIndex-Eigenschaft des Zellen-Dropdown-Felds geändert wird.|
|CellClick|Tritt auf, wenn auf eine Rasterzelle geklickt wird.|
||CellDoubleClick|Tritt auf, wenn auf eine Rasterzelle doppelgeklickt wird.|
|CellKeyPressed|Tritt auf, wenn eine Taste gedrückt wird, während eine Zelle den Fokus hat. Wenn Sie einen Ereignishandler für das CellKeyPressed-Ereignis erstellen möchten, setzen Sie die Handled-Eigenschaft des CellKeyEventArgs-Arguments auf true, um zu verhindern, dass die GridDesktop-Steuerung das Tastaturereignis behandelt.|
|AfterInsertColumns|Tritt auf, wenn eine Spalte eingefügt wird. Sie können den Spaltenindex mithilfe der Index-Eigenschaft des Aspose.Cells.GridDesktop.WorksheetEventArgs-Arguments erhalten.|
|AfterInsertRows|Tritt auf, wenn eine Zeile eingefügt wird. Sie können den Zeilenindex erhalten, indem Sie die Eigenschaft Index des Arguments Aspose.Cells.GridDesktop.WorksheetEventArgs verwenden.|
|FailLoadFile|Tritt auf, wenn das Arbeitsbuch nicht geladen werden kann.|
|FinishCalculate|Tritt nach der Berechnung der Formel im Arbeitsbuch auf.|
|FinishLoadFile|Tritt auf, wenn das Arbeitsbuch geladen ist.|
|FocusedCellChanged|Tritt immer dann auf, wenn der Fokus einer Zelle geändert wird.|
|RowHeaderClick|Tritt auf, wenn auf die Zeilenüberschrift geklickt wird.|
|RowHeaderDoubleClick|Tritt auf, wenn auf die Zeilenüberschrift doppelt geklickt wird.|
|RowColumnHiddenChanged|Tritt auf, wenn der Status der ausgeblendeten Zeile oder Spalte geändert wird.|
|SelectedSheetIndexChanged|Tritt auf, wenn ein Benutzer ein neues Arbeitsblatt auswählt, d.h. wenn das ausgewählte Blatt von einem Arbeitsblatt zu einem anderen wechselt. Dieses Ereignis kann auch programmgesteuert ausgelöst werden, wenn sich die Eigenschaft ActiveSheetIndex des Steuerelements GridDesktop ändert.|
## **Behandlung von Grid-Ereignissen**
Um eine bestimmte Operation durchzuführen, wenn ein bestimmtes Ereignis ausgelöst wird, erstellen Sie einen Ereignishandler. Ein Ereignishandler führt eine bestimmte Aufgabe aus, wenn ein bestimmtes Ereignis ausgelöst wird. Im Folgenden wird ein Ereignishandler eingerichtet, um ein einfaches Grid-Ereignis unter Verwendung von Visual Studio.NET zu behandeln.

**Schritt 1: Auswahl eines Ereignisses des Aspose.Cells.GridDesktop-Control**

1. Wählen Sie in Visual Studio das Aspose.Cells.GridDesktop-Control aus und öffnen Sie seinen **Eigenschaften**-Dialog.
1. Klicken Sie auf die Registerkarte **Ereignisse**.
1. Wählen Sie ein Ereignis aus. (Für dieses Beispiel wird das Ereignis **CellClick** ausgewählt).

**Schritt 2: Erstellung eines Ereignishandlers**

1. Doppelklicken Sie auf ein ausgewähltes Ereignis im Dialogfeld **Eigenschaften**.
1. Wenn das Ereignis doppelt geklickt wird, wird von Visual Studio.NET ein Ereignishandler erstellt. Im Folgenden wird der vom Designer generierte Code gezeigt, der zeigt, dass ein Ereignis für das GridControl-Control erstellt wird.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents.Designer-DesignerGeneratedCode.cs" >}}


Fügen Sie nun Code hinzu, um die gewünschte Operation im Ereignishandler auszuführen. In diesem Beispiel haben wir eine Codezeile hinzugefügt, die ein Meldungsfenster für Benachrichtigungen anzeigt. 
Werfen Sie einen Blick auf den Ereignishandler, den Visual Studio dem CellClick-Ereignis des GridDesktop-Control hinzugefügt hat. Es wird etwa wie der folgende Code aussehen.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-GridDesktopEvents-ClickEvent.cs" >}}


**Schritt 3: Ausführen der Anwendung**

1. Erstellen und Ausführen der Anwendung.
1. Immer wenn auf eine Zellenkachel geklickt wird, erscheint ein Meldungsfenster mit der Meldung "Zelle wurde angeklickt".
