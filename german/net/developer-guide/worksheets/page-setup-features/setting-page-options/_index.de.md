---
title: Seitenoptionen festlegen
type: docs
weight: 10
url: /de/net/setting-page-options/
---
{{% alert color="primary" %}}

Manchmal ist es erforderlich, Seiteneinrichtungseinstellungen für Arbeitsblätter zu konfigurieren, um den Druck zu steuern. Diese Seiteneinrichtungseinstellungen bieten verschiedene Optionen.

{{% /alert %}}

## **Seitenoptionen festlegen**

Seiteneinrichtungsoptionen werden in Aspose.Cells vollständig unterstützt. Dieser Artikel erläutert, wie Seitenoptionen mit Aspose.Cells festgelegt werden, und zeigt Codebeispiele für die Einstellung:

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , die eine Microsoft Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)Klasse.

 Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet die[**Seiteneinrichtung**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) -Eigenschaft, die zum Festlegen der Seiteneinrichtungsoptionen des Arbeitsblatts verwendet wird. In der Tat dies[**Seiteneinrichtung**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) Eigentum ist ein Objekt der[**Seiteneinrichtung**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) Klasse zum Festlegen verschiedener Seitenlayoutoptionen für ein gedrucktes Arbeitsblatt. Das[**Seiteneinrichtung**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)-Klasse stellt verschiedene Eigenschaften bereit, die zum Festlegen von Seiteneinrichtungsoptionen verwendet werden. Einige dieser Eigenschaften werden unten diskutiert.

### **Seitenausrichtung**

 Die Seitenausrichtung kann mithilfe von auf Hoch- oder Querformat eingestellt werden[**Seiteneinrichtung**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) Klasse'[**Orientierung**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/orientation) Eigentum. Das[**Orientierung**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/orientation) Die Eigenschaft akzeptiert einen der vordefinierten Werte in der[**Seitenausrichtungstyp**](https://reference.aspose.com/cells/net/aspose.cells/pageorientationtype)Aufzählung, unten aufgeführt.

|**Seitenausrichtungstypen**|**Beschreibung**|
|:- |:- |
|Landschaft|Landschaftsorientierung|
|Porträt|Hochkant|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-PageOrientation-1.cs" >}}

### **Vergößerungsfaktor, Verkleinerungsfaktor**

 Es ist möglich, die Größe eines Arbeitsblatts zu verkleinern oder zu vergrößern, indem Sie den Skalierungsfaktor mit anpassen[**Seiteneinrichtung.Zoom**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/zoom)Eigentum.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ScalingFactor-1.cs" >}}

### **FitToPages-Optionen**

 Um den Inhalt des Arbeitsblatts auf eine bestimmte Anzahl von Seiten anzupassen, verwenden Sie die[**Seiteneinrichtung**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) Klasse'[**FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall) und[**FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide)Eigenschaften. Diese Eigenschaften werden auch zum Skalieren von Arbeitsblättern verwendet.

{{% alert color="primary" %}}

 Sie können entweder die auswählen[**FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall)/[**FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide) oder der[**Zoomen**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/zoom) Eigentum, aber nicht beides gleichzeitig.

{{% /alert %}}

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-FitToPagesOptions-1.cs" >}}

### **Papier größe**

 Legen Sie die Papiergröße fest, auf die die Arbeitsblätter gedruckt werden, indem Sie die verwenden[**Seiteneinrichtung**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) Klasse'[**Papier größe**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/papersize) Eigentum. Das[**Papier größe**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/papersize) Die Eigenschaft akzeptiert einen der vordefinierten Werte in der[**PaperSizeType**](https://reference.aspose.com/cells/net/aspose.cells/papersizetype)Aufzählung, unten aufgeführt.

|**Papierformattypen**|**Beschreibung**|
|:- |:- |
|Papierbrief|Letter (8-1/2 Zoll x 11 Zoll)|
|PaperLetterSmall|Letter Small (8-1/2 Zoll x 11 Zoll)|
|PapierTabloid|Tabloid (11 Zoll x 17 Zoll)|
|PaperLedger|Hauptbuch (17 Zoll x 11 Zoll)|
|PapierLegal|Legal (8-1/2 Zoll x 14 Zoll)|
|Papierauszug|Erklärung (5-1/2 Zoll x 8-1/2 Zoll)|
|PapierExecutive|Executive (7-1/4 Zoll x 10-1/2 Zoll)|
|PapierA3|A3 (297 mm x 420 mm)|
|PapierA4|A4 (210 x 297 mm)|
|PapierA4Klein|A4 klein (210 mm x 297 mm)|
|PapierA5|A5 (148 x 210 mm)|
|PapierB4|JIS B4 (257 mm x 364 mm)|
|PapierB5|JIS B5 (182 mm x 257 mm)|
|PaperFolio|Folio (8-1/2 Zoll x 13 Zoll)|
|PapierQuarto|Quarto (215 mm x 275 mm)|
|Papier10x14|10 Zoll x 14 Zoll|
|Papier11x17|11 Zoll x 17 Zoll|
|PaperNote|Hinweis (8-1/2 Zoll x 11 Zoll)|
|Papierumschlag9|Umschlag Nr. 9 (3-7/8 Zoll x 8-7/8 Zoll)|
|Papierumschlag10|Umschlag Nr. 10 (4-1/8 Zoll x 9-1/2 Zoll)|
|Papierumschlag11|Umschlag Nr. 11 (4-1/2 Zoll x 10-3/8 Zoll)|
|Papierumschlag12|Umschlag Nr. 12 (4-1/2 Zoll x 11 Zoll)|
|Papierumschlag14|Umschlag Nr. 14 (5 Zoll x 11-1/2 Zoll)|
|PapierCSheet|Blatt in C-Größe|
|PaperDSheet|Blatt in D-Größe|
|PaperESheet|Blatt in E-Größe|
|PapierumschlagDL|Umschlag DL (110 mm x 220 mm)|
|PapierumschlagC5|Umschlag C5 (162 mm x 229 mm)|
|PapierumschlagC3|Umschlag C3 (324 mm x 458 mm)|
|PapierumschlagC4|Umschlag C4 (229 mm x 324 mm)|
|PapierumschlagC6|Umschlag C6 (114 mm x 162 mm)|
|PapierumschlagC65|Umschlag C65 (114 mm x 229 mm)|
|PapierumschlagB4|Umschlag B4 (250 mm x 353 mm|
|PapierumschlagB5|Umschlag B5 (176 mm x 250 mm)|
|PapierumschlagB6|Umschlag B6 (176 mm x 125 mm)|
|PapierumschlagItalien|Briefumschlag Italien (110 mm x 230 mm)|
|PapierumschlagMonarch|Umschlag Monarch (3-7/8 Zoll x 7-1/2 Zoll)|
|PapierUmschlagPersönlich|Umschlag (3-5/8 Zoll x 6-1/2 Zoll)|
|PaperFanfoldUS|Endlosfaltung nach US-Standard (14-7/8 Zoll x 11 Zoll)|
|PapierFanfoldStdDeutsch|Deutscher Standard Endlospapier (8-1/2 Zoll x 12 Zoll)|
|PapierFanfoldImpressumDeutsch|Deutsches Legal Endlospapier (8-1/2 Zoll x 13 Zoll)|
|PapierISOB4|B4 (ISO) 250 x 353 mm|
|PapierJapanischPostkarte|Japanische Postkarte (100 mm x 148 mm)|
|Papier9x11|9 Zoll x 11 Zoll|
|Papier10x11|10 Zoll x 11 Zoll|
|Papier15x11|15 Zoll x 11 Zoll|
|PapierUmschlagEinladung|Umschlageinladung (220 mm x 220 mm)|
|PaperLetterExtra|US Letter Extra 9 \275 x 12 Zoll|
|PaperLegalExtra|US Legal Extra 9 \275 x 15 Zoll|
|PaperTabloidExtra|US Tabloid Extra 11,69 x 18 Zoll|
|PapierA4Extra|A4 Extra 9,27 x 12,69 Zoll|
|PapierLetterQuer|Buchstabe quer 8 \275 x 11 Zoll|
|PapierA4Quer|A4 quer 210 x 297 mm|
|PaperLetterExtraQuer|Buchstabe extra quer 9\275 x 12 Zoll|
|PapierSuperA|SuperA/SuperA/A4 227 x 356 mm|
|PapierSuperB|SuperB/SuperB/A3 305 x 487 mm|
|PaperLetterPlus|US Letter Plus 8,5 x 12,69 Zoll|
|PapierA4Plus|A4 Plus 210 x 330 mm|
|PapierA5Quer|A5 quer 148 x 210 mm|
|PapierJISB5Quer|B5 (JIS) Quer 182 x 257 mm|
|PapierA3Extra|A3 Extra 322 x 445 mm|
|PapierA5Extra|A5 Extra 174 x 235 mm|
|PapierISOB5Extra|B5 (ISO) Extra 201 x 276 mm|
|PapierA2|A2 420 x 594 mm|
|PapierA3Quer|A3 quer 297 x 420 mm|
|PapierA3ExtraQuer|A3 extra quer 322 x 445 mm|
|PapierJapanischDoppeltPostkarte|Japanische Doppelpostkarte 200 x 148 mm|
|PapierA6|A6 105 x 148 mm|
|PapierJapanischUmschlagKaku2|Japanischer Umschlag Kaku #2|
|PapierJapanischUmschlagKaku3|Japanischer Umschlag Kaku #3|
|PapierJapanischUmschlagChou3|Japanischer Umschlag Chou #3|
|PapierJapanischUmschlagChou4|Japanischer Umschlag Chou #4|
|PaperLetterRotated|11 Zoll x 8,5 Zoll|
|PapierA3Gedreht|420 x 297 mm|
|PapierA4Gedreht|297 mm x 210 mm|
|PapierA5Gedreht|210 mm x 148 mm|
|PapierJISB4Gedreht|B4 (JIS) Gedreht 364 x 257 mm|
|PapierJISB5Gedreht|B5 (JIS) gedreht 257 x 182 mm|
|PapierJapanischPostkarteGedreht|Japanische Postkarte gedreht 148 x 100 mm|
|PapierJapanischDoppeltPostkarteGedreht|Doppelte japanische Postkarte gedreht 148 x 200 mm|
|PapierA6Gedreht|A6 gedreht 148 x 105 mm|
|PapierJapanischUmschlagKaku2Gedreht|Japanischer Umschlag Kaku #2 gedreht|
|PapierJapanischUmschlagKaku3Gedreht|Japanischer Umschlag Kaku #3 gedreht|
|PapierJapanischUmschlagChou3Rotated|Japanischer Umschlag Chou #3 gedreht|
|PapierJapanischUmschlagChou4Rotated|Japanischer Umschlag Chou #4 gedreht|
|PapierJISB6|B6 (JIS) 128 x 182 mm|
|PapierJISB6Gedreht|B6 (JIS) gedreht 182 x 128 mm|
|Papier12x11|12 x 11 Zoll|
|PapierJapanischUmschlagSie4|Japanischer Umschlag Sie #4|
|PapierJapanischUmschlagYou4Rotated|Japanischer Umschlag Sie Nr. 4 gedreht|
|PapierPRC16K|PRC 16K 146 x 215 mm|
|PapierPRC32K|PRC 32K 97 x 151 mm|
|PapierPRCBig32K|PRC 32K (groß) 97 x 151 mm|
|PapierPRCUmschlag1|PRC-Umschlag #1 102 x 165 mm|
|PapierPRCUmschlag2|PRC-Umschlag #2 102 x 176 mm|
|PapierPRCUmschlag3|PRC-Umschlag #3 125 x 176 mm|
|PapierPRCUmschlag4|PRC-Umschlag #4 110 x 208 mm|
|PapierPRCUmschlag5|PRC-Umschlag #5 110 x 220 mm|
|PapierPRCUmschlag6|PRC-Umschlag #6 120 x 230 mm|
|PapierPRCUmschlag7|PRC-Umschlag #7 160 x 230 mm|
|PapierPRCUmschlag8|PRC-Umschlag #8 120 x 309 mm|
|PapierPRCUmschlag9|PRC-Umschlag #9 229 x 324 mm|
|PapierPRCUmschlag10|PRC-Umschlag #10 324 x 458 mm|
|PapierPRC16KGedreht|PRC 16K gedreht|
|PapierPRC32KGedreht|PRC 32K gedreht|
|PapierPRCBig32KGedreht|PRC 32K (groß) gedreht|
|PapierPRCUmschlag1Gedreht|PRC-Umschlag #1 Gedreht 165 x 102 mm|
|PapierPRCEnvelope2Rotated|PRC-Umschlag Nr. 2 gedreht 176 x 102 mm|
|PapierPRCUmschlag3Gedreht|PRC-Umschlag #3 Gedreht 176 x 125 mm|
|PapierPRCEnvelope4Rotated|PRC-Umschlag #4 gedreht 208 x 110 mm|
|PapierPRCUmschlag5Gedreht|PRC-Umschlag #5 Gedreht 220 x 110 mm|
|PapierPRCUmschlag6Gedreht|PRC-Umschlag #6 Gedreht 230 x 120 mm|
|PapierPRCUmschlag7Gedreht|PRC-Umschlag #7 gedreht 230 x 160 mm|
|PapierPRCUmschlag8Gedreht|PRC-Umschlag #8 Gedreht 309 x 120 mm|
|PapierPRCUmschlag9Gedreht|PRC-Umschlag #9 Gedreht 324 x 229 mm|
|PapierPRCUmschlag10Gedreht|PRC-Umschlag #10 gedreht 458 x 324 mm|
|PapierB3|normales B3 (13,9 x 19,7 Zoll)|
|PapierVisitenkarte|Visitenkarte (90 mm x 55 mm)|
|PapierThermal|Thermisch (3 x 11 Zoll)|
|Brauch|Stellt das benutzerdefinierte Papierformat dar.|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ManagePaperSize-1.cs" >}}

### **Druckqualität**

 Stellen Sie die Druckqualität der zu druckenden Arbeitsblätter mit ein[**Seiteneinrichtung**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) Klasse'[**Druckqualität**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printquality)Eigentum. Die Maßeinheit für die Druckqualität ist Dots Per Inches (DPI).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintQuality-1.cs" >}}

### **Erste Seitenzahl**

 Beginnen Sie die Nummerierung der Arbeitsblattseiten mit dem[**Seiteneinrichtung**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) Klasse'[**ErsteSeitennummer**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/firstpagenumber) Eigentum. Das[**ErsteSeitennummer**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/firstpagenumber)-Eigenschaft legt die Seitennummer der ersten Arbeitsblattseite fest und die nächsten Seiten werden in aufsteigender Reihenfolge nummeriert.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetFirstPageNumber-1.cs" >}}
