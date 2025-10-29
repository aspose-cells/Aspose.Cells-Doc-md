---
title: Руководство по настройке мультиязыковой поддержки GridJs
type: docs
weight: 250
url: /ru/net/aspose-cells-gridjs/how-to-configuration-multi-language/
description: Это руководство проведет вас по настройке поддержки нескольких языков
keywords: GridJs, мультиязычность, локализация, интернационализация, культура, CultureInfo
aliases:
- /net/aspose-cells-gridjs/multi-language/
- /net/aspose-cells-gridjs/multi-language-guide/
- /net/aspose-cells-gridjs/localization-setup/
- /net/aspose-cells-gridjs/multi-language-configuration/
- /net/aspose-cells-gridjs/internationalization-guide/
- /net/aspose-cells-gridjs/culture-configuration/
---

# Руководство по настройке мультиязыковой поддержки Aspose.Cells GridJs

## Обзор

Это руководство проведет вас по настройке мультиязыковой поддержки в вашем проекте Aspose.Cells GridJs. Оно охватывает как фронтенд, так и бэкенд настройки.

Руководство основано на [демо-проекте](https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/tree/master/Examples_GridJs), пожалуйста, скорректируйте по ситуации

## Конфигурация фронтенда

На ваших фронтенд-страницах задайте язык интерфейса с помощью опции `local`.

В демо-проекте необходимо изменить файл [uidload.html](https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/uidload.html)

Вот пример:

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

## Конфигурация бэкенда

В коде бэкенда необходимо установить соответствующий CultureInfo перед обработкой данных Excel.

В демо-проекте необходимо изменить файл [Controller](https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/blob/master/Examples_GridJs/Controllers/GridJs2Controller.cs)

### Точки настройки контроллера

Следующие методы в вашем контроллере требуют настройки культуры:

#### Метод UpdateCell

Устанавливайте информацию о регионе при обновлении ячеек:

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

#### Метод DetailFileJsonWithUid

Устанавливатьregion информацию при получении Excel JSON

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

#### Метод DetailStreamJsonWithUid

Устанавливатьregion информацию при потоковой передаче Excel JSON

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

## Важные заметки

1. Языковые настройки фронтенда и бэкенда должны совпадать.
2. CultureInfo должен быть установлен перед обработкой данных Excel.
3. Поддерживаемые языки: en(английский), zh(китайский), es(испанский), pt(португальский), de(немецкий), ru(русский), nl(голландский), pl(польский).
4. В примере используется польский (pl-PL), но его можно изменить на любой другой поддерживаемый язык.
