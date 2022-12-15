---
title: Editor di fogli di calcolo - Lavorare con i file
type: docs
weight: 10
url: /it/java/spreadsheet-editor-working-with-files/
---
**Sommario**

- [File supportati](#SpreadsheetEditor-WorkingwithFiles-SupportedFiles)
- [Apri file locali](#SpreadsheetEditor-WorkingwithFiles-OpenLocalFiles) 
 - LoaderService.buildColumnWidthCache
 - LoaderService.buildRowHeightCache
- [Apri da Dropbox](#SpreadsheetEditor-WorkingwithFiles-OpenfromDropbox)
- [Apri dall'URL](#SpreadsheetEditor-WorkingwithFiles-OpenfromURL) 
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
HTML5 Spreadsheet Editor può aprire file nei seguenti formati:

- Excel 1997-2003 XLS
- Excel 2007-2013 XLSX
- XLSM
- XLSB
- XLTX
- Foglio di calcoloML
- CVS
- ApriDocumento
### **Apri file locali**
Per caricare un file dal computer locale:

1.  Passa a**Scheda File** in cima.
1.  Clic**Apri dal computer** per aprire la finestra di dialogo Sfoglia.
1. Vai alla posizione desiderata del file.
1. Fare clic sul file desiderato per selezionarlo.
1.  Clic**Aprire**.

Il file verrà aperto nell'editor.

![cose da fare:immagine_alt_testo](bwyl3xi.png)

**Come funziona?**

**Upload di file**

 L'utente seleziona un file dal computer locale che viene caricato dal browser Web sul server e ricevuto da[File PrimeFaces Caricamento](https://www.primefaces.org/showcase/ui/file/upload/basic.xhtml) componente.

{{< highlight "java" >}}

 <p:fileUpload fileUploadListener="#\{workbook.onFileUpload\}" update=":ribbon :intro :sheet" />

{{< /highlight >}}

**Gestire la cartella di lavoro**

 Non appena il file viene caricato completamente, il metodo WorkbookService.onFileUpload entra in azione per gestire la situazione. WorkbookService riceve gli eventi dal browser Web e tiene traccia dello stato dell'intera cartella di lavoro. WorkbookService.onFileUpload passa il controllo a LoaderService per caricare la cartella di lavoro in memoria. Come la***upload di file*** componente fornisce il file caricato come file[InputStream](https://docs.oracle.com/javase/8/docs/api/index.html?java/io/InputStream.html), il LoaderService lo carica utilizzando il metodo LoaderService.fromInputStream.







{{< highlight "java" >}}

 public void onFileUpload(FileUploadEvent e) {

    this.current = loader.fromInputStream(e.getFile().getInputstream(), e.getFile().getFileName());

}

{{< /highlight >}}







**Caricamento e scaricamento**

 Il metodo***LoaderService.fromInputStream*** legge il***InputStream*** fornito da fileUpload***componente*** creare un'istanza di***com.aspose.cells.Workbook*** classe. Questa istanza viene mantenuta in memoria finché l'utente continua a visualizzare o modificare il foglio di calcolo nel browser web. Quando l'utente lascia l'editor o chiude il browser, le istanze inutilizzate vengono automaticamente scaricate dalla memoria per mantenere pulito il server.







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







**Cache**

La memorizzazione nella cache è molto importante per l'editor di fogli di calcolo HTML5. Fa funzionare tutto senza intoppi. CellsService mantiene nella cache righe, colonne, celle e proprietà di tutte le cartelle di lavoro caricate dall'editor. Quando LoaderService carica completamente un foglio di calcolo, lo legge dall'alto verso il basso e riempie la cache chiamando LoaderService.buildCellsCache, LoaderService.buildColumnWidthCache, LoaderService.buildRowHeightCache







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






### **Apri da Dropbox**
Per aprire file da Dropbox:

1.  Passa a**Scheda File** in cima.
1.  Clic**Apri da Dropbox** per aprire il selettore di file di Dropbox.
1. Se non hai già effettuato l'accesso, ti verrà richiesto di accedere al tuo account Dropbox.
1. Passare al file desiderato e fare clic per selezionarlo.
1.  Clic**Scegliere** in fondo.

Il file selezionato verrà aperto da Dropbox.

![cose da fare:immagine_alt_testo](1e2sfo0.png)

**Come funziona?**

 Il**Apri da Dropbox** pulsante utilizza**API di selezione JavaScript di Dropbox**per aprire la finestra di dialogo di Dropbox Chooser. Il Chooser fornisce l'URL del file selezionato, che viene acquisito dalla funzione di callback e rispedito al server. Il server crea un'istanza di foglio di calcolo dall'URL, inizializza alcune cose di pulizia e invia gli aggiornamenti DOM al browser. Il browser esegue il rendering e aggiorna l'HTML e l'utente è pronto per modificare il documento caricato.
### **Apri dall'URL**
 I file possono essere aperti direttamente dagli URL. Ciò consente all'utente di modificare qualsiasi file pubblicamente disponibile su Internet. Per aprire il file append**?url=posizione** parametro con il valore desiderato**Posizione** durante il caricamento dell'editor. Per esempio:

{{< highlight "java" >}}

 http://editor.aspose.com/?url=http://example.com/Sample.xlsx

{{< /highlight >}}

![cose da fare:immagine_alt_testo](exc9ckp.png)

**Come funziona?**

**Crea un'istanza durante l'avvio**

 quando**Foglio di lavoroVisualizza** bean backend è istanziato da JSF the**PostConstruct** metodo**dentro** viene chiamato che carica il foglio di calcolo utilizzando LoaderService.fromUrl.

**Cache**

 La memorizzazione nella cache avviene subito dopo il caricamento del foglio di calcolo. Il**LoaderService** chiamate**LoaderService.buildCellsCache**, **LoaderService.buildColumnWidthCache** e**LoaderService.buildRowHeightCache**uno a uno per memorizzare nella cache il contenuto del foglio di calcolo e mantenere tutte le operazioni veloci e fluide.

**Aggiornamenti DOM**

Quando il foglio di calcolo è pronto sul lato server, i componenti JSF vengono utilizzati per generare nuovo HTML e inviare aggiornamenti DOM all'utente che vengono visualizzati dal browser web.







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






### **Crea un nuovo foglio di calcolo**
Per creare un nuovo foglio di calcolo vuoto:

1.  Passa a**Scheda File**.
1.  Clicca il**Nuovo** pulsante.

L'editor chiuderà il foglio di calcolo aperto, se presente, e ne aprirà uno nuovo.

![cose da fare:immagine_alt_testo](lnydmmf.png)

**Come funziona?**

**Crea un'istanza di un nuovo oggetto**

 Quando il**Nuovo** il pulsante viene cliccato dall'utente,**WorksheetView.loadBlank** , che alla fine chiama**LoaderService.fromBlank**. LoaderService crea una nuova istanza di foglio di calcolo vuoto.

**Cache**

 La memorizzazione nella cache avviene subito dopo il caricamento del foglio di calcolo. Il**LoaderService** chiamate**LoaderService.buildCellsCache**, **LoaderService.buildColumnWidthCache** e**LoaderService.buildRowHeightCache**uno a uno per memorizzare nella cache il contenuto del foglio di calcolo e mantenere tutte le operazioni veloci e fluide.

**Aggiornamenti DOM**

Quando il foglio di calcolo è pronto sul lato server, i componenti JSF vengono utilizzati per generare nuovo HTML e inviare aggiornamenti DOM all'utente che vengono visualizzati dal browser web.







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






### **Esporta in vari formati**
Dopo aver modificato i file, l'utente vorrà salvare le modifiche. L'editor consente all'utente di esportare e scaricare il foglio di calcolo modificato sul computer locale. Per esportare il file:

1.  Passa a**Scheda File** in cima.
1.  Clic**Esportare** come pulsante.
1. Scegli il formato desiderato dal menu a discesa.

Il file modificato verrà esportato per il download. I seguenti formati sono supportati per l'esportazione:

- Excel 2007-2013 XLSX
- Excel 1997-2003 XLS
- Excel XLSM
- Excel XLSB
- Excel XLTX
- Excel XL™
- Foglio di calcoloML
- Formato documento portatile (PDF)
- Foglio di calcolo OpenDocument (ODS)

**Come funziona?**

 Il foglio di calcolo aperto viene convertito nel formato specificato dall'utente utilizzando**WorksheetView.getOutputFile**.







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






