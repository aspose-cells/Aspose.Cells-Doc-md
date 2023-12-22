---
title: Schriftart für Überschriften und Hauptthema
description: Aspose.Cells ist eine .NET-Bibliothek für die Arbeit mit Tabellenkalkulationsdateien. Es unterstützt das Festlegen von Schriftarten für Überschriften und Textthemen in Excel-Dokumenten, sodass Benutzer das Erscheinungsbild und den Stil des Dokuments anpassen können. In diesem Artikel wird erläutert, wie Sie die Bibliothek Aspose.Cells verwenden, um mit Schriftarten für Überschriften und Textthemen in Excel-Dokumenten zu arbeiten.
keywords: Aspose.Cells, Excel Document, Heading, Body, Theme Font, Appearance, Style
type: docs
weight: 120
url: /de/net/headings-and-body-theme-font/
---
{{% alert color="primary" %}}

 Die Standardschriftart ändert sich automatisch, wenn die Regoin-Einstellung geändert wird.

Wenn die Standardschriftart geändert wird, ändern sich auch die Zeilenhöhe und die Spaltenbreite, und es kann sogar zu Störungen im Seitenlayout kommen.

Was hat dazu geführt, dass sich die Standardschriftart geändert hat?

Wenn eine Excel-Designschriftart festgelegt ist, wechselt Excel basierend auf der aktuellen Sprachumgebung automatisch zwischen verschiedenen Schriftarten.


{{% /alert %}}

##  **Schriftarten für Überschriften und Hauptthemen in Excel**

Wählen Sie in Excel die Registerkarte „Startseite“ aus, klicken Sie auf das Dropdown-Feld „Schriftart“. Oben sehen Sie „Themenschriftarten“ mit zwei Themenschriftarten: Calibri Light (Überschriften) und Calibri (Textkörper) mit englischer Regionseinstellung.

**![Themenschriftarten](Theme-Fonts.png)**

Wenn „Themenschriftart“ ausgewählt ist, wird der Schriftartname in verschiedenen Regionen unterschiedlich angezeigt.
Wenn Sie nicht möchten, dass die Schriftart in verschiedenen Regionen automatisch geändert wird, wählen Sie nicht die beiden Design-Schriftarten aus.


##  **Überschriften und Textkörperschrift programmgesteuert ändern**
 Mit Aspose.Cells für .Net können wir überprüfen, ob die Standardschriftart eine Themenschriftart ist, oder die Themenschriftart mit festlegen[**Font.SchemeType**](https://reference.aspose.com/cells/net/aspose.cells/font/schemetype/) Eigentum.

Der folgende Beispielcode zeigt, wie man die Designschriftart manipuliert.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Headings-and-body-font.cs" >}}


##  **Ruft die Schriftart des lokalen Designs dynamisch programmgesteuert ab**
Manchmal befinden sich unsere Server und Benutzercomputer nicht in derselben Region. Wie können wir die gleiche Schriftart erhalten, die Benutzer für die Dateiverarbeitung wünschen?

 Wir müssen die regionalen Systemeinstellungen festlegen, bevor wir die Datei laden[**LoadOptions.Region**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/region/) Eigentum

Der folgende Beispielcode zeigt, wie Sie eine lokale Designschriftart erhalten.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Local-Theme-Font.cs" >}}