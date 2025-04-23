---
title: Benutzerdefiniertes Zahlenformat überprüfen beim Festlegen von Style.Custom Eigenschaft
description: Aspose.Cells ist eine Python Bibliothek für die Arbeit mit Tabellenkalkulationsdateien, welche das Prüfen benutzerdefinierter Nummernformate beim Stylen unterstützt. Dieser Artikel zeigt, wie man mit der Aspose.Cells Bibliothek benutzerdefinierte Nummernformate überprüft, um die Korrektheit des Stylings sicherzustellen.
keywords: Aspose.Cells, Python Bibliotheken, Tabellen, Styling, benutzerdefinierte Nummernformatierung, Prüfung, Validierung
type: docs
weight: 170
url: /de/python-net/check-custom-number-format-when-setting-style-custom-property/
---

## **Mögliche Verwendungsszenarien**

Wenn Sie eine ungültige benutzerdefinierte Zahlenformatierung der [**Style.custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom) Eigenschaft zuweisen, wird Aspose.Cells keine Ausnahme auslösen. Wenn Sie jedoch möchten, dass Aspose.Cells überprüft, ob das zugewiesene benutzerdefinierte Zahlenformat gültig ist oder nicht, setzen Sie die Eigenschaft [**Workbook.settings.check_custom_number_format**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/check_custom_number_format/) auf **true**.

## **Benutzerdefiniertes Zahlenformat überprüfen beim Festlegen der Style.Custom-Eigenschaft**

Der folgende Beispielcode weist der [**Style.custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom) Eigenschaft eine ungültige benutzerdefinierte Zahlenformatierung zu. Da wir bereits die [**Workbook.settings.check_custom_number_format**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/check_custom_number_format/) Eigenschaft auf **true** gesetzt haben, wird daher eine Ausnahme ausgelöst, z.B. Ungültiges Zahlenformat. Bitte lesen Sie die Kommentare im Code für weitere Hilfe.

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-CheckCustomFormatPattern.py" >}}

