---
title: Überprüfen Sie das benutzerdefinierte Zahlenformat, wenn Sie die Style.Custom-Eigenschaft festlegen
type: docs
weight: 170
url: /de/net/check-custom-number-format-when-setting-style-custom-property/
---
## **Mögliche Nutzungsszenarien**

 Wenn Sie ein ungültiges benutzerdefiniertes Zahlenformat zuweisen[**Stil.Benutzerdefiniert**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)-Eigenschaft, dann löst Aspose.Cells keine Ausnahme aus. Wenn Sie aber möchten, dass die Aspose.Cells prüfen soll, ob das zugewiesene benutzerdefinierte Nummernformat gültig ist oder nicht, dann stellen Sie bitte die[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) Eigentum zu**Stimmt**.

## **Aktivieren Sie das benutzerdefinierte Zahlenformat, wenn Sie die Eigenschaft Style.Custom festlegen**

 Der folgende Beispielcode weist ein ungültiges benutzerdefiniertes Zahlenformat zu[**Stil.Benutzerdefiniert**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) Eigentum. Da haben wir schon eingestellt[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) Eigentum zu**Stimmt**, daher wird eine Ausnahme ausgelöst, z. B. Ungültiges Zahlenformat. Bitte lesen Sie die Kommentare im Code für weitere Hilfe.

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-CheckCustomFormatPattern.cs" >}}
