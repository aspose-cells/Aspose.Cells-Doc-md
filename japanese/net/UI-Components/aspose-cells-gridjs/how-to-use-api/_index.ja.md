---
title: GridJsサーバーサイドで作業する
type: docs
weight: 250
url: /ja/net/aspose-cells-gridjs/how-to-use-api/
description: この記事では、GridJsでAPIを使用する方法について説明しています。
keywords: GridJs,server,GridCacheForStream
aliases:
  - /net/aspose-cells-gridjs/server/
  - /net/aspose-cells-gridjs/server-api/
  - /net/aspose-cells-gridjs/api-introduction/
  - /net/aspose-cells-gridjs/how-to-use-apis/
  - /net/aspose-cells-gridjs/work-with-serverside-api/
  - /net/aspose-cells-gridjs/work-with-serverside-apis/
---


# GridJsサーバーサイドで作業する
## 1. startup.csのConfigureServicesでサービスを追加。 
```C#
   services.AddScoped<IGridJsService, GridJsService>();
```
## 2. キャッシュファイルを保存するパスの設定。

次のいずれかの方法を選択できます。

 オプション1：Startup.csのConfigureServicesでGridJsOptionsを設定。
```C#
   services.Configure<GridJsOptions>(options =>
	{
		options.FileCacheDirectory = TestConfig.TempDir;
	});
```

 オプション2：静的プロパティを直接設定。
```C#
   Config.FileCacheDirectory = TestConfig.TempDir;
```

 オプション3：GridCacheForStreamを実装して独自のキャッシュストレージルールを定義。

ローカルファイルストレージの例は次のとおりです:

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "LocalFileCache.cs" >}}


サーバーサイドストレージの場合、例も提供しています。こちらを確認してください。 

<https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/blob/master/Examples_GridJs/Models/AwsCache.cs>


詳細なストレージについては、こちらの[ガイド](/cells/ja/net/aspose-cells-gridjs/storage/) を参照してください。


## 3. コントローラーアクションの実装。

### 1. GridJsControllerBaseを拡張したコントローラーを作成。
```C#
public class GridJs2Controller : GridJsControllerBase
```
### 2. アクション内でJSONを取得。

アクション内でJSONデータを取得する方法は2つあります：

オプション1：GridJsWorkbookを使用。
```C#
GridJsWorkbook wbj = new GridJsWorkbook();
Workbook wb = new Workbook(fullFilePath); 
wbj.ImportExcelFile(wb);
String ret =wbj.ExportToJson(fileName);
```
オプション2：GridJsControllerBaseのIGridJsServiceを使用。
```C#
 String uid= GridJsWorkbook.GetUidForFile(fileName)
 StringBuilder ret= _gridJsService.DetailFileJsonWithUid(fullFilePath, uid);
```

詳細については、こちらの例をご覧ください：
<https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/tree/master/Examples_GridJs>
