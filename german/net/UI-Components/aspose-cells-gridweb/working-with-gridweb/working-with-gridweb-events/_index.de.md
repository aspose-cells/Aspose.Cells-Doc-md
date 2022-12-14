---
title: Arbeiten mit GridWeb-Ereignissen
type: docs
weight: 70
url: /de/net/working-with-gridweb-events/
---
{{% alert color="primary" %}} 

Alle Programmierer müssen mit Ereignissen und ihrem Zweck vertraut sein. Ereignisse werden verwendet, um Benachrichtigungen über Änderungen zu senden, die in einem Steuerelement oder einer Klasse auftreten können. Aspose.Cells. GridWeb verfügt über mehrere Ereignisse, die verwendet werden können, um bestimmte Aufgaben auszuführen, wenn bestimmte Änderungen im Steuerelement auftreten.

Dieses Thema bietet eine Einführung in alle Ereignisse, die vom Aspose.Cells.GridWeb-Steuerelement unterstützt werden, zusammen mit einigen Details zur Behandlung dieser Ereignisse.

{{% /alert %}} 
## **Arbeiten mit Grid-Events**
### **Einführung in Grid-Events**
Aspose.Cells. Das GridWeb-Steuerelement unterstützt mehrere Ereignisse, die mehr Kontrolle für die Ausführung von Vorgängen bieten, wenn bestimmte Ereignisse im Steuerelement ausgelöst werden. Eine vollständige Liste der vom Aspose.Cells.GridWeb-Steuerelement unterstützten Ereignisse finden Sie unten.

{{% alert color="primary" %}} 

Diese Liste enthält keine Ereignisse, die von Aspose.Cells.GridWeb von der Control-Klasse geerbt wurden.

{{% /alert %}} 

|**Veranstaltungen** |**Beschreibung** |
|:- |:- |
| CellCommand| Tritt auf, wenn auf den Befehls-Hyperlink einer Zelle geklickt wird. Wenn dieses Ereignis ausgelöst wird, stellt sein Parameter e.Argument den Namen des Befehls bereit.|
| CellDoubleClick| Tritt auf, wenn auf die Zelle doppelgeklickt wird.|
| Zellenfehler| Tritt auf, wenn der Eingabewert einer Zelle einen Fehler aufweist.|
| SpalteGelöscht|Tritt auf, wenn ein Benutzer eine Spalte aus einem Arbeitsblatt mithilfe des clientseitigen Menüs löscht.|
| SpalteLöschen| Tritt auf, wenn ein Benutzer versucht, eine Spalte aus einem Arbeitsblatt mithilfe des clientseitigen Menüs zu löschen.|
| ColumnDoubleClick| Tritt auf, wenn auf die Spaltenüberschrift doppelgeklickt wird.|
| Spalte eingefügt| Tritt auf, wenn ein Benutzer über das clientseitige Menü eine Spalte in ein Arbeitsblatt einfügt.|
| CustomCommand| Tritt auf, wenn ein Benutzer auf eine benutzerdefinierte Befehlsschaltfläche klickt.|
| Benutzerdefinierte Daten laden| Tritt auf, wenn die EnableSession-Eigenschaft des Steuerelements auf „false“ festgelegt ist und Arbeitsblattdaten geladen werden müssen. Sie können dieses Ereignis im sitzungslosen Modus behandeln, um Arbeitsblattdaten aus einer Datei oder Datenbank zu laden.|
| SeitenindexGeändert| Tritt auf, wenn der Blattseitenindex des Steuerelements geändert wird.|
| ZeileGelöscht| Tritt auf, wenn ein Benutzer über das clientseitige Menü eine Zeile aus einem Arbeitsblatt löscht.|
| ZeilenLöschen| Tritt auf, wenn ein Benutzer versucht, eine Zeile aus einem Arbeitsblatt mithilfe des clientseitigen Menüs zu löschen.|
| RowDoubleClick|Tritt auf, wenn auf den Zeilenkopf doppelgeklickt wird.|
| Zeile eingefügt| Tritt auf, wenn ein Benutzer über das clientseitige Menü eine Zeile in ein Arbeitsblatt einfügt.|
| SaveCommand| Tritt auf, wenn die**Speichern** Schaltfläche angeklickt wird.|
| BlattdatenAktualisiert| Tritt auf, wenn das Steuerelement die bereitgestellten Daten geladen und die Arbeitsblattdaten aktualisiert hat.|
| SheetTabClick| Tritt auf, wenn auf eine Blattregisterkarte geklickt wird.|
| SubmitCommand| Tritt auf, wenn die**Einreichen** Schaltfläche angeklickt wird.|
| Rückgängig-Befehl| Tritt auf, wenn die**Rückgängig machen** Schaltfläche angeklickt wird.|
| AjaxCallFertig| Wird ausgelöst, wenn das AJAX-Update des Steuerelements abgeschlossen ist. (EnableAJAX muss auf true gesetzt werden).|
| CellModifiedOnAjax| Wird ausgelöst, wenn die Zelle im AJAX-Aufruf geändert wird.|
| OnAfterColumnFilter| Wird ausgelöst, nachdem der Filter auf eine Spalte angewendet wurde.|
| OnBeforeColumnFilter| Wird ausgelöst, bevor der Filter auf eine Spalte angewendet wird.|
## **Umgang mit Grid-Ereignissen**
Um eine bestimmte Operation beim Auslösen eines bestimmten Ereignisses auszuführen, müssen wir einen Ereignishandler erstellen. Ein Event-Handler führt die gewünschte Aufgabe aus, wenn ein bestimmtes Ereignis ausgelöst wird. Die unten dargestellten Schritte zeigen, wie ein einfaches Rasterereignis mit Visual Studio behandelt wird.
### **Schritt 1: Auswählen eines Ereignisses von Aspose.Cells.GridWeb Control**
1. Wählen Sie das Steuerelement Aspose.Cells.GridWeb aus und öffnen Sie auf der rechten Seite das Dialogfeld Eigenschaften.
1.  Drücke den**Registerkarte „Ereignisse“.** Taste.
1. Wählen Sie eine Veranstaltung aus.
 Für dieses Beispiel wird das SaveCommand-Ereignis ausgewählt.
### **Schritt 2: Erstellen eines Ereignishandlers**
1.  Doppelklicken Sie im Dialogfeld Eigenschaften auf ein Ereignis.

   **Doppelklicken Sie auf ein ausgewähltes Ereignis** 

![todo: Bild_alt_Text](working-with-gridweb-events_1.png)




 Wenn auf das Ereignis doppelgeklickt wird, wird automatisch ein Ereignishandler von Visual Studio erstellt.

**Ein von Visual Studio erstellter Ereignishandler** 

![todo: Bild_alt_Text](working-with-gridweb-events_2.png)




1. Fügen Sie Code hinzu, um eine Aktion innerhalb des Ereignishandlers auszuführen.

 Hier eine einzelne Codezeile, die den Rasterinhalt in einer Excel-Datei speichert, wenn die**Speichern** Schaltfläche angeklickt wurde hinzugefügt.

Um weitere Informationen zu erhalten, bewegen Sie den Cursor nach oben, um Code anzuzeigen, und Sie werden feststellen, dass Visual Studio intelligent genug ist, um einen Ereignishandler zum SaveCommand-Ereignis von GridWeb hinzuzufügen.
### **Schritt 3: Ausführen Ihrer Anwendung**
1. Erstellen Sie die Anwendung und führen Sie sie aus.
1.  Klicken**Speichern**.

 Der Rasterinhalt wird in einer Excel-Datei gespeichert.

**Anwendung im laufenden Modus** 

![todo: Bild_alt_Text](working-with-gridweb-events_3.png)
