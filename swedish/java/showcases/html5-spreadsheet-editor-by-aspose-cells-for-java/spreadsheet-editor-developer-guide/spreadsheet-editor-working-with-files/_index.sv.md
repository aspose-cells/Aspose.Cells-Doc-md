---
title: Kalkylbladsredigerare  Arbeta med filer
type: docs
weight: 10
url: /sv/java/spreadsheet-editor-working-with-files/
---

Innehållsförteckning

- [Understödda filer](#SpreadsheetEditor-WorkingwithFiles-SupportedFiles)
- [Öppna Lokala Filer](#SpreadsheetEditor-WorkingwithFiles-OpenLocalFiles) 
  - LoaderService.buildColumnWidthCache
  - LoaderService.buildRowHeightCache
- [Öppna från Dropbox](#SpreadsheetEditor-WorkingwithFiles-OpenfromDropbox)
- [Öppna från URL](#SpreadsheetEditor-WorkingwithFiles-OpenfromURL) 
  - LoaderService.fromUrl
  - LoaderService.buildCellsCache
  - LoaderService.buildColumnWidthCache
  - LoaderService.buildRowHeightCache
- [Skapa en ny kalkylblad](#SpreadsheetEditor-WorkingwithFiles-CreateaNewSpreadsheet) 
  - LoaderService.fromBlank
  - buildCellsCache
  - buildColumnWidthCache
  - buildRowHeightCache
- [Exportera till olika format](#SpreadsheetEditor-WorkingwithFiles-ExporttoVariousFormats)
### **Understödda filer**
HTML5 Kalkylbladsredigerare kan öppna filer i följande format:

- Excel 1997-2003 XLS
- Excel 2007-2013 XLSX
- XLSM
- XLSB
- XLTX
- SpreadsheetML
- CVS
- OpenDocument
### **Öppna Lokala Filer**
För att ladda upp en fil från lokal dator:

1. Byt till fliken **Arkiv** högst upp.
1. Klicka på **Öppna från datorn** för att öppna dialogrutan Bläddra.
1. Gå till den önskade filens plats.
1. Klicka på den önskade filen för att välja den.
1. Klicka på **Öppna**.

Filen öppnas i redigeraren.

![todo:image_alt_text](bwyl3xi.png)

**Hur fungerar det?**

**Filuppladdning**

Användaren väljer en fil från den lokala datorn som laddas upp från webbläsaren till servern och tas emot av [PrimeFaces fileUpload](https://www.primefaces.org/showcase/ui/file/upload/basic.xhtml) komponent.

{{< highlight java >}}

 <p:fileUpload fileUploadListener="#\{workbook.onFileUpload\}" update=":ribbon :intro :sheet" />

{{< /highlight >}}

**Hantera arbetsbok**

Så snart filen är helt uppladdad, träder WorkbookService.onFileUpload-metoden i kraft för att hantera situationen. WorkbookService tar emot händelser från webbläsaren och håller koll på hela arbetsbokens status. WorkbookService.onFileUpload skickar kontrollen vidare till LoaderService för att ladda arbetsboken i minnet. Eftersom ***fileUpload***-komponenten tillhandahåller den uppladdade filen som en [InputStream](https://docs.oracle.com/javase/8/docs/api/index.html?java/io/InputStream.html), laddar LoaderService in den med hjälp av LoaderService.fromInputStream-metoden.







{{< highlight java >}}

 public void onFileUpload(FileUploadEvent e) {

    this.current = loader.fromInputStream(e.getFile().getInputstream(), e.getFile().getFileName());

}

{{< /highlight >}}







**Laddning och lossning**

Metoden ***LoaderService.fromInputStream*** läser ***InputStream*** som tillhandahålls av fileUpload ***komponenten*** och skapar en instans av klassen ***com.aspose.cells.Workbook***. Denna instans hålls i minnet så länge användaren fortsätter att visa eller redigera kalkylarket i webbläsaren. När användaren lämnar redigeraren eller stänger webbläsaren läses de oanvända instanserna automatiskt ut från minnet för att hålla servern ren.







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







**Cachning**

Cachning är väldigt viktigt för HTML5 Kalkylbladsredigeraren. Det får allting att fungera smidigt. CellsService behåller cache-rader, kolumner, celler och egenskaper för alla arbetsböcker som laddats av redigeraren. När LoaderService laddar ett kalkylblad helt, läser den igenom det från början till slut och fyller upp cachen genom att anropa LoaderService.buildCellsCache, LoaderService.buildColumnWidthCache, LoaderService.buildRowHeightCache







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






### **Öppna från Dropbox**
För att öppna filer från Dropbox:

1. Byt till fliken **Arkiv** högst upp.
1. Klicka på **Öppna från Dropbox** för att öppna Dropbox-filväljaren.
1. Om du inte redan är inloggad kommer du att behöva logga in på ditt Dropbox-konto.
1. Navigera till önskad fil och klicka för att välja den.
1. Klicka på **Välj** längst ned.

Din valda fil öppnas från Dropbox.

![todo:image_alt_text](1e2sfo0.png)

**Hur fungerar det?**

Knappen **Öppna från Dropbox** använder **Dropbox JavaScript Chooser API** för att öppna Dropbox väljardialogen. Väljaren tillhandahåller URL till vald fil, som fångas av callback-funktionen och skickas tillbaka till servern. Servern skapar en instans av kalkylblad från URL, initierar vissa administrationssaker och skickar tillbaka DOM-uppdateringar till webbläsaren. Webbläsaren renderar och uppdaterar HTML och användaren är redo att redigera det inlästa dokumentet.
### **Öppna från URL**
Filer kan öppnas direkt från webbadresser. Detta gör att användaren kan redigera vilken offentligt tillgänglig fil som helst på internet. För att öppna filen lägger du till parameteren **?url=plats** med värdet av din önskade **plats** vid inladdningen av redigeraren. Till exempel:

{{< highlight java >}}

 http://editor.aspose.com/?url=http://example.com/Sample.xlsx

{{< /highlight >}}

![todo:image_alt_text](exc9ckp.png)

**Hur fungerar det?**

**Instantiate vid start**

När **WorksheetView** backend-beanen instantieras av JSF, anropas metoden **init** av **PostConstruct** vilket laddar kalkylarket med hjälp av LoaderService.fromUrl.

**Cachning**

Cachning sker direkt efter att kalkylbladet har laddats. **LoaderService** anropar **LoaderService.buildCellsCache**, **LoaderService.buildColumnWidthCache** och **LoaderService.buildRowHeightCache** var för sig för att cacha innehållet i kalkylbladet och hålla alla operationer snabba och smidiga.

**DOM-uppdateringar**

När kalkylbladet är redo på serverns sida används JSF-komponenter för att generera ny HTML och skicka DOM-uppdateringar till användaren, vilka renderas av webbläsaren.







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






### **Skapa en ny kalkylblad**
För att skapa ett nytt tomt kalkylblad:

1. Byt till fliken **Arkiv**.
1. Klicka på **Ny**-knappen.

Redigeraren stänger det öppnade kalkylbladet, om något, och öppnar ett nytt.

![todo:image_alt_text](lnydmmf.png)

**Hur fungerar det?**

**Instansiera ett nytt objekt**

När användaren klickar på **Ny**-knappen, **WorksheetView.loadBlank** aktiveras, vilket slutligen anropar **LoaderService.fromBlank**. LoaderService skapar en ny instans av tomt kalkylblad.

**Cachning**

Cachning sker direkt efter att kalkylbladet har laddats. **LoaderService** anropar **LoaderService.buildCellsCache**, **LoaderService.buildColumnWidthCache** och **LoaderService.buildRowHeightCache** var för sig för att cacha innehållet i kalkylbladet och hålla alla operationer snabba och smidiga.

**DOM-uppdateringar**

När kalkylbladet är redo på serverns sida används JSF-komponenter för att generera ny HTML och skicka DOM-uppdateringar till användaren, vilka renderas av webbläsaren.







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






### **Exportera till olika format**
Efter att ha redigerat filer vill användaren spara ändringar. Redigeraren tillåter användaren att exportera och ladda ner det modifierade kalkylbladet till den lokala datorn. För att exportera filen:

1. Byt till fliken **Arkiv** högst upp.
1. Klicka på **Exportera som**-knappen.
1. Välj önskat format från rullgardinsmenyn.

Den modifierade filen kommer att exporteras för nedladdning. Följande format stöds för export:

- Excel 2007-2013 XLSX
- Excel 1997-2003 XLS
- Excel XLSM
- Excel XLSB
- Excel XLTX
- Excel XLTM
- SpreadsheetML
- Bärbar dokumentformat (PDF)
- OpenDocument kalkylblad (ODS)

**Hur fungerar det?**

Det öppnade kalkylbladet konverteras till det användarspecificerade formatet med hjälp av **WorksheetView.getOutputFile**.







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






{{< app/cells/assistant language="java" >}}
