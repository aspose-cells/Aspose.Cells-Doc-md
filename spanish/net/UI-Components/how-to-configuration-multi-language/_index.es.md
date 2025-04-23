---
title: Guía de configuración multilingüe de GridJs
type: docs
weight: 250
url: /es/net/aspose-cells-gridjs/how-to-configuration-multi-language/
description: Esta tutorial te guiará en la configuración del soporte multilenguaje
keywords: GridJs, multilenguaje, localización, internacionalización, cultura, CultureInfo
aliases:
- /net/aspose-cells-gridjs/multi-language/
- /net/aspose-cells-gridjs/multi-language-guide/
- /net/aspose-cells-gridjs/localization-setup/
- /net/aspose-cells-gridjs/multi-language-configuration/
- /net/aspose-cells-gridjs/internationalization-guide/
- /net/aspose-cells-gridjs/culture-configuration/
---

# Guía de configuración multilingual de Aspose.Cells GridJs

## Resumen

Este tutorial te guiará en la configuración del soporte multilenguaje en tu proyecto Aspose.Cells GridJs. Cubre configuraciones tanto del frontend como del backend.

El tutorial está basado en el [proyecto de demostración](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs), ajusta según la situación actual

## Configuración del frontend

En tus páginas de frontend, establece el idioma de la interfaz usando la opción `local`.

En el proyecto de demostración, necesitas modificar el archivo [uidload.html](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/uidload.html)

Aquí tienes un ejemplo:

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

## Configuración del backend

En el código backend, necesitas establecer la CultureInfo apropiada antes de procesar datos de Excel.

En el proyecto de demostración, necesitas modificar el archivo [Controller](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/Controllers/GridJs2Controller.cs)

### Puntos de configuración del Controller

Los siguientes métodos en tu Controller necesitan configuración de cultura:

#### Método UpdateCell

Establecer información de región al actualizar celdas:

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

#### Método DetailFileJsonWithUid

Establecer información de la región al obtener JSON de Excel

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

#### Método DetailStreamJsonWithUid

Establecer información de la región al transmitir JSON de Excel

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

## Notas importantes

1. Las configuraciones de idioma en frontend y backend deben ser coherentes.
2. La cultura (CultureInfo) debe establecerse antes de procesar datos de Excel.
3. Idiomas soportados: en (Inglés), zh (Chino), es (Español), pt (Portugués), de (Alemán), ru (Ruso), nl (Holandés), pl (Polaco).
4. El ejemplo usa polaco (pl-PL), pero puedes cambiarlo por cualquier otra localidad compatible.
