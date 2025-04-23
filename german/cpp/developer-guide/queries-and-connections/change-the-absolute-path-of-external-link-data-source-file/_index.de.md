---
title: Ändern Sie den absoluten Pfad der externen Link Datenquelle mit C++
linktitle: Ändern des absoluten Pfads der externen Link Datenquellendatei
type: docs
weight: 290
url: /de/cpp/change-the-absolute-path-of-external-link-data-source-file/
description: Ändern Sie den absoluten Pfad der externen Link Datenquelle in Aspose.Cells mit C++.
---

## Mögliche Anwendungsszenarien

Wenn Sie den absoluten Pfad der externen Link-Datenquelle ändern möchten, verwenden Sie bitte die [**GetAbsolutePath()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getabsolutepath/)-Methode. Anfangs ist diese Eigenschaft auf den Pfad gesetzt, von dem aus die Excel-Datei geladen wurde. Sie können sie jedoch auf eine leere Zeichenfolge setzen oder auf einen lokalen Ordnerpfad oder einen entfernten Netzwerklaufwerks-Pfad. Jedes Mal, wenn Sie diese Eigenschaft ändern, wird auch der Pfad der externen Link-Datenquelle aktualisiert.

## Ändern Sie den absoluten Pfad der externen Verknüpfungsdatenquelle

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](5115146.xlsx), die eine externe Verknüpfung enthält. Zuerst gibt er die externe Link-Datenquelle aus, die den Remote-Pfad zeigt. Dann entfernt er den Remote-Pfad und gibt erneut aus, diesmal mit lokalem Pfad. Danach ändert er die [**GetAbsolutePath()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getabsolutepath/)-Methode auf einen lokalen und einen Remote-Pfad und gibt die externe Link-Datenquelle erneut aus, wobei die Änderungen in der Konsolenausgabe reflektiert werden.

Hier ist die Konsolen- oder Debug-Ausgabe nach der Ausführung des obigen Beispielcodes mit der [Beispiel-Excel-Datei](5115146.xlsx).

{{< highlight cpp >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
