---
title: Datenformatierung
type: docs
weight: 80
url: /de/java/data-formatting/
---
## **Ansätze zum Formatieren von Daten in Cells**
Es ist eine allgemeine Tatsache, dass es für die Benutzer einfacher wird, den Inhalt (Daten) der Zelle zu lesen, wenn die Arbeitsblattzellen richtig formatiert sind. Es gibt viele Möglichkeiten, Zellen und ihren Inhalt zu formatieren. Am einfachsten ist es, Zellen mit Microsoft Excel in einer WYSIWYG-Umgebung zu formatieren, während Sie eine Designer-Tabelle erstellen. Nachdem das Designer-Arbeitsblatt erstellt wurde, können Sie das Arbeitsblatt mit Aspose.Cells öffnen und alle Formateinstellungen beibehalten, die mit dem Arbeitsblatt gespeichert wurden. Eine andere Möglichkeit zum Formatieren von Zellen und deren Inhalten ist die Verwendung von Aspose.Cells API. In diesem Thema beschreiben wir zwei Ansätze zum Formatieren von Zellen und deren Inhalten mithilfe von Aspose.Cells API.
### **Formatierung Cells**
 Entwickler können Zellen und ihre Inhalte mit dem flexiblen API von Aspose.Cells formatieren. Aspose.Cells bietet eine Klasse,[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , die eine Microsoft Excel-Datei darstellt. Das[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse enthält a[Arbeitsblattsammlung](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse. Das[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse stellt eine Cells-Sammlung bereit. Jeder Artikel in der[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells)Sammlung stellt ein Objekt von dar**Cell** Klasse.

 Aspose.Cells bietet die[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) Eigentum in der[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) Klasse, die zum Festlegen des Formatierungsstils einer Zelle verwendet wird. Darüber hinaus bietet Aspose.Cells auch eine[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) Klasse, die dem gleichen Zweck dient. Wenden Sie verschiedene Arten von Formatierungsstilen auf die Zellen an, um ihre Hintergrund- oder Vordergrundfarben, Rahmen, Schriftarten, horizontale und vertikale Ausrichtung, Einzugsebene, Textrichtung, Drehwinkel und vieles mehr festzulegen.
#### **Verwenden der setStyle-Methode**
 Wenn Sie verschiedene Formatierungsstile auf verschiedene Zellen anwenden, ist es besser, die setStyle-Methode der zu verwenden[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) Klasse. Ein Beispiel wird unten gegeben, um die Verwendung der setStyle-Methode zu demonstrieren, um verschiedene Formatierungseinstellungen auf eine Zelle anzuwenden.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formatting-FormattingCellsUsingsetStyleMethod-1.java" >}}




#### **Verwenden des Style-Objekts**
 Wenn Sie denselben Formatierungsstil auf verschiedene Zellen anwenden, verwenden Sie die[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) Objekt.

1.  Füge hinzu ein[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) Objekt der Styles-Auflistung der[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse durch Aufrufen der createStyle-Methode der Workbook-Klasse.
1. Greifen Sie auf das neu hinzugefügte Style-Objekt aus der Styles-Auflistung zu.
1. Legen Sie die gewünschten Eigenschaften des Style-Objekts fest, um die gewünschten Formatierungseinstellungen anzuwenden.
1. Weisen Sie das konfigurierte Style-Objekt der Style-Eigenschaft einer beliebigen Zelle zu.

Dieser Ansatz kann die Effizienz Ihrer Anwendungen erheblich verbessern und auch Speicher sparen.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingCellsUsingStyleObject-FormattingCellsUsingStyleObject.java" >}}




#### **Anwenden von Verlaufsfülleffekten**
Um die gewünschten Verlaufsfülleffekte auf die Zelle anzuwenden, verwenden Sie die setTwoColorGradient-Methode des Style-Objekts entsprechend.
#### **Codebeispiel**
 Die folgende Ausgabe wird durch Ausführen des folgenden Codes erreicht.

**Anwenden von Verlaufsfülleffekten** 

![todo: Bild_alt_Text](data-formatting_1.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ApplyGradientFillEffects-ApplyGradientFillEffects.java" >}}




## **Ausrichtungseinstellungen konfigurieren**
Jeder, der Microsoft Excel zum Formatieren von Zellen verwendet hat, ist mit den Ausrichtungseinstellungen in Microsoft Excel vertraut.

**Ausrichtungseinstellungen in Microsoft Excel** 

![todo: Bild_alt_Text](data-formatting_2.png)

Wie Sie der obigen Abbildung entnehmen können, gibt es verschiedene Ausrichtungsoptionen:

- [Textausrichtung](/cells/de/java/data-formatting/) (Horizontal, Vertikal)
- [Vertiefung](/cells/de/java/data-formatting/).
- [Orientierung](/cells/de/java/data-formatting/).
- [Textsteuerung](/cells/de/java/data-formatting/).
- [Textrichtung](/cells/de/java/data-formatting/).

Alle diese Ausrichtungseinstellungen werden von Aspose.Cells vollständig unterstützt und unten ausführlicher erläutert.
### **Ausrichtungseinstellungen konfigurieren**
 Aspose.Cells bietet eine Klasse,[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , die eine Excel-Datei darstellt. Die Workbook-Klasse enthält eine WorksheetCollection, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse.

 Die Worksheet-Klasse stellt eine Cells-Sammlung bereit. Jeder Artikel in der Sammlung Cells repräsentiert ein Objekt der[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) Klasse.

Aspose.Cells stellt die setStyle-Methode in der[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) Klasse, die für die Formatierung einer Zelle verwendet wird. Das[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) -Klasse bietet nützliche Eigenschaften zum Konfigurieren von Schriftarteinstellungen.

Wählen Sie mithilfe der TextAlignmentType-Enumeration einen beliebigen Textausrichtungstyp aus. Die vordefinierten Textausrichtungstypen in der Aufzählung TextAlignmentType sind:

|**Textausrichtungstypen**|**Beschreibung**|
|:- |:- |
|Unterseite|Stellt die untere Textausrichtung dar|
|Center|Stellt die zentrierte Textausrichtung dar|
|CenterAcross|Stellt die Mitte über der Textausrichtung dar|
|Verteilt|Stellt die verteilte Textausrichtung dar|
|Füllen|Stellt die Fülltextausrichtung dar|
|Allgemein|Stellt die allgemeine Textausrichtung dar|
|Rechtfertigen|Stellt die Textausrichtung im Blocksatz dar|
|Links|Stellt die linke Textausrichtung dar|
|Recht|Stellt die rechte Textausrichtung dar|
|oben|Stellt die obere Textausrichtung dar|
{{% alert color="primary" %}} 

Sie können die verteilte Justify-Einstellung auch mithilfe der Style.setJustifyDistributed()-Methode anwenden.

{{% /alert %}} 
#### **Horizontale Ausrichtung**
 Verwenden Sie die[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) setHorizontalAlignment-Methode des Objekts, um den Text horizontal auszurichten.

Die folgende Ausgabe wird durch Ausführen des folgenden Beispielcodes erzielt:

**Horizontale Ausrichtung des Textes** 

![todo: Bild_alt_Text](data-formatting_3.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentHorizontal-TextAlignmentHorizontal.java" >}}




#### **Vertikale Ausrichtung**
 Verwenden Sie die[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) setVerticalAlignment-Methode des Objekts, um den Text vertikal auszurichten.

Die folgende Ausgabe wird erzielt, wenn VerticalAlignment auf center gesetzt ist.

**Text vertikal ausrichten** 

![todo: Bild_alt_Text](data-formatting_4.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentVertical-TextAlignmentVertical.java" >}}




### **Vertiefung**
 Es ist möglich, die Einzugsebene des Textes in einer Zelle festzulegen, indem Sie die verwenden[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) setIndentLevel-Methode des Objekts.

Die folgende Ausgabe wird erzielt, wenn IndentLevel auf 2 gesetzt ist.

**Einzugsstufe auf 2 angepasst** 

![todo: Bild_alt_Text](data-formatting_5.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Indentation-ImportingfromResultSet.java" >}}




### **Orientierung**
 Stellen Sie die Ausrichtung (Drehung) des Textes in einer Zelle mit ein[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) setRotationAngle-Methode des Objekts.

Die folgende Ausgabe wird erreicht, wenn der Drehwinkel auf 25 eingestellt ist.

**Drehwinkel auf 25 eingestellt** 

![todo: Bild_alt_Text](data-formatting_6.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Orientation-Orientation.java" >}}




### **Textsteuerung**
Im folgenden Abschnitt wird erläutert, wie Sie Text steuern, indem Sie Textumbruch, Anpassen verkleinern und andere Formatierungsoptionen festlegen.
#### **Textumbruch**
Das Umbrechen von Text in einer Zelle erleichtert das Lesen: Die Höhe der Zelle passt sich an den gesamten Text an, anstatt ihn abzuschneiden oder in benachbarte Zellen zu überlaufen.

 Stellen Sie den Textumbruch mit ein oder aus[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) setTextWrapped-Methode des Objekts.

Die folgende Ausgabe wird erzielt, wenn Textumbruch aktiviert ist.

**Text, der innerhalb der Zelle umbrochen wird** 

![todo: Bild_alt_Text](data-formatting_7.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WrapText-WrapText.java" >}}




#### **Schrumpfen, um zu passen**
 Eine Option zum Umbrechen von Text in einem Feld besteht darin, die Textgröße zu verkleinern, um sie an die Abmessungen einer Zelle anzupassen. Dies geschieht durch die Einstellung von[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) IsTextWrapped-Eigenschaft des Objekts auf**wahr**.

Die folgende Ausgabe wird erzielt, wenn Text verkleinert wird, um in die Zelle zu passen.

**Der Text wurde so verkleinert, dass er in die Grenzen der Zelle passt** 

![todo: Bild_alt_Text](data-formatting_8.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ShrinkingToFit-ShrinkingToFit.java" >}}




#### **Cells zusammenführen**
Wie Microsoft Excel unterstützt Aspose.Cells das Zusammenführen mehrerer Zellen zu einer.

Die folgende Ausgabe wird erzielt, wenn die drei Zellen in der ersten Zeile zu einer großen einzelnen Zelle zusammengeführt werden.

**Drei Zellen verschmolzen zu einer großen Zelle** 

![todo: Bild_alt_Text](data-formatting_9.png)

 Verwenden Sie die[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells) -Collection-Methode zum Zusammenführen von Zellen. Die Merge-Methode übernimmt die folgenden Parameter:

- Erste Reihe, die erste Reihe, ab der mit dem Zusammenführen begonnen werden soll.
- Erste Spalte, die erste Spalte, ab der mit dem Zusammenführen begonnen werden soll.
- Anzahl der Zeilen, die Anzahl der zusammenzuführenden Zeilen.
- Anzahl der Spalten, die Anzahl der zusammenzuführenden Spalten.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MergingCellsInWorksheet-MergingCellsInWorksheet.java" >}}




### **Textrichtung**
Es ist möglich, die Lesereihenfolge von Text in Zellen festzulegen. Die Lesereihenfolge ist die visuelle Reihenfolge, in der Zeichen, Wörter usw. angezeigt werden. Zum Beispiel ist Englisch eine Sprache von links nach rechts, während Arabisch eine Sprache von rechts nach links ist.

 Die Lesereihenfolge wird mit eingestellt[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) die TextDirection-Eigenschaft des Objekts. Aspose.Cells stellt vordefinierte Textrichtungstypen in der TextDirectionType-Enumeration bereit.

|**Textrichtungstypen**|**Beschreibung**|
|:- |:- |
|Kontext|Die Lesereihenfolge in Übereinstimmung mit der Sprache des ersten eingegebenen Zeichens|
|Links nach rechts|Lesereihenfolge von links nach rechts|
|Rechts nach links|Lesereihenfolge von rechts nach links|






{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ChangeTextDirection-ChangeTextDirection.java" >}}





Die folgende Ausgabe wird erreicht, wenn die Leserichtung des Textes auf rechts nach links eingestellt ist.

**Einstellen der Textlesereihenfolge von rechts nach links** 

![todo: Bild_alt_Text](data-formatting_10.png)
## **Ausgewählte Zeichen in Cell formatieren**
[Umgang mit Schrifteinstellungen](/cells/de/java/dealing-with-font-settings/)erklärt, wie man Zellen formatiert, aber nur, wie man den Inhalt der ganzen Zellen formatiert. Was ist, wenn Sie nur ausgewählte Zeichen formatieren möchten?

Aspose.Cells unterstützt diese Funktion. In diesem Thema wird die Verwendung dieser Funktion erläutert.
### **Ausgewählte Zeichen formatieren**
 Aspose.Cells bietet eine Klasse,[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , die eine Microsoft Excel-Datei darstellt. Die Workbook-Klasse enthält eine Worksheets-Auflistung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse. Die Worksheet-Klasse stellt eine Cells-Sammlung bereit. Jeder Artikel in der Sammlung Cells repräsentiert ein Objekt der[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) Klasse.

Die Klasse Cell stellt eine Zeichenmethode bereit, die die folgenden Parameter verwendet, um einen Bereich von Zeichen in einer Zelle auszuwählen:

- **Startindex**, der Index des Zeichens, ab dem die Auswahl beginnen soll.
- **Anzahl von Charakteren**, die Anzahl der auszuwählenden Zeichen.

In der Ausgabedatei ist in der Zelle „A1“ das Wort „Besuch“ mit der Standardschrift formatiert, aber „Aspose!“ ist fett und blau.

**Ausgewählte Zeichen formatieren** 

![todo: Bild_alt_Text](data-formatting_11.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}







{{% alert color="primary" %}} 

 Wenn du interessiert bist[Einen Teil von Rich Text in einer [Zelle] formatieren](/cells/de/java/access-and-update-the-portions-of-rich-text-of-cell/) , sollten Sie die Methoden Cell.getCharacters und Cell.setCharacters verwenden. Die Methode Cell.getCharacters muss verwendet werden, um auf die Teile des Textes zuzugreifen, und dann können Änderungen mit der Methode Cell.setCharacters vorgenommen werden, während die**bekommen** -Methode gibt ein Array von FontSetting-Objekten zurück, die manipuliert werden können, um verschiedene Eigenschaften Schriftartname, Schriftfarbe, Fettschrift usw. festzulegen**einstellen** -Methode verwendet werden, um die Änderungen anzuwenden.

{{% /alert %}} 
## **Aktivieren von Blättern und Aktivieren von Cell oder Wählen Sie einen Bereich von Cells im Arbeitsblatt aus**
Manchmal müssen Sie möglicherweise ein bestimmtes Arbeitsblatt aktivieren, damit es als erstes angezeigt wird, wenn jemand die Datei in Microsoft Excel öffnet. Möglicherweise müssen Sie auch eine bestimmte Zelle so aktivieren, dass die Bildlaufleisten zur aktiven Zelle scrollen, damit sie deutlich sichtbar ist. Aspose.Cells ist in der Lage, alle oben genannten Aufgaben zu erledigen.

Ein aktives Blatt ist das Blatt, an dem Sie in einer Arbeitsmappe arbeiten. Der Name auf der Registerkarte des aktiven Blatts ist standardmäßig fett. Eine aktive Zelle hingegen ist die Zelle, die ausgewählt ist und in die Daten eingegeben werden, wenn Sie mit der Eingabe beginnen. Es ist immer nur eine Zelle aktiv. Die aktive Zelle ist von einem dicken Rahmen umgeben, damit sie sich von den anderen Zellen abhebt. Mit Aspose.Cells können Sie auch einen Bereich von Zellen im Arbeitsblatt auswählen.
### **Aktivieren eines Blatts und Aktivieren einer Cell**
Aspose.Cells stellt für diese Aufgaben eine spezielle API zur Verfügung. Beispielsweise ist die WorksheetCollection.setActiveSheetIndex-Methode nützlich, um ein aktives Blatt festzulegen. In ähnlicher Weise wird die Worksheet.setActiveCell-Methode verwendet, um eine aktive Zelle in einem Arbeitsblatt festzulegen und abzurufen.

Wenn Sie möchten, dass die horizontalen und vertikalen Bildlaufleisten zur Zeilen- und Spaltenindexposition gescrollt werden, um eine gute Ansicht der ausgewählten Daten zu bieten, wenn die Datei in Microsoft Excel geöffnet wird, verwenden Sie die Eigenschaften Worksheet.setFirstVisibleRow und Worksheet.setFirstVisibleColumn.

Das folgende Beispiel zeigt, wie Sie ein Arbeitsblatt aktivieren und eine Zelle darin aktivieren. Die Bildlaufleisten werden gescrollt, um die 2. Zeile und 2. Spalte als ihre erste sichtbare Zeile und Spalte zu machen.

**Festlegen der B2-Zelle als aktive Zelle** 

![todo: Bild_alt_Text](data-formatting_12.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MakeCellActive-MakeCellActive.java" >}}




#### **Auswahl eines Bereichs von Cells im Arbeitsblatt**
Aspose.Cells bietet die Methode Worksheet.selectRange(int startRow, int startColumn, int totalRows, int totalColumns, bool removeOthers). Wenn Sie den letzten Parameter – removeOthers – auf „true“ setzen, werden andere Zell- oder Zellbereichsauswahlen im Blatt entfernt.

Das folgende Beispiel zeigt, wie Sie einen Zellbereich im aktiven Arbeitsblatt auswählen.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SelectRangeofCellsinWorksheet-SelectRangeofCellsinWorksheet.java" >}}







{{% alert color="primary" %}} 

Alle oben genannten Klassen und Methoden sind mit der lizenzierten Version von Aspose.Cells verfügbar.

{{% /alert %}} 
## **Zeilen und Spalten formatieren**
Das Formatieren der Zeilen und Spalten in einer Tabelle, um dem Bericht ein Aussehen zu verleihen, ist möglicherweise die am weitesten verbreitete Funktion der Excel-Anwendung. Aspose.Cells-APIs stellen diese Funktionalität auch über ihr Datenmodell bereit, indem sie die Style-Klasse verfügbar machen, die hauptsächlich alle Styling-bezogenen Funktionen wie Schriftart und ihre Attribute, Textausrichtung, Hintergrund-/Vordergrundfarben, Rahmen, Anzeigeformat für Zahlen und Datumsliterale usw. behandelt . Eine weitere nützliche Klasse, die Aspose.Cells-APIs bereitstellen, ist das StyleFlag, das die Wiederverwendbarkeit des Style-Objekts ermöglicht.

In diesem Artikel versuchen wir zu erklären, wie Sie Aspose.Cells for Java API verwenden, um Formatierungen auf Zeilen und Spalten anzuwenden.
### **Zeilen und Spalten formatieren**
 Aspose.Cells bietet eine Klasse,[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) das stellt eine Microsoft Excel-Datei dar. Das[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) -Klasse enthält eine WorksheetCollection, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Worksheet-Klasse dargestellt. Das[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse stellt die Sammlung Cells bereit. Die Cells-Sammlung stellt eine Rows-Sammlung bereit.
#### **Formatieren einer Zeile**
Jedes Element in der Rows-Auflistung repräsentiert ein Row-Objekt. Das Row-Objekt bietet die applyStyle-Methode, die zum Anwenden der Formatierung auf eine Zeile verwendet wird.

Um dieselbe Formatierung auf eine Zeile anzuwenden, verwenden Sie das Style-Objekt:

1. Fügen Sie der Workbook-Klasse ein Style-Objekt hinzu, indem Sie seine createStyle-Methode aufrufen.
1. Legen Sie die Eigenschaften des Style-Objekts fest, um die Formatierungseinstellungen anzuwenden.
1. Weisen Sie das konfigurierte Style-Objekt der applyStyle-Methode eines Row-Objekts zu.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingARow-FormattingARow.java" >}}




#### **Formatieren einer Spalte**
Die Sammlung Cells stellt eine Spaltensammlung bereit. Jedes Element in der Columns-Auflistung repräsentiert ein Column-Objekt. Ähnlich wie das Row-Objekt bietet das Column-Objekt die Methode applyStyle zum Festlegen der Spaltenformatierung. Verwenden Sie die applyStyle-Methode des Column-Objekts, um eine Spalte auf die gleiche Weise wie eine Zeile zu formatieren.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingAColumn-FormattingAColumn.java" >}}




#### **Festlegen des Anzeigeformats von Numbers und Daten für Zeilen und Spalten**
Wenn das Anzeigeformat von Zahlen und Datumsangaben für eine komplette Zeile oder Spalte festgelegt werden soll, ist der Vorgang mehr oder weniger der gleiche wie oben beschrieben, aber anstatt Parameter für den Textinhalt festzulegen, werden Sie die Formatierung für Zahlen festlegen und Datumsangaben mit Style.Number oder Style.Custom. Bitte beachten Sie, dass die Eigenschaft „Style.Number“ vom Typ „Integer“ ist und sich auf die integrierten Zahlen- und Datumsformate bezieht, während die Eigenschaft „Style.Custom“ vom Typ „String“ ist und die gültigen Muster akzeptiert.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingDisplayFormat-SettingDisplayFormat.java" >}}







{{% alert color="primary" %}} 

 Bitte lesen Sie den ausführlichen Artikel auf[Einstellen der Anzeigeformate von Numbers und [Datum]](/cells/de/java/data-formatting/).

{{% /alert %}}
