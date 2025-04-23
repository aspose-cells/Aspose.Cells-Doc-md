---
title: Öffentliche API Änderungen in Aspose.Cells 8.1.2
type: docs
weight: 70
url: /de/java/public-api-changes-in-aspose-cells-8-1-2/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt Änderungen an der Aspose.Cells API von Version 8.1.1 auf 8.1.2, die für Modul-/Anwendungs-Entwickler von Interesse sein könnten. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, sondern auch eine Beschreibung etwaiger Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzufügen von Unterstützung für Warnungen bei Schriftarten-Ersatz**
Mit Aspose.Cells for Java 8.1.2 wurden die Klassen WarningInfo und WarningType, das Interface IWarningCallback sowie die Eigenschaften SaveOptions.WarningCallback und ImageOrPrintOptions.WarningCallback hinzugefügt, um den Entwicklern zu ermöglichen, Warnungen zu erhalten, wenn bei der Konvertierung von Tabellenkalkulationen in Bilder, XPS- & PDF-Formate Schriftarten-Ersatz auftritt. 

{{% alert color="primary" %}} 

Bitte überprüfen Sie den ausführlichen Artikel zu [Warnungen für Schriftarten-Ersatz beim Rendern von Tabellenkalkulationen](http://aspose.com/docs/display/cellsjava/Get+Warnings+for+Font+Substitution+while+Rendering+Excel+File) für weitere Informationen.

{{% /alert %}}
## **Entfernen der veralteten PdfSaveOptions.ChartImageType-Eigenschaft**
Aspose.Cells for Java 8.1.2 hat die veraltete PdfSaveOptions.ChartImageType-Eigenschaft aus der öffentlichen API entfernt.
{{< app/cells/assistant language="java" >}}
