---
title: Überschriften und Text Theme Schriftarten mit Golang über C++
linktitle: Überschriften und Textkörper Thema Schriftart
description: Aspose.Cells ist eine C++ Bibliothek für die Arbeit mit Tabellenkalkulationsdateien. Sie unterstützt das Festlegen von Überschriften und Fließtext Design Schriftarten in Excel Dokumenten, sodass Benutzer das Aussehen und den Stil des Dokuments anpassen können. Dieser Artikel zeigt, wie man mit der Aspose.Cells Bibliothek an Überschrift und Fließtext Design Schriftarten in Excel Dokumenten arbeitet.
keywords: Aspose.Cells, Excel Dokument, Überschrift, Körper, Themen Schriftart, Aussehen, Stil
type: docs
weight: 120
url: /de/go-cpp/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

Die Standardschriftart ändert sich automatisch, wenn die Regionseinstellung geändert wird.

Wenn die Standard-Schriftart geändert wird, ändert sich auch die Zeilenhöhe und Spaltenbreite, und es kann sogar die Seitenlayout durcheinander bringen.

Was hat die Änderung der Standard-Schriftart verursacht?

Wenn die Excel-Themenschriftart festgelegt ist, wechselt Excel automatisch zwischen verschiedenen Schriftarten basierend auf der aktuellen Sprachumgebung.

{{% /alert %}}

## **Überschriften- und Textkörper-Themenschriftart in Excel**

Wählen Sie in Excel die Registerkarte Start aus, klicken Sie auf das Dropdown-Menü für Schriftarten. Sie sehen "Design-Schriftarten" mit zwei Design-Schriftarten: Calibri Light (Überschriften) und Calibri (Fließtext) oben mit englischer Regionseinstellung.

**![Themenschriften](Theme-Fonts.png)**

Wenn Design-Schriftart ausgewählt ist, wird der Schriftartname je nach Region unterschiedlich angezeigt.
Wenn Sie nicht möchten, dass die Schriftart in verschiedenen Regionen automatisch geändert wird, wählen Sie die beiden Design-Schriftarten nicht aus.

## **Ändern der Überschrift- und Fließtext-Schriftart programmatisch**
Mit Aspose.Cells for C++ können wir überprüfen, ob die Standard-Schriftart eine Design-Schriftart ist oder die Design-Schriftart mit der [**Font.GetSchemeType()**](https://reference.aspose.com/cells/go-cpp/font/getschemetype/)-Eigenschaft setzen.

Der folgende Beispielcode zeigt, wie man Schriftarten im Design manipuliert.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MajorMinorFont.go" >}}
## **Dynamisch lokale Design-Schriftart programmatisch abrufen**
Manchmal befinden sich unsere Server und die Rechner der Benutzer nicht in der gleichen Region. Wie können wir dieselbe Schriftart, die Benutzer für die Dateiverarbeitung möchten, erhalten?

Wir müssen die regionalen Systemeinstellungen festlegen, bevor wir die Datei mit der [**LoadOptions.GetRegion()**](https://reference.aspose.com/cells/go-cpp/loadoptions/getregion/)-Eigenschaft laden.

Das folgende Beispiel zeigt, wie man die lokale Design-Schriftart erhält.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MajorMinorFont-1.go" >}}
