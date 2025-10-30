---
title: GridJs Çok Dilli Konfigürasyon Kılavuzu
type: docs
weight: 250
url: /tr/net/aspose-cells-gridjs/how-to-configuration-multi-language/
description: Bu eğitim, çok dilli desteği yapılandırmanıza rehberlik edecektir.
keywords: GridJs, çok dilli, yerelleştirme, uluslararasılaştırma, kültür, CultureInfo
aliases:
- /net/aspose-cells-gridjs/multi-language/
- /net/aspose-cells-gridjs/multi-language-guide/
- /net/aspose-cells-gridjs/localization-setup/
- /net/aspose-cells-gridjs/multi-language-configuration/
- /net/aspose-cells-gridjs/internationalization-guide/
- /net/aspose-cells-gridjs/culture-configuration/
---

# Aspose.Cells GridJs Çok Dilli Konfigürasyon Kılavuzu

## Genel Bakış

Bu eğitim, Aspose.Cells GridJs projenizde çok dilli desteği yapılandırmanıza rehberlik edecektir. Hem ön yüz hem de arka uç yapılandırmalarını kapsar.

Eğitici, [demo projesine](https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/tree/master/Examples_GridJs) dayanır, lütfen gerçek duruma göre ayarlayın

## Ön Yüz Yapılandırması

Frontend sayfalarınızda arayüz dilini `local` seçeneği kullanarak ayarlayın.

Demo projesinde, [uidload.html](https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/uidload.html) dosyasını değiştirmeniz gerekir

İşte bir örnek:

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

## Sunucu Yapılandırması

Arka uç kodunda, Excel verisi işlenmeden önce uygun CultureInfo ayarlamanız gerekir.

Demo projesinde, [Controller](https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/blob/master/Examples_GridJs/Controllers/GridJs2Controller.cs) dosyasını değiştirmeniz gerekir

### Kontrol Yönlendirme Noktaları

Aşağıdaki yöntemlerde, Culture ayarları olması gerekir:

#### UpdateCell Yöntemi

Hücreleri güncellerken bölge bilgisi ayarla:

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

#### DetailFileJsonWithUid Yöntemi

Excel JSON alınırken bölge bilgisi ayarla

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

#### DetailStreamJsonWithUid Yöntemi

Excel JSON akışı sırasında bölge bilgisi ayarla

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

## Önemli Notlar

1. Ön yüz ve arka uç dil ayarları tutarlı olmalıdır.
2. Excel verileri işlenmeden önce CultureInfo ayarlanmalıdır.
3. Desteklenen diller: en(İngilizce), zh(Çince), es(İspanyolca), pt(Portekizce), de(Almanca), ru(Rusça), nl(Hollanda), pl(Lehçe).
4. Örnek Polonyaca (pl-PL) kullanır, ancak başka herhangi bir desteklenen bölgeye değiştirebilirsiniz.
