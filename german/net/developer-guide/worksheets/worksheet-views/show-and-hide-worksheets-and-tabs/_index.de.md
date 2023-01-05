---
title: Arbeitsblätter und Registerkarten ein- und ausblenden
type: docs
weight: 10
url: /de/net/show-and-hide-worksheets-and-tabs/
description: Dieser Artikel enthält Beispielcode für die Verwendung der Bibliothek C# API oder .NET zum programmgesteuerten Anzeigen und Ausblenden eines Excel-Arbeitsblatts. Außerdem erfahren Sie, wie Sie Excel-Arbeitsmappen-Registerkarten ein- und ausblenden.
---
{{% alert color="primary" %}}

Aspose.Cells ermöglicht dem Benutzer das Ein- und Ausblenden von Elementen einer Arbeitsmappe, einschließlich Arbeitsblättern und Registerkarten.

{{% /alert %}}

## **Ein Arbeitsblatt ein- und ausblenden**

 Eine Excel-Datei kann ein oder mehrere Arbeitsblätter enthalten. Immer wenn wir eine Excel-Datei erstellen, fügen wir der Excel-Datei, in der wir arbeiten, Arbeitsblätter hinzu. Jedes Arbeitsblatt in einer Excel-Datei ist unabhängig von dem anderen Arbeitsblatt, da es seine eigenen Daten und Formatierungseinstellungen usw. hat. Manchmal müssen Entwickler möglicherweise einige Arbeitsblätter ausblenden und andere in der Excel-Datei aus eigenem Interesse sichtbar machen. Damit,**Aspose.Cells** ermöglicht Entwicklern, die Sichtbarkeit der Arbeitsblätter in ihren Excel-Dateien zu steuern.

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , die eine Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht.

 Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-Klasse bietet eine breite Palette von Eigenschaften und Methoden zum Verwalten von Arbeitsblättern. Um die Sichtbarkeit eines Arbeitsblatts zu steuern, verwenden Sie die[**Ist sichtbar**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) Eigentum der[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse.[**Ist sichtbar**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) ist eine boolesche Eigenschaft, was bedeutet, dass sie nur a speichern kann**wahr** oder**FALSCH** Wert.

### **Ein Arbeitsblatt sichtbar machen**

 Machen Sie ein Arbeitsblatt sichtbar, indem Sie das festlegen[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse'[**Ist sichtbar**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) Eigentum zu**wahr**

### **Ausblenden eines Arbeitsblatts**

Blenden Sie ein Arbeitsblatt aus, indem Sie das festlegen[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse'[**Ist sichtbar**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) Eigentum zu**FALSCH**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideUnhideWorksheet-1.cs" >}}

## **Registerkarten ein- und ausblenden**

Wenn Sie sich das Ende einer Microsoft-Excel-Datei genau ansehen, sehen Sie eine Reihe von Steuerelementen. Diese beinhalten:

- Blattregisterkarten.
- Tab-Scroll-Schaltflächen.

Blattregisterkarten stellen die Arbeitsblätter in der Excel-Datei dar. Klicken Sie auf eine beliebige Registerkarte, um zu diesem Arbeitsblatt zu wechseln. Je mehr Arbeitsblätter in der Arbeitsmappe vorhanden sind, desto mehr Blattregisterkarten gibt es. Wenn die Excel-Datei eine große Anzahl von Arbeitsblättern enthält, benötigen Sie Schaltflächen, um durch sie zu navigieren. So stellt Microsoft Excel Schaltflächen zum Scrollen von Registerkarten bereit, um durch die Blattregisterkarten zu scrollen.

Mit Aspose.Cells können Entwickler die Sichtbarkeit von Blattregisterkarten und Schaltflächen zum Scrollen von Registerkarten in Excel-Dateien steuern.

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , die eine Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) -Klasse bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten einer Excel-Datei. Um die Sichtbarkeit von Registerkarten in einer Excel-Datei zu steuern, können Entwickler die[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse'[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) Eigentum.[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) ist eine boolesche Eigenschaft, was bedeutet, dass sie nur a speichern kann**wahr** oder**FALSCH** Wert.

### **Registerkarten sichtbar machen**

 Machen Sie Registerkarten mit sichtbar[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse'[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) Eigentum zu**wahr**.

### **Registerkarten ausblenden**

 Blenden Sie Registerkarten in einer Excel-Datei aus, indem Sie die[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse'[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs)Eigenschaft auf false.

Nachfolgend finden Sie ein vollständiges Beispiel, das eine Excel-Datei (book1.xls) öffnet, ihre Registerkarten ausblendet und die geänderte Datei als output.xls speichert. Nach der Codeausführung sehen Sie, dass die Registerkarten der Arbeitsmappe ausgeblendet sind.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideTabs-1.cs" >}}

### **Steuern der Breite der Registerkartenleiste**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-ControlTabBarWidth-1.cs" >}}
