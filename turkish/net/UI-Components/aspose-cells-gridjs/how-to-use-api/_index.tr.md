---
title: GridJs Sunucu Tarafı ile Çalışmak
type: docs
weight: 250
url: /tr/net/aspose-cells-gridjs/how-to-use-api/
description: Bu makale, GridJs deki API leri nasıl kullanacağınızı açıklar.
keywords: GridJs, sunucu, GridCacheForStream
aliases:
  - /net/aspose-cells-gridjs/server/
  - /net/aspose-cells-gridjs/server-api/
  - /net/aspose-cells-gridjs/api-introduction/
  - /net/aspose-cells-gridjs/how-to-use-apis/
  - /net/aspose-cells-gridjs/work-with-serverside-api/
  - /net/aspose-cells-gridjs/work-with-serverside-apis/
---


# GridJs Sunucu Tarafı ile Çalışmak
## 1. startup.cs'de ConfigureServices içine servis ekleyin 
```C#
   services.AddScoped<IGridJsService, GridJsService>();
```
## 2. Önbellek Dosyalarını Saklamak İçin Yolu Ayarlayın

Aşağıdaki yolları seçebilirsiniz:

 Seçenek 1: GridJsOptions'i Startup.cs'de ConfigureServices içinde ayarlayın
```C#
   services.Configure<GridJsOptions>(options =>
	{
		options.FileCacheDirectory = TestConfig.TempDir;
	});
```

 Seçenek 2: Statik Özelliği Doğrudan Ayarlayın
```C#
   Config.FileCacheDirectory = TestConfig.TempDir;
```

 Seçenek 3: GridCacheForStream'i Uygulayarak Kendi Önbellek Saklama Kurallarınızı Tanımlayın

Yerel dosya depolama için burada bir örnek:

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "LocalFileCache.cs" >}}


Sunucu tarafı depolama için, bir örnek de sunuyoruz. Lütfen kontrol edin: 

<https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/blob/master/Examples_GridJs/Models/AwsCache.cs>


Depolama hakkında daha fazla detay için, lütfen bu [kılavuza](/cells/tr/net/aspose-cells-gridjs/storage/) bakın


## 3. Kontrolcü Eylemlerini Uygula

### 1. GridJsControllerBase'yi Uzatan Bir Kontrolcü Oluşturun
```C#
public class GridJs2Controller : GridJsControllerBase
```
### 2. Eylemde JSON alın

Eyleminizde JSON verisi almak için iki yöntem vardır:

Seçenek 1: GridJsWorkbook kullanma
```C#
GridJsWorkbook wbj = new GridJsWorkbook();
Workbook wb = new Workbook(fullFilePath); 
wbj.ImportExcelFile(wb);
String ret =wbj.ExportToJson(fileName);
```
Seçenek 2: GridJsControllerBase'de IGridJsService kullanma
```C#
 String uid= GridJsWorkbook.GetUidForFile(fileName)
 StringBuilder ret= _gridJsService.DetailFileJsonWithUid(fullFilePath, uid);
```

Detaylı bilgiler için buradaki örneği kontrol edebilirsiniz:
<https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/tree/master/Examples_GridJs>
