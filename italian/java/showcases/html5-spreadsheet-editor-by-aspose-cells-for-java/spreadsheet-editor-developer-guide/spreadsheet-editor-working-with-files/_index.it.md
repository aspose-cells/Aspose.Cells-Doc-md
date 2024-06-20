---
title: Editor di fogli di calcolo  Lavorare con i file
type: docs
weight: 10
url: /it/java/spreadsheet-editor-working-with-files/
---

**Tabella dei contenuti**

- [File supportati](#SpreadsheetEditor-WorkingwithFiles-SupportedFiles)
- [Apri file locali](#SpreadsheetEditor-WorkingwithFiles-OpenLocalFiles) 
  - LoaderService.buildColumnWidthCache
  - LoaderService.buildRowHeightCache
- [Apri da Dropbox](#SpreadsheetEditor-WorkingwithFiles-OpenfromDropbox)
- [Apri da URL](#SpreadsheetEditor-WorkingwithFiles-OpenfromURL) 
  - LoaderService.fromUrl
  - LoaderService.buildCellsCache
  - LoaderService.buildColumnWidthCache
  - LoaderService.buildRowHeightCache
- [Crea un nuovo foglio di calcolo](#SpreadsheetEditor-WorkingwithFiles-CreateaNewSpreadsheet) 
  - LoaderService.fromBlank
  - buildCellsCache
  - buildColumnWidthCache
  - buildRowHeightCache
- [Esporta in vari formati](#SpreadsheetEditor-WorkingwithFiles-ExporttoVariousFormats)
### **File supportati**
L'editor di fogli di calcolo HTML5 può aprire file nei seguenti formati:

- Excel 1997-2003 XLS
- Excel 2007-2013 XLSX
- XLSM
- XLSB
- XLTX
- SpreadsheetML
- CVS
- OpenDocument
### **Apri file locali**
Per caricare un file dal computer locale:

1. Passa alla scheda **File** in alto.
1. Fai clic su **Apri da Computer** per aprire la finestra di dialogo Sfoglia.
1. Vai alla posizione desiderata del file.
1. Fare clic sul file desiderato per selezionarlo.
1. Fare clic su **Apri**.

Il file verrà aperto nell'editor.

![todo:image_alt_text](bwyl3xi.png)

**Come funziona?**

**Caricamento file**

L'utente seleziona un file dal computer locale che viene caricato dal browser web al server e ricevuto dal componente [PrimeFaces fileUpload](https://www.primefaces.org/showcase/ui/file/upload/basic.xhtml).

{{< highlight java >}}

 <p:fileUpload fileUploadListener="#\{workbook.onFileUpload\}" update=":ribbon :intro :sheet" />

{{< /highlight >}}

**Gestione del foglio di lavoro**

Non appena il file viene caricato completamente, il metodo WorkbookService.onFileUpload entra in azione per gestire la situazione. WorkbookService riceve eventi dal browser web e tiene traccia dello stato di tutto il foglio di lavoro. WorkbookService.onFileUpload passa il controllo a LoaderService per caricare il foglio di lavoro in memoria. Poiché il componente ***fileUpload*** fornisce il file caricato come un [InputStream](https://docs.oracle.com/javase/8/docs/api/index.html?java/io/InputStream.html), LoaderService lo carica utilizzando il metodo LoaderService.fromInputStream.







{{< highlight java >}}

 public void onFileUpload(FileUploadEvent e) {

    this.current = loader.fromInputStream(e.getFile().getInputstream(), e.getFile().getFileName());

}

{{< /highlight >}}







**Caricamento e scaricamento**

Il metodo ***LoaderService.fromInputStream*** legge l'***InputStream*** fornito dal componente ***fileUpload*** e crea un'istanza della classe ***com.aspose.cells.Workbook***. Questa istanza viene conservata in memoria finché l'utente continua a visualizzare o modificare il foglio di calcolo nel browser web. Quando l'utente lascia l'editor o chiude il browser, le istanze inutilizzate vengono scaricate automaticamente dalla memoria per mantenere pulito il server.







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







**Memorizzazione nella cache**

La memorizzazione nella cache è molto importante per l'Editor di fogli di calcolo HTML5. Rende tutto più fluido. Il CellsService mantiene in cache righe, colonne, celle e proprietà di tutti i fogli di lavoro caricati dall'editor. Quando LoaderService carica completamente un foglio di calcolo, lo legge dall'alto verso il basso e riempie la cache chiamando LoaderService.buildCellsCache, LoaderService.buildColumnWidthCache, LoaderService.buildRowHeightCache







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






### **Apri da Dropbox**
Per aprire i file da Dropbox:

1. Passa alla scheda **File** in alto.
1. Fare clic su **Apri da Dropbox** per aprire il selettore dei file di Dropbox.
1. Se non si è già effettuato l'accesso, verrà richiesto di accedere al proprio account Dropbox.
1. Passa al file desiderato e fai clic per selezionarlo.
1. Fai clic su **Scegli** in fondo.

Il file selezionato verrà aperto da Dropbox.

![todo:image_alt_text](1e2sfo0.png)

**Come funziona?**

Il pulsante **Apri da Dropbox** utilizza **Dropbox JavaScript Chooser API** per aprire il dialogo di scelta di Dropbox. Il selettore fornisce l'URL del file selezionato, che viene catturato dalla funzione di callback e inviato indietro al server. Il server crea un'istanza del foglio di calcolo dall'URL, inizializza alcune cose relative alla gestione e invia aggiornamenti del DOM al browser. Il browser renderizza e aggiorna l'HTML e l'utente è pronto per modificare il documento caricato.
### **Apri da URL**
I file possono essere aperti direttamente da URL. Questo consente all'utente di modificare qualsiasi file disponibile pubblicamente su Internet. Per aprire il file, aggiungi il parametro **?url=ubicazione** con il valore della tua **ubicazione** desiderata durante il caricamento dell'editor. Ad esempio:

{{< highlight java >}}

 http://editor.aspose.com/?url=http://example.com/Sample.xlsx

{{< /highlight >}}

![todo:image_alt_text](exc9ckp.png)

**Come funziona?**

**Istanziare durante l'avvio**

Quando il bean di backend **WorksheetView** viene istanziato da JSF il metodo **PostConstruct** **init** viene chiamato, caricando il foglio di calcolo utilizzando LoaderService.fromUrl.

**Memorizzazione nella cache**

La memorizzazione nella cache avviene subito dopo il caricamento del foglio di calcolo. Il **LoaderService** chiama **LoaderService.buildCellsCache**, **LoaderService.buildColumnWidthCache** e **LoaderService.buildRowHeightCache** uno per uno per memorizzare nella cache il contenuto del foglio di calcolo e mantenere tutte le operazioni veloci e fluide.

**Aggiornamenti del DOM**

Quando il foglio di calcolo è pronto sul lato server, i componenti JSF vengono utilizzati per generare un nuovo HTML e inviare aggiornamenti del DOM all'utente che vengono resi dal browser web.







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






### **Crea un nuovo foglio di calcolo**
Per creare un nuovo foglio di calcolo vuoto:

1. Passa alla scheda **File**.
1. Fai clic sul pulsante **Nuovo**.

L'editor chiuderà il foglio di calcolo aperto, se presente, e ne aprirà uno nuovo.

![todo:image_alt_text](lnydmmf.png)

**Come funziona?**

**Istituire un nuovo oggetto**

Quando l'utente fa clic sul pulsante **Nuovo**, **WorksheetView.loadBlank** viene chiamato, che alla fine chiama **LoaderService.fromBlank**. LoaderService crea una nuova istanza di foglio di calcolo vuoto.

**Memorizzazione nella cache**

La memorizzazione nella cache avviene subito dopo il caricamento del foglio di calcolo. Il **LoaderService** chiama **LoaderService.buildCellsCache**, **LoaderService.buildColumnWidthCache** e **LoaderService.buildRowHeightCache** uno per uno per memorizzare nella cache il contenuto del foglio di calcolo e mantenere tutte le operazioni veloci e fluide.

**Aggiornamenti del DOM**

Quando il foglio di calcolo è pronto sul lato server, i componenti JSF vengono utilizzati per generare un nuovo HTML e inviare aggiornamenti del DOM all'utente che vengono resi dal browser web.







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






### **Esporta in vari formati**
Dopo aver modificato i file, l'utente vorrà salvare le modifiche. L'editor consente all'utente di esportare e scaricare il foglio di calcolo modificato sul computer locale. Per esportare il file:

1. Passa alla scheda **File** in alto.
1. Fai clic su **Esporta** come pulsante.
1. Scegli il formato desiderato dal menu a discesa.

Il file modificato verrà esportato per il download. I seguenti formati sono supportati per l'esportazione:

- Excel 2007-2013 XLSX
- Excel 1997-2003 XLS
- Excel XLSM
- Excel XLSB
- Excel XLTX
- Excel XLTM
- SpreadsheetML
- Formato di Documento Portatile (PDF)
- Foglio di calcolo OpenDocument (ODS)

**Come funziona?**

Il foglio di calcolo aperto viene convertito nel formato specificato dall'utente utilizzando **WorksheetView.getOutputFile**.







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






