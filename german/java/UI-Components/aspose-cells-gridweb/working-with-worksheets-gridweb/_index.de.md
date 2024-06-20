---
title: Arbeiten mit Arbeitsblättern in GridWeb
type: docs
weight: 30
url: /de/java/working-with-worksheets-gridweb/
---

## **Arbeitsblätter abrufen**

In diesem Thema wird der Zugriff auf Arbeitsblätter des GridWeb-Steuerelements diskutiert. Wir können diese Arbeitsblätter auch Web-Arbeitsblätter nennen, da sie zu GridWeb gehören und in Webanwendungen verwendet werden.

Alle Arbeitsblätter im GridWeb-Steuerelement sind in einer GridWorksheetCollection des GridWeb-Steuerelements gespeichert. Es ist einfach, auf ein bestimmtes Arbeitsblatt anhand seines Blattindexes zuzugreifen.

Entwickler können auf ein bestimmtes Arbeitsblatt zugreifen, indem sie seinen Tabellenindex wie im untenstehenden Beispielcode-Schnipsel angegeben.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingWorksheet-AccessingWorksheet.jsp" >}}

## **Arbeitsblatt entfernen**

Dieses Thema bietet eine kurze Information zum Entfernen von Arbeitsblättern aus Microsoft Excel-Dateien mithilfe der GridWeb-API. Entfernen Sie ein Arbeitsblatt, indem Sie seinen Tabellenindex angeben.

Entwickler können ein bestimmtes Arbeitsblatt entfernen, indem sie seinen Tabellenindex unter Verwendung der removeAt-Methode der GridWorksheetCollection-Sammlung wie im untenstehenden Beispielcode-Schnipsel angegeben.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingWorksheet-RemovingWorksheet.jsp" >}}

## **Arbeitsblätter hinzufügen**

Arbeitsblätter sind ein integraler Bestandteil von GridWeb. Alle Daten werden in Form von Arbeitsblättern verwaltet und gespeichert. GridWeb ermöglicht Entwicklern, ein oder mehrere Arbeitsblätter zur Aspose.Cells.GridWeb-Steuerung hinzuzufügen. Dieses Thema zeigt einfache Ansätze zum Hinzufügen von Arbeitsblättern zu GridWeb.

### **Ohne Angabe des Blattnamens**

Der einfachste Weg, ein Arbeitsblatt zu Aspose.Cells.GridWeb hinzuzufügen, besteht darin, die add-Methode der Klasse GridWorksheetCollection in der GridWeb-Steuerung aufzurufen. Dadurch werden Arbeitsblätter erstellt, die Standardnamen verwenden (beispielsweise Blatt1, Blatt2, Blatt3 usw.) und der GridWeb-Steuerung hinzugefügt.

**Ausgabe: Ein Arbeitsblatt mit Standardnamen wurde zu GridWeb hinzugefügt** 

![todo:image_alt_text](working-with-worksheets-gridweb_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithoutSpecificName-AddingWorksheetWithoutSpecificName.jsp" >}}

### **Mit angegebenem Blattnamen**

Um anstelle des Standardbenennungsschemas ein Arbeitsblatt mit einem bestimmten Namen zur GridWeb-Steuerung hinzuzufügen, rufen Sie eine überladene Version der add-Methode auf, die den angegebenen String SheetName akzeptiert. Beispielsweise fügt das untenstehende Beispiel ein Arbeitsblatt mit dem Namen Rechnung hinzu.

**Ausgabe: Ein Arbeitsblatt mit angegebenem Namen wurde zu GridWeb hinzugefügt** 

![todo:image_alt_text](working-with-worksheets-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithSpecificName-AddingWorksheetWithSpecificName.jsp" >}}

{{% alert color="primary" %}}

Die Methode add() gibt den Index des neuen Arbeitsblatts zurück, der zum Zugriff auf die Instanz dieses Arbeitsblatts verwendet werden kann. Weitere Details zum Zugriff auf Arbeitsblätter finden Sie unter [Zugriff auf Arbeitsblätter](/cells/de/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

## **Arbeitsblatt umbenennen**

Das Umbenennen eines Arbeitsblatts kann sehr nützlich sein, wenn Sie mit vielen Arbeitsblättern in GridWeb arbeiten und sich dafür entscheiden, ihre Namen zu ändern, um sie aussagekräftiger zu machen. Zum Beispiel kann ein Arbeitsblatt, das eine Rechnung enthält, anstelle von Blatt1 in Rechnung umbenannt werden. In diesem Thema wird diese einfache, aber nützliche Funktion beschrieben.

### **Arbeitsblatt umbenennen**

Alle Arbeitsblätter enthalten eine Name-Eigenschaft, die es Entwicklern ermöglicht, auf Arbeitsblattnamen zuzugreifen oder diese zu ändern. Um ein Arbeitsblatt umzubenennen:

1. Greifen Sie auf ein Arbeitsblatt aus der GridWorksheetCollection zu.
1. Benennen Sie das ausgewählte Arbeitsblatt um.

{{% alert color="primary" %}}

Weitere Informationen zum Zugriff auf Arbeitsblätter in Aspose.Cells.GridWeb finden Sie unter [Zugriff auf Arbeitsblätter](/cells/de/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

Bevor der Code ausgeführt wird, hat das Arbeitsblatt einen Standardnamen wie Blatt1.

**Eingabedatei: ein Arbeitsblatt mit einem Standardnamen Blatt1** 

![todo:image_alt_text](working-with-worksheets-gridweb_3.png)

Nach Ausführung des Codes wurde das Arbeitsblatt in Rechnung umbenannt.

**Ausgabe: Das Arbeitsblatt wurde in Rechnung umbenannt** 

![todo:image_alt_text](working-with-worksheets-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RenamingWorksheet-RenamingWorksheet.jsp" >}}

## **Kopieren eines Arbeitsblatts**

[Arbeitsblätter hinzufügen](/cells/de/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-addingworksheets) beschreibt, wie neue Arbeitsblätter zu GridWeb hinzugefügt werden können. Es ist auch möglich, eine Kopie (oder Replik) eines anderen Arbeitsblatts zur Aspose.Cells.GridWeb-Steuerung hinzuzufügen. Diese Funktion kann nützlich sein, wenn identische oder ähnliche Daten in einem Arbeitsblatt auch in einem anderen Arbeitsblatt benötigt werden. In diesem Fall ist es einfacher, ein vorhandenes Arbeitsblatt zu kopieren und als neues Arbeitsblatt zu Aspose.Cells.GridWeb hinzuzufügen, anstatt es von Grund auf neu zu erstellen.

### **Verwendung des Blattindex**

Im untenstehenden Beispielcode wird gezeigt, wie eine Kopie eines Arbeitsblatts zur GridWeb-Steuerung hinzugefügt wird, indem der Index des Arbeitsblatts in der addCopy-Methode der GridWorksheetCollection angegeben wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetIndex-CopyWorksheetUsingSheetIndex.jsp" >}}
### **Verwendung des Blattnamens**
Das unten stehende Beispiel zeigt, wie Sie eine Kopie eines Arbeitsblatts zum GridWeb-Control hinzufügen, indem Sie den Namen des Arbeitsblatts in der addCopy-Methode der GridWorksheetCollection angeben.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetName-CopyWorksheetUsingSheetName.jsp" >}}

{{% alert color="primary" %}}

Die addCopy-Methode gibt den Index des neu hinzugefügten Arbeitsblatts zurück, der verwendet werden kann, um das Arbeitsblatt-Instanz aufzurufen. Weitere Details zum Zugriff auf Arbeitsblätter finden Sie unter [Zugriff auf Arbeitsblätter](/cells/de/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

## **Arbeiten mit benannten Bereichen**

Normalerweise werden Spalten- und Zeilenbezeichnungen verwendet, um eindeutig auf Zellen zu verweisen. Sie können jedoch aussagekräftige Namen erstellen, um Zellen, Zellenbereiche, Formeln oder Konstanten zu repräsentieren.

Das Wort **Name** kann sich auf eine Zeichenfolge von Zeichen beziehen, die eine Zelle, einen Zellenbereich, eine Formel oder einen Konstantenwert darstellt. Verwenden Sie beispielsweise leicht verständliche Namen wie z.B. Produkte, um auf schwer verständliche Bereiche wie z.B. Umsatz!C20:C30 zu verweisen.

Labels können in Formeln verwendet werden, die sich auf Daten im selben Arbeitsblatt beziehen. Wenn Sie einen Bereich in einem anderen Arbeitsblatt darstellen möchten, können Sie einen Namen verwenden. **Benannte Bereiche** sind eine der leistungsstärksten Funktionen von Microsoft Excel.

Benutzer können einem Bereich einen Namen zuweisen und diesen Namen in Formeln verwenden. Aspose.Cells.GridWeb unterstützt diese Funktion.

### **Hinzufügen/Referenzierung benannter Bereiche in Formeln**

Das GridWeb-Control bietet zwei Klassen (GridName und GridNameCollection) für die Arbeit mit benannten Bereichen.

Der folgende Code-Schnipsel wird Ihnen helfen, zu verstehen, wie Sie sie verwenden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingNamedRangesinFormulas-AddingNamedRangesinFormulas.jsp" >}}

## **Verwalten von Kommentaren im Arbeitsblatt**

Dieses Thema behandelt das Hinzufügen, Zugreifen und Entfernen von Kommentaren aus Arbeitsblättern. Kommentare sind nützlich, um Notizen oder nützliche Informationen für Benutzer hinzuzufügen, die mit dem Blatt arbeiten werden. Entwickler haben die Flexibilität, Kommentare zu jeder Zelle des Arbeitsblatts hinzuzufügen.

### **Arbeiten mit Kommentaren**

#### **Kommentare hinzufügen**

Um einem Arbeitsblatt einen Kommentar hinzuzufügen, befolgen Sie bitte die folgenden Schritte:

1. Fügen Sie das Aspose.Cells.GridWeb-Control dem Webformular hinzu.
1. Greifen Sie auf das Arbeitsblatt zu, zu dem Sie Kommentare hinzufügen.
1. Fügen Sie einem Zelle einen Kommentar hinzu.
1. Setzen Sie eine Notiz für den neuen Kommentar.

**Ein Kommentar wurde dem Arbeitsblatt hinzugefügt** 

![todo:image_alt_text](working-with-worksheets-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingComments-AddingComments.jsp" >}}

#### **Zugriff auf Kommentare**

Um auf einen Kommentar zuzugreifen:

1. Greifen Sie auf die Zelle zu, die den Kommentar enthält.
1. Ermitteln Sie die Referenz der Zelle.
1. Geben Sie die Referenz an die Kommentar-Sammlung weiter, um auf den Kommentar zuzugreifen.
1. Es ist jetzt möglich, die Eigenschaften des Kommentars zu ändern.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingComments-AccessingComments.jsp" >}}

#### **Kommentare entfernen**

Um einen Kommentar zu entfernen:

1. Greifen Sie wie oben erläutert auf die Zelle zu.
1. Verwenden Sie die removeAt-Methode der Kommentarsammlung, um den Kommentar zu entfernen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingComments-RemovingComments.jsp" >}}

## **Verwalten von Hyperlinks im Arbeitsblatt**

Dieses Thema behandelt, welche Arten von Hyperlinks von Aspose.Cells.GridWeb unterstützt werden und wie man sie programmgesteuert verwaltet. Hyperlinks können entweder zum Erstellen von Links zu Web-URLs oder zum Ausführen von Postbacks an einen Server verwendet werden.

### **Arten von Hyperlinks**

Die folgenden Hyperlinks werden von Aspose.Cells.GridWeb unterstützt:

- Text-URL-Hyperlinks, URL-Hyperlinks, die auf den Text angewendet werden.
- Bild-URL-Hyperlinks, URL-Hyperlinks, die auf Bilder angewendet werden.

#### **Text-URL-Hyperlinks**

Das folgende Beispiel fügt zwei Hyperlinks zu einem Arbeitsblatt hinzu. Einer hat ein _blank-Ziel, während der andere auf _parent gesetzt ist.

![todo:image_alt_text](working-with-worksheets-gridweb_6.png)

**Output: Text-Hyperlinks zum Arbeitsblatt hinzugefügt**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-TextURLHyperlinks-TextURLHyperlinks.jsp" >}}

#### **Bild-URL-Hyperlinks**

Das folgende Beispiel fügt einem Arbeitsblatt einen Bild-URL-Hyperlink hinzu.

![todo:image_alt_text](working-with-worksheets-gridweb_7.png)

**Ausgabe: Bild-Hyperlink zum Arbeitsblatt hinzugefügt**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-ImageURLHyperlinks-ImageURLHyperlinks.jsp" >}}

## **Daten sortieren**

Das Sortieren ist ein sehr wertvolles Feature, wenn es um die Datenverarbeitung geht. Unsortierte Daten sind für Benutzer eine Qual bei der Suche nach bestimmten Informationen. Aspose.Cells.GridWeb unterstützt leistungsstarke Sortierfunktionen. Dieses Thema behandelt das Sortieren von Daten mithilfe der Aspose.Cells.GridWeb-API.

Aspose.Cells.GridWeb ermöglicht Entwicklern, Daten horizontal und vertikal zu sortieren, sodass Daten von oben nach unten oder von links nach rechts sortiert werden können.

### **Von oben nach unten**

Um Daten von oben nach unten zu sortieren:

1. Fügen Sie die Aspose.Cells.GridWeb-Steuerung Ihrem Webformular hinzu.
1. Greifen Sie auf das Arbeitsblatt zu, das Sie sortieren möchten.
1. Sortieren Sie den Datenbereich in beliebiger Reihenfolge (aufsteigend oder absteigend). Wählen Sie dabei die Orientierung von oben nach unten aus.

Das folgende Beispiel sortiert Daten in zwei Spalten (Schüler-ID und Schülername) eines Arbeitsblatts in aufsteigender Reihenfolge. Es werden nur zwölf Zeilen mit zwei Spalten von oben nach unten sortiert.

Vor der Anwendung des Codes enthält das Arbeitsblatt ungeordnete Daten.

**Eingabe: unsortierte Daten** 

![todo:image_alt_text](working-with-worksheets-gridweb_8.png)

Nach Ausführung des Codes sind die Daten in aufsteigender Reihenfolge sortiert.

**Ausgabe: Daten von oben nach unten in aufsteigender Reihenfolge sortiert** 

![todo:image_alt_text](working-with-worksheets-gridweb_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromtoptobottomascendingorder-datasortedfromtoptobottomascendingorder.jsp" >}}

### **Von links nach rechts**

Um Daten von links nach rechts zu sortieren:

1. Fügen Sie die Aspose.Cells.GridWeb-Steuerung Ihrem Webformular hinzu.
1. Greifen Sie auf das Arbeitsblatt zu, das Sie sortieren möchten.
1. Sortieren Sie den Datenbereich in beliebiger Reihenfolge (aufsteigend oder absteigend). Stellen Sie sicher, dass Sie von links nach rechts auswählen.

Das folgende Beispiel sortiert Daten in zwei Zeilen (Schüler-ID und Schülername) in aufsteigender Reihenfolge. Es werden nur zwei Zeilen mit vier Spalten von links nach rechts sortiert.

Vor der Anwendung des Codes enthält das Arbeitsblatt ungeordnete Daten.

**Eingabe: unsortierte Daten vor Ausführung des Code-Snippets** 

![todo:image_alt_text](working-with-worksheets-gridweb_10.png)

Nach Ausführen des Codes werden die Daten in aufsteigender Reihenfolge sortiert.

**Ausgabe: Daten von links nach rechts in aufsteigender Reihenfolge sortiert** 

![todo:image_alt_text](working-with-worksheets-gridweb_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromleftrightascendingorder-datasortedfromleftrightascendingorder.jsp" >}}

## **Suchen und Ersetzen**

Einer der schnellsten Wege, wiederholte Änderungen in einer großen Tabellenkalkulation vorzunehmen, besteht darin, die Suchen-und-Ersetzen-Funktion zu verwenden. Die Suchfunktion hilft Ihnen dabei, einen Textstring oder Daten zu finden, und die Ersetzen-Funktion ersetzt diesen durch einen neuen Wert. Aspose.Cells.GridWeb bietet diese Funktion. Sie ermöglicht es Ihnen, clientseitig nach einem spezifischen Textstring oder Wert zu suchen und diesen durch einen einfachen Dialog zu ersetzen. Sie ermöglicht es Ihnen sogar, nach Teildaten zu suchen.

### **Der Suchen/Ersetzen-Dialog**

Es gibt zwei Möglichkeiten, den Suchen/Ersetzen-Dialog zu öffnen:

1. Wenn die Steuerung aktiv ist, drücken Sie **STRG+F**, um den Dialog zu öffnen, oder drücken Sie die **STRG+R**-Taste, um den Dialog mit der **Ersetzen**-Schaltfläche zu öffnen.
1. Bewegen Sie den Cursor in den Zellenbereich des Arbeitsblatts, dann klicken Sie mit der rechten Maustaste. Wählen Sie **Suchen** oder **Ersetzen** aus dem Menü.

**Auswählen von Suchen**

![todo:image_alt_text](working-with-worksheets-gridweb_12.png)

Ein Suchen-und-Ersetzen-Dialogfeld wird angezeigt.

**Der Suchen/Ersetzen-Dialog**

![todo:image_alt_text](working-with-worksheets-gridweb_13.png)

**Mit Finden**

Um zu suchen:

1. Öffnen Sie den Suchen/Ersetzen-Dialog.
1. Geben Sie den Text ein, den Sie im Feld „Suchen nach“ suchen möchten.
1. Klicken Sie auf „Weitersuchen“, um zu suchen.

Die nächste Zelle, die Ihrer Suchbedingung entspricht, wird hervorgehoben.

{{% alert color="primary" %}}

Wenn Ihr Suchkriterium nicht gefunden wird, wird ein Dialog angezeigt, um Sie zu informieren.

{{% /alert %}}

### **Suchoptionen**

Es gibt einige Suchoptionen, die Sie im Dialog anpassen können. Die Tabelle unten listet sie auf.

|**Nr.**|**Optionsname**|**Beschreibung**|
| :- | :- | :- |
|1|Groß-/Kleinschreibung beachten|Gibt an, ob bei der Suche die Groß-/Kleinschreibung berücksichtigt werden soll.|
|2|Ganzes Wort passen|Gibt an, ob das ganze Wort bei der Suche übereinstimmen soll.|
|3|Nach oben suchen|Gibt an, ob die Suche von unten nach oben durchgeführt wird.|
|4|Regulärer Ausdruck|Wenn aktiviert, behandelt das Steuerelement den Text im Feld „Suchen nach“ als regulären Ausdruck im Suchvorgang.|
|5|In Formeln/Werten suchen|Wenn „Formeln“ ausgewählt ist, vergleicht das Steuerelement die Formel oder den nicht formatierten Wert der Zellen, falls die Formel oder der nicht formatierte Wert vorhanden ist. Wenn „Werte“ ausgewählt ist, wird nur der angezeigte Wert der Zellen verglichen.|

### **Verwenden von Ersetzen**

Zum Ersetzen von Text oder Werten:

1. Öffnen Sie das Dialogfeld „Suchen/Ersetzen“, indem Sie **STRG+F** drücken, oder klicken Sie mit der rechten Maustaste auf eine Zelle und wählen Sie **Suchen** aus, bevor Sie auf **Ersetzen** klicken.
1. Geben Sie den Ersatztext im Feld „Ersetzen durch“ ein.
1. Klicken Sie auf **Ersetzen**.

Um Text zu ersetzen:

1. Öffnen Sie das Dialogfeld.
1. Geben Sie den Text ein, den Sie im Feld „Suchen nach“ finden möchten, und den Text, den Sie im Feld „Ersetzen durch“ ersetzen möchten.
1. Ersetzen Sie jeweils ein Vorkommen, indem Sie zuerst auf **Weitersuchen** und dann auf **Ersetzen** klicken.
1. Wenn Sie sehr sicher sind, was sich auf dem Arbeitsblatt befindet, klicken Sie auf **Alle ersetzen**.

{{% alert color="primary" %}}

Wenn sich das Arbeitsblatt nicht im Bearbeitungsmodus befindet, wird die Schaltfläche „Ersetzen“ nicht angezeigt.

{{% /alert %}}

## Hyperlinks von der Clientseite hinzufügen/entfernen

Aspose.Cells GridWeb unterstützt jetzt das Hinzufügen und Entfernen von Hyperlinks von der Clientseite. Dafür bietet die API die Funktionen "addCelllink" und "delCelllink". Der folgende Code-Demonstrationsausschnitt zeigt das Hinzufügen und Entfernen von Hyperlinks von der Clientseite in GridWeb.

### Beispielcode

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-1.jsp" >}}

Sie können auch zu einem Blatt verlinken, indem Sie den folgenden Codeausschnitt verwenden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-2.jsp" >}}

## Schriftart-Einstellungen von der Clientseite aktualisieren

Aspose.Cells GridWeb unterstützt jetzt das Ändern von Schriftarteinstellungen von der Clientseite. Dafür bietet die API folgende Funktionen:

- **updateCellFontStyle**: Parameter - r/i/b/ib für normal/kursiv/fett/kursiv&&fett
- **updateCellFontSize**: Parameter - schriftnamen, usw. 'System'
- **updateCellFontName**: Parameter - schriftgröße, usw. '12pt'
- **updateCellFontColor**: Parameter - keine/u/l/ul/ für keine/unterstreichen/durchgestrichen/unterstreichen&&durchgestrichen
- **updateCellFontLine**: Parameter - HTML-Farbe wie #aa22ee oder bekannte Farbnamen wie grün, rot,...
- **updateCellBackGroundColor**: Parameter - HTML-Farbe wie #aa22ee oder bekannte Farbnamen wie grün, rot,...

Der folgende Code-Demonstrationsausschnitt zeigt das Ändern von Schriftarteinstellungen von der Clientseite in GridWeb.

### Beispielcode

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-update_font_from_client_side-1.jsp" >}}

## Kommentare von der Clientseite hinzufügen/entfernen

Aspose.Cells GridWeb unterstützt jetzt das Hinzufügen und Entfernen von Kommentaren von der Clientseite. Dafür bietet die API die Funktionen "addcomments" und "delcomments". Der folgende Code-Demonstrationsausschnitt zeigt das Hinzufügen und Entfernen von Kommentaren von der Clientseite in GridWeb.

### Beispielcode

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add_remove_comments_from_client_side.jsp" >}}

## Schaltflächen zum Hinzufügen/Entfernen von Arbeitsblättern anzeigen

Aspose.Cells GridWeb unterstützt jetzt das Hinzufügen und Entfernen von Blättern durch Verwenden von Schaltflächen in der Symbolleiste. Damit die Schaltflächen auf der Benutzeroberfläche sichtbar sind, müssen Sie **GridWeb1.ShowAddButton** auf **true** setzen. Der folgende Codeausschnitt zeigt das Hinzufügen von Hinzufügen/Entfernen-Schaltflächen zur GridWeb-Symbolleiste.

### Beispielcode

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "GridWeb-show_add_remove_worksheet_buttons.java" >}}
