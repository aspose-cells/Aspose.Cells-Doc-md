---
title: Редактор электронных таблиц — Работа с файлами
type: docs
weight: 10
url: /ru/java/spreadsheet-editor-working-with-files/
---
**Оглавление**

- [Поддерживаемые файлы](#SpreadsheetEditor-WorkingwithFiles-SupportedFiles)
- [Открыть локальные файлы](#SpreadsheetEditor-WorkingwithFiles-OpenLocalFiles) 
 - LoaderService.buildColumnWidthCache
 - LoaderService.buildRowHeightCache
- [Открыть из Dropbox](#SpreadsheetEditor-WorkingwithFiles-OpenfromDropbox)
- [Открыть с URL-адреса](#SpreadsheetEditor-WorkingwithFiles-OpenfromURL) 
 - LoaderService.fromUrl
 - LoaderService.buildCellsCache
 - LoaderService.buildColumnWidthCache
 - LoaderService.buildRowHeightCache
- [Создать новую таблицу](#SpreadsheetEditor-WorkingwithFiles-CreateaNewSpreadsheet) 
 - LoaderService.fromBlank
 - buildCellsCache
 - buildColumnWidthCache
 - buildRowHeightCache
- [Экспорт в различные форматы](#SpreadsheetEditor-WorkingwithFiles-ExporttoVariousFormats)
### **Поддерживаемые файлы**
Редактор электронных таблиц HTML5 может открывать файлы следующих форматов:

- Excel 1997-2003 XLS
- Эксель 2007-2013 XLSX
- XLSM
- XLSB
- XLTX
- Электронная таблицаML
- CVS
- OpenDocument
### **Открыть локальные файлы**
Чтобы загрузить файл с локального компьютера:

1.  Переключить на**Вкладка «Файл»** наверху.
1.  Нажмите**Открыть с компьютера** чтобы открыть диалоговое окно Обзор.
1. Перейдите к нужному местоположению файла.
1. Щелкните нужный файл, чтобы выбрать его.
1.  Нажмите**Открытым**.

Файл будет открыт в редакторе.

![дело:изображение_альтернативный_текст](bwyl3xi.png)

**Как это работает?**

**Файл загружен**

 Пользователь выбирает файл с локального компьютера, который загружается из веб-браузера на сервер и принимается[PrimeFaces файлЗагрузить](https://www.primefaces.org/showcase/ui/file/upload/basic.xhtml) составная часть.

{{< highlight "java" >}}

 <p:fileUpload fileUploadListener="#\{workbook.onFileUpload\}" update=":ribbon :intro :sheet" />

{{< /highlight >}}

**Управление книгой**

 Как только файл полностью загружен, для обработки ситуации вступает в действие метод WorkbookService.onFileUpload. WorkbookService получает события от веб-браузера и отслеживает состояние всей книги. WorkbookService.onFileUpload передает управление LoaderService для загрузки книги в память. Как***файл загружен*** компонент предоставляет загруженный файл как[Входной поток](https://docs.oracle.com/javase/8/docs/api/index.html?java/io/InputStream.html), LoaderService загружает его с помощью метода LoaderService.fromInputStream.







{{< highlight "java" >}}

 public void onFileUpload(FileUploadEvent e) {

    this.current = loader.fromInputStream(e.getFile().getInputstream(), e.getFile().getFileName());

}

{{< /highlight >}}







**Погрузка и разгрузка**

 Метод***LoaderService.fromInputStream*** читает***Входной поток*** предоставлено fileUpload***составная часть*** создать экземпляр***com.aspose.cells.Workbook***учебный класс. Этот экземпляр хранится в памяти, пока пользователь продолжает просматривать или редактировать электронную таблицу в веб-браузере. Когда пользователь выходит из редактора или закрывает браузер, неиспользуемые экземпляры автоматически выгружаются из памяти, чтобы поддерживать чистоту сервера.







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







**Кэширование**

Кэширование очень важно для редактора электронных таблиц HTML5. Это заставляет все работать гладко. CellsService хранит в кэше строки, столбцы, ячейки и свойства всех книг, загруженных редактором. Когда LoaderService полностью загружает электронную таблицу, он считывает ее сверху вниз и заполняет кеш, вызывая LoaderService.buildCellsCache, LoaderService.buildColumnWidthCache, LoaderService.buildRowHeightCache.







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






### **Открыть из Dropbox**
Чтобы открыть файлы из Dropbox:

1.  Переключить на**Вкладка «Файл»** наверху.
1.  Нажмите**Открыть из Dropbox** чтобы открыть средство выбора файлов Dropbox.
1. Если вы еще не вошли в систему, вам потребуется войти в свою учетную запись Dropbox.
1. Перейдите к нужному файлу и нажмите, чтобы выбрать его.
1.  Нажмите**Выбирать** внизу.

Выбранный вами файл будет открыт из Dropbox.

![дело:изображение_альтернативный_текст](1e2sfo0.png)

**Как это работает?**

**Открыть из Dropbox** кнопка использует**Выбор JavaScript в Dropbox API** чтобы открыть диалоговое окно Dropbox Chooser. Chooser предоставляет URL-адрес выбранного файла, который перехватывается функцией обратного вызова и отправляется обратно на сервер. Сервер создает экземпляр электронной таблицы из URL-адреса, инициализирует некоторые вспомогательные функции и отправляет обновления DOM обратно в браузер. Браузер отображает и обновляет HTML, и пользователь готов редактировать загруженный документ.
### **Открыть с URL-адреса**
 Файлы можно открывать напрямую с URL-адресов. Это позволяет пользователю редактировать любой общедоступный файл в Интернете. Чтобы открыть файл, добавьте**?url=местоположение** параметр со значением желаемого**расположение** при загрузке редактора. Например:

{{< highlight "java" >}}

 http://editor.aspose.com/?url=http://example.com/Sample.xlsx

{{< /highlight >}}

![дело:изображение_альтернативный_текст](exc9ckp.png)

**Как это работает?**

**Создание экземпляра во время запуска**

 Когда**Вид рабочего листа** backend bean создается JSF**PostConstruct** метод**в этом** вызывается, который загружает электронную таблицу, используя LoaderService.fromUrl.

**Кэширование**

 Кэширование происходит сразу после загрузки электронной таблицы.**LoaderService** звонки**LoaderService.buildCellsCache**, **LoaderService.buildColumnWidthCache** а также**LoaderService.buildRowHeightCache** один за другим, чтобы кэшировать содержимое электронной таблицы и обеспечить быстроту и плавность всех операций.

**Обновления DOM**

Когда электронная таблица готова на стороне сервера, компоненты JSF используются для создания нового HTML и отправки обновлений DOM пользователю, которые отображаются веб-браузером.







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






### **Создать новую таблицу**
Чтобы создать новую пустую таблицу:

1.  Переключить на**Вкладка «Файл»**.
1.  Нажмите на**Новый** кнопка.

Редактор закроет открытую таблицу, если она есть, и откроет новую.

![дело:изображение_альтернативный_текст](lnydmmf.png)

**Как это работает?**

**Создать новый объект**

 Когда**Новый** кнопка нажата пользователем,**WorksheetView.loadBlank** , который в итоге вызывает**LoaderService.fromBlank**. LoaderService создает новый экземпляр пустой электронной таблицы.

**Кэширование**

 Кэширование происходит сразу после загрузки электронной таблицы.**LoaderService** звонки**LoaderService.buildCellsCache**, **LoaderService.buildColumnWidthCache** а также**LoaderService.buildRowHeightCache** один за другим, чтобы кэшировать содержимое электронной таблицы и обеспечить быстроту и плавность всех операций.

**Обновления DOM**

Когда электронная таблица готова на стороне сервера, компоненты JSF используются для создания нового HTML и отправки обновлений DOM пользователю, которые отображаются веб-браузером.







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






### **Экспорт в различные форматы**
После редактирования файлов пользователь захочет сохранить изменения. Редактор позволяет пользователю экспортировать и загружать измененную электронную таблицу на локальный компьютер. Чтобы экспортировать файл:

1.  Переключить на**Вкладка «Файл»** наверху.
1.  Нажмите**Экспорт** как кнопка.
1. Выберите нужный формат из раскрывающегося списка.

Измененный файл будет экспортирован для скачивания. Для экспорта поддерживаются следующие форматы:

- Эксель 2007-2013 XLSX
- Excel 1997-2003 XLS
- Эксель XLSM
- Эксель XLSB
- Эксель XLTX
- Эксель XLTM
- Электронная таблицаML
- Переносимый формат документа (PDF)
- Электронная таблица OpenDocument (ODS)

**Как это работает?**

 Открытая электронная таблица преобразуется в указанный пользователем формат с помощью**WorksheetView.getOutputFile**.







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






