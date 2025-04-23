---
title: Festlegen von Kopf und Fußzeilen
type: docs
weight: 30
url: /de/python-net/setting-headers-and-footers/
description: Dieser Artikel erklärt, wie man programmatisch ein Bild in den Kopf und Fußbereich von Excel Arbeitsblättern einfügt, indem man den Kopf und Fußbereich mit Skriptbefehlen unter Verwendung der Aspose.Cells for Python via .NET API setzt.
keywords: Python Excel Bibliothek, Python Bild in Excel Kopf und Fußzeile einfügen, Skriptbefehle zum Festlegen des Excel Kopf und Fußbereichs mit Python.
---

{{% alert color="primary" %}}

Header und Fußzeilen sind die Zeilen mit Text, die unterhalb des oberen Randes oder oberhalb des unteren Randes angezeigt werden. Es ist auch möglich, Header und Fußzeilen zu den Arbeitsblättern hinzuzufügen. Header und Fußzeilen können genutzt werden, um nützliche Informationen wie Seitenzahl, Autorname, Thema oder Datum und Uhrzeit anzuzeigen. Header und Fußzeilen werden über die Seiteneinrichtungseinstellungen verwaltet.

{{% /alert %}}

## **Kopf- und Fußzeilen einstellen**

Aspose.Cells for Python via .NET ermöglicht es, Überschriften und Fußzeilen während der Laufzeit zu hinzufügen, aber wir empfehlen, Überschriften und Fußzeilen manuell in einer vordefinierten Datei zum Drucken festzulegen. Sie können Microsoft Excel als GUI-Tool verwenden, um Überschriften und Fußzeilen einzustellen und so Aufwand und Entwicklungszeit zu sparen. Aspose.Cells for Python via .NET kann die Datei importieren und die Einstellungen speichern.

Um Überschriften und Fußzeilen zur Laufzeit hinzuzufügen, bietet Aspose.Cells for Python via .NET spezielle API-Aufrufe und Skriptbefehle zum Formatieren von Überschriften und Fußzeilen.

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
|&"\<FontName>"|Stellt einen Schriftartnamen dar. Beispiel: &"Arial"|
|&"\<FontName>, \<FontStyle>"|Stellt Schriftartnamen mit Stil dar. Beispiel: &"Arial,Fett"|
|&\<FontSize>|Stellt die Schriftgröße dar. Zum Beispiel: “&14abc”. Wenn jedoch dieser Befehl von einer reinen Zahl gefolgt wird, die im Kopf gedruckt werden soll, sollte diese durch ein Leerzeichen von der Schriftgröße getrennt werden. Zum Beispiel: “&14 123”.|

### **So setzen Sie Überschriften und Fußzeilen**

Die Klasse [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) stellt zwei Methoden bereit, [**set_header**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_header/#int-str) und [**set_footer**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_footer/#int-str), die zum Hinzufügen von Header und Fußzeilen zu einem Arbeitsblatt verwendet werden. Diese Methoden nehmen nur zwei Parameter:

- **Abschnitt** – der Abschnitt, in dem der Header oder die Fußzeile platziert werden soll. Es gibt drei Abschnitte: links, zentriert und rechts, die jeweils durch 0, 1 und 2 dargestellt werden.
- **Skript** – das Skript, das für den Header oder die Fußzeile verwendet werden soll. Dieses Skript enthält Skriptbefehle zur Formatierung von Headern oder Fußzeilen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetHeadersAndFooters-1.py" >}}

### **So fügen Sie ein Bild in eine Kopf- oder Fußzeile ein**

Die Klasse [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) hat zwei zusätzliche Methoden, [**set_header_picture**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_header_picture/#int-bytes) und [**set_footer_picture**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_footer_picture/#int-bytes), die zum Hinzufügen von Bildern in den Header und die Fußzeile verwendet werden. Diese Methoden nehmen die Parameter:

- **Abschnitt** – der Header- oder Fußzeilenabschnitt, in den das Bild platziert wird. Es gibt drei Abschnitte, links, zentriert und rechts, die jeweils durch die Werte 0, 1 und 2 dargestellt werden.
- **Byte-Array** – die grafischen Daten (die Binärdaten sollten in den Puffer eines Byte-Arrays geschrieben werden).

Nach Ausführung des folgenden Codes und Öffnen der Datei überprüfen Sie den Kopfzeilenbereich des Arbeitsblatts:

1. Wählen Sie im Menü **Datei** die Option **Seitenlayout** aus. Es wird ein Dialogfeld angezeigt.
1. Wählen Sie den Tab **Kopfzeile/Fußzeile** aus.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-InsertImageInHeaderFooter-1.py" >}}
