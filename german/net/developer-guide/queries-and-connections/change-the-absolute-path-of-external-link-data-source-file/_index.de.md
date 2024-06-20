---
title: Ändern des absoluten Pfads der externen Link Datenquellendatei
type: docs
weight: 290
url: /de/net/change-the-absolute-path-of-external-link-data-source-file/
---

## Mögliche Anwendungsszenarien

Wenn Sie den absoluten Pfad der externen Verknüpfungsdatenquelle ändern möchten, verwenden Sie bitte die [**Workbook.AbsolutePath**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/absolutepath)-Eigenschaft. Diese Eigenschaft wird ursprünglich auf den Pfad eingestellt, von dem aus die Excel-Datei geladen wurde. Sie können sie jedoch auf einen leeren String setzen oder auf einen lokalen Ordnerpfad oder Netzwerkpfad. Wenn Sie diese Eigenschaft ändern, wird auch der Pfad der externen Verknüpfungsdatenquelle geändert.

## Ändern Sie den absoluten Pfad der externen Verknüpfungsdatenquelle

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](5115146.xlsx), die eine externe Verknüpfung enthält. Zuerst wird die externe Verknüpfungsdatenquelle gedruckt, die den entfernten Pfad angibt. Dann wird der entfernte Pfad entfernt und erneut gedruckt, dieses Mal wird die externe Verknüpfungsdatenquelle mit dem lokalen Pfad gedruckt. Dann wird die [**Workbook.AbsolutePath**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/absolutepath)-Eigenschaft auf einen lokalen und entfernten Pfad geändert und die externe Verknüpfungsdatenquelle erneut gedruckt, und die Änderungen werden in der Konsolenausgabe widergespiegelt.

Hier ist die Konsolen- oder Debug-Ausgabe nach der Ausführung des obigen Beispielcodes mit der [Beispiel-Excel-Datei](5115146.xlsx).

{{< highlight java >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
