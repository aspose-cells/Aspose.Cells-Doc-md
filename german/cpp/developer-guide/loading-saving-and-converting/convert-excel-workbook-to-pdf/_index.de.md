---
title: Konvertieren Sie die Excel-Arbeitsmappe in PDF
type: docs
weight: 80
url: /de/cpp/convert-excel-workbook-to-pdf/
---
## **Konvertieren der Excel-Arbeitsmappe in PDF**
PDF-Dateien werden häufig zum Austausch von Dokumenten zwischen Organisationen, Regierungssektoren und Einzelpersonen verwendet. Es ist ein Standarddokumentformat und Softwareentwickler werden oft gebeten, einen Weg zu finden, Microsoft-Excel-Dateien in PDF-Dokumente umzuwandeln.

Aspose.Cells unterstützt die Konvertierung von Excel-Dateien in PDF und behält eine hohe visuelle Wiedergabetreue bei der Konvertierung bei.

{{% alert color="primary" %}} 

 Aspose.Cells schreibt die Informationen über API und die Versionsnummer direkt in Ausgabedokumente. Zum Beispiel wird beim Rendern von Document zu PDF Aspose.Cells for C++ gefüllt**Anwendung** Feld mit dem Wert 'Aspose.Cells' und**PDF Hersteller** Feld mit Wert, zB 'Aspose.Cells v18.5.0'.

Bitte beachten Sie, dass Sie Aspose.Cells for C++ nicht anweisen können, diese Informationen aus Ausgabedokumenten zu ändern oder zu entfernen.

{{% /alert %}} 
### **Direkte Konvertierung**
Aspose.Cells unterstützt die Konvertierung von Tabellenkalkulationen zu PDF unabhängig von anderer Software. Speichern Sie einfach eine Excel-Datei unter PDF mit der[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)Klasse'[Speichern](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)Methode. Das[Speichern](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)Methode bietet die[SaveFormat_Pdf](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a)Enumerationsmember, der die nativen Excel-Dateien in das PDF-Format konvertiert.

Führen Sie die folgenden Schritte aus, um die Excel-Tabellen direkt in das Format PDF zu konvertieren:

1.  Instanziieren Sie ein Objekt der[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)Klasse, indem Sie ihren leeren Konstruktor aufrufen.
1. Sie können eine vorhandene Vorlagendatei öffnen/laden oder diesen Schritt überspringen, wenn Sie die Arbeitsmappe von Grund auf neu erstellen.
1. Führen Sie alle Arbeiten (Daten eingeben, Formatierung anwenden, Formeln festlegen, Bilder oder andere Zeichnungsobjekte einfügen usw.) in der Tabelle mithilfe von Aspose.Cells-APIs durch.
1.  Wenn der Tabellenkalkulationscode vollständig ist, rufen Sie die auf[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)Klasse'[Speichern](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)Methode zum Speichern der Tabelle.

Das Dateiformat sollte PDF sein, wählen Sie also den relevanten PDF (einen vordefinierten Wert) aus der SaveFormat-Enumeration aus, um das endgültige PDF-Dokument zu generieren

 Bitte sehen Sie sich den folgenden Beispielcode an, its[Beispiel-Excel-Datei](67338368.xlsx) und[Ausgang PDF](67338369.pdf) für ihre referenz.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_DirectConversion.cpp" >}}
### **Erweiterte Konvertierung**
Sie können sich auch für die Verwendung entscheiden[IPdfSaveOptions](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_pdf_save_options)-Klasse, um verschiedene Attribute für die Konvertierung festzulegen. Festlegen verschiedener Eigenschaften der**IPdfSaveOptions** -Klasse gibt Ihnen die Kontrolle über die Druck-, Schriftart-, Sicherheits- und Komprimierungseinstellungen für die Ausgabe PDF. Die wichtigste Eigenschaft ist[SetCompliance](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_pdf_save_options#a2158ff23d7c071f8224b1cd063233c07)Dadurch können Sie die Excel-Dateien in PDF/A-kompatible PDF-Dateien speichern.
#### **Speichern der Arbeitsmappe in PDF/A Kompilierte Dateien**
Das folgende Code-Snippet zeigt, wie Sie die verwenden**IPdfSaveOptions**Klasse zum Speichern von Excel-Dateien im PDF/A-kompatiblen PDF-Format

 Bitte sehen Sie sich den folgenden Beispielcode und seine an[Ausgang PDF](67338370.pdf) für ihre referenz.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_A_CompliedFiles.cpp" >}}
#### **Stellen Sie die Erstellungszeit PDF ein**
Mit dem**IPdfSaveOptions** Klasse können Sie die Erstellungszeit PDF erhalten oder festlegen.

 Bitte sehen Sie sich den folgenden Beispielcode und seine an[Ausgang PDF](67338371.pdf) für ihre referenz.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_SetPDFCreationTime.cpp" >}}
