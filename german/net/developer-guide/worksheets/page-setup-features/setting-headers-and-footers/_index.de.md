---
title: Kopf- und Fußzeilen festlegen
type: docs
weight: 30
url: /de/net/setting-headers-and-footers/
description: In diesem Artikel wird erläutert, wie Sie programmgesteuert ein Bild in die Kopf- und Fußzeile von Excel-Arbeitsblättern einfügen, indem Sie die Kopf- und Fußzeile mit Skriptbefehlen mithilfe der Bibliothek C#, API oder .NET festlegen.
keywords: insert image in excel header footer c#, set excel header footer script commands c#
---
{{% alert color="primary" %}}

Kopf- und Fußzeilen sind die Textzeilen, die unterhalb des oberen Randes bzw. oberhalb des unteren Randes angezeigt werden. Es ist auch möglich, den Arbeitsblättern Kopf- und Fußzeilen hinzuzufügen. Kopf- und Fußzeilen können verwendet werden, um nützliche Informationen wie Seitenzahl, Autorenname, Themenname oder Datum und Uhrzeit anzuzeigen. Kopf- und Fußzeilen werden über die Seiteneinrichtungseinstellungen verwaltet.

{{% /alert %}}

##  **Kopf- und Fußzeilen festlegen**

Mit Aspose.Cells können Sie zur Laufzeit Kopf- und Fußzeilen zu Arbeitsblättern hinzufügen. Wir empfehlen jedoch, Kopf- und Fußzeilen manuell in einer vorgefertigten Datei zum Drucken festzulegen. Sie können Microsoft Excel als GUI-Tool zum Festlegen von Kopf- und Fußzeilen verwenden, um Aufwand und Entwicklungszeit zu sparen. Aspose.Cells kann die Datei importieren und die Einstellungen speichern.

Um Kopf- und Fußzeilen zur Laufzeit hinzuzufügen, bietet Aspose.Cells spezielle API-Aufrufe und Skriptbefehle zum Formatieren von Kopf- und Fußzeilen.

###  **Skriptbefehle**

Skriptbefehle sind spezielle Befehle, mit denen Sie die Formatierung von Kopf- und Fußzeilen festlegen können.

|**Skriptbefehle**|**Beschreibung**|
| :- | :- |
|&P|Die aktuelle Seitenzahl|
|&G|Ein Bild|
|&N|Die Gesamtzahl der Seiten|
|&D|Das aktuelle Datum|
|&T|Die aktuelle Uhrzeit|
|&A|Der Arbeitsblattname|
|&F|Der Dateiname ohne Pfad|
|&"\<FontName>"|Stellt einen Schriftartnamen dar. Zum Beispiel: &"Arial"|
|&"\<FontName>, \<FontStyle>"|Stellt den Schriftartnamen mit Stil dar. Zum Beispiel: &"Arial,Bold"|
|&\<FontSize>|Stellt die Schriftgröße dar. Beispiel: „&14abc“. Wenn diesem Befehl jedoch eine einfache Zahl folgt, die in der Kopfzeile ausgegeben werden soll, sollte diese durch ein Leerzeichen von der Schriftgröße getrennt werden. Beispiel: „&14 123“.|

###  **Kopf- und Fußzeilen festlegen**

 Der[**Seiteneinrichtung**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) Die Klasse bietet zwei Methoden:[**SetHeader**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setheader) Und[**SetFooter**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setfooter), wird zum Hinzufügen einer Kopf- und Fußzeile zu einem Arbeitsblatt verwendet. Diese Methoden benötigen nur zwei Parameter:

- **Abschnitt** – der Abschnitt, in dem die Kopf- oder Fußzeile platziert werden soll. Es gibt drei Abschnitte: links, Mitte und rechts, dargestellt durch 0, 1 bzw. 2.
- **Skript** – das Skript, das für die Kopf- oder Fußzeile verwendet werden soll. Dieses Skript enthält Skriptbefehle zum Formatieren von Kopf- oder Fußzeilen.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetHeadersAndFooters-1.cs" >}}

###  **Fügen Sie ein Bild in eine Kopf- oder Fußzeile ein**

 Der[**Seiteneinrichtung**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) Die Klasse verfügt über zwei zusätzliche Methoden:[**SetHeaderPicture**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setheaderpicture) Und[**SetFooterPicture**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setfooterpicture), wird verwendet, um Bilder in die Kopf- und Fußzeile einzufügen. Diese Methoden übernehmen die Parameter:

- **Abschnitt**– der Kopf- oder Fußzeilenbereich, in dem das Bild platziert wird. Es gibt drei Abschnitte: links, in der Mitte und rechts, die jeweils durch die Werte 0, 1 und 2 dargestellt werden.
- **Byte-Array** – die grafischen Daten (die Binärdaten sollen in den Puffer eines Byte-Arrays geschrieben werden).

Nachdem Sie den folgenden Code ausgeführt und die Datei geöffnet haben, überprüfen Sie die Kopfzeile des Arbeitsblatts wie folgt:

1.  Auf der**Datei** Wählen Sie im Menü *Seite einrichten**. Ein Dialog wird angezeigt.
1.  Wähle aus**Kopfzeile Fußzeile** Tab.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-InsertImageInHeaderFooter-1.cs" >}}
