---
title: Arbeiten mit GridWeb Ereignissen
type: docs
weight: 70
url: /de/net/aspose-cells-gridweb/gridweb-events/
keywords: GridWeb, Ereignisse, Ereignis
description: Dieser Artikel stellt vor, wie man mit verschiedenen Ereignissen in GridWeb arbeitet.
---

{{% alert color="primary" %}} 

Alle Programmier müssen mit Ereignissen und deren Verwendung vertraut sein. Ereignisse werden verwendet, um Benachrichtigungen über Änderungen zu senden, die in einer Steuerung oder Klasse auftreten können. Aspose.Cells.GridWeb verfügt über mehrere Ereignisse, die verwendet werden können, um spezifische Aufgaben auszuführen, wenn bestimmte Änderungen in der Steuerung auftreten.

Dieses Thema bietet eine Einführung in alle von Aspose.Cells.GridWeb-Steuerelement unterstützten Ereignisse sowie einige Details dazu, wie diese Ereignisse gehandhabt werden können.

{{% /alert %}} 
## **Arbeiten mit Grid-Ereignissen**
### **Einführung in Grid-Ereignisse**
Das Aspose.Cells.GridWeb-Steuerelement unterstützt mehrere Ereignisse, die eine genauere Steuerung bei der Ausführung von Operationen ermöglichen, wenn bestimmte Ereignisse im Steuerelement ausgelöst werden. Eine vollständige Liste der von Aspose.Cells.GridWeb-Steuerelement unterstützten Ereignisse finden Sie unten.

{{% alert color="primary" %}} 

Diese Liste enthält nicht die von der Control-Klasse geerbten Ereignisse von Aspose.Cells.GridWeb.

{{% /alert %}} 

|**Ereignisse** |**Beschreibung** |
| :- | :- |
|CellCommand |Tritt auf, wenn der Befehls-Hyperlink einer Zelle angeklickt wird. Wenn dieses Ereignis ausgelöst wird, liefert sein Parameter e.Argument den Namen des Befehls. |
|CellDoubleClick |Tritt auf, wenn auf eine Zelle doppelgeklickt wird. |
|CellError |Tritt auf, wenn der Eingabewert einer Zelle einen Fehler aufweist. |
|ColumnDeleted |Tritt auf, wenn ein Benutzer eine Spalte aus einem Arbeitsblatt über das Client-Seitenmenü löscht. |
|ColumnDeleting |Tritt auf, wenn ein Benutzer versucht, eine Spalte aus einem Arbeitsblatt über das Client-Seitenmenü zu löschen. |
|ColumnDoubleClick |Tritt auf, wenn auf die Spaltenüberschrift doppelgeklickt wird. |
|ColumnInserted |Tritt auf, wenn ein Benutzer über das Client-Seitenmenü eine Spalte in ein Arbeitsblatt einfügt. |
|CustomCommand |Tritt auf, wenn ein Benutzer auf eine benutzerdefinierte Befehlsschaltfläche klickt. |
|LoadCustomData |Tritt auf, wenn die Eigenschaft EnableSession der Steuerung auf false gesetzt ist und Arbeitsblattdaten geladen werden müssen. Sie können dieses Ereignis im moduslosen Modus behandeln, um Arbeitsblattdaten aus einer Datei oder einer Datenbank zu laden. |
|PageIndexChanged |Tritt auf, wenn der Blattseitenindex der Steuerelemente geändert wird. |
|RowDeleted |Tritt auf, wenn ein Benutzer eine Zeile aus einem Arbeitsblatt über das Klientenseitenmenü löscht. |
|RowDeleting |Tritt auf, wenn ein Benutzer versucht, eine Zeile aus einem Arbeitsblatt über das Klientenseitenmenü zu löschen. |
|RowDoubleClick |Tritt auf, wenn auf die Zeilenüberschrift doppelgeklickt wird. |
|RowInserted |Tritt auf, wenn ein Benutzer über das Klientenseitenmenü eine Zeile in das Arbeitsblatt einfügt. |
|SaveCommand |Tritt auf, wenn auf die Schaltfläche **Speichern** geklickt wird. |
|SheetDataUpdated |Tritt auf, wenn das Steuerelement die übermittelten Daten geladen und die Arbeitsblattdaten aktualisiert hat. |
|SheetTabClick |Tritt auf, wenn auf eine Blattregisterkarte geklickt wird. |
|SubmitCommand |Tritt auf, wenn auf die Schaltfläche **Senden** geklickt wird. |
|UndoCommand |Tritt auf, wenn auf die Schaltfläche **Rückgängig** geklickt wird. |
|AjaxCallFinished |Wird ausgelöst, wenn das AJAX-Update des Steuerelements abgeschlossen ist (EnableAJAX muss auf true gesetzt sein). |
|CellModifiedOnAjax |Tritt auf, wenn die Zelle in einem AJAX-Aufruf geändert wird. |
|OnAfterColumnFilter |Wird ausgelöst, nachdem der Filter auf eine Spalte angewendet wurde. |
|OnBeforeColumnFilter |Wird ausgelöst, bevor der Filter auf eine Spalte angewendet wird. |
## **Behandlung von Grid-Ereignissen**
Um eine bestimmte Operation bei Auslösung eines bestimmten Ereignisses durchzuführen, müssen wir einen Ereignishandler erstellen. Ein Ereignishandler führt die gewünschte Aufgabe aus, wenn ein bestimmtes Ereignis ausgelöst wird. Die unten dargestellten Schritte zeigen, wie man ein einfaches Grid-Ereignis mithilfe von Visual Studio behandelt.
### **Schritt 1: Auswahl eines Ereignisses des Aspose.Cells.GridWeb-Steuerelements**
1. Wählen Sie das Aspose.Cells.GridWeb-Steuerelement und öffnen Sie den Eigenschaften-Dialog auf der rechten Seite.
1. Klicken Sie auf die Schaltfläche **Ereignisse** Tab.
1. Wählen Sie ein Ereignis aus.
   In diesem Beispiel ist das SaveCommand-Ereignis ausgewählt.
### **Schritt 2: Erstellen eines Ereignisbehandlers**
1. Doppelklicken Sie auf ein Ereignis im Dialogfeld Eigenschaften. 

   **Doppelklick auf ein ausgewähltes Ereignis** 

![todo:image_alt_text](working-with-gridweb-events_1.png)




Wenn auf das Ereignis doppelgeklickt wird, wird automatisch ein Ereignisbehandler von Visual Studio erstellt. 

**Ein Ereignisbehandler erstellt von Visual Studio** 

![todo:image_alt_text](working-with-gridweb-events_2.png)




1. Fügen Sie Code hinzu, um im Ereignisbehandler eine Aktion auszuführen.

Hier wurde eine einzelne Codezeile hinzugefügt, die den Rasterinhalt in eine Excel-Datei speichert, wenn die Schaltfläche **Speichern** geklickt wird.

Um weitere Informationen zu erhalten, bewegen Sie den Cursor nach oben, um etwas Code zu sehen. Dann werden Sie feststellen, dass Visual Studio intelligent genug ist, um einen Ereignisbehandler für das GridWeb's SaveCommand-Ereignis hinzuzufügen.
### **Schritt 3: Ausführen Ihrer Anwendung**
1. Erstellen und Ausführen der Anwendung.
1. Klicken Sie auf **Speichern**.

Der Rasterinhalt wird in eine Excel-Datei gespeichert. 

**Anwendungsmodus ausgeführt** 

![todo:image_alt_text](working-with-gridweb-events_3.png)
