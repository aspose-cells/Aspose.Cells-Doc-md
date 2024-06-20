---
title: محرر الجداول  العمل مع الملفات
type: docs
weight: 10
url: /ar/java/spreadsheet-editor-working-with-files/
---

جدول المحتويات

- [الملفات المدعومة](#SpreadsheetEditor-WorkingwithFiles-SupportedFiles)
- [فتح ملفات محلية](#SpreadsheetEditor-WorkingwithFiles-OpenLocalFiles) 
  - LoaderService.buildColumnWidthCache
  - LoaderService.buildRowHeightCache
- [فتح من Dropbox](#SpreadsheetEditor-WorkingwithFiles-OpenfromDropbox)
- [فتح من عنوان URL](#SpreadsheetEditor-WorkingwithFiles-OpenfromURL) 
  - LoaderService.fromUrl
  - LoaderService.buildCellsCache
  - LoaderService.buildColumnWidthCache
  - LoaderService.buildRowHeightCache
- [إنشاء جدول بيانات جديد](#SpreadsheetEditor-WorkingwithFiles-CreateaNewSpreadsheet) 
  - LoaderService.fromBlank
  - buildCellsCache
  - buildColumnWidthCache
  - buildRowHeightCache
- [تصدير إلى تنسيقات مختلفة](#SpreadsheetEditor-WorkingwithFiles-ExporttoVariousFormats)
### **الملفات المدعومة**
يمكن لمحرر جدول البيانات HTML5 فتح الملفات بالتنسيقات التالية:

- Excel 1997-2003 XLS
- Excel 2007-2013 XLSX
- XLSM
- XLSB
- XLTX
- SpreadsheetML
- CVS
- OpenDocument
### **فتح ملفات محلية**
لتحميل ملف من جهاز الكمبيوتر المحلي:

1. التبديل إلى **علامة الملف** في الأعلى.
1. انقر فوق **فتح من الكمبيوتر** لفتح حوار التصفح.
1. انتقل إلى المكان المرغوب فيه للملف.
1. انقر على الملف المطلوب لتحديده.
1. انقر فوق **فتح**.

سيتم فتح الملف في المحرر.

![todo:image_alt_text](bwyl3xi.png)

**كيف يعمل هذا؟**

**تحميل الملف**

يختار المستخدم ملفًا من جهاز الكمبيوتر المحلي والذي يتم تحميله من متصفح الويب إلى الخادم ويتم استقباله بواسطة [عنصر PrimeFaces fileUpload](https://www.primefaces.org/showcase/ui/file/upload/basic.xhtml).

{{< highlight java >}}

 <p:fileUpload fileUploadListener="#\{workbook.onFileUpload\}" update=":ribbon :intro :sheet" />

{{< /highlight >}}

**إدارة الورقة العمل**

بمجرد إكتمال تحميل الملف تمامًا، تقوم طريقة WorkbookService.onFileUpload بالدخول في التأثير للتعامل مع الوضع. يستقبل WorkbookService الأحداث من متصفح الويب ويتتبع حالة الورقة العمل بأكملها. تقوم طريقة WorkbookService.onFileUpload بتمرير التحكم إلى LoaderService لتحميل الورقة العمل في الذاكرة. نظرًا لأن عنصر fileUpload يوفر الملف المحمل كـ [InputStream](https://docs.oracle.com/javase/8/docs/api/index.html?java/io/InputStream.html)، يقوم LoaderService بتحميله باستخدام طريقة LoaderService.fromInputStream.







{{< highlight java >}}

 public void onFileUpload(FileUploadEvent e) {

    this.current = loader.fromInputStream(e.getFile().getInputstream(), e.getFile().getFileName());

}

{{< /highlight >}}







**التحميل والتفريغ**

تقوم الطريقة ***LoaderService.fromInputStream*** بقراءة ***InputStream*** المقدم من عنصر fileUpload ***component*** وإنشاء مثال من فئة ***com.aspose.cells.Workbook***. يُحتفظ بهذا المثال في الذاكرة طالما يُحتفظ المستخدم بعرض أو تحرير جدول البيانات في متصفح الويب. عندما يغادر المستخدم المحرر أو يُغلق المتصفح، يتم تفريغ النسخ غير المستخدمة تلقائيًا من الذاكرة للحفاظ على نظافة الخادم.







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







**التخزين المؤقت**

التخزين المؤقت مهم جدًا لمحرر جدول البيانات HTML5. يجعل كل شيء يعمل بسلاسة. يحتفظ CellsService بتخزين صفوف، أعمدة، خلايا وخصائص جميع أوراق العمل المحملة عن طريق المحرر. عندما يحمل LoaderService جدول بيانات بالكامل، يقرأه من الأعلى إلى الأسفل ويملأ التخزين المؤقت عن طريق استدعاء طرق LoaderService.buildCellsCache, LoaderService.buildColumnWidthCache, LoaderService.buildRowHeightCache







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






### **فتح من Dropbox**
لفتح الملفات من Dropbox:

1. التبديل إلى **علامة الملف** في الأعلى.
1. انقر على **فتح من Dropbox** لفتح مُمْتَزِؚل Dropbox.
1. إذا لم تكن قد قمت بتسجيل الدخول بالفعل، سيتطلب منك تسجيل الدخول إلى حساب Dropbox الخاص بك.
1. قم بالانتقال إلى الملف المرغوب وانقر لتحديده.
1. انقر على **اختيار** في الأسفل.

سيتم فتح الملف المحدد من Dropbox.

![todo:image_alt_text](1e2sfo0.png)

**كيف يعمل هذا؟**

يستخدم زر **الفتح من Dropbox** واجهة برمجة التطبيقات الخاصة بـ **Dropbox Chooser** لفتح حوار اختيار Dropbox. يوفر الفاعل URL للملف المحدد، الذي يتم التقاطه بواسطة وظيفة الرد وإرسالها إلى الخادم. ينشئ الخادم مثيلًا من الجدول الخلايا من URL، ويبدأ في بعض الأمور الروتينية، ويعيد تحديث دوم إلى المتصفح. يقوم المتصفح بإظهار وتحديث HTML ويصبح المستخدم جاهزًا لتحرير المستند المحمل.
### **فتح من عنوان URL**
يمكن فتح الملفات مباشرة من عناوين الويب. يتيح هذا للمستخدم تحرير أي ملف متوفر للعامة على الإنترنت. لفتح الملف، أضف المعلم **?url=الموقع** مع قيمة **الموقع** المرغوبة الخاصة بك أثناء تحميل المحرر. على سبيل المثال:

{{< highlight java >}}

 http://editor.aspose.com/?url=http://example.com/Sample.xlsx

{{< /highlight >}}

![todo:image_alt_text](exc9ckp.png)

**كيف يعمل هذا؟**

**التثبيت خلال بدء التشغيل**

عندما يتم إنشاء كائن **WorksheetView** من خلال خرج جافاسكريبت للواجهة الأمامية، يتم استدعاء الطريقة **PostConstruct** **init** التي تحمل الجدول باستخدام LoaderService.fromUrl.

**التخزين المؤقت**

يحدث التخزين المؤقت مباشرة بعد تحميل جدول البيانات. يقوم **LoaderService** بدعوة **LoaderService.buildCellsCache**، **LoaderService.buildColumnWidthCache**، و **LoaderService.buildRowHeightCache** بشكل تتابع لتخزين محتوى جدول البيانات والاحتفاظ بكل العمليات سريعة وسلسة.

**تحديثات DOM**

بمجرد أن يكون جدول البيانات جاهزًا من الناحية الخادم، يتم استخدام مكونات JSF لإنشاء HTML جديد وإرسال تحديثات DOM إلى المستخدم التي يتم عرضها من قبل متصفح الويب.







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






### **إنشاء جدول بيانات جديد**
لإنشاء جدول بيانات جديد فارغ:

1. التبديل إلى **علامة الملف**.
1. انقر فوق زر **جديد**.

سيتم إغلاق المحرر لجدول البيانات المفتوح، إن وجد، وسيتم فتح واحد جديد.

![todo:image_alt_text](lnydmmf.png)

**كيف يعمل هذا؟**

**قم بإنشاء كائن جديد**

عندما ينقر المستخدم على زر **جديد**، سيتم استدعاء **WorksheetView.loadBlank**، الذي في النهاية يدعو **LoaderService.fromBlank**. يقوم LoaderService بإنشاء نسخة جديدة من جدول البيانات الفارغ.

**التخزين المؤقت**

يحدث التخزين المؤقت مباشرة بعد تحميل جدول البيانات. يقوم **LoaderService** بدعوة **LoaderService.buildCellsCache**، **LoaderService.buildColumnWidthCache**، و **LoaderService.buildRowHeightCache** بشكل تتابع لتخزين محتوى جدول البيانات والاحتفاظ بكل العمليات سريعة وسلسة.

**تحديثات DOM**

بمجرد أن يكون جدول البيانات جاهزًا من الناحية الخادم، يتم استخدام مكونات JSF لإنشاء HTML جديد وإرسال تحديثات DOM إلى المستخدم التي يتم عرضها من قبل متصفح الويب.







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






### **تصدير إلى تنسيقات مختلفة**
بعد تحرير الملفات، سيود المستخدم حفظ التغييرات. يسمح المحرر للمستخدم بتصدير وتنزيل جدول البيانات المعدل إلى جهاز الكمبيوتر المحلي. لتصدير الملف:

1. التبديل إلى **علامة الملف** في الأعلى.
1. انقر على زر **تصدير**.
1. اختر التنسيق المطلوب من القائمة المنسدلة.

سيتم تصدير الملف المعدل للتنزيل. يتم دعم الصيغ التالية للتصدير:

- Excel 2007-2013 XLSX
- Excel 1997-2003 XLS
- Excel XLSM
- Excel XLSB
- Excel XLTX
- Excel XLTM
- SpreadsheetML
- ملف تنسيق محمول (PDF)
- جدول بيانات مفتوح (ODS)

**كيف يعمل هذا؟**

يتم تحويل جدول البيانات المفتوح إلى الشكل المحدد من قبل المستخدم باستخدام **WorksheetView.getOutputFile**.







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






