---
title: Gruppieren von Zeilen und Erstellen von Teilergebnissen
type: docs
weight: 70
url: /de/net/aspose-cells-gridweb/group-rows-and-create-subtotal/
keywords: GridWeb,subtotal,group,ungroup
description: Dieser Artikel zeigt, wie man Zeilen/Spalten gruppieren/aufheben und mit Teilergebnissen in GridWeb arbeiten kann.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb kann eine Gliederung Ihrer Daten erstellen. Dadurch können Sie Detailstufen ein- und ausblenden, indem Sie auf die Gliederungssymbole '+' und '-' klicken, um nur die Zeilen anzuzeigen, die Zusammenfassungen oder Überschriften für Abschnitte in einem Arbeitsblatt bieten. Sie können die Symbole verwenden, um Details unter einer einzelnen Zusammenfassung oder Überschrift zu sehen.

Beim Gruppieren von Zeilen ist es wichtig, nur die Detailzeilen auszuwählen, die die Gruppe bilden. Schließen Sie nicht die dazugehörige Zusammenfassungszeile ein. Wenn beispielsweise Zeile 6 Summen für die Daten in den Zeilen 3 bis 5 enthält, wählen Sie nur Zeile 3 bis 5 aus, um die Gruppe zu definieren. Die Aspose.Cells.GridWeb-Kontrolle zeigt die Symbole **Detail anzeigen** (+) und **Detail ausblenden** (-) neben den Zeilenüberschriften an, die die Gruppen im Arbeitsblatt angeben.

Mit Aspose.Cells.GridWeb können Sie auch Teilergebnisse basierend auf einem beliebigen Datenfeld erstellen. Ein Teilergebnis ist nicht unbedingt eine Summe: Es kann ein Durchschnitt, eine Anzahl, ein Minimum, ein Maximum oder andere statistische Berechnungen sein.

In diesem Thema wird das Gruppieren von Zeilen und das Erstellen von Teilergebnissen mithilfe der Aspose.Cells.GridWeb-API behandelt. Entwickler können Zeilen mit beliebig vielen Verschachtelungsebenen gruppieren und problemlos Teilergebnisse erstellen.

{{% /alert %}} 
## **Zeilen gruppieren**
Um eine bestimmte Anzahl von Zeilen zu gruppieren:

1. Fügen Sie der Webformularsteuerung Aspose.Cells.GridWeb hinzu.
1. Greifen Sie auf ein Arbeitsblatt zu.
1. Wählen Sie die gewünschte Anzahl von Zellen in den Zeilen aus.
1. Gruppieren Sie die Zeilen.

Wenn die Zeilen gruppiert sind, wird oben an der Zusammenfassungszeile der Zeilen ein Ein-/Ausblenden-Button angezeigt. Sie können die Richtungseinstellung ändern. Die Eigenschaft WebWorksheet.IsSummaryRowBelow ist eine boolesche Eigenschaft. Setzen Sie sie auf false (Standard) und die Zusammenfassungszeile wird über den Detailzeilen angezeigt. Setzen Sie sie auf true und die Zusammenfassungszeile wird unter den Detailzeilen angezeigt. Klicken Sie auf den Einblenden/Ausblenden-Button, um gruppierte Zeilen einzublenden oder auszublenden.

Das folgende Beispiel gruppiert die Zeilen von der 2. Zeile bis zur 10. Zeile.

**Zeilen gruppieren** 

![todo:image_alt_text](group-rows-and-create-subtotal_1.png)



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Group the rows

sheet.Cells.GroupRows(1, 9);

{{< /highlight >}}
### **Verschachtelte gruppierte Zeilen**
Sie können Ebenen der Organisation erstellen, während Sie eine Reihe von Zeilen gruppieren. Sie können Zeilen unter den gruppierten Zeilen gruppieren. Das folgende Beispiel zeigt verschachtelte gruppierte Zeilen.

**Zeilen gruppieren** 

![todo:image_alt_text](group-rows-and-create-subtotal_2.png)



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Group the rows

sheet.Cells.GroupRows(1, 9);

// Create nested group of rows

sheet.Cells.GroupRows(4, 6);

{{< /highlight >}}
### **Interner Prozess: Wie funktioniert die Steuerung?**
Jede Zeile des Blattes hat eine Gliederungsnummer. Der Standardwert der Gliederungsnummer ist null. Jedes Mal, wenn Sie die Zeilen gruppieren, wird die Gliederungsnummer um 1 erhöht. Sie können die Gliederungsnummer erhalten, indem Sie die Methode GridWorksheet.Cells.GetRowOutlineLevel() aufrufen.
## **Zeilen gruppieren**
Aspose.Cells.GridWeb ermöglicht es Ihnen, gruppierte Zeilen zu entgruppieren.

Um eine bestimmte Anzahl von Zeilen zu entgruppieren:

1. Wählen Sie eine Anzahl von Zellen in den Zeilen im Arbeitsblatt, die Sie entgruppieren möchten.
1. Entgruppieren Sie die Zeilen.

Im folgenden Beispiel werden die Zeilen von der 2. Zeile bis zur 10. Zeile entgruppiert.



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Ungroup the rows

sheet.Cells.UngroupRows(1, 9); 

{{< /highlight >}}

{{% alert color="primary" %}} 

Wenn Sie die Methode GridWorksheet.Cells.UngroupRows() aufrufen, wird die Gliederungsnummer grupierter Zeilen auf null gesetzt.

{{% /alert %}} 
## **Summe erstellen**
Die Summenfunktion des Steuerungselements kann die Zeilen im Blatt mit einer bestimmten Spalte gruppieren und die Zusammenfassung der Spalten berechnen. Aspose.Cells.GridWeb kann automatisch Summenwerte für eine Liste berechnen. Wenn Sie Zwischensummen implementieren, gliedert das Steuerungselement die Liste, sodass Sie die Detailzeilen für jede Zwischensumme anzeigen und ausblenden können. Bevor Sie Zwischensummen hinzufügen, sortieren Sie nach dem Feld, für das Sie Zwischensummen wünschen. Verwenden Sie zur Erstellung von Zwischensummen eine beliebige Version der überladenen Methode WebWorksheet.CreateSubtotal.



{{< highlight java >}}

 public void CreateSubtotal

(

           int columnNameRowIndex,

           int dataRows,

           int groupByColumnIndex,

           SubtotalFunction subtotalFunction,

           int[] subtotalColumnIndexList

);

{{< /highlight >}}
### **Parameterliste**

|**Nr.**|**Parametername**|**Beschreibung**|
| :- | :- | :- |
|1|columnNameRowIndex|Der Zeilenindex der Spaltennamenzeile.|
|2|dataRows|Die Anzahl der Datensätze.|
|3|groupByColumnIndex|Der Spaltenindex der zu gruppierenden Spalte.|
|4|subtotalFunction|Die Aufzählung der Funktionstypen für die Zwischensumme.|
|5|subtotalColumnIndexList|Die Spaltenindizes, für die Zwischensummen gebildet werden sollen.|
### **Zusammenfassungsfunktionenliste**
Es gibt mehrere Arten von Zusammenfassungsfunktionen, die von der {[SubtotalFunction}}-Aufzählung unterstützt werden:

|**Nr.**|**Funktionsname**|**Beschreibung**|
| :- | :- | :- |
|1|AVERAGE|Berechnet den Durchschnitt der Werte.|
|2|COUNT|Zählt die numerischen Werte in den Zellen.|
|3|COUNTA|Zählt die nicht-numerischen Daten in den Zellen.|
|4|MAX|Berechnet den größten Wert.|
|5|MIN|Berechnet den kleinsten Wert.|
|6|PRODUCT|Berechnet das Produkt der Werte.|
|7|SUM|Berechnet die Summe der Werte.|
Das folgende Beispiel generiert die Zwischensummen, die die nicht-numerischen Werte gruppiert nach der zweiten Spalte im Arbeitsblatt berechnen.

**Zwischensummen** 

![todo:image_alt_text](group-rows-and-create-subtotal_3.png)



{{< highlight java >}}

 sheet.CreateSubtotal(0, sheet.Cells.MaxRow, 1, SubtotalFunction.COUNTA, new int[] { 1, 2, 3, 4, 5 });

{{< /highlight >}}
## **Zwischensumme entfernen**
Um eine Zwischensumme zu entfernen, verwenden Sie die Methode WebWorksheet.RemoveSubtotal. Das folgende Beispiel entfernt die Zwischensummen.



{{< highlight java >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

//Remove the subtotals

sheet.RemoveSubtotal();

{{< /highlight >}}
## **Über die SUBTOTAL-Funktion**
Der GridWeb-Steuerung verwendet die Formelfunktion SUBTOTAL, um den Zwischensummenwert zu berechnen.

Syntax: SUBTOTAL(function_num, ref1, ref2, ...)

function_num ist eine Zahl, die den Typ der Funktion angibt, die bei der Zwischensummenberechnung verwendet wird.

|**1**|**DURCHSCHNITT**|
| :- | :- |
|2|COUNT|
|3|COUNTA|
|4|MAX|
|5|MIN|
|6|PRODUCT|
|7|SUM|
Ref1, Ref2 usw. sind die Bereiche, die summiert werden sollen. Wenn Ref1, Ref2, ... andere Zwischensummenfunktionen enthalten, werden die referenzierten Zellen ignoriert, um doppelte Berechnungen zu vermeiden.
