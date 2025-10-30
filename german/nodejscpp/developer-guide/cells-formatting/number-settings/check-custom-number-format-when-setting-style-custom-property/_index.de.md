---
title: Benutzerdefiniertes Zahlenformat überprüfen beim Festlegen von Style.Custom Eigenschaft
linktitle: Benutzerdefiniertes Zahlenformat überprüfen beim Festlegen von Style.Custom Eigenschaft
description: Aspose.Cells ist eine Node.js Bibliothek zur Arbeit mit Tabellenkalkulationsdateien, die die Überprüfung benutzerdefinierter Zahlenformate beim Formatieren unterstützt. Dieser Artikel zeigt, wie Sie die Aspose.Cells Bibliothek verwenden, um benutzerdefinierte Zahlenformate zu prüfen und sicherzustellen, dass die Formatierung korrekt ist.
keywords: Aspose.Cells, Node.js Bibliotheken, Tabellen, Formatierung, benutzerdefinierte Zahlenformatierung, Überprüfung, Validierung
type: docs
weight: 170
url: /de/nodejs-cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **Mögliche Verwendungsszenarien**

Wenn Sie eine ungültige benutzerdefinierte Zahlenformatierung an die [**Style.setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-) Methode zuweisen, wirft Aspose.Cells for Node.js via C++ keine Ausnahme. Wenn Sie jedoch möchten, dass Aspose.Cells überprüft, ob die zugewiesene benutzerdefinierte Zahlenformatierung gültig ist oder nicht, setzen Sie bitte die [**Workbook.getSettings().setCheckCustomNumberFormat(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setCheckCustomNumberFormat-boolean-)-Methode auf **true**.

## **Benutzerdefiniertes Zahlenformat beim Setzen von Style.setCustom(string) überprüfen**

Der folgende Beispielcode weist der [**Style.setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-) Methode eine ungültige benutzerdefinierte Zahlenformatierung zu. Da wir die [**Workbook.getSettings().setCheckCustomNumberFormat(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setCheckCustomNumberFormat-boolean-)-Methode bereits auf **true** gesetzt haben, löst es eine Ausnahme aus, z.B. Ungültiges Zahlenformat. Lesen Sie die Kommentare im Code für weitere Hilfe.

## **Beispielcode**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-CheckCustomNumberFormat.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
