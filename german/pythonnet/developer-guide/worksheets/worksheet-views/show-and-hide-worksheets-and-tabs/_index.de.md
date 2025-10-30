---
title: Arbeitsblätter und Registerkarten anzeigen und ausblenden
type: docs
weight: 10
url: /de/python-net/show-and-hide-worksheets-and-tabs/
description: Dieser Artikel bietet Beispielcode für die Verwendung der Aspose.Cells für Python via .NET API, um eine Excel Arbeitsmappe programmgesteuert anzuzeigen und auszublenden. Darüber hinaus wird gezeigt, wie man Excel Arbeitsblatt Registerkarten anzeigt und ausblendet.
keywords: Python Excel Bibliothek, Arbeitsblatt anzeigen und ausblenden, Registerkarten anzeigen und ausblenden, Tab Leiste steuern.
---

{{% alert color="primary" %}}

Aspose.Cells für Python via .NET ermöglicht es dem Benutzer, Elemente eines Arbeitsbuchs, einschließlich Arbeitsblätter und Registerkarten, anzuzeigen und auszublenden.

{{% /alert %}}

## **Arbeitsblatt anzeigen und ausblenden**

Eine Excel-Datei kann ein oder mehrere Arbeitsblätter enthalten. Wann immer wir eine Excel-Datei erstellen, fügen wir Arbeitsblätter hinzu, mit denen wir arbeiten. Jedes Arbeitsblatt in einer Excel-Datei ist unabhängig von den anderen Arbeitsblättern, da es eigene Daten und Formatierungseinstellungen usw. hat. Manchmal möchten Entwickler einige Arbeitsblätter ausblenden und andere sichtbar machen, um ihre eigenen Interessen zu verfolgen. Daher erlaubt **Aspose.Cells für Python via .NET** Entwicklern, die Sichtbarkeit der Arbeitsblätter in ihren Excel-Dateien zu steuern.

Aspose.Cells für Python via .NET stellt eine Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) bereit, die eine Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) enthält eine [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung von Arbeitsblättern. Um die Sichtbarkeit eines Arbeitsblatts zu steuern, verwenden Sie die Eigenschaft [**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible) der Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). [**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible) ist eine boolesche Eigenschaft, die nur einen **true** oder **false** Wert speichern kann.

### **Ein Arbeitsblatt sichtbar machen**

Machen Sie ein Arbeitsblatt sichtbar, indem Sie die Eigenschaft [**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible) der Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) auf **true** setzen

### **Arbeitsblatt ausblenden**

Blenden Sie ein Arbeitsblatt aus, indem Sie die Eigenschaft [**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible) der Klasse [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) auf **false** setzen

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-HideUnhideWorksheet-1.py" >}}

## **Registerkarten anzeigen und ausblenden**

Wenn Sie am unteren Rand einer Microsoft Excel-Datei genau hinsehen, sehen Sie eine Reihe von Steuerelementen. Dazu gehören:

- Registerkarten.
- Registerkarten-Scrolltasten.

Registerkarten stellen die Arbeitsblätter in der Excel-Datei dar. Klicken Sie auf eine beliebige Registerkarte, um zu diesem Arbeitsblatt zu wechseln. Je mehr Arbeitsblätter in der Arbeitsmappe sind, desto mehr Registerkarten gibt es. Wenn die Excel-Datei eine gute Anzahl von Arbeitsblättern hat, benötigen Sie Tasten, um zwischen ihnen zu navigieren. Daher bietet Microsoft Excel Registerkarten-Scrolltasten zum Scrollen durch die Registerkarten an.

Mit Aspose.Cells für Python via .NET können Entwickler die Sichtbarkeit von Blatt-Registerkarten und den Scroll-Buttons in Excel-Dateien steuern.

Aspose.Cells für Python via .NET stellt eine Klasse {0 bereit}, die eine Excel-Datei repräsentiert. Die Klasse {1} bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung einer Excel-Datei. Um die Sichtbarkeit der Registerkarten in einer Excel-Datei zu steuern, können Entwickler die Eigenschaft {2} der Klasse {3} mit {4} verwenden. {5} ist eine Boolesche Eigenschaft, die nur **true** oder **false** speichern kann.

### **Sichtbarkeit von Registerkarten**

Machen Sie Registerkarten mit der Eigenschaft [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) der Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) auf **true** sichtbar.

### **Registerkarten ausblenden**

Blenden Sie Registerkarten in einer Excel-Datei aus, indem Sie die Eigenschaft [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) der Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) auf false setzen.

Nachfolgend finden Sie ein vollständiges Beispiel, das eine Excel-Datei (book1.xls) öffnet, ihre Registerkarten ausblendet und die modifizierte Datei als Output.xls speichert. Nach der Codeausführung werden Sie feststellen, dass die Registerkarten der Arbeitsmappe ausgeblendet sind.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-HideTabs-1.py" >}}

### **Steuerung der Registerkartenleistenbreite**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-ControlTabBarWidth-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
