---
title: Tablo Düzenleyici  Dosyalarla Çalışma
type: docs
weight: 10
url: /tr/java/spreadsheet-editor-working-with-files/
---

**İçindekiler**

- [Desteklenen Dosyalar](#SpreadsheetEditor-WorkingwithFiles-SupportedFiles)
- [Yerel Dosyaları Aç](#SpreadsheetEditor-WorkingwithFiles-OpenLocalFiles) 
  - LoaderService.buildColumnWidthCache
  - LoaderService.buildRowHeightCache
- [Dropbox'tan Aç](#SpreadsheetEditor-WorkingwithFiles-OpenfromDropbox)
- [URL'den Aç](#SpreadsheetEditor-WorkingwithFiles-OpenfromURL) 
  - LoaderService.fromUrl
  - LoaderService.buildCellsCache
  - LoaderService.buildColumnWidthCache
  - LoaderService.buildRowHeightCache
- [Yeni Çalışsayısı Oluştur](#SpreadsheetEditor-WorkingwithFiles-CreateaNewSpreadsheet) 
  - LoaderService.fromBlank
  - buildCellsCache
  - buildColumnWidthCache
  - buildRowHeightCache
- [Çeşitli Biçimlere Dışa Aktar](#SpreadsheetEditor-WorkingwithFiles-ExporttoVariousFormats)
### **Desteklenen Dosyalar**
HTML5 Tablo Düzenleyici aşağıdaki formatlarda dosyaları açabilir:

- Excel 1997-2003 XLS
- Excel 2007-2013 XLSX
- XLSM
- XLSB
- XLTX
- SpreadsheetML
- CVS
- OpenDocument
### **Yerel Dosyaları Aç**
Yerel bilgisayardan dosya yüklemek için:

1. Üst kısımda **Dosya sekmesine** geçin.
1. Açma Dialogunu açmak için **Bilgisayardan Aç**'a tıklayın.
1. Dosyanın istenilen konumuna gidin.
1. Seçmek için istediğiniz dosyaya tıklayın.
1. **Aç**'a tıklayın.

Dosya düzenleyicide açılacaktır.

![todo:image_alt_text](bwyl3xi.png)

**Nasıl çalışır?**

**Dosya yükleme**

Kullanıcı, yerel bilgisayarından bir dosya seçer, bu dosya web tarayıcısı aracılığıyla sunucuya yüklenir ve [PrimeFaces fileUpload](https://www.primefaces.org/showcase/ui/file/upload/basic.xhtml) bileşeni tarafından alınır.

{{< highlight java >}}

 <p:fileUpload fileUploadListener="#\{workbook.onFileUpload\}" update=":ribbon :intro :sheet" />

{{< /highlight >}}

**Çalışma kitabı yönetimi**

Dosya tamamen yüklendiğinde, WorkbookService.onFileUpload yöntemi durumu ele almak için devreye girer. WorkbookService, web tarayıcısından olaylar alır ve tüm çalışma kitabının durumunu takip eder. WorkbookService.onFileUpload kontrolü LoaderService'e ileterek çalışma kitabını belleğe yüklemek için LoaderService'e kontolü ileter. ***fileUpload*** bileşeni yüklendiği dosyayı bir [InputStream](https://docs.oracle.com/javase/8/docs/api/index.html?java/io/InputStream.html) olarak sağladığından, LoaderService.fromInputStream yöntemi kullanarak yükler.







{{< highlight java >}}

 public void onFileUpload(FileUploadEvent e) {

    this.current = loader.fromInputStream(e.getFile().getInputstream(), e.getFile().getFileName());

}

{{< /highlight >}}







**Yükleme ve boşaltma**

LoaderService.fromInputStream yöntemi, dosyaYükleme bileşeni tarafından sağlanan ***InputStream***i okur ve ***com.aspose.cells.Workbook*** sınıfından bir örnek oluşturur. Bu örnek, kullanıcı çalışsayı veya web tarayıcısında tekrar tekrar görüntülerken bellekte tutulur. Kullanıcı düzenleyiciyi terk ettiğinde veya tarayıcıyı kapattığında kullanılmayan örnekler, sunucuyu temiz tutmak için otomatik olarak bellekten boşaltılır.







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







**Ön belleğe alma**

Önbellekleme, HTML5 Çalışsayı Düzenleyici için çok önemlidir. Her şeyin düzgün çalışmasını sağlar. CellsService, düzenleyici tarafından yüklenen tüm çalışsayıların satırlarını, sütunlarını, hücrelerini ve özelliklerini önbellekte tutar. LoaderService bir çalışma kitabını tamamen yüklediğinde, önbelleği yukarıdan aşağıya okur ve LoaderService.buildCellsCache, LoaderService.buildColumnWidthCache, LoaderService.buildRowHeightCache'ı çağırarak önbelleği doldurur.







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






### **Dropbox'tan Aç**
Dropbox'tan dosya açmak için:

1. Üst kısımda **Dosya sekmesine** geçin.
1. Dropbox'tan Aç'ı tıklayarak Dropbox dosya seçicisini açın.
1. Zaten oturum açmadıysanız, Dropbox hesabınıza oturum açmanızı gerektirecektir.
1. İstenilen dosyaya gidin ve seçmek için tıklayın.
1. Altta **Seç**'i tıklayın.

Seçtiğiniz dosya Dropbox'tan açılacak.

![todo:image_alt_text](1e2sfo0.png)

**Nasıl çalışır?**

**Dropbox'tan Aç** düğmesi, **Dropbox JavaScript Chooser API**'yi açmak için kullanır. Seçici, kullanıcının tarafından seçilen dosyanın URL'sini sağlar, bu URL,callback işlevi tarafından yakalanır ve sunucuya geri gönderilir. Sunucu, URL'den çalışsayısı örneği oluşturur, bazı ev bakım işlerini başlatır ve DOM güncellemelerini tarayıcıya geri gönderir. Tarayıcı, HTML'yi yeniden çizer ve kullanıcı düzenlenmiş belgeyi düzenlemeye hazır olur.
### **URL'den Aç**
Dosyalar doğrudan URL'lerden açılabilir. Bu, kullanıcının İnternet'te herkese açık bir dosyayı düzenlemesine olanak tanır. Dosyayı açarken düzenleyiciyi yüklerken, **?url=location** parametresini istediğiniz **location** değeri ile birlikte ekleyin. Örneğin:

{{< highlight java >}}

 http://editor.aspose.com/?url=http://example.com/Sample.xlsx

{{< /highlight >}}

![todo:image_alt_text](exc9ckp.png)

**Nasıl çalışır?**

**Başlatma sırasında örnekleme**

**WorksheetView** arka uç nesnesi JSF tarafından başlatıldığında **PostConstruct** yöntemi olan **init** çağrılır ve LoaderService.fromUrl kullanılarak çalışma kitabı yüklenir.

**Ön belleğe alma**

Ön belleğe alma, elektronik tablo yüklendikten hemen sonra gerçekleşir. **LoaderService**, elektronik tablonun içeriğini ön belleğe almak ve tüm işlemleri hızlı ve sorunsuz tutmak için sırayla **LoaderService.buildCellsCache**, **LoaderService.buildColumnWidthCache** ve **LoaderService.buildRowHeightCache** 'i çağırır.

**DOM güncellemeleri**

Elektronik tablo sunucu tarafında hazır olduğunda, JSF bileşenleri yeni HTML oluşturmak ve DOM güncellemelerini web tarayıcısı tarafından işlenen kullanıcıya göndermek için kullanılır.







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






### **Yeni Çalışsayısı Oluştur**
Yeni boş bir çalışsayısı oluşturmak için:

1. **Dosya sekmesine** geçin.
1. **Yeni** düğmesine tıklayın.

Editör, varsa açık olan elektronik tabloyu kapatır ve yeni bir tane açar.

![todo:image_alt_text](lnydmmf.png)

**Nasıl çalışır?**

**Yeni bir nesne oluşturun.**

Kullanıcı **Yeni** düğmesine tıkladığında, sonunda **LoaderService.fromBlank** 'ı çağıran **WorksheetView.loadBlank** çağrılır. LoaderService, boş bir elektronik tablonun yeni bir örneğini oluşturur.

**Ön belleğe alma**

Ön belleğe alma, elektronik tablo yüklendikten hemen sonra gerçekleşir. **LoaderService**, elektronik tablonun içeriğini ön belleğe almak ve tüm işlemleri hızlı ve sorunsuz tutmak için sırayla **LoaderService.buildCellsCache**, **LoaderService.buildColumnWidthCache** ve **LoaderService.buildRowHeightCache** 'i çağırır.

**DOM güncellemeleri**

Elektronik tablo sunucu tarafında hazır olduğunda, JSF bileşenleri yeni HTML oluşturmak ve DOM güncellemelerini web tarayıcısı tarafından işlenen kullanıcıya göndermek için kullanılır.







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






### **Çeşitli Biçimlere Dışa Aktar**
Dosyaları düzenledikten sonra, kullanıcı değişiklikleri kaydetmek isteyecektir. Editör, kullanıcının değiştirilmiş elektronik tabloyu yerel bilgisayarına dışa aktarmasına izin verir. Dosyayı dışa aktarmak için:

1. Üst kısımda **Dosya sekmesine** geçin.
1. **Dışa Aktar** olarak düğmesine tıklayın.
1. Açılır listeden istediğiniz biçimi seçin.

Değiştirilmiş dosya indirilmek üzere dışa aktarılacaktır. Aşağıdaki biçimler dışa aktarma için desteklenir:

- Excel 2007-2013 XLSX
- Excel 1997-2003 XLS
- Excel XLSM
- Excel XLSB
- Excel XLTX
- Excel XLTM
- SpreadsheetML
- Taşınabilir Belge Biçimi (PDF)
- OpenDocument Elektronik Tablo Biçimi (ODS)

**Nasıl çalışır?**

Açık olan elektronik tablo, **WorksheetView.getOutputFile** kullanılarak belirtilen formata dönüştürülür.







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






