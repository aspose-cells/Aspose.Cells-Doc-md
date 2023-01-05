---
title: Tabelleneditor - Arbeiten mit Dateien
type: docs
weight: 10
url: /de/java/spreadsheet-editor-working-with-files/
---
**Inhaltsverzeichnis**

- [Unterstützte Dateien](#SpreadsheetEditor-WorkingwithFiles-SupportedFiles)
- [Lokale Dateien öffnen](#SpreadsheetEditor-WorkingwithFiles-OpenLocalFiles) 
 - LoaderService.buildColumnWidthCache
 - LoaderService.buildRowHeightCache
- [Aus Dropbox öffnen](#SpreadsheetEditor-WorkingwithFiles-OpenfromDropbox)
- [Von URL öffnen](#SpreadsheetEditor-WorkingwithFiles-OpenfromURL) 
 - LoaderService.fromUrl
 - LoaderService.buildCellsCache
 - LoaderService.buildColumnWidthCache
 - LoaderService.buildRowHeightCache
- [Erstellen Sie eine neue Tabelle](#SpreadsheetEditor-WorkingwithFiles-CreateaNewSpreadsheet) 
 - LoaderService.fromBlank
 - buildCellsCache
 - buildColumnWidthCache
 - buildRowHeightCache
- [Export in verschiedene Formate](#SpreadsheetEditor-WorkingwithFiles-ExporttoVariousFormats)
### **Unterstützte Dateien**
Der HTML5-Tabellen-Editor kann Dateien in den folgenden Formaten öffnen:

- Excel 1997-2003 XLS
- Excel 2007-2013 XLSX
- XLSM
- XLSB
- XLTX
- SpreadsheetML
- Lebenslauf
- OpenDocument
### **Lokale Dateien öffnen**
So laden Sie eine Datei vom lokalen Computer hoch:

1.  Wechseln zu**Registerkarte Datei** oben drauf.
1.  Klicken**Vom Computer öffnen** , um das Dialogfeld „Durchsuchen“ zu öffnen.
1. Gehen Sie zum gewünschten Speicherort der Datei.
1. Klicken Sie auf die gewünschte Datei, um sie auszuwählen.
1.  Klicken**Offen**.

Die Datei wird im Editor geöffnet.

![todo: Bild_alt_Text](bwyl3xi.png)

**Wie es funktioniert?**

**Datei-Upload**

 Der Benutzer wählt eine Datei vom lokalen Computer aus, die vom Webbrowser auf den Server hochgeladen und empfangen wird[PrimeFaces-DateiUpload](https://www.primefaces.org/showcase/ui/file/upload/basic.xhtml) Komponente.

{{< highlight "java" >}}

 <p:fileUpload fileUploadListener="#\{workbook.onFileUpload\}" update=":ribbon :intro :sheet" />

{{< /highlight >}}

**Arbeitsbuch verwalten**

 Sobald die Datei vollständig hochgeladen ist, tritt die WorkbookService.onFileUpload-Methode in Aktion, um die Situation zu behandeln. WorkbookService empfängt Ereignisse vom Webbrowser und verfolgt den Status der gesamten Arbeitsmappe. WorkbookService.onFileUpload übergibt die Steuerung an LoaderService, um die Arbeitsmappe in den Arbeitsspeicher zu laden. Als die***Datei-Upload*** Komponente stellt die hochgeladene Datei als[Eingabestrom](https://docs.oracle.com/javase/8/docs/api/index.html?java/io/InputStream.html), der LoaderService lädt es mit der Methode LoaderService.fromInputStream.







{{< highlight "java" >}}

 public void onFileUpload(FileUploadEvent e) {

    this.current = loader.fromInputStream(e.getFile().getInputstream(), e.getFile().getFileName());

}

{{< /highlight >}}







**Laden und Entladen**

 Die Methode***LoaderService.fromInputStream*** liest die***Eingabestrom*** bereitgestellt von fileUpload***Komponente*** Instanz erstellen von***com.aspose.cells.Workbook***Klasse. Diese Instanz wird gespeichert, solange der Benutzer die Tabelle im Webbrowser anzeigt oder bearbeitet. Wenn der Benutzer den Editor verlässt oder den Browser schließt, werden die nicht verwendeten Instanzen automatisch aus dem Speicher entfernt, um den Server sauber zu halten.







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







**Caching**

Caching ist für den HTML5-Tabellen-Editor sehr wichtig. Damit funktioniert alles reibungslos. Der CellsService speichert Zeilen, Spalten, Zellen und Eigenschaften aller vom Editor geladenen Arbeitsmappen im Cache. Wenn LoaderService eine Tabelle vollständig lädt, liest es sie von oben nach unten und füllt den Cache durch Aufrufen von LoaderService.buildCellsCache, LoaderService.buildColumnWidthCache, LoaderService.buildRowHeightCache







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






### **Aus Dropbox öffnen**
So öffnen Sie Dateien aus Dropbox:

1.  Wechseln zu**Registerkarte Datei** oben drauf.
1.  Klicken**Aus Dropbox öffnen** um die Dropbox-Dateiauswahl zu öffnen.
1. Wenn Sie noch nicht angemeldet sind, müssen Sie sich bei Ihrem Dropbox-Konto anmelden.
1. Navigieren Sie zur gewünschten Datei und klicken Sie darauf, um sie auszuwählen.
1.  Klicken**Wählen** unten.

Ihre ausgewählte Datei wird von Dropbox geöffnet.

![todo: Bild_alt_Text](1e2sfo0.png)

**Wie es funktioniert?**

 Das**Aus Dropbox öffnen** Schaltfläche verwendet**Dropbox-JavaScript-Auswahl API** , um das Dropbox-Auswahldialogfeld zu öffnen. Die Auswahl stellt die URL der ausgewählten Datei bereit, die von der Rückruffunktion erfasst und an den Server zurückgesendet wird. Der Server erstellt eine Instanz der Tabelle aus der URL, initialisiert einige Verwaltungsaufgaben und sendet DOM-Aktualisierungen an den Browser zurück. Der Browser rendert und aktualisiert HTML und der Benutzer ist bereit, das geladene Dokument zu bearbeiten.
### **Von URL öffnen**
 Dateien können direkt aus URLs geöffnet werden. Dadurch kann der Benutzer jede öffentlich verfügbare Datei im Internet bearbeiten. Zum Öffnen der Datei anhängen**?url=Standort** Parameter mit dem gewünschten Wert**Lage** beim Laden des Editors. Zum Beispiel:

{{< highlight "java" >}}

 http://editor.aspose.com/?url=http://example.com/Sample.xlsx

{{< /highlight >}}

![todo: Bild_alt_Text](exc9ckp.png)

**Wie es funktioniert?**

**Instanziieren Sie während des Starts**

 Wann**Arbeitsblattansicht** Backend-Bean wird von JSF instanziiert**PostKonstrukt** Methode**drin** aufgerufen, die die Tabelle mit LoaderService.fromUrl lädt.

**Caching**

 Das Caching erfolgt direkt nach dem Laden der Tabelle. Das**LoaderService** Anrufe**LoaderService.buildCellsCache**, **LoaderService.buildColumnWidthCache** und**LoaderService.buildRowHeightCache** eins nach dem anderen, um den Inhalt der Tabelle zwischenzuspeichern und alle Vorgänge schnell und reibungslos zu halten.

**DOM-Updates**

Wenn die Tabelle serverseitig bereit ist, werden JSF-Komponenten verwendet, um neue HTML zu generieren und DOM-Aktualisierungen an den Benutzer zu senden, die vom Webbrowser gerendert werden.







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






### **Erstellen Sie eine neue Tabelle**
So erstellen Sie eine neue leere Tabelle:

1.  Wechseln zu**Registerkarte Datei**.
1.  Drücke den**Neu** Knopf.

Der Editor schließt die geöffnete Tabelle, falls vorhanden, und öffnet eine neue.

![todo: Bild_alt_Text](lnydmmf.png)

**Wie es funktioniert?**

**Instanziieren Sie ein neues Objekt**

 Wenn die**Neu** Schaltfläche wird vom Benutzer angeklickt,**WorksheetView.loadBlank** , die schließlich anruft**LoaderService.fromBlank**. LoaderService erstellt eine neue Instanz einer leeren Tabelle.

**Caching**

 Das Caching erfolgt direkt nach dem Laden der Tabelle. Das**LoaderService** Anrufe**LoaderService.buildCellsCache**, **LoaderService.buildColumnWidthCache** und**LoaderService.buildRowHeightCache** eins nach dem anderen, um den Inhalt der Tabelle zwischenzuspeichern und alle Vorgänge schnell und reibungslos zu halten.

**DOM-Updates**

Wenn die Tabelle serverseitig bereit ist, werden JSF-Komponenten verwendet, um neue HTML zu generieren und DOM-Aktualisierungen an den Benutzer zu senden, die vom Webbrowser gerendert werden.







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






### **Export in verschiedene Formate**
Nach dem Bearbeiten von Dateien möchte der Benutzer die Änderungen speichern. Der Editor ermöglicht es dem Benutzer, die modifizierte Tabelle zu exportieren und auf den lokalen Computer herunterzuladen. So exportieren Sie die Datei:

1.  Wechseln zu**Registerkarte Datei** oben drauf.
1.  Klicken**Export** als Knopf.
1. Wählen Sie Ihr gewünschtes Format aus der Dropdown-Liste.

Die geänderte Datei wird zum Download exportiert. Die folgenden Formate werden für den Export unterstützt:

- Excel 2007-2013 XLSX
- Excel 1997-2003 XLS
- Excel XLSM
- Excel XLSB
- Excel XLTX
- Excel XLTM
- SpreadsheetML
- Portables Dokumentenformat (PDF)
- OpenDocument-Tabelle (ODS)

**Wie es funktioniert?**

 Die geöffnete Tabelle wird mit in ein benutzerdefiniertes Format konvertiert**WorksheetView.getOutputFile**.







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






