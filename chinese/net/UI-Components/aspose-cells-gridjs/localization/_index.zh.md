---
title: GridJs 多语言配置指南
type: docs
weight: 250
url: /zh/net/aspose-cells-gridjs/how-to-configuration-multi-language/
description: 本教程将引导您配置多语言支持
keywords: GridJs、多语言、本地化、国际化、文化、CultureInfo
aliases:
- /net/aspose-cells-gridjs/multi-language/
- /net/aspose-cells-gridjs/multi-language-guide/
- /net/aspose-cells-gridjs/localization-setup/
- /net/aspose-cells-gridjs/multi-language-configuration/
- /net/aspose-cells-gridjs/internationalization-guide/
- /net/aspose-cells-gridjs/culture-configuration/
---

# Aspose.Cells GridJs 多语言配置指南

## 概述

本教程将引导您在 Aspose.Cells GridJs 项目中配置多语言支持。涵盖前端和后端配置内容。

该教程基于[演示项目](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs)，请根据实际情况调整。

## 前端配置

在前端页面中，使用 `local` 选项设置界面语言。

在演示项目中，需修改 [uidload.html](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/wwwroot/xspread/uidload.html) 文件

以下是一个例子：

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

## 后端配置

在后端代码中，处理Excel数据前需要设置合适的 CultureInfo。

在演示项目中，需修改 [Controller](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/Controllers/GridJs2Controller.cs) 文件

### 控制器配置要点

控制器中的以下方法需要进行文化配置：

#### UpdateCell 方法

更新单元格时设置区域信息：

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

#### DetailFileJsonWithUid 方法

获取Excel JSON时设置区域信息

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

#### DetailStreamJsonWithUid 方法

流式获取Excel JSON时设置区域信息

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

## 重要说明

1. 前端和后端的语言设置必须一致。
2. 在处理Excel数据之前，必须设置CultureInfo。
3. 支持的语言：en（英语）、zh（中文）、es（西班牙语）、pt（葡萄牙语）、de（德语）、ru（俄语）、nl（荷兰语）、pl（波兰语）。
4. 示例使用波兰语（pl-PL），但可以更改为其他支持的区域设置。
