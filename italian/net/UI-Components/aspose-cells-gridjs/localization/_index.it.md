---
title: Guida alla configurazione multi lingua di GridJs
type: docs
weight: 250
url: /it/net/aspose-cells-gridjs/how-to-configuration-multi-language/
description: Questa guida ti aiuterà a configurare il supporto multilingue
keywords: GridJs, multilingue, localizzazione, internazionalizzazione, cultura, CultureInfo
aliases:
- /net/aspose-cells-gridjs/multi-language/
- /net/aspose-cells-gridjs/multi-language-guide/
- /net/aspose-cells-gridjs/localization-setup/
- /net/aspose-cells-gridjs/multi-language-configuration/
- /net/aspose-cells-gridjs/internationalization-guide/
- /net/aspose-cells-gridjs/culture-configuration/
---

# Guida alla configurazione multilingue di Aspose.Cells GridJs

## Panoramica

Questa guida ti guiderà nella configurazione del supporto multilingue nel tuo progetto Aspose.Cells GridJs. Copre sia le configurazioni frontend che backend.

La guida si basa sul [progetto demo](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs), si prega di adattarla alla situazione reale

## Configurazione frontend

Nelle tue pagine frontend, imposta la lingua dell'interfaccia utilizzando l'opzione `local`.

Nel progetto demo, è necessario modificare il file [uidload.html](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/uidload.html)

Ecco un esempio:

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

## Configurazione backend

Nel codice backend, è necessario impostare CultureInfo appropriato prima di elaborare i dati Excel.

Nel progetto demo, è necessario modificare il file [Controller](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/Controllers/GridJs2Controller.cs)

### Punti di configurazione del controller

I seguenti metodi nel controller richiedono la configurazione della cultura:

#### Metodo UpdateCell

Imposta le informazioni sulla regione durante l'aggiornamento delle celle:

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

#### Metodo DetailFileJsonWithUid

Imposta le informazioni sulla regione durante il recupero del JSON di Excel

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

#### Metodo DetailStreamJsonWithUid

Imposta le informazioni sulla regione durante la streaming del JSON di Excel

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

## Note importanti

1. Le impostazioni della lingua frontend e backend devono essere coerenti.
2. CultureInfo deve essere impostato prima di elaborare i dati Excel.
3. Lingue supportate: en(inglese), zh(cinese), es(spagnolo), pt(portoghese), de(tedesco), ru(russo), nl(olandese), pl(polacco).
4. L'esempio utilizza il polacco (pl-PL), ma puoi cambiarlo in qualsiasi altra locale supportata.
