---
title: スプレッドシート エディター - ファイルの操作
type: docs
weight: 10
url: /ja/java/spreadsheet-editor-working-with-files/
---
**目次**

- [サポートされているファイル](#SpreadsheetEditor-WorkingwithFiles-SupportedFiles)
- [ローカル ファイルを開く](#SpreadsheetEditor-WorkingwithFiles-OpenLocalFiles) 
 LoaderService.buildColumnWidthCache
 - LoaderService.buildRowHeightCache
- [ドロップボックスから開く](#SpreadsheetEditor-WorkingwithFiles-OpenfromDropbox)
- [URLから開く](#SpreadsheetEditor-WorkingwithFiles-OpenfromURL) 
 LoaderService.fromUrl
 - LoaderService.buildCellsCache
 LoaderService.buildColumnWidthCache
 - LoaderService.buildRowHeightCache
- [新しいスプレッドシートを作成する](#SpreadsheetEditor-WorkingwithFiles-CreateaNewSpreadsheet) 
 LoaderService.fromBlank
 - buildCellsCache
 -buildColumnWidthCache
 -buildRowHeightCache
- [さまざまな形式にエクスポート](#SpreadsheetEditor-WorkingwithFiles-ExporttoVariousFormats)
### **サポートされているファイル**
HTML5 スプレッドシート エディターでは、次の形式のファイルを開くことができます。

- Excel 1997-2003 XLS
- Excel 2007-2013 XLSX
- XLSM
- XLSB
- XLTX
- スプレッドシートML
- CVS
- OpenDocument
### **ローカル ファイルを開く**
ローカル コンピューターからファイルをアップロードするには:

1. 切り替える**ファイルタブ**上に。
1. クリック**パソコンから開く**参照ダイアログを開きます。
1. ファイルの目的の場所に移動します。
1. 目的のファイルをクリックして選択します。
1. クリック**開ける**.

ファイルがエディターで開かれます。

![todo:画像_代替_文章](bwyl3xi.png)

**使い方？**

**ファイルのアップロード**

ユーザーはローカル コンピューターからファイルを選択します。このファイルは、Web ブラウザーからサーバーにアップロードされ、によって受信されます。[PrimeFaces ファイルアップロード](https://www.primefaces.org/showcase/ui/file/upload/basic.xhtml)成分。

{{< highlight "java" >}}

 <p:fileUpload fileUploadListener="#\{workbook.onFileUpload\}" update=":ribbon :intro :sheet" />

{{< /highlight >}}

**ワークブックの管理**

ファイルが完全にアップロードされるとすぐに、 WorkbookService.onFileUpload メソッドが動作して状況を処理します。 WorkbookService は Web ブラウザーからイベントを受け取り、ブック全体の状態を追跡します。 WorkbookService.onFileUpload は、コントロールを LoaderService に渡し、ワークブックをメモリに読み込みます。として***ファイルアップロード***コンポーネントは、アップロードされたファイルを[入力ストリーム](https://docs.oracle.com/javase/8/docs/api/index.html?java/io/InputStream.html)、LoaderService は LoaderService.fromInputStream メソッドを使用してそれをロードします。







{{< highlight "java" >}}

 public void onFileUpload(FileUploadEvent e) {

    this.current = loader.fromInputStream(e.getFile().getInputstream(), e.getFile().getFileName());

}

{{< /highlight >}}







**上げ下ろし**

方法***LoaderService.fromInputStream***を読む***入力ストリーム***fileUpload 提供***成分***のインスタンスを作成***com.aspose.cells.Workbook***クラス。このインスタンスは、ユーザーが Web ブラウザーでスプレッドシートを表示または編集し続ける限り、メモリに保持されます。ユーザーがエディターを離れるかブラウザーを閉じると、使用されていないインスタンスがメモリから自動的にアンロードされ、サーバーがクリーンに保たれます。







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







**キャッシング**

キャッシングは、HTML5 スプレッドシート エディターにとって非常に重要です。すべてがスムーズに機能します。 CellsService は、エディターによって読み込まれたすべてのワークブックのキャッシュ行、列、セル、およびプロパティを保持します。 LoaderService がスプレッドシートを完全にロードすると、スプレッドシートを上から下に読み取り、LoaderService.buildCellsCache、LoaderService.buildColumnWidthCache、LoaderService.buildRowHeightCache を呼び出してキャッシュをいっぱいにします。







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






### **ドロップボックスから開く**
Dropbox からファイルを開くには:

1. 切り替える**ファイルタブ**上に。
1. クリック**ドロップボックスから開く** Dropbox ファイル チューザーを開きます。
1. まだサインインしていない場合は、Dropbox アカウントにサインインする必要があります。
1. 目的のファイルに移動し、クリックして選択します。
1. クリック**選ぶ**底に。

選択したファイルが Dropbox から開かれます。

![todo:画像_代替_文章](1e2sfo0.png)

**使い方？**

の**ドロップボックスから開く**ボタンの使用**Dropbox JavaScript セレクター API**Dropbox Chooser ダイアログを開きます。 Chooser は、コールバック関数によってキャプチャされ、サーバーに送り返される、選択されたファイルの URL を提供します。サーバーは URL からスプレッドシートのインスタンスを作成し、いくつかのハウスキーピングを初期化し、DOM の更新をブラウザーに送り返します。ブラウザーが HTML をレンダリングして更新すると、ユーザーは読み込まれたドキュメントを編集できるようになります。
### **URLから開く**
ファイルは URL から直接開くことができます。これにより、ユーザーはインターネット上で公開されているファイルを編集できます。ファイルを開くには追加**?url=場所**希望の値を持つパラメーター**位置**エディタのロード中。例えば：

{{< highlight "java" >}}

 http://editor.aspose.com/?url=http://example.com/Sample.xlsx

{{< /highlight >}}

![todo:画像_代替_文章](exc9ckp.png)

**使い方？**

**起動時にインスタンス化**

いつ**ワークシート ビュー**バックエンド Bean は、JSF によってインスタンス化されます。**ポストコンストラクト**方法**初期化**が呼び出され、LoaderService.fromUrl を使用してスプレッドシートをロードします。

**キャッシング**

キャッシュは、スプレッドシートが読み込まれた直後に発生します。の**ローダーサービス**通話**LoaderService.buildCellsCache**, **LoaderService.buildColumnWidthCache**と**LoaderService.buildRowHeightCache**スプレッドシートのコンテンツを 1 つずつキャッシュし、すべての操作を高速かつスムーズに保ちます。

**DOM の更新**

サーバー側でスプレッドシートの準備ができると、JSF コンポーネントを使用して新しい HTML が生成され、Web ブラウザーによってレンダリングされる DOM 更新がユーザーに送信されます。







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






### **新しいスプレッドシートを作成する**
新しい空のスプレッドシートを作成するには:

1. 切り替える**ファイルタブ**.
1. クリック**新しい**ボタン。

エディターは、開いているスプレッドシートがあればそれを閉じ、新しいスプレッドシートを開きます。

![todo:画像_代替_文章](lnydmmf.png)

**使い方？**

**新しいオブジェクトをインスタンス化する**

とき**新しい**ボタンがユーザーによってクリックされ、**WorksheetView.loadBlank** 、最終的に呼び出します**LoaderService.fromBlank**. LoaderService は、空白のスプレッドシートの新しいインスタンスを作成します。

**キャッシング**

キャッシュは、スプレッドシートが読み込まれた直後に発生します。の**ローダーサービス**通話**LoaderService.buildCellsCache**, **LoaderService.buildColumnWidthCache**と**LoaderService.buildRowHeightCache**スプレッドシートのコンテンツを 1 つずつキャッシュし、すべての操作を高速かつスムーズに保ちます。

**DOM の更新**

サーバー側でスプレッドシートの準備ができると、JSF コンポーネントを使用して新しい HTML が生成され、Web ブラウザーによってレンダリングされる DOM 更新がユーザーに送信されます。







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






### **さまざまな形式にエクスポート**
ファイルを編集した後、ユーザーは変更を保存したいと思うでしょう。エディタを使用すると、変更したスプレッドシートをエクスポートしてローカル コンピュータにダウンロードできます。ファイルをエクスポートするには:

1. 切り替える**ファイルタブ**上に。
1. クリック**輸出**ボタンとして。
1. ドロップダウンから目的の形式を選択します。

変更されたファイルはダウンロード用にエクスポートされます。エクスポートでは、次の形式がサポートされています。

- Excel 2007-2013 XLSX
- Excel 1997-2003 XLS
- エクセルXLSM
- エクセルXLSB
- エクセルXLTX
- エクセルXLTM
- スプレッドシートML
- ポータブル ドキュメント形式 (PDF)
- OpenDocument スプレッドシート (ODS)

**使い方？**

開いたスプレッドシートは、次を使用してユーザー指定の形式に変換されます**WorksheetView.getOutputFile**.







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






