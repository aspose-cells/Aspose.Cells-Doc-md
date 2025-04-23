---
title: Trabajando con el almacenamiento de GridJs
type: docs
weight: 250
url: /es/net/aspose-cells-gridjs/storage/
description: Este artículo describe el procesamiento general de archivos para GridJs.
keywords: caché de archivos,almacenamiento,GridJs,almacenamiento de GridJs,UID de GridJs,descargar,identifier único
aliases:
  - /net/aspose-cells-gridjs/storage-introduction/
  - /net/aspose-cells-gridjs/work-with-storage/
---


# Trabajando con el almacenamiento de GridJs
## el proceso general de archivos 

Después de importar un archivo de hoja de cálculo,

GridJs creará un archivo en caché con el uid especificado según la implementación GridCacheForStream,

con el formato de [Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat") ,

GridJs también guarda todas las formas/imágenes en un archivo zip en la carpeta de caché para mostrar formas/imágenes en la interfaz de usuario del cliente posteriormente.

y después de cada operación de actualización en la interfaz de usuario del cliente,

por ejemplo, establecer el valor de celda, establecer el estilo de celda, etc.,

El js del lado cliente de GridJs activará una acción del controlador para realizar una operación de actualización.

En esta acción, ocurrirá un guardado de nuevo al archivo de caché durante el método UpdateCell.
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
###  ¿dónde se encuentra realmente el archivo de caché 

A. Si implementas GridCacheForStream tú mismo.
por ejemplo, en el siguiente código, podemos simplemente poner y obtener el archivo de caché desde **"D:\temp"**
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
B. Si no configuras GridJsWorkbook.CacheImp, 

GridJs ya implementa uno por defecto.

GridJs creará y guardará el archivo en caché en la ruta: **`Config.FileCacheDirectory/streamcache`** .

### cómo obtener el archivo de resultado actualizado
#### 1. crear un uid especificado para el archivo 
Asegúrese de tener una correspondencia de mapeo especificada entre el archivo y el uid, 

Por ejemplo 

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


#### 2. obtener el archivo de la caché mediante el uid
por ejemplo: en la acción de descarga, simplemente puedes obtenerlo del directorio de caché usando el uid y el nombre de archivo.
```C#
	 Stream fileStream = GridJsWorkbook.CacheImp.LoadStream(uid + "/" + filename);
```

Para obtener más información detallada, puedes consultar el ejemplo aquí:
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>
