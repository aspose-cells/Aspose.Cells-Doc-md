---
title: ワークシートをCSVに変換
type: docs
weight: 30
url: /ja/java/convert-worksheet-to-csv/
---
## **Aspose.Cells - ワークシートを CSV に変換**
開発者がファイルを保存場所に保存する必要がある場合は、ファイル名 (完全な保存パスを含む) と目的のファイル形式 (**ファイル形式の種類**列挙) の呼び出し中**セーブ**方法**ワークブック**物体。

**Java**

{{< highlight "java" >}}

 //Instantiate a new workbook with Excel file path

Workbook workbook = new Workbook(dataPath + "workbook.xls");

//Save the document in PDF format

workbook.save(dataPath + "AsposeWorkbookCSV.csv", SaveFormat.CSV);

{{< /highlight >}}
## **Apache POI SS - HSSF & XSSF - ワークシートを CSV に変換**
以下のコードは、Aspose.Cells Java API と比較して、Apache POI HSSF および XSSF API を使用してワークシートを CSV に変換する方法を示しています。

**Java**

{{< highlight "java" >}}

 /**

\* をモデルにした基本的な XLSX -> CSV プロセッサ

\* POI サンプル プログラム XLS2CSVmra by Nick Burch

\* パッケージ org.apache.poi.hssf.eventusermodel.examples.

\* HSSF バージョンとは異なり、これは完全に無視されます

\* 行がありません。

\* <p/>

\* データ シートは SAX パーサーを使用して読み込まれ、

\* メモリ使用量が比較的小さいため、これは

\* 巨大なワークブックを読むことができます。スタイル テーブルと

\* 共有文字列テーブルはメモリに保持する必要があります。の

\* 標準の POI スタイル テーブル クラスが使用されますが、カスタム

\* (読み取り専用) クラスは共有文字列テーブルに使用されます

\* 標準の POI SharedStringsTable が非常に大きくなるため

\* 一意の文字列の数ですばやく。

\* <p/>

\* 問題を修正するパッチを提供してくれた Eric Smith に感謝します

\* 複数の "t" 要素を持つセルによってトリガーされます。

\* Excel がさまざまな形式を表す方法 (たとえば、1 つの単語

\* プレーンで 1 単語太字)。

\*

\* @作者 クリス・ロット

*/

public class ApacheXLSX2CSV {  /**  * データ値のタイプは、セルの属性によって示されます.  * 値は通常、セル内の「v」要素にあります.  */  enum xssfDataType {  BOOL,  ERROR,  FORMULA,  INLINESTR,  SSTINDEX,  NUMBER,  }   /**  * Derived from http://poi.apache.org /spreadsheet/how-to.html#xssf_sax_api  * <p/>  * 標準 ECMA-376、第 1 版、パート 4、1928ff ページ、at  * http://www.ecma-international.org/ も参照Publications/standards/Ecma-376.htm  * <p/>  * ウェブに適したバージョンは http://openiso.org/Ecma/376/Part4  */  class MyXSSFSheetHandler extends DefaultHandler { / **  * スタイルのあるテーブル  */  プライベートte StylesTable stylesTable;  /**  * Table with unique strings  */  private ReadOnlySharedStringsTable sharedStringsTable;  /**  * Destination for data  */  private final PrintStream output;  /* *  * leftmost から始まる読み取る列の数  */  private final int minColumnCount;  // V 開始要素が見られるときに設定します  private boolean vIsOpen; セル開始 0 要素 _x0 が見られる場合に設定されます //   //セルクローズ要素が見られたときに使用。 private xssfdatatype nextdatatype;   // numeric cell値をフォーマットするために使用private int thisColumn = -1;  // 出力に出力される最後の列Stream  private int lastcolumnnumber = -1;   // gathers characters as seed.    ** ** ** _ x000d_x000d_x000dx000dx000dx000dx000d_x000 of styles  * @param strings Table of shared strings  * @param cols Minimum number of columns to show  * @param target Sink for output  */  public MyXSSFSheetHandler(  StylesTable styles,  ReadOnlySharedStringsTable strings,  int cols,  PrintStream target) {  this.stylesTable = styles;  this.sharedStringsTable = string;  this.minColumnCount = cols;  this.output = target;  new String.output = target;  );  this.nextDataType = xssfDataType.NUMBER;  this.formatter = new DataFormatter();_x000 @see org.xml.sax.helpers.DefaultHandler#startElement(java.lang.String, java.lang.String, java.lang.String, org.xml.sax.Attributes)  */  public void startElement(String uri, String localName, String name,  Attributes attributes) throws SAXException {  if ("inlineStr".equals(name) || "v".equals(name)) {  vIsOpen = true;  // コンテンツをクリア cache  value.setLength(0);  }  // c => cell else" if ("0c else" if ("0c else" if equals(name)) {  // セル参照を取得します  String r = attributes.getValue("r");  int firstDigit = -1;  for (int c = 0; c < r.length( ); ++c) {  if (Character.isDigit(r.charAt(c))) {  firstDigit = c;  break;  }  } Tosub.Tosub.Column(dthisColumn =d 0, firstDigit));  // デフォルトを設定します。 "t");  String cellStyleStr = attributes.getValue("s");  if ("b".equals(cellType))  nextDataType = xssfDataType.BOOL; _x00 0d_ else if ("e".equals(cellType))  nextDataType = xssfDataType.ERROR;  else if ("inlineStr".equals(cellType))  nextDataType = xssfDataType.INLINESTR;  else if ( ".equals(cellType))  nextDataType = xssfDataType.SSTINDEX;  else if ("str".equals(cellType))  nextDataType = xssfDataType.FORMULA;  else if (cellStyleStr_ !x0d_x00 null) // これは数値ですが、ほぼ確実に one  // 特殊なスタイルまたは format  int styleIndex = Integer.parseInt(cellStyleStr);  XSSFCellStyle style = stylesTable.getStyleAt(styleIndex);  this.formatIndex = style. getDataFormat();  this.formatString = style.getDataFormatString();  if (this.formatString == null)  this.formatString = BuiltinFormats.getBuiltinFormat(this.formatIndex);  } 0d_0d_00 } _x000 d_ /*  * (非 Javadoc)  * @org.xml.sax.helpers.DefaultHandler#endElement(java.lang.String, java.lang.String, java.lang.String)  */ を参照  public void endElement(String uri, String localName, String name)  throws SAXException {  String thisStr = null;  // v => cell  if ("v".equals(name)) の内容{  // 必要に応じて値の内容を処理します。  // characters() は複数回呼び出される可能性があるため、今すぐ実行してください  switch (nextDataType) {  case BOOL:  char first = value.charAt(0 );  thisStr = 最初 == '0' ? "FALSE" : "TRUE";  break;  case ERROR:  thisStr = "\"ERROR:" + value.toString() + '"';  break;  case FORMULAd_x000 / 数式は文字列値になる可能性があります,  // したがって、常に二重引用符を追加してください.  thisStr = '"' + value.toString() + '"';  break;  case INLINESTR:  // TODO: この例を見たので、未テストです。  break;  case SSTINDEX:  String sstIndex = value.toString();  try {  int idx = Integer.parseInt(sstIndex);  XSSFRichTextString rtss = new XSSFRichTextString(sharedStringsTable.getEntryAt(idx)) ;  thisStr = '"' + rtss.toString() + '"';  }  catch (NumberFormatExc eption ex) {  output.println("SST インデックスの解析に失敗しました '" + sstIndex + "': " + ex.toString());  } String  break;  case NUMBER: _x0 =00d_ n value.toString();  if (this.formatString != null)  thisStr = formatter.formatRawCellContents(Double.parseDouble(n), this.formatIndex, this.formatString);  else  thisStr = n;_x000d  break;  default:  thisStr = "(TODO: Unexpected type: " + nextDataType + ")";  break;  }  //0 文字列の内容を見た後に出力 Emitd_0d_x0この row  if (lastColumnNumber == -1) {  lastColumnNumber = 0;  }  for (int i = lastColumnNumber; i < thisColumn; ++i)  output.print(',');  // 空の文字列の可能性があります.  output.print(thisStr);  // column  if (thisColumn > -1) _x0 を更新しますlastColumnNumber = thisColumn;  } else if ("row".equals(name)) {  // 不足しているコンマがある場合は出力します  if (minColumns > 0) {  // 列は 0 ベース 0 if ( lastColumnNumber == -1) {  lastColumnNumber = 0;  }  for (int i = lastColumnNumber; i < (this.minColumnCount); i++) {  output.print(','); _ } _X000D_ _X000D_} _X000D_ _X000D_ //私たちは新しいrow  output.println（）; _ x000d_  lastcolumnnumber = -1;  } _______________________________________________________________________________________________________X000のCARPARUMNNUMBERN（）; open.  * 元々はただの "v" でした。 inlineStr 用に拡張されています。   }  /**  * Converts an Excel column name like "C" to a zero-based index.  *  * @param name  * @return Index corresponding to the specified name  */  private int nameToColumn(文字列名) {  int column = -1;  for (int i = 0; i < name.length(); ++i) {  int c = name.charAt(i) ;  column = (column + 1) * 26 + c - 'A';  }  return column;  }  }  ///////// ///////////////////////  private OPCPackage xlsxPackage;  private int minColumns;  private PrintStream 出力;  /**_x0 00d_  * 新しい XLSX を作成します -> CSV コンバーター  *  * @param pkg 処理する XLSX パッケージ  * @param output CSV を出力する PrintStream to  * @param minColumns 出力する列の最小数-1 for no minimum  */  public ApacheXLSX2CSV(OPCPackage pkg, PrintStream output, int minColumns) {  this.xlsxPackage = pkg;  this.output = output;  this.minColumns = minColumns;  } _X000D_ _X000D_ /** _ X000D_ _X000D_ *パンソルと表示された1つのSHEIT_X000D_のコンテンツを表示します。   public void processSheet(  StylesTable スタイル、  ReadOnlySharedStringsTable 文字列、  InputStream sheetInputStream)_x000 d_  throws IOException, ParserConfigurationException, SAXException {  InputSource sheetSource = new InputSource(sheetInputStream);  SAXParserFactory saxFactory = SAXParserFactory.newInstance();  SAXParser saxParser = saxFactory.newSAXParser();  XMLReader sheetParser = saxParser.getXMLReader ();  ContentHandler handler = new MyXSSFSheetHandler(styles, strings, this.minColumns, this.output);  sheetParser.setContentHandler(handler);  sheetParser.parse(sheetSource);  } _x /**0   * Initiates the processing of the XLS workbook file to CSV.  *  * @throws IOException  * @throws OpenXML4JException  * @throws ParserConfigurationException  * @throws SAXException  */  public void process()  IOException、OpenXML4JException、ParserConfiguratio をスローしますnException, SAXException {  ReadOnlySharedStringsTable strings = new ReadOnlySharedStringsTable(this.xlsxPackage);  XSSFReader xssfReader = new XSSFReader(this.xlsxPackage);  StylesTable styles = xssfReader.getStylesTable();  XSSFReader.SheetIterator iter = (XSSFReader .SheetIterator) xssfReader.getSheetsData();  int index = 0;  while (iter.hasNext()) {  InputStream ストリーム = iter.next();  文字列 sheetName = iter.getSheetName(0d_x);  this.output.println();  this.output.println(sheetName + " [index=" + index + "]:");  processSheet(スタイル、文字列、ストリーム);  stream.close( ）; _ x000d_  ++ index;  }  }   public static void main（string [] args [] args） _ File xlsxFile = new File(dataPath + "workbook.xls");  if (!xlsxFile.exists())  {  System.err.println("見つからないか、ファイルではありません: " + xlsxFile. getPath());  return;  }  int minColumns = -1;  if (args.length >= 2) minColumns = Integer.parseInt(args[0d_x00]; //0d _x00);パッケージのオープンは瞬時に行われます.  OPCPackage p = OPCPackage.open(xlsxFile.getPath(), PackageAccess.READ);  ApacheXLSX2CSV xlsx2csv = new ApacheXLSX2CSV(p, System.out, minColumns);  xlsx2 .process();  }   {{< /highlight >}} ## **実行中のコードをダウンロード** 以下のいずれかのソーシャル コーディング サイトから **ワークシートを CSV に変換**をダウンロード:  - [GitHub](https: //github.com/aspose-cells/Aspose.Cells-for-Java/releases/download/Aspose.Cells_Java_vs_POI_SS_v1.4/Convert.Worksheet.to.CSV.Aspose.Cells.vs.Apache.POI.SS.zip)_x00 0d_  {{% alert color="primary" %}}   詳細は、[ファイルの保存](/cells/java/ Saving-excel-files-to-csv-pdf-and-other-formats/).  {{% /alert %}} をご覧ください。