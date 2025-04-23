---
title: Seiteneinrichtungsfunktionen
type: docs
weight: 40
url: /de/java/page-setup-features/
---

Manchmal ist es notwendig, Seiteneinrichtungseinstellungen für Arbeitsblätter zu konfigurieren, um den Druck zu steuern. Diese Seiteneinrichtungseinstellungen bieten verschiedene Optionen.

**Seitenoptionen** 

![todo:image_alt_text](page-setup-features_1.png)

Seiteneinrichtungsoptionen werden in Aspose.Cells vollständig unterstützt. Dieser Artikel erklärt, wie Sie Seiteneinstellungen mit Aspose.Cells festlegen.

## **Seiteneinstellungen**

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), die eine Microsoft Excel-Datei repräsentiert. Die Arbeitsmappe-Klasse enthält eine Arbeitsblätter-Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) dargestellt.

Die Worksheet-Klasse bietet die PageSetup-Eigenschaft, die verwendet wird, um Seiteneinrichtungsoptionen festzulegen. Tatsächlich ist die PageSetup-Eigenschaft ein Objekt der PageSetup-Klasse, das es ermöglicht, Seiteneinrichtungsoptionen für ein gedrucktes Arbeitsblatt festzulegen. Die PageSetup-Klasse bietet verschiedene Eigenschaften, die verwendet werden, um Seiteneinrichtungsoptionen festzulegen. Einige dieser Eigenschaften werden unten erläutert.

### **Seitenausrichtung**

Die Seitenausrichtung kann mit der Methode [**setOrientation(PageOrientationType)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation) der Klasse [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) auf Hoch- oder Querformat eingestellt werden. Die Methode [**setOrientation(PageOrientationType)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation) verwendet die Aufzählung [**PageOrientationType**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType) als Parameter. Die Elemente der Aufzählung [**PageOrientationType**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType) sind unten aufgelistet.

|**Seitenausrichtungstypen**|**Beschreibung**|
| :- | :- |
|[**QUERFORMAT**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#LANDSCAPE)|Querformat|
|[**HOCHFORMAT**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#PORTRAIT)|Hochformat|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageOrientation-PageOrientation.java" >}}

### **Maßstab**

Es ist möglich, die Größe eines Arbeitsblatts durch Anpassen des Maßstabsfaktors mit der Methode [**setZoom**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Zoom) der Klasse [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) zu verkleinern oder zu vergrößern.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ScalingFactor-ScalingFactor.java" >}}

### **FitToPages-Optionen**

Um den Inhalt des Arbeitsblatts auf eine bestimmte Anzahl von Seiten anzupassen, verwenden Sie die Methoden [**setFitToPagesTall**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall) und [**setFitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide) der Klasse [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). Diese Methoden werden auch zum Skalieren von Arbeitsblättern verwendet.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FitToPagesOptions-FitToPagesOptions.java" >}}

### **Papierformat**

Legen Sie das Papierformat fest, auf das die Arbeitsblätter gedruckt werden sollen, mit der Eigenschaft [**PaperSize**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperSize) der Klasse [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). Die PaperSize-Eigenschaft akzeptiert einen der vordefinierten Werte in der Aufzählung [**PaperSizeType**](https://reference.aspose.com/cells/java/com.aspose.cells/PaperSizeType), die unten aufgeführt sind.

|**Papierformattypen**|**Beschreibung**|
| :- | :- |
|Paper10x14|10 in. x 14 in.|
|Paper11x17|11 in. x 17 in.|
|PaperA3|A3 (297 mm x 420 mm)|
|PaperA4|A4 (210 mm x 297 mm)|
|PaperA4Small|A4 Small (210 mm x 297 mm)|
|PaperA5|A5 (148 mm x 210 mm)|
|PaperB3|B3 (13.9 x 19.7 inches)|
|PaperB4|B4 (250 mm x 354 mm)|
|PaperB5|B5 (182 mm x 257 mm)|
|PaperBusinessCard|Business Card (90 mm x 55 mm)|
|PaperCSheet|C size sheet|
|PaperDSheet|D size sheet|
|PaperEnvelope10|Envelope #10 (4-1/8 in. x 9-1/2 in.)|
|PaperEnvelope11|Envelope #11 (4-1/2 in. x 10-3/8 in.)|
|PaperEnvelope12|Envelope #12 (4-1/2 in. x 11 in.)|
|PaperEnvelope14|Envelope #14 (5 in. x 11-1/2 in.)|
|PaperEnvelope9|Envelope #9 (3-7/8 in. x 8-7/8 in.)|
|PaperEnvelopeB4|Envelope B4 (250 mm x 353 mm)|
|PaperEnvelopeB5|Envelope B5 (176 mm x 250 mm)|
|PaperEnvelopeB6|Envelope B6 (176 mm x 125 mm)|
|PaperEnvelopeC3|Envelope C3 (324 mm x 458 mm)|
|PaperEnvelopeC4|Envelope C4 (229 mm x 324 mm)|
|PaperEnvelopeC5|Envelope C5 (162 mm x 229 mm)|
|PaperEnvelopeC6|Envelope C6 (114 mm x 162 mm)|
|PaperEnvelopeC65|Envelope C65 (114 mm x 229 mm)|
|PaperEnvelopeDL|Envelope DL (110 mm x 220 mm)|
|PaperEnvelopeItaly|Envelope Italy (110 mm x 230 mm)|
|PaperEnvelopeMonarch|Envelope Monarch (3-7/8 in. x 7-1/2 in.)|
|PaperEnvelopePersonal|Envelope (3-5/8 in. x 6-1/2 in.)|
|PaperESheet|E size sheet|
|PaperExecutive|Executive (7-1/2 in. x 10-1/2 in.)|
|PaperFanfoldLegalGerman|German Legal Fanfold (8-1/2 in. x 13 in.)|
|PaperFanfoldStdGerman|German Standard Fanfold (8-1/2 in. x 12 in.)|
|PaperFanfoldUS|U.S. Standard Fanfold (14-7/8 in. x 11 in.)|
|PaperFolio|Folio (8-1/2 in. x 13 in.)|
|PaperLedger|Ledger (17 in. x 11 in.)|
|PaperLegal|Legal (8-1/2 in. x 14 in.)|
|PaperLetter|Letter (8-1/2 in. x 11 in.)|
|PaperLetterSmall|Letter Small (8-1/2 in. x 11 in.)|
|PaperNote|Note (8-1/2 in. x 11 in.)|
|PaperQuarto|Quarto (215 mm x 275 mm)|
|PaperStatement|Statement (5-1/2 in. x 8-1/2 in.)|
|PaperTabloid|Tabloid (11 in. x 17 in.)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ManagePaperSize-ManagePaperSize.java" >}}

### **Druckqualität**

Legen Sie mit der Methode [**setPrintQuality**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintQuality) der Klasse [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) die Druckqualität der zu druckenden Arbeitsblätter fest. Die Maßeinheit für die Druckqualität sind Punkte pro Zoll (DPI).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintQuality-SetPrintQuality.java" >}}

### **Erste Seitenzahl**

Beginnen Sie mit der Numerierung der Arbeitsblattseiten mit der [**setFirstPageNumber**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FirstPageNumber) Methode der Klasse [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). Die setFirstPageNumber-Methode legt die Seitenzahl der ersten Arbeitsblattseite fest, und die folgenden Seiten werden in aufsteigender Reihenfolge nummeriert.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetFirstPageNumber-SetFirstPageNumber.java" >}}

## **Ränder einstellen**

Aspose.Cells unterstützt vollständig die Seiteneinrichtungsoptionen von Microsoft Excel. Entwickler müssen möglicherweise die Seiteneinrichtungseinstellungen für Arbeitsblätter konfigurieren, um den Druckprozess zu steuern. Dieses Thema erläutert, wie Sie Aspose.Cells verwenden, um die Seitennränder zu konfigurieren.

**Seitenränder in Microsoft Excel**

![todo:image_alt_text](page-setup-features_2.png)

Aspose.Cells bietet eine Klasse [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), die eine Microsoft Excel-Datei darstellt. Die Workbook-Klasse enthält die Arbeitsblattsammlung, die Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) repräsentiert.

Die Worksheet-Klasse bietet das PageSetup-Attribut, um Seiteneinrichtungsoptionen festzulegen. Das PageSetup-Attribut ist ein Objekt der Klasse [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup), das es ermöglicht, verschiedene Seitenlayoutoptionen für ein gedrucktes Arbeitsblatt festzulegen. Die PageSetup-Klasse bietet verschiedene Eigenschaften und Methoden zur Festlegung von Seiteneinrichtungsoptionen.

### **Seitenränder**

Legen Sie die Ränder (links, rechts, oben, unten) einer Seite mit Mitgliedern der Klasse [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) fest. Einige der zur Festlegung von Seitenrändern verwendeten Methoden sind unten aufgeführt:

- [**setLeftMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#LeftMargin)
- [**setRightMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#RightMargin)
- [**setTopMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#TopMargin)
- [**setBottomMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BottomMargin)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetMargins-SetMargins.java" >}}

### **In der Lage zu zentrieren etwas auf einer Seite horizontal und vertikal. Die Klasse {0} hat Mitglieder zu diesem Zweck: {1} und {2}.**

Es ist möglich, etwas auf einer Seite horizontal und vertikal zu zentrieren. Die Klasse [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) enthält Mitglieder für diesen Zweck: [**setCenterHorizontally**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterHorizontally) und [**setCenterVertically**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterVertically).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CenterOnPage-CenterOnPage.java" >}}

### **Kopf- und Fußzeilen Ränder**

Legen Sie Kopf- und Fußzeilenränder mit Mitgliedern von [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) wie [**setHeaderMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#HeaderMargin) und [**setFooterMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FooterMargin) fest.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HeaderAndFooterMargins-HeaderAndFooterMargins.java" >}}

## **Kopf- und Fußzeilen einstellen**

Kopf- und Fußzeilen sind die Text- und Bildabschnitte oberhalb des oberen Randes oder unterhalb des unteren Randes auf einer Seite. Es ist auch möglich, Kopf- und Fußzeilen zu Arbeitsblättern hinzuzufügen. Kopf- und Fußzeilen können verwendet werden, um verschiedene nützliche Informationen anzuzeigen, z.B. Seitenzahl, Autorname, Dokumenttitel oder Datum und Uhrzeit. Kopf- und Fußzeilen werden auch über den Seiteneinrichtungsdialog verwaltet.

**Der Seiteneinrichtungsdialog** 

![todo:image_alt_text](page-setup-features_3.png)

Aspose.Cells ermöglicht das Hinzufügen von Kopf- und Fußzeilen zu den Arbeitsblättern zur Laufzeit, aber es empfiehlt sich, dass Kopf- und Fußzeilen manuell in einer vorab gestalteten Datei für den Druck festgelegt werden. Sie können Microsoft Excel als GUI-Tool verwenden, um Kopf- und Fußzeilen einfach festzulegen, um die Entwicklungszeit zu verkürzen. Aspose.Cells kann die Datei importieren und diese Einstellungen beibehalten.

Um Kopf- und Fußzeilen zur Laufzeit hinzuzufügen, bietet Aspose.Cells spezielle Klassen und einige Skriptbefehle zur Formatsteuerung.

### **Skriptbefehle**

Skriptbefehle sind spezielle Befehle von Aspose.Cells, die es Entwicklern ermöglichen, Kopf- und Fußzeilen zu formatieren.

|**Skriptbefehle**|**Beschreibung**|
| :- | :- |
|&P|Die aktuelle Seitenzahl.|
|&G|Ein Bild.|
|&N|Die Gesamtzahl der Seiten.|
|&D|Das aktuelle Datum.|
|&T|Die aktuelle Zeit.|
|&A|Der Name des Arbeitsblatts.|
|&F|Der Dateiname ohne den Pfad.|
|&&Text|Zeigt &Text. Zum Beispiel: &&WO wird als &WO angezeigt|
|&"\<FontName>"|Ein Schriftartname. Zum Beispiel: &"Arial"|
|&"\<FontName>, \<FontStyle>"|Ein Schriftartname mit einem Stil. Zum Beispiel: &"Arial,Fett"|
|&\<FontSize>|Stellt die Schriftgröße dar. Zum Beispiel: “&14abc”. Wenn jedoch dieser Befehl von einer reinen Zahl gefolgt wird, die im Kopf gedruckt werden soll, sollte diese durch ein Leerzeichen von der Schriftgröße getrennt werden. Zum Beispiel: “&14 123”.|

### **Header und Fußzeilen festlegen**

Die [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)-Klasse bietet die Methode [**setHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeader-int-java.lang.String-) zum Hinzufügen eines Headers und [**setFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooter-int-java.lang.String-) zum Hinzufügen eines Footers zu einem Arbeitsblatt. Das Skript wird als Argument für alle oben genannten Methoden verwendet. Es repräsentiert das Skript, das für den Header oder Footer verwendet werden soll. Dieses Skript enthält Befehle zum Formatieren von Headern oder Footern.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetHeadersAndFooters-SetHeadersAndFooters.java" >}}

### **Fügen Sie eine Grafik in einen Header oder Footer ein.**

Die [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)-Klasse verfügt über die Methoden [**setHeadPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeaderPicture-int-byte[]-) und [**setFooterPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooterPicture-int-byte[]-) zum Hinzufügen von Bildern zu Kopf- und Fußzeilen eines Arbeitsblatts. Diese Methoden nehmen zwei Parameter:

- **Abschnitt**, der Bereich des Headers oder Footers, in dem das Bild platziert wird. Es gibt drei Abschnitte: links, zentriert und rechts, dargestellt durch die numerischen Werte 0, 1 und 2.
- **Datei-InputStream**, die grafischen Daten. Die binären Daten sollten in den Puffer eines Byte-Arrays geschrieben werden.

Nach Ausführen des Codes und Öffnen der Datei überprüfen Sie den Header des Arbeitsblatts in Microsoft Excel:

1. Wählen Sie im **Datei**-Menü **Seitenlayout**.
1. Wählen Sie im Dialogfeld Seitenlayout die Registerkarte **Kopfzeile/Fußzeile**.

**Einfügen einer Grafik in eine Kopfzeile/Fußzeile** 

![todo:image_alt_text](page-setup-features_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertImageInHeaderFooter-InsertImageInHeaderFooter.java" >}}

### **Fügen Sie eine Grafik nur in den Kopf der ersten Seite ein**

Die Klasse [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) hat auch andere nützliche Methoden, zum Beispiel [**setPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setPicture-boolean-boolean-boolean-int-byte[]-), [**setFirstPageHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageHeader-int-java.lang.String-), [**setFirstPageFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageFooter-int-java.lang.String-), um Bilder in den Kopf/Fußzeile der ersten Seite eines Arbeitsblatts hinzuzufügen. Die erste Seite ist eine besondere Seite: es ist üblich, dass sie spezielle Informationen anzeigen soll, wie z.B. ein Firmenlogo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertGraphicinFirstPageHeaderOnly-InsertGraphicinFirstPageHeaderOnly.java" >}}

## **Druckoptionen einstellen**

Die Seiteneinrichtungseinstellungen von Microsoft Excel bieten verschiedene Druckoptionen (auch als Blattoptionen bezeichnet), mit denen Benutzer steuern können, wie Arbeitsblattseiten gedruckt werden. Diese Druckoptionen ermöglichen es Benutzern:

- Einen bestimmten Druckbereich auf einem Arbeitsblatt auswählen.
- Titel drucken.
- Gitternetzlinien drucken.
- Zeilen- und Spaltenüberschriften drucken
- Entwurfsqualität erreichen.
- Kommentare drucken.
- Zellenfehler drucken.
- Seiteneinteilung definieren.

Alle diese Druckoptionen werden unten angezeigt.

**Druck (Blatt) Optionen** 

![todo:image_alt_text](page-setup-features_5.png)

### **Druck- und Blattoptionen festlegen**

spose.Cells unterstützt alle von Microsoft Excel angebotenen Druckoptionen und Entwickler können diese Optionen für Arbeitsblätter mithilfe der Eigenschaften der Klasse [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) einfach konfigurieren. Wie diese Eigenschaften verwendet werden, wird unten genauer erläutert.

### **Druckbereich festlegen**

Standardmäßig umfasst nur der Druckbereich alle Bereiche des Arbeitsblatts, die Daten enthalten. Entwickler können einen spezifischen Druckbereich des Arbeitsblatts festlegen.

Um einen spezifischen Druckbereich auszuwählen, verwenden Sie die Eigenschaft [**setPrintArea**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintArea) der Klasse [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). Weisen Sie dieser Eigenschaft einen Zellenbereich zu, der den Druckbereich definiert.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintArea-SetPrintArea.java" >}}

### **Drucktitel festlegen**

Aspose.Cells ermöglicht es Ihnen, Zeilen- und Spaltenüberschriften auf allen Seiten eines gedruckten Arbeitsblatts zu wiederholen. Verwenden Sie dazu die Eigenschaften [**setPrintTitleColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleColumns) und [**setPrintTitleRows**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleRows) der Klasse [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup).

Die zu wiederholenden Zeilen oder Spalten werden durch Übergabe ihrer Zeilen- oder Spaltennummern definiert. Zum Beispiel werden Zeilen als $1:$2 und Spalten als $A:$B definiert.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintTitle-SetPrintTitle.java" >}}

### **Andere Druckoptionen festlegen**

Die Klasse [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) bietet auch mehrere andere Eigenschaften zur Festlegung allgemeiner Druckoptionen wie folgt:

- [**setPrintGridlines**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintGridlines), eine boolesche Eigenschaft, die definiert, ob Gitterlinien gedruckt oder nicht gedruckt werden.
- [*setPrintHeadings*](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintHeadings), eine boolesche Eigenschaft, die definiert, ob Zeilen- und Spaltenüberschriften gedruckt oder nicht gedruckt werden.
- [**setBlackAndWhite**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BlackAndWhite), eine boolesche Eigenschaft, die definiert, ob das Arbeitsblatt im Schwarz-Weiß-Modus gedruckt wird oder nicht.
- [**setPrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments), definiert, ob die Druckkommentare im Arbeitsblatt angezeigt werden oder am Ende des Arbeitsblatts.
- [**setPrintDraft**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintDraft), eine boolesche Eigenschaft, die definiert, ob das Arbeitsblatt in Entwurfsqualität gedruckt wird oder nicht.
- [**setPrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors), definiert, ob Zellenfehler wie angezeigt, leer, Bindestrich oder N/V gedruckt werden.

Um die Eigenschaften [**PrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments) und [**PrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors) festzulegen, bietet Aspose.Cells auch zwei Aufzählungen, [**PrintCommentsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType) und [**PrintErrorsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType), die vordefinierte Werte enthalten, die den Eigenschaften [**setPrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments) und [**setPrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors) jeweils zugewiesen werden.

Die vordefinierten Werte in der Aufzählung [**PrintCommentsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType) werden unten beschrieben.

|**Druckkommentartypen**|**Beschreibung**|
| :- | :- |
|[**PRINT_IN_PLACE**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT-IN-PLACE)|Gibt an, Kommentare so zu drucken, wie sie im Arbeitsblatt angezeigt werden.|
|[**PRINT_NO_COMMENTS**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT-NO-COMMENTS)|Gibt an, keine Kommentare zu drucken.|
|[**PRINT_SHEET_END**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT-SHEET-END)|Gibt an, Kommentare am Ende des Arbeitsblatts zu drucken.|

Die vordefinierten Werte der Aufzählung [**PrintErrorsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType) werden unten beschrieben.

|**Druckfehlertypen**|**Beschreibung**|
| :- | :- |
|[**PRINT_ERRORS_BLANK**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT-ERRORS-BLANK)|Gibt an, keine Fehler zu drucken.|
|[**PRINT_ERRORS_DASH**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT-ERRORS-DASH)|Gibt an, Fehler als "--" zu drucken.|
|[**PRINT_ERRORS_DISPLAYED**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT-ERRORS-DISPLAYED)|Gibt an, Fehler so wie angezeigt zu drucken.|
|[**PRINT_ERRORS_NA**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT-ERRORS-NA)|Gibt an, Fehler als "#N/A" zu drucken.|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-OtherPrintOptions-OtherPrintOptions.java" >}}

### **Seitenreihenfolge festlegen**

Die Klasse [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) bietet die Eigenschaft [**setOrder**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order), die verwendet wird, um die Reihenfolge mehrerer Seiten Ihres Arbeitsblatts festzulegen, die gedruckt werden sollen. Es gibt zwei Möglichkeiten, die Seiten wie folgt zu ordnen:

- **Zuerst nach unten** druckt alle Seiten nach unten, bevor irgendeine Seite rechts gedruckt wird.
- **Zuerst nach rechts** druckt Seiten von links nach rechts, bevor irgendeine Seite darunter gedruckt wird.

Aspose.Cells bietet eine Aufzählung, [**PrintOrderType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType), die alle vordefinierten Reihenfolgetypen enthält, die der Methode [**setOrder**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order) zugewiesen werden sollen.

Die vordefinierten Werte der [**PrintOrderType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType)-Aufzählung werden unten beschrieben.

|**Druckreihenfolgetypen**|**Beschreibung**|
| :- | :- |
|[**DOWN_THEN_OVER**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#DOWN-THEN-OVER)|Zuerst nach unten, dann nach rechts drucken.|
|[**OVER_THEN_DOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#OVER-THEN-DOWN)|Zuerst nach rechts, dann nach unten drucken.|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPageOrder-SetPageOrder.java" >}}

## **Entfernen Sie die vorhandenen Druckereinstellungen von Arbeitsblättern in der Excel-Datei**

Bitte lesen Sie diesen Artikel zu diesem Thema.

## **Erweiterte Themen**
- [Seitenformatierungs-Skalierungsfaktor berechnen](/cells/de/java/calculate-page-setup-scaling-factor/)
- [Seiteneinrichtungseinstellungen von der Quellarbeitsmappe in die Zieltabelle kopieren](/cells/de/java/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/)
- [Feststellen, ob die Papiergröße des Arbeitsblatts automatisch ist](/cells/de/java/determine-if-paper-size-of-worksheet-is-automatic/)
- [Papierbreite und -höhe aus den Seiteinstellungen des Arbeitsblatts abrufen](/cells/de/java/get-paper-width-and-height-from-pagesetup-of-worksheet/)
- [Benutzerdefinierte Papiergröße des Arbeitsblatts für die Darstellung implementieren](/cells/de/java/implement-custom-paper-size-of-worksheet-for-rendering/)
- [Seiteneinrichtungs- und Druckoptionen](/cells/de/java/page-setup-and-printing-options/)
- [Entfernen Sie die vorhandenen Druckereinstellungen von Arbeitsblättern in der Excel-Datei](/cells/de/java/remove-existing-printersettings-of-worksheets-in-excel-file/)
{{< app/cells/assistant language="java" >}}
