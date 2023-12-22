---
title: Arbeiten mit Arbeitsblättern GridWeb
type: docs
weight: 30
url: /de/java/working-with-worksheets-gridweb/
---
##  **Auf Arbeitsblätter zugreifen**

In diesem Thema wird der Zugriff auf Arbeitsblätter des GridWeb-Steuerelements erläutert. Wir können diese Arbeitsblätter auch Web-Arbeitsblätter nennen, da sie zu GridWeb gehören und in Webanwendungen verwendet werden.

Alle im GridWeb-Steuerelement enthaltenen Arbeitsblätter werden in einer GridWorksheetCollection des GridWeb-Steuerelements gespeichert. Es ist einfach, über den Blattindex auf ein bestimmtes Arbeitsblatt zuzugreifen.

Entwickler können auf ein bestimmtes Arbeitsblatt zugreifen, indem sie dessen Blattindex angeben, wie unten im Beispielcodeausschnitt gezeigt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingWorksheet-AccessingWorksheet.jsp" >}}

##  **Entfernen eines Arbeitsblatts**

Dieses Thema enthält kurze Informationen zum Entfernen von Arbeitsblättern aus Microsoft Excel-Dateien mithilfe von GridWeb API. Entfernen Sie ein Arbeitsblatt, indem Sie seinen Blattindex angeben.

Entwickler können ein bestimmtes Arbeitsblatt entfernen, indem sie seinen Blattindex mithilfe der Methode „removeAt“ der GridWorksheetCollection-Sammlung angeben, wie unten im Beispielcodeausschnitt gezeigt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingWorksheet-RemovingWorksheet.jsp" >}}

##  **Arbeitsblätter hinzufügen**

Arbeitsblätter sind ein integraler Bestandteil von GridWeb. Alle Daten werden in Form von Arbeitsblättern verwaltet und gespeichert. Mit GridWeb können Entwickler ein oder mehrere Arbeitsblätter zum Aspose.Cells.GridWeb-Steuerelement hinzufügen. Dieses Thema zeigt einfache Ansätze zum Hinzufügen von Arbeitsblättern zu GridWeb.

###  **Ohne Angabe des Blattnamens**

Die einfachste Möglichkeit, ein Arbeitsblatt zu Aspose.Cells.GridWeb hinzuzufügen, besteht darin, die Add-Methode der GridWorksheetCollection-Klasse im GridWeb-Steuerelement aufzurufen. Dadurch werden Arbeitsblätter erstellt, die Standardnamen verwenden (Blatt1, Blatt2, Blatt3 usw.), und sie werden dem GridWeb-Steuerelement hinzugefügt.

**Ausgabe: Ein Arbeitsblatt mit Standardnamen wurde zu GridWeb hinzugefügt** 

![todo:image_alt_text](working-with-worksheets-gridweb_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithoutSpecificName-AddingWorksheetWithoutSpecificName.jsp" >}}

###  **Mit angegebenem Blattnamen**

Um ein Arbeitsblatt mit einem bestimmten Namen zum GridWeb-Steuerelement hinzuzufügen, anstatt das Standardbenennungsschema zu verwenden, rufen Sie eine überladene Version der Add-Methode auf, die die angegebene Zeichenfolge SheetName annimmt. Im folgenden Beispiel wird beispielsweise ein Arbeitsblatt mit dem Namen „Rechnung“ hinzugefügt.

**Ausgabe: Ein Arbeitsblatt mit einem angegebenen Namen wurde zu GridWeb hinzugefügt** 

![todo:image_alt_text](working-with-worksheets-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithSpecificName-AddingWorksheetWithSpecificName.jsp" >}}

{{% alert color="primary" %}}

 Die Methode add() gibt den Index des neuen Arbeitsblatts zurück, mit dem auf die Instanz dieses Arbeitsblatts zugegriffen werden kann. Weitere Informationen zum Zugriff auf Arbeitsblätter finden Sie unter[Auf Arbeitsblätter zugreifen](/cells/de/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

##  **Ein Arbeitsblatt umbenennen**

Das Umbenennen eines Arbeitsblatts kann sehr nützlich sein, wenn Sie mit vielen Arbeitsblättern in GridWeb arbeiten und sich entscheiden, deren Namen zu ändern, um sie aussagekräftiger zu machen. Beispielsweise kann ein Arbeitsblatt, das eine Rechnung enthält, in „Rechnung“ anstelle von „Blatt1“ umbenannt werden. In diesem Thema wird diese einfache, aber nützliche Funktion beschrieben.

###  **Ein Arbeitsblatt umbenennen**

Alle Arbeitsblätter enthalten eine Name-Eigenschaft, die es Entwicklern ermöglicht, auf die Namen der Arbeitsblätter zuzugreifen oder diese zu ändern. Um ein Arbeitsblatt umzubenennen:

1. Greifen Sie über die GridWorksheetCollection auf ein Arbeitsblatt zu.
1. Benennen Sie das ausgewählte Arbeitsblatt um.

{{% alert color="primary" %}}

 Weitere Informationen zum Zugriff auf Arbeitsblätter in Aspose.Cells.GridWeb finden Sie unter[Auf Arbeitsblätter zugreifen](/cells/de/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

Vor der Ausführung des Codes erhält das Arbeitsblatt einen Standardnamen, z. B. Sheet1.

**Eingabedatei: ein Arbeitsblatt mit dem Standardnamen Sheet1** 

![todo:image_alt_text](working-with-worksheets-gridweb_3.png)

Nach der Ausführung des Codes wird das Arbeitsblatt in „Rechnung“ umbenannt.

**Ausgabe: Das Arbeitsblatt wird in „Rechnung“ umbenannt** 

![todo:image_alt_text](working-with-worksheets-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RenamingWorksheet-RenamingWorksheet.jsp" >}}

##  **Kopieren eines Arbeitsblatts**

[Arbeitsblätter hinzufügen](/cells/de/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-addingworksheets)beschreibt, wie neue Arbeitsblätter zu GridWeb hinzugefügt werden. Es ist auch möglich, dem Aspose.Cells.GridWeb-Steuerelement eine Kopie (oder Replik) eines anderen Arbeitsblatts hinzuzufügen. Diese Funktion kann nützlich sein, wenn identische oder ähnliche Daten in einem Arbeitsblatt auch in einem anderen Arbeitsblatt benötigt werden. In diesem Fall ist es einfacher, ein vorhandenes Arbeitsblatt zu kopieren und als neues Arbeitsblatt zu Aspose.Cells.GridWeb hinzuzufügen, anstatt es von Grund auf neu zu erstellen.

###  **Verwenden des Blattindex**

Der folgende Beispielcode zeigt, wie Sie dem GridWeb-Steuerelement eine Kopie eines Arbeitsblatts hinzufügen, indem Sie den Index des Arbeitsblatts in der addCopy-Methode der GridWorksheetCollection angeben.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetIndex-CopyWorksheetUsingSheetIndex.jsp" >}}
###  **Blattnamen verwenden**
Der folgende Beispielcode zeigt, wie Sie dem GridWeb-Steuerelement eine Kopie eines Arbeitsblatts hinzufügen, indem Sie den Namen des Arbeitsblatts in der addCopy-Methode der GridWorksheetCollection angeben.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetName-CopyWorksheetUsingSheetName.jsp" >}}

{{% alert color="primary" %}}

 Die Methode addCopy gibt den Index des neu hinzugefügten Arbeitsblatts zurück, der für den Zugriff auf die Arbeitsblattinstanz verwendet werden kann. Weitere Informationen zum Zugriff auf Arbeitsblätter finden Sie unter[Auf Arbeitsblätter zugreifen](/cells/de/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

##  **Arbeiten mit benannten Bereichen**

Normalerweise werden Spalten- und Zeilenbeschriftungen verwendet, um eindeutig auf Zellen zu verweisen. Sie können jedoch beschreibende Namen erstellen, um Zellen, Zellbereiche, Formeln oder konstante Werte darzustellen.

 Das Wort**Name** kann sich auf eine Zeichenfolge beziehen, die eine Zelle, einen Zellbereich, eine Formel oder einen konstanten Wert darstellt. Verwenden Sie beispielsweise leicht verständliche Namen wie „Produkte“, um auf schwer verständliche Bereiche wie „Sales!C20:C30“ zu verweisen.

 Beschriftungen können in Formeln verwendet werden, die sich auf Daten im selben Arbeitsblatt beziehen; Wenn Sie einen Bereich auf einem anderen Arbeitsblatt darstellen möchten, können Sie einen Namen verwenden.**Benannte Bereiche** ist eine der leistungsstärksten Funktionen von Microsoft Excel.

Benutzer können einem Bereich einen Namen zuweisen und diesen Namen in Formeln verwenden. Aspose.Cells.GridWeb unterstützt diese Funktion.

###  **Benannte Bereiche in Formeln hinzufügen/referenzieren**

Das GridWeb-Steuerelement stellt zwei Klassen (GridName und GridNameCollection) für die Arbeit mit benannten Bereichen bereit.

Der folgende Codeausschnitt hilft Ihnen zu verstehen, wie Sie sie verwenden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingNamedRangesinFormulas-AddingNamedRangesinFormulas.jsp" >}}

##  **Kommentare im Arbeitsblatt verwalten**

In diesem Thema wird das Hinzufügen, Zugreifen auf und Entfernen von Kommentaren aus Arbeitsblättern erläutert. Kommentare sind nützlich, um Notizen oder nützliche Informationen für Benutzer hinzuzufügen, die mit dem Blatt arbeiten. Entwickler haben die Flexibilität, Kommentare zu jeder Zelle des Arbeitsblatts hinzuzufügen.

###  **Arbeiten mit Kommentaren**

####  **Kommentare hinzufügen**

Um einen Kommentar zum Arbeitsblatt hinzuzufügen, führen Sie bitte die folgenden Schritte aus:

1. Fügen Sie das Aspose.Cells.GridWeb-Steuerelement zum Webformular hinzu.
1. Greifen Sie auf das Arbeitsblatt zu, zu dem Sie Kommentare hinzufügen.
1. Fügen Sie einer Zelle einen Kommentar hinzu.
1. Legen Sie eine Notiz für den neuen Kommentar fest.

**Dem Arbeitsblatt wurde ein Kommentar hinzugefügt** 

![todo:image_alt_text](working-with-worksheets-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingComments-AddingComments.jsp" >}}

####  **Auf Kommentare zugreifen**

So greifen Sie auf einen Kommentar zu:

1. Greifen Sie auf die Zelle zu, die den Kommentar enthält.
1. Rufen Sie die Referenz der Zelle ab.
1. Übergeben Sie den Verweis auf die Kommentarsammlung, um auf den Kommentar zuzugreifen.
1. Es ist jetzt möglich, die Eigenschaften des Kommentars zu ändern.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingComments-AccessingComments.jsp" >}}

####  **Kommentare entfernen**

So entfernen Sie einen Kommentar:

1. Greifen Sie wie oben beschrieben auf die Zelle zu.
1. Verwenden Sie die Methode „removeAt“ der Comment-Sammlung, um den Kommentar zu entfernen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingComments-RemovingComments.jsp" >}}

##  **Verwalten von Hyperlinks im Arbeitsblatt**

In diesem Thema wird erläutert, welche Arten von Hyperlinks in Aspose.Cells.GridWeb unterstützt werden und wie sie programmgesteuert verwaltet werden. Hyperlinks können entweder zum Erstellen von Links zu Web-URLs oder zum Durchführen eines Postbacks an einen Server verwendet werden.

###  **Arten von Hyperlinks**

Die folgenden Hyperlinks werden von Aspose.Cells.GridWeb unterstützt:

- Text-URL-Hyperlinks, auf den Text angewendete URL-Hyperlinks.
- Bild-URL-Hyperlinks, auf Bilder angewendete URL-Hyperlinks.

####  **Text-URL-Hyperlinks**

Das folgende Beispiel fügt einem Arbeitsblatt zwei Hyperlinks hinzu. Einer hat ein _blank-Ziel, während der andere auf _parent gesetzt ist.

![todo:image_alt_text](working-with-worksheets-gridweb_6.png)

**Ausgabe: Text-Hyperlinks zum Arbeitsblatt hinzugefügt**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-TextURLHyperlinks-TextURLHyperlinks.jsp" >}}

####  **Bild-URL-Hyperlinks**

Das folgende Beispiel fügt einem Arbeitsblatt einen Bild-URL-Hyperlink hinzu.

![todo:image_alt_text](working-with-worksheets-gridweb_7.png)

**Ausgabe: Bild-Hyperlink zum Arbeitsblatt hinzugefügt**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-ImageURLHyperlinks-ImageURLHyperlinks.jsp" >}}

##  **Daten sortieren**

Das Sortieren ist eine sehr wertvolle Funktion bei der Datenverarbeitung. Unsortierte Daten sind für Benutzer ein Problem bei der Suche nach bestimmten Informationen. Aspose.Cells.GridWeb unterstützt leistungsstarke Sortierfunktionen. In diesem Thema wird das Sortieren von Daten mithilfe des Aspose.Cells.GridWeb API erläutert.

Aspose.Cells.GridWeb ermöglicht Entwicklern das horizontale und vertikale Sortieren von Daten, sodass Entwickler Daten von oben nach unten oder von links nach rechts sortieren können.

###  **Von oben nach unten**

So sortieren Sie Daten von oben nach unten:

1. Fügen Sie das Aspose.Cells.GridWeb-Steuerelement zu Ihrem Webformular hinzu.
1. Greifen Sie auf das Arbeitsblatt zu, das Sie sortieren möchten.
1. Sortieren Sie den Datenbereich in beliebiger Reihenfolge (aufsteigend oder absteigend). Stellen Sie sicher, dass Sie die Ausrichtung von oben nach unten wählen.

Das folgende Beispiel sortiert Daten in zwei Spalten (Studenten-ID und Studentenname) eines Arbeitsblatts in aufsteigender Reihenfolge. Nur zwölf Zeilen mit zwei Spalten werden von oben nach unten sortiert.

Vor der Anwendung des Codes enthält das Arbeitsblatt ungeordnete Daten.

**Eingabe: unsortierte Daten** 

![todo:image_alt_text](working-with-worksheets-gridweb_8.png)

Nach der Ausführung des Codes werden die Daten in aufsteigender Reihenfolge sortiert.

**Ausgabe: Daten von oben nach unten in aufsteigender Reihenfolge sortiert** 

![todo:image_alt_text](working-with-worksheets-gridweb_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromtoptobottomascendingorder-datasortedfromtoptobottomascendingorder.jsp" >}}

###  **Von links nach rechts**

So sortieren Sie Daten von links nach rechts:

1. Fügen Sie das Aspose.Cells.GridWeb-Steuerelement zu Ihrem Webformular hinzu.
1. Greifen Sie auf das Arbeitsblatt zu, das Sie sortieren möchten.
1. Sortieren Sie den Datenbereich in beliebiger Reihenfolge (aufsteigend oder absteigend). Achten Sie darauf, von links nach rechts auszuwählen.

Im folgenden Beispiel werden die Daten in zwei Zeilen (Studenten-ID und Studentenname) in aufsteigender Reihenfolge sortiert. Nur zwei Reihen mit je vier Spalten werden von links nach rechts sortiert.

Vor der Anwendung des Codes enthält das Arbeitsblatt ungeordnete Daten.

**Eingabe: unsortierte Daten vor der Ausführung des Code-Snippets** 

![todo:image_alt_text](working-with-worksheets-gridweb_10.png)

Nach der Ausführung des Codes werden die Daten in aufsteigender Reihenfolge sortiert.

**Ausgabe: Daten von links nach rechts in aufsteigender Reihenfolge sortiert** 

![todo:image_alt_text](working-with-worksheets-gridweb_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromleftrightascendingorder-datasortedfromleftrightascendingorder.jsp" >}}

##  **Suchen und Ersetzen**

Eine der schnellsten Möglichkeiten, sich wiederholende Änderungen in einer großen Tabelle vorzunehmen, ist die Verwendung der Funktion „Suchen und Ersetzen“. Mit „Suchen“ können Sie eine Textzeichenfolge oder Daten finden und diese durch einen neuen Wert ersetzen. Aspose.Cells.GridWeb bietet diese Funktion. Es ermöglicht Ihnen, clientseitig über einen einfachen Dialog nach einer bestimmten Textzeichenfolge oder einem bestimmten Wert im Arbeitsblatt zu suchen und diese durch diese zu ersetzen. Es ermöglicht Ihnen sogar, nach Teildaten zu suchen.

###  **Das Dialogfeld „Suchen/Ersetzen“.**

Es gibt zwei Möglichkeiten, das Dialogfeld „Suchen/Ersetzen“ zu öffnen:

1.  Wenn die Steuerung aktiv ist, drücken Sie**STRG+F** , um den Dialog zu öffnen, oder drücken Sie**STRG+R** Taste, um den Dialog mit dem zu öffnen**Ersetzen** Schaltfläche aktiviert.
1.  Bewegen Sie den Cursor auf den Zellenbereich im Arbeitsblatt und klicken Sie dann mit der rechten Maustaste. Wählen**Finden** oder**Ersetzen** aus dem Menü.

**Wählen Sie „Suchen“.**

![todo:image_alt_text](working-with-worksheets-gridweb_12.png)

Ein Dialogfeld zum Suchen und Ersetzen wird angezeigt.

**Das Dialogfeld „Suchen/Ersetzen“.**

![todo:image_alt_text](working-with-worksheets-gridweb_13.png)

**Verwenden von Suchen**

Suchen:

1. Öffnen Sie das Dialogfeld „Suchen/Ersetzen“.
1. Geben Sie die Zeichenfolge, nach der Sie suchen möchten, in das Feld „Suchen nach“ ein.
1. Klicken Sie zum Suchen auf Weitersuchen.

Die nächste Zelle, die Ihrer Suchbedingung entspricht, wird hervorgehoben.

{{% alert color="primary" %}}

Wenn Ihr Suchkriterium nicht gefunden wird, wird ein Dialog angezeigt, der Sie darüber informiert.

{{% /alert %}}

###  **Suchoptionen**

Es gibt einige Suchoptionen, die Sie im Dialog anpassen können. Die folgende Tabelle listet sie auf.

|**NEIN.**|**Optionsname**|**Beschreibung**|
| :- | :- | :- |
|1|Streichholzetui|Gibt an, ob bei der Suche die Groß-/Kleinschreibung beachtet werden soll.|
|2|Ganzes Wort zuordnen|Gibt an, ob bei der Suche das ganze Wort gefunden werden soll.|
|3|Nachschlagen|Gibt an, ob die Suche von unten nach oben durchgeführt wird.|
|4|Regulären Ausdruck|Wenn diese Option aktiviert ist, behandelt das Steuerelement die Zeichenfolge im Textfeld „Suchen nach“ als regulären Ausdruck im Suchvorgang.|
|5|Suchen Sie in Formeln/Werte|Wenn die Formeln ausgewählt sind, gleicht das Steuerelement die Formel oder den unformatierten Wert der Zellen ab, wenn die Formel oder der unformatierte Wert vorhanden ist. Wenn „Werte“ ausgewählt ist, stimmt das Steuerelement nur mit dem angezeigten Wert der Zellen überein.|

###  **Verwenden von Ersetzen**

So ersetzen Sie Text oder Werte:

1.  Öffnen Sie das Dialogfeld „Suchen/Ersetzen“, indem Sie auf drücken**STRG+F**, oder klicken Sie mit der rechten Maustaste auf eine Zelle und wählen Sie **Suchen** bevor Sie auf *Ersetzen** klicken.
1.  Geben Sie die Ersatzzeichenfolge ein**Ersetzen mit**Feld.
1. Klicken Sie auf *Ersetzen**.

Um Text zu ersetzen:

1. Öffnen Sie das Dialogfeld.
1.  Geben Sie den Text ein, den Sie suchen möchten**Finde was** Feld und den Text, den Sie ersetzen möchten**Ersetzen mit** Feld.
1.  Ersetzen Sie jeweils ein Vorkommen, indem Sie darauf klicken**Nächstes finden** gefolgt von *Ersetzen**.
1. Wenn Sie sehr sicher sind, was das Arbeitsblatt enthält, klicken Sie auf *Alle ersetzen**.

{{% alert color="primary" %}}

 Wenn sich das Arbeitsblatt nicht im Bearbeitungsmodus befindet, wird die**Ersetzen** Die Schaltfläche wird nicht angezeigt.

{{% /alert %}}

## Hyperlinks auf der Clientseite hinzufügen/entfernen

Aspose.Cells GridWeb unterstützt jetzt das Hinzufügen und Entfernen von Hyperlinks auf der Clientseite. Hierzu stellt die API die Funktionen „addCelllink“ und „delCelllink“ zur Verfügung. Die folgenden Codeausschnitte demonstrieren das Hinzufügen und Entfernen von Hyperlinks auf der Clientseite in GridWeb.

###  Beispielcode

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-1.jsp" >}}

Sie können das Blatt auch mit dem folgenden Codeausschnitt verlinken.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-2.jsp" >}}

##  Aktualisieren Sie die Schriftarteinstellungen clientseitig

Aspose.Cells GridWeb unterstützt jetzt das Ändern von Schriftarteinstellungen auf der Clientseite. Hierzu stellt die API folgende Funktionen zur Verfügung

- *updateCellFontStyle**: Parameter – r/i/b/ib für normal/kursiv/fett/kursiv&&fett
- *updateCellFontSize**: Parameter – Schriftartname usw. „System“
- *updateCellFontName**: Parameter – Schriftgröße usw. '12pt'
- *updateCellFontColor**: Parameter – none/u/l/ul/ für none/underline/strikeout/underline&&strikeout
- *updateCellFontLine**: Parameter – HTML-Farbe wie #aa22ee oder bekannte Farbnamen wie grün, rot, ...
- *updateCellBackGroundColor**: Parameter – HTML-Farbe wie #aa22ee oder bekannte Farbnamen wie grün, rot, ...

Der folgende Codeausschnitt demonstriert das Ändern der Schriftarteinstellungen auf der Clientseite in GridWeb.

###  Beispielcode

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-update_font_from_client_side-1.jsp" >}}

##  Kommentare auf der Clientseite hinzufügen/entfernen

Aspose.Cells GridWeb unterstützt jetzt das Hinzufügen und Entfernen von Kommentaren auf der Clientseite. Hierzu stellt die API die Funktionen „Addcomments“ und „Delcomments“ zur Verfügung. Der folgende Codeausschnitt veranschaulicht das Hinzufügen und Entfernen von Kommentaren auf der Clientseite in GridWeb.

###  Beispielcode

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add_remove_comments_from_client_side.jsp" >}}

##  Schaltflächen zum Hinzufügen/Entfernen von Arbeitsblättern anzeigen

 Aspose.Cells GridWeb unterstützt jetzt das Hinzufügen und Entfernen von Blättern mithilfe von Schaltflächen in der Symbolleiste. Damit die Buttons im Frontend sichtbar sind, müssen Sie einstellen**GridWeb1.ShowAddButton** zu *wahr**. Der folgende Codeausschnitt veranschaulicht das Hinzufügen von Schaltflächen zum Hinzufügen/Entfernen zur GridWeb-Symbolleiste.

###  Beispielcode

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "GridWeb-show_add_remove_worksheet_buttons.java" >}}
