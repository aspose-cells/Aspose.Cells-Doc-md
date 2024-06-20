---
title: Benutzerdefiniertes Zahlenformat überprüfen beim Festlegen von Style.Custom Eigenschaft
type: docs
weight: 160
url: /de/java/check-custom-number-format-when-setting-style-custom-property/
---

## **Mögliche Verwendungsszenarien**

Wenn Sie dem [**Style.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom)-Eigenschaft eine ungültige benutzerdefinierte Zahlenformatierung zuweisen, wirft Aspose.Cells keine Ausnahme. Wenn Sie jedoch möchten, dass Aspose.Cells überprüft, ob die zugewiesene benutzerdefinierte Zahlenformatierung gültig ist oder nicht, setzen Sie bitte die [**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat)-Eigenschaft auf **true**.

## **Überprüfen Sie das benutzerdefinierte Zahlenformat beim Festlegen der Style.Custom-Eigenschaft**

Der folgende Beispielcode weist der [**Style.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom)-Eigenschaft ein ungültiges benutzerdefiniertes Zahlenformat zu. Da wir bereits die [**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat)-Eigenschaft auf **true** gesetzt haben, wirft die API also eine CellsException z.B. *Ungültige Zahlenformatierung*.

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CheckCustomNumberFormat-CheckCustomNumberFormat.java" >}}
