---
title: Arbeiten mit Zeilen und Spalten GridWeb
type: docs
weight: 20
url: /de/java/working-with-rows-and-columns-gridweb/
---
##  **Einfügen von Zeilen und Spalten**
In diesem Thema wird erläutert, wie Sie mit Aspose.Cells.GridWeb API neue Zeilen und Spalten in ein Arbeitsblatt einfügen. Zeilen oder Spalten können an jeder Position im Arbeitsblatt eingefügt werden.
###  **Zeilen einfügen**
So fügen Sie eine Zeile an einer beliebigen Position in einem Arbeitsblatt ein:

1. Fügen Sie das Aspose.Cells.GridWeb-Steuerelement zum Webformular oder zur Seite hinzu.
1. Greifen Sie auf das Arbeitsblatt zu, dem Sie Zeilen hinzufügen.
1. Fügen Sie eine Zeile ein, indem Sie einen Zeilenindex angeben, an der die Zeile eingefügt werden soll.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingRows-InsertingRows.jsp" >}}
###  **Spalten einfügen**
So fügen Sie eine Spalte an einer beliebigen Position in einem Arbeitsblatt ein:

1. Fügen Sie das Aspose.Cells.GridWeb-Steuerelement zu einem Webformular oder einer Webseite hinzu.
1. Greifen Sie auf das Arbeitsblatt zu, dem Sie Spalten hinzufügen.
1. Fügen Sie eine Spalte ein, indem Sie den Spaltenindex angeben, an dem die Spalte eingefügt werden soll.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingColumns-InsertingColumns.jsp" >}}

{{% alert color="primary" %}} 

Sie können auch die Methoden insertRows()/insertColumns() verwenden, um entsprechend mehrere Zeilen/Spalten in die Arbeitsblätter einzufügen.

{{% /alert %}} 
##  **Zeilen und Spalten löschen**
In diesem Thema wird gezeigt, wie Sie mithilfe von Aspose.Cells.GridWeb API Zeilen und Spalten aus einem Arbeitsblatt löschen. Mithilfe dieser Funktion können Entwickler Zeilen oder Spalten zur Laufzeit löschen.
###  **Zeilen löschen**
So löschen Sie eine Zeile aus Ihrem Arbeitsblatt:

1. Fügen Sie das Aspose.Cells.GridWeb-Steuerelement zu einem Webformular oder einer Webseite hinzu.
1. Greifen Sie auf das Arbeitsblatt zu, aus dem Sie Zeilen löschen möchten.
1. Löschen Sie eine Zeile aus dem Arbeitsblatt, indem Sie ihren Zeilenindex angeben.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingRows-DeletingRows.jsp" >}}
###  **Spalten löschen**
So löschen Sie eine Spalte aus Ihrem Arbeitsblatt:

1. Fügen Sie das Aspose.Cells.GridWeb-Steuerelement zu einem Webformular oder einer Webseite hinzu.
1. Greifen Sie auf das Arbeitsblatt zu, aus dem Sie Spalten löschen möchten.
1. Löschen Sie eine Spalte aus dem Arbeitsblatt, indem Sie ihren Spaltenindex angeben.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingColumns-DeletingColumns.jsp" >}}
##  **Zeilenhöhe und Spaltenbreite festlegen**
Manchmal sind Zellwerte breiter als die Zelle, in der sie sich befinden, oder liegen auf mehreren Zeilen. Solche Werte sind für Benutzer nicht vollständig sichtbar, es sei denn, sie ändern die Höhe und Breite von Zeilen und Spalten. Aspose.Cells.GridWeb unterstützt die Einstellung von Zeilenhöhen und Spaltenbreiten vollständig. In diesem Thema werden diese Funktionen anhand von Beispielen ausführlich erläutert.
###  **Arbeiten mit Zeilenhöhen und Spaltenbreiten**
####  **Zeilenhöhe festlegen**
So legen Sie die Höhe einer Zeile fest:

1. Fügen Sie das Aspose.Cells.GridWeb-Steuerelement zu Ihrem Webformular/Ihrer Webformularseite hinzu.
1. Greifen Sie auf die GridCells-Sammlung des Arbeitsblatts zu.
1. Legen Sie die Höhe aller Zellen in einer beliebigen angegebenen Zeile fest.

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb akzeptiert Zeilenhöhen- und Spaltenbreitenmessungen in Punkt, Zoll, Pixel usw.

{{% /alert %}} 

**Ausgabe: Die Höhe der 1. Reihe wurde auf 50 Punkte eingestellt** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingRowHeight-SettingRowHeight.jsp" >}}
####  **Spaltenbreite festlegen**
So legen Sie die Breite einer Spalte fest:

1. Fügen Sie das Aspose.Cells.GridWeb-Steuerelement zu Ihrem Webformular/Ihrer Webformularseite hinzu.
1. Greifen Sie auf die GridCells-Sammlung des Arbeitsblatts zu.
1. Legen Sie die Breite aller Zellen in einer beliebigen angegebenen Spalte fest.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingColumnWidth-SettingColumnWidth.jsp" >}}
##  **Anpassen von Zeilen- und Spaltenüberschriften**
Wie Microsoft Excel verwendet auch Aspose.Cells.GridWeb Standardüberschriften oder -beschriftungen für Zeilen (Zahlen wie 1, 2, 3 usw.) und Spalten (alphabetisch wie A, B, C usw.). Aspose.Cells.GridWeb ermöglicht auch die Anpassung von Untertiteln. In diesem Thema wird das Anpassen von Zeilen- und Spaltenüberschriften zur Laufzeit mithilfe von Aspose.Cells.GridWeb API erläutert.
###  **Zeilenkopf anpassen**
So passen Sie die Kopfzeile oder Beschriftung einer Zeile an:

1. Fügen Sie das Aspose.Cells.GridWeb-Steuerelement zu einem Webformular/einer Webformularseite hinzu.
1. Greifen Sie auf das Arbeitsblatt in der GridWorksheetCollection zu.
1. Legen Sie die Beschriftung einer beliebigen angegebenen Zeile fest.

**Die Überschriften der Zeilen 1 und 2 wurden angepasst** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_2.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingRowHeader-CustomizingRowHeader.jsp" >}}
###  **Anpassen der Spaltenüberschrift**
So passen Sie die Kopfzeile oder Beschriftung einer Spalte an:

1. Fügen Sie das Aspose.Cells.GridWeb-Steuerelement zu einem Webformular/einer Webformularseite hinzu.
1. Greifen Sie auf das Arbeitsblatt in der GridWorksheetCollection zu.
1. Legen Sie die Beschriftung einer beliebigen angegebenen Spalte fest.

**Die Überschriften der Spalten 1 und 2 wurden angepasst** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_3.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingColumnHeader-CustomizingColumnHeader.jsp" >}}
##  **Einfrieren und Freigeben von Zeilen und Spalten**
In diesem Thema wird erläutert, wie Zeilen und Spalten eingefroren und freigegeben werden. Durch das Einfrieren von Spalten oder Zeilen können Benutzer die Spaltenüberschriften oder Zeilentitel sichtbar halten, während sie zu anderen Teilen des Arbeitsblatts scrollen. Diese Funktion ist sehr hilfreich, wenn Sie mit Arbeitsblättern arbeiten, die große Datenmengen enthalten. Wenn Benutzer scrollen, werden nur die Daten nach unten gescrollt und die Überschriften bleiben an Ort und Stelle, sodass das Datum besser lesbar ist. Die Funktion „Fenster einfrieren“ wird nur in Internet Explorer 6.0 oder höher unterstützt.
###  **Zeilen und Spalten einfrieren**
So frieren Sie eine bestimmte Anzahl von Zeilen und Spalten ein:

1. Fügen Sie das Aspose.Cells.GridWeb-Steuerelement zu einem Webformular/einer Webformularseite hinzu.
1. Greifen Sie auf ein Arbeitsblatt zu.
1. Frieren Sie eine Reihe von Zeilen und Spalten ein.

{{% alert color="primary" %}} 

 Es ist auch möglich, über die Schnittstelle eine bestimmte Anzahl von Zeilen und Spalten einzufrieren. Klicken Sie mit der rechten Maustaste auf eine Zelle, in der Sie Zeilen und Spalten einfrieren möchten, und wählen Sie sie aus**Einfrieren** von der Liste.

{{% /alert %}} 

**Zeilen und Spalten im eingefrorenen Zustand** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-FreezingRowsandColumns-FreezingRowsandColumns.jsp" >}}
###  **Freigeben von Zeilen und Spalten**
So entsperren Sie Zeilen und Spalten:

1. Fügen Sie das Aspose.Cells.GridWeb-Steuerelement zu einem Webformular/einer Webformularseite hinzu.
1. Greifen Sie auf ein Arbeitsblatt zu.
1. Freigeben von Zeilen und Spalten.

**Arbeitsblatt nach dem Auftauen** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-UnfreezingRowsandColumns-UnfreezingRowsandColumns.jsp" >}}
##  **Zeilen und Spalten schützen**
In diesem Thema werden einige Techniken zum Schutz von Zellen in Zeilen und Spalten vor Aktionen jeglicher Art durch Endbenutzer erläutert. Entwickler können diesen Schutz mit zwei Techniken implementieren: indem sie Zellen in Zeilen und Spalten schreibgeschützt machen oder indem sie die Kontextmenüoptionen von GridWeb einschränken.
###  **Einschränken der Kontextmenüoptionen**
GridWeb bietet ein Kontextmenü, mit dem Endbenutzer Vorgänge am Steuerelement ausführen können. Das Menü bietet viele Optionen zum Bearbeiten von Zellen, Zeilen und Spalten.

**Vollständige kontextbezogene Optionen** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_6.png)

Es ist möglich, jede Art von clientseitigen Vorgängen auf Zeilen und Spalten einzuschränken, indem die im Kontextmenü verfügbaren Optionen eingeschränkt werden. Dies kann erreicht werden, indem die Attribute „EnableClientColumnOperations“ und „EnableClientRowOperations“ des GridWeb-Steuerelements auf „false“ gesetzt werden. Es ist auch möglich, Benutzer daran zu hindern, Zeilen und Spalten einzufrieren, indem das EnableClientFreeze-Attribut des GridWeb-Steuerelements auf „false“ gesetzt wird.

**Kontextmenü nach Einschränkung der Zeilen- und Spaltenoptionen** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_7.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-ProtectingCellsinRowsandColumns-ProtectingCellsinRowsandColumns.jsp" >}}
