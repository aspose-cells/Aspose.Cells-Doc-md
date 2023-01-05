---
title: Ändern Sie den absoluten Pfad der externen Link-Datenquelldatei
type: docs
weight: 290
url: /de/net/change-the-absolute-path-of-external-link-data-source-file/
---
## Mögliche Nutzungsszenarien

 Wenn Sie den absoluten Pfad der Datenquellendatei des externen Links ändern möchten, verwenden Sie bitte die[**Arbeitsmappe.AbsolutePath**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/absolutepath)Eigentum. Anfänglich wird diese Eigenschaft auf den Pfad gesetzt, aus dem die Excel-Datei geladen wurde. Sie können es jedoch auf eine leere Zeichenfolge oder auf einen lokalen Ordnerpfad oder einen Remote-Netzwerkpfad festlegen. Immer wenn Sie diese Eigenschaft ändern, wird auch der Pfad der externen Link-Datenquelldatei geändert.

## Ändern Sie den absoluten Pfad der externen Link-Datenquelldatei

 Der folgende Beispielcode lädt die[Excel-Beispieldatei](5115146.xlsx) die einen externen Link enthält. Es druckt zuerst die externe Link-Datenquelle, die den entfernten Pfad druckt. Dann entfernt es den Remote-Pfad und druckt erneut, dieses Mal druckt es die externe Link-Datenquelle mit dem lokalen Pfad. Dann ändert sich das[**Arbeitsmappe.AbsolutePath**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/absolutepath)-Eigenschaft in einen lokalen und einen Remote-Pfad und druckt die Datenquelle des externen Links erneut, und die Änderungen werden in der Konsolenausgabe widergespiegelt.

Hier ist die Konsolen- oder Debug-Ausgabe nach der Ausführung des obigen Beispielcodes mit der[Excel-Beispieldatei](5115146.xlsx).

{{< highlight "java" >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
