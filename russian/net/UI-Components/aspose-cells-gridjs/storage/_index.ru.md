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

GridJs создаст файл кэша с указанным uid в папке **`Config.FileCacheDirectory`** ,

в формате [Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat") ,

GridJs также сохранит все формы/изображения в zip-архиве в папке **`Config.PictureCacheDirectory`** для последующего отображения их на клиентском интерфейсе.

и после каждой операции обновления в клиентском интерфейсе (UI),

например, установка значения ячейки, установка стиля ячейки и т. д.,

клиентский js GridJs вызовет действие контроллера для выполнения операции UpdateCell.

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

A. Если мы реализуем GridCacheForStream и установим GridJsWorkbook.CacheImp.
например, в приведенном ниже коде мы можем просто поместить и получить файл кэша из **"D:\temp"**
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
B. Если мы не установим GridJsWorkbook.CacheImp,

GridJs создаст и сохранит файл в папке **`Config.FileCacheDirectory`** , которая является кэш-каталогом по умолчанию, который мы можем установить.

###  как получить обновленный результат файла
#### 1. указанный идентификатор (UID) для файла 
Убедитесь, что существует соответствие между файлом и идентификатором (UID), 

вы всегда можете получить один и тот же идентификатор (UID) для заданного имени файла, а не случайно сгенерированный.

Например, достаточно использовать имя файла.
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

#### 2. синхронизация с клиентским интерфейсом (UI)
Фактически, для некоторых операций интерфейса (UI) клиента,

например:

смена активного листа на другой,

изменение позиции изображения,

вращать/изменить размер изображения и т. д.

действие UpdateCell не будет вызвано.

Таким образом, если мы хотим получить обновленный файл такой же, как показывает клиентский интерфейс,

нам нужно выполнить операцию слияния перед сохранением, чтобы синхронизировать операции клиентского интерфейса.
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
#### 3. получить файл из кэша
например: в операции загрузки, вы можете просто получить его из каталога кэша по UID.
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

Для получения более подробной информации вы можете проверить пример здесь:
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>
