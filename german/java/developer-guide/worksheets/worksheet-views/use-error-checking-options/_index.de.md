---
title: Verwenden von Fehlerüberprüfungsoptionen
type: docs
weight: 60
url: /de/java/use-error-checking-options/
---

{{% alert color="primary" %}} 

Microsoft Excel ermöglicht es Benutzern, Fehlerüberprüfungsoptionen und -regeln zu definieren. Benutzer sehen oft Fehlerüberprüfungen, wenn sie Formeln erstellen, ein kleines Dreieck in der rechten oberen Ecke einer Zelle zeigt an, wenn es ein Problem mit einer Zelle gibt. Excel bietet Informationen, die Benutzern helfen, häufige Probleme zu korrigieren.

{{% /alert %}} 
## **Arten von Fehlern**
Fehler, die bedeuten, dass die Formel kein Ergebnis zurückgeben kann - zum Beispiel das Teilen einer Zahl durch Null - erfordern sofortige Aufmerksamkeit, und ein Fehlerwert wird in der Zelle angezeigt. Durch Klick auf das grüne Dreieck wird ein Ausrufezeichen angezeigt, ein Klick darauf öffnet eine Liste von Optionen. 

Der Fehler kann mithilfe der Optionen behoben oder ignoriert werden. Das Ignorieren eines Fehlers bedeutet, dass dieser bei weiteren Fehlerprüfungen nicht mehr angezeigt wird.

Aspose.Cells bietet Funktionen für die Fehlerüberprüfung. Die ErrorCheckOptions-Klasse verwaltet verschiedene Arten von Fehlerüberprüfungen, z. B. Zahlen, die als Text gespeichert sind, Formelberechnungsfehler und Validierungsfehler. Verwenden Sie die ErrorCheckType-Aufzählung, um die gewünschte Fehlerüberprüfung festzulegen.
## **Als Text gespeicherte Zahlen**
Gelegentlich werden Zahlen formatiert und in Zellen als Text gespeichert. Dies kann Probleme bei Berechnungen verursachen oder irreführende Sortierreihenfolgen erzeugen. Zahlen, die als Text formatiert sind, sind in der Zelle linksbündig anstelle von rechtsbündig. Wenn eine Formel, die eine mathematische Operation mit Zellen durchführen sollte, kein Ergebnis zurückgibt, überprüfen Sie die Ausrichtung in den Zellen, auf die sich die Formel bezieht - einige oder alle diese Zellen könnten als Text formatierte Zahlen sein.

Sie können die Fehlerprüfungsoptionen verwenden, um Zahlen, die als Text gespeichert sind, schnell in echte Zahlen umzuwandeln. In Microsoft Excel 2003:

1. Klicken Sie im Menü **Extras** auf **Optionen**.
1. Wählen Sie den Tab Fehlerüberprüfung aus.
   Die Option **Als Text gespeicherte Zahl** ist standardmäßig aktiviert. 
1. Deaktivieren Sie es.
   Sehen Sie untenstehendes Bild, wie das grüne Dreieck für die Daten in MS Excel angezeigt wird.

![todo:image_alt_text](use-error-checking-options_1.png)

Der folgende Beispielcode zeigt, wie Sie die Option zur Fehlerprüfung von als Text gespeicherten Zahlen für ein Arbeitsblatt in der Vorlage XLS-Datei mithilfe der Aspose.Cells-APIs deaktivieren. 

**Java**

{{< highlight csharp >}}

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
{{< app/cells/assistant language="java" >}}
