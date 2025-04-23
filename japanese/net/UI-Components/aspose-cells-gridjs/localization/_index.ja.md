---
title: GridJs多言語設定ガイド
type: docs
weight: 250
url: /ja/net/aspose-cells-gridjs/how-to-configuration-multi-language/
description: このチュートリアルは、多言語サポートの設定方法をご案内します
keywords: GridJs、多言語、ローカリゼーション、国際化、カルチャー、CultureInfo
aliases:
- /net/aspose-cells-gridjs/multi-language/
- /net/aspose-cells-gridjs/multi-language-guide/
- /net/aspose-cells-gridjs/localization-setup/
- /net/aspose-cells-gridjs/multi-language-configuration/
- /net/aspose-cells-gridjs/internationalization-guide/
- /net/aspose-cells-gridjs/culture-configuration/
---

# Aspose.Cells GridJs 多言語設定ガイド

## 概要

このチュートリアルは、Aspose.Cells GridJsプロジェクトでの多言語サポート設定方法をご案内します。フロントエンドとバックエンドの両方の設定をカバーしています。

このチュートリアルは、[デモプロジェクト](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs)を基にしています。実際の状況に応じて調整してください。

## フロントエンド設定

フロントエンドページで、`local`オプションを使用してインターフェース言語を設定します。

デモプロジェクトでは、[uidload.html](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/uidload.html)ファイルを修正する必要があります。

次に例を示します。

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

## バックエンド設定

バックエンドコードでは、Excelデータを処理する前に適切なCultureInfoを設定する必要があります。

デモプロジェクトでは、[コントローラー](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/Controllers/GridJs2Controller.cs)ファイルを修正する必要があります。

### コントローラー設定ポイント

コントローラーの以下のメソッドにはカルチャー設定が必要です：

#### UpdateCellメソッド

セル更新時にリージョン情報を設定：

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

#### DetailFileJsonWithUidメソッド

Excel JSONを取得する際にリージョン情報を設定：

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

#### DetailStreamJsonWithUid メソッド

Excel JSONをストリーミングするときにリージョン情報を設定する

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

## 重要な注意事項

1. フロントエンドとバックエンドの言語設定は一貫している必要があります。
2. CultureInfoはExcelデータを処理する前に設定する必要があります。
3. サポートされている言語：en（英語）、zh（中国語）、es（スペイン語）、pt（ポルトガル語）、de（ドイツ語）、ru（ロシア語）、nl（オランダ語）、pl（ポーランド語）。
4. 例ではポーランド語（pl-PL）を使用していますが、他のサポートされているロケールに変更できます。
