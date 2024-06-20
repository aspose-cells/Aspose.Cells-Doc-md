---
title: Ändern des absoluten Pfads der externen Link Datenquellendatei
type: docs
weight: 1020
url: /de/java/change-the-absolute-path-of-external-link-data-source-file/
---

## **Mögliche Verwendungsszenarien**
Wenn Sie den absoluten Pfad der externen Link-Datenquellendatei ändern möchten, verwenden Sie bitte die Eigenschaft [Workbook.AbsolutePath](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#AbsolutePath). Diese Eigenschaft ist zunächst auf den Pfad eingestellt, von dem aus die Excel-Datei geladen wurde. Sie können sie jedoch auf einen leeren String setzen oder auf einen lokalen Ordnerpfad oder einen Pfad für entfernte Netzwerkressourcen. Bei Änderung dieser Eigenschaft wird auch der Pfad der externen Link-Datenquellendatei geändert.
## **Ändern des absoluten Pfads der externen Link-Datenquellendatei**
Der folgende Beispielcode lädt die [Beispieldatei](5472589.xlsx) , die einen externen Link enthält. Zuerst wird die Datenquelle des externen Links gedruckt, dann wird der entfernte Pfad entfernt und erneut gedruckt, diesmal wird die Datenquelle des externen Links mit dem lokalen Pfad gedruckt. Dann wird die Eigenschaft [Workbook.AbsolutePath](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#AbsolutePath) auf einen lokalen und entfernten Pfad geändert und die Datenquelle des externen Links wird erneut gedruckt, wobei die Änderungen in der Konsolenausgabe sichtbar sind.
## **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeAbsolutePathofExternalLink-ChangeAbsolutePathofExternalLink.java" >}}
## **Konsolenausgabe**
Hier ist die Konsolen- oder Debug-Ausgabe nach der Ausführung des obigen Beispielcodes mit der [Beispieldatei](5472589.xlsx).

{{< highlight java >}}

 External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
