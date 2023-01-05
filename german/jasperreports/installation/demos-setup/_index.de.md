---
title: Demo-Setup
type: docs
weight: 40
url: /de/jasperreports/demos-setup/
---
{{% alert color="primary" %}}

Aspose.Cells for JasperReports enthält eine Reihe von Demoprojekten, die Ihnen beim Einstieg in den Export von Berichten in Microsoft Excel-Dokumentformate aus Ihrer Anwendung helfen sollen.

Die mit Aspose.Cells for JasperReports bereitgestellten Demos sind standardmäßige JasperReports-Demos, die modifiziert wurden, um die Verwendung der neuen Exporter zu demonstrieren.

{{% /alert %}}

Um Aspose.Cells for JasperReports Demos auszuführen, führen Sie die folgenden Schritte aus:

1.  Laden Sie JasperReports herunter (zB<https://sourceforge.net/projects/jasperreports/files/archive/>). Stellen Sie sicher, dass Sie das gesamte archivierte Projekt mit dem Quellcode und den Demos herunterladen, nicht nur ein einzelnes JAR.
1. Entpacken Sie das archivierte Projekt an einen Ort auf Ihrer Festplatte, zB C:\.
1.  Kopieren Sie alle Demo-Ordner aus dem \demo-Ordner von**Aspose.Cells.JasperReports.zip** zu**\<Installationsverzeichnis>\demo\samples**, wo "\<InstallDir>" ist der Speicherort, an dem Sie JasperReports entpackt haben. Dieser Schritt ist erforderlich, da Demo-Build-Skripts auf der Ordnerstruktur von JasperReports basieren, andernfalls müssen Sie Build-Skripts ändern.
1.  Kopieren**aspose.cells.jasperreports.jar** aus dem \lib-Ordner von Aspose.Cells.JasperReports.zip nach**\<Installationsverzeichnis>\lib**.
1.  Ant Build Tool und Ivy Dependency Manager vorbereiten, siehe**\<Installationsverzeichnis>\readme.txt**.
1.  Modifiziere den**build.xml** bei**\<Installationsverzeichnis>\demo\samples**, fügen Sie die aspose.cells.jasperreports.jar in den Klassenpfad ein:
   **\<path id="project-classpath"> ... \<pathelement location="../../lib/aspose.cells.jasperreports.jar"/> </path>**.
1.  Ändern Sie das aktuelle Verzeichnis in**\<Installationsverzeichnis>\demo\hsqldb** und führen Sie die folgende Befehlszeile aus:
   **ant runServer**
1.  Ändern Sie das aktuelle Verzeichnis beispielsweise in eines der Demos Aspose.Cells for JasperReports**\<Installationsverzeichnis>\demo\samples\ac.charts** und führen Sie die folgenden Befehle in der Befehlszeile aus:
   **Ameisentest** - zum Erstellen von Berichtsdateien mit dem Exportprogramm Aspose XLS.
1.  Öffnen Sie beispielsweise eines der resultierenden Dokumente, um es anzuzeigen**\<Installationsverzeichnis>\demo\samples\ac.charts\build\reports\AreaChartReport.xls** in Microsoft Excel oder einer anderen Anwendung.
