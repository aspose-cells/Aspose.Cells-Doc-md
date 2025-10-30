---
title: GridJs Fler språk Konfigurationsguide
type: docs
weight: 250
url: /sv/net/aspose-cells-gridjs/how-to-configuration-multi-language/
description: Denna handledning guidar dig genom att konfigurera flerspråkstöd
keywords: GridJs, flerspråk, lokalisation, internationalisering, kultur, CultureInfo
aliases:
- /net/aspose-cells-gridjs/multi-language/
- /net/aspose-cells-gridjs/multi-language-guide/
- /net/aspose-cells-gridjs/localization-setup/
- /net/aspose-cells-gridjs/multi-language-configuration/
- /net/aspose-cells-gridjs/internationalization-guide/
- /net/aspose-cells-gridjs/culture-configuration/
---

# Aspose.Cells GridJs Flerspråkig Konfigurationsguide

## Översikt

Denna handledning guidar dig genom att konfigurera flerspråkstöd i ditt Aspose.Cells GridJs-projekt. Den täcker både frontend- och backend-konfigurationer.

Tutorialen är baserad på [demo-projekt](https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/tree/master/Examples_GridJs), vänligen justera enligt den faktiska situationen

## Frontend-Konfiguration

I dina frontend-sidor, ställ in gränssnittets språk med `local`-alternativet.

I demo-projektet måste du ändra filen [uidload.html](https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/uidload.html)

Här är ett exempel:

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

I backend-koden måste du ställa in lämplig CultureInfo innan du bearbetar Excel-data.

I demo-projektet måste du ändra [Controller](https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/blob/master/Examples_GridJs/Controllers/GridJs2Controller.cs) filen

### Kontrollpunkter för controller-konfiguration

Följande metoder i din Controller behöver kulturell konfiguration:

#### UpdateCell-metod

Ställ in regionsinformation vid uppdatering av celler:

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

#### DetailFileJsonWithUid-metod

Ställ in regionsinformation när du hämtar Excel JSON

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

#### DetaljStreamJsonMedUid-metod

Ställ in regionsinformation när du strömmar Excel JSON

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

## Viktiga Anmärkningar

1. Frontend och backend språkinställningar måste vara konsekventa.
2. CultureInfo måste anges innan bearbetning av Excel-data.
3. Supported languages: en(Engelska), zh(Kinesiska), es(Spanska), pt(Portugisiska), de(Tyska), ru(Ryska), nl(Holländska), pl(Polska).
4. Exemplet använder polska (pl-PL), men du kan ändra till vilken som helst annan stödd lokal.
