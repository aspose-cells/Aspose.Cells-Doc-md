---
title: Trabajando con el almacenamiento de GridJs
type: docs
weight: 250
url: /es/java/aspose-cells-gridjs/storage/
description: Este artículo describe el procesamiento general de archivos para GridJs.
keywords: caché de archivos,almacenamiento,GridJs,almacenamiento de GridJs,UID de GridJs,descargar,identifier único
aliases:
  - /java/aspose-cells-gridjs/storage-introduction/
  - /java/aspose-cells-gridjs/work-with-storage/
---


# Trabajando con el almacenamiento de GridJs
## el proceso general de archivos 
Después de importar un archivo de hoja de cálculo,

GridJs creará un archivo de caché con el uid especificado en la carpeta **`Config.getFileCacheDirectory()`** ,

con el formato de [Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/java/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat"),

GridJs también guarda todas las formas/imágenes en un archivo zip en la carpeta **`Config.getPictureCacheDirectory()`** para su visualización posterior en la interfaz de usuario del cliente.

y después de cada operación de actualización en la interfaz de usuario del cliente,

por ejemplo, establecer el valor de celda, establecer el estilo de celda, etc.,

El cliente-side js de GridJs disparará la acción del controlador para realizar la operación de Actualizar celda.

En esta acción, ocurrirá un guardado de nuevo al archivo de caché durante el método UpdateCell.
```JAVA  
    @PostMapping("/UpdateCell")
    public ResponseEntity<String> updateCell(HttpServletRequest request) {
        String p = request.getParameter("p");
        String uid = request.getParameter("uid");
        GridJsWorkbook gwb = new GridJsWorkbook();
        String ret;
		try {
			ret = gwb.updateCell(p, uid);
			return new ResponseEntity<>(ret, HttpStatus.OK);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			return new ResponseEntity<>(gwb.errorJson(e.getMessage()), HttpStatus.OK);
		}

    }
```
###  ¿dónde se encuentra realmente el archivo de caché 

A. Si implementamos GridCacheForStream y establecemos GridJsWorkbook.CacheImp.
por ejemplo, en el siguiente código, podemos simplemente poner y obtener el archivo de caché desde **"D:\temp"**
```JAVA
Config.setFileCacheDirectory("D:\temp");
GridJsWorkbook.CacheImp=new LocalFileCache();
public class LocalFileCache extends GridCacheForStream {

	@Override
	public void saveStream(InputStream s, String uid) {
		// make sure the directory is exist
		String filepath = Paths.get(Config.getFileCacheDirectory(), "streamcache", uid.replace('/', '.')).toString();
		try (FileOutputStream fos = new FileOutputStream(filepath.toString())) {
			s.reset(); // Equivalent to s.Position = 0 in C#
			byte[] buffer = new byte[1024];
			int length;
			while ((length = s.read(buffer)) > 0) {
				fos.write(buffer, 0, length);
			}
			fos.flush();
		} catch (IOException e) {
			e.printStackTrace();
		}

	}

	@Override
	public InputStream loadStream(String uid) {
		String filepath = Paths.get(Config.getFileCacheDirectory(), "streamcache", uid.replace('/', '.')).toString();
		try {
			return new FileInputStream(filepath);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
			return null;
		}
	}

	@Override
	public boolean isExisted(String uid) {
		String filepath = Paths.get(Config.getFileCacheDirectory(), "streamcache", uid.replace('/', '.')).toString();
		return Files.exists(Paths.get(filepath));
	}

	@Override
	public String getFileUrl(String uid) {
		return "/GridJs2/GetFileUseCacheStream?id=" + uid;
	}

}
		...
```
B. Si no establecemos GridJsWorkbook.CacheImp,

GridJs creará y guardará el archivo dentro de la carpeta **`Config.getFileCacheDirectory()`**, que es el directorio de caché predeterminado que podemos establecer.

### cómo obtener el archivo de resultado actualizado
#### 1. un uid especificado para el archivo 
Asegúrese de tener una correspondencia de mapeo especificada entre el archivo y el uid, 

siempre puede obtener el mismo uid para un nombre de archivo específico, no generado aleatoriamente.

Por ejemplo, simplemente usar el nombre del archivo está bien.
```JAVA
//in controller  

     @GetMapping("/DetailStreamJsonWithUid")
    public void detailStreamJsonWithUid(@RequestParam String filename, @RequestParam String uid,HttpServletResponse response) {


        	Path filePath = Paths.get(listDir, filename);
            GridJsWorkbook wbj = new GridJsWorkbook();

            response.setContentType("application/json");
            response.setHeader("Content-Encoding", "gzip");
            try (GZIPOutputStream gzipOutputStream = new GZIPOutputStream(response.getOutputStream())) {
                wbj.importExcelFile(filePath.toString());
                wbj.jsonToStream(gzipOutputStream, filename);
            } catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
    }
```

#### 2. sincronizar con la operación de la interfaz de usuario del cliente
En realidad, para algunas operaciones de la interfaz de usuario del cliente,

por ejemplo:

cambiar la hoja activa a otra,

cambiar la posición de la imagen,

rotar/redimensionar la imagen, etc.

la acción UpdateCell no se activará.

Por lo tanto, si queremos obtener el archivo actualizado tal como lo muestra la interfaz de usuario del cliente,

necesitamos realizar una operación de fusión antes de la acción de guardado para sincronizar esas operaciones de la interfaz de usuario del cliente.
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
```JAVA
//in controller action 
  GridJsWorkbook wb = new GridJsWorkbook();
  wb.mergeExcelFileFromJson(uid, p);
  //after merge do save to chache or to a stream or whaterver you want to save to ,here we just save to cache
  wb.saveToCacheWithFileName(uid,filename,password);
```         
#### 3. obtener la url del archivo desde la caché
por ejemplo: en la acción de descarga, simplemente puedes obtenerlo desde el directorio de caché por uid.
```JAVA
//in controller  

      String fileUrl = null;
			if (GridJsWorkbook.CacheImp != null) {
				fileUrl = GridJsWorkbook.CacheImp.getFileUrl(uid + "/" + filename);
			} else {
				fileUrl = "/GridJs2/GetFile?id=" + uid + "&filename=" + filename;
			}
			return ResponseEntity.ok("\""+fileUrl+"\"");
```

Para obtener más información detallada, puedes consultar el ejemplo aquí:
<https://github.com/aspose-cells/Aspose.Cells-for-java/tree/master/Examples_GridJs>
