---
title: Header oder Footer erhalten
type: docs
weight: 30
url: /de/net/get-headers-or-footers/
description: Dieser Artikel erklärt, wie Sie über die C# API oder die .NET Bibliothek programmgesteuert Header und Fußzeilen aus Excel oder OpenOffice Dateien erhalten.
---

{{% alert color="primary" %}}

Header und Fußzeilen werden nur in der Seitenlayoutansicht, der Druckvorschau und auf gedruckten Seiten angezeigt. 

Sie können auch das Dialogfeld Seitenlayout verwenden, wenn Sie Header oder Footer für mehr als ein Arbeitsblatt gleichzeitig anzeigen möchten. 

Für andere Blatttypen wie Diagrammblätter oder Diagramme können Header und Fußzeilen nur über das Dialogfeld Seitenlayout eingefügt werden.

{{% /alert %}}

## **Header und Fußzeilen in MS Excel erhalten**
1. Klicken Sie auf das Arbeitsblatt, auf dem Sie Header oder Footer anzeigen bzw. ändern möchten.
2. Klicken Sie in der Gruppe Workbook-Ansichten auf der Registerkarte Ansicht auf Seitenlayout.
  Excel zeigt das Arbeitsblatt in der Seitenlayoutansicht an.
3. Klicken Sie zum Anzeigen oder Bearbeiten eines Headers oder Footers auf die linke, mittlere oder rechte Kopf- oder Fußzeile am oberen oder unteren Rand der Arbeitsblattseite (unter Kopfzeile oder über Fußzeile).


## **Header und Fußzeilen mit Aspose.Cells für .Net erhalten**
Mit den Methoden [**Worksheet.GetHeader**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetHeader/) und [**Worksheet.GetFooter**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetFooter/) kann ein .Net-Entwickler ganz einfach Header oder Footer aus der Datei erhalten.

1. Arbeitsmappe erstellen, um die Datei zu öffnen.
2. Holen Sie sich das Arbeitsblatt, von dem aus Sie Header oder Footer erhalten möchten.
3. Erhält Header oder Footer mit spezifischer Abschnitts-ID.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Gets-Header-Footer.cs" >}}

## **Kopf- und Fußzeilen zu Befehlsliste parsen**
Der Header- oder Fußzeilentext kann spezielle Befehle enthalten, zum Beispiel einen Platzhalter für die Seitenzahl, das aktuelle Datum oder Textformatierungseigenschaften.

Spezielle Befehle werden durch einen einzelnen Buchstaben mit einem vorangestellten Kaufmannsund ("&") dargestellt.

Die Header- und Fußzeichenketten werden mithilfe der ABNF-Grammatik konstruiert. Ohne Betrachter ist es nicht einfach zu verstehen.

Aspose.Cells für .Net stellt die Methode [**Worksheet.GetCommands**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetCommands/) bereit, um Kopf- und Fußzeilen als Befehlsliste zu parsen.

Der folgende Code zeigt, wie der Kopf oder der Fuß als Befehlsliste geparst und Befehle verarbeitet werden:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Parses-Header-Footer.cs" >}}
