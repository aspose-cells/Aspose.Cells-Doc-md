---
title: Editor de hojas de cálculo  Trabajando con archivos
type: docs
weight: 10
url: /es/java/spreadsheet-editor-working-with-files/
---

**Tabla de contenidos**

- [Archivos admitidos](#SpreadsheetEditor-WorkingwithFiles-SupportedFiles)
- [Abrir archivos locales](#SpreadsheetEditor-WorkingwithFiles-OpenLocalFiles) 
  - LoaderService.buildColumnWidthCache
  - LoaderService.buildRowHeightCache
- [Abrir desde Dropbox](#SpreadsheetEditor-WorkingwithFiles-OpenfromDropbox)
- [Abrir desde URL](#SpreadsheetEditor-WorkingwithFiles-OpenfromURL) 
  - LoaderService.fromUrl
  - LoaderService.buildCellsCache
  - LoaderService.buildColumnWidthCache
  - LoaderService.buildRowHeightCache
- [Crear una nueva hoja de cálculo](#SpreadsheetEditor-WorkingwithFiles-CreateaNewSpreadsheet) 
  - LoaderService.fromBlank
  - buildCellsCache
  - buildColumnWidthCache
  - buildRowHeightCache
- [Exportar a varios formatos](#SpreadsheetEditor-WorkingwithFiles-ExporttoVariousFormats)
### **Archivos admitidos**
El editor de hojas de cálculo HTML5 puede abrir archivos en los siguientes formatos:

- Excel 1997-2003 XLS
- Excel 2007-2013 XLSX
- XLSM
- XLSB
- XLTX
- SpreadsheetML
- CVS
- OpenDocument
### **Abrir archivos locales**
Para cargar un archivo desde el equipo local:

1. Cambie a la pestaña **Archivo** en la parte superior.
1. Haga clic en **Abrir desde el equipo** para abrir el cuadro de diálogo de exploración.
1. Vaya a la ubicación deseada del archivo.
1. Haga clic en el archivo deseado para seleccionarlo.
1. Haga clic en **Abrir**.

El archivo se abrirá en el editor.

![todo:image_alt_text](bwyl3xi.png)

**¿Cómo funciona?**

**Cargar archivo**

El usuario selecciona un archivo desde el equipo local que se carga desde el navegador web al servidor y se recibe mediante el componente [PrimeFaces fileUpload](https://www.primefaces.org/showcase/ui/file/upload/basic.xhtml).

{{< highlight java >}}

 <p:fileUpload fileUploadListener="#\{workbook.onFileUpload\}" update=":ribbon :intro :sheet" />

{{< /highlight >}}

**Gestión de libros de trabajo**

Tan pronto como el archivo se carga por completo, el método WorkbookService.onFileUpload entra en acción para manejar la situación. WorkbookService recibe eventos desde el navegador web y lleva un seguimiento del estado de todo el libro de trabajo. El WorkbookService.onFileUpload pasa el control al LoaderService para cargar el libro de trabajo en la memoria. Como el componente ***fileUpload*** proporciona el archivo cargado como un [InputStream](https://docs.oracle.com/javase/8/docs/api/index.html?java/io/InputStream.html), LoaderService lo carga mediante el método LoaderService.fromInputStream.







{{< highlight java >}}

 public void onFileUpload(FileUploadEvent e) {

    this.current = loader.fromInputStream(e.getFile().getInputstream(), e.getFile().getFileName());

}

{{< /highlight >}}







**Carga y descarga**

El método ***LoaderService.fromInputStream*** lee el ***InputStream*** proporcionado por el ***componente*** fileUpload para crear una instancia de la clase ***com.aspose.cells.Workbook***. Esta instancia se mantiene en memoria mientras el usuario sigue viendo o editando la hoja de cálculo en el navegador web. Cuando el usuario abandona el editor o cierra el navegador, las instancias no utilizadas se descargan automáticamente de la memoria para mantener el servidor limpio.







{{< highlight java >}}

 public String fromInputStream(InputStream s, String name) {

    com.aspose.cells.Workbook w;

    try (InputStream i = s) {

        w = new com.aspose.cells.Workbook(i);

    } catch (Exception x) {

        return null;

    }

    String key = this.generateKey();

    this.workbooks.put(key, w);

    this.buildCellsCache(key);

    this.buildColumnWidthCache(key);

    this.buildRowHeightCache(key);

    return key;

}

{{< /highlight >}}







**Caché**

El caché es muy importante para el Editor de Hojas de Cálculo en HTML5. Hace que todo funcione de manera fluida. El CellsService mantiene en caché filas, columnas, celdas y propiedades de todas las hojas de cálculo cargadas por el editor. Cuando LoaderService carga una hoja de cálculo por completo, la lee de arriba abajo y llena la caché llamando a LoaderService.buildCellsCache, LoaderService.buildColumnWidthCache, LoaderService.buildRowHeightCache







{{< highlight java >}}

     public void buildCellsCache(String key) {

        com.aspose.cells.Workbook wb = workbooks.get(key);

        com.aspose.cells.Worksheet ws = wb.getWorksheets().get(wb.getWorksheets().getActiveSheetIndex());

        int maxColumn = ws.getCells().getMaxColumn() + 1;

        maxColumn = maxColumn + 26 - (maxColumn % 26);

        int maxRow = 20 + ws.getCells().getMaxRow() + 1;

        maxRow = maxRow + 10 - (maxRow % 10);

        ArrayList<Column> columns = new ArrayList<>(maxColumn);

        ArrayList<Row> rows = new ArrayList<>(maxRow);

        for (int i = 0; i < maxColumn; i++) {

            columns.add(i, new Column(i, com.aspose.cells.CellsHelper.columnIndexToName(i)));

        }

        for (int i = 0; i < maxRow; i++) {

            rows.add(i, new Row.Builder().setId(i).build());

        }

        for (Object o : ws.getCells()) {

            com.aspose.cells.Cell c = (com.aspose.cells.Cell) o;

            rows.get(c.getRow()).putCell(c.getColumn(), cells.fromAsposeCell(c));

        }

        for (int i = 0; i < maxRow; i++) {

            for (int j = 0; j < maxColumn; j++) {

                String col = com.aspose.cells.CellsHelper.columnIndexToName(j);

                if (!rows.get(i).getCellsMap().containsKey(col)) {

                    rows.get(i).putCell(col, cells.fromBlank(j, i));

                }

            }

        }

        cells.putColumns(key, columns);

        cells.putRows(key, rows);

    }

{{< /highlight >}}




#### **LoaderService.buildColumnWidthCache**
{{< highlight java >}}

     public void buildColumnWidthCache(String key) {

        com.aspose.cells.Workbook wb = workbooks.get(key);

        com.aspose.cells.Worksheet ws = wb.getWorksheets().get(wb.getWorksheets().getActiveSheetIndex());

        ArrayList<Integer> columnWidth = new ArrayList<>();

        for (int i = 0; i < cells.getColumns(key).size(); i++) {

            columnWidth.add(i, ws.getCells().getColumnWidthPixel(i));

        }

        cells.putColumnWidth(key, columnWidth);

    }

{{< /highlight >}}




#### **LoaderService.buildRowHeightCache**
{{< highlight java >}}

     public void buildRowHeightCache(String key) {

        com.aspose.cells.Workbook wb = workbooks.get(key);

        com.aspose.cells.Worksheet ws = wb.getWorksheets().get(wb.getWorksheets().getActiveSheetIndex());

        ArrayList<Integer> rowHeight = new ArrayList<>();

        for (int i = 0; i < cells.getRows(key).size(); i++) {

            rowHeight.add(i, ws.getCells().getRowHeightPixel(i));

        }

        cells.putRowHeight(key, rowHeight);

    }

{{< /highlight >}}






### **Abrir desde Dropbox**
Para abrir archivos desde Dropbox:

1. Cambie a la pestaña **Archivo** en la parte superior.
1. Haga clic en **Abrir desde Dropbox** para abrir el selector de archivos de Dropbox.
1. Si aún no ha iniciado sesión, se le pedirá que inicie sesión en su cuenta de Dropbox.
1. Vaya al archivo deseado y haga clic para seleccionarlo.
1. Haga clic en **Elegir** en la parte inferior.

Su archivo seleccionado se abrirá desde Dropbox.

![todo:image_alt_text](1e2sfo0.png)

**¿Cómo funciona?**

El botón **Abrir desde Dropbox** utiliza la **API de Selector de Dropbox JavaScript** para abrir el diálogo de Selector de Dropbox. El Selector proporciona la URL del archivo seleccionado, que es capturada por la función de devolución de llamada y enviada de vuelta al servidor. El servidor crea una instancia de la hoja de cálculo desde la URL, inicializa algunas cosas de mantenimiento, y envía actualizaciones del DOM de vuelta al navegador. El navegador renderiza y actualiza el HTML, y el usuario está listo para editar el documento cargado.
### **Abrir desde URL**
Los archivos se pueden abrir directamente desde las URL. Esto permite al usuario editar cualquier archivo disponible públicamente en Internet. Para abrir el archivo, agregue el parámetro **?url=ubicación** con el valor de su **ubicación** deseada mientras carga el editor. Por ejemplo:

{{< highlight java >}}

 http://editor.aspose.com/?url=http://example.com/Sample.xlsx

{{< /highlight >}}

![todo:image_alt_text](exc9ckp.png)

**¿Cómo funciona?**

**Inicializar durante el inicio**

Cuando se instancie el bean **WorksheetView** en el backend por JSF, se llamará al método **PostConstruct** **init** que carga la hoja de cálculo utilizando LoaderService.fromUrl.

**Caché**

La caché ocurre justo después de que se carga la hoja de cálculo. El **LoaderService** llama a **LoaderService.buildCellsCache**, **LoaderService.buildColumnWidthCache** y **LoaderService.buildRowHeightCache** uno por uno para almacenar en caché el contenido de la hoja de cálculo y mantener todas las operaciones rápidas y suaves.

**Actualizaciones en el DOM**

Cuando la hoja de cálculo está lista en el lado del servidor, se utilizan componentes JSF para generar HTML nuevo y enviar actualizaciones al DOM al usuario, las cuales son renderizadas por el navegador web.







{{< highlight java >}}

     @PostConstruct

    private void init() {

        String requestedSourceUrl = FacesContext.getCurrentInstance().getExternalContext().getRequestParameterMap().get("url");

        if (requestedSourceUrl != null) {

            try {

                this.sourceUrl = new URL(requestedSourceUrl).toString();

                this.loadFromUrl();

            } catch (MalformedURLException x) {

                msg.sendMessageDialog("The specified URL is invalid", requestedSourceUrl);

            }

        }

    }

{{< /highlight >}}




#### **LoaderService.fromUrl**
{{< highlight java >}}

     public String fromUrl(String url) {

        com.aspose.cells.Workbook w;

        try (InputStream i = new URL(url).openStream()) {

            w = new com.aspose.cells.Workbook(i);

        } catch (Exception x) {

            throw new RuntimeException(x);

        }

        String key = generateKey();

        workbooks.put(key, w);

        buildCellsCache(key);

        buildColumnWidthCache(key);

        buildRowHeightCache(key);

        return key;

    }

{{< /highlight >}}




#### **LoaderService.buildCellsCache**
{{< highlight java >}}

     public void buildCellsCache(String key) {

        com.aspose.cells.Workbook wb = workbooks.get(key);

        com.aspose.cells.Worksheet ws = wb.getWorksheets().get(wb.getWorksheets().getActiveSheetIndex());

        int maxColumn = ws.getCells().getMaxColumn() + 1;

        maxColumn = maxColumn + 26 - (maxColumn % 26);

        int maxRow = 20 + ws.getCells().getMaxRow() + 1;

        maxRow = maxRow + 10 - (maxRow % 10);

        ArrayList<Column> columns = new ArrayList<>(maxColumn);

        ArrayList<Row> rows = new ArrayList<>(maxRow);

        for (int i = 0; i < maxColumn; i++) {

            columns.add(i, new Column(i, com.aspose.cells.CellsHelper.columnIndexToName(i)));

        }

        for (int i = 0; i < maxRow; i++) {

            rows.add(i, new Row.Builder().setId(i).build());

        }

        for (Object o : ws.getCells()) {

            com.aspose.cells.Cell c = (com.aspose.cells.Cell) o;

            rows.get(c.getRow()).putCell(c.getColumn(), cells.fromAsposeCell(c));

        }

        for (int i = 0; i < maxRow; i++) {

            for (int j = 0; j < maxColumn; j++) {

                String col = com.aspose.cells.CellsHelper.columnIndexToName(j);

                if (!rows.get(i).getCellsMap().containsKey(col)) {

                    rows.get(i).putCell(col, cells.fromBlank(j, i));

                }

            }

        }

        cells.putColumns(key, columns);

        cells.putRows(key, rows);

    }

{{< /highlight >}}




#### **LoaderService.buildColumnWidthCache**
{{< highlight java >}}

     public void buildColumnWidthCache(String key) {

        com.aspose.cells.Workbook wb = workbooks.get(key);

        com.aspose.cells.Worksheet ws = wb.getWorksheets().get(wb.getWorksheets().getActiveSheetIndex());

        ArrayList<Integer> columnWidth = new ArrayList<>();

        for (int i = 0; i < cells.getColumns(key).size(); i++) {

            columnWidth.add(i, ws.getCells().getColumnWidthPixel(i));

        }

        cells.putColumnWidth(key, columnWidth);

    }

{{< /highlight >}}




#### **LoaderService.buildRowHeightCache**
{{< highlight java >}}

     public void buildRowHeightCache(String key) {

        com.aspose.cells.Workbook wb = workbooks.get(key);

        com.aspose.cells.Worksheet ws = wb.getWorksheets().get(wb.getWorksheets().getActiveSheetIndex());

        ArrayList<Integer> rowHeight = new ArrayList<>();

        for (int i = 0; i < cells.getRows(key).size(); i++) {

            rowHeight.add(i, ws.getCells().getRowHeightPixel(i));

        }

        cells.putRowHeight(key, rowHeight);

    }

{{< /highlight >}}






### **Crear una nueva hoja de cálculo**
Para crear una nueva hoja de cálculo vacía:

1. Cambiar a la pestaña **Archivo**.
1. Hacer clic en el botón **Nuevo**.

El editor cerrará la hoja de cálculo abierta, si la hubiera, y abrirá una nueva.

![todo:image_alt_text](lnydmmf.png)

**¿Cómo funciona?**

**Instanciar un nuevo objeto**

Cuando el usuario hace clic en el botón **Nuevo**, **WorksheetView.loadBlank**, que eventualmente llama a **LoaderService.fromBlank**. LoaderService crea una nueva instancia de hoja de cálculo en blanco.

**Caché**

La caché ocurre justo después de que se carga la hoja de cálculo. El **LoaderService** llama a **LoaderService.buildCellsCache**, **LoaderService.buildColumnWidthCache** y **LoaderService.buildRowHeightCache** uno por uno para almacenar en caché el contenido de la hoja de cálculo y mantener todas las operaciones rápidas y suaves.

**Actualizaciones en el DOM**

Cuando la hoja de cálculo está lista en el lado del servidor, se utilizan componentes JSF para generar HTML nuevo y enviar actualizaciones al DOM al usuario, las cuales son renderizadas por el navegador web.







{{< highlight java >}}

     public void loadBlank() {

        this.loadedWorkbook = loader.fromBlank();

    }

{{< /highlight >}}




#### **LoaderService.fromBlank**
{{< highlight java >}}

     public String fromBlank() {

        com.aspose.cells.Workbook w = new com.aspose.cells.Workbook();

        String key = generateKey();

        workbooks.put(key, w);

        buildCellsCache(key);

        buildColumnWidthCache(key);

        buildRowHeightCache(key);

        return key;

    }

{{< /highlight >}}




#### **buildCellsCache**
{{< highlight java >}}

     public void buildCellsCache(String key) {

        com.aspose.cells.Workbook wb = workbooks.get(key);

        com.aspose.cells.Worksheet ws = wb.getWorksheets().get(wb.getWorksheets().getActiveSheetIndex());

        int maxColumn = ws.getCells().getMaxColumn() + 1;

        maxColumn = maxColumn + 26 - (maxColumn % 26);

        int maxRow = 20 + ws.getCells().getMaxRow() + 1;

        maxRow = maxRow + 10 - (maxRow % 10);

        ArrayList<Column> columns = new ArrayList<>(maxColumn);

        ArrayList<Row> rows = new ArrayList<>(maxRow);

        for (int i = 0; i < maxColumn; i++) {

            columns.add(i, new Column(i, com.aspose.cells.CellsHelper.columnIndexToName(i)));

        }

        for (int i = 0; i < maxRow; i++) {

            rows.add(i, new Row.Builder().setId(i).build());

        }

        for (Object o : ws.getCells()) {

            com.aspose.cells.Cell c = (com.aspose.cells.Cell) o;

            rows.get(c.getRow()).putCell(c.getColumn(), cells.fromAsposeCell(c));

        }

        for (int i = 0; i < maxRow; i++) {

            for (int j = 0; j < maxColumn; j++) {

                String col = com.aspose.cells.CellsHelper.columnIndexToName(j);

                if (!rows.get(i).getCellsMap().containsKey(col)) {

                    rows.get(i).putCell(col, cells.fromBlank(j, i));

                }

            }

        }

        cells.putColumns(key, columns);

        cells.putRows(key, rows);

    }

{{< /highlight >}}




#### **buildColumnWidthCache**
{{< highlight java >}}

     public void buildColumnWidthCache(String key) {

        com.aspose.cells.Workbook wb = workbooks.get(key);

        com.aspose.cells.Worksheet ws = wb.getWorksheets().get(wb.getWorksheets().getActiveSheetIndex());

        ArrayList<Integer> columnWidth = new ArrayList<>();

        for (int i = 0; i < cells.getColumns(key).size(); i++) {

            columnWidth.add(i, ws.getCells().getColumnWidthPixel(i));

        }

        cells.putColumnWidth(key, columnWidth);

    }

{{< /highlight >}}




#### **buildRowHeightCache**
{{< highlight java >}}

     public void buildRowHeightCache(String key) {

        com.aspose.cells.Workbook wb = workbooks.get(key);

        com.aspose.cells.Worksheet ws = wb.getWorksheets().get(wb.getWorksheets().getActiveSheetIndex());

        ArrayList<Integer> rowHeight = new ArrayList<>();

        for (int i = 0; i < cells.getRows(key).size(); i++) {

            rowHeight.add(i, ws.getCells().getRowHeightPixel(i));

        }

        cells.putRowHeight(key, rowHeight);

    }

{{< /highlight >}}






### **Exportar a varios formatos**
Después de editar archivos, el usuario querrá guardar los cambios. El editor permite al usuario exportar y descargar la hoja de cálculo modificada en su computadora local. Para exportar el archivo:

1. Cambie a la pestaña **Archivo** en la parte superior.
1. Haga clic en el botón **Exportar**.
1. Elija el formato deseado en el menú desplegable.

El archivo modificado se exportará para su descarga. Los siguientes formatos son compatibles para la exportación:

- Excel 2007-2013 XLSX
- Excel 1997-2003 XLS
- Excel XLSM
- Excel XLSB
- Excel XLTX
- Excel XLTM
- SpreadsheetML
- Formato de Documentos Portátiles (PDF)
- Hoja de Cálculo de OpenDocument (ODS)

**¿Cómo funciona?**

La hoja de cálculo abierta se convierte al formato especificado por el usuario utilizando **WorksheetView.getOutputFile**.







{{< highlight java >}}

     public StreamedContent getOutputFile(int saveFormat) {

        byte[] buf;

        String ext = null;

        switch (saveFormat) {

            case com.aspose.cells.SaveFormat.EXCEL_97_TO_2003:

                ext = "xls";

                break;

            case com.aspose.cells.SaveFormat.XLSX:

                ext = "xlsx";

                break;

            case com.aspose.cells.SaveFormat.XLSM:

                ext = "xlsm";

                break;

            case com.aspose.cells.SaveFormat.XLSB:

                ext = "xlsb";

                break;

            case com.aspose.cells.SaveFormat.XLTX:

                ext = "xltx";

                break;

            case com.aspose.cells.SaveFormat.XLTM:

                ext = "xltm";

                break;

            case com.aspose.cells.SaveFormat.SPREADSHEET_ML:

                ext = "xml";

                break;

            case com.aspose.cells.SaveFormat.PDF:

                ext = "pdf";

                break;

            case com.aspose.cells.SaveFormat.ODS:

                ext = "ods";

                break;

        }

        try {

            ByteArrayOutputStream out = new ByteArrayOutputStream();

            getAsposeWorkbook().save(out, saveFormat);

            buf = out.toByteArray();

        } catch (Exception x) {

            throw new RuntimeException(x);

        }

        return new DefaultStreamedContent(new ByteArrayInputStream(buf), "application/octet-stream", "Spreadsheet." + ext);

    }

{{< /highlight >}}






