---
title: Табличный редактор  Работа с файлами
type: docs
weight: 10
url: /ru/java/spreadsheet-editor-working-with-files/
---

**Содержание**

- [Поддерживаемые файлы](#SpreadsheetEditor-WorkingwithFiles-SupportedFiles)
- [Открыть локальные файлы](#SpreadsheetEditor-WorkingwithFiles-OpenLocalFiles) 
  - LoaderService.buildColumnWidthCache
  - LoaderService.buildRowHeightCache
- [Открыть из Dropbox](#SpreadsheetEditor-WorkingwithFiles-OpenfromDropbox)
- [Открыть из URL](#SpreadsheetEditor-WorkingwithFiles-OpenfromURL) 
  - LoaderService.fromUrl
  - LoaderService.buildCellsCache
  - LoaderService.buildColumnWidthCache
  - LoaderService.buildRowHeightCache
- [Создать новую электронную таблицу](#SpreadsheetEditor-WorkingwithFiles-CreateaNewSpreadsheet) 
  - LoaderService.fromBlank
  - buildCellsCache
  - buildColumnWidthCache
  - buildRowHeightCache
- [Экспорт в различные форматы](#SpreadsheetEditor-WorkingwithFiles-ExporttoVariousFormats)
### **Поддерживаемые файлы**
Редактор электронных таблиц HTML5 может открывать файлы следующих форматов:

- Excel 1997-2003 XLS
- Excel 2007-2013 XLSX
- XLSM
- XLSB
- XLTX
- SpreadsheetML
- CVS
- OpenDocument
### **Открыть локальные файлы**
Чтобы загрузить файл с локального компьютера:

1. Переключитесь на вкладку **Файл** вверху.
1. Нажмите **Открыть с компьютера**, чтобы открыть диалоговое окно Обзор.
1. Перейдите в нужную папку с файлом.
1. Щелкните нужный файл, чтобы выбрать его.
1. Нажмите **Открыть**.

Файл будет открыт в редакторе.

![todo:image_alt_text](bwyl3xi.png)

**Как это работает?**

**Загрузка файла**

Пользователь выбирает файл с локального компьютера, который загружается из веб-браузера на сервер и принимается [компонентом PrimeFaces fileUpload](https://www.primefaces.org/showcase/ui/file/upload/basic.xhtml).

{{< highlight java >}}

 <p:fileUpload fileUploadListener="#\{workbook.onFileUpload\}" update=":ribbon :intro :sheet" />

{{< /highlight >}}

**Управление электронной книгой**

Как только файл загружен полностью, метод WorkbookService.onFileUpload начинает обрабатывать ситуацию. WorkbookService получает события из веб-браузера и отслеживает состояние всей электронной книги. Метод WorkbookService.onFileUpload передает управление в LoaderService для загрузки электронной книги в память. Поскольку компонент ***fileUpload*** предоставляет загруженный файл в виде [InputStream](https://docs.oracle.com/javase/8/docs/api/index.html?java/io/InputStream.html), LoaderService загружает его, используя метод LoaderService.fromInputStream.







{{< highlight java >}}

 public void onFileUpload(FileUploadEvent e) {

    this.current = loader.fromInputStream(e.getFile().getInputstream(), e.getFile().getFileName());

}

{{< /highlight >}}







**Загрузка и выгрузка**

Метод ***LoaderService.fromInputStream*** считывает ***InputStream***, предоставленный компонентом fileUpload, создает экземпляр класса ***com.aspose.cells.Workbook***. Этот экземпляр хранится в памяти, пока пользователь просматривает или редактирует электронную таблицу в веб-браузере. Когда пользователь покидает редактор или закрывает браузер, неиспользуемые экземпляры автоматически выгружаются из памяти, чтобы поддерживать чистоту сервера.







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







**Кэширование**

Кэширование очень важно для HTML5 Редактора электронных таблиц. Это делает все работу гладкой. CellsService хранит кэш строк, столбцов, ячеек и свойств всех электронных таблиц, загруженных редактором. Когда LoaderService полностью загружает электронную таблицу, он читает ее сверху вниз и заполняет кэш, вызывая LoaderService.buildCellsCache, LoaderService.buildColumnWidthCache, LoaderService.buildRowHeightCache.







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






### **Открыть из Dropbox**
Чтобы открыть файлы из Dropbox:

1. Переключитесь на вкладку **Файл** вверху.
1. Щелкните **Открыть из Dropbox**, чтобы открыть выбор файла Dropbox.
1. Если вы еще не вошли в систему, вам потребуется войти в свою учетную запись Dropbox.
1. Перейдите к нужному файлу и щелкните, чтобы выбрать его.
1. Нажмите **Выбрать** внизу.

Выбранный файл будет открыт из Dropbox.

![todo:image_alt_text](1e2sfo0.png)

**Как это работает?**

Кнопка **Открыть из Dropbox** использует **Dropbox JavaScript Chooser API** для открытия диалогового окна Dropbox Chooser. Chooser предоставляет URL выбранного файла, который захватывается обратным вызовом и отправляется обратно на сервер. Сервер создает экземпляр электронной таблицы по URL, инициализирует некоторые вспомогательные функции и отправляет обновления DOM обратно в браузер. Браузер отображает и обновляет HTML, и пользователь готов редактировать загруженный документ.
### **Открыть из URL**
Файлы могут быть открыты непосредственно из URL-адресов. Это позволяет пользователю редактировать любой общедоступный файл в Интернете. Чтобы открыть файл, добавьте **?url=location** параметр со значением вашего желаемого **location** при загрузке редактора. Например:

{{< highlight java >}}

 http://editor.aspose.com/?url=http://example.com/Sample.xlsx

{{< /highlight >}}

![todo:image_alt_text](exc9ckp.png)

**Как это работает?**

**Инициализация во время запуска**

Когда бэкенд-бин **WorksheetView** создается с помощью JSF, вызывается метод **init** аннотации **PostConstruct**, который загружает электронную таблицу с помощью LoaderService.fromUrl.

**Кэширование**

Кэширование происходит сразу после загрузки таблицы. **LoaderService** вызывает **LoaderService.buildCellsCache**, **LoaderService.buildColumnWidthCache** и **LoaderService.buildRowHeightCache** поочередно для кэширования содержимого таблицы и обеспечения быстрой и плавной работы всех операций.

**Обновление DOM**

Когда таблица готова на сервере, компоненты JSF используются для генерации нового HTML, который отправляется пользователю в виде обновлений DOM, которые рендерятся веб-браузером.







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






### **Создать новую электронную таблицу**
Чтобы создать новую пустую электронную таблицу:

1. Переключитесь на вкладку **Файл**.
1. Нажмите кнопку **Новый**.

Редактор закроет открытую таблицу, если она есть, и откроет новую.

![todo:image_alt_text](lnydmmf.png)

**Как это работает?**

**Создание нового объекта**

Когда пользователь нажимает кнопку **Новый**, вызывается **WorksheetView.loadBlank**, который в конечном итоге вызывает **LoaderService.fromBlank**. LoaderService создает новый экземпляр пустой таблицы.

**Кэширование**

Кэширование происходит сразу после загрузки таблицы. **LoaderService** вызывает **LoaderService.buildCellsCache**, **LoaderService.buildColumnWidthCache** и **LoaderService.buildRowHeightCache** поочередно для кэширования содержимого таблицы и обеспечения быстрой и плавной работы всех операций.

**Обновление DOM**

Когда таблица готова на сервере, компоненты JSF используются для генерации нового HTML, который отправляется пользователю в виде обновлений DOM, которые рендерятся веб-браузером.







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






### **Экспорт в различные форматы**
После редактирования файлов пользователю захочется сохранить изменения. Редактор позволяет пользователю экспортировать и скачать измененную таблицу на локальный компьютер. Чтобы экспортировать файл:

1. Переключитесь на вкладку **Файл** вверху.
1. Нажмите кнопку **Экспорт как**.
1. Выберите нужный формат из выпадающего списка.

Измененный файл будет экспортирован для скачивания. Поддерживаются следующие форматы для экспорта:

- Excel 2007-2013 XLSX
- Excel 1997-2003 XLS
- Excel XLSM
- Excel XLSB
- Excel XLTX
- Excel XLTM
- SpreadsheetML
- Формат портативного документа (PDF)
- Документ таблицы OpenDocument (ODS)

**Как это работает?**

Открытая электронная таблица преобразуется в заданный пользователем формат с использованием **WorksheetView.getOutputFile**.







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






