---
title: Arbeitsblätter und Registerkarten anzeigen und ausblenden
type: docs
weight: 10
url: /de/net/show-and-hide-worksheets-and-tabs/
description: Dieser Artikel bietet Beispielscode für die Verwendung der C# API oder der .NET Bibliothek, um ein Excel Arbeitsblatt programmgesteuert anzuzeigen und auszublenden. Darüber hinaus wird erläutert, wie Excel Arbeitsmappenregisterkarten angezeigt und ausgeblendet werden.
---

{{% alert color="primary" %}}

Aspose.Cells ermöglicht es dem Benutzer, Elemente einer Arbeitsmappe einschließlich Arbeitsblätter und Registerkarten anzuzeigen und auszublenden.

{{% /alert %}}

## **Arbeitsblatt anzeigen und ausblenden**

Eine Excel-Datei kann ein oder mehrere Arbeitsblätter enthalten. Immer wenn wir eine Excel-Datei erstellen, fügen wir Arbeitsblätter hinzu, in denen wir arbeiten. Jedes Arbeitsblatt in einer Excel-Datei ist unabhängig von anderen Arbeitsblättern und verfügt über eigene Daten- und Formatierungseinstellungen usw. Manchmal benötigen Entwickler möglicherweise, dass einige Arbeitsblätter in der Excel-Datei ausgeblendet und andere sichtbar sind, um ihre eigenen Interessen zu wahren. **Aspose.Cells** ermöglicht Entwicklern daher, die Sichtbarkeit der Arbeitsblätter in ihren Excel-Dateien zu steuern.

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), die eine Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) enthält eine [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung von Arbeitsblättern. Um die Sichtbarkeit eines Arbeitsblatts zu steuern, verwenden Sie die Eigenschaft [**IsVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) der Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). [**IsVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) ist eine boolesche Eigenschaft, die nur einen **true** oder **false** Wert speichern kann.

### **Ein Arbeitsblatt sichtbar machen**

Machen Sie ein Arbeitsblatt sichtbar, indem Sie die Eigenschaft [**IsVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) der Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) auf **true** setzen

### **Arbeitsblatt ausblenden**

Blenden Sie ein Arbeitsblatt aus, indem Sie die Eigenschaft [**IsVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) der Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) auf **false** setzen

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideUnhideWorksheet-1.cs" >}}

## **Registerkarten anzeigen und ausblenden**

Wenn Sie am unteren Rand einer Microsoft Excel-Datei genau hinsehen, sehen Sie eine Reihe von Steuerelementen. Dazu gehören:

- Registerkarten.
- Registerkarten-Scrolltasten.

Registerkarten stellen die Arbeitsblätter in der Excel-Datei dar. Klicken Sie auf eine beliebige Registerkarte, um zu diesem Arbeitsblatt zu wechseln. Je mehr Arbeitsblätter in der Arbeitsmappe sind, desto mehr Registerkarten gibt es. Wenn die Excel-Datei eine gute Anzahl von Arbeitsblättern hat, benötigen Sie Tasten, um zwischen ihnen zu navigieren. Daher bietet Microsoft Excel Registerkarten-Scrolltasten zum Scrollen durch die Registerkarten an.

Mit Aspose.Cells können Entwickler die Sichtbarkeit von Registerkarten und Bildlaufschaltflächen für Registerkarten in Excel-Dateien steuern.

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), die eine Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) bietet eine breite Palette von Eigenschaften und Methoden zur Verwaltung einer Excel-Datei. Um die Sichtbarkeit von Registerkarten in einer Excel-Datei zu steuern, können Entwickler die Eigenschaft [**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) der Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) verwenden. [**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) ist eine boolesche Eigenschaft, die nur einen **true** oder **false** Wert speichern kann.

### **Sichtbarkeit von Registerkarten**

Machen Sie Registerkarten mit der Eigenschaft [**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) der Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) auf **true** sichtbar.

### **Registerkarten ausblenden**

Blenden Sie Registerkarten in einer Excel-Datei aus, indem Sie die Eigenschaft [**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) der Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) auf false setzen.

Nachfolgend finden Sie ein vollständiges Beispiel, das eine Excel-Datei (book1.xls) öffnet, ihre Registerkarten ausblendet und die modifizierte Datei als Output.xls speichert. Nach der Codeausführung werden Sie feststellen, dass die Registerkarten der Arbeitsmappe ausgeblendet sind.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideTabs-1.cs" >}}

### **Steuerung der Registerkartenleistenbreite**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-ControlTabBarWidth-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
