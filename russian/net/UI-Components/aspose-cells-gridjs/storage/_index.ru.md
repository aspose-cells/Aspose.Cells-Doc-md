---
title: Работа с хранилищем GridJs
type: docs
weight: 250
url: /ru/net/aspose-cells-gridjs/storage/
description: Эта статья описывает обработку общего файла для GridJs.
keywords: кэш файлов, хранение, GridJs, хранение GridJs, идентификатор, загрузка, уникальный идентификатор
aliases:
  - /net/aspose-cells-gridjs/storage-introduction/
  - /net/aspose-cells-gridjs/work-with-storage/
---


# Работа с хранилищем GridJs
##  процесс работы с общим файлом 

После импорта файла таблицы ,

GridJs создаст файл кеша с указанным uid в соответствии с реализацией GridCacheForStream,

в формате [Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat") ,

GridJs также сохраняет все фигуры/изображения в zip-архив в папке кеша для последующего отображения фигур/изображений в клиентском UI.

и после каждой операции обновления в клиентском интерфейсе (UI),

например, установка значения ячейки, установка стиля ячейки и т. д.,

Клиентский JS GridJs инициирует вызов действия контроллера для обновления данных.

В этом действии происходит сохранение обратно в файл кэша во время выполнения метода UpdateCell.
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
###  где на самом деле находится файл кэша 

А. Если вы реализуете GridCacheForStream самостоятельно.
например, в приведенном ниже коде мы можем просто поместить и получить файл кэша из **"D:\temp"**
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
Б. Если вы не устанавливаете GridJsWorkbook.CacheImp, 

GridJs уже реализовал дефолтную реализацию.

GridJs создаст и сохранит файл кеша в папке: **`Config.FileCacheDirectory/streamcache`**.

###  как получить обновленный результат файла
#### 1. создать указанный uid для файла 
Убедитесь, что существует соответствие между файлом и идентификатором (UID), 

Например 

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


#### 2. получить файл из кэша по uid
например: в действиях загрузки, вы можете взять его из каталога кэша по uid и имени файла.
```C#
	 Stream fileStream = GridJsWorkbook.CacheImp.LoadStream(uid + "/" + filename);
```

Для получения более подробной информации вы можете проверить пример здесь:
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>
