---
title: Datenformatierung
type: docs
weight: 80
url: /de/java/data-formatting/
---

## **Ansätze zur Formatierung von Daten in Zellen**
Es ist allgemein bekannt, dass es für die Benutzer einfacher wird, den Inhalt (Daten) der Zellen zu lesen, wenn die Arbeitsblattzellen ordnungsgemäß formatiert sind. Es gibt viele Möglichkeiten, Zellen und ihren Inhalt zu formatieren. Der einfachste Weg besteht darin, Zellen unter Verwendung von Microsoft Excel in einer WYSIWYG-Umgebung zu formatieren, während Sie ein Designer-Arbeitsblatt erstellen. Nachdem das Designer-Arbeitsblatt erstellt wurde, können Sie das Arbeitsblatt unter Verwendung von Aspose.Cells öffnen und alle Formatierungseinstellungen mit dem Arbeitsblatt speichern. Ein weiterer Weg, Zellen und ihren Inhalt zu formatieren, besteht darin, die Aspose.Cells-API zu verwenden. In diesem Thema beschreiben wir zwei Ansätze zur Formatierung von Zellen und ihrem Inhalt unter Verwendung der Aspose.Cells-API.
### **Formatierung von Zellen**
Entwickler können Zellen und ihren Inhalt unter Verwendung der flexiblen API von Aspose.Cells formatieren. Aspose.Cells bietet eine Klasse, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), die eine Microsoft Excel-Datei darstellt. Die [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-Klasse enthält eine [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection), die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-Klasse dargestellt. Die [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-Klasse bietet eine Zellenkollektion. Jedes Element in der [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells)-Kollektion stellt ein Objekt der **Cell**-Klasse dar.

Aspose.Cells bietet die [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)-Eigenschaft in der [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)-Klasse, die zur Festlegung des Formatierungsstils einer Zelle verwendet wird. Darüber hinaus bietet Aspose.Cells auch eine [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)-Klasse, die für den gleichen Zweck verwendet wird. Wenden Sie verschiedene Arten von Formatierungsstilen auf die Zellen an, um ihre Hintergrund- oder Vordergrundfarben, Rahmen, Schriftarten, horizontale und vertikale Ausrichtungen, Einzugsebene, Textausrichtung, Drehwinkel und vieles mehr festzulegen.
#### **Verwendung der setStyle Methode**
Wenn verschiedene Formatierungsstile auf verschiedene Zellen angewendet werden, ist es besser, die setStyle-Methode der [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)-Klasse zu verwenden. Ein Beispiel wird unten gegeben, um die Verwendung der setStyle-Methode zur Anwendung verschiedener Formatierungseinstellungen auf eine Zelle zu demonstrieren.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formatting-FormattingCellsUsingsetStyleMethod-1.java" >}}




#### **Verwendung des Style-Objekts**
Bei der Anwendung desselben Formatierungsstils auf unterschiedliche Zellen verwenden Sie das [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)-Objekt.

1. Fügen Sie der Styles-Sammlung der [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-Klasse ein [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)-Objekt hinzu, indem Sie die createStyle-Methode der Workbook-Klasse aufrufen.
1. Greifen Sie auf das neu hinzugefügte Style-Objekt aus der Styles-Sammlung zu.
1. Legen Sie die gewünschten Eigenschaften des Style-Objekts fest, um die gewünschten Formatierungseinstellungen anzuwenden.
1. Weisen Sie das konfigurierte Style-Objekt der Style-Eigenschaft einer beliebigen gewünschten Zelle zu.

Dieser Ansatz kann die Effizienz Ihrer Anwendungen erheblich verbessern und auch Speicherplatz sparen.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingCellsUsingStyleObject-FormattingCellsUsingStyleObject.java" >}}




#### **Anwendung von Verlaufsfülleffekten**
Um die gewünschten Verlaufsfülleffekte auf die Zelle anzuwenden, verwenden Sie die Methode setTwoColorGradient des Style-Objekts entsprechend.
#### **Codebeispiel**
Der folgende Output wird durch Ausführen des untenstehenden Codes erzielt. 

**Verlaufsfülleffekte anwenden** 

![todo:image_alt_text](data-formatting_1.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ApplyGradientFillEffects-ApplyGradientFillEffects.java" >}}




## **Konfigurieren von Ausrichtungseinstellungen**
Jeder, der Microsoft Excel verwendet hat, um Zellen zu formatieren, wird mit den Ausrichtungseinstellungen in Microsoft Excel vertraut sein.

**Ausrichtungseinstellungen in Microsoft Excel** 

![todo:image_alt_text](data-formatting_2.png)

Wie Sie aus der obigen Abbildung sehen können, gibt es verschiedene Arten von Ausrichtungsoptionen:

- [Textausrichtung](/cells/de/java/data-formatting/) (horizontal & vertikal)
- [Einzug](/cells/de/java/data-formatting/)
- [Orientierung](/cells/de/java/data-formatting/)
- [Textsteuerung](/cells/de/java/data-formatting/)
- [Textrichtung](/cells/de/java/data-formatting/)

Alle diese Ausrichtungseinstellungen werden vollständig von Aspose.Cells unterstützt und werden im Folgenden näher erläutert.
### **Konfigurieren von Ausrichtungseinstellungen**
Aspose.Cells bietet eine Klasse, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), die eine Excel-Datei repräsentiert. Die Workbook-Klasse enthält eine WorksheetCollection, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-Klasse repräsentiert.

Die Worksheet-Klasse bietet eine Cells-Sammlung. Jedes Element in der Cells-Sammlung stellt ein Objekt der [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)-Klasse dar.

Aspose.Cells bietet die setStyle-Methode in der [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)-Klasse, die zur Formatierung einer Zelle verwendet wird. Die [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)-Klasse bietet nützliche Eigenschaften zur Konfiguration von Schriftarteinstellungen.

Wählen Sie einen Textausrichtungstyp mit Hilfe der Enumeration TextAlignmentType aus. Die vordefinierten Textausrichtungstypen in der Enumeration TextAlignmentType sind:

|**Textausrichtungstypen**|**Beschreibung**|
| :- | :- |
|Bottom|Stellt die untere Textausrichtung dar
|Center|Stellt die zentrale Textausrichtung dar
|CenterAcross|Stellt die zentrale überkreuzte Textausrichtung dar
|Distributed|Stellt die verteilte Textausrichtung dar
|Fill|Stellt die Fülltextausrichtung dar
|General|Stellt die allgemeine Textausrichtung dar
|Justify|Stellt die Textausrichtung als blocksatz dar
|Left|Stellt die linksbündige Textausrichtung dar
|Right|Stellt die rechtsbündige Textausrichtung dar
|Top|Stellt die obere Textausrichtung dar
{{% alert color="primary" %}} 

Mit der Methode Style.setJustifyDistributed() kann auch die Blocksatzverteilung angewendet werden.

{{% /alert %}} 
#### **Horizontale Ausrichtung**
Verwenden Sie die setHorizontalAlignment-Methode des [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)-Objekts, um den Text horizontal auszurichten.

Der folgende Ausgabetext wird durch Ausführen des unten stehenden Beispielcodes erzielt:

**Text horizontal ausrichten** 

![todo:image_alt_text](data-formatting_3.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentHorizontal-TextAlignmentHorizontal.java" >}}




#### **Vertikale Ausrichtung**
Verwenden Sie die setVerticalAlignment-Methode des [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)-Objekts, um den Text vertikal auszurichten.

Die folgende Ausgabe wird erzielt, wenn VerticalAlignment auf zentriert gesetzt ist.

**Text vertikal ausrichten** 

![todo:image_alt_text](data-formatting_4.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentVertical-TextAlignmentVertical.java" >}}




### **Einrückung**
Es ist möglich, die Einzugsebene des Textes in einer Zelle festzulegen, indem die Methode setIndentLevel des [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)-Objekts verwendet wird.

Das folgende Ergebnis wird erzielt, wenn IndentLevel auf 2 gesetzt wird.

**Einzugsebene auf 2 angepasst** 

![todo:image_alt_text](data-formatting_5.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Indentation-ImportingfromResultSet.java" >}}




### **Ausrichtung**
Legen Sie die Ausrichtung (Rotation) des Textes in einer Zelle mit der Methode setRotationAngle des [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)-Objekts fest.

Das folgende Ergebnis wird erzielt, wenn der Rotationswinkel auf 25 gesetzt wird.

**Rotationswinkel auf 25 eingestellt** 

![todo:image_alt_text](data-formatting_6.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Orientation-Orientation.java" >}}




### **Textsteuerung**
Im Folgenden wird erläutert, wie Sie Text steuern können, indem Sie Textrahmen, Anpassung an die Größe und andere Formatierungsoptionen festlegen.
#### **Textumschlag**
Textumbruch in einer Zelle erleichtert das Lesen: Die Höhe der Zelle passt sich an, um den gesamten Text aufzunehmen, anstatt ihn abzuschneiden oder in benachbarte Zellen zu überlaufen.

Legen Sie den Textumbruch mit der Methode setTextWrapped des [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)-Objekts auf Ein oder Aus.

Das folgende Ergebnis wird erzielt, wenn der Textumbruch aktiviert ist.

**Text innerhalb der Zelle umgebrochen** 

![todo:image_alt_text](data-formatting_7.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WrapText-WrapText.java" >}}




#### **Anpassen an Größe**
Eine Option zum Umbringen von Text in einem Feld besteht darin, die Textgröße an die Zellendimensionen anzupassen. Dies wird durch Festlegen der Eigenschaft IsTextWrapped des [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)-Objekts auf **true** erreicht.

Das folgende Ergebnis wird erzielt, wenn der Text an die Zelle angepasst wird.

**Text an die Begrenzungen der Zelle angepasst** 

![todo:image_alt_text](data-formatting_8.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ShrinkingToFit-ShrinkingToFit.java" >}}




#### **Zellen zusammenführen**
Wie Microsoft Excel unterstützt auch Aspose.Cells das Zusammenführen mehrerer Zellen zu einer einzigen.

Das folgende Ergebnis wird erzielt, wenn die drei Zellen in der ersten Zeile zusammengeführt werden, um eine große einzelne Zelle zu erstellen.

**Drei Zellen zusammengeführt, um eine große Zelle zu erstellen** 

![todo:image_alt_text](data-formatting_9.png)

Verwenden Sie die Merge-Methode der [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells)-Sammlung, um Zellen zusammenzuführen. Die Merge-Methode benötigt folgende Parameter:

- Erste Zeile, die erste Zeile, von der aus das Zusammenführen beginnen soll.
- Erste Spalte, die erste Spalte, von der aus das Zusammenführen beginnen soll.
- Anzahl der Zeilen, die zusammengeführt werden sollen.
- Anzahl der Spalten, die zusammengeführt werden sollen.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MergingCellsInWorksheet-MergingCellsInWorksheet.java" >}}




### **Textausrichtung**
Es ist möglich, die Lesereihenfolge von Text in Zellen festzulegen. Die Lesereihenfolge ist die visuelle Reihenfolge, in der Zeichen, Wörter usw. angezeigt werden. Zum Beispiel ist Englisch eine von links nach rechts geschriebene Sprache, während Arabisch von rechts nach links geschrieben wird.

Die Leserichtung wird mit der TextDirection-Eigenschaft des [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)-Objekts festgelegt. Aspose.Cells bietet vordefinierte Textrichtungstypen in der TextDirectionType-Enumeration an.

|**Text Direction Types**|**Beschreibung**|
| :- | :- |
|Context|Die Lese-Reihenfolge, die mit der Sprache des ersten eingegebenen Zeichens übereinstimmt|
|LeftToRight|Lesereihenfolge von links nach rechts|
|RightToLeft|Lesereihenfolge von rechts nach links|






{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ChangeTextDirection-ChangeTextDirection.java" >}}





Das folgende Ergebnis wird erzielt, wenn die Leserichtung des Textes auf von rechts nach links festgelegt wird.

**Festlegen der Textleserichtung auf von rechts nach links** 

![todo:image_alt_text](data-formatting_10.png)
## **Formatieren ausgewählter Zeichen in einer Zelle**
[Umgang mit Schriftarten-Einstellungen](/cells/de/java/dealing-with-font-settings/) erklärte, wie Zellen formatiert werden, jedoch nur wie der Inhalt der gesamten Zellen formatiert wird. Was, wenn nur ausgewählte Zeichen formatiert werden sollen?

Aspose.Cells unterstützt diese Funktion. Dieser Artikel erläutert, wie Sie diese Funktion verwenden können.
### **Formatieren ausgewählter Zeichen**
Aspose.Cells bietet eine Klasse, [Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), die eine Microsoft Excel-Datei darstellt. Die Klasse Workbook enthält eine Arbeitsblättersammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) dargestellt. Die Klasse Arbeitsblatt bietet eine Zellenkollektion. Jedes Element in der Zellenkollektion stellt ein Objekt der Klasse [Zelle](https://reference.aspose.com/cells/java/com.aspose.cells/cell) dar.

Die Zellklasse bietet die Methode characters, die die folgenden Parameter annimmt, um einen Bereich von Zeichen in einer Zelle auszuwählen:

- **Start-Index**, der Index des Zeichens, von dem aus die Auswahl beginnen soll.
- **Anzahl der Zeichen**: Die Anzahl der ausgewählten Zeichen.

In der Ausgabedatei ist in der Zelle A1 das Wort 'Besuchen' mit der Standardschrift formatiert, aber 'Aspose!' ist fett und blau.

**Auswahl von formatierten Zeichen** 

![todo:image_alt_text](data-formatting_11.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}







{{% alert color="primary" %}} 

Wenn Sie daran interessiert sind, [einen Teil des Rich-Texts in einer [Zelle](/cells/de/java/access-and-update-the-portions-of-rich-text-of-cell/) zu formatieren, sollten Sie die Methoden Cell.getCharacters & Cell.setCharacters verwenden. Die Methode Cell.getCharacters dient zum Zugriff auf die Textteile und anschließend können Änderungen mithilfe der Methode Cell.setCharacters vorgenommen werden, während die **get**-Methode ein Array von FontSetting-Objekten zurückgibt, die manipuliert werden können, um verschiedene Eigenschaften wie Schriftart, Schriftfarbe, Fettschrift usw. festzulegen, und die **set**-Methode verwendet werden kann, um die Änderungen anzuwenden.

{{% /alert %}} 
## **Aktivieren von Arbeitsblättern und Aktivieren einer Zelle oder Auswahl eines Zellbereichs im Arbeitsblatt**
Manchmal müssen Sie ein bestimmtes Arbeitsblatt aktivieren, damit es das erste ist, das angezeigt wird, wenn jemand die Datei in Microsoft Excel öffnet. Möglicherweise müssen Sie auch eine bestimmte Zelle aktivieren, sodass die Bildlaufleisten zur aktiven Zelle scrollen, damit sie deutlich sichtbar ist. Aspose.Cells ist in der Lage, all diese genannten Aufgaben zu erledigen.

Ein aktives Arbeitsblatt ist das Blatt, an dem Sie in einer Arbeitsmappe arbeiten. Der Name auf der Registerkarte des aktiven Arbeitsblatts ist standardmäßig fett formatiert. Eine aktive Zelle hingegen ist die ausgewählte Zelle, in die Daten eingegeben werden, wenn Sie mit der Eingabe beginnen. Es kann jeweils nur eine Zelle aktiv sein. Die aktive Zelle ist von einem starken Rahmen umgeben, um sie gegenüber den anderen Zellen hervorzuheben. Aspose.Cells ermöglicht es auch, einen Bereich von Zellen im Arbeitsblatt auszuwählen.
### **Aktivieren eines Arbeitsblatts und Aktivieren einer Zelle**
Aspose.Cells bietet eine spezifische API für diese Aufgaben. Zum Beispiel ist die Methode WorksheetCollection.setActiveSheetIndex nützlich zum Setzen eines aktiven Arbeitsblatts. Ebenso wird die Methode Worksheet.setActiveCell zum Setzen und Abrufen einer aktiven Zelle in einem Arbeitsblatt verwendet.

Wenn Sie möchten, dass die horizontalen und vertikalen Bildlaufleisten zur Zeilen- und Spaltenindexposition scrollen, um beim Öffnen der Datei in Microsoft Excel eine gute Ansicht der ausgewählten Daten zu erhalten, verwenden Sie die Eigenschaften Worksheet.setFirstVisibleRow und Worksheet.setFirstVisibleColumn.

Im folgenden Beispiel wird gezeigt, wie ein Arbeitsblatt aktiviert und eine Zelle darin aktiviert wird. Die Bildlaufleisten werden verschoben, damit die 2. Zeile und die 2. Spalte als ihre erste sichtbare Zeile und Spalte erscheinen.

**Die Zelle B2 als aktive Zelle setzen** 

![todo:image_alt_text](data-formatting_12.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MakeCellActive-MakeCellActive.java" >}}




#### **Auswählen eines Zellbereichs im Arbeitsblatt**
Aspose.Cells bietet die Methode Worksheet.selectRange(int startRow, int startColumn, int totalRows, int totalColumns, bool removeOthers). Wenn der letzte Parameter - removeOthers - auf true gesetzt ist, werden andere Zell- oder Zellbereichsauswahlen im Blatt entfernt.

Im folgenden Beispiel wird gezeigt, wie man in einem aktiven Arbeitsblatt einen Zellbereich auswählt.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SelectRangeofCellsinWorksheet-SelectRangeofCellsinWorksheet.java" >}}







{{% alert color="primary" %}} 

Alle oben genannten Klassen und Methoden sind in der lizenzierten Version von Aspose.Cells verfügbar.

{{% /alert %}} 
## **Formatieren von Zeilen und Spalten**
Das Formatieren von Zeilen und Spalten in einer Tabelle, um dem Bericht ein bestimmtes Aussehen zu verleihen, ist möglicherweise die am häufigsten verwendete Funktion der Excel-Anwendung. Aspose.Cells-APIs bieten diese Funktionalität ebenfalls durch ihr Datenmodell, indem sie die Klasse Style freigeben, die hauptsächlich alle mit dem Styling zusammenhängenden Funktionen wie Schriftart und ihre Attribute, Textausrichtung, Hintergrund-/Vordergrundfarben, Rahmen, Anzeigeformat für Zahlen & Datumsangaben usw. behandelt. Eine weitere nützliche Klasse, die die Aspose.Cells-APIs bereitstellen, ist die StyleFlag, die die Wiederverwendbarkeit des Style-Objekts ermöglicht. 

In diesem Artikel werden wir versuchen zu erklären, wie die Aspose.Cells for Java-API zur Formatierung von Zeilen und Spalten verwendet wird. 
### **Formatierung von Zeilen & Spalten**
Aspose.Cells bietet eine Klasse, [Workbook] (https://reference.aspose.com/cells/java/com.aspose.cells/workbook), die eine Microsoft Excel-Datei darstellt. Die Klasse [Workbook] (https://reference.aspose.com/cells/java/com.aspose.cells/workbook) enthält eine WorksheetCollection, die den Zugriff auf jede Arbeitsmappe in der Excel-Datei ermöglicht. Eine Arbeitsmappe wird durch die Klasse Worksheet dargestellt. Die Klasse [Worksheet] (https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) bietet die Cells-Sammlung. Die Zellenkollektion bietet eine Reihenkollektion.
#### **Formatierung einer Zeile**
Jedes Element in der Reihenkollektion stellt ein Reihenobjekt dar. Das Reihenobjekt bietet die applyStyle-Methode, um die Formatierung auf eine Zeile anzuwenden.

Um dieselbe Formatierung auf eine Zeile anzuwenden, verwenden Sie das Style-Objekt:

1. Fügen Sie der Klasse Workbook ein Style-Objekt hinzu, indem Sie ihre createStyle-Methode aufrufen.
1. Legen Sie die Eigenschaften des Style-Objekts fest, um die Formatierungseinstellungen anzuwenden.
1. Weisen Sie das konfigurierte Style-Objekt der applyStyle-Methode eines Reihenobjekts zu.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingARow-FormattingARow.java" >}}




#### **Formatierung einer Spalte**
Die Zellenkollektion bietet eine Spaltenkollektion. Jedes Element in der Spaltenkollektion stellt ein Spaltenobjekt dar. Ähnlich wie das Reihenobjekt bietet das Spaltenobjekt die applyStyle-Methode, die zur Formatierung einer Spalte verwendet wird. Verwenden Sie die applyStyle-Methode des Spaltenobjekts, um eine Spalte auf die gleiche Weise wie eine Zeile zu formatieren.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingAColumn-FormattingAColumn.java" >}}




#### **Einstellen des Anzeigeformats von Zahlen und Datum für Zeilen und Spalten**
Wenn die Anforderung darin besteht, das Anzeigeformat von Zahlen & Datum für eine komplette Zeile oder Spalte festzulegen, ist der Prozess mehr oder weniger dasselbe wie oben besprochen, jedoch anstatt Parameter für den textlichen Inhalt festzulegen, legen Sie das Format für Zahlen und Daten mithilfe von Style.Number oder Style.Custom fest. Bitte beachten Sie, dass die Style.Number-Eigenschaft vom Typ Integer ist und sich auf die integrierten Zahl- und Datumsformate bezieht, während die Style.Custom-Eigenschaft vom Typ String ist und die gültigen Muster akzeptiert.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingDisplayFormat-SettingDisplayFormat.java" >}}







{{% alert color="primary" %}} 

Bitte lesen Sie den ausführlichen Artikel zu [Einstellen von Anzeigeformaten von Zahlen und [Daten](/cells/de/java/data-formatting/).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
