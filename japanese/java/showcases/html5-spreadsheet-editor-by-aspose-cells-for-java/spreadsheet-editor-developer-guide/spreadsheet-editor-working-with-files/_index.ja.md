---
title: スプレッドシートエディタ  ファイル操作
type: docs
weight: 10
url: /ja/java/spreadsheet-editor-working-with-files/
---

**目次**

- [サポートされているファイル](#SpreadsheetEditor-WorkingwithFiles-SupportedFiles)
- [ローカルファイルを開く](#SpreadsheetEditor-WorkingwithFiles-OpenLocalFiles) 
  - LoaderService.buildColumnWidthCache
  - LoaderService.buildRowHeightCache
- [Dropboxから開く](#SpreadsheetEditor-WorkingwithFiles-OpenfromDropbox)
- [URLから開く](#SpreadsheetEditor-WorkingwithFiles-OpenfromURL) 
  - LoaderService.fromUrl
  - LoaderService.buildCellsCache
  - LoaderService.buildColumnWidthCache
  - LoaderService.buildRowHeightCache
- [新しいスプレッドシートを作成](#SpreadsheetEditor-WorkingwithFiles-CreateaNewSpreadsheet) 
  - LoaderService.fromBlank
  - buildCellsCache
  - buildColumnWidthCache
  - buildRowHeightCache
- [さまざまな形式へのエクスポート](#SpreadsheetEditor-WorkingwithFiles-ExporttoVariousFormats)
### **サポートされているファイル**
HTML5スプレッドシートエディタは、以下の形式のファイルを開くことができます:

- Excel 1997-2003 XLS
- Excel 2007-2013 XLSX
- XLSM
- XLSB
- XLTX
- SpreadsheetML
- CVS
- OpenDocument
### **ローカルファイルを開く**
ローカルコンピュータからファイルをアップロードするには:

1. 上部の**ファイル**タブに切り替えます。
1. **コンピュータから開く** をクリックして、ブラウズダイアログを開きます。
1. ファイルの希望する場所に移動します。
1. 選択したいファイルをクリックします。
1. **開く** をクリックします。

ファイルがエディタで開かれます。

![todo:image_alt_text](bwyl3xi.png)

**動作仕様**

**ファイルのアップロード**

ユーザーはWebブラウザからサーバーにアップロードされるローカルコンピュータからファイルを選択し、[PrimeFaces fileUpload](https://www.primefaces.org/showcase/ui/file/upload/basic.xhtml) コンポーネントによって受け取ります。

{{< highlight java >}}

 <p:fileUpload fileUploadListener="#\{workbook.onFileUpload\}" update=":ribbon :intro :sheet" />

{{< /highlight >}}

**ワークブックの管理**

ファイルのアップロードが完了すると、WorkbookService.onFileUploadメソッドが状況を処理するために実行されます。 WorkbookServiceはWebブラウザからイベントを受信し、ワークブック全体の状態を追跡します。 WorkbookService.onFileUploadは制御をLoaderServiceに渡してワークブックをメモリにロードします。 ***fileUpload*** コンポーネントがアップロードされたファイルを[InputStream](https://docs.oracle.com/javase/8/docs/api/index.html?java/io/InputStream.html)として提供するため、LoaderServiceはLoaderService.fromInputStreamメソッドを使用してそれをロードします。







{{< highlight java >}}

 public void onFileUpload(FileUploadEvent e) {

    this.current = loader.fromInputStream(e.getFile().getInputstream(), e.getFile().getFileName());

}

{{< /highlight >}}







**読み込みと解放**

***LoaderService.fromInputStream*** メソッドは、***fileUpload*** コンポーネントによって提供された ***InputStream*** を読み取り、 ***com.aspose.cells.Workbook*** クラスのインスタンスを作成します。このインスタンスは、ユーザーがWebブラウザでスプレッドシートを表示または編集している間はメモリに保持されます。ユーザーがエディタを離れるかブラウザを閉じると、未使用のインスタンスはサーバーをクリーンに保つために自動的にメモリから解放されます。







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







キャッシュ

キャッシュはHTML5スプレッドシートエディタにとって非常に重要です。すべてがスムーズに機能するようにします。CellsServiceは、エディタによって読み込まれたすべてのワークブックの行、列、セル、およびプロパティのキャッシュを保持します。 LoaderServiceはスプレッドシートを完全にロードすると、それを上から下まで読み取り、LoaderService.buildCellsCache、LoaderService.buildColumnWidthCache、LoaderService.buildRowHeightCache を呼び出してキャッシュを埋めます。







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






### **Dropboxから開く**
Dropboxからファイルを開くには:

1. 上部の**ファイル**タブに切り替えます。
1. **Dropboxから開く** をクリックして、Dropboxファイルの選択画面を開きます。
1. まだサインインしていない場合は、Dropboxアカウントにサインインする必要があります。
1. 希望のファイルに移動し、選択してクリックします。
1. 下部の **選択** をクリックします。

選択したファイルがDropboxから開かれます。

![todo:image_alt_text](1e2sfo0.png)

**動作仕様**

「Dropboxから開く」ボタンは、DropboxのChooserダイアログを開くためにDropbox JavaScript Chooser APIを使用しています。Chooserは選択したファイルのURLを提供し、そのURLはコールバック関数によってキャプチャされ、サーバーに送信されます。サーバーはそのURLからスプレッドシートのインスタンスを作成し、いくつかの準備作業を初期化し、DOMの更新をブラウザに送り返します。ブラウザがHTMLをレンダリングし、ドキュメントの編集が可能になります。
### **URLから開く**
ファイルは直接URLから開くことができます。これにより、ユーザーはインターネット上で公開されているファイルを編集できます。エディタをロードする際に、**?url=location**パラメータを望む**location**の値とともに追加してください。例:

{{< highlight java >}}

 http://editor.aspose.com/?url=http://example.com/Sample.xlsx

{{< /highlight >}}

![todo:image_alt_text](exc9ckp.png)

**動作仕様**

起動時にインスタンス化

JSFによって**WorksheetView**バックエンドビーンがインスタンス化されると、**PostConstruct**メソッド**init**が呼び出され、LoaderService.fromUrlを使用してスプレッドシートがロードされます。

キャッシュ

スプレッドシートのロード直後にキャッシュが行われます。**LoaderService**は、**LoaderService.buildCellsCache**、**LoaderService.buildColumnWidthCache**、**LoaderService.buildRowHeightCache**を一つずつ呼び出して、スプレッドシートのコンテンツをキャッシュし、全ての操作を速くスムーズに保ちます。

**DOMの更新**

サーバーサイドでスプレッドシートが準備できたとき、JSFコンポーネントを使用して新しいHTMLを生成し、ユーザーにDOMの更新が送信され、それがウェブブラウザによってレンダリングされます。







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






### **新しいスプレッドシートを作成**
新しい空のスプレッドシートを作成するには:

1. **ファイル**タブに切り替えます。
1. **新規**ボタンをクリックします。

エディタは開いているスプレッドシートを閉じ、新しいスプレッドシートを開きます。

![todo:image_alt_text](lnydmmf.png)

**動作仕様**

新しいオブジェクトをインスタンス化

ユーザーが**新規**ボタンをクリックすると、**WorksheetView.loadBlank**が呼び出され、最終的に**LoaderService.fromBlank**が呼び出されます。LoaderServiceは新しい空のスプレッドシートのインスタンスを作成します。

キャッシュ

スプレッドシートのロード直後にキャッシュが行われます。**LoaderService**は、**LoaderService.buildCellsCache**、**LoaderService.buildColumnWidthCache**、**LoaderService.buildRowHeightCache**を一つずつ呼び出して、スプレッドシートのコンテンツをキャッシュし、全ての操作を速くスムーズに保ちます。

**DOMの更新**

サーバーサイドでスプレッドシートが準備できたとき、JSFコンポーネントを使用して新しいHTMLを生成し、ユーザーにDOMの更新が送信され、それがウェブブラウザによってレンダリングされます。







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






### **さまざまな形式へのエクスポート**
ファイルの編集後、ユーザーは変更を保存したくなるでしょう。エディタを使って変更したスプレッドシートをローカルコンピュータにエクスポートおよびダウンロードすることができます。ファイルをエクスポートするには:

1. 上部の**ファイル**タブに切り替えます。
1. **エクスポート**ボタンをクリックします。
1. ドロップダウンから希望のフォーマットを選択します。

変更されたファイルがダウンロード用にエクスポートされます。以下の形式がエクスポートに対応しています:

- Excel 2007-2013 XLSX
- Excel 1997-2003 XLS
- Excel XLSM
- Excel XLSB
- Excel XLTX
- Excel XLTM
- SpreadsheetML
- Portable Document Format (PDF)
- OpenDocument Spreadsheet (ODS)

**動作仕様**

開いているスプレッドシートは、**WorksheetView.getOutputFile**を使用してユーザー指定の形式に変換されます。







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






