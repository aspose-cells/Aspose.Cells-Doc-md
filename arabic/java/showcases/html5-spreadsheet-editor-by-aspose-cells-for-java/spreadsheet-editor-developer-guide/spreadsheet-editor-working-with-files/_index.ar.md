---
title: محرر جداول البيانات - العمل مع الملفات
type: docs
weight: 10
url: /ar/java/spreadsheet-editor-working-with-files/
---
**جدول المحتويات**

- [الملفات المدعومة](#SpreadsheetEditor-WorkingwithFiles-SupportedFiles)
- [افتح الملفات المحلية](#SpreadsheetEditor-WorkingwithFiles-OpenLocalFiles) 
 - LoaderService.buildColumnWidthCache
 - LoaderService.buildRowHeightCache
- [افتح من Dropbox](#SpreadsheetEditor-WorkingwithFiles-OpenfromDropbox)
- [افتح من URL](#SpreadsheetEditor-WorkingwithFiles-OpenfromURL) 
 - LoaderService.fromUrl
 - LoaderService.buildCellsCache
 - LoaderService.buildColumnWidthCache
 - LoaderService.buildRowHeightCache
- [قم بإنشاء جدول بيانات جديد](#SpreadsheetEditor-WorkingwithFiles-CreateaNewSpreadsheet) 
 - LoaderService.fromBlank
 - buildCellsCache
 - buildColumnWidthCache
 - buildRowHeightCache
- [تصدير إلى تنسيقات مختلفة](#SpreadsheetEditor-WorkingwithFiles-ExporttoVariousFormats)
### **الملفات المدعومة**
يمكن لـ HTML5 Spreadsheet Editor فتح الملفات بالتنسيقات التالية:

- Excel 1997-2003 XLS
- برنامج Excel 2007-2013 XLSX
- XLSM
- XLSB
- XLTX
- SpreadsheetML
- CVS
- OpenDocument
### **افتح الملفات المحلية**
لتحميل ملف من جهاز كمبيوتر محلي:

1.  التبديل إلى**تبويب الملف** على القمة.
1.  انقر**افتح من الكمبيوتر** لفتح مربع الحوار "استعراض".
1. انتقل إلى موقع الملف المطلوب.
1. انقر فوق الملف المطلوب لتحديده.
1.  انقر**فتح**.

سيتم فتح الملف في المحرر.

![ما يجب القيام به: image_بديل_نص](bwyl3xi.png)

**كيف تعمل؟**

**تحميل الملف**

 يقوم المستخدم بتحديد ملف من جهاز كمبيوتر محلي يتم تحميله من متصفح الويب إلى الخادم واستلامه بواسطة[ملف PrimeFaces](https://www.primefaces.org/showcase/ui/file/upload/basic.xhtml) مكون.

{{< highlight "java" >}}

 <p:fileUpload fileUploadListener="#\{workbook.onFileUpload\}" update=":ribbon :intro :sheet" />

{{< /highlight >}}

**إدارة المصنف**

 بمجرد تحميل الملف بالكامل ، تدخل طريقة WorkbookService.onFileUpload للتعامل مع الموقف. تتلقى WorkbookService الأحداث من مستعرض الويب وتتابع حالة المصنف بالكامل. WorkbookService.onFileUpload تمرير عنصر التحكم إلى LoaderService لتحميل المصنف في الذاكرة. مثل***تحميل الملف*** يوفر المكون الملف الذي تم تحميله كملف[تيار الإدخال](https://docs.oracle.com/javase/8/docs/api/index.html?java/io/InputStream.html)، تقوم LoaderService بتحميله باستخدام طريقة LoaderService.fromInputStream.







{{< highlight "java" >}}

 public void onFileUpload(FileUploadEvent e) {

    this.current = loader.fromInputStream(e.getFile().getInputstream(), e.getFile().getFileName());

}

{{< /highlight >}}







**التحميل والتفريغ**

 طريقة***LoaderService.fromInputStream*** يقرأ***تيار الإدخال*** مقدمة من fileUpload***مكون*** إنشاء مثيل***com.aspose.cells.Workbook*** صف دراسي. يتم الاحتفاظ بهذا المثيل في الذاكرة طالما استمر المستخدم في عرض جدول البيانات أو تحريره في متصفح الويب. عندما يترك المستخدم المحرر أو يغلق المتصفح ، يتم إلغاء تحميل المثيلات غير المستخدمة تلقائيًا من الذاكرة للحفاظ على الخادم نظيفًا.







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







**التخزين المؤقت**

التخزين المؤقت مهم جدًا لمحرر جداول بيانات HTML5. يجعل كل شيء يعمل بسلاسة. تحتفظ CellsService بصفوف وأعمدة وخلايا وخصائص ذاكرة التخزين المؤقت لجميع المصنفات التي تم تحميلها بواسطة المحرر. عندما يقوم LoaderService بتحميل جدول بيانات بالكامل ، فإنه يقرأه من أعلى إلى أسفل ويملأ ذاكرة التخزين المؤقت عن طريق استدعاء LoaderService.buildCellsCache، LoaderService.buildColumnWidthCache، LoaderService.buildRowHeightCache







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






### **افتح من Dropbox**
لفتح الملفات من Dropbox:

1.  التبديل إلى**تبويب الملف** على القمة.
1.  انقر**افتح من Dropbox** لفتح منتقي ملف Dropbox.
1. إذا لم تكن قد سجلت الدخول بالفعل ، فسيتطلب منك تسجيل الدخول إلى حساب Dropbox الخاص بك.
1. انتقل إلى الملف المطلوب وانقر لتحديده.
1.  انقر**يختار** في الأسفل.

سيتم فتح الملف الذي اخترته من Dropbox.

![ما يجب القيام به: image_بديل_نص](1e2sfo0.png)

**كيف تعمل؟**

 ال**افتح من Dropbox** يستخدم زر**منتقي جافا سكريبت دروب بوكس API**لفتح مربع حوار منتقي Dropbox. يوفر المنتقي عنوان URL للملف المحدد ، والذي يتم التقاطه بواسطة وظيفة رد الاتصال وإرساله مرة أخرى إلى الخادم. يقوم الخادم بإنشاء مثيل لجدول بيانات من عنوان URL ، وتهيئة بعض عناصر التدبير المنزلي ، وإرسال تحديثات DOM مرة أخرى إلى المتصفح. يقوم المتصفح بعرض وتحديث HTML ويكون المستخدم جاهزًا لتحرير المستند الذي تم تحميله.
### **افتح من URL**
 يمكن فتح الملفات مباشرة من عناوين المواقع. هذا يسمح للمستخدم بتحرير أي ملف متاح للجمهور على الإنترنت. لفتح ملف الإلحاق**؟ url = الموقع** المعلمة مع القيمة التي تريدها**موقعك** أثناء تحميل المحرر. فمثلا:

{{< highlight "java" >}}

 http://editor.aspose.com/?url=http://example.com/Sample.xlsx

{{< /highlight >}}

![ما يجب القيام به: image_بديل_نص](exc9ckp.png)

**كيف تعمل؟**

**إنشاء مثيل أثناء بدء التشغيل**

 متي**WorksheetView** يتم إنشاء مثيل فول الواجهة الخلفية بواسطة JSF the**PostConstruct** طريقة**فيه** يسمى الذي يقوم بتحميل جدول البيانات باستخدام LoaderService.fromUrl.

**التخزين المؤقت**

 يحدث التخزين المؤقت مباشرة بعد تحميل جدول البيانات. ال**خدمة لودر** المكالمات**LoaderService.buildCellsCache**, **LoaderService.buildColumnWidthCache** و**LoaderService.buildRowHeightCache**واحدًا تلو الآخر لتخزين محتوى جدول البيانات مؤقتًا والحفاظ على سرعة وسلاسة جميع العمليات.

**تحديثات DOM**

عندما يكون جدول البيانات جاهزًا على جانب الخادم ، يتم استخدام مكونات JSF لإنشاء HTML جديد وإرسال تحديثات DOM إلى المستخدم والتي يتم تقديمها بواسطة متصفح الويب.







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






### **قم بإنشاء جدول بيانات جديد**
لإنشاء جدول بيانات فارغ جديد:

1.  التبديل إلى**تبويب الملف**.
1.  انقر على**جديد** زر.

سيغلق المحرر جدول البيانات المفتوح ، إن وجد ، وسيفتح جدولًا جديدًا.

![ما يجب القيام به: image_بديل_نص](lnydmmf.png)

**كيف تعمل؟**

**إنشاء كائن جديد**

 عندما**جديد** تم النقر فوق الزر من قبل المستخدم ،**WorksheetView.loadBlank** ، والذي يستدعي في النهاية**LoaderService.fromBlank**. يقوم LoaderService بإنشاء مثيل جديد لجدول بيانات فارغ.

**التخزين المؤقت**

 يحدث التخزين المؤقت مباشرة بعد تحميل جدول البيانات. ال**خدمة لودر** المكالمات**LoaderService.buildCellsCache**, **LoaderService.buildColumnWidthCache** و**LoaderService.buildRowHeightCache**واحدًا تلو الآخر لتخزين محتوى جدول البيانات مؤقتًا والحفاظ على سرعة وسلاسة جميع العمليات.

**تحديثات DOM**

عندما يكون جدول البيانات جاهزًا على جانب الخادم ، يتم استخدام مكونات JSF لإنشاء HTML جديد وإرسال تحديثات DOM إلى المستخدم والتي يتم تقديمها بواسطة متصفح الويب.







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






### **تصدير إلى تنسيقات مختلفة**
بعد تحرير الملفات ، سيرغب المستخدم في حفظ التغييرات. يسمح المحرر للمستخدم بتصدير وتنزيل جدول البيانات المعدل إلى الكمبيوتر المحلي. لتصدير الملف:

1.  التبديل إلى**تبويب الملف** على القمة.
1.  انقر**يصدّر** كزر.
1. اختر التنسيق الذي تريده من القائمة المنسدلة.

سيتم تصدير الملف المعدل للتحميل. التنسيقات التالية مدعومة للتصدير:

- برنامج Excel 2007-2013 XLSX
- Excel 1997-2003 XLS
- اكسل XLSM
- اكسل XLSB
- اكسل XLTX
- برنامج Excel XLTM
- SpreadsheetML
- تنسيق المستندات المحمولة (PDF)
- جدول بيانات OpenDocument (ODS)

**كيف تعمل؟**

 يتم تحويل جدول البيانات المفتوح إلى تنسيق محدد بواسطة المستخدم**WorksheetView.getOutputFile**.







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






