---
title: دليل تكوين متعدد اللغات GridJs
type: docs
weight: 250
url: /ar/net/aspose-cells-gridjs/how-to-configuration-multi-language/
description: سيساعدك هذا الدليل على تكوين دعم متعدد اللغات
keywords: GridJs، متعدد اللغات، التعريب، الدولية، الثقافة، CultureInfo
aliases:
- /net/aspose-cells-gridjs/multi-language/
- /net/aspose-cells-gridjs/multi-language-guide/
- /net/aspose-cells-gridjs/localization-setup/
- /net/aspose-cells-gridjs/multi-language-configuration/
- /net/aspose-cells-gridjs/internationalization-guide/
- /net/aspose-cells-gridjs/culture-configuration/
---

# دليل تكوين متعدد اللغات لـ Aspose.Cells GridJs

## نظرة عامة

سيساعدك هذا الدليل على تكوين دعم متعدد اللغات في مشروع Aspose.Cells GridJs الخاص بك. يغطي التكوينات الأمامية والخلفية على حد سواء.

البرنامج التعليمي مستند إلى [مشروع العرض التوضيحي](https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/tree/master/Examples_GridJs)، يرجى التعديل وفقًا للوضع الفعلي

## التكوين الأمامي

في صفحات الواجهة الأمامية الخاصة بك، حدد لغة الواجهة باستخدام الخيار `local`.

في مشروع العرض التوضيحي، تحتاج إلى تعديل ملف [uidload.html](https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/uidload.html)

إليك مثال:

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

## التكوين الخلفي

في كود الخلفية، تحتاج إلى ضبط CultureInfo المناسب قبل معالجة بيانات Excel.

في مشروع العرض التوضيحي، تحتاج إلى تعديل ملف [Controller](https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/blob/master/Examples_GridJs/Controllers/GridJs2Controller.cs)

### نقاط تكوين الوحدة التحكم

الأساليب التالية في وحدة التحكم الخاصة بك تحتاج إلى تكوين الثقافة لها:

#### طريقة UpdateCell

تعيين معلومات المنطقة عند تحديث الخلايا:

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

#### طريقة DetailFileJsonWithUid

تعيين معلومات المنطقة عند استرجاع JSON Excel

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

#### طريقة DetailStreamJsonWithUid

تعيين معلومات المنطقة عند تدفق JSON Excel

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

## ملاحظات مهمة

1. يجب أن تكون إعدادات لغة الواجهة الأمامية والخلفية متطابقة.
2. يجب تعيين CultureInfo قبل معالجة بيانات Excel.
3. اللغات المدعومة: en(الإنجليزية)، zh(الصينية)، es(الإسبانية)، pt(البرتغالية)، de(الألمانية)، ru(الروسية)، nl(الهولندية)، pl(البولندية).
4. يستخدم المثال اللغة البولندية (pl-PL)، ولكن يمكنك تغييرها إلى أي لائحة أخرى مدعومة.
