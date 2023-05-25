---
title: LoadOptions für GridWeb
type: docs
weight: 90
url: /de/net/aspose-cells-gridweb/loadoptions/
keywords: loadoption,loadoptions,setting,
---
{{% alert color="primary" %}} 

Es gibt einige Ladeoptionen, die wir vor dem Importieren der Datei festlegen können.

 wir können benutzen[GridLoadOptions](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridloadoptions/)(für allgemeine Datei) und[GridTxtLoadOptions](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridtxtloadoptions/) (für CSV-Datei)
 
{{% /alert %}} 
##  ** mit anderer Kodierung laden**
Bei der CSV-Datei handelt es sich tatsächlich um eine textbasierte Datei ohne die in der XLSX-Formatdatei beschriebene spezifische Codierung.

Daher können Benutzer vor dem Laden der Datei eine bestimmte Zeichenkodierung festlegen.

Hier ist ein Beispielcode zum Laden mit Chinesisch:

```csharp
    GridTxtLoadOptions topt = new GridTxtLoadOptions();
    topt.Encoding = (Encoding.GetEncoding("GB2312"));
    GridWeb1.LoadOptions = topt;
    String filePath = Server.MapPath("~/workbook/chinesefile.csv");
    GridWeb1.ImportExcelFile(filePath);
```