---
title: Kopf- oder Fußzeilen abrufen
type: docs
weight: 30
url: /de/net/get-headers-or-footers/
description: In diesem Artikel wird erläutert, wie Sie mithilfe der Bibliothek C#, API oder .NET programmgesteuert Kopf- und Fußzeilen aus Excel- oder OpenOffice-Dateien abrufen.
---
{{% alert color="primary" %}}

 Kopf- und Fußzeilen werden nur in der Seitenlayoutansicht, der Druckvorschau und auf gedruckten Seiten angezeigt.

 Sie können auch das Dialogfeld „Seite einrichten“ verwenden, wenn Sie Kopf- oder Fußzeilen für mehr als ein Arbeitsblatt gleichzeitig anzeigen möchten.

Bei anderen Blatttypen wie Diagrammblättern oder Diagrammen können Sie Kopf- und Fußzeilen nur über das Dialogfeld „Seite einrichten“ einfügen.

{{% /alert %}}

##  **Kopf- und Fußzeilen in MS Excel abrufen**
1. Klicken Sie auf das Arbeitsblatt, in dem Sie Kopf- oder Fußzeilen anzeigen oder ändern möchten.
2. Klicken Sie auf der Registerkarte „Ansicht“ in der Gruppe „Arbeitsmappenansichten“ auf „Seitenlayout“.
Excel zeigt das Arbeitsblatt in der Seitenlayoutansicht an.
3. Um eine Kopf- oder Fußzeile anzuzeigen oder zu bearbeiten, klicken Sie oben oder unten auf der Arbeitsblattseite (unter Kopfzeile oder über Fußzeile) auf das linke, mittlere oder rechte Textfeld für die Kopf- oder Fußzeile.


##  **Kopf- und Fußzeilen mit Aspose.Cells für .Net abrufen**
 Mit[**Worksheet.GetHeader**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetHeader/) Und[**Arbeitsblatt.GetFooter**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetFooter/) Mit diesen Methoden können .NET-Entwickler einfach Kopf- oder Fußzeilen aus der Datei abrufen.

1. Arbeitsmappe erstellen, um die Datei zu öffnen.
2. Ruft das Arbeitsblatt ab, in das Sie Kopf- oder Fußzeilen einfügen möchten.
3. Ruft die Kopf- oder Fußzeile mit einer bestimmten Abschnitts-ID ab.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Gets-Header-Footer.cs" >}}

##  **Kopf- und Fußzeilen in Befehlsliste analysieren**
Der Kopf- oder Fußzeilentext kann spezielle Befehle enthalten, beispielsweise einen Platzhalter für die Seitenzahl, das aktuelle Datum oder Textformatierungsattribute.

Sonderbefehle werden durch einen einzelnen Buchstaben mit einem führenden Und-Zeichen („&“) dargestellt.

Die Kopf- und Fußzeilenzeichenfolgen werden mithilfe der ABNF-Grammatik erstellt. Ohne Betrachter ist es nicht leicht zu verstehen.

 Aspose.Cells für .Net bietet[**Worksheet.GetCommands**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetCommands/)Methode zum Parsen von Kopf- und Fußzeilen als Befehlsliste.

Die folgenden Codes zeigen, wie Kopf- oder Fußzeilen als Befehlsliste analysiert und Befehle verarbeitet werden:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Parses-Header-Footer.cs" >}}
