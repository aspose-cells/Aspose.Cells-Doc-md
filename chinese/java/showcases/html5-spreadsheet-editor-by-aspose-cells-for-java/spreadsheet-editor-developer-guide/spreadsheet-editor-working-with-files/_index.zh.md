---
title: 电子表格编辑器 - 使用文件
type: docs
weight: 10
url: /zh/java/spreadsheet-editor-working-with-files/
---
**目录**

- [支持的文件](#SpreadsheetEditor-WorkingwithFiles-SupportedFiles)
- [打开本地文件](#SpreadsheetEditor-WorkingwithFiles-OpenLocalFiles) 
 LoaderService.buildColumnWidthCache
 - LoaderService.buildRowHeightCache
- [从 Dropbox 打开](#SpreadsheetEditor-WorkingwithFiles-OpenfromDropbox)
- [从网址打开](#SpreadsheetEditor-WorkingwithFiles-OpenfromURL) 
 LoaderService.fromUrl
 - LoaderService.buildCellsCache
 LoaderService.buildColumnWidthCache
 - LoaderService.buildRowHeightCache
- [创建一个新的电子表格](#SpreadsheetEditor-WorkingwithFiles-CreateaNewSpreadsheet) 
 LoaderService.fromBlank
 - buildCellsCache
 - buildColumnWidthCache
 - buildRowHeightCache
- [导出为各种格式](#SpreadsheetEditor-WorkingwithFiles-ExporttoVariousFormats)
### **支持的文件**
HTML5 电子表格编辑器可以打开以下格式的文件：

- Excel 1997-2003 XLS
- Excel 2007-2013 XLSX
- XLSM
- XLSB
- XLTX
- SpreadsheetML
- 简历
- 打开文档
### **打开本地文件**
从本地计算机上传文件：

1. 切换到**文件选项卡**在上面。
1. 点击**从计算机打开**打开浏览对话框。
1. 转到所需的文件位置。
1. 单击所需的文件以将其选中。
1. 点击**打开**.

该文件将在编辑器中打开。

![待办事项：图片_替代_文本](bwyl3xi.png)

**怎么运行的？**

**上传文件**

用户从本地计算机选择一个文件，该文件从网络浏览器上传到服务器并由[PrimeFaces 文件上传](https://www.primefaces.org/showcase/ui/file/upload/basic.xhtml)零件。

{{< highlight "java" >}}

 <p:fileUpload fileUploadListener="#\{workbook.onFileUpload\}" update=":ribbon :intro :sheet" />

{{< /highlight >}}

**管理工作簿**

一旦文件完全上传，WorkbookService.onFileUpload 方法就会开始处理这种情况。 WorkbookService 从 Web 浏览器接收事件并跟踪整个工作簿的状态。 WorkbookService.onFileUpload 将控制权传递给 LoaderService 以将工作簿加载到内存中。作为***上传文件***组件提供上传的文件作为[输入流](https://docs.oracle.com/javase/8/docs/api/index.html?java/io/InputStream.html)，LoaderService 使用 LoaderService.fromInputStream 方法加载它。







{{< highlight "java" >}}

 public void onFileUpload(FileUploadEvent e) {

    this.current = loader.fromInputStream(e.getFile().getInputstream(), e.getFile().getFileName());

}

{{< /highlight >}}







**上货和下货**

方法***LoaderService.fromInputStream***阅读***输入流***由 fileUpload 提供***零件***创建实例***com.aspose.cells.Workbook***班级。只要用户在 Web 浏览器中查看或编辑电子表格，此实例就会保留在内存中。当用户离开编辑器或关闭浏览器时，未使用的实例会自动从内存中卸载以保持服务器清洁。







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







**缓存**

缓存对于 HTML5 电子表格编辑器非常重要。它使一切工作顺利。 CellsService 缓存编辑器加载的所有工作簿的行、列、单元格和属性。当 LoaderService 完全加载电子表格时，它会从上到下读取电子表格并通过调用 LoaderService.buildCellsCache、LoaderService.buildColumnWidthCache、LoaderService.buildRowHeightCache 填充缓存







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






### **从 Dropbox 打开**
从 Dropbox 打开文件：

1. 切换到**文件选项卡**在上面。
1. 点击**从 Dropbox 打开**打开 Dropbox 文件选择器。
1. 如果您尚未登录，则需要您登录您的 Dropbox 帐户。
1. 导航到所需的文件并单击以选择它。
1. 点击**选择**在底部。

您选择的文件将从 Dropbox 打开。

![待办事项：图片_替代_文本](1e2sfo0.png)

**怎么运行的？**

这**从 Dropbox 打开**按钮使用**Dropbox JavaScript 选择器 API**打开 Dropbox 选择器对话框。 Chooser 提供所选文件的 URL，该 URL 由回调函数捕获并发送回服务器。服务器从 URL 创建一个电子表格实例，初始化一些内务处理的东西，并将 DOM 更新发送回浏览器。浏览器呈现并刷新 HTML 并且用户已准备好编辑加载的文档。
### **从网址打开**
可以直接从 URL 打开文件。这允许用户编辑 Internet 上任何公开可用的文件。打开文件追加**？网址=位置**具有所需值的参数**地点**在加载编辑器时。例如：

{{< highlight "java" >}}

 http://editor.aspose.com/?url=http://example.com/Sample.xlsx

{{< /highlight >}}

![待办事项：图片_替代_文本](exc9ckp.png)

**怎么运行的？**

**在启动时实例化**

什么时候**工作表视图**后端bean是由JSF实例化的**后构造**方法**在里面**被调用，它使用 LoaderService.fromUrl 加载电子表格。

**缓存**

加载电子表格后立即进行缓存。这**装载机服务**打电话**LoaderService.buildCellsCache**, **LoaderService.buildColumnWidthCache**和**LoaderService.buildRowHeightCache**逐一缓存电子表格的内容并保持所有操作快速流畅。

**DOM 更新**

当电子表格在服务器端准备就绪时，JSF 组件用于生成新的 HTML 并将 DOM 更新发送给由 Web 浏览器呈现的用户。







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






### **创建一个新的电子表格**
要创建一个新的空电子表格：

1. 切换到**文件选项卡**.
1. 点击**新的**按钮。

编辑器将关闭打开的电子表格（如果有），然后打开一个新电子表格。

![待办事项：图片_替代_文本](lnydmmf.png)

**怎么运行的？**

**实例化一个新对象**

当。。。的时候**新的**按钮被用户点击，**工作表视图.loadBlank** ，最终调用**LoaderService.fromBlank**. LoaderService 创建空白电子表格的新实例。

**缓存**

加载电子表格后立即进行缓存。这**装载机服务**打电话**LoaderService.buildCellsCache**, **LoaderService.buildColumnWidthCache**和**LoaderService.buildRowHeightCache**逐一缓存电子表格的内容并保持所有操作快速流畅。

**DOM 更新**

当电子表格在服务器端准备就绪时，JSF 组件用于生成新的 HTML 并将 DOM 更新发送给由 Web 浏览器呈现的用户。







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






### **导出为各种格式**
编辑文件后，用户会想要保存更改。该编辑器允许用户将修改后的电子表格导出并下载到本地计算机。要导出文件：

1. 切换到**文件选项卡**在上面。
1. 点击**出口**作为按钮。
1. 从下拉列表中选择您想要的格式。

修改后的文件将被导出以供下载。支持导出以下格式：

- Excel 2007-2013 XLSX
- Excel 1997-2003 XLS
- Excel XLSM
- Excel XLSB
- Excel XLTX
- Excel XLTM
- SpreadsheetML
- 便携式文档格式 (PDF)
- OpenDocument 电子表格 (ODS)

**怎么运行的？**

打开的电子表格被转换为用户指定的格式，使用**工作表视图.getOutputFile**.







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






