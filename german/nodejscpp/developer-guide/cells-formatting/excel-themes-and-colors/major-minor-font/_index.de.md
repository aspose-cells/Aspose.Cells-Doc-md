---
title: Überschriften und Textkörper Thema Schriftart
linktitle: Überschriften und Textkörper Thema Schriftart
description: Aspose.Cells ist eine Node.js Bibliothek zum Arbeiten mit Tabellenkalkulationsdateien. Es unterstützt die Festlegung von Heading und Body Theme Schriftarten in Excel Dokumenten, sodass Benutzer das Erscheinungsbild und den Stil des Dokuments anpassen können. Dieser Artikel zeigt, wie man die Aspose.Cells Bibliothek für die Arbeit mit Heading und Body Theme Schriftarten in Excel Dokumenten nutzt.
keywords: Aspose.Cells, Excel Dokument, Überschrift, Körper, Theme Schriftart, Erscheinungsbild, Stil, Node.js via C++
type: docs
weight: 120
url: /de/nodejs-cpp/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

Die Standardschriftart ändert sich automatisch, wenn die Regionseinstellung geändert wird.

Wenn die Standard-Schriftart geändert wird, ändert sich auch die Zeilenhöhe und Spaltenbreite, und es kann sogar die Seitenlayout durcheinander bringen.

Was hat die Änderung der Standard-Schriftart verursacht?

Wenn die Excel-Themenschriftart festgelegt ist, wechselt Excel automatisch zwischen verschiedenen Schriftarten basierend auf der aktuellen Sprachumgebung.

{{% /alert %}}

## **Überschriften- und Textkörper-Themenschriftart in Excel**

Wählen Sie in Excel die Registerkarte Start, klicken Sie auf die Dropdown-Box für Schriftarten. Sie sehen "Theme Fonts" mit zwei Theme-Schriftarten: Calibri Light (Überschriften) und Calibri (Körper) mit englischer Regions-Einstellung.

**![Themenschriften](Theme-Fonts.png)**

Wenn Theme Font ausgewählt ist, wird der Schriftartname in verschiedenen Regionen unterschiedlich angezeigt. Wenn Sie nicht möchten, dass sich die Schriftart automatisch in verschiedenen Regionen ändert, wählen Sie die beiden Theme Fonts nicht aus.

## **Ändern der Überschrift- und Fließtext-Schriftart programmatisch**
Mit Aspose.Cells for Node.js via C++ können wir überprüfen, ob die Standardschriftart eine Theme-Schriftart ist, oder setzen die Theme-Schriftart mit der Methode [**Font.setSchemeType(FontSchemeType)**](https://reference.aspose.com/cells/nodejs-cpp/font/#setSchemeType-fontschemetype-).

Das folgende Beispiel zeigt, wie man die Theme-Schriftart manipuliert.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-HeadingsAndBodyThemeFont.js" >}}



## **Dynamisch lokale Design-Schriftart programmatisch abrufen**
Manchmal befinden sich unsere Server und die Rechner der Benutzer nicht in der gleichen Region. Wie können wir dieselbe Schriftart, die Benutzer für die Dateiverarbeitung möchten, erhalten?

Wir müssen die regionalen Systemeinstellungen festlegen, bevor die Datei mit der Methode [**LoadOptions.setRegion(CountryCode)**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setRegion-countrycode-) geladen wird.

Der folgende Beispielcode zeigt, wie man lokale Design-Schriftarten erhält.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-GetLocalThemeFont.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
