---
title: Editor de hojas de cálculo - Trabajar con archivos
type: docs
weight: 10
url: /es/java/spreadsheet-editor-working-with-files/
---
**Tabla de contenido**

- [Archivos compatibles](#SpreadsheetEditor-WorkingwithFiles-SupportedFiles)
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
### **Archivos compatibles**
HTML5 Spreadsheet Editor puede abrir archivos en los siguientes formatos:

- Excel 1997-2003 XLS
- Excel 2007-2013 XLSX
- XLSM
- XLSB
- XLTX
- Hoja de cálculoML
- CVS
- Abrir documento
### **Abrir archivos locales**
Para cargar un archivo desde la computadora local:

1.  Cambiar a**pestaña Archivo** en la parte superior.
1.  Hacer clic**Abrir desde la computadora** para abrir el cuadro de diálogo Examinar.
1. Vaya a la ubicación deseada del archivo.
1. Haga clic en el archivo deseado para seleccionarlo.
1.  Hacer clic**Abierto**.

El archivo se abrirá en el editor.

![todo:imagen_alternativa_texto](bwyl3xi.png)

**¿Cómo funciona?**

**Subir archivo**

 El usuario selecciona un archivo de la computadora local que se carga desde el navegador web al servidor y es recibido por[Archivo PrimeFacesSubir](https://www.primefaces.org/showcase/ui/file/upload/basic.xhtml) componente.

{{< highlight "java" >}}

 <p:fileUpload fileUploadListener="#\{workbook.onFileUpload\}" update=":ribbon :intro :sheet" />

{{< /highlight >}}

**Gestión del libro de trabajo**

 Tan pronto como el archivo se carga por completo, el método WorkbookService.onFileUpload entra en acción para manejar la situación. WorkbookService recibe eventos del navegador web y realiza un seguimiento del estado de todo el libro de trabajo. WorkbookService.onFileUpload pasa el control a LoaderService para cargar el libro en la memoria. como el***Subir archivo*** componente proporciona el archivo cargado como un[Flujo de entrada](https://docs.oracle.com/javase/8/docs/api/index.html?java/io/InputStream.html), LoaderService lo carga mediante el método LoaderService.fromInputStream.







{{< highlight "java" >}}

 public void onFileUpload(FileUploadEvent e) {

    this.current = loader.fromInputStream(e.getFile().getInputstream(), e.getFile().getFileName());

}

{{< /highlight >}}







**Carga y descarga**

 El método***LoaderService.fromInputStream*** lee el***Flujo de entrada*** proporcionado por fileUpload***componente*** crear instancia de***com.aspose.cells.Workbook*** clase. Esta instancia se mantiene en la memoria siempre que el usuario siga viendo o editando la hoja de cálculo en el navegador web. Cuando el usuario sale del editor o cierra el navegador, las instancias no utilizadas se descargan automáticamente de la memoria para mantener limpio el servidor.







{{< highlight "java" >}}

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







**almacenamiento en caché**

El almacenamiento en caché es muy importante para HTML5 Spreadsheet Editor. Hace que todo funcione sin problemas. CellsService mantiene en caché las filas, columnas, celdas y propiedades de todos los libros de trabajo cargados por el editor. Cuando LoaderService carga una hoja de cálculo por completo, la lee de arriba a abajo y llena el caché llamando a LoaderService.buildCellsCache, LoaderService.buildColumnWidthCache, LoaderService.buildRowHeightCache







{{< highlight "java" >}}

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
{{< highlight "java" >}}

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
{{< highlight "java" >}}

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

1.  Cambiar a**pestaña Archivo** en la parte superior.
1.  Hacer clic**Abrir desde Dropbox** para abrir el selector de archivos de Dropbox.
1. Si aún no ha iniciado sesión, se le pedirá que inicie sesión en su cuenta de Dropbox.
1. Navegue hasta el archivo deseado y haga clic para seleccionarlo.
1.  Hacer clic**Elegir** en el fondo.

Su archivo seleccionado se abrirá desde Dropbox.

![todo:imagen_alternativa_texto](1e2sfo0.png)

**¿Cómo funciona?**

 los**Abrir desde Dropbox** usos del botón**Selector de JavaScript de Dropbox API**para abrir el cuadro de diálogo Selector de Dropbox. El Selector proporciona la URL del archivo seleccionado, que es capturado por la función de devolución de llamada y enviado de vuelta al servidor. El servidor crea una instancia de hoja de cálculo a partir de la URL, inicializa algunas cosas de limpieza y envía actualizaciones de DOM al navegador. El navegador procesa y actualiza el HTML y el usuario está listo para editar el documento cargado.
### **Abrir desde URL**
 Los archivos se pueden abrir directamente desde las URL. Esto permite al usuario editar cualquier archivo disponible públicamente en Internet. Para abrir el archivo anexar**?url=ubicación** parámetro con el valor de su deseado**ubicación** mientras se carga el editor. Por ejemplo:

{{< highlight "java" >}}

 http://editor.aspose.com/?url=http://example.com/Sample.xlsx

{{< /highlight >}}

![todo:imagen_alternativa_texto](exc9ckp.png)

**¿Cómo funciona?**

**Instanciar durante el inicio**

 Cuando**Vista de hoja de trabajo** El backend bean es instanciado por JSF el**PostConstrucción** método**en eso** se llama, que carga la hoja de cálculo mediante LoaderService.fromUrl.

**almacenamiento en caché**

 El almacenamiento en caché se produce justo después de cargar la hoja de cálculo. los**Servicio de cargador** llamadas**LoaderService.buildCellsCache**, **LoaderService.buildColumnWidthCache** y**LoaderService.buildRowHeightCache**uno por uno para almacenar en caché el contenido de la hoja de cálculo y mantener todas las operaciones rápidas y fluidas.

**actualizaciones de DOM**

Cuando la hoja de cálculo está lista en el lado del servidor, los componentes JSF se utilizan para generar un nuevo HTML y enviar actualizaciones DOM al usuario que son procesadas por el navegador web.







{{< highlight "java" >}}

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
{{< highlight "java" >}}

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
{{< highlight "java" >}}

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
{{< highlight "java" >}}

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
{{< highlight "java" >}}

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

1.  Cambiar a**pestaña Archivo**.
1.  Haga clic en el**Nuevo** botón.

El editor cerrará la hoja de cálculo abierta, si la hay, y abrirá una nueva.

![todo:imagen_alternativa_texto](lnydmmf.png)

**¿Cómo funciona?**

**Crear una instancia de un nuevo objeto**

 Cuando el**Nuevo** el botón es presionado por el usuario,**WorksheetView.loadBlank** , que eventualmente llama**LoaderService.fromBlank**. LoaderService crea una nueva instancia de hoja de cálculo en blanco.

**almacenamiento en caché**

 El almacenamiento en caché se produce justo después de cargar la hoja de cálculo. los**Servicio de cargador** llamadas**LoaderService.buildCellsCache**, **LoaderService.buildColumnWidthCache** y**LoaderService.buildRowHeightCache**uno por uno para almacenar en caché el contenido de la hoja de cálculo y mantener todas las operaciones rápidas y fluidas.

**actualizaciones de DOM**

Cuando la hoja de cálculo está lista en el lado del servidor, los componentes JSF se utilizan para generar un nuevo HTML y enviar actualizaciones DOM al usuario que son procesadas por el navegador web.







{{< highlight "java" >}}

     public void loadBlank() {

        this.loadedWorkbook = loader.fromBlank();

    }

{{< /highlight >}}




#### **LoaderService.fromBlank**
{{< highlight "java" >}}

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
{{< highlight "java" >}}

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
{{< highlight "java" >}}

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
{{< highlight "java" >}}

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
Después de editar archivos, el usuario querrá guardar los cambios. El editor permite al usuario exportar y descargar la hoja de cálculo modificada a la computadora local. Para exportar el archivo:

1.  Cambiar a**pestaña Archivo** en la parte superior.
1.  Hacer clic**Exportar** como botón.
1. Elija el formato que desee en el menú desplegable.

El archivo modificado se exportará para su descarga. Los siguientes formatos son compatibles para la exportación:

- Excel 2007-2013 XLSX
- Excel 1997-2003 XLS
- Excel XLSM
- Excel XLSB
- Excel XLTX
- Excel XL™
- Hoja de cálculoML
- Formato de documento portátil (PDF)
- Hoja de cálculo OpenDocument (ODS)

**¿Cómo funciona?**

 La hoja de cálculo abierta se convierte al formato especificado por el usuario usando**WorksheetView.getOutputFile**.







{{< highlight "java" >}}

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






