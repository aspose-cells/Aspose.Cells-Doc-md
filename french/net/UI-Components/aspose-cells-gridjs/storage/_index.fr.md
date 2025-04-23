---
title: Travailler avec le stockage GridJs
type: docs
weight: 250
url: /fr/net/aspose-cells-gridjs/storage/
description: Cet article décrit le traitement général des fichiers pour GridJs.
keywords: cache de fichier, stockage, GridJs, stockage GridJs, uid GridJs, téléchargement, uniqueid
aliases:
  - /net/aspose-cells-gridjs/storage-introduction/
  - /net/aspose-cells-gridjs/work-with-storage/
---


# Travailler avec le stockage GridJs
## le processus général du fichier 

Après avoir importé un fichier de feuille de calcul,

GridJs créera un fichier cache avec l'uid spécifié selon l'implémentation GridCacheForStream,

avec le format [Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat"),

GridJs enregistrera également toutes les formes/images dans un fichier archive zip dans le dossier cache pour une affichage ultérieur des formes/images dans l'interface utilisateur client.

et après chaque opération de mise à jour dans l'interface utilisateur du client,

par exemple, définir la valeur de la cellule, définir le style de la cellule, etc. ,

Le js client side de GridJs déclenchera une action du contrôleur pour effectuer une opération de mise à jour.

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

A. Si vous implémentez GridCacheForStream vous-même.
par exemple, dans le code ci-dessous, nous pouvons simplement mettre et obtenir le fichier cache depuis **"D:\temp"**
```C#
Config.FileCacheDirectory=@"D:\temp";
GridJsWorkbook.CacheImp=new LocalFileCache();
public class LocalFileCache  : GridCacheForStream
    {

        public LocalFileCache()
        {
            string streampath = Config.FileCacheDirectory;
            if (!Directory.Exists(streampath))
            {

                Directory.CreateDirectory(streampath);

            }
        }
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
B. Si vous ne définissez pas GridJsWorkbook.CacheImp, 

GridJs a déjà une implémentation par défaut.

GridJs créera et enregistrera le fichier cache dans le chemin : **`Config.FileCacheDirectory/streamcache`** .

### comment obtenir le fichier de résultat mis à jour
#### 1. créer un uid spécifique pour le fichier 
Assurez-vous qu'il existe une correspondance de mappage spécifiée entre le fichier et l'uid. 

Par exemple 

```C#

...     
        //generte a uid for the file
        String uid = GridJsWorkbook.GetUidForFile(filename)
...
        //get JSON result which will be used in client ui for the file by filename and uid
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


#### 2. obtenir le fichier du cache par l'UID
par exemple : dans l'action de téléchargement, vous pouvez simplement l'obtenir du répertoire de cache via l'UID et le nom de fichier.
```C#
	 Stream fileStream = GridJsWorkbook.CacheImp.LoadStream(uid + "/" + filename);
```

Pour plus d'informations détaillées, vous pouvez consulter l'exemple ici :
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>
