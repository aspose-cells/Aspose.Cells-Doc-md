---
title: Travailler avec le stockage GridJs
type: docs
weight: 250
url: /fr/net/aspose-cells-gridjs/storage/
description: Cet article décrit le traitement général des fichiers pour GridJs.
keywords: cache de fichier, stockage, GridJs, stockage GridJs, uid GridJs, téléchargement, uniqueid
---


# Travailler avec le stockage GridJs
## le processus général du fichier 
Après avoir importé un fichier de feuille de calcul,

GridJs créera un fichier de cache avec l'uid spécifié dans le **`Config.FileCacheDirectory`** dossier,

avec le format [Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat"),

GridJs sauvegardera également toutes les formes/images dans un fichier d'archive zip dans le dossier **`Config.PictureCacheDirectory`** pour afficher ultérieurement les formes/images dans l'interface client.

et après chaque opération de mise à jour dans l'interface utilisateur du client,

par exemple, définir la valeur de la cellule, définir le style de la cellule, etc. ,

Le code côté client de GridJs déclenchera une action de contrôleur pour effectuer une opération UpdateCell.

Dans cette action, une sauvegarde dans le fichier de cache se produira pendant la méthode UpdateCell.
```C#   
        // post: /GridJs/UpdateCell
        [HttpPost] 
        public ActionResult UpdateCell( )
        {
            string p = HttpContext.Request.Form["p"];
            string uid = HttpContext.Request.Form["uid"];
            GridJsWorkbook gwb = new GridJsWorkbook();
            String ret = gwb.UpdateCell(p, uid);
            return Content(ret, "text/plain", System.Text.Encoding.UTF8);
        }
```
### où se trouve le fichier cache en réalité 

A. Si nous implementons GridCacheForStream et configurons GridJsWorkbook.CacheImp.
par exemple, dans le code ci-dessous, nous pouvons simplement mettre et obtenir le fichier cache depuis **"D:\temp"**
```C#
Config.FileCacheDirectory=@"D:\temp";
GridJsWorkbook.CacheImp=new LocalFileCache();
public class LocalFileCache  : GridCacheForStream
    {

        /// <summary>
        /// Implement this method to savecache,save the stream to the cache object with the key id.
        /// </summary>
        /// <param name="s">the source stream </param>
        /// <param name="uid">the key id.</param>
        public override void SaveStream(Stream s, String uid)
        {//make sure the directory exist
            String filepath = Path.Combine(Config.FileCacheDirectory, uid);
            using (FileStream fs = new FileStream(filepath, FileMode.Create)) 
            {
                s.Position = 0;
                s.CopyTo(fs);
            }

        }

        /// <summary>
        /// Implement this method to loadcache with the key uid,return the stream from the cache object.
        /// </summary>
        /// <param name="uid">the key id</param>
        /// <returns>the stream from  the cache</returns>
        public override Stream LoadStream(String uid)
        {//make sure the directory is exist
            String filepath = Path.Combine(Config.FileCacheDirectory, uid);;
            FileStream fs = new FileStream(filepath, FileMode.Open);
            return fs;
        }
		...
```
B. Si nous ne configurons pas GridJsWorkbook.CacheImp,

GridJs va créer et sauvegarder le fichier dans le **`Config.FileCacheDirectory`** , qui est le répertoire de cache par défaut que nous pouvons configurer.

### comment obtenir le fichier de résultat mis à jour
#### 1. un uid spécifié pour le fichier 
Assurez-vous qu'il existe une correspondance de mappage spécifiée entre le fichier et l'uid. 

vous pouvez toujours obtenir le même uid pour un nom de fichier spécifié, pas généré aléatoirement.

Par exemple, utilisez simplement le nom du fichier.
```C#
//in controller  
...
        public ActionResult Uidtml(String filename)
        {

            return Redirect("~/xspread/uidload.html?file=" + filename + "&uid=" +  Path.GetFileNameWithoutExtension(filename));
        }
 ...
        public ActionResult DetailFileJsonWithUid(string filename,string uid)
        {
            String file = Path.Combine(TestConfig.ListDir, filename);
            GridJsWorkbook wbj = new GridJsWorkbook();
            //check if already in cache
           StringBuilder sb= wbj.GetJsonByUid(uid, filename);
            if(sb==null)
            {
                Workbook wb = new Workbook(file);
                wbj.ImportExcelFile(uid, wb);
                sb = wbj.ExportToJsonStringBuilder(filename);
            }

            return Content(sb.ToString(), "text/plain", System.Text.Encoding.UTF8);
        }
```

#### 2. synchroniser avec l'opération de l'interface utilisateur du client
En fait, pour certaines opérations de l'interface utilisateur du client,

par exemple :

passer à une autre feuille active,

changer la position de l'image,

faire pivoter/redimensionner l'image, etc.

l'action UpdateCell ne sera pas déclenchée.

Ainsi, si nous voulons obtenir le fichier mis à jour exactement comme l'interface utilisateur du client le montre,

nous devons effectuer une opération de fusion avant l'action de sauvegarde pour synchroniser ces opérations de l'interface utilisateur du client.
```javascript
//in the js
  function save() {
            if (!xs.buffer.isFinish()) {
              alert('updating is inprogress,please try later');
                return;
            }
            let datas = xs.datas;
            delete datas.history;
            delete datas.search;
            delete datas.images;
            delete datas.shapes;

        var jsondata = {
          sheetname: xs.sheet.data.name,
          actrow: xs.sheet.data.selector.ri,
          actcol: xs.sheet.data.selector.ci,
          datas: xs.getUpdateDatas(),
        };

        const data = {
          p: JSON.stringify(jsondata),
          uid: uniqueid,
        };
		....
		//go on to do ajax post to trigger controller action
```
```C#
//in controller action 
  GridJsWorkbook wb = new GridJsWorkbook();
  wb.MergeExcelFileFromJson(uid, p);
  //after merge do save to chache or to a stream or whaterver you want to save to ,here we just save to cache
  wb.SaveToXlsx(Path.Combine(Config.FileCacheDirectory, uid));
```         
#### 3. obtenir le fichier depuis le cache
par exemple : dans l'action de téléchargement, vous pouvez simplement le récupérer dans le répertoire de cache par uid.
```C#
//in controller  

        public async Task<IActionResult> DownloadfromBytes(string uid,string ext)
        {
            byte[] byteArr = await System.IO.File.ReadAllBytesAsync(Path.Combine(Config.FileCacheDirectory, uid) );
            string mimeType = "application/octet-stream";
            return new FileContentResult(byteArr, mimeType)
            {
                FileDownloadName = uid+ ext
            };
        }
```

Pour plus d'informations détaillées, vous pouvez consulter l'exemple ici :
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>
