---
title: Arbeiten mit Zeilen und Spalten in GridWeb
type: docs
weight: 20
url: /de/java/working-with-rows-and-columns-gridweb/
---

## **Einfügen von Zeilen und Spalten**
Dieser Abschnitt erläutert, wie Sie neue Zeilen und Spalten in ein Arbeitsblatt einfügen können, indem Sie die Aspose.Cells.GridWeb-API verwenden. Zeilen oder Spalten können an beliebiger Stelle im Arbeitsblatt eingefügt werden.
### **Einfügen von Zeilen**
Um eine Zeile an beliebiger Stelle in einem Arbeitsblatt einzufügen:

1. Fügen Sie die Aspose.Cells.GridWeb-Steuerung dem Web-Formular oder der Seite hinzu.
1. Greifen Sie auf das Arbeitsblatt zu, in das Sie Zeilen hinzufügen.
1. Fügen Sie eine Zeile ein, indem Sie einen Zeilenindex angeben, an dem die Zeile eingefügt werden soll.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingRows-InsertingRows.jsp" >}}
### **Einfügen von Spalten**
Um eine Spalte an beliebiger Stelle in einem Arbeitsblatt einzufügen:

1. Fügen Sie der Webform oder Seite die Aspose.Cells.GridWeb-Kontrolle hinzu.
1. Greifen Sie auf das Arbeitsblatt zu, in das Sie Spalten hinzufügen.
1. Fügen Sie eine Spalte ein, indem Sie einen Spaltenindex angeben, an dem die Spalte eingefügt werden soll.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-InsertingColumns-InsertingColumns.jsp" >}}

{{% alert color="primary" %}} 

Sie können auch die Methoden insertRows() / insertColumns() verwenden, um entsprechend mehrere Zeilen / Spalten in die Arbeitsblätter einzufügen.

{{% /alert %}} 
## **Zeilen und Spalten löschen**
Dieses Thema zeigt, wie man Zeilen und Spalten aus einem Arbeitsblatt mithilfe der Aspose.Cells.GridWeb-API löscht. Mit dieser Funktion können Entwickler Zeilen oder Spalten zur Laufzeit löschen.
### **Zeilen löschen**
Um eine Zeile aus Ihrem Arbeitsblatt zu löschen:

1. Fügen Sie der Webform oder Seite die Aspose.Cells.GridWeb-Kontrolle hinzu.
1. Greifen Sie auf das Arbeitsblatt zu, aus dem Sie Zeilen löschen möchten.
1. Löschen Sie eine Zeile aus dem Arbeitsblatt, indem Sie ihren Zeilenindex angeben.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingRows-DeletingRows.jsp" >}}
### **Spalten löschen**
Um eine Spalte aus Ihrem Arbeitsblatt zu löschen:

1. Fügen Sie der Webform oder Seite die Aspose.Cells.GridWeb-Kontrolle hinzu.
1. Greifen Sie auf das Arbeitsblatt zu, aus dem Sie Spalten löschen möchten.
1. Löschen Sie eine Spalte aus dem Arbeitsblatt, indem Sie ihren Spaltenindex angeben.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-DeletingColumns-DeletingColumns.jsp" >}}
## **Zeilenhöhe und Spaltenbreite festlegen**
Manchmal sind Zellenwerte breiter als die Zelle, in der sie sich befinden, oder sie erstrecken sich über mehrere Zeilen. Solche Werte sind für Benutzer nicht vollständig sichtbar, es sei denn, sie ändern die Höhe und Breite von Zeilen und Spalten. Aspose.Cells.GridWeb unterstützt vollständig das Festlegen von Zeilenhöhen und Spaltenbreiten. Dieses Thema erörtert diese Funktionen im Detail anhand von Beispielen.
### **Arbeiten mit Zeilenhöhen und Spaltenbreiten**
#### **Zeilenhöhe festlegen**
Um die Höhe einer Zeile festzulegen:

1. Fügen Sie der Web-Formular/Seite die Aspose.Cells.GridWeb-Steuerung hinzu.
1. Greifen Sie auf die GridCells-Sammlung des Arbeitsblatts zu.
1. Legen Sie die Höhe aller Zellen in einer bestimmten Zeile fest.

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb akzeptiert Maßeinheiten wie Punkte, Zoll, Pixel usw. für Zeilenhöhen und Spaltenbreiten.

{{% /alert %}} 

**Ausgabe: Die Höhe der 1. Zeile wurde auf 50 Punkte festgelegt** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingRowHeight-SettingRowHeight.jsp" >}}
#### **Spaltenbreite festlegen**
Um die Breite einer Spalte festzulegen:

1. Fügen Sie der Web-Formular/Seite die Aspose.Cells.GridWeb-Steuerung hinzu.
1. Greifen Sie auf die GridCells-Sammlung des Arbeitsblatts zu.
1. Legen Sie die Breite aller Zellen in einer bestimmten Spalte fest.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-SettingColumnWidth-SettingColumnWidth.jsp" >}}
## **Anpassen von Zeilen- und Spaltenüberschriften**
Wie Microsoft Excel verwendet auch Aspose.Cells.GridWeb standardmäßige Überschriften oder Beschriftungen für Zeilen (Nummern wie 1, 2, 3 usw.) und Spalten (alphabetisch wie A, B, C usw.). Mit Aspose.Cells.GridWeb ist es auch möglich, Beschriftungen anzupassen. Dieses Thema behandelt die Anpassung von Zeilen- und Spaltenüberschriften zur Laufzeit mithilfe der Aspose.Cells.GridWeb-API.
### **Anpassen der Zeilenüberschrift**
Um die Überschrift oder Beschriftung einer Zeile anzupassen:

1. Fügen Sie der Webformular-/Seite das Aspose.Cells.GridWeb-Control hinzu.
1. Greifen Sie auf das Arbeitsblatt in der GridWorksheetCollection zu.
1. Legen Sie die Beschriftung einer bestimmten Zeile fest.

**Die Überschriften der Zeile 1 und 2 wurden angepasst** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_2.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingRowHeader-CustomizingRowHeader.jsp" >}}
### **Anpassen der Spaltenüberschrift**
Um die Überschrift oder Beschriftung einer Spalte anzupassen:

1. Fügen Sie der Webformular-/Seite das Aspose.Cells.GridWeb-Control hinzu.
1. Greifen Sie auf das Arbeitsblatt in der GridWorksheetCollection zu.
1. Legen Sie die Beschriftung einer bestimmten Spalte fest.

**Die Überschriften der Spalte 1 und 2 wurden angepasst** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_3.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-CustomizingColumnHeader-CustomizingColumnHeader.jsp" >}}
## **Zeilen und Spalten einfrieren und auftauen**
Dieses Thema erläutert, wie Sie Zeilen und Spalten einfrieren und auftauen können. Durch das Einfrieren von Spalten oder Zeilen können Benutzer die Spaltenüberschriften oder Zeilentitel sichtbar halten, während sie zu anderen Teilen des Arbeitsblatts scrollen. Diese Funktion ist sehr hilfreich, wenn mit Arbeitsblättern gearbeitet wird, die große Datenmengen enthalten. Wenn Benutzer scrollen, werden nur Daten heruntergescrollt und die Überschriften bleiben an Ort und Stelle, wodurch die Daten einfacher zu lesen sind. Die Funktion zum Einfrieren von Bereichen wird nur in Internet Explorer 6.0 oder höher unterstützt.
### **Zeilen und Spalten einfrieren**
Um eine bestimmte Anzahl von Zeilen und Spalten einzufrieren:

1. Fügen Sie der Webformular-/Seite das Aspose.Cells.GridWeb-Control hinzu.
1. Greifen Sie auf ein Arbeitsblatt zu.
1. Einfrieren einer bestimmten Anzahl von Zeilen & Spalten.

{{% alert color="primary" %}} 

Es ist auch möglich, eine bestimmte Anzahl von Zeilen und Spalten über die Benutzeroberfläche einzufrieren. Klicken Sie mit der rechten Maustaste auf eine Zelle, an der Sie Zeilen & Spalten einfrieren möchten, und wählen Sie **Einfrieren** aus der Liste.

{{% /alert %}} 

**Zeilen & Spalten im eingefrorenen Zustand** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-FreezingRowsandColumns-FreezingRowsandColumns.jsp" >}}
### **Zeilen und Spalten auftauen**
Um Zeilen und Spalten aufzutauen:

1. Fügen Sie der Webformular-/Seite das Aspose.Cells.GridWeb-Control hinzu.
1. Greifen Sie auf ein Arbeitsblatt zu.
1. Zeilen & Spalten auftauen.

**Arbeitsblatt nach dem Auftauen** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-UnfreezingRowsandColumns-UnfreezingRowsandColumns.jsp" >}}
## **Schutz von Zeilen und Spalten**
In diesem Thema werden einige Techniken zum Schutz von Zellen in Zeilen und Spalten vor jeglicher Aktion durch Endbenutzer erläutert. Entwickler können diesen Schutz mit zwei Techniken umsetzen: durch das Festlegen von Zellen in Zeilen und Spalten als schreibgeschützt oder durch die Einschränkung der Kontextmenüoptionen des GridWeb.
### **Einschränkung von Kontextmenüoptionen**
GridWeb bietet ein Kontextmenü, das Endbenutzer zur Durchführung von Operationen an der Steuerelement verwenden können. Das Menü bietet viele Optionen zur Manipulation von Zellen, Zeilen und Spalten.

**Vollständige Kontextmenüoptionen** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_6.png)

Es ist möglich, jegliche Art von Client-seitigen Operationen in Zeilen und Spalten zu beschränken, indem die verfügbaren Optionen im Kontextmenü eingeschränkt werden. Dies kann durch Festlegen der Attribute EnableClientColumnOperations und EnableClientRowOperations des GridWeb-Steuerelements auf false erfolgen. Es ist auch möglich, Benutzer daran zu hindern, Zeilen und Spalten einzufrieren, indem das Attribut EnableClientFreeze des GridWeb-Steuerelements auf false gesetzt wird.

**Kontextmenü nach Beschränkung der Zeilen- & Spaltenoptionen** 

![todo:image_alt_text](working-with-rows-and-columns-gridweb_7.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-rowsandcolumns-ProtectingCellsinRowsandColumns-ProtectingCellsinRowsandColumns.jsp" >}}
