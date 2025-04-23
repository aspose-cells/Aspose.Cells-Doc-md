---
title: Guide de configuration multilingue de GridJs
type: docs
weight: 250
url: /fr/net/aspose-cells-gridjs/how-to-configuration-multi-language/
description: Ce tutoriel vous guidera dans la configuration du support multilingue
keywords: GridJs, multilingue, localisation, internationalisation, culture, CultureInfo
aliases:
- /net/aspose-cells-gridjs/multi-language/
- /net/aspose-cells-gridjs/multi-language-guide/
- /net/aspose-cells-gridjs/localization-setup/
- /net/aspose-cells-gridjs/multi-language-configuration/
- /net/aspose-cells-gridjs/internationalization-guide/
- /net/aspose-cells-gridjs/culture-configuration/
---

# Guide de configuration multilingue Aspose.Cells GridJs

## Aperçu

Ce tutoriel vous guidera dans la configuration du support multilingue dans votre projet Aspose.Cells GridJs. Il couvre les configurations côté frontend et backend.

Le tutoriel est basé sur le [projet de démonstration](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs), veuillez l'ajuster en fonction de la situation réelle

## Configuration frontend

Dans vos pages frontend, définissez la langue de l'interface en utilisant l'option `local`.

Dans le projet de démonstration, vous devez modifier le fichier [uidload.html](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/uidload.html)

Voici un exemple :

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

## Configuration backend

Dans le code backend, vous devez définir le CultureInfo approprié avant de traiter les données Excel.

Dans le projet de démonstration, vous devez modifier le fichier [Controller](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/Controllers/GridJs2Controller.cs)

### Points de configuration du contrôleur

Les méthodes suivantes dans votre contrôleur nécessitent une configuration de la culture :

#### Méthode UpdateCell

Définir les informations de région lors de la mise à jour des cellules :

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

#### Méthode DetailFileJsonWithUid

Définir les informations de région lors de la récupération du JSON Excel

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

#### Méthode DetailStreamJsonWithUid

Définir les informations de région lors de la diffusion du JSON Excel

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

## Notes importantes

1. Les paramètres de langue du frontend et du backend doivent être cohérents.
2. Le CultureInfo doit être défini avant le traitement des données Excel.
3. Langues prises en charge : en (Anglais), zh (Chinois), es (Espagnol), pt (Portuguais), de (Allemand), ru (Russe), nl (Néerlandais), pl (Polonais).
4. L'exemple utilise le polonais (pl-PL), mais vous pouvez le changer pour toute autre locale supportée.
