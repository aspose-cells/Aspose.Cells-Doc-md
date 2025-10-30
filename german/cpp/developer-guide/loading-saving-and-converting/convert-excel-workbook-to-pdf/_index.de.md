---
title: Excel Arbeitsmappe in PDF konvertieren
type: docs
weight: 80
url: /de/cpp/convert-excel-workbook-to-pdf/
---

## **Konvertierung der Excel-Arbeitsmappe in PDF**
PDF-Dateien werden weit verbreitet eingesetzt, um Dokumente zwischen Organisationen, Regierungsbereichen und Einzelpersonen auszutauschen. Es handelt sich um ein standardisiertes Dokumentenformat, und Softwareentwickler werden oft gebeten, eine Möglichkeit zu finden, Microsoft Excel-Dateien in PDF-Dokumente zu konvertieren.

Aspose.Cells unterstützt die Konvertierung von Excel-Dateien in PDF und gewährleistet dabei eine hohe visuelle Genauigkeit bei der Konvertierung.

{{% alert color="primary" %}} 

Aspose.Cells schreibt die Informationen über API und Versionsnummer direkt in die Ausgabedokumente. Beispielsweise, beim Rendern des Dokuments in PDF, Aspose.Cells for C++ füllt das **Anwendungs**-Feld mit dem Wert 'Aspose.Cells' und das **PDF-Produzent**-Feld mit dem Wert, z.B. 'Aspose.Cells v18.5.0'.

{{% /alert %}} 
### **Direkte Konvertierung**
Aspose.Cells unterstützt die Konvertierung von Tabellenkalkulationen in PDF unabhängig von anderen Software. Speichern Sie einfach eine Excel-Datei als PDF mithilfe der Methode [Speichern](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) der Klasse [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). Die Methode [Speichern](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) bietet das Enumerationsmember [SaveFormat_Pdf](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/), der native Excel-Dateien in das PDF-Format konvertiert.

Befolgen Sie die folgenden Schritte, um die Excel-Tabellenkalkulationen direkt in das PDF-Format zu konvertieren:

1. Instanziieren Sie ein Objekt der Klasse [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) durch Aufrufen seines leeren Konstruktors.
1. Sie können eine vorhandene Vorlagendatei öffnen/laden oder diesen Schritt überspringen, wenn Sie die Arbeitsmappe von Grund auf erstellen.
1. Führen Sie beliebige Arbeiten (Eingabe von Daten, Anwendung von Formatierungen, Setzen von Formeln, Einfügen von Bildern oder anderen Zeichenobjekten usw.) auf der Tabellenkalkulation mithilfe der APIs von Aspose.Cells durch.
1. Wenn der Tabellenkalkulationscode vollständig ist, rufen Sie die Methode [Speichern](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) der Klasse [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) auf, um die Tabellenkalkulation zu speichern.

Das Dateiformat sollte PDF sein. Wählen Sie zur Generierung des endgültigen PDF-Dokuments das relevante PDF (einen vordefinierten Wert) aus der Enumeration SaveFormat aus.

Bitte sehen Sie sich den folgenden Beispielcode sowie die [Beispiel-Excel-Datei](67338368.xlsx) und das [Ausgabepdf](67338369.pdf) zu Ihrer Referenz an.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_DirectConversion-new.cpp" >}}
### **Erweiterte Konvertierung**
Sie können auch die Klasse [PdfSaveOptions](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) verwenden, um verschiedene Attribute für die Konvertierung festzulegen. Durch das Setzen verschiedener Eigenschaften der Klasse **PdfSaveOptions** haben Sie Kontrolle über die Druck-, Schriftarten-, Sicherheits- und Kompressionseinstellungen für das Ausgabepdf. Die wichtigste Eigenschaft ist [SetCompliance](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/setcompliance/), mit der Sie Excel-Dateien in PDF/A-konforme PDF-Dateien speichern können.
#### **Speichern der Arbeitsmappe als PDF/A-kompatible Dateien**
Der folgende Code-Ausschnitt zeigt, wie die Klasse **PdfSaveOptions** zum Speichern von Excel-Dateien im PDF/A-konformen PDF-Format verwendet wird.

Bitte sehen Sie sich den folgenden Beispielcode und das [Ausgabepdf](67338370.pdf) zu Ihrer Referenz an.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_A_CompliedFiles-new.cpp" >}}
#### **Legen Sie die Erstellungszeit des PDF fest**
Mit der Klasse **IPdfSaveOptions** können Sie die Erstellungszeit des PDF abrufen oder festlegen.

Bitte sehen Sie sich den folgenden Beispielcode und das [Ausgabepdf](67338371.pdf) zu Ihrer Referenz an.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_SetPDFCreationTime-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
