---
title: Ladeoptionen für GridWeb
type: docs
weight: 90
url: /de/net/aspose-cells-gridweb/aspose-cells-gridweb/loadoptions/
keywords: Lademöglichkeit, Lademöglichkeiten, Einstellung, laden, Optionen, Option
description: Dieser Artikel zeigt, wie man mit Ladeoptionen in GridWeb arbeitet.
---

{{% alert color="primary" %}} 

Es gibt einige Lademöglichkeiten, die wir vor dem Import der Datei einstellen können.

Wir können [GridLoadOptions](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridloadoptions/) (für allgemeine Dateien) und [GridTxtLoadOptions](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridtxtloadoptions/) (für CSV-Dateien) verwenden.	

{{% /alert %}} 
## **Laden mit einer anderen Codierung**
Für die CSV-Datei handelt es sich tatsächlich um eine textbasierte Datei, ohne die in der XLSX-Dateiformatdatei beschriebene spezifische Codierung.

Daher können Benutzer eine spezifische Zeichenkodierung vor dem Laden der Datei festlegen.

Hier ist ein Beispielscode zum Laden mit Chinesisch:

```csharp
    GridTxtLoadOptions topt = new GridTxtLoadOptions();
    topt.Encoding = (Encoding.GetEncoding("GB2312"));
    GridWeb1.LoadOptions = topt;
    String filePath = Server.MapPath("~/workbook/chinesefile.csv");
    GridWeb1.ImportExcelFile(filePath);
```
