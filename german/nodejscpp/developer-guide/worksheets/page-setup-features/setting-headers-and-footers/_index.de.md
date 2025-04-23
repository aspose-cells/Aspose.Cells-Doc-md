---
title: Header und Footer mit Node.js via C++ einstellen
linktitle: Festlegen von Kopf und Fußzeilen
type: docs
weight: 30
url: /de/nodejs-cpp/setting-headers-and-footers/
description: In diesem Artikel wird erklärt, wie man programmatisch ein Bild in den Header und Footer von Excel Arbeitsblättern mit Aspose.Cells for Node.js via C++ einfügt. 
keywords: Bild in Excel Header/Footer mit Node.js via C++ einfügen, Header und Footer Skriptsbefehle in Excel mit Node.js via C++ setzen
---

{{% alert color="primary" %}}

Header und Fußzeilen sind die Zeilen mit Text, die unterhalb des oberen Randes oder oberhalb des unteren Randes angezeigt werden. Es ist auch möglich, Header und Fußzeilen zu den Arbeitsblättern hinzuzufügen. Header und Fußzeilen können genutzt werden, um nützliche Informationen wie Seitenzahl, Autorname, Thema oder Datum und Uhrzeit anzuzeigen. Header und Fußzeilen werden über die Seiteneinrichtungseinstellungen verwaltet.

{{% /alert %}}

## **Kopf- und Fußzeilen einstellen**

Aspose.Cells for Node.js via C++ ermöglicht das Hinzufügen von Headern und Fußzeilen zu Arbeitsblättern zur Laufzeit, aber wir empfehlen, Header und Fußzeilen manuell in einer vorgefertigten Datei für den Druck festzulegen. Sie können Microsoft Excel als GUI-Tool verwenden, um Header und Footer einzustellen, um Aufwand und Entwicklungszeit zu sparen. Aspose.Cells kann die Datei importieren und die Einstellungen speichern.

Um Header und Fußzeilen dynamisch hinzuzufügen, bietet Aspose.Cells spezielle API-Aufrufe und Skriptbefehle zur Formatierung von Header und Fußzeilen.

### **Skriptbefehle**

Skriptbefehle sind besondere Befehle, die es ermöglichen, die Formatierung von Header und Fußzeilen festzulegen.

|**Skriptbefehle**|**Beschreibung**|
| :- | :- |
|&P|Aktuelle Seitennummer|
|&G|Ein Bild|
|&N|Gesamtanzahl der Seiten|
|&D|Aktuelles Datum|
|&T|Aktuelle Uhrzeit|
|&A|Name des Arbeitsblatts|
|&F|Dateiname ohne Pfadangabe|
|&&Text|Zeigt &Text. Zum Beispiel: &&WO wird als &WO angezeigt|
|&"\<FontName>"|Stellt einen Schriftartnamen dar. Beispiel: &"Arial"|
|&"\<FontName>, \<FontStyle>"|Stellt Schriftartnamen mit Stil dar. Beispiel: &"Arial,Fett"|
|&\<FontSize>|Stellt die Schriftgröße dar. Zum Beispiel: “&14abc”. Wenn jedoch dieser Befehl von einer reinen Zahl gefolgt wird, die im Kopf gedruckt werden soll, sollte diese durch ein Leerzeichen von der Schriftgröße getrennt werden. Zum Beispiel: “&14 123”.|

### **Header und Fußzeilen festlegen**

Die Klasse [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) bietet zwei Methoden, [**setHeader(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setHeader-number-string-) und [**setFooter(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setFooter-number-string-), mit denen ein Header und Footer zu einem Arbeitsblatt hinzugefügt werden. Diese Methoden benötigen nur zwei Parameter:

- **Abschnitt** – der Abschnitt, in dem der Header oder die Fußzeile platziert werden soll. Es gibt drei Abschnitte: links, zentriert und rechts, die jeweils durch 0, 1 und 2 dargestellt werden.
- **Skript** – das Skript, das für den Header oder die Fußzeile verwendet werden soll. Dieses Skript enthält Skriptbefehle zur Formatierung von Headern oder Fußzeilen.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const excel = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = excel.getWorksheets().get(0).getPageSetup();

// Setting worksheet name at the left section of the header
pageSetup.setHeader(0, "&A");

// Setting current date and current time at the central section of the header
// and changing the font of the header
pageSetup.setHeader(1, "&\"Times New Roman,Bold\"&D-&T");

// Setting current file name at the right section of the header and changing the
// font of the header
pageSetup.setHeader(2, "&\"Times New Roman,Bold\"&12&F");

// Setting a string at the left section of the footer and changing the font
// of a part of this string ("123")
pageSetup.setFooter(0, "Hello World! &\"Courier New\"&14 123");

// Setting the current page number at the central section of the footer
pageSetup.setFooter(1, "&P");

// Setting page count at the right section of footer
pageSetup.setFooter(2, "&N");

// Save the Workbook.
excel.save("SetHeadersAndFooters_out.xls");
```

### **Fügen Sie ein Bild in einen Header oder eine Fußzeile ein**

Die Klasse [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) hat zwei weitere Methoden, [**setHeaderPicture(number, number[])**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setHeaderPicture-number-numberarray-) und [**setFooterPicture(number, number[])**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setFooterPicture-number-numberarray-), mit denen Bilder in den Header und Footer eingefügt werden. Diese Methoden nehmen die Parameter an:

- **Abschnitt** – der Header- oder Fußzeilenabschnitt, in den das Bild platziert wird. Es gibt drei Abschnitte, links, zentriert und rechts, die jeweils durch die Werte 0, 1 und 2 dargestellt werden.
- **Byte-Array** – die grafischen Daten (die Binärdaten sollten in den Puffer eines Byte-Arrays geschrieben werden).

Nach Ausführung des folgenden Codes und Öffnen der Datei überprüfen Sie den Kopfzeilenbereich des Arbeitsblatts:

1. Wählen Sie im Menü **Datei** die Option **Seitenlayout** aus. Es wird ein Dialogfeld angezeigt.
1. Wählen Sie den Tab **Kopfzeile/Fußzeile** aus.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Creating a Workbook object
const workbook = new AsposeCells.Workbook();

// Creating a string variable to store the url of the logo/picture
const logoUrl = path.join(dataDir, "aspose-logo.jpg");

// Declaring a byte array
const binaryData = fs.readFileSync(logoUrl);

// Creating a PageSetup object to get the page settings of the first worksheet of the workbook
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Setting the logo/picture in the central section of the page header
pageSetup.setHeaderPicture(1, binaryData);

// Setting the script for the logo/picture
pageSetup.setHeader(1, "&G");

// Setting the Sheet's name in the right section of the page header with the script
pageSetup.setHeader(2, "&A");

// Saving the workbook
workbook.save(path.join(dataDir, "InsertImageInHeaderFooter_out.xls"));
```
