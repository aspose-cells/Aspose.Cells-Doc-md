---
title: Überprüfen Sie das benutzerdefinierte Zahlenformat, wenn Sie die Style.Custom-Eigenschaft festlegen
type: docs
weight: 160
url: /de/java/check-custom-number-format-when-setting-style-custom-property/
---
## **Mögliche Nutzungsszenarien**

 Wenn Sie ein ungültiges benutzerdefiniertes Zahlenformat zuweisen[**Stil.Benutzerdefiniert**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom)Eigenschaft dann Aspose.Cells wird keine Ausnahme auslösen. Aber wenn Sie möchten, dass die Aspose.Cells prüfen soll, ob das zugewiesene benutzerdefinierte Nummernformat gültig ist oder nicht, dann stellen Sie dies bitte ein[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat) Eigentum zu**wahr**.

## **Überprüfen Sie das benutzerdefinierte Zahlenformat, wenn Sie die Eigenschaft Style.Custom festlegen**

 Der folgende Beispielcode weist ein ungültiges benutzerdefiniertes Zahlenformat zu[**Stil.Benutzerdefiniert**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) Eigentum. Da haben wir schon eingestellt[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat) Eigentum zu**wahr** , daher wird die API CellsException zB auslösen*Ungültiges Zahlenformat*.

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CheckCustomNumberFormat-CheckCustomNumberFormat.java" >}}
