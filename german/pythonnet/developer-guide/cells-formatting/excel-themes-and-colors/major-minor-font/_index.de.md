---
title: Überschriften und Textkörper Thema Schriftart
description: Aspose.Cells ist eine Python Bibliothek zur Arbeit mit Tabellenkalkulationsdateien. Sie unterstützt das Festlegen von Kopf und Fliessthema Schriftarten in Excel Dokumenten, wodurch Nutzer das Aussehen und den Stil des Dokuments anpassen können. Dieser Artikel zeigt, wie man die Aspose.Cells für Python via .NET Bibliothek verwendet, um mit Kopf und Fliessthema Schriftarten in Excel Dokumenten zu arbeiten.
keywords: Aspose.Cells für Python via .NET, Excel Dokument, Kopf, Fliessthema, Schriftart, Erscheinungsbild, Stil
type: docs
weight: 120
url: /de/python-net/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

Die Standard-Schriftart ändert sich automatisch, wenn die Regionseinstellung geändert wird. 

Wenn die Standard-Schriftart geändert wird, ändert sich auch die Zeilenhöhe und Spaltenbreite, und es kann sogar die Seitenlayout durcheinander bringen.

Was hat die Änderung der Standard-Schriftart verursacht?

Wenn die Excel-Themenschriftart festgelegt ist, wechselt Excel automatisch zwischen verschiedenen Schriftarten basierend auf der aktuellen Sprachumgebung.


{{% /alert %}}

## **Überschriften- und Textkörper-Themenschriftart in Excel**

In Excel wählen Sie die Registerkarte Start, klicken Sie auf das Schriftarten-Dropdown-Feld, Sie sehen "Themenschriften" mit zwei Themen-Schriftarten: Calibri Light (Überschriften) und Calibri (Textkörper) oben mit Englischer Regionseinstellung.

**![Themenschriften](Theme-Fonts.png)**

Wenn die Themen-Schriftart ausgewählt wird, wird der Schriftname je nach Region unterschiedlich angezeigt.
Wenn Sie nicht möchten, dass die Schriftart in verschiedenen Regionen automatisch geändert wird, wählen Sie nicht die beiden Themen-Schriftarten.


## **Überschriften- und Textkörper-Schriftart programmgesteuert ändern**
Mit Aspose.Cells für Python via .NET können wir überprüfen, ob die Standardschriftart eine Thema-Schriftart ist oder eine Thema-Schriftart mit der [**Font.scheme_type**](https://reference.aspose.com/cells/python-net/aspose.cells/font/scheme_type) Eigenschaft festlegen.

Der folgende Beispielcode zeigt, wie man Schriftarten im Design manipuliert.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Headings-and-body-font.py" >}}


## **Dynamisch erhält lokale Design-Schriftart programmgesteuert**
Manchmal befinden sich unsere Server und die Rechner der Benutzer nicht in der gleichen Region. Wie können wir dieselbe Schriftart, die Benutzer für die Dateiverarbeitung möchten, erhalten?

Wir müssen die regionalen Einstellungen des Systems setzen, bevor die Datei mit der Eigenschaft [**LoadOptions.region**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/region) geladen wird

Der folgende Beispielcode zeigt, wie man lokale Design-Schriftarten erhält.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Local-Theme-Font.py" >}}

