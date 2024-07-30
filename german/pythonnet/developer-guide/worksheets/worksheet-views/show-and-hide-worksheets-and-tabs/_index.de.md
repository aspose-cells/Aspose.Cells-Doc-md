---
title: Arbeitsblätter und Registerkarten anzeigen und ausblenden
type: docs
weight: 10
url: /de/python-net/show-and-hide-worksheets-and-tabs/
description: Dieser Artikel enthält Beispielcode zur Verwendung der Aspose.Cells for Python via .NET API, um ein Excel Arbeitsblatt programmgesteuert anzuzeigen und auszublenden. Zusätzlich, wie man Excel Arbeitsmappenregisterkarten anzeigen und ausblenden kann.
keywords: Python Excel Bibliothek, Python Arbeitsblatt anzeigen und ausblenden, Python Registerkarten anzeigen und ausblenden, Python Steuerung der Registerkartenleistenbreite.
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET ermöglicht es dem Benutzer, Elemente einer Arbeitsmappe wie Arbeitsblätter und Registerkarten anzuzeigen und auszublenden.

{{% /alert %}}

## **Arbeitsblatt anzeigen und ausblenden**

Eine Excel-Datei kann ein oder mehrere Arbeitsblätter haben. Immer wenn wir eine Excel-Datei erstellen, fügen wir Arbeitsblätter zur Excel-Datei hinzu, in der wir arbeiten. Jedes Arbeitsblatt in einer Excel-Datei ist unabhängig von den anderen Arbeitsblättern, indem es über eigene Daten und Formatierungseinstellungen etc. verfügt. Manchmal müssen Entwickler einige Arbeitsblätter in der Excel-Datei ausblenden und andere für ihr eigenes Interesse sichtbar machen. So erlaubt es **Aspose.Cells für Python via .NET** Entwicklern, die Sichtbarkeit der Arbeitsblätter in ihren Excel-Dateien zu steuern.

Aspose.Cells for Python via .NET bietet eine Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), die eine Excel-Datei darstellt. Die Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) enthält eine Sammlung [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets), die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

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

Mit Aspose.Cells für Python via .NET können Entwickler die Sichtbarkeit von Registerkarten und Registerkarten-Scrolling-Schaltflächen in Excel-Dateien steuern.

Aspose.Cells für Python via .NET bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), die eine Excel-Datei darstellt. Die [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) Klasse bietet eine Vielzahl von Eigenschaften und Methoden zur Verwaltung einer Excel-Datei. Um die Sichtbarkeit von Registerkarten in einer Excel-Datei zu steuern, können Entwickler die [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) Klasse verwenden. [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) ist eine boolesche Eigenschaft, was bedeutet, dass sie nur einen **true** oder **false** Wert speichern kann.

### **Sichtbarkeit von Registerkarten**

Machen Sie Registerkarten mit der Eigenschaft [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) der Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) auf **true** sichtbar.

### **Registerkarten ausblenden**

Blenden Sie Registerkarten in einer Excel-Datei aus, indem Sie die Eigenschaft [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) der Klasse [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) auf false setzen.

Nachfolgend finden Sie ein vollständiges Beispiel, das eine Excel-Datei (book1.xls) öffnet, ihre Registerkarten ausblendet und die modifizierte Datei als Output.xls speichert. Nach der Codeausführung werden Sie feststellen, dass die Registerkarten der Arbeitsmappe ausgeblendet sind.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-HideTabs-1.py" >}}

### **Steuerung der Registerkartenleistenbreite**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-ControlTabBarWidth-1.py" >}}
