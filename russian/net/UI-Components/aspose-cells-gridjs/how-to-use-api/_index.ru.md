---
title: Работа с GridJs на стороне сервера
type: docs
weight: 250
url: /ru/net/aspose-cells-gridjs/how-to-use-api/
description: Эта статья описывает, как использовать API в GridJs .
keywords: GridJs, сервер, GridCacheForStream
aliases:
  - /net/aspose-cells-gridjs/server/
  - /net/aspose-cells-gridjs/server-api/
  - /net/aspose-cells-gridjs/api-introduction/
  - /net/aspose-cells-gridjs/how-to-use-apis/
  - /net/aspose-cells-gridjs/work-with-serverside-api/
  - /net/aspose-cells-gridjs/work-with-serverside-apis/
---


# Работа с сервером GridJs
## 1. Добавьте сервис в ConfigureServices в startup.cs 
```C#
   services.AddScoped<IGridJsService, GridJsService>();
```
## 2. Установите путь для хранения файлов кеша

Вы можете выбрать любой из следующих способов:

 Вариант 1: Установка GridJsOptions в ConfigureServices в Startup.cs
```C#
   services.Configure<GridJsOptions>(options =>
	{
		options.FileCacheDirectory = TestConfig.TempDir;
	});
```

 Вариант 2: Прямое установление статического свойства
```C#
   Config.FileCacheDirectory = TestConfig.TempDir;
```

 Вариант 3: Определение собственного правила хранения кеша через реализацию GridCacheForStream

Для локального хранения файлов вот пример:

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "LocalFileCache.cs" >}}


Для хранения на сервере также предоставлен пример. Подробнее смотрите: 

<https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/blob/master/Examples_GridJs/Models/AwsCache.cs>


Подробнее об хранения смотрите в [руководстве](/cells/ru/net/aspose-cells-gridjs/storage/)


## 3. Реализуйте действия в контроллере

### 1. Создайте контроллер, расширяющий GridJsControllerBase
```C#
public class GridJs2Controller : GridJsControllerBase
```
### 2. Получение JSON в действии

Существует два способа получения JSON данных в вашем действии:

Вариант 1: Использование GridJsWorkbook
```C#
GridJsWorkbook wbj = new GridJsWorkbook();
Workbook wb = new Workbook(fullFilePath); 
wbj.ImportExcelFile(wb);
String ret =wbj.ExportToJson(fileName);
```
Вариант 2: Использование IGridJsService в GridJsControllerBase
```C#
 String uid= GridJsWorkbook.GetUidForFile(fileName)
 StringBuilder ret= _gridJsService.DetailFileJsonWithUid(fullFilePath, uid);
```

Для получения дополнительной информации, вы можете проверить пример здесь:
<https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/tree/master/Examples_GridJs>
