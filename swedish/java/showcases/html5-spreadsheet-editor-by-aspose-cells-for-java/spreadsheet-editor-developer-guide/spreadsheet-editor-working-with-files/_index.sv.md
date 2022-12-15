---
title: Kalkylarksredigerare - Arbeta med filer
type: docs
weight: 10
url: /sv/java/spreadsheet-editor-working-with-files/
---
**Innehållsförteckning**

- [Filer som stöds](#SpreadsheetEditor-WorkingwithFiles-SupportedFiles)
- [Öppna Lokala filer](#SpreadsheetEditor-WorkingwithFiles-OpenLocalFiles) 
 - LoaderService.buildColumnWidthCache
 - LoaderService.buildRowHeightCache
- [Öppna från Dropbox](#SpreadsheetEditor-WorkingwithFiles-OpenfromDropbox)
- [Öppna från URL](#SpreadsheetEditor-WorkingwithFiles-OpenfromURL) 
 - LoaderService.fromUrl
 - LoaderService.buildCellsCache
 - LoaderService.buildColumnWidthCache
 - LoaderService.buildRowHeightCache
- [Skapa ett nytt kalkylblad](#SpreadsheetEditor-WorkingwithFiles-CreateaNewSpreadsheet) 
 - LoaderService.fromBlank
 - buildCellsCache
 - buildColumnWidthCache
 - buildRowHeightCache
- [Exportera till olika format](#SpreadsheetEditor-WorkingwithFiles-ExporttoVariousFormats)
### **Filer som stöds**
HTML5 Spreadsheet Editor kan öppna filer i följande format:

- Excel 1997-2003 XLS
- Excel 2007-2013 XLSX
- XLSM
- XLSB
- XLTX
- SpreadsheetML
- CVS
- Öppna Dokument
### **Öppna Lokala filer**
Så här laddar du upp en fil från en lokal dator:

1.  Byta till**Fliken Arkiv** överst.
1.  Klick**Öppna från datorn** för att öppna dialogrutan Bläddra.
1. Gå till önskad plats för filen.
1. Klicka på önskad fil för att välja den.
1.  Klick**Öppna**.

Filen kommer att öppnas i editorn.

![todo:image_alt_text](bwyl3xi.png)

**Hur det fungerar?**

**Filuppladdning**

 Användaren väljer en fil från den lokala datorn som laddas upp från webbläsaren till servern och tas emot av[Ladda upp PrimeFaces-fil](https://www.primefaces.org/showcase/ui/file/upload/basic.xhtml) komponent.

{{< highlight "java" >}}

 <p:fileUpload fileUploadListener="#\{workbook.onFileUpload\}" update=":ribbon :intro :sheet" />

{{< /highlight >}}

**Hantera arbetsbok**

 Så snart filen har laddats upp helt, träder metoden WorkbookService.onFileUpload till handling för att hantera situationen. WorkbookService tar emot händelser från webbläsaren och håller reda på tillståndet för hela arbetsboken. WorkbookService.onFileUpload överför kontrollen till LoaderService för att ladda arbetsboken i minnet. Som den***filuppladdning*** komponenten tillhandahåller den uppladdade filen som en[InputStream](https://docs.oracle.com/javase/8/docs/api/index.html?java/io/InputStream.html), laddar LoaderService den med metoden LoaderService.fromInputStream.







{{< highlight "java" >}}

 public void onFileUpload(FileUploadEvent e) {

    this.current = loader.fromInputStream(e.getFile().getInputstream(), e.getFile().getFileName());

}

{{< /highlight >}}







**Lasta och lasta av**

 Metoden***LoaderService.fromInputStream*** läser***InputStream*** tillhandahålls av fileUpload***komponent*** skapa instans av***com.aspose.cells.Workbook*** klass. Denna instans sparas i minnet så länge användaren fortsätter att visa eller redigera kalkylarket i webbläsaren. När användaren lämnar editorn eller stänger webbläsaren laddas de oanvända instanserna automatiskt bort från minnet för att hålla servern ren.







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







**Cachning**

Cachning är mycket viktigt för HTML5 Spreadsheet Editor. Det gör att allt fungerar smidigt. CellsService behåller cache-rader, kolumner, celler och egenskaper för alla arbetsböcker som laddas av redigeraren. När LoaderService laddar ett kalkylark helt läser det uppifrån och ned och fyller cachen genom att anropa LoaderService.buildCellsCache, LoaderService.buildColumnWidthCache, LoaderService.buildRowHeightCache







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






### **Öppna från Dropbox**
Så här öppnar du filer från Dropbox:

1.  Byta till**Fliken Arkiv** överst.
1.  Klick**Öppna från Dropbox** för att öppna Dropbox-filväljaren.
1. Om du inte redan är inloggad måste du logga in på ditt Dropbox-konto.
1. Navigera till önskad fil och klicka för att välja den.
1.  Klick**Välja** på botten.

Din valda fil kommer att öppnas från Dropbox.

![todo:image_alt_text](1e2sfo0.png)

**Hur det fungerar?**

 De**Öppna från Dropbox** knappen använder**Dropbox JavaScript-väljare API**för att öppna dialogrutan Dropbox Väljare. Väljaren tillhandahåller URL till den valda filen, som fångas upp av återuppringningsfunktionen och skickas tillbaka till servern. Servern skapar en instans av kalkylblad från URL, initierar några hushållsgrejer och skickar DOM-uppdateringar tillbaka till webbläsaren. Webbläsaren renderar och uppdaterar HTML-koden och användaren är redo att redigera det laddade dokumentet.
### **Öppna från URL**
 Filer kan öppnas direkt från URL:er. Detta tillåter användaren att redigera alla offentligt tillgängliga filer på Internet. För att öppna filen lägg till**?url=plats** parameter med värdet av önskat värde**plats** medan du laddar redigeraren. Till exempel:

{{< highlight "java" >}}

 http://editor.aspose.com/?url=http://example.com/Sample.xlsx

{{< /highlight >}}

![todo:image_alt_text](exc9ckp.png)

**Hur det fungerar?**

**Instantiera under uppstart**

 När**Arbetsbladsvy** backend bean instansieras av JSF**PostConstruct** metod**i det** kallas som laddar kalkylarket med LoaderService.fromUrl.

**Cachning**

 Cachning sker direkt efter att kalkylarket har laddats. De**LoaderService** samtal**LoaderService.buildCellsCache**, **LoaderService.buildColumnWidthCache** och**LoaderService.buildRowHeightCache**en efter en för att cachelagra innehållet i kalkylarket och hålla alla operationer snabba och smidiga.

**DOM-uppdateringar**

När kalkylbladet är klart på serversidan används JSF-komponenter för att generera ny HTML och skicka DOM-uppdateringar till användaren som renderas av webbläsaren.







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






### **Skapa ett nytt kalkylblad**
Så här skapar du ett nytt tomt kalkylblad:

1.  Byta till**Fliken Arkiv**.
1.  Klicka på**Ny** knapp.

Redaktören stänger det öppnade kalkylarket, om det finns, och öppnar ett nytt.

![todo:image_alt_text](lnydmmf.png)

**Hur det fungerar?**

**Instantiera ett nytt objekt**

 När**Ny** knappen klickas av användaren,**WorksheetView.loadBlank** , som så småningom ringer**LoaderService.fromBlank**. LoaderService skapar en ny instans av tomt kalkylblad.

**Cachning**

 Cachning sker direkt efter att kalkylarket har laddats. De**LoaderService** samtal**LoaderService.buildCellsCache**, **LoaderService.buildColumnWidthCache** och**LoaderService.buildRowHeightCache**en efter en för att cachelagra innehållet i kalkylarket och hålla alla operationer snabba och smidiga.

**DOM-uppdateringar**

När kalkylbladet är klart på serversidan används JSF-komponenter för att generera ny HTML och skicka DOM-uppdateringar till användaren som renderas av webbläsaren.







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






### **Exportera till olika format**
Efter att ha redigerat filer vill användaren spara ändringarna. Redaktören låter användaren exportera och ladda ner det modifierade kalkylarket till den lokala datorn. Så här exporterar du filen:

1.  Byta till**Fliken Arkiv** överst.
1.  Klick**Exportera** som knapp.
1. Välj önskat format från rullgardinsmenyn.

Den ändrade filen kommer att exporteras för nedladdning. Följande format stöds för export:

- Excel 2007-2013 XLSX
- Excel 1997-2003 XLS
- Excel XLSM
- Excel XLSB
- Excel XLTX
- Excel XLTM
- SpreadsheetML
- Portable Document Format (PDF)
- OpenDocument Spreadsheet (ODS)

**Hur det fungerar?**

 Det öppnade kalkylarket konverteras till användarspecificerat format med hjälp av**WorksheetView.getOutputFile**.







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






