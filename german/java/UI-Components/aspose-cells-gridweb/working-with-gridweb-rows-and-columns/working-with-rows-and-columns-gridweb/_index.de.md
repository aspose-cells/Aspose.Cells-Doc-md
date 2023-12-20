---
title: Arbeiten mit Zeilen und Spalten GridWeb
type: docs
weight: 20
url: /de/java/working-with-rows-and-columns-gridweb/
---
## **Zeilen und Spalten einfügen**
In diesem Thema wird erläutert, wie Sie mithilfe von Aspose.Cells.GridWeb API neue Zeilen und Spalten in ein Arbeitsblatt einfügen. Zeilen oder Spalten können an jeder Position im Arbeitsblatt eingefügt werden.
### **Zeilen einfügen**
So fügen Sie eine Zeile an einer beliebigen Position in einem Arbeitsblatt ein:

1. Fügen Sie dem Webformular oder der Seite das Steuerelement Aspose.Cells.GridWeb hinzu.
1. Greifen Sie auf das Arbeitsblatt zu, dem Sie Zeilen hinzufügen.
1. Fügen Sie eine Zeile ein, indem Sie einen Zeilenindex angeben, an dem die Zeile eingefügt werden soll.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingRows-InsertingRows.jsp" >}}
### **Spalten einfügen**
So fügen Sie eine Spalte an einer beliebigen Position in einem Arbeitsblatt ein:

1. Fügen Sie das Steuerelement Aspose.Cells.GridWeb einem Webformular oder einer Seite hinzu.
1. Greifen Sie auf das Arbeitsblatt zu, dem Sie Spalten hinzufügen.
1. Fügen Sie eine Spalte ein, indem Sie den Spaltenindex angeben, an dem die Spalte eingefügt werden soll.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingColumns-InsertingColumns.jsp" >}}

{{% alert color="primary" %}} 

Sie können auch die Methoden insertRows()/insertColumns() verwenden, um entsprechend mehrere Zeilen/Spalten in die Arbeitsblätter einzufügen.

{{% /alert %}} 
## **Löschen von Zeilen und Spalten**
Dieses Thema zeigt, wie Zeilen und Spalten aus einem Arbeitsblatt mit Aspose.Cells.GridWeb API gelöscht werden. Mithilfe dieser Funktion können Entwickler Zeilen oder Spalten zur Laufzeit löschen.
### **Zeilen löschen**
So löschen Sie eine Zeile aus Ihrem Arbeitsblatt:

1. Fügen Sie das Steuerelement Aspose.Cells.GridWeb einem Webformular oder einer Seite hinzu.
1. Greifen Sie auf das Arbeitsblatt zu, aus dem Sie Zeilen löschen möchten.
1. Löschen Sie eine Zeile aus dem Arbeitsblatt, indem Sie ihren Zeilenindex angeben.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingRows-DeletingRows.jsp" >}}
### **Spalten löschen**
So löschen Sie eine Spalte aus Ihrem Arbeitsblatt:

1. Fügen Sie das Steuerelement Aspose.Cells.GridWeb einem Webformular oder einer Seite hinzu.
1. Greifen Sie auf das Arbeitsblatt zu, aus dem Sie Spalten löschen möchten.
1. Löschen Sie eine Spalte aus dem Arbeitsblatt, indem Sie ihren Spaltenindex angeben.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingColumns-DeletingColumns.jsp" >}}
## **Zeilenhöhe und Spaltenbreite einstellen**
Manchmal sind Zellenwerte breiter als die Zelle, in der sie sich befinden, oder befinden sich in mehreren Zeilen. Solche Werte sind für Benutzer nicht vollständig sichtbar, es sei denn, sie ändern die Höhe und Breite von Zeilen und Spalten. Aspose.Cells. GridWeb unterstützt die Einstellung von Zeilenhöhen und Spaltenbreiten vollständig. In diesem Thema werden diese Features ausführlich anhand von Beispielen erläutert.
### **Arbeiten mit Zeilenhöhen und Spaltenbreiten**
#### **Zeilenhöhe einstellen**
So legen Sie die Höhe einer Zeile fest:

1. Fügen Sie das Aspose.Cells.GridWeb-Steuerelement zu Ihrer Web Form/-Seite hinzu.
1. Greifen Sie auf die GridCells-Auflistung des Arbeitsblatts zu.
1. Legen Sie die Höhe aller Zellen in einer beliebigen angegebenen Zeile fest.

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb akzeptiert Zeilenhöhen- und Spaltenbreitenmessungen in Punkt, Zoll, Pixel usw.

{{% /alert %}} 

**Ausgabe: Die Höhe der 1. Reihe wurde auf 50 Punkte gesetzt** 

![todo: Bild_alt_Text](working-with-rows-and-columns-gridweb_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingRowHeight-SettingRowHeight.jsp" >}}
#### **Spaltenbreite einstellen**
So legen Sie die Breite einer Spalte fest:

1. Fügen Sie das Aspose.Cells.GridWeb-Steuerelement zu Ihrer Web Form/-Seite hinzu.
1. Greifen Sie auf die GridCells-Auflistung des Arbeitsblatts zu.
1. Legen Sie die Breite aller Zellen in einer beliebigen angegebenen Spalte fest.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingColumnWidth-SettingColumnWidth.jsp" >}}
## **Anpassen von Zeilen- und Spaltenüberschriften**
Wie Microsoft Excel verwendet auch Aspose.Cells.GridWeb Standardüberschriften oder Beschriftungen für Zeilen (Zahlen wie 1, 2, 3 usw.) und Spalten (alphabetisch wie A, B, C usw.). Aspose.Cells.GridWeb macht es auch möglich, Beschriftungen anzupassen. In diesem Thema wird das Anpassen von Zeilen- und Spaltenüberschriften zur Laufzeit mit Aspose.Cells.GridWeb API erläutert.
### **Zeilenkopf anpassen**
So passen Sie die Kopfzeile oder Beschriftung einer Zeile an:

1. Fügen Sie das Aspose.Cells.GridWeb-Steuerelement zu einer Web Form/-Seite hinzu.
1. Greifen Sie auf das Arbeitsblatt in der GridWorksheetCollection zu.
1. Legen Sie die Beschriftung einer beliebigen angegebenen Zeile fest.

**Die Überschriften der Zeilen 1 und 2 wurden angepasst** 

![todo: Bild_alt_Text](working-with-rows-and-columns-gridweb_2.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingRowHeader-CustomizingRowHeader.jsp" >}}
### **Anpassen der Spaltenüberschrift**
So passen Sie die Kopfzeile oder Beschriftung einer Spalte an:

1. Fügen Sie das Aspose.Cells.GridWeb-Steuerelement zu einer Web Form/-Seite hinzu.
1. Greifen Sie auf das Arbeitsblatt in der GridWorksheetCollection zu.
1. Legen Sie die Überschrift einer beliebigen angegebenen Spalte fest.

**Die Überschriften der Spalten 1 und 2 wurden angepasst** 

![todo: Bild_alt_Text](working-with-rows-and-columns-gridweb_3.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingColumnHeader-CustomizingColumnHeader.jsp" >}}
## **Einfrieren und Freigeben von Zeilen und Spalten**
In diesem Thema wird erläutert, wie Sie Zeilen und Spalten einfrieren und die Fixierung aufheben. Durch das Einfrieren von Spalten oder Zeilen können Benutzer die Spaltenüberschriften oder Zeilentitel sichtbar lassen, während sie zu anderen Teilen des Arbeitsblatts scrollen. Diese Funktion ist sehr hilfreich, wenn Sie mit Arbeitsblättern arbeiten, die große Datenmengen enthalten. Wenn Benutzer scrollen, werden nur die Daten nach unten gescrollt und die Überschriften bleiben an Ort und Stelle, wodurch das Datum leichter lesbar wird. Die Funktion zum Einfrieren von Fenstern wird nur in Internet Explorer 6.0 oder höher unterstützt.
### **Einfrieren von Zeilen und Spalten**
So frieren Sie eine bestimmte Anzahl von Zeilen und Spalten ein:

1. Fügen Sie das Aspose.Cells.GridWeb-Steuerelement zu einer Web Form/-Seite hinzu.
1. Greifen Sie auf ein Arbeitsblatt zu.
1. Frieren Sie eine Reihe von Zeilen und Spalten ein.

{{% alert color="primary" %}} 

 Es ist auch möglich, eine bestimmte Anzahl von Zeilen und Spalten über die Schnittstelle einzufrieren. Klicken Sie mit der rechten Maustaste auf eine Zelle, in der Sie Zeilen und Spalten einfrieren möchten, und wählen Sie sie aus**Einfrieren** von der Liste.

{{% /alert %}} 

**Zeilen und Spalten in eingefrorenem Zustand** 

![todo: Bild_alt_Text](working-with-rows-and-columns-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-FreezingRowsandColumns-FreezingRowsandColumns.jsp" >}}
### **Auftauen von Zeilen und Spalten**
So heben Sie die Fixierung von Zeilen und Spalten auf:

1. Fügen Sie das Aspose.Cells.GridWeb-Steuerelement zu einer Web Form/-Seite hinzu.
1. Greifen Sie auf ein Arbeitsblatt zu.
1. Entsperren Sie Zeilen und Spalten.

**Arbeitsblatt nach dem Auftauen** 

![todo: Bild_alt_Text](working-with-rows-and-columns-gridweb_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-UnfreezingRowsandColumns-UnfreezingRowsandColumns.jsp" >}}
## **Zeilen und Spalten schützen**
In diesem Thema werden einige Techniken zum Schützen von Zellen in Zeilen und Spalten vor jeder Art von Aktion erläutert, die von Endbenutzern ausgeführt wird. Entwickler können diesen Schutz mit zwei Techniken implementieren: indem sie Zellen in Zeilen und Spalten schreibgeschützt machen oder indem sie die Kontextmenüoptionen von GridWeb einschränken.
### **Einschränken der Kontextmenüoptionen**
GridWeb bietet ein Kontextmenü, das Endbenutzer verwenden können, um Operationen auf dem Steuerelement auszuführen. Das Menü bietet viele Optionen zum Bearbeiten von Zellen, Zeilen und Spalten.

**Vollständige kontextbezogene Optionen** 

![todo: Bild_alt_Text](working-with-rows-and-columns-gridweb_6.png)

Es ist möglich, jede Art von clientseitigen Operationen auf Zeilen und Spalten einzuschränken, indem Sie die im Kontextmenü verfügbaren Optionen einschränken. Dies kann erreicht werden, indem die Attribute EnableClientColumnOperations und EnableClientRowOperations des GridWeb-Steuerelements auf „false“ festgelegt werden. Es ist auch möglich, Benutzer daran zu hindern, Zeilen und Spalten einzufrieren, indem Sie das EnableClientFreeze-Attribut des GridWeb-Steuerelements auf „false“ festlegen.

**Kontextmenü nach dem Einschränken der Zeilen- und Spaltenoptionen** 

![todo: Bild_alt_Text](working-with-rows-and-columns-gridweb_7.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-ProtectingCellsinRowsandColumns-ProtectingCellsinRowsandColumns.jsp" >}}
