---
title: Seiteneinrichtungsfunktionen
type: docs
weight: 40
url: /de/java/page-setup-features/
---
Manchmal ist es erforderlich, Seiteneinrichtungseinstellungen für Arbeitsblätter zu konfigurieren, um den Druck zu steuern. Diese Seiteneinrichtungseinstellungen bieten verschiedene Optionen.

**Seitenoptionen** 

![todo: Bild_alt_Text](page-setup-features_1.png)

Seiteneinrichtungsoptionen werden in Aspose.Cells vollständig unterstützt. In diesem Artikel wird erläutert, wie Sie Seitenoptionen mit Aspose.Cells festlegen.

## **Seitenoptionen festlegen**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , die eine Microsoft Excel-Datei darstellt. Die Workbook-Klasse enthält eine Worksheets-Auflistung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse.

Die Worksheet-Klasse stellt die PageSetup-Eigenschaft bereit, die zum Festlegen von Seiteneinrichtungsoptionen verwendet wird. Tatsächlich ist die PageSetup-Eigenschaft ein Objekt der PageSetup-Klasse, das es ermöglicht, Seitenlayoutoptionen für ein gedrucktes Arbeitsblatt festzulegen. Die PageSetup-Klasse stellt verschiedene Eigenschaften bereit, die zum Festlegen von Seiteneinrichtungsoptionen verwendet werden. Einige dieser Eigenschaften werden unten diskutiert.

### **Seitenausrichtung**

 Die Seitenausrichtung kann mithilfe von auf Hoch- oder Querformat eingestellt werden[**Seiteneinrichtung**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) Klasse'[**setOrientation(PageOrientationType)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation) Methode. Das[**setOrientation(PageOrientationType)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation) Methode nimmt die[**Seitenausrichtungstyp**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType) Aufzählung als Parameter. Die Mitglieder der[**Seitenausrichtungstyp**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType)Aufzählung sind unten aufgeführt.

|**Seitenausrichtungstypen**|**Beschreibung**|
|:- |:- |
|[**LANDSCHAFT**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#LANDSCAPE)|Landschaftsorientierung|
|[**PORTRÄT**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#PORTRAIT)|Hochkant|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageOrientation-PageOrientation.java" >}}

### **Vergößerungsfaktor, Verkleinerungsfaktor**

 Es ist möglich, die Größe eines Arbeitsblatts zu verkleinern oder zu vergrößern, indem Sie den Skalierungsfaktor mit anpassen[**setZoom**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Zoom) Methode der[**Seiteneinrichtung**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) Klasse.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ScalingFactor-ScalingFactor.java" >}}

### **FitToPages-Optionen**

 Um den Inhalt des Arbeitsblatts auf eine bestimmte Anzahl von Seiten anzupassen, verwenden Sie die[**Seiteneinrichtung**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) Klasse'[**setFitToPagesTall**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall) und[**setFitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide) Methoden. Diese Methoden werden auch verwendet, um Arbeitsblätter zu skalieren.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FitToPagesOptions-FitToPagesOptions.java" >}}

### **Papier größe**

 Legen Sie die Papiergröße fest, auf die die Arbeitsblätter gedruckt werden, indem Sie die verwenden[**Seiteneinrichtung**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) Klasse'[**Papier größe**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperSize) Eigentum. Die PaperSize-Eigenschaft akzeptiert einen der vordefinierten Werte in der[**PaperSizeType**](https://reference.aspose.com/cells/java/com.aspose.cells/PaperSizeType) Aufzählung, unten aufgeführt.

|**Papierformattypen**|**Beschreibung**|
|:- |:- |
|Papier10x14|10 Zoll x 14 Zoll|
|Papier11x17|11 Zoll x 17 Zoll|
|PapierA3|A3 (297 mm x 420 mm)|
|PapierA4|A4 (210 x 297 mm)|
|PapierA4Klein|A4 klein (210 mm x 297 mm)|
|PapierA5|A5 (148 x 210 mm)|
|PapierB3|B3 (13,9 x 19,7 Zoll)|
|PapierB4|B4 (250 x 354 mm)|
|PapierB5|B5 (182 mm x 257 mm)|
|PapierVisitenkarte|Visitenkarte (90 mm x 55 mm)|
|PapierCSheet|Blatt in C-Größe|
|PaperDSheet|Blatt in D-Größe|
|Papierumschlag10|Umschlag Nr. 10 (4-1/8 Zoll x 9-1/2 Zoll)|
|Papierumschlag11|Umschlag Nr. 11 (4-1/2 Zoll x 10-3/8 Zoll)|
|Papierumschlag12|Umschlag Nr. 12 (4-1/2 Zoll x 11 Zoll)|
|Papierumschlag14|Umschlag Nr. 14 (5 Zoll x 11-1/2 Zoll)|
|Papierumschlag9|Umschlag Nr. 9 (3-7/8 Zoll x 8-7/8 Zoll)|
|PapierumschlagB4|Umschlag B4 (250 mm x 353 mm)|
|PapierumschlagB5|Umschlag B5 (176 mm x 250 mm)|
|PapierumschlagB6|Umschlag B6 (176 mm x 125 mm)|
|PapierumschlagC3|Umschlag C3 (324 mm x 458 mm)|
|PapierumschlagC4|Umschlag C4 (229 mm x 324 mm)|
|PapierumschlagC5|Umschlag C5 (162 mm x 229 mm)|
|PapierumschlagC6|Umschlag C6 (114 mm x 162 mm)|
|PapierumschlagC65|Umschlag C65 (114 mm x 229 mm)|
|PapierumschlagDL|Umschlag DL (110 mm x 220 mm)|
|PapierumschlagItalien|Briefumschlag Italien (110 mm x 230 mm)|
|PapierumschlagMonarch|Umschlag Monarch (3-7/8 Zoll x 7-1/2 Zoll)|
|PapierUmschlagPersönlich|Umschlag (3-5/8 Zoll x 6-1/2 Zoll)|
|PaperESheet|Blatt in E-Größe|
|PapierExecutive|Exekutive (7-1/2 Zoll x 10-1/2 Zoll)|
|PapierFanfoldImpressumDeutsch|Deutsches Legal Endlospapier (8-1/2 Zoll x 13 Zoll)|
|PapierFanfoldStdDeutsch|Deutscher Standard Endlospapier (8-1/2 Zoll x 12 Zoll)|
|PaperFanfoldUS|Endlosfaltung nach US-Standard (14-7/8 Zoll x 11 Zoll)|
|PaperFolio|Folio (8-1/2 Zoll x 13 Zoll)|
|PaperLedger|Hauptbuch (17 Zoll x 11 Zoll)|
|PapierLegal|Legal (8-1/2 Zoll x 14 Zoll)|
|Papierbrief|Letter (8-1/2 Zoll x 11 Zoll)|
|PaperLetterSmall|Letter Small (8-1/2 Zoll x 11 Zoll)|
|PaperNote|Hinweis (8-1/2 Zoll x 11 Zoll)|
|PapierQuarto|Quarto (215 mm x 275 mm)|
|Papierauszug|Erklärung (5-1/2 Zoll x 8-1/2 Zoll)|
|PapierTabloid|Tabloid (11 Zoll x 17 Zoll)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ManagePaperSize-ManagePaperSize.java" >}}

### **Druckqualität**

 Stellen Sie die Druckqualität der zu druckenden Arbeitsblätter mit ein[**Seiteneinrichtung**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) Klasse'[**setPrintQuality**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintQuality) Methode. Die Maßeinheit für die Druckqualität ist Punkte pro Zoll (DPI).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintQuality-SetPrintQuality.java" >}}

### **Erste Seitenzahl**

 Beginnen Sie die Nummerierung der Arbeitsblattseiten mit dem[**Seiteneinrichtung**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) Klasse'[**setFirstPageNumber**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FirstPageNumber) Methode. Die Methode setFirstPageNumber setzt die Seitennummer der ersten Arbeitsblattseite und die folgenden Seiten werden in aufsteigender Reihenfolge nummeriert.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetFirstPageNumber-SetFirstPageNumber.java" >}}

## **Ränder einstellen**

Aspose.Cells unterstützt die Seiteneinrichtungsoptionen von Microsoft Excel vollständig. Entwickler müssen möglicherweise Seiteneinrichtungseinstellungen für Arbeitsblätter konfigurieren, um den Druckprozess zu steuern. In diesem Thema wird erläutert, wie Sie Aspose.Cells verwenden, um Seitenränder zu konfigurieren.

**Seitenränder in Microsoft Excel**

![todo: Bild_alt_Text](page-setup-features_2.png)

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)das stellt eine Microsoft Excel-Datei dar. Die Workbook-Klasse enthält die Worksheets-Auflistung, die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse.

 Die Worksheet-Klasse stellt die PageSetup-Eigenschaft bereit, die zum Festlegen von Seiteneinrichtungsoptionen verwendet wird. Das PageSetup-Attribut ist ein Objekt der[**Seiteneinrichtung**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) -Klasse, die es ermöglicht, verschiedene Seitenlayoutoptionen für ein gedrucktes Arbeitsblatt festzulegen. Die PageSetup-Klasse stellt verschiedene Eigenschaften und Methoden bereit, die zum Festlegen von Seiteneinrichtungsoptionen verwendet werden.

### **Seitenränder**

 Stellen Sie die Ränder (links, rechts, oben, unten) einer Seite mit ein[**Seiteneinrichtung**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) Klassenmitglieder. Nachfolgend sind einige Methoden aufgeführt, die zum Festlegen von Seitenrändern verwendet werden:

- [**setLeftMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#LeftMargin)
- [**setRightMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#RightMargin)
- [**setTopMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#TopMargin)
- [**setBottomMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BottomMargin)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetMargins-SetMargins.java" >}}

### **Auf Seite zentrieren**

 Es ist möglich, etwas auf einer Seite horizontal und vertikal zu zentrieren. Das[**Seiteneinrichtung**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) Klasse hat Mitglieder für diesen Zweck:[**setCenterHorizontally**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterHorizontally) und[**setCenterVertical**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterVertically).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CenterOnPage-CenterOnPage.java" >}}

### **Kopf- und Fußzeilenränder**

Kopf- und Fußzeilenränder mit einstellen[**Seiteneinrichtung**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) Mitglieder wie z[**setHeaderMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#HeaderMargin) und[**setFooterMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FooterMargin).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HeaderAndFooterMargins-HeaderAndFooterMargins.java" >}}

## **Kopf- und Fußzeilen einstellen**

Kopf- und Fußzeilen sind die Text- und Bildabschnitte über dem oberen Rand oder unter dem unteren Rand einer Seite. Es ist auch möglich, Kopf- und Fußzeilen zu Arbeitsblättern hinzuzufügen. Kopf- und Fußzeilen können verwendet werden, um jede Art von nützlichen Informationen anzuzeigen, zum Beispiel Seitenzahl, Autorenname, Dokumenttitel oder Datum und Uhrzeit. Kopf- und Fußzeilen werden ebenfalls über das Dialogfeld „Seite einrichten“ verwaltet.

**Der Dialog Seite einrichten** 

![todo: Bild_alt_Text](page-setup-features_3.png)

Aspose.Cells ermöglicht das Hinzufügen von Kopf- und Fußzeilen zu den Arbeitsblättern zur Laufzeit, es wird jedoch empfohlen, Kopf- und Fußzeilen manuell in einer vorgefertigten Datei zum Drucken festzulegen. Sie können Microsoft Excel als GUI-Tool verwenden, um Kopf- und Fußzeilen einfach festzulegen, um die Entwicklungszeit zu verkürzen. Aspose.Cells kann die Datei importieren und diese Einstellungen reservieren.

Um Kopf- und Fußzeilen zur Laufzeit hinzuzufügen, bietet Aspose.Cells spezielle Klassen und einige Skriptbefehle zur Steuerung der Formatierung.

### **Skriptbefehle**

Skriptbefehle sind spezielle Befehle, die von Aspose.Cells bereitgestellt werden und es Entwicklern ermöglichen, Kopf- und Fußzeilen zu formatieren.

|**Skriptbefehle**|**Beschreibung**|
|:- |:- |
|&P|Die aktuelle Seitenzahl.|
|&G|Ein Bild.|
|&N|Die Gesamtzahl der Seiten.|
|&D|Das aktuelle Datum.|
|&T|Die aktuelle Zeit.|
|&EIN|Der Name des Arbeitsblatts.|
|&F|Der Dateiname ohne den Pfad.|
|&"\<FontName>"|Ein Schriftartname. Zum Beispiel: &"Arial"|
|&"\<FontName>, \<FontStyle>"|Ein Schriftartname mit einem Stil. Zum Beispiel: &"Arial,Fett"|
|&\<FontSize>|Stellt die Schriftgröße dar. Beispiel: „&14abc“. Wenn diesem Befehl jedoch eine einfache Zahl folgt, die in der Kopfzeile gedruckt werden soll, sollte diese mit einem Leerzeichen von der Schriftgröße getrennt werden. Beispiel: „&14 123“.|

### **Legen Sie Kopf- und Fußzeilen fest**

 Das[**Seiteneinrichtung**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) Klasse stellt Methode bereit[**setHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeader(int,%20java.lang.String) zum Hinzufügen einer Kopfzeile und[**setFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooter(int,%20java.lang.String)) zum Hinzufügen einer Fußzeile zu einem Arbeitsblatt. Das Skript wird als Argument für alle oben genannten Methoden verwendet. Es stellt das Skript dar, das für die Kopf- oder Fußzeile verwendet werden soll. Dieses Skript enthält Skriptbefehle zum Formatieren von Kopf- oder Fußzeilen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetHeadersAndFooters-SetHeadersAndFooters.java" >}}

### **Fügen Sie eine Grafik in eine Kopf- oder Fußzeile ein**

 Das[**Seiteneinrichtung**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) Klasse hat die Methoden[**setHeadPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeaderPicture(int,%20byte[]) ) und[**setFooterPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooterPicture(int,%20byte[])) zum Hinzufügen von Bildern zur Kopf- und Fußzeile eines Arbeitsblatts. Diese Methoden nehmen zwei Parameter:

- **Abschnitt**, der Abschnitt der Kopf- oder Fußzeile, in dem das Bild platziert wird. Es gibt drei Abschnitte: links, Mitte und rechts, dargestellt durch die numerischen Werte 0, 1 bzw. 2.
- **Datei InputStream**, die grafischen Daten. Die Binärdaten sollen in den Puffer eines Byte-Arrays geschrieben werden.

Nachdem Sie den Code ausgeführt und die Datei geöffnet haben, überprüfen Sie die Kopfzeile des Arbeitsblatts in Microsoft Excel:

1.  Auf der**Datei** Menü, auswählen**Seiteneinrichtung**.
1.  Wählen Sie im Dialogfeld Seite einrichten die aus**Kopfzeile Fußzeile** Tab.

**Einfügen einer Grafik in eine Kopf-/Fußzeile** 

![todo: Bild_alt_Text](page-setup-features_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertImageInHeaderFooter-InsertImageInHeaderFooter.java" >}}

### **Fügen Sie eine Grafik nur in die Kopfzeile der ersten Seite ein**

 Das[**Seiteneinrichtung**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) Die Klasse hat zum Beispiel auch andere nützliche Methoden[**setBild**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setPicture(boolean,%20boolean,%20boolean,%20int,%20byte[])), [**setFirstPageHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageHeader(int,%20java.lang.String)), [**setFirstPageFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageFooter(int,%20java.lang.String)), um Bilder in die Kopf-/Fußzeile der ersten Seite eines Arbeitsblatts einzufügen. Die erste Seite ist eine Sonderseite: Es ist üblich, dass sie spezielle Informationen zeigen soll, zum Beispiel ein Firmenlogo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertGraphicinFirstPageHeaderOnly-InsertGraphicinFirstPageHeaderOnly.java" >}}

## **Druckoptionen einstellen**

Microsoft Die Seiteneinrichtungseinstellungen von Excel bieten mehrere Druckoptionen (auch als Blattoptionen bezeichnet), mit denen Benutzer steuern können, wie Arbeitsblattseiten gedruckt werden. Mit diesen Druckoptionen können Benutzer:

- Wählen Sie einen bestimmten Druckbereich auf einem Arbeitsblatt aus.
- Titel drucken.
- Rasterlinien drucken.
- Zeilen- und Spaltenüberschriften drucken
- Erzielen Sie Entwurfsqualität.
- Kommentare drucken.
- Zellfehler drucken.
- Definieren Sie die Seitenreihenfolge.

Alle diese Druckoptionen sind unten aufgeführt.

**Druckoptionen (Blatt).** 

![todo: Bild_alt_Text](page-setup-features_5.png)

### **Einstellen von Druck- und Blattoptionen**

 spose.Cells unterstützt alle Druckoptionen, die von Microsoft Excel angeboten werden, und Entwickler können diese Optionen für Arbeitsblätter einfach konfigurieren, indem sie die von angebotenen Eigenschaften verwenden[**Seiteneinrichtung**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)Klasse. Wie diese Eigenschaften verwendet werden, wird unten ausführlicher erörtert.

### **Druckbereich festlegen**

Standardmäßig enthält nur der Druckbereich alle Bereiche des Arbeitsblatts, die Daten enthalten. Entwickler können einen bestimmten Druckbereich des Arbeitsblatts festlegen.

 Um einen bestimmten Druckbereich auszuwählen, verwenden Sie die[**Seiteneinrichtung**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) Klasse'[**setPrintArea**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintArea) Eigentum. Weisen Sie dieser Eigenschaft einen Zellbereich zu, der den Druckbereich definiert.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintArea-SetPrintArea.java" >}}

### **Drucktitel festlegen**

 Aspose.Cells ermöglicht es Ihnen, Zeilen- und Spaltenüberschriften festzulegen, die auf allen Seiten eines gedruckten Arbeitsblatts wiederholt werden sollen. Verwenden Sie dazu die[**Seiteneinrichtung**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) Klasse'[**setPrintTitleColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleColumns) und[**setPrintTitleRows**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleRows) Eigenschaften.

Die Zeilen oder Spalten, die wiederholt werden, werden durch die Übergabe ihrer Zeilen- oder Spaltennummern definiert. Beispielsweise werden Zeilen als $1:$2 und Spalten als $A:$B definiert.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintTitle-SetPrintTitle.java" >}}

### **Legen Sie andere Druckoptionen fest**

 Das[**Seiteneinrichtung**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) Die Klasse bietet auch mehrere andere Eigenschaften, um allgemeine Druckoptionen wie folgt festzulegen:

- [**setPrintGridlines**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintGridlines), eine boolesche Eigenschaft, die definiert, ob Gitternetzlinien gedruckt werden oder nicht.
- [*setPrintHeadings*](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintHeadings), eine boolesche Eigenschaft, die definiert, ob Zeilen- und Spaltenüberschriften gedruckt werden oder nicht.
- [**setBlackAndWhite**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BlackAndWhite), eine boolesche Eigenschaft, die definiert, ob das Arbeitsblatt im Schwarzweißmodus gedruckt werden soll oder nicht.
- [**setPrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments), legt fest, ob die Druckkommentare auf dem Arbeitsblatt oder am Ende des Arbeitsblatts angezeigt werden.
- [**setPrintDraft**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintDraft), eine boolesche Eigenschaft, die definiert, ob das Arbeitsblatt in Entwurfsqualität gedruckt werden soll oder nicht.
- [**setPrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors), definiert, ob Zellfehler als angezeigt, leer, Bindestrich oder N/A gedruckt werden.

 Zum Einstellen der[**Kommentare drucken**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments) und[**Druckfehler**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors) Eigenschaften, Aspose.Cells bietet auch zwei Aufzählungen,[**PrintCommentsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType) und[**PrintErrorsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType) die vordefinierte Werte enthalten, die dem zugewiesen werden[**setPrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments) und[**setPrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors) Eigenschaften bzw.

 Die vordefinierten Werte in der[**PrintCommentsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType) Aufzählung sind unten beschrieben.

|**Kommentartypen drucken**|**Beschreibung**|
|:- |:- |
|[**PRINT_IN_PLACE**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_IN_PLACE)|Gibt an, dass Kommentare so gedruckt werden, wie sie auf dem Arbeitsblatt angezeigt werden.|
|[**PRINT_NO_COMMENTS**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_NO_COMMENTS)|Gibt an, dass Kommentare nicht gedruckt werden.|
|[**PRINT_SHEET_END**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_SHEET_END)|Gibt an, dass Kommentare am Ende des Arbeitsblatts gedruckt werden.|

 Die vordefinierten Werte der[**PrintErrorsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType) Aufzählung sind unten beschrieben.

|**Druckfehlertypen**|**Beschreibung**|
|:- |:- |
|[*PRINT_ERRORS_BLANK*](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_BLANK)|Gibt an, Fehler nicht zu drucken.|
|[**PRINT_ERRORS_DASH**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_DASH)|Gibt an, dass Fehler als "--" gedruckt werden.|
|[**PRINT_ERRORS_DISPLAYED**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_DISPLAYED)|Gibt an, dass Fehler wie angezeigt gedruckt werden.|
|[**PRINT_ERRORS_NA**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_NA)|Gibt an, dass Fehler als „#N/A“ gedruckt werden.|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-OtherPrintOptions-OtherPrintOptions.java" >}}

### **Seitenreihenfolge festlegen**

 Das[**Seiteneinrichtung**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) Klasse bietet die[**setOrder**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order) -Eigenschaft, die verwendet wird, um mehrere Seiten Ihres Arbeitsblatts zum Drucken anzuordnen. Es gibt zwei Möglichkeiten, die Seiten wie folgt anzuordnen:

- **Runter dann vorbei** druckt alle Seiten nach unten, bevor Seiten nach rechts gedruckt werden.
- **Rüber dann runter** druckt Seiten von links nach rechts, bevor die darunter liegenden Seiten gedruckt werden.

 Aspose.Cells liefert eine Aufzählung,[**Druckauftragstyp**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType) , die alle vordefinierten Auftragstypen enthält, denen zugeordnet werden soll[**setOrder**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order) Methode.

 Die vordefinierten Werte von[**Druckauftragstyp**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType) Aufzählung sind unten beschrieben.

|**Auftragsarten drucken**|**Beschreibung**|
|:- |:- |
|[**DOWN_THEN_OVER**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#DOWN_THEN_OVER)|Drucke runter, dann rüber.|
|[**OVER_THEN_DOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#OVER_THEN_DOWN)|Drüber drucken, dann runter.|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPageOrder-SetPageOrder.java" >}}

## **Entfernen Sie vorhandene Druckereinstellungen von Arbeitsblättern in einer Excel-Datei**

Bitte lesen Sie diesen Artikel zu diesem Thema.

## **Themen vorantreiben**
- [Berechnen Sie den Skalierungsfaktor für die Seiteneinrichtung](/cells/de/java/calculate-page-setup-scaling-factor/)
- [Seiteneinrichtungseinstellungen aus dem Quellarbeitsblatt in das Zielarbeitsblatt kopieren](/cells/de/java/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/)
- [Stellen Sie fest, ob die Papiergröße des Arbeitsblatts automatisch ist](/cells/de/java/determine-if-paper-size-of-worksheet-is-automatic/)
- [Holen Sie sich die Papierbreite und -höhe von PageSetup des Arbeitsblatts](/cells/de/java/get-paper-width-and-height-from-pagesetup-of-worksheet/)
- [Implementieren Sie die benutzerdefinierte Papiergröße des Arbeitsblatts zum Rendern](/cells/de/java/implement-custom-paper-size-of-worksheet-for-rendering/)
- [Seiteneinrichtung und Druckoptionen](/cells/de/java/page-setup-and-printing-options/)
- [Entfernen Sie vorhandene Druckereinstellungen von Arbeitsblättern in einer Excel-Datei](/cells/de/java/remove-existing-printersettings-of-worksheets-in-excel-file/)
