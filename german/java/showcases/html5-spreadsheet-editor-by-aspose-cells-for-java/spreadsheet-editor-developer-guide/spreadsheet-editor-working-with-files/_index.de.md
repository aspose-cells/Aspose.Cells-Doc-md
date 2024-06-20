---
title: Tabellenkalkulations Editor – Arbeiten mit Dateien
type: docs
weight: 10
url: /de/java/spreadsheet-editor-working-with-files/
---

**Inhaltsverzeichnis**

- [Unterstützte Dateien](#SpreadsheetEditor-WorkingwithFiles-SupportedFiles)
- [Öffnen Sie lokale Dateien](#SpreadsheetEditor-WorkingwithFiles-OpenLocalFiles) 
  - LoaderService.buildColumnWidthCache
  - LoaderService.buildRowHeightCache
- [Aus Dropbox öffnen](#SpreadsheetEditor-WorkingwithFiles-OpenfromDropbox)
- [Von URL öffnen](#SpreadsheetEditor-WorkingwithFiles-OpenfromURL) 
  - LoaderService.fromUrl
  - LoaderService.buildCellsCache
  - LoaderService.buildColumnWidthCache
  - LoaderService.buildRowHeightCache
- [Neue Tabelle erstellen](#SpreadsheetEditor-WorkingwithFiles-CreateaNewSpreadsheet) 
  - LoaderService.fromBlank
  - buildCellsCache
  - buildColumnWidthCache
  - buildRowHeightCache
- [Exportieren in verschiedene Formate](#SpreadsheetEditor-WorkingwithFiles-ExporttoVariousFormats)
### **Unterstützte Dateien**
Der HTML5-Tabellen-Editor kann Dateien in den folgenden Formaten öffnen:

- Excel 1997-2003 XLS
- Excel 2007-2013 XLSX
- XLSM
- XLSB
- XLTX
- SpreadsheetML
- CVS
- OpenDocument
### **Öffnen Sie lokale Dateien**
Um eine Datei vom lokalen Computer hochzuladen:

1. Wechseln Sie zum **Datei-Tab** oben.
1. Klicken Sie auf **Von Computer öffnen**, um den Dialog zum Durchsuchen zu öffnen.
1. Gehen Sie zu Ihrem gewünschten Speicherort der Datei.
1. Klicken Sie auf die gewünschte Datei, um sie auszuwählen.
1. Klicken Sie auf **Öffnen**.

Die Datei wird im Editor geöffnet.

![todo:image_alt_text](bwyl3xi.png)

**Wie funktioniert es?**

**Datei-Upload**

Der Benutzer wählt eine Datei vom lokalen Computer aus, die vom Webbrowser auf den Server hochgeladen und vom [PrimeFaces-Datei-Upload](https://www.primefaces.org/showcase/ui/file/upload/basic.xhtml) Komponent empfangen wird.

{{< highlight java >}}

 <p:fileUpload fileUploadListener="#\{workbook.onFileUpload\}" update=":ribbon :intro :sheet" />

{{< /highlight >}}

**Arbeitsmappe verwalten**

Sobald die Datei vollständig hochgeladen ist, wird die WorkbookService.onFileUpload-Methode aktiviert, um die Situation zu behandeln. Der WorkbookService erhält Ereignisse vom Webbrowser und behält den Zustand der gesamten Arbeitsmappe im Auge. Der WorkbookService.onFileUpload übergibt die Kontrolle an den LoaderService, um die Arbeitsmappe in den Speicher zu laden. Da die ***fileUpload*** Komponente die hochgeladene Datei als [InputStream](https://docs.oracle.com/javase/8/docs/api/index.html?java/io/InputStream.html) bereitstellt, lädt der LoaderService sie mithilfe der Methode LoaderService.fromInputStream.







{{< highlight java >}}

 public void onFileUpload(FileUploadEvent e) {

    this.current = loader.fromInputStream(e.getFile().getInputstream(), e.getFile().getFileName());

}

{{< /highlight >}}







**Laden und Entladen**

Die Methode ***LoaderService.fromInputStream*** liest den ***InputStream***, den die fileUpload ***Komponente*** bereitstellt, erstellt eine Instanz der ***com.aspose.cells.Workbook*** Klasse. Diese Instanz wird im Speicher behalten, solange der Benutzer die Tabelle im Webbrowser ansieht oder bearbeitet. Wenn der Benutzer den Editor verlässt oder den Browser schließt, werden die unbenutzten Instanzen automatisch aus dem Speicher entfernt, um den Server sauber zu halten.







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







**Zwischenspeicherung**

Caching ist für den HTML5-Tabellenkalkulationseditor sehr wichtig. Es sorgt für reibungslosen Ablauf. Der CellsService speichert Zwischenspeicherzeilen, -spalten, -zellen und -eigenschaften aller Arbeitsmappen, die vom Editor geladen wurden. Wenn der LoaderService eine Tabelle vollständig lädt, liest er sie von oben nach unten und füllt den Cache, indem er LoaderService.buildCellsCache, LoaderService.buildColumnWidthCache, LoaderService.buildRowHeightCache aufruft.







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






### **Aus Dropbox öffnen**
Um Dateien von Dropbox zu öffnen:

1. Wechseln Sie zum **Datei-Tab** oben.
1. Klicken Sie auf **Von Dropbox öffnen**, um den Dateiauswähler von Dropbox zu öffnen.
1. Falls Sie nicht bereits angemeldet sind, müssen Sie sich in Ihrem Dropbox-Konto anmelden.
1. Navigieren Sie zur gewünschten Datei und klicken Sie darauf, um sie auszuwählen.
1. Klicken Sie unten auf **Auswählen**.

Die ausgewählte Datei wird von Dropbox geöffnet.

![todo:image_alt_text](1e2sfo0.png)

**Wie funktioniert es?**

Der **Von Dropbox öffnen**-Button verwendet die **Dropbox JavaScript Chooser API**, um den Dropbox-Auswählerdialog zu öffnen. Der Auswähler stellt die URL der ausgewählten Datei bereit, die von der Callback-Funktion erfasst und an den Server gesendet wird. Der Server erstellt eine Instanz der Tabelle aus der URL, initialisiert einige Verwaltungsaufgaben und sendet DOM-Updates zurück an den Browser. Der Browser rendert und aktualisiert das HTML, und der Benutzer kann das geladene Dokument bearbeiten.
### **Von URL öffnen**
Dateien können direkt von URLs geöffnet werden. Dies ermöglicht es dem Benutzer, jede öffentlich verfügbare Datei im Internet zu bearbeiten. Um die Datei zu öffnen, fügen Sie beim Laden des Editors den Parameter **?url=Standort** mit dem Wert Ihres gewünschten **Standorts** hinzu. Zum Beispiel:

{{< highlight java >}}

 http://editor.aspose.com/?url=http://example.com/Sample.xlsx

{{< /highlight >}}

![todo:image_alt_text](exc9ckp.png)

**Wie funktioniert es?**

**Beim Start instanziieren**

Wenn das Backend-Bean **WorksheetView** von JSF instanziiert wird, wird die Methode **init** von **PostConstruct** aufgerufen, um die Tabelle mithilfe von LoaderService.fromUrl zu laden.

**Zwischenspeicherung**

Das Caching erfolgt direkt nachdem die Tabelle geladen ist. Der **LoaderService** ruft nacheinander **LoaderService.buildCellsCache**, **LoaderService.buildColumnWidthCache** und **LoaderService.buildRowHeightCache** auf, um den Inhalt der Tabelle zu zwischenspeichern und alle Operationen schnell und reibungslos zu halten.

**DOM-Aktualisierungen**

Wenn die Tabelle auf der Serverseite bereit ist, werden JSF-Komponenten verwendet, um ein neues HTML zu generieren und DOM-Aktualisierungen an den Benutzer zu senden, die vom Webbrowser gerendert werden.







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






### **Neue Tabelle erstellen**
Um eine neue leere Tabelle zu erstellen:

1. Wechseln Sie zum **Datei-Tab**.
1. Klicken Sie auf die Schaltfläche **Neu**.

Der Editor wird die geöffnete Tabelle schließen, falls vorhanden, und eine neue öffnen.

![todo:image_alt_text](lnydmmf.png)

**Wie funktioniert es?**

**Instanziieren Sie ein neues Objekt**

Wenn der Benutzer auf die Schaltfläche **Neu** klickt, wird **WorksheetView.loadBlank** aufgerufen, was letztendlich **LoaderService.fromBlank** aufruft. LoaderService erstellt eine neue Instanz einer leeren Tabelle.

**Zwischenspeicherung**

Das Caching erfolgt direkt nachdem die Tabelle geladen ist. Der **LoaderService** ruft nacheinander **LoaderService.buildCellsCache**, **LoaderService.buildColumnWidthCache** und **LoaderService.buildRowHeightCache** auf, um den Inhalt der Tabelle zu zwischenspeichern und alle Operationen schnell und reibungslos zu halten.

**DOM-Aktualisierungen**

Wenn die Tabelle auf der Serverseite bereit ist, werden JSF-Komponenten verwendet, um ein neues HTML zu generieren und DOM-Aktualisierungen an den Benutzer zu senden, die vom Webbrowser gerendert werden.







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






### **Exportieren in verschiedene Formate**
Nachdem Dateien bearbeitet wurden, möchte der Benutzer die Änderungen speichern. Der Editor ermöglicht es dem Benutzer, die modifizierte Tabelle zu exportieren und auf seinen lokalen Computer herunterzuladen. Um die Datei zu exportieren:

1. Wechseln Sie zum **Datei-Tab** oben.
1. Klicken Sie auf **Export** als Schaltfläche.
1. Wählen Sie Ihr gewünschtes Format aus der Dropdown-Liste.

Die modifizierte Datei wird zum Download exportiert. Folgende Formate werden für den Export unterstützt:

- Excel 2007-2013 XLSX
- Excel 1997-2003 XLS
- Excel XLSM
- Excel XLSB
- Excel XLTX
- Excel XLTM
- SpreadsheetML
- Portable Document Format (PDF)
- OpenDocument-Tabellenkalkulation (ODS)

**Wie funktioniert es?**

Die geöffnete Tabelle wird in das vom Benutzer angegebene Format über **WorksheetView.getOutputFile** konvertiert.







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






