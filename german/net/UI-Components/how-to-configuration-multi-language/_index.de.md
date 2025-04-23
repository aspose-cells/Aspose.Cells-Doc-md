---
title: GridJs Mehrsprachigkeitskonfigurationsanleitung
type: docs
weight: 250
url: /de/net/aspose-cells-gridjs/how-to-configuration-multi-language/
description: Dieses Tutorial führt Sie durch die Konfiguration der Mehrsprachigkeit.
keywords: GridJs, Mehrsprachigkeit, Lokalisierung, Internationalisierung, Kultur, CultureInfo
aliases:
- /net/aspose-cells-gridjs/multi-language/
- /net/aspose-cells-gridjs/multi-language-guide/
- /net/aspose-cells-gridjs/localization-setup/
- /net/aspose-cells-gridjs/multi-language-configuration/
- /net/aspose-cells-gridjs/internationalization-guide/
- /net/aspose-cells-gridjs/culture-configuration/
---

# Aspose.Cells GridJs Mehrsprachigkeitskonfigurationsleitfaden

## Übersicht

Dieses Tutorial führt Sie durch die Konfiguration der Mehrsprachigkeit in Ihrem Aspose.Cells GridJs-Projekt. Es behandelt sowohl Frontend- als auch Backend-Konfigurationen.

Das Tutorial basiert auf dem [Demo-Projekt](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs), passen Sie es je nach Situation an.

## Frontend-Konfiguration

Auf Ihren Frontend-Seiten setzen Sie die Schnittstellent Sprache mit der Option `local`.

Im Demo-Projekt müssen Sie die Datei [uidload.html](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/uidload.html) ändern.

Hier ist ein Beispiel:

```javascript
const loadNormalContext = (sheet) => {
    const option = {
        updateMode: 'server',
        updateUrl: '/GridJs2/UpdateCell',
        showToolbar: true,
        mode: 'edit',
        // Supported languages: en/zh/es/pt/de/ru/nl/pl
        local: 'pl', // Set to Polish in this example
    };
    loadWithOption(jsondata, option);
};
```

## Backend-Konfiguration

Im Backend-Code müssen Sie die entsprechende CultureInfo vor der Verarbeitung der Excel-Daten einstellen.

Im Demo-Projekt müssen Sie die [Controller](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/Controllers/GridJs2Controller.cs) Datei ändern.

### Punkte zur Controller-Konfiguration

Folgende Methoden in Ihrem Controller benötigen eine Kulturkonfiguration:

#### UpdateCell-Methode

Setzen Sie Regionsinformationen beim Aktualisieren von Zellen:

```csharp
[HttpPost]
public ActionResult UpdateCell()
{
    // Set culture info
    CultureInfo polishCulture = new CultureInfo("pl-PL");
    Thread.CurrentThread.CurrentCulture = polishCulture;
    Thread.CurrentThread.CurrentUICulture = polishCulture;

    string p = HttpContext.Request.Form["p"];
    string uid = HttpContext.Request.Form["uid"];
    GridJsWorkbook gwb = new GridJsWorkbook();
    String ret = gwb.UpdateCell(p, uid);
    return Content(ret, "text/plain", System.Text.Encoding.UTF8);
}
```

#### DetailFileJsonWithUid-Methode

Regioninformationen beim Abrufen von Excel-JSON festlegen

```csharp
public ActionResult DetailFileJsonWithUid(string filename, string uid)
{
    // Set culture info
    CultureInfo polishCulture = new CultureInfo("pl-PL");
    Thread.CurrentThread.CurrentCulture = polishCulture;
    Thread.CurrentThread.CurrentUICulture = polishCulture;

    String file = Path.Combine(TestConfig.ListDir, filename);
    GridJsWorkbook wbj = new GridJsWorkbook();
    StringBuilder sb = wbj.GetJsonByUid(uid, filename);
    if(sb == null)
    {
        Workbook wb = new Workbook(file);
        wbj.ImportExcelFile(uid, wb);
        sb = wbj.ExportToJsonStringBuilder(filename);
    }
    return Content(sb.ToString(), "text/plain", System.Text.Encoding.UTF8);
}
```

#### DetailStreamJsonWithUid Methode

Regioninformationen beim Streaming von Excel-JSON festlegen

```csharp
public ActionResult DetailStreamJsonWithUid(string filename, string uid)
{
    // Set culture info
    CultureInfo polishCulture = new CultureInfo("pl-PL");
    Thread.CurrentThread.CurrentCulture = polishCulture;
    Thread.CurrentThread.CurrentUICulture = polishCulture;

    String file = Path.Combine(TestConfig.ListDir, filename);
    GridJsWorkbook wbj = new GridJsWorkbook();
    Response.ContentType = "application/json";
    Response.Headers.Add("Content-Encoding", "gzip");
    using (GZipStream gzip = new GZipStream(Response.Body, CompressionLevel.Optimal))
    {
        bool isdone = wbj.JsonToStreamByUid(gzip, uid, filename);
        if(!isdone)
        {
            Workbook wb = new Workbook(file);
            wbj.ImportExcelFile(uid, wb);
            wbj.JsonToStream(gzip, filename);
        }
    }
    return new EmptyResult();
}
```

## Wichtige Hinweise

1. Frontend- und Backend-Spracheneinstellungen müssen übereinstimmen.
2. CultureInfo muss vor der Verarbeitung von Excel-Daten festgelegt werden.
3. Unterstützte Sprachen: en(Englisch), zh(Chinesisch), es(Spanisch), pt(Portugiesisch), de(Deutsch), ru(Russisch), nl( Niederländisch), pl(Polnisch).
4. Das Beispiel verwendet Polnisch (pl-PL), aber Sie können es auf jede andere unterstützte Sprache ändern.
