---
title: 电子表格编辑器  与文件一起使用
type: docs
weight: 10
url: /zh/java/spreadsheet-editor-working-with-files/
---

**目录**

- [支持的文件](#SpreadsheetEditor-WorkingwithFiles-SupportedFiles)
- [打开本地文件](#SpreadsheetEditor-WorkingwithFiles-OpenLocalFiles) 
  - LoaderService.buildColumnWidthCache
  - LoaderService.buildRowHeightCache
- [从 Dropbox 打开](#SpreadsheetEditor-WorkingwithFiles-OpenfromDropbox)
- [从URL打开](#SpreadsheetEditor-WorkingwithFiles-OpenfromURL) 
  - LoaderService.fromUrl
  - LoaderService.buildCellsCache
  - LoaderService.buildColumnWidthCache
  - LoaderService.buildRowHeightCache
- [创建新电子表格](#SpreadsheetEditor-WorkingwithFiles-CreateaNewSpreadsheet) 
  - LoaderService.fromBlank
  - buildCellsCache
  - buildColumnWidthCache
  - buildRowHeightCache
- [导出到各种格式](#SpreadsheetEditor-WorkingwithFiles-ExporttoVariousFormats)
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
上传来自本地计算机的文件:

1. 切换到顶部的 **文件** 选项卡。
1. 单击**从计算机打开**以打开浏览对话框.
1. 转到所需的文件位置。
1. 点击所需的文件以选择它。
1. 点击 **打开**。

文件将在编辑器中打开。

![todo:image_alt_text](bwyl3xi.png)

**它是如何工作的？**

**文件上传**

用户从本地计算机中选择一个文件，该文件通过 Web 浏览器上传到服务器，并由 [PrimeFaces fileUpload](https://www.primefaces.org/showcase/ui/file/upload/basic.xhtml) 组件接收。

{{< highlight java >}}

 <p:fileUpload fileUploadListener="#\{workbook.onFileUpload\}" update=":ribbon :intro :sheet" />

{{< /highlight >}}

**管理工作簿**

一旦文件完全上传，WorkbookService.onFileUpload 方法开始处理情况。WorkbookService 从 Web 浏览器接收事件，并跟踪整个工作簿的状态。WorkbookService.onFileUpload 将控制权转交给 LoaderService 将工作簿加载到内存中。由于 ***fileUpload*** 组件将已上传的文件提供为 [InputStream](https://docs.oracle.com/javase/8/docs/api/index.html?java/io/InputStream.html)，LoaderService 使用 LoaderService.fromInputStream 方法进行加载。







{{< highlight java >}}

 public void onFileUpload(FileUploadEvent e) {

    this.current = loader.fromInputStream(e.getFile().getInputstream(), e.getFile().getFileName());

}

{{< /highlight >}}







**加载和卸载**

***LoaderService.fromInputStream*** 方法读取 ***component*** 提供的 ***InputStream***，创建 ***com.aspose.cells.Workbook*** 类的实例。只要用户在 Web 浏览器中查看或编辑电子表格，这个实例就会保留在内存中。当用户离开编辑器或关闭浏览器时，未使用的实例会自动从内存中卸载，以保持服务器的整洁。







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

缓存对 HTML5 电子表格编辑器非常重要。它使一切运行顺畅。CellsService 保持缓存行、列、单元格和编辑器加载的所有工作簿的属性。当 LoaderService 完全加载电子表格时，它从上到下读取它，并通过调用 LoaderService.buildCellsCache、LoaderService.buildColumnWidthCache、LoaderService.buildRowHeightCache 填充缓存。







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






### **从 Dropbox 打开**
要从 Dropbox 打开文件：

1. 切换到顶部的 **文件** 选项卡。
1. 点击 **从 Dropbox 打开** 打开 Dropbox 文件选择器。
1. 如果您尚未登录，它将要求您登录到您的 Dropbox 帐户。
1. 导航到所需的文件并单击选择。
1. 在底部单击**选择**。

您选择的文件将从Dropbox中打开。

![todo:image_alt_text](1e2sfo0.png)

**它是如何工作的？**

**从Dropbox打开**按钮使用**Dropbox JavaScript选择器API**来打开Dropbox选择器对话框。选择器提供所选文件的URL，由回调函数捕获并发送回服务器。服务器从URL创建电子表格的实例，初始化一些日常事务处理工作，并将DOM更新发送回浏览器。浏览器渲染并刷新HTML，用户准备编辑加载的文档。
### **从URL打开**
文件可以直接从URL打开。这允许用户编辑互联网上的任何公开可用的文件。在加载编辑器时，添加**?url=位置**参数，并将您所需的**位置**的值附加到文件末尾。例如：

{{< highlight java >}}

 http://editor.aspose.com/?url=http://example.com/Sample.xlsx

{{< /highlight >}}

![todo:image_alt_text](exc9ckp.png)

**它是如何工作的？**

**在启动期间实例化**

当**WorksheetView**后端bean由JSF实例化时，将调用**PostConstruct**方法**init**，使用LoaderService.fromUrl加载电子表格。

**缓存**

电子表格加载完毕后立即进行缓存。**LoaderService** 依次调用 **LoaderService.buildCellsCache**、**LoaderService.buildColumnWidthCache** 和 **LoaderService.buildRowHeightCache** 进行电子表格内容的缓存，以确保所有操作快速流畅。

**DOM 更新**

服务器端准备好电子表格后，使用 JSF 组件生成新的 HTML，并向用户发送 DOM 更新，由 Web 浏览器进行渲染。







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
要创建一个新的空白电子表格：

1. 切换到 **文件** 选项卡。
1. 点击 **新建** 按钮。

如果有打开的电子表格文件，编辑器将关闭该文件并打开一个新的文件。

![todo:image_alt_text](lnydmmf.png)

**它是如何工作的？**

**实例化一个新对象**

当用户点击 **新建** 按钮时，将调用 **WorksheetView.loadBlank**，最终调用 **LoaderService.fromBlank**。 LoaderService 会创建一个新的空白电子表格实例。

**缓存**

电子表格加载完毕后立即进行缓存。**LoaderService** 依次调用 **LoaderService.buildCellsCache**、**LoaderService.buildColumnWidthCache** 和 **LoaderService.buildRowHeightCache** 进行电子表格内容的缓存，以确保所有操作快速流畅。

**DOM 更新**

服务器端准备好电子表格后，使用 JSF 组件生成新的 HTML，并向用户发送 DOM 更新，由 Web 浏览器进行渲染。







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






### **导出到各种格式**
编辑文件后，用户希望保存更改。编辑器允许用户将修改后的电子表格导出并下载到本地计算机。要导出文件：

1. 切换到顶部的 **文件** 选项卡。
1. 点击 **导出** 按钮。
1. 从下拉菜单中选择所需的格式。

修改后的文件将被导出并可下载。支持以下格式进行导出:

- Excel 2007-2013 XLSX
- Excel 1997-2003 XLS
- Excel XLSM
- Excel XLSB
- Excel XLTX
- Excel XLTM
- SpreadsheetML
- 便携式文档格式 (PDF)
- 开放文档表格 (ODS)

**它是如何工作的？**

打开的电子表格将使用 **WorksheetView.getOutputFile** 转换为用户指定的格式。







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
