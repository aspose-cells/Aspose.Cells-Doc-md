---
title: Überprüfen Sie das benutzerdefinierte Zahlenformat, wenn Sie die Style.Custom-Eigenschaft festlegen
description: Aspose.Cells ist eine .NET-Bibliothek für die Arbeit mit Tabellenkalkulationsdateien, die die Überprüfung benutzerdefinierter Zahlenformate beim Stylen unterstützt. In diesem Artikel erfahren Sie, wie Sie mit der Bibliothek Aspose.Cells benutzerdefinierte Zahlenformate überprüfen, um sicherzustellen, dass der Stil korrekt ist.
keywords: Aspose.Cells, NET libraries, spreadsheets, styling, custom number formatting, checking, validation
type: docs
weight: 170
url: /de/net/check-custom-number-format-when-setting-style-custom-property/
---
##  **Mögliche Nutzungsszenarien**

 Wenn Sie ein ungültiges benutzerdefiniertes Zahlenformat zuweisen[**Stil.Benutzerdefiniert**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) Eigenschaft, dann löst Aspose.Cells keine Ausnahme aus. Wenn Sie jedoch möchten, dass Aspose.Cells prüft, ob das zugewiesene benutzerdefinierte Nummernformat gültig ist oder nicht, dann legen Sie bitte das fest[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) Eigenschaft auf *true**.

##  **Überprüfen Sie das benutzerdefinierte Zahlenformat, wenn Sie die Style.Custom-Eigenschaft festlegen**

 Der folgende Beispielcode weist ein ungültiges benutzerdefiniertes Zahlenformat zu[**Stil.Benutzerdefiniert**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) Eigentum. Da haben wir uns schon eingestellt[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) Eigenschaft auf *true**, daher wird eine Ausnahme ausgelöst, z. B. Ungültiges Zahlenformat. Bitte lesen Sie die Kommentare im Code, um weitere Hilfe zu erhalten.

##  **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-CheckCustomFormatPattern.cs" >}}
