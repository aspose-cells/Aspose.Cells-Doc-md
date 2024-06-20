---
title: Überschriften und Textkörper Thema Schriftart
description: Aspose.Cells ist eine .NET Bibliothek zum Arbeiten mit Tabellenkalkulationsdateien. Sie unterstützt das Festlegen von Überschriften und Körperschriftarten Themen in Excel Dokumenten, was es Benutzern ermöglicht, das Aussehen und den Stil des Dokuments anzupassen. Dieser Artikel wird vorstellen, wie man mit der Aspose.Cells Bibliothek Überschriften und Körperschriftarten Themen in Excel Dokumenten verwenden kann.
keywords: Aspose.Cells, Excel Dokument, Überschrift, Körper, Themen Schriftart, Aussehen, Stil
type: docs
weight: 120
url: /de/net/headings-and-body-theme-font/
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
Mit Aspose.Cells für .Net können wir überprüfen, ob die Standard-Schriftart eine Themen-Schriftart ist oder eine Themen-Schriftart mit [**Font.SchemeType**](https://reference.aspose.com/cells/net/aspose.cells/font/schemetype/)-Eigenschaft setzen.

Der folgende Beispielcode zeigt, wie man Schriftarten im Design manipuliert.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Headings-and-body-font.cs" >}}


## **Dynamisch erhält lokale Design-Schriftart programmgesteuert**
Manchmal befinden sich unsere Server und die Rechner der Benutzer nicht in der gleichen Region. Wie können wir dieselbe Schriftart, die Benutzer für die Dateiverarbeitung möchten, erhalten?

Wir müssen die regionalen Einstellungen des Systems setzen, bevor die Datei mit der Eigenschaft [**LoadOptions.Region**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/region/) geladen wird

Der folgende Beispielcode zeigt, wie man lokale Design-Schriftarten erhält.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Local-Theme-Font.cs" >}}
