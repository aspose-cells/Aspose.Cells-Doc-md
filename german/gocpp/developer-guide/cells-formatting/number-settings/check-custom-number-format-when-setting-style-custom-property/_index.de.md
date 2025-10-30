---
title: Benutzerdefiniertes Zahlenformat beim Festlegen der Style.Custom Eigenschaft prüfen mit Golang über C++
description: Aspose.Cells ist eine C++ Bibliothek zur Arbeit mit Tabellenkalkulationsdateien, die das Überprüfen benutzerdefinierter Zahlenformate beim Styling unterstützt. Dieser Artikel zeigt, wie man die Aspose.Cells Bibliothek verwendet, um benutzerdefinierte Zahlenformate zu überprüfen und sicherzustellen, dass das Styling korrekt ist.
keywords: Aspose.Cells, C++ Bibliotheken, Tabellenkalkulationen, Styling, benutzerdefiniertes Zahlenformat, Überprüfung, Validierung
type: docs
weight: 170
url: /de/go-cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **Mögliche Verwendungsszenarien**

Wenn Sie eine ungültige benutzerdefinierte Zahlenformatierung an die [**Style.GetCustom()**](https://reference.aspose.com/cells/go-cpp/style/getcustom/)-Eigenschaft zuweisen, wirft Aspose.Cells keine Ausnahme. Wenn Sie jedoch möchten, dass Aspose.Cells überprüft, ob das zugewiesene benutzerdefinierte Zahlenformat gültig ist, setzen Sie bitte die [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/)-Eigenschaft auf **true**.

## **Benutzerdefiniertes Zahlenformat überprüfen beim Festlegen der Style.Custom-Eigenschaft**

Das folgende Beispiel weist der [**Style.GetCustom()**](https://reference.aspose.com/cells/go-cpp/style/getcustom/)-Eigenschaft ein ungültiges benutzerdefiniertes Zahlenformat zu. Da wir bereits die [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/)-Eigenschaft auf **true** gesetzt haben, wird eine Ausnahme ausgelöst, z.B. Ungültiges Zahlenformat. Lesen Sie die Kommentare im Code für weitere Hinweise.

## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CheckCustomNumberFormatWhenSettingStyleCustomProperty.go" >}}
