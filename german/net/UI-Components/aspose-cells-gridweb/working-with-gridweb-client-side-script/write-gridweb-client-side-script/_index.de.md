---
title: Schreiben von clientseitigem Skript für GridWeb
type: docs
weight: 10
url: /de/net/aspose-cells-gridweb/write-gridweb-client-side-script/
keywords: GridWeb,client,js,javascript
description: Dieser Artikel zeigt, wie man mit Client JS APIs in GridWeb arbeitet.
---

{{% alert color="primary" %}} 

Entwickler können clientseitige Skripte für die Aspose.Cells.GridWeb-Steuerung schreiben. Dies bedeutet, dass es möglich ist, clientseitig eine JavaScript-Funktion aufzurufen, um eine bestimmte Aufgabe im Zusammenhang mit der GridWeb-Steuerung auszuführen. Beispielsweise können Entwickler JavaScript-Funktionen schreiben, um GridWeb-Daten an einen Server zu senden oder eine Warnmeldung anzuzeigen, wenn ein Validierungsfehler auftritt usw.

Dieses Thema erläutert diese Funktion anhand von Beispielen.

{{% /alert %}} 
## **Clientseitige Skripte für Aspose.Cells.GridWeb schreiben**
### **Grundlegende Informationen**
Aspose.Cells.GridWeb bietet zwei eigens erstellte Eigenschaften zur Unterstützung von clientseitigen Skripten:

- OnSubmitClientFunction
- OnValidationErrorClientFunction

Erstellen Sie JavaScript-Funktionen in einer ASPX-Seite und weisen Sie den Namen dieser Funktionen den Eigenschaften OnSubmitClientFunction und OnValidationErrorClientFunction zu.

{{% alert color="primary" %}} 

Die JavaScript-Funktion, die der Eigenschaft OnSubmitClientFunction zugewiesen wird, muss wie unten dargestellt ordnungsgemäß definiert sein:

**JavaScript**

{{< highlight csharp >}}

 function function_name(arg, cancelEdit)

 {

   //Add javascript code here

 }



{{< /highlight >}}

wobei der [arg]-Parameter den vom Steuerelement generierten Befehl darstellt. Der Befehl kann "Speichern", "Senden", "Rückgängig machen" usw. sein und der [cancelEdit]-Parameter ist ein boolescher Wert, der angibt, ob die Benutzereingabe storniert wird oder nicht.

Jede JavaScript-Funktion, die der Eigenschaft OnSubmitClientFunction zugewiesen ist, wird vor dem Senden von GridWeb-Daten an einen Server jedes Mal von der GridWeb-Steuerung aufgerufen. Ebenso wird, wenn einer Funktion die Eigenschaft OnValidationErrorClientFunction zugewiesen ist, diese Funktion jedes Mal aufgerufen, wenn ein Validierungsfehler auftritt.

{{% /alert %}} 
### **Funktionen für clientseitige Skripte**
Aspose.Cells.GridWeb bietet auch speziell für clientseitige Skripte entwickelte Funktionen. Diese Funktionen können in JavaScript-Funktionen verwendet werden, um mehr Kontrolle über Aspose.Cells.GridWeb zu erhalten. Diese clientseitigen Funktionen umfassen Folgendes:

|**Funktionen**|**Beschreibung**|
| :- | :- |
|updateData(bool cancelEdit)|Aktualisiert alle clientseitigen Daten von Aspose.Cells.GridWeb, bevor sie an den Server gesendet werden. Wenn der cancelEdit-Parameter true ist, verwirft GridWeb alle Benutzereingaben.|
|validateAll()|Wird verwendet, um zu überprüfen, ob Fehler bei der Validierung der Benutzereingabe vorliegen. Falls ein Fehler vorliegt, gibt die Funktion false zurück, ansonsten true.|
|submit(string arg, bool cancelEdit)|Rufen Sie diese Funktion auf, um Daten an den Server zu senden oder zu übermitteln. Diese Funktion führt beide Aufgaben aus, nämlich Daten aktualisieren und Benutzereingabe validieren. Diese Funktion kann auch ein Befehlsereignis auf der Serverseite auslösen. Verwenden Sie den arg-Parameter, um Ihren Befehl zu übergeben. Zum Beispiel wird der BEFEHL SPEICHERN zum Klicken auf die Schaltfläche **Speichern** in der Befehlsleiste der GridWeb-Steuerung verwendet und der CCMD:MYCOMMAND-Befehl löst ein benutzerdefiniertes Befehlsereignis aus.|
|setActiveCell(int row, int column)|Wird verwendet, um eine bestimmte Zelle zu aktivieren.|
|setCellValue(int row, int column, string value)|Wird verwendet, um einen Wert in eine beliebige Zelle einzufügen, die mit ihren Zeilen- und Spaltennummern angegeben ist.|
|getCellValue(int row, int column)|Gibt den Wert einer bestimmten Zelle zurück.|
|getActiveRow()|Wird in Verbindung mit der Funktion getActiveColumn() verwendet, um die Position einer aktiven Zelle zu bestimmen.|
|getActiveColumn()|Wird in Verbindung mit der Funktion getActiveRow() verwendet, um die Position einer aktiven Zelle zu bestimmen.|
|getSelectRange()|Gibt den zuletzt ausgewählten Bereich zurück.|
|setSelectRange()|Wählt den angegebenen Bereich aus.|
|clearSelections()|Löscht alle Auswahl außer der aktuellen aktiven Zelle.|
|getCellsArray()|Wird zusammen mit anderen verwandten Funktionen wie getCellName(), getCellValueByCell(), getCellRow() und getCellColumn() verwendet. Bitte lesen Sie diesen Artikel für weitere Informationen zur Verwendung dieser Funktion: [Lesen Sie die Werte der GridWeb-Zellen auf der Clientseite](/cells/de/net/aspose-cells-gridweb/read-the-values-of-the-gridweb-cells-on-client-side/)|
Um eine Testanwendung zu erstellen, die clientseitige Skripte enthält, die mit Aspose.Cells.GridWeb funktionieren, befolgen Sie die folgenden Schritte:

1. Erstellen Sie JavaScript-Funktionen, die von GridWeb aufgerufen werden sollen.
   These functions will be added to the ASP.NET page's <script></script> tag.
1. Weisen Sie den Funktionen Namen zu den Eigenschaften OnSubmitClientFunction und OnValidationErrorClientFunction zu.

Der Ausgabecodebeispiel wird unten angezeigt:

**Eine Validierung wurde der Zelle C1 hinzugefügt** 

![todo:image_alt_text](write-gridweb-client-side-script_1.png)

Fügen Sie einen ungültigen Wert hinzu und klicken Sie auf **Speichern**. Es tritt ein Validierungsfehler auf und die ValidationErrorFunction wird ausgeführt.

**ValidationErrorFunction wird bei Validierungsfehler aufgerufen** 

![todo:image_alt_text](write-gridweb-client-side-script_2.png)

Bis Sie einen gültigen Wert eingeben, werden keine Daten an den Server übermittelt. Geben Sie einen gültigen Wert ein und klicken Sie auf **Speichern**. Die ConfirmFunction wird ausgeführt.

**ConfirmFunction wird aufgerufen, bevor GridWeb-Daten an den Server übermittelt werden** 

![todo:image_alt_text](write-gridweb-client-side-script_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript-WriteClientSideScript.aspx" >}}

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript.aspx-WriteClientSideScript.cs" >}}
