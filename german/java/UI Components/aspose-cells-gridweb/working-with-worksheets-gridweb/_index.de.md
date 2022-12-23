---
title: Arbeiten mit Arbeitsblättern GridWeb
type: docs
weight: 30
url: /de/java/working-with-worksheets-gridweb/
---
## **Zugriff auf Arbeitsblätter**

In diesem Thema wird der Zugriff auf Arbeitsblätter des GridWeb-Steuerelements erläutert. Wir können diese Arbeitsblätter auch als Webarbeitsblätter bezeichnen, da sie zu GridWeb gehören und in Webanwendungen verwendet werden.

Alle im GridWeb-Steuerelement enthaltenen Arbeitsblätter werden in einer GridWorksheetCollection des GridWeb-Steuerelements gespeichert. Auf ein bestimmtes Arbeitsblatt kann einfach über seinen Blattindex zugegriffen werden.

Entwickler können auf ein bestimmtes Arbeitsblatt zugreifen, indem sie seinen Blattindex angeben, wie unten im Beispielcodeausschnitt gezeigt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingWorksheet-AccessingWorksheet.jsp" >}}

## **Entfernen eines Arbeitsblatts**

Dieses Thema enthält kurze Informationen zum Entfernen von Arbeitsblättern aus Microsoft Excel-Dateien mithilfe von GridWeb API. Entfernen Sie ein Arbeitsblatt, indem Sie seinen Blattindex angeben.

Entwickler können ein bestimmtes Arbeitsblatt entfernen, indem sie seinen Blattindex mithilfe der Methode removeAt der GridWorksheetCollection-Sammlung angeben, wie unten im Beispielcodeausschnitt gezeigt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingWorksheet-RemovingWorksheet.jsp" >}}

## **Arbeitsblätter hinzufügen**

Arbeitsblätter sind ein integraler Bestandteil von GridWeb. Alle Daten werden in Form von Arbeitsblättern verwaltet und gespeichert. GridWeb ermöglicht es Entwicklern, dem Aspose.Cells.GridWeb-Steuerelement ein oder mehrere Arbeitsblätter hinzuzufügen. Dieses Thema zeigt einfache Ansätze zum Hinzufügen von Arbeitsblättern zu GridWeb.

### **Ohne Angabe des Blattnamens**

Die einfachste Methode zum Hinzufügen eines Arbeitsblatts zu Aspose.Cells.GridWeb besteht darin, die add-Methode der GridWorksheetCollection-Klasse im GridWeb-Steuerelement aufzurufen. Dadurch werden Arbeitsblätter erstellt, die Standardnamen verwenden (dh Sheet1, Sheet2, Sheet3 usw.) und dem GridWeb-Steuerelement hinzugefügt.

**Ausgabe: GridWeb wurde ein Arbeitsblatt mit Standardnamen hinzugefügt** 

![todo: Bild_alt_Text](working-with-worksheets-gridweb_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithoutSpecificName-AddingWorksheetWithoutSpecificName.jsp" >}}

### **Mit angegebenem Blattnamen**

Um dem GridWeb-Steuerelement ein Arbeitsblatt mit einem bestimmten Namen hinzuzufügen, anstatt das standardmäßige Benennungsschema zu verwenden, rufen Sie eine überladene Version der add-Methode auf, die die angegebene Zeichenfolge SheetName annimmt. Im folgenden Beispiel wird beispielsweise ein Arbeitsblatt mit dem Namen „Rechnung“ hinzugefügt.

**Ausgabe: GridWeb wurde ein Arbeitsblatt mit einem bestimmten Namen hinzugefügt** 

![todo: Bild_alt_Text](working-with-worksheets-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithSpecificName-AddingWorksheetWithSpecificName.jsp" >}}

{{% alert color="primary" %}}

 Die Methode add() gibt den Index des neuen Arbeitsblatts zurück, der verwendet werden kann, um auf die Instanz dieses Arbeitsblatts zuzugreifen. Weitere Informationen zum Zugriff auf Arbeitsblätter finden Sie unter[Zugriff auf Arbeitsblätter](/cells/de/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

## **Umbenennen eines Arbeitsblatts**

Das Umbenennen eines Arbeitsblatts kann sehr nützlich sein, wenn Sie mit vielen Arbeitsblättern in GridWeb arbeiten und sich entscheiden, ihre Namen zu ändern, um sie aussagekräftiger zu machen. Beispielsweise kann ein Arbeitsblatt, das eine Rechnung enthält, in Rechnung statt in Blatt1 umbenannt werden. In diesem Thema wird diese einfache, aber nützliche Funktion beschrieben.

### **Umbenennen eines Arbeitsblatts**

Alle Arbeitsblätter enthalten eine Name-Eigenschaft, mit der Entwickler auf die Namen von Arbeitsblättern zugreifen oder diese ändern können. So benennen Sie ein Arbeitsblatt um:

1. Greifen Sie auf ein Arbeitsblatt aus der GridWorksheetCollection zu.
1. Benennen Sie das ausgewählte Arbeitsblatt um.

{{% alert color="primary" %}}

 Weitere Einzelheiten zum Zugriff auf Arbeitsblätter in Aspose.Cells.GridWeb finden Sie unter[Zugriff auf Arbeitsblätter](/cells/de/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

Vor dem Ausführen des Codes hat das Arbeitsblatt einen Standardnamen, z. B. Sheet1.

**Eingabedatei: ein Arbeitsblatt mit dem Standardnamen Sheet1** 

![todo: Bild_alt_Text](working-with-worksheets-gridweb_3.png)

Nach dem Ausführen des Codes wird das Arbeitsblatt in Invoice umbenannt.

**Ausgabe: Das Arbeitsblatt wird in Rechnung umbenannt** 

![todo: Bild_alt_Text](working-with-worksheets-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RenamingWorksheet-RenamingWorksheet.jsp" >}}

## **Kopieren eines Arbeitsblatts**

[Arbeitsblätter hinzufügen](/cells/de/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-addingworksheets)beschreibt, wie man GridWeb neue Arbeitsblätter hinzufügt. Es ist auch möglich, dem Aspose.Cells.GridWeb-Steuerelement eine Kopie (oder ein Replikat) eines anderen Arbeitsblatts hinzuzufügen. Diese Funktion kann nützlich sein, wenn identische oder ähnliche Daten in einem Arbeitsblatt auch in einem anderen Arbeitsblatt benötigt werden. In diesem Fall ist es einfacher, ein vorhandenes Arbeitsblatt zu kopieren und es als neues Arbeitsblatt zu Aspose.Cells.GridWeb hinzuzufügen, anstatt es von Grund auf neu zu erstellen.

### **Blattindex verwenden**

Der folgende Beispielcode zeigt, wie dem GridWeb-Steuerelement eine Kopie eines Arbeitsblatts hinzugefügt wird, indem der Index des Arbeitsblatts in der addCopy-Methode der GridWorksheetCollection angegeben wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetIndex-CopyWorksheetUsingSheetIndex.jsp" >}}
### **Blattname verwenden**
Der folgende Beispielcode zeigt, wie dem GridWeb-Steuerelement eine Kopie eines Arbeitsblatts hinzugefügt wird, indem der Name des Arbeitsblatts in der addCopy-Methode der GridWorksheetCollection angegeben wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetName-CopyWorksheetUsingSheetName.jsp" >}}

{{% alert color="primary" %}}

 Die Methode addCopy gibt den Index des neu hinzugefügten Arbeitsblatts zurück, der für den Zugriff auf die Arbeitsblattinstanz verwendet werden kann. Weitere Informationen zum Zugriff auf Arbeitsblätter finden Sie unter[Zugriff auf Arbeitsblätter](/cells/de/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

## **Arbeiten mit benannten Bereichen**

Normalerweise werden Spalten- und Zeilenbeschriftungen verwendet, um eindeutig auf Zellen zu verweisen. Sie können jedoch aussagekräftige Namen erstellen, um Zellen, Zellbereiche, Formeln oder konstante Werte darzustellen.

 Das Wort**Name** kann sich auf eine Zeichenfolge beziehen, die eine Zelle, einen Zellbereich, eine Formel oder einen konstanten Wert darstellt. Verwenden Sie beispielsweise leicht verständliche Namen wie Produkte, um auf schwer verständliche Bereiche wie Sales!C20:C30 zu verweisen.

 Beschriftungen können in Formeln verwendet werden, die auf Daten auf demselben Arbeitsblatt verweisen; Wenn Sie einen Bereich auf einem anderen Arbeitsblatt darstellen möchten, können Sie einen Namen verwenden.**Benannte Bereiche** ist eine der leistungsstärksten Funktionen von Microsoft Excel.

Benutzer können einem Bereich einen Namen zuweisen und diesen Namen in Formeln verwenden. Aspose.Cells.GridWeb unterstützt diese Funktion.

### **Benannte Bereiche in Formeln hinzufügen/referenzieren**

Das GridWeb-Steuerelement stellt zwei Klassen (GridName und GridNameCollection) zum Arbeiten mit benannten Bereichen bereit.

Das folgende Code-Snippet hilft Ihnen zu verstehen, wie Sie sie verwenden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingNamedRangesinFormulas-AddingNamedRangesinFormulas.jsp" >}}

## **Verwalten von Kommentaren im Arbeitsblatt**

In diesem Thema wird das Hinzufügen von, Zugreifen auf und Entfernen von Kommentaren aus Arbeitsblättern erläutert. Kommentare sind nützlich, um Notizen oder nützliche Informationen für Benutzer hinzuzufügen, die mit dem Blatt arbeiten werden. Entwickler haben die Flexibilität, jeder Zelle des Arbeitsblatts Kommentare hinzuzufügen.

### **Arbeiten mit Kommentaren**

#### **Kommentare hinzufügen**

Um einen Kommentar zum Arbeitsblatt hinzuzufügen, führen Sie bitte die folgenden Schritte aus:

1. Fügen Sie dem Webformular das Steuerelement Aspose.Cells.GridWeb hinzu.
1. Greifen Sie auf das Arbeitsblatt zu, dem Sie Kommentare hinzufügen.
1. Fügen Sie einer Zelle einen Kommentar hinzu.
1. Legen Sie eine Notiz für den neuen Kommentar fest.

**Dem Arbeitsblatt wurde ein Kommentar hinzugefügt** 

![todo: Bild_alt_Text](working-with-worksheets-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingComments-AddingComments.jsp" >}}

#### **Zugriff auf Kommentare**

So greifen Sie auf einen Kommentar zu:

1. Greifen Sie auf die Zelle zu, die den Kommentar enthält.
1. Holen Sie sich die Referenz der Zelle.
1. Übergeben Sie den Verweis auf die Kommentarsammlung, um auf den Kommentar zuzugreifen.
1. Es ist jetzt möglich, die Eigenschaften des Kommentars zu ändern.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingComments-AccessingComments.jsp" >}}

#### **Kommentare entfernen**

So entfernen Sie einen Kommentar:

1. Greifen Sie wie oben beschrieben auf die Zelle zu.
1. Verwenden Sie die removeAt-Methode der Comment-Auflistung, um den Kommentar zu entfernen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingComments-RemovingComments.jsp" >}}

## **Verwalten von Hyperlinks im Arbeitsblatt**

In diesem Thema wird erläutert, welche Arten von Hyperlinks in Aspose.Cells.GridWeb unterstützt werden und wie sie programmgesteuert verwaltet werden. Hyperlinks können entweder zum Erstellen von Links zu Web-URLs oder zum Durchführen von Postbacks zu einem Server verwendet werden.

### **Arten von Hyperlinks**

Die folgenden Hyperlinks werden von Aspose.Cells.GridWeb unterstützt:

- Text-URL-Hyperlinks, auf den Text angewendete URL-Hyperlinks.
- Bild-URL-Hyperlinks, auf Bilder angewendete URL-Hyperlinks.

#### **Text-URL-Hyperlinks**

 Im folgenden Beispiel werden einem Arbeitsblatt zwei Hyperlinks hinzugefügt. Man hat eine_ leeres Ziel, während das andere auf gesetzt ist_Elternteil.

![todo: Bild_alt_Text](working-with-worksheets-gridweb_6.png)

**Ausgabe: Text-Hyperlinks, die dem Arbeitsblatt hinzugefügt wurden**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-TextURLHyperlinks-TextURLHyperlinks.jsp" >}}

#### **Bild-URL-Hyperlinks**

Im folgenden Beispiel wird einem Arbeitsblatt ein Bild-URL-Hyperlink hinzugefügt.

![todo: Bild_alt_Text](working-with-worksheets-gridweb_7.png)

**Ausgabe: Bild-Hyperlink zum Arbeitsblatt hinzugefügt**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-ImageURLHyperlinks-ImageURLHyperlinks.jsp" >}}

## **Daten sortieren**

Das Sortieren ist ein sehr wertvolles Feature, wenn es um die Datenverarbeitung geht. Unsortierte Daten sind für Benutzer bei der Suche nach bestimmten Informationen mühsam. Aspose.Cells.GridWeb unterstützt leistungsstarke Sortierfunktionen. In diesem Thema wird das Sortieren von Daten mit Aspose.Cells.GridWeb API erläutert.

Aspose.Cells.GridWeb ermöglicht es Entwicklern, Daten horizontal und vertikal zu sortieren, sodass Entwickler Daten von oben nach unten oder von links nach rechts sortieren können.

### **Von oben nach unten**

So sortieren Sie Daten von oben nach unten:

1. Fügen Sie Ihrem Webformular das Steuerelement Aspose.Cells.GridWeb hinzu.
1. Greifen Sie auf das Arbeitsblatt zu, das Sie sortieren möchten.
1. Sortieren Sie den Datenbereich in beliebiger Reihenfolge (aufsteigend oder absteigend). Achten Sie darauf, die Ausrichtung von oben nach unten auszuwählen.

Im folgenden Beispiel werden Daten in zwei Spalten (Studenten-ID und Schülername) eines Arbeitsblatts in aufsteigender Reihenfolge sortiert. Nur zwölf Zeilen mit zwei Spalten werden in der Ausrichtung von oben nach unten sortiert.

Vor dem Anwenden des Codes enthält das Arbeitsblatt ungeordnete Daten.

**Eingabe: unsortierte Daten** 

![todo: Bild_alt_Text](working-with-worksheets-gridweb_8.png)

Nach Ausführung des Codes werden die Daten aufsteigend sortiert.

**Ausgabe: Daten von oben nach unten aufsteigend sortiert** 

![todo: Bild_alt_Text](working-with-worksheets-gridweb_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromtoptobottomascendingorder-datasortedfromtoptobottomascendingorder.jsp" >}}

### **Von links nach rechts**

So sortieren Sie Daten von links nach rechts:

1. Fügen Sie Ihrem Webformular das Steuerelement Aspose.Cells.GridWeb hinzu.
1. Greifen Sie auf das Arbeitsblatt zu, das Sie sortieren möchten.
1. Sortieren Sie den Datenbereich in beliebiger Reihenfolge (aufsteigend oder absteigend). Achten Sie darauf, von links nach rechts auszuwählen.

Das folgende Beispiel sortiert Daten in zwei Zeilen (Student ID und Student Name) in aufsteigender Reihenfolge. Nur zwei Zeilen mit vier Spalten werden von links nach rechts sortiert.

Vor dem Anwenden des Codes enthält das Arbeitsblatt ungeordnete Daten.

**Eingabe: unsortierte Daten vor der Ausführung des Code-Snippets** 

![todo: Bild_alt_Text](working-with-worksheets-gridweb_10.png)

Nach Ausführung des Codes werden die Daten in aufsteigender Reihenfolge sortiert.

**Ausgabe: Daten von links nach rechts aufsteigend sortiert** 

![todo: Bild_alt_Text](working-with-worksheets-gridweb_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromleftrightascendingorder-datasortedfromleftrightascendingorder.jsp" >}}

## **Suchen und Ersetzen**

Eine der schnellsten Möglichkeiten, sich wiederholende Änderungen in einer großen Tabelle vorzunehmen, ist die Verwendung der Funktion „Suchen und Ersetzen“. Suchen hilft Ihnen, eine Textzeichenfolge oder Daten zu finden und sie durch einen neuen Wert zu ersetzen. Aspose.Cells. GridWeb bietet diese Funktion. Es ermöglicht Ihnen das Suchen und Ersetzen durch eine bestimmte Textzeichenfolge oder einen bestimmten Wert auf der Arbeitsblatt-Client-Seite über einen einfachen Dialog. Sie können sogar nach Teildaten suchen.

### **Der Dialog Suchen/Ersetzen**

Es gibt zwei Möglichkeiten, das Dialogfeld „Suchen/Ersetzen“ zu öffnen:

1.  Wenn die Steuerung aktiv ist, drücken Sie**STRG+F** um das Dialogfeld zu öffnen, oder drücken Sie**STRG+R** Taste, um den Dialog mit der zu öffnen**Ersetzen** Schaltfläche aktiviert.
1.  Bewegen Sie den Cursor auf den Zellenbereich im Arbeitsblatt und klicken Sie dann mit der rechten Maustaste. Wählen**Finden** oder**Ersetzen** aus dem Menü.

**Auswählen von Suchen**

![todo: Bild_alt_Text](working-with-worksheets-gridweb_12.png)

Ein Dialogfeld zum Suchen und Ersetzen wird angezeigt.

**Der Dialog Suchen/Ersetzen**

![todo: Bild_alt_Text](working-with-worksheets-gridweb_13.png)

**Verwenden von Suchen**

Suchen:

1. Öffnen Sie das Dialogfeld „Suchen/Ersetzen“.
1. Geben Sie die Zeichenfolge, nach der Sie suchen möchten, in das Feld Suchen nach ein.
1. Klicken Sie zum Suchen auf Weitersuchen.

Die nächste Zelle, die Ihrer Suchbedingung entspricht, wird hervorgehoben.

{{% alert color="primary" %}}

Wenn Ihr Suchkriterium nicht gefunden wird, wird ein Dialog angezeigt, der Sie darüber informiert.

{{% /alert %}}

### **Suchoptionen**

Es gibt einige Suchoptionen, die Sie im Dialogfeld anpassen können. Die folgende Tabelle listet sie auf.

|**Nein.**|**Optionsname**|**Beschreibung**|
|:- |:- |:- |
|1|Streichholzschachtel|Gibt an, ob bei der Suche zwischen Groß- und Kleinschreibung unterschieden werden soll.|
|2|Ganzes Wort abgleichen|Gibt an, ob bei der Suche nach dem ganzen Wort gesucht werden soll.|
|3|Nachschlagen|Gibt an, ob die Suche von unten nach oben durchgeführt wird.|
|4|Regulären Ausdruck|Wenn diese Option aktiviert ist, behandelt das Steuerelement die Zeichenfolge im Textfeld Suchen nach als regulären Ausdruck im Suchprozess.|
|5|Suchen Sie in Formeln/Werte|Wenn Formeln ausgewählt ist, stimmt das Steuerelement mit der Formel oder dem unformatierten Wert der Zellen überein, wenn die Formel oder der unformatierte Wert vorhanden ist. Wenn die Werte ausgewählt sind, stimmt das Steuerelement nur mit dem angezeigten Wert der Zellen überein.|

### **Verwendung von Ersetzen**

So ersetzen Sie Text oder Werte:

1.  Öffnen Sie das Dialogfeld „Suchen/Ersetzen“, indem Sie auf drücken**STRG+F** , oder wählen Sie aus, klicken Sie mit der rechten Maustaste auf eine Zelle, und wählen Sie sie aus**Finden** vor dem Klicken**Ersetzen**.
1.  Geben Sie die Ersetzungszeichenfolge in die ein**Ersetzen mit**Gebiet.
1.  Klicken**Ersetzen**.

So ersetzen Sie Text:

1. Öffnen Sie das Dialogfeld.
1.  Geben Sie den gesuchten Text ein**Finde was** Feld und den Text, den Sie darin ersetzen möchten**Ersetzen mit** Gebiet.
1.  Ersetzen Sie jeweils ein Vorkommen, indem Sie auf klicken**Nächstes finden** gefolgt von**Ersetzen**.
1.  Wenn Sie sich sehr sicher sind, was das Arbeitsblatt enthält, klicken Sie auf**Alles ersetzen**.

{{% alert color="primary" %}}

 Wenn sich das Arbeitsblatt nicht im Bearbeitungsmodus befindet, wird die**Ersetzen** Schaltfläche wird nicht angezeigt.

{{% /alert %}}

## Hyperlinks von der Client-Seite hinzufügen/entfernen

Aspose.Cells GridWeb unterstützt jetzt das Hinzufügen und Entfernen von Hyperlinks von der Client-Seite. Dafür stellt die API die Funktionen „addCelllink“ und „delCelllink“ zur Verfügung. Die folgenden Codeausschnitte zeigen das Hinzufügen und Entfernen von Hyperlinks von der Clientseite in GridWeb.

### Beispielcode

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-1.jsp" >}}

Sie können auch mit dem folgenden Code-Snippet auf das Blatt verlinken.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-2.jsp" >}}

## Aktualisieren Sie die Schriftarteinstellungen von der Clientseite

Aspose.Cells GridWeb unterstützt jetzt das Ändern von Schriftarteinstellungen von der Clientseite. Dafür stellt die API folgende Funktionen zur Verfügung

- **updateCellFontStyle**: Params - r/i/b/ib für normal/kursiv/fett/kursiv&&fett
- **updateCellFontSize**: Params - Schriftartname usw. 'System'
- **updateCellFontName**: Params - Schriftgröße usw. '12pt'
- **updateCellFontColor**: Params - none/u/l/ul/ für none/underline/strikeout/underline&&strikeout
- **updateCellFontLine**: Params - HTML-Farbe wie #aa22ee oder bekannte Farbnamen wie grün, rot, ...
- **updateCellBackGroundColor**: Params - HTML-Farbe wie #aa22ee oder bekannte Farbnamen wie grün, rot, ...

Das folgende Code-Snippet zeigt das Ändern von Schriftarteinstellungen von der Clientseite in GridWeb.

### Beispielcode

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-update_font_from_client_side-1.jsp" >}}

## Kommentare vom Client hinzufügen/entfernen

Aspose.Cells GridWeb unterstützt jetzt das Hinzufügen und Entfernen von Kommentaren von der Client-Seite. Dafür stellt die API die Funktionen „addcomments“ und „delcomments“ zur Verfügung. Das folgende Code-Snippet veranschaulicht das Hinzufügen und Entfernen von Kommentaren von der Client-Seite in GridWeb.

### Beispielcode

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add_remove_comments_from_client_side.jsp" >}}

## Schaltflächen zum Hinzufügen/Entfernen von Arbeitsblättern anzeigen

 Aspose.Cells GridWeb unterstützt jetzt das Hinzufügen und Entfernen von Blättern mithilfe von Schaltflächen in der Symbolleiste. Damit die Schaltflächen im Frontend sichtbar sind, müssen Sie festlegen**GridWeb1.ShowAddButton** zu**wahr**. Der folgende Codeausschnitt veranschaulicht das Hinzufügen von Schaltflächen zum Hinzufügen/Entfernen zur GridWeb-Symbolleiste.

### Beispielcode

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "GridWeb-show_add_remove_worksheet_buttons.java" >}}
