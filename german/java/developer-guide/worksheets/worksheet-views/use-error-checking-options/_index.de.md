---
title: Verwenden Sie die Optionen zur Fehlerprüfung
type: docs
weight: 60
url: /de/java/use-error-checking-options/
---
{{% alert color="primary" %}} 

Microsoft Mit Excel können Benutzer Optionen und Regeln für die Fehlerprüfung definieren. Benutzer sehen beim Erstellen von Formeln häufig Fehlerprüfungen. Ein kleines Dreieck in der oberen rechten Ecke einer Zelle hebt hervor, wenn ein Problem mit einer Zelle vorliegt. Excel bietet Informationen, die Benutzern helfen, allgemeine Probleme zu beheben.

{{% /alert %}} 
## **Arten von Fehlern**
Fehler, die dazu führen, dass die Formel kein Ergebnis zurückgeben kann – wie z. B. das Teilen einer Zahl durch Null – erfordern sofortige Aufmerksamkeit, und in der Zelle wird ein Fehlerwert angezeigt. Ein Klick auf das grüne Dreieck zeigt ein Ausrufezeichen, ein Klick darauf öffnet eine Liste mit Optionen.

Der Fehler kann mit den Optionen behoben oder ignoriert werden. Das Ignorieren eines Fehlers bedeutet, dass dieser Fehler bei weiteren Fehlerprüfungen nicht angezeigt wird.

Aspose.Cells bietet Optionen zur Fehlerprüfung. Die ErrorCheckOptions-Klasse verwaltet verschiedene Arten von Fehlerprüfungen, beispielsweise als Text gespeicherte Zahlen, Formelberechnungsfehler und Validierungsfehler. Verwenden Sie die ErrorCheckType-Enumeration, um die gewünschte Fehlerprüfung festzulegen.
## **Als Text gespeicherte Zahlen**
Gelegentlich können Zahlen formatiert und in Zellen als Text gespeichert werden. Dies kann zu Berechnungsproblemen oder verwirrenden Sortierreihenfolgen führen. Als Text formatierte Zahlen werden in der Zelle linksbündig statt rechtsbündig ausgerichtet. Wenn eine Formel, die eine mathematische Operation an Zellen ausführen soll, keinen Wert zurückgibt, überprüfen Sie die Ausrichtung in den Zellen, auf die sich die Formel bezieht – einige oder alle dieser Zellen könnten Zahlen sein, die als Text formatiert sind.

Sie können die Fehlerprüfungsoptionen verwenden, um als Text gespeicherte Zahlen schnell in reelle Zahlen umzuwandeln. In Microsoft Excel 2003:

1.  Auf der**Werkzeug** Menü, klicken**Optionen**.
1. Wählen Sie die Registerkarte Fehlerprüfung.
   **Nummer als Text gespeichert** Option ist standardmäßig aktiviert.
1. Deaktivieren Sie es.
 Sehen Sie sich das folgende Bild an, wie das grüne Dreieck für die Daten in MS Excel angezeigt wird.

![todo: Bild_alt_Text](use-error-checking-options_1.png)

 Der folgende Beispielcode zeigt, wie die als Textfehlerprüfungsoption für ein Arbeitsblatt in der Vorlagen-XLS-Datei gespeicherten Zahlen mithilfe der Aspose.Cells-APIs deaktiviert werden.

**Java**

{{< highlight "csharp" >}}

 //Create a workbook and opening a template spreadsheet

Workbook workbook = new Workbook("d:\\files\\Book1.xls");

//Get the first worksheet

Worksheet sheet = workbook.getWorksheets().get(0);

//Instantiate the error checking options

ErrorCheckOptionCollection opts = sheet.getErrorCheckOptions();

int index = opts.add();

ErrorCheckOption opt = opts.get(index);

//Disable the numbers stored as text option

opt.setErrorCheck(ErrorCheckType.TEXT_NUMBER, false);

//Set the range

opt.addRange(CellArea.createCellArea(0, 0, 65535, 255));

//Save the Excel file

workbook.save("d:\\files\\out_test.xls");



{{< /highlight >}}
