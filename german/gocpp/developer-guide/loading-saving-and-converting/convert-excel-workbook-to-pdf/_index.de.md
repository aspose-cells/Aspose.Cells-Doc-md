---
title: Excel Arbeitsmappe in PDF konvertieren
type: docs
weight: 80
url: /de/go-cpp/convert-excel-workbook-to-pdf/
---

## **Konvertierung der Excel-Arbeitsmappe in PDF**

Aspose.Cells unterstützt die Konvertierung von Excel-Dateien in PDF und gewährleistet dabei eine hohe visuelle Genauigkeit bei der Konvertierung.

{{% alert color="primary" %}}

Aspose.Cells schreibt direkt die Informationen über API und Versionsnummer in Ausgabedokumente. Zum Beispiel, beim Rendern des Dokuments in PDF, füllt Aspose.Cells for Go via C++ das **Application**-Feld mit dem Wert 'Aspose.Cells' und das **PDF Producer**-Feld mit einem Wert, z.B. 'Aspose.Cells v24.12.0'.

Bitte beachten Sie, dass Sie Aspose.Cells for Go via C++ nicht anweisen können, diese Informationen in Ausgabedokumenten zu ändern oder zu entfernen.

{{% /alert %}}

### **Direkte Konvertierung**

Befolgen Sie die folgenden Schritte, um die Excel-Tabellenkalkulationen direkt in das PDF-Format zu konvertieren:

1. Erstellen Sie ein Objekt der [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) Klasse durch Aufruf ihres leeren Konstruktors.
1. Sie können eine vorhandene Vorlagendatei öffnen/laden oder diesen Schritt überspringen, wenn Sie die Arbeitsmappe von Grund auf erstellen.
1. Führen Sie beliebige Arbeiten (Eingabe von Daten, Anwendung von Formatierungen, Setzen von Formeln, Einfügen von Bildern oder anderen Zeichenobjekten usw.) auf der Tabellenkalkulation mithilfe der APIs von Aspose.Cells durch.
1. Wenn der Code für die Tabellenkalkulation fertig ist, rufen Sie die [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) Klasse's [Save](https://reference.aspose.com/cells/go-cpp/workbook/save/) Methode auf, um die Tabelle zu speichern.

Das Dateiformat sollte PDF sein, wählen Sie also die entsprechende PDF-Option (ein vordefinierter Wert) aus der **SaveFormat** Enumeration, um das endgültige PDF-Dokument zu erstellen.

Bitte sehen Sie sich den folgenden Beispielcode, die [Beispieldatei Excel](67338368.xlsx) und das [Ausgabepdf](67338369.pdf) zu Ihrer Referenz an.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveWorkbookAsPDF.go" >}}
