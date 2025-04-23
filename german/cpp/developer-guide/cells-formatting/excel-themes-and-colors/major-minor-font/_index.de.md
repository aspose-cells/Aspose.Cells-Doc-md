---
title: Überschriften und Fließtext Design Schriftart mit C++
linktitle: Überschriften und Textkörper Thema Schriftart
description: Aspose.Cells ist eine C++ Bibliothek für die Arbeit mit Tabellenkalkulationsdateien. Sie unterstützt das Festlegen von Überschriften und Fließtext Design Schriftarten in Excel Dokumenten, sodass Benutzer das Aussehen und den Stil des Dokuments anpassen können. Dieser Artikel zeigt, wie man mit der Aspose.Cells Bibliothek an Überschrift und Fließtext Design Schriftarten in Excel Dokumenten arbeitet.
keywords: Aspose.Cells, Excel Dokument, Überschrift, Körper, Themen Schriftart, Aussehen, Stil
type: docs
weight: 120
url: /de/cpp/headings-and-body-theme-font/
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
Mit Aspose.Cells for C++ können wir überprüfen, ob die Standard-Schriftart eine Design-Schriftart ist oder die Design-Schriftart mit der [**Font.GetSchemeType()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getschemetype/)-Eigenschaft setzen.

Der folgende Beispielcode zeigt, wie man Schriftarten im Design manipuliert.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook object
    Workbook workbook(u"Book1.xlsx");

    // Get the default style
    Style defaultStyle = workbook.GetDefaultStyle();

    // Get the font scheme type
    FontSchemeType schemeType = defaultStyle.GetFont().GetSchemeType();

    // Check if the font is a theme font
    if (schemeType == FontSchemeType::Major || schemeType == FontSchemeType::Minor)
    {
        std::cout << "It's theme font" << std::endl;
    }

    // Change theme font to normal font
    defaultStyle.GetFont().SetSchemeType(FontSchemeType::None);

    // Set the modified default style back to the workbook
    workbook.SetDefaultStyle(defaultStyle);

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Dynamisch lokale Design-Schriftart programmatisch abrufen**
Manchmal befinden sich unsere Server und die Rechner der Benutzer nicht in der gleichen Region. Wie können wir dieselbe Schriftart, die Benutzer für die Dateiverarbeitung möchten, erhalten?

Wir müssen die regionalen Systemeinstellungen festlegen, bevor wir die Datei mit der [**LoadOptions.GetRegion()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getregion/)-Eigenschaft laden.

Das folgende Beispiel zeigt, wie man die lokale Design-Schriftart erhält.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new LoadOptions
    LoadOptions options;

    // Set the customer's region to Japan
    options.SetRegion(CountryCode::Japan);

    // Instantiate a new Workbook with the specified options
    Workbook workbook(u"Book1.xlsx", options);

    // Get the default style of the workbook
    Style defaultStyle = workbook.GetDefaultStyle();

    // Get the customer's local font name
    U16String localFontName = defaultStyle.GetFont().GetName();

    std::cout << "Local Font Name: " << localFontName.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
