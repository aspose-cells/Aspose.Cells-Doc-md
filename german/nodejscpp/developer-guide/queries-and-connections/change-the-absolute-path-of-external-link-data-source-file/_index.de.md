---
title: Ändern Sie den absoluten Pfad der externen Link Datenquelle Datei mit Node.js über C++
linktitle: Ändern des absoluten Pfads der externen Link Datenquellendatei
type: docs
weight: 290
url: /de/nodejs-cpp/change-the-absolute-path-of-external-link-data-source-file/
description: Erfahren Sie, wie Sie den absoluten Pfad der externen Link Datenquelle mit Aspose.Cells for Node.js via C++ ändern. 
---

## Mögliche Anwendungsszenarien

Wenn Sie den absoluten Pfad der externen Link-Datenquelle ändern möchten, verwenden Sie bitte die Eigenschaft [**Workbook.getAbsolutePath()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getAbsolutePath--). Anfangs ist diese auf den Pfad gesetzt, von dem die Excel-Datei geladen wurde. Sie können sie aber auch auf einen leeren String setzen oder auf einen lokalen Ordnerpfad oder einen Remote-Netzwerkpfad. Jedes Mal, wenn Sie diese Eigenschaft ändern, wird auch der Pfad der externen Link-Datenquelle angepasst.

## Ändern Sie den absoluten Pfad der externen Verknüpfungsdatenquelle

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](5115146.xlsx), die eine externe Verknüpfung enthält. Zuerst gibt er die externe Link-Datenquelle aus, die den Remote-Pfad anzeigt. Dann entfernt er den Remote-Pfad und gibt erneut aus; diesmal zeigt er die externe Link-Datenquelle mit dem lokalen Pfad. Danach ändert er die [**Workbook.getAbsolutePath()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getAbsolutePath--)-Eigenschaft auf einen lokalen und einen Remote-Pfad und gibt die externe Link-Datenquelle erneut aus, wobei die Änderungen in der Konsolenausgabe sichtbar sind.

Hier ist die Konsolen- oder Debug-Ausgabe nach der Ausführung des obigen Beispielcodes mit der [Beispiel-Excel-Datei](5115146.xlsx).

{{< highlight javascript >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
