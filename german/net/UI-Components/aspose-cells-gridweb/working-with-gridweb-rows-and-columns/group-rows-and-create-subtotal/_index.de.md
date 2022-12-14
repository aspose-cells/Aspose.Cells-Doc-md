---
title: Zeilen gruppieren und Zwischensumme erstellen
type: docs
weight: 70
url: /de/net/group-rows-and-create-subtotal/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb kann eine Gliederung für Ihre Daten erstellen. Auf diese Weise können Sie Detailebenen ein- und ausblenden, indem Sie auf die Gliederungssymbole "+" und "-" klicken, um nur die Zeilen anzuzeigen, die Zusammenfassungen oder Überschriften für Abschnitte in einem Arbeitsblatt enthalten. Sie können die Symbole verwenden, um Details unter einer einzelnen Zusammenfassung oder Überschrift anzuzeigen.

Beim Gruppieren von Zeilen ist es wichtig, nur die Detailzeilen auszuwählen, aus denen die Gruppe besteht. Schließen Sie die zugehörige Zusammenfassungszeile nicht ein. Wenn beispielsweise Zeile 6 Summen für die Daten in Zeile 3 bis 5 enthält, wählen Sie nur Zeile 3 bis 5 aus, um die Gruppe zu definieren. Das Aspose.Cells.GridWeb-Steuerelement zeigt die**Detail anzeigen** (+) und**Details verstecken** (-)-Symbole neben den Zeilenüberschriften, die die Gruppen im Arbeitsblatt angeben.

Aspose.Cells.GridWeb ermöglicht es Ihnen auch, Zwischensummen basierend auf beliebigen Datenfeldern zu erstellen. Eine Zwischensumme ist nicht unbedingt eine Summe: Sie kann ein Durchschnitt, eine Anzahl, ein Minimum, ein Maximum oder eine andere statistische Berechnung sein.

In diesem Thema wird das Gruppieren von Zeilen und das Erstellen von Zwischensummen mit Aspose.Cells.GridWeb API behandelt. Entwickler können Zeilen mit jeder Verschachtelungsebene gruppieren und Zwischensummen einfach erstellen.

{{% /alert %}} 
## **Zeilen gruppieren**
So gruppieren Sie eine bestimmte Anzahl von Zeilen:

1. Fügen Sie einem Webformular das Aspose.Cells.GridWeb-Steuerelement hinzu.
1. Greifen Sie auf ein Arbeitsblatt zu.
1. Wählen Sie die gewünschte Anzahl von Zellen in Zeilen aus.
1. Gruppieren Sie die Zeilen.

Wenn die Zeilen gruppiert sind, wird oben in der Zusammenfassungszeile der Zeilen eine Schaltfläche zum Erweitern/Reduzieren angezeigt. Sie können die Richtungseinstellung ändern. Die WebWorksheet.IsSummaryRowBelow-Eigenschaft ist eine boolesche Eigenschaft. Setzen Sie es auf „false“ (Standard) und die Zusammenfassungszeile befindet sich über den Detailzeilen. Setzen Sie es auf „true“ und die Zusammenfassungszeile befindet sich unter den Detailzeilen. Klicken Sie auf die Schaltfläche Erweitern/Reduzieren, um gruppierte Zeilen zu erweitern oder zu reduzieren.

Im folgenden Beispiel werden die Zeilen von der 2. bis zur 10. Zeile gruppiert.

**Zeilen gruppieren** 

![todo: Bild_alt_Text](group-rows-and-create-subtotal_1.png)



{{< highlight "java" >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Group the rows

sheet.Cells.GroupRows(1, 9);

{{< /highlight >}}
### **Gruppierte Zeilen verschachteln**
Sie können Organisationsebenen erstellen, während Sie eine Reihe von Zeilen gruppieren. Sie können Zeilen unter den gruppierten Zeilen gruppieren. Das folgende Beispiel zeigt das Verschachteln gruppierter Zeilen.

**Zeilen gruppieren** 

![todo: Bild_alt_Text](group-rows-and-create-subtotal_2.png)



{{< highlight "java" >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Group the rows

sheet.Cells.GroupRows(1, 9);

// Create nested group of rows

sheet.Cells.GroupRows(4, 6);

{{< /highlight >}}
### **Interner Prozess: Wie funktioniert die Kontrolle?**
Jede Reihe des Blattes hat eine Gliederungsnummer. Der Standardwert der Gliederungsnummer ist Null. Jedes Mal, wenn Sie die Zeilen gruppieren, wird die Gliederungsnummer um 1 erhöht. Sie können die Gliederungsnummer erhalten, indem Sie die Methode GridWorksheet.Cells.GetRowOutlineLevel() aufrufen.
## **Gruppierung von Zeilen aufheben**
Aspose.Cells.GridWeb ermöglicht es Ihnen, gruppierte Zeilen aufzuheben.

So heben Sie die Gruppierung einer bestimmten Anzahl von Zeilen auf:

1. Wählen Sie eine Reihe von Zellen in den Zeilen im Arbeitsblatt aus, um die Gruppierung aufzuheben.
1. Heben Sie die Gruppierung der Zeilen auf.

Im folgenden Beispiel wird die Gruppierung der Zeilen von der 2. bis zur 10. Zeile aufgehoben.



{{< highlight "java" >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Ungroup the rows

sheet.Cells.UngroupRows(1, 9); 

{{< /highlight >}}

{{% alert color="primary" %}} 

Wenn Sie die Methode GridWorksheet.Cells.UngroupRows() aufrufen, wird die Gliederungsnummer der gruppierten Zeilen auf Null gesetzt.

{{% /alert %}} 
## **Zwischensumme erstellen**
Die Zwischensummenfunktion des Steuerelements kann die Zeilen im Blatt mit einer bestimmten Spalte gruppieren und die Zusammenfassung der Spalten berechnen. Aspose.Cells.GridWeb kann Zwischensummenwerte für eine Liste automatisch berechnen. Wenn Sie Zwischensummen implementieren, gliedert das Steuerelement die Liste, sodass Sie die Detailzeilen für jede Zwischensumme anzeigen und ausblenden können. Sortieren Sie vor dem Hinzufügen von Zwischensummen nach dem Feld, für das Sie eine Zwischensumme erstellen möchten. Verwenden Sie zum Erstellen von Zwischensummen eine beliebige Version der überladenen WebWorksheet.CreateSubtotal-Methode.



{{< highlight "java" >}}

 public void CreateSubtotal

(

           int columnNameRowIndex,

           int dataRows,

           int groupByColumnIndex,

           SubtotalFunction subtotalFunction,

           int[]subtotalColumnIndexList

);

{{< /highlight >}}
### **Parameterliste**

|**Nein.**|**Parametername**|**Beschreibung**|
|:- |:- |:- |
|1|SpaltennameZeilenIndex|Der Zeilenindex der Zeile mit dem Spaltennamen.|
|2|Datenzeilen|Die Anzahl der Datenzeilen.|
|3|groupByColumnIndex|Der Spaltenindex der zu gruppierenden Spalte.|
|4|subtotalFunction|Die Aufzählung des Typs der Zwischensummenfunktion.|
|5|subtotalColumnIndexList|Die Spaltenindizes, für die Zwischensummen gebildet werden sollen.|
### **Liste der zusammenfassenden Funktionen**
Es gibt mehrere Arten von Zusammenfassungsfunktionen, die von der Enumeration {[SubtotalFunction}} unterstützt werden:

|**Nein.**|**Funktionsname**|**Beschreibung**|
|:- |:- |:- |
|1|DURCHSCHNITT|Berechnet den Durchschnitt der Werte.|
|2|ZÄHLEN|Zählt die numerischen Werte in den Zellen.|
|3|GRAF|Zählt die nicht numerischen Daten in den Zellen.|
|4|max|Berechnet den größten Wert.|
|5|MINDEST|Berechnet den kleinsten Wert.|
|6|PRODUKT|Berechnet das Produkt der Werte.|
|7|SUMME|Berechnet die Summe der Werte.|
Im folgenden Beispiel werden die Zwischensummen generiert, die die nicht numerischen Werte berechnen, die nach der zweiten Spalte im Arbeitsblatt gruppiert sind.

**Zwischensummen** 

![todo: Bild_alt_Text](group-rows-and-create-subtotal_3.png)



{{< highlight "java" >}}

 sheet.CreateSubtotal(0, sheet.Cells.MaxRow, 1, SubtotalFunction.COUNTA, new int[]{ 1, 2, 3, 4, 5 });

{{< /highlight >}}
## **Zwischensumme entfernen**
Um eine Zwischensumme zu entfernen, verwenden Sie die WebWorksheet.RemoveSubtotal-Methode. Im folgenden Beispiel werden die Zwischensummen entfernt.



{{< highlight "java" >}}

 // Accessing the reference of the worksheet that is currently active

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

//Remove the subtotals

sheet.RemoveSubtotal();

{{< /highlight >}}
## **Über die SUBTOTAL-Funktion**
Das GridWeb-Steuerelement verwendet die Formelfunktion SUBTOTAL, um den Zwischensummenwert zu berechnen.

Syntax: ZWISCHENSUMME(funktion_num, ref1, ref2, ...)

function_num ist eine Zahl, die den Typ der Funktion angibt, die bei der Zwischensummenberechnung verwendet wird.

|**1**|**DURCHSCHNITT**|
|:- |:- |
|2|ZÄHLEN|
|3|GRAF|
|4|max|
|5|MINDEST|
|6|PRODUKT|
|7|SUMME|
ref1, ref2 sind die zu subsumierenden Bereiche. Wenn ref1, ref2, ... andere Zwischensummenfunktionen enthalten, werden die referenzierten Zellen ignoriert, um eine doppelte Berechnung zu vermeiden.
