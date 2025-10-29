---
title: Travailler avec GridJs côté serveur
type: docs
weight: 250
url: /fr/net/aspose-cells-gridjs/how-to-use-api/
description: Cet article décrit comment utiliser les API dans GridJs.
keywords: GridJs,serveur,GridCacheForStream
aliases:
  - /net/aspose-cells-gridjs/server/
  - /net/aspose-cells-gridjs/server-api/
  - /net/aspose-cells-gridjs/api-introduction/
  - /net/aspose-cells-gridjs/how-to-use-apis/
  - /net/aspose-cells-gridjs/work-with-serverside-api/
  - /net/aspose-cells-gridjs/work-with-serverside-apis/
---


# Travailler avec GridJs côté serveur
## 1. ajouter un service dans ConfigureServices dans startup.cs 
```C#
   services.AddScoped<IGridJsService, GridJsService>();
```
## 2. Définir le chemin pour stocker les fichiers de cache

Vous pouvez choisir parmi les méthodes suivantes :

 Option 1 : Définir GridJsOptions dans ConfigureServices dans Startup.cs
```C#
   services.Configure<GridJsOptions>(options =>
	{
		options.FileCacheDirectory = TestConfig.TempDir;
	});
```

 Option 2 : Définir directement la propriété statique
```C#
   Config.FileCacheDirectory = TestConfig.TempDir;
```

 Option 3 : Définir votre propre règle de stockage du cache en implémentant GridCacheForStream

Pour le stockage de fichiers local, voici un exemple :

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "LocalFileCache.cs" >}}


Pour le stockage côté serveur, nous fournissons également un exemple. Veuillez vérifier : 

<https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/blob/master/Examples_GridJs/Models/AwsCache.cs>


Pour plus de détails sur le stockage, veuillez consulter ce [guide](/cells/fr/net/aspose-cells-gridjs/storage/)


## 3. Implémenter les actions du contrôleur

### 1. Créer un contrôleur qui hérite de GridJsControllerBase
```C#
public class GridJs2Controller : GridJsControllerBase
```
### 2. Obtenir JSON dans l'action

Il y a deux façons d'obtenir des données JSON dans votre action :

Option 1 : Utiliser GridJsWorkbook
```C#
GridJsWorkbook wbj = new GridJsWorkbook();
Workbook wb = new Workbook(fullFilePath); 
wbj.ImportExcelFile(wb);
String ret =wbj.ExportToJson(fileName);
```
Option 2 : Utiliser IGridJsService dans GridJsControllerBase
```C#
 String uid= GridJsWorkbook.GetUidForFile(fileName)
 StringBuilder ret= _gridJsService.DetailFileJsonWithUid(fullFilePath, uid);
```

Pour plus d'informations, vous pouvez consulter l'exemple ici :
<https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/tree/master/Examples_GridJs>
