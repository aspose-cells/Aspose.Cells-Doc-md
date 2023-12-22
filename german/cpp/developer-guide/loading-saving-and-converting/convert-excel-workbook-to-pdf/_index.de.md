---
title: Konvertieren Sie die Excel-Arbeitsmappe in PDF
type: docs
weight: 80
url: /de/cpp/convert-excel-workbook-to-pdf/
---
##  **Konvertieren einer Excel-Arbeitsmappe in PDF**
PDF-Dateien werden häufig zum Austausch von Dokumenten zwischen Organisationen, Behörden und Einzelpersonen verwendet. Es handelt sich um ein Standarddokumentformat und Softwareentwickler werden oft gebeten, eine Möglichkeit zu finden, Microsoft-Excel-Dateien in PDF-Dokumente zu konvertieren.

Aspose.Cells unterstützt die Konvertierung von Excel-Dateien in PDF und sorgt für eine hohe visuelle Wiedergabetreue bei der Konvertierung.

{{% alert color="primary" %}} 

 Aspose.Cells schreibt die Informationen zu API und der Versionsnummer direkt in Ausgabedokumente. Wenn Sie beispielsweise das Dokument in PDF rendern, wird Aspose.Cells for C++ ausgefüllt**Anwendung** Feld mit dem Wert 'Aspose.Cells' und**PDF Produzent** Feld mit Wert, z. B. „Aspose.Cells v18.5.0“.

Bitte beachten Sie, dass Sie Aspose.Cells for C++ nicht anweisen können, diese Informationen aus Ausgabedokumenten zu ändern oder zu entfernen.

{{% /alert %}} 
###  **Direkte Konvertierung**
Aspose.Cells unterstützt die Konvertierung von Tabellenkalkulationen in PDF unabhängig von anderer Software. Speichern Sie einfach eine Excel-Datei unter PDF mit[Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)Klasse'[Speichern](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)Methode. Der[Speichern](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)Methode bietet die[SaveFormat_Pdf](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)Aufzählungsmitglied, das die nativen Excel-Dateien in das Format PDF konvertiert.

Führen Sie die folgenden Schritte aus, um die Excel-Tabellen direkt in das Format PDF zu konvertieren:

1.  Instanziieren Sie ein Objekt von[Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)Klasse durch Aufrufen ihres leeren Konstruktors.
1. Sie können eine vorhandene Vorlagendatei öffnen/laden oder diesen Schritt überspringen, wenn Sie die Arbeitsmappe von Grund auf erstellen.
1. Führen Sie beliebige Arbeiten (Eingabe von Daten, Anwenden von Formatierungen, Festlegen von Formeln, Einfügen von Bildern oder anderen Zeichenobjekten usw.) in der Tabelle mithilfe der APIs von Aspose.Cells aus.
1.  Wenn der Tabellenkalkulationscode vollständig ist, rufen Sie auf[Arbeitsmappe](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)Klasse'[Speichern](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)Methode zum Speichern der Tabelle.

Das Dateiformat sollte PDF sein. Wählen Sie daher den entsprechenden Wert PDF (einen vordefinierten Wert) aus der SaveFormat-Enumeration aus, um das endgültige Dokument PDF zu generieren

 Bitte sehen Sie sich den folgenden Beispielcode an:[Beispiel-Excel-Datei](67338368.xlsx) Und[Ausgabe PDF](67338369.pdf) als Referenz.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_DirectConversion-new.cpp" >}}
###  **Erweiterte Konvertierung**
Sie können sich auch für die Verwendung entscheiden[PDFSaveOptions](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)Klasse, um verschiedene Attribute für die Konvertierung festzulegen. Festlegen verschiedener Eigenschaften des**PDFSaveOptions** Mit der Klasse können Sie die Druck-, Schriftart-, Sicherheits- und Komprimierungseinstellungen für die Ausgabe PDF steuern. Die wichtigste Eigenschaft ist[SetCompliance](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/setcompliance/)Dadurch können Sie die Excel-Dateien in PDF/A-kompatiblen PDF-Dateien speichern.
####  **Speichern der Arbeitsmappe in PDF/A-kompatiblen Dateien**
Der folgende Codeausschnitt zeigt die Verwendung von**PDFSaveOptions**Klasse zum Speichern von Excel-Dateien im PDF/A-kompatiblen PDF-Format

 Bitte sehen Sie sich den folgenden Beispielcode und dessen Details an[Ausgabe PDF](67338370.pdf) als Referenz.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_A_CompliedFiles-new.cpp" >}}
####  **Legen Sie die Erstellungszeit PDF fest**
Mit dem**IPdfSaveOptions** Klasse können Sie die Erstellungszeit PDF abrufen oder festlegen.

 Bitte sehen Sie sich den folgenden Beispielcode und dessen Details an[Ausgabe PDF](67338371.pdf) als Referenz.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_SetPDFCreationTime-new.cpp" >}}
