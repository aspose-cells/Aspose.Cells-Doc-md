---
title: Hesap Tablosu Düzenleyicisi - Dosyalarla Çalışma
type: docs
weight: 10
url: /tr/java/spreadsheet-editor-working-with-files/
---
**İçindekiler**

- [Desteklenen Dosyalar](#SpreadsheetEditor-WorkingwithFiles-SupportedFiles)
- [Yerel Dosyaları Aç](#SpreadsheetEditor-WorkingwithFiles-OpenLocalFiles) 
 - LoaderService.buildColumnWidthCache
 - LoaderService.buildRowHeightCache
- [Dropbox'tan aç](#SpreadsheetEditor-WorkingwithFiles-OpenfromDropbox)
- [URL'den aç](#SpreadsheetEditor-WorkingwithFiles-OpenfromURL) 
 - LoaderService.fromUrl
 - LoaderService.buildCellsCache
 - LoaderService.buildColumnWidthCache
 - LoaderService.buildRowHeightCache
- [Yeni Bir Elektronik Tablo Oluşturun](#SpreadsheetEditor-WorkingwithFiles-CreateaNewSpreadsheet) 
 - LoaderService.fromBlank
 - buildCellsCache
 - buildColumnWidthCache
 - buildRowHeightCache
- [Çeşitli Biçimlerde Dışa Aktarma](#SpreadsheetEditor-WorkingwithFiles-ExporttoVariousFormats)
### **Desteklenen Dosyalar**
HTML5 Elektronik Tablo Düzenleyicisi, aşağıdaki biçimlerdeki dosyaları açabilir:

- Excel 1997-2003 XLS
- Excel 2007-2013 XLSX
- XLSM
- XLSB
- XLTX
- E-tabloML
- özgeçmiş
- Açık Belge
### **Yerel Dosyaları Aç**
Yerel bilgisayardan dosya yüklemek için:

1.  Çevirmek**Dosya sekmesi** üstte
1.  Tıklamak**Bilgisayardan aç** Gözat iletişim kutusunu açmak için
1. İstediğiniz dosya konumuna gidin.
1. Seçmek için istediğiniz dosyayı tıklayın.
1.  Tıklamak**Açık**.

Dosya düzenleyicide açılacaktır.

![yapılacaklar:resim_alternatif_Metin](bwyl3xi.png)

**Nasıl çalışır?**

**Dosya yükleme**

 Kullanıcı, web tarayıcısından sunucuya yüklenen ve tarafından alınan yerel bilgisayardan bir dosya seçer.[PrimeFaces dosyasıYükle](https://www.primefaces.org/showcase/ui/file/upload/basic.xhtml) bileşen.

{{< highlight "java" >}}

 <p:fileUpload fileUploadListener="#\{workbook.onFileUpload\}" update=":ribbon :intro :sheet" />

{{< /highlight >}}

**Çalışma kitabını yönetme**

 Dosya tamamen yüklenir yüklenmez, durumu halletmek için WorkbookService.onFileUpload yöntemi devreye girer. WorkbookService, web tarayıcısından olayları alır ve tüm çalışma kitabının durumunu takip eder. WorkbookService.onFileUpload, çalışma kitabını belleğe yüklemek için denetimi LoaderService'e aktarır. olarak***dosya yükleme*** bileşeni, yüklenen dosyayı bir[Giriş Akışı](https://docs.oracle.com/javase/8/docs/api/index.html?java/io/InputStream.html), LoaderService bunu LoaderService.fromInputStream yöntemini kullanarak yükler.







{{< highlight "java" >}}

 public void onFileUpload(FileUploadEvent e) {

    this.current = loader.fromInputStream(e.getFile().getInputstream(), e.getFile().getFileName());

}

{{< /highlight >}}







**Yükleme ve boşaltma**

 yöntem***LoaderService.fromInputStream*** okur***Giriş Akışı*** fileUpload tarafından sağlanan***bileşen*** örneğini oluştur***com.aspose.cells.Workbook***sınıf. Bu örnek, kullanıcı e-tabloyu web tarayıcısında görüntülemeye veya düzenlemeye devam ettiği sürece bellekte tutulur. Kullanıcı editörden ayrıldığında veya tarayıcıyı kapattığında, sunucuyu temiz tutmak için kullanılmayan örnekler otomatik olarak bellekten kaldırılır.







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







**Önbelleğe almak**

Önbelleğe alma, HTML5 Elektronik Tablo Düzenleyicisi için çok önemlidir. Her şeyin sorunsuz çalışmasını sağlar. CellsService, düzenleyici tarafından yüklenen tüm çalışma kitaplarının önbellek satırlarını, sütunlarını, hücrelerini ve özelliklerini tutar. LoaderService bir elektronik tabloyu tamamen yüklediğinde, onu yukarıdan aşağıya okur ve LoaderService.buildCellsCache, LoaderService.buildColumnWidthCache, LoaderService.buildRowHeightCache'yi çağırarak önbelleği doldurur.







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






### **Dropbox'tan aç**
Dropbox'tan dosya açmak için:

1.  Çevirmek**Dosya sekmesi** üstte
1.  Tıklamak**Dropbox'tan aç** Dropbox dosya seçiciyi açmak için.
1. Henüz oturum açmadıysanız, Dropbox hesabınızda oturum açmanız gerekir.
1. İstediğiniz dosyaya gidin ve seçmek için tıklayın.
1.  Tıklamak**Seçmek** altta.

Seçtiğiniz dosya Dropbox'tan açılacaktır.

![yapılacaklar:resim_alternatif_Metin](1e2sfo0.png)

**Nasıl çalışır?**

 bu**Dropbox'tan aç** düğme kullanır**Dropbox JavaScript Seçici API** Dropbox Seçici iletişim kutusunu açmak için. Seçici, geri arama işlevi tarafından yakalanan ve sunucuya geri gönderilen seçili dosyanın URL'sini sağlar. Sunucu, URL'den bir elektronik tablo örneği oluşturur, bazı temizlik işlerini başlatır ve DOM güncellemelerini tarayıcıya geri gönderir. Tarayıcı HTML'yi işler ve yeniler ve kullanıcı yüklenen belgeyi düzenlemeye hazırdır.
### **URL'den aç**
 Dosyalar doğrudan URL'lerden açılabilir. Bu, kullanıcının İnternet üzerindeki herkese açık herhangi bir dosyayı düzenlemesine izin verir. Dosya ekini açmak için**?url=konum** İstediğiniz değere sahip parametre**yer** editör yüklenirken. Örneğin:

{{< highlight "java" >}}

 http://editor.aspose.com/?url=http://example.com/Sample.xlsx

{{< /highlight >}}

![yapılacaklar:resim_alternatif_Metin](exc9ckp.png)

**Nasıl çalışır?**

**Başlatma sırasında örneklendir**

 Ne zaman**Çalışma Sayfası Görünümü** arka uç fasulyesi, JSF tarafından başlatılır**Yapı Sonrası** yöntem**içinde** LoaderService.fromUrl kullanarak elektronik tabloyu yükleyen çağrılır.

**Önbelleğe almak**

 Önbelleğe alma, elektronik tablo yüklendikten hemen sonra gerçekleşir. bu**Yükleyici Hizmeti** aramalar**LoaderService.buildCellsCache**, **LoaderService.buildColumnWidthCache** ve**LoaderService.buildRowHeightCache** elektronik tablonun içeriğini önbelleğe almak ve tüm işlemleri hızlı ve sorunsuz tutmak için tek tek.

**DOM güncellemeleri**

Elektronik tablo sunucu tarafında hazır olduğunda, yeni HTML oluşturmak ve web tarayıcısı tarafından işlenen DOM güncellemelerini kullanıcıya göndermek için JSF bileşenleri kullanılır.







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






### **Yeni Bir Elektronik Tablo Oluşturun**
Yeni bir boş e-tablo oluşturmak için:

1.  Çevirmek**Dosya sekmesi**.
1.  Tıkla**Yeni** buton.

Düzenleyici, varsa açılan elektronik tabloyu kapatır ve yeni bir hesap tablosu açar.

![yapılacaklar:resim_alternatif_Metin](lnydmmf.png)

**Nasıl çalışır?**

**Yeni bir nesne örneği oluşturun**

 Ne zaman**Yeni** butonu kullanıcı tarafından tıklandığında,**WorksheetView.loadBlank** , sonunda çağıran**LoaderService.fromBlank**. LoaderService, yeni bir boş elektronik tablo örneği oluşturur.

**Önbelleğe almak**

 Önbelleğe alma, elektronik tablo yüklendikten hemen sonra gerçekleşir. bu**Yükleyici Hizmeti** aramalar**LoaderService.buildCellsCache**, **LoaderService.buildColumnWidthCache** ve**LoaderService.buildRowHeightCache** elektronik tablonun içeriğini önbelleğe almak ve tüm işlemleri hızlı ve sorunsuz tutmak için tek tek.

**DOM güncellemeleri**

Elektronik tablo sunucu tarafında hazır olduğunda, yeni HTML oluşturmak ve web tarayıcısı tarafından işlenen DOM güncellemelerini kullanıcıya göndermek için JSF bileşenleri kullanılır.







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






### **Çeşitli Biçimlerde Dışa Aktarma**
Dosyaları düzenledikten sonra, kullanıcı değişiklikleri kaydetmek isteyecektir. Düzenleyici, kullanıcının değiştirilen elektronik tabloyu yerel bilgisayara aktarmasına ve indirmesine izin verir. Dosyayı dışa aktarmak için:

1.  Çevirmek**Dosya sekmesi** üstte
1.  Tıklamak**İhracat** düğme olarak.
1. Açılır listeden istediğiniz formatı seçin.

Değiştirilen dosya indirilmek üzere dışa aktarılacaktır. Aşağıdaki biçimler dışa aktarma için desteklenir:

- Excel 2007-2013 XLSX
- Excel 1997-2003 XLS
- Excel XLSM
- Excel XLSB
- Excel XLTX
- Excel XL™
- E-tabloML
- Taşınabilir Belge Formatı (PDF)
- OpenDocument Elektronik Tablosu (ODS)

**Nasıl çalışır?**

 Açılan elektronik tablo, kullanılarak kullanıcı tarafından belirlenen biçime dönüştürülür.**WorksheetView.getOutputFile**.







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






