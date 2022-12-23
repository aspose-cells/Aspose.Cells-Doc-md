---
title: Schreiben Sie GridWeb Client-seitiges Skript
type: docs
weight: 10
url: /de/net/write-gridweb-client-side-script/
---
{{% alert color="primary" %}} 

Entwickler können clientseitige Skripts für das Aspose.Cells.GridWeb-Steuerelement schreiben. Dies bedeutet, dass es möglich ist, eine clientseitige JavaScript-Funktion aufzurufen, um eine bestimmte Aufgabe im Zusammenhang mit dem GridWeb-Steuerelement auszuführen. Beispielsweise können Entwickler JavaScript-Funktionen schreiben, um GridWeb-Daten an einen Server zu senden oder eine Warnmeldung anzuzeigen, wenn ein Validierungsfehler auftritt usw.

In diesem Thema wird diese Funktion anhand von Beispielen erläutert.

{{% /alert %}} 
## **Clientseitige Skripte für Aspose.Cells.GridWeb schreiben**
### **Grundinformation**
Aspose.Cells.GridWeb bietet zwei Eigenschaften, die speziell zur Unterstützung clientseitiger Skripts erstellt wurden:

- OnSubmitClientFunction
- OnValidationErrorClientFunction

Erstellen Sie JavaScript-Funktionen auf einer ASPX-Seite, und weisen Sie die Namen dieser Funktionen den Eigenschaften OnSubmitClientFunction und OnValidationErrorClientFunction zu.

{{% alert color="primary" %}} 

Die JavaScript-Funktion, die der OnSubmitClientFunction-Eigenschaft zugewiesen wird, muss wie unten gezeigt richtig definiert werden:

**JavaScript**

{{< highlight "csharp" >}}

 function function_name(arg, cancelEdit)

 {

   //Add javascript code here

 }



{{< /highlight >}}

wobei der Parameter [arg] den von der Steuerung generierten Befehl darstellt. Der Befehl kann "Save", "Submit", "Undo" usw. sein und der Parameter [cancelEdit] ist ein boolescher Wert, der angibt, ob die Benutzereingabe abgebrochen wird oder nicht.

Jede der OnSubmitClientFunction-Eigenschaft zugewiesene JavaScript-Funktion wird jedes Mal vom GridWeb-Steuerelement aufgerufen, bevor GridWeb-Daten an einen Server gesendet werden. Wenn der OnValidationErrorClientFunction-Eigenschaft eine Funktion zugewiesen ist, wird diese Funktion entsprechend jedes Mal aufgerufen, wenn ein Validierungsfehler auftritt.

{{% /alert %}} 
### **Funktionen für Client-seitiges Scripting**
Aspose.Cells. GridWeb stellt auch Funktionen speziell für clientseitige Skripterstellung bereit. Diese Funktionen können innerhalb von JavaScript-Funktionen verwendet werden, um mehr Kontrolle über Aspose.Cells.GridWeb zu erlangen. Diese clientseitigen Funktionen umfassen Folgendes:

|**Funktionen**|**Beschreibung**|
|:- |:- |
|updateData(bool cancelEdit)|Aktualisiert alle Client-Daten von Aspose.Cells.GridWeb, bevor sie an den Server gesendet werden. Wenn der Parameter cancelEdit wahr ist, verwirft GridWeb alle Benutzereingaben.|
|validateAll()|Wird verwendet, um zu überprüfen, ob es Validierungsfehler in der Benutzereingabe gibt. Im Fehlerfall gibt die Funktion false zurück, ansonsten true .|
|submit(string arg, bool cancelEdit)|Rufen Sie diese Funktion zum Postback auf oder senden Sie Daten an den Server. Diese Funktion führt beide Aufgaben aus, nämlich das Aktualisieren von Daten und das Validieren von Benutzereingaben. Diese Funktion kann auch ein Befehlsereignis auf der Serverseite auslösen. Verwenden Sie den arg-Parameter, um Ihren Befehl zu übergeben. Beispiel: Der SAVE-Befehl wird zum Anklicken von verwendet**Speichern** auf der Befehlsleiste des GridWeb-Steuerelements und der Befehl CCMD:MYCOMMAND löst ein CustomCommand-Ereignis aus.|
|setActiveCell(int-Zeile, int-Spalte)|Wird verwendet, um eine bestimmte Zelle zu aktivieren.|
|setCellValue(int-Zeile, int-Spalte, String-Wert)|Wird verwendet, um einen Wert in eine beliebige Zelle einzugeben, die anhand ihrer Zeilen- und Spaltennummern angegeben wird.|
|getCellValue(int Zeile, int Spalte)|Gibt den Wert einer beliebigen angegebenen Zelle zurück.|
|getActiveRow()|Wird zusammen mit der Funktion getActiveColumn() verwendet, um die Position einer aktiven Zelle zu bestimmen.|
|getActiveColumn()|Wird zusammen mit der Funktion getActiveRow() verwendet, um die Position einer aktiven Zelle zu bestimmen.|
|getSelectRange()|Gibt den zuletzt ausgewählten Bereich zurück.|
|setSelectRange()|Wählt den angegebenen Bereich aus.|
|clearSelections()|Löscht die gesamte Auswahl mit Ausnahme der aktuell aktiven Zelle.|
|getCellsArray()| Es wird mit anderen verwandten Funktionen wie getCellName(), getCellValueByCell(), getCellRow() und getCellColumn() verwendet. Bitte lesen Sie diesen Artikel für weitere Informationen zur Verwendung dieser Funktion:[Lesen Sie die Werte der GridWeb-Zellen auf der Clientseite](/cells/de/net/read-the-values-of-the-gridweb-cells-on-client-side/)|
Führen Sie die folgenden Schritte aus, um eine Testanwendung mit clientseitigen Skripts zu erstellen, die mit Aspose.Cells.GridWeb funktionieren:

1. Erstellen Sie JavaScript-Funktionen, die von GridWeb aufgerufen werden sollen.
 Diese Funktionen werden der Seite ASP.NET hinzugefügt<script></script> Schild.
1. Weisen Sie den Eigenschaften OnSubmitClientFunction und OnValidationErrorClientFunction die Namen der Funktionen zu.

Die Ausgabe des Codebeispiels ist unten dargestellt:

**Eine Validierung, die der C1-Zelle hinzugefügt wurde** 

![todo: Bild_alt_Text](write-gridweb-client-side-script_1.png)

 Fügen Sie einen ungültigen Wert hinzu und klicken Sie auf**Speichern**. Es tritt ein Validierungsfehler auf und die ValidationErrorFunction wird ausgeführt.

**ValidationErrorFunction wird bei einem Validierungsfehler aufgerufen** 

![todo: Bild_alt_Text](write-gridweb-client-side-script_2.png)

 Bis Sie einen gültigen Wert eingeben, werden keine Daten an den Server gesendet. Geben Sie einen gültigen Wert ein und klicken Sie auf**Speichern**. Die ConfirmFunction wird ausgeführt.

**ConfirmFunction wird aufgerufen, bevor GridWeb-Daten an den Server gesendet werden** 

![todo: Bild_alt_Text](write-gridweb-client-side-script_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript-WriteClientSideScript.aspx" >}}

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript.aspx-WriteClientSideScript.cs" >}}
