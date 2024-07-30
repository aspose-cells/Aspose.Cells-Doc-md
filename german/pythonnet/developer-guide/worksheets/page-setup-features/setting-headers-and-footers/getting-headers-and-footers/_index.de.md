---
title: Header oder Footer erhalten
type: docs
weight: 30
url: /de/python-net/get-headers-or-footers/
description: Dieser Artikel erläutert, wie man programmgesteuert Kopf und Fußzeilen aus Excel oder OpenOffice Dateien mit der Aspose.Cells Python Library via .NET API erhält.
keywords: Python Excel Bibliothek, Kopf und Fußzeilen erhalten, Kopf und Fußzeilen Parsen in Befehlsliste mit Python.
---

{{% alert color="primary" %}}

Header und Fußzeilen werden nur in der Seitenlayoutansicht, der Druckvorschau und auf gedruckten Seiten angezeigt. 

Sie können auch das Dialogfeld Seitenlayout verwenden, wenn Sie Header oder Footer für mehr als ein Arbeitsblatt gleichzeitig anzeigen möchten. 

Für andere Blatttypen wie Diagrammblätter oder Diagramme können Header und Fußzeilen nur über das Dialogfeld Seitenlayout eingefügt werden.

{{% /alert %}}

## **Wie man Kopf- und Fußzeilen in MS Excel erhält**
1. Klicken Sie auf das Arbeitsblatt, auf dem Sie Header oder Footer anzeigen bzw. ändern möchten.
2. Klicken Sie in der Gruppe Workbook-Ansichten auf der Registerkarte Ansicht auf Seitenlayout.
  Excel zeigt das Arbeitsblatt in der Seitenlayoutansicht an.
3. Klicken Sie zum Anzeigen oder Bearbeiten eines Headers oder Footers auf die linke, mittlere oder rechte Kopf- oder Fußzeile am oberen oder unteren Rand der Arbeitsblattseite (unter Kopfzeile oder über Fußzeile).


## **Wie man Kopf- und Fußzeilen mit der Aspose.Cells für Python Excel-Bibliothek erhält**
Mit den Methoden [**Worksheet.page_setup.get_header**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/get_header/#int) und [**Worksheet.page_setup.get_footer**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/get_footer/#int) kann ein .Net-Entwickler ganz einfach Header oder Footer aus der Datei erhalten.

1. Arbeitsmappe erstellen, um die Datei zu öffnen.
2. Holen Sie sich das Arbeitsblatt, von dem aus Sie Header oder Footer erhalten möchten.
3. Erhält Header oder Footer mit spezifischer Abschnitts-ID.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Gets-Header-Footer.py" >}}

## **Wie man Kopf- und Fußzeilen in Befehlsliste parsen**
Der Header- oder Fußzeilentext kann spezielle Befehle enthalten, zum Beispiel einen Platzhalter für die Seitenzahl, das aktuelle Datum oder Textformatierungseigenschaften.

Spezielle Befehle werden durch einen einzelnen Buchstaben mit einem vorangestellten Kaufmannsund ("&") dargestellt.

Die Header- und Fußzeichenketten werden mithilfe der ABNF-Grammatik konstruiert. Ohne Betrachter ist es nicht einfach zu verstehen.

Aspose.Cells für Python via .NET bietet eine [**Worksheet.page_setup.get_commands**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/get_commands/#str) Methode, um Kopf- und Fußzeilen als Befehlsliste zu parsen.

Der folgende Code zeigt, wie der Kopf oder der Fuß als Befehlsliste geparst und Befehle verarbeitet werden:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Parses-Header-Footer.py" >}}
