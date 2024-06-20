---
title: Öffentliche API Änderungen in Aspose.Cells 8.1.2
type: docs
weight: 60
url: /de/net/public-api-changes-in-aspose-cells-8-1-2/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt Änderungen an der Aspose.Cells API von Version 8.1.1 auf 8.1.2, die für Modul-/Anwendungs-Entwickler von Interesse sein könnten. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, sondern auch eine Beschreibung etwaiger Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **Hinzufügen von Unterstützung für Warnungen bei Schriftarten-Ersatz**
Mit Aspose.Cells for .NET 8.1.2 wurden die Klassen WarningInfo, WarningType, das Interface IWarningCallback und die Eigenschaften SaveOptions.WarningCallback und ImageOrPrintOptions.WarningCallback hinzugefügt, um dem Benutzer das Empfangen einer Warnung zu ermöglichen, wenn bei der Konvertierung von Tabellenkalkulationen in Bilder oder das PDF-Format eine Schriftart ausgetauscht wird. 

{{% alert color="primary" %}} 

Bitte prüfen Sie den ausführlichen Artikel zu [Erhalt von Warnungen bei Schriftarten-Ersatz beim Rendern von Tabellenkalkulationen](http://aspose.com/docs/display/cellsnet/Get+Warnings+for+Font+Substitution+while+Rendering+Excel+File)

{{% /alert %}}
## **Entfernen der veralteten PdfSaveOptions.ChartImageType-Eigenschaft**
Aspose.Cells for .NET 8.1.2 hat die veraltete PdfSaveOptions.ChartImageType-Eigenschaft aus der öffentlichen API entfernt.
