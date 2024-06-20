---
title: Festlegen von Kopf und Fußzeilen
type: docs
weight: 30
url: /de/net/setting-headers-and-footers/
description: In diesem Artikel wird erläutert, wie Sie programmgesteuert ein Bild im Kopf und Fußzeilenbereich von Excel Arbeitsblättern einfügen, indem Sie den Kopf und Fußzeilen mit Skriptbefehlen mithilfe der C# API oder .NET Bibliothek einstellen.
keywords: Bild in Excel Header Fußzeile einfügen, C#; Skriptbefehle für das Festlegen von Excel Header Fußzeilen, C#
---

{{% alert color="primary" %}}

Header und Fußzeilen sind die Zeilen mit Text, die unterhalb des oberen Randes oder oberhalb des unteren Randes angezeigt werden. Es ist auch möglich, Header und Fußzeilen zu den Arbeitsblättern hinzuzufügen. Header und Fußzeilen können genutzt werden, um nützliche Informationen wie Seitenzahl, Autorname, Thema oder Datum und Uhrzeit anzuzeigen. Header und Fußzeilen werden über die Seiteneinrichtungseinstellungen verwaltet.

{{% /alert %}}

## **Kopf- und Fußzeilen einstellen**

Aspose.Cells ermöglicht es Ihnen, Header und Fußzeilen dynamisch zu Arbeitsblättern hinzuzufügen, aber wir empfehlen, Header und Fußzeilen manuell in einer vordefinierten Datei für den Druck festzulegen. Sie können Microsoft Excel als GUI-Werkzeug verwenden, um Header und Fußzeilen einzurichten, um Aufwand und Entwicklungszeit zu sparen. Aspose.Cells kann die Datei importieren und die Einstellungen speichern.

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
|&"\<FontName>"|Stellt einen Schriftartnamen dar. Beispiel: &"Arial"|
|&"\<FontName>, \<FontStyle>"|Stellt Schriftartnamen mit Stil dar. Beispiel: &"Arial,Fett"|
|&\<FontSize>|Stellt die Schriftgröße dar. Zum Beispiel: “&14abc”. Wenn jedoch dieser Befehl von einer reinen Zahl gefolgt wird, die im Kopf gedruckt werden soll, sollte diese durch ein Leerzeichen von der Schriftgröße getrennt werden. Zum Beispiel: “&14 123”.|

### **Header und Fußzeilen festlegen**

Die Klasse [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) stellt zwei Methoden bereit, [**SetHeader**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setheader) und [**SetFooter**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setfooter), die zum Hinzufügen von Header und Fußzeilen zu einem Arbeitsblatt verwendet werden. Diese Methoden nehmen nur zwei Parameter:

- **Abschnitt** – der Abschnitt, in dem der Header oder die Fußzeile platziert werden soll. Es gibt drei Abschnitte: links, zentriert und rechts, die jeweils durch 0, 1 und 2 dargestellt werden.
- **Skript** – das Skript, das für den Header oder die Fußzeile verwendet werden soll. Dieses Skript enthält Skriptbefehle zur Formatierung von Headern oder Fußzeilen.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetHeadersAndFooters-1.cs" >}}

### **Fügen Sie ein Bild in einen Header oder eine Fußzeile ein**

Die Klasse [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) hat zwei zusätzliche Methoden, [**SetHeaderPicture**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setheaderpicture) und [**SetFooterPicture**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setfooterpicture), die zum Hinzufügen von Bildern in den Header und die Fußzeile verwendet werden. Diese Methoden nehmen die Parameter:

- **Abschnitt** – der Header- oder Fußzeilenabschnitt, in den das Bild platziert wird. Es gibt drei Abschnitte, links, zentriert und rechts, die jeweils durch die Werte 0, 1 und 2 dargestellt werden.
- **Byte-Array** – die grafischen Daten (die Binärdaten sollten in den Puffer eines Byte-Arrays geschrieben werden).

Nach Ausführung des folgenden Codes und Öffnen der Datei überprüfen Sie den Kopfzeilenbereich des Arbeitsblatts:

1. Wählen Sie im Menü **Datei** die Option **Seitenlayout** aus. Es wird ein Dialogfeld angezeigt.
1. Wählen Sie den Tab **Kopfzeile/Fußzeile** aus.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-InsertImageInHeaderFooter-1.cs" >}}
