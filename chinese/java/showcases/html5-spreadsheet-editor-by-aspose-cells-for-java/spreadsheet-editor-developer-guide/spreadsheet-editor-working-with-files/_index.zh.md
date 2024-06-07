---
title: 电子表格编辑器 - 使用文件
type: docs
weight: 10
url: /zh/java/spreadsheet-editor-working-with-files/
---

**目录**

- [支持的文件](#SpreadsheetEditor-WorkingwithFiles-SupportedFiles)
- [打开本地文件](#SpreadsheetEditor-WorkingwithFiles-OpenLocalFiles) 
  - LoaderService.buildColumnWidthCache
  - LoaderService.buildRowHeightCache
- [从Dropbox中打开](#SpreadsheetEditor-WorkingwithFiles-OpenfromDropbox)
- [从URL打开](#SpreadsheetEditor-WorkingwithFiles-OpenfromURL) 
  - LoaderService.fromUrl
  - LoaderService.buildCellsCache
  - LoaderService.buildColumnWidthCache
  - LoaderService.buildRowHeightCache
- [创建新电子表格](#SpreadsheetEditor-WorkingwithFiles-CreateaNewSpreadsheet) 
  - LoaderService.fromBlank
  - buildCellsCache
  - 构建列宽缓存
  - 构建行高缓存
- [导出为各种格式](#SpreadsheetEditor-WorkingwithFiles-ExporttoVariousFormats)
### **支持的文件**
HTML5 电子表格编辑器可以打开以下格式的文件:

- Excel 1997-2003 XLS
- Excel 2007-2013 XLSX
- XLSM
- XLSB
- XLTX
- SpreadsheetML
- CVS
- OpenDocument
### **打开本地文件**
要从本地计算机上传文件:

1. 在顶部切换到 **文件标签**。
1. 点击**从计算机打开**打开浏览对话框。
1. 进入所需文件的位置。
1. 点击所需文件以选择。
1. 点击**打开**。

文件将在编辑器中打开。

![todo:image_alt_text](bwyl3xi.png)

**它是如何工作的？**

**文件上传**

用户从本地计算机选择上传到服务器并由[PrimeFaces fileUpload](https://www.primefaces.org/showcase/ui/file/upload/basic.xhtml)组件接收的文件。

{{< highlight java >}}

 <p:fileUpload fileUploadListener="#\{workbook.onFileUpload\}" update=":ribbon :intro :sheet" />

{{< /highlight >}}

**管理工作簿**

一旦文件完全上传，WorkbookService.onFileUpload方法开始处理情况。WorkbookService从Web浏览器接收事件并跟踪整个工作簿的状态。 WorkbookService.onFileUpload将控制权转交给LoaderService，将工作簿加载到内存中。 由于***fileUpload***组件提供上传的文件，可以作为[InputStream](https://docs.oracle.com/javase/8/docs/api/index.html?java/io/InputStream.html) LoaderService使用LoaderService.fromInputStream方法加载。







{{< highlight java >}}

 public void onFileUpload(FileUploadEvent e) {

    this.current = loader.fromInputStream(e.getFile().getInputstream(), e.getFile().getFileName());

}

{{< /highlight >}}







**加载和卸载**

方法***LoaderService.fromInputStream***读取fileUpload***组件提供的***InputStream***创建***com.aspose.cells.Workbook***类的实例。 只要用户在Web浏览器中查看或编辑电子表格，这个实例就会保留在内存中。 当用户离开编辑器或关闭浏览器时，未使用的实例将自动从内存中卸载，以保持服务器的干净。







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







**缓存**

缓存对于HTML5电子表格编辑器非常重要。 它使一切都能够顺利进行。 CellsService保留由编辑器加载的所有工作簿的行、列、单元格和属性的缓存。 当LoaderService完全加载电子表格时，它从上到下读取，并通过调用LoaderService.buildCellsCache、LoaderService.buildColumnWidthCache、LoaderService.buildRowHeightCache填充缓存。







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






### **从Dropbox中打开**
要从Dropbox中打开文件:

1. 在顶部切换到 **文件标签**。
1. 单击**从Dropbox打开**以打开Dropbox文件选择器。
1. 如果还未登录，将需要您登录到您的Dropbox帐户。
1. 转到所需的文件并单击以选择。
1. 单击底部的**选择**。

您选择的文件将从Dropbox中打开。

![todo:image_alt_text](1e2sfo0.png)

**它是如何工作的？**

**从Dropbox打开**按钮使用**Dropbox JavaScript Chooser API**来打开Dropbox选择器对话框。 选择器会提供所选文件的URL，该URL由回调函数捕获并发送回服务器。 服务器从URL创建一个电子表格实例，初始化一些管理事项，并将DOM更新发送回到浏览器。 浏览器渲染并刷新HTML，用户可以编辑已加载的文档。
### **从URL打开**
可以直接从URL打开文件。这允许用户编辑互联网上任何公开可用的文件。要打开文件，加载编辑器时附加**?url=location**参数，并填入所需**location**的值。例如:

{{< highlight java >}}

 http://editor.aspose.com/?url=http://example.com/Sample.xlsx

{{< /highlight >}}

![todo:image_alt_text](exc9ckp.png)

**它是如何工作的？**

**启动时实例化**

当通过JSF实例化**WorksheetView**后端bean时，将调用**PostConstruct**方法**init**，该方法使用LoaderService.fromUrl加载电子表格。

**缓存**

缓存在电子表格加载后立即发生。 ** LoaderService **依次调用** LoaderService.buildCellsCache **，** LoaderService.buildColumnWidthCache **和** LoaderService.buildRowHeightCache **来缓存电子表格的内容，使所有操作都快速且平滑。

**DOM更新**

当服务器端准备好电子表格时，使用JSF组件生成新的HTML并将DOM更新发送给用户，由Web浏览器呈现。







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






### **创建新电子表格**
创建一个新的空白电子表格：

1. 切换到 **文件标签**。
1. 单击 **新建** 按钮。

如果有打开的电子表格，则编辑器将关闭该文件并打开一个新文件。

![todo:image_alt_text](lnydmmf.png)

**它是如何工作的？**

**实例化一个新对象**

当用户单击**新建**按钮时，会调用** WorksheetView.loadBlank **，最终调用** LoaderService.fromBlank **。 LoaderService创建一个新的空白电子表格实例。

**缓存**

缓存在电子表格加载后立即发生。 ** LoaderService **依次调用** LoaderService.buildCellsCache **，** LoaderService.buildColumnWidthCache **和** LoaderService.buildRowHeightCache **来缓存电子表格的内容，使所有操作都快速且平滑。

**DOM更新**

当服务器端准备好电子表格时，使用JSF组件生成新的HTML并将DOM更新发送给用户，由Web浏览器呈现。







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






### **导出为各种格式**
编辑文件后，用户将希望保存更改。编辑器允许用户将修改后的电子表格导出并下载到本地计算机。 要导出文件：

1. 在顶部切换到 **文件标签**。
1. 单击 **导出** 按钮。
1. 从下拉菜单中选择所需的格式。

修改后的文件将被导出以供下载。 支持以下格式进行导出：

- Excel 2007-2013 XLSX
- Excel 1997-2003 XLS
- Excel XLSM
- Excel XLSB
- Excel XLTX
- Excel XLTM
- SpreadsheetML
- 便携式文档格式 (PDF)
- OpenDocument电子制表软件(ODS)

**它是如何工作的？**

打开的电子表格被转换为用户指定的格式，使用**WorksheetView.getOutputFile**。







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






