---
title: 将工作表转换为 CSV
type: docs
weight: 30
url: /zh/java/convert-worksheet-to-csv/
---
## **Aspose.Cells - 将工作表转换为 CSV**
如果开发人员需要将他们的文件保存到某个存储位置，那么他们可以简单地指定文件名（及其完整的存储路径）和所需的文件格式（使用**文件格式类型**枚举），同时调用**救球**的方法**工作簿**目的。

**Java**

{{< highlight "java" >}}

 //Instantiate a new workbook with Excel file path

Workbook workbook = new Workbook(dataPath + "workbook.xls");

//Save the document in PDF format

workbook.save(dataPath + "AsposeWorkbookCSV.csv", SaveFormat.CSV);

{{< /highlight >}}
## **Apache POI SS - HSSF 和 XSSF - 将工作表转换为 CSV**
下面的代码显示了如何使用 Apache POI HSSF 和 XSSF 将工作表转换为 CSV API 与 Aspose.Cells Java API 相比。

**Java**

{{< highlight "java" >}}

 /**

\* 一个基本的 XLSX -> CSV 处理器仿照

\* Nick Burch 的 POI 示例程序 XLS2CSVmra 来自

\* 包 org.apache.poi.hssf.eventusermodel.examples。

\* 与 HSSF 版本不同，这个完全忽略了

\* 缺少行。

\* <p/>

\* 使用 SAX 解析器读取数据表以保持

\* 内存占用比较小，所以应该这样

\* 能够阅读大量的工作簿。样式表和

\* 共享字符串表必须保存在内存中。这

\* 使用标准 POI 样式表类，但自定义

\*（只读）类用于共享字符串表

\* 因为标准 POI SharedStringsTable 增长非常快

\* 快速添加唯一字符串的数量。

\* <p/>

\* 感谢 Eric Smith 提供的修复问题的补丁

\* 由具有多个“t”元素的单元格触发，即

\* Excel 如何表示不同的格式（例如，一个单词

\* 普通和一个单词粗体）。

\*

\* @author 克里斯·洛特

*/

public class ApacheXLSX2CSV {  /**  * 数据值的类型由单元格上的属性指示。  * 该值通常位于单元格中的“v”元素中。  */  enum xssfDataType {  BOOL,  ERROR,  FORMULA,  INLINESTR,  SSTINDEX,  NUMBER,  }   /**  * Derived from http://poi.apache.org /spreadsheet/how-to.html#xssf_sax_api  * <p/>  * 另见标准 ECMA-376，第一版，第 4 部分，第 1928ff 页，at  * http://www.ecma-international.org/ publications/standards/Ecma-376.htm  * <p/>  * Web 友好版本为 http://openiso.org/Ecma/376/Part4  */  class MyXSSFSheetHandler extends Default_000d / _x0 **  * 样式表  */  priva te StylesTable stylesTable;  /**  * Table with unique strings  */  private ReadOnlySharedStringsTable sharedStringsTable;  /**  * Destination for data  */  private final PrintStream output;  /* *  * 从最左端开始读取的列数 //使用时使用了单元关闭元件。 private int thisColumn = -1;  // 打印到输出的最后一列stream private int lastColumnNumber = -1;  // gathers字符所看到的。 of styles  * @param strings Table of shared strings  * @param cols Minimum number of columns to show  * @param target Sink for output  */  public MyXSSFSheetHandler(  StylesTable styles,  ReadOnlySharedStringsTable strings,  int cols，  PrintStream 目标）{  this.stylesTable = 样式；  this.sharedStringsTable = 字符串；  this.minColumnCount = cols；  this.output0 = new__x000d string__x000d（0d String_Buffer this.output = target__x0x00 );  this.nextDataType = xssfDataType.NUMBER;  this.formatter = new DataFormatter();_x000 d_  }  /*  *（非 Javadoc）  * @see org.xml.sax.helpers.DefaultHandler#startElement（java.lang.String，java.lang.String，java.lang.String， org.xml.sax.Attributes)  */  public void startElement(String uri, String localName, String name,  Attributes attributes) 抛出 SAXException {  if ("inlineStr".equals(name) || "v".equals(name)) {  vIsOpen = true;  // 清除内容缓存  value.setLength(0);  }  // c => cell  if (0)._x00d else equals(name)) {  // 获取单元格引用  String r = attributes.getValue("r");  int firstDigit = -1;  for (int c = 0; c < r.length( ）; ++ c）{if（tarria.isdigit（r.charat（c）））{firstDigit = c;  break; __000d___000d___00 _strimn 0, firstDigit));  // 设置默认值。  this.nextDataType = xssfDataType.NUMBER;  this.formatIndex = -1;  this.formatString = null;  string_Valuex =00 attributes( "t");  String cellStyleStr = attributes.getValue("s");  if ("b".equals(cellType))  nextDataType = xssfDataType.BOOL; _x00 0d_ else if ("e".equals(cellType))  nextDataType = xssfDataType.ERROR;  else if ("inlineStr".equals(cellType))  nextDataType = xssfDataType.INLINESTR;  其他如果".equals(cellType))  nextDataType = xssfDataType.SSTINDEX;  else if ("str".equals(cellType))  nextDataType = xssfDataType.FORMULA;  else if (cellStyle_x00d_0 nullStrx != 0 // 这是一个数字，但几乎可以肯定是一个  // 具有特殊的样式或格式getDataFormat（）; _ x000d_this.formatString = style.getDataFormatString（）; _ x000d_ if（this.this.formattring == null）_x00d___x _______00 _form_form_form_form_000_000_000_000d_000.getBuittAtextaTIftAtt（tishd.dext） } _x000 d_ /*  * (非 Javadoc)  * @see org.xml.sax.helpers.DefaultHandler#endElement(java.lang.String, java.lang.String, java.lang.String)  */   public void endElement(String uri, String localName, String name)  throws SAXException {  String thisStr = null;  // v => 单元格的内容  if ("v".equals(name)) {  // 根据需要处理值内容。  // 现在执行，因为 characters() 可能被调用多次  switch (nextDataType) {  case BOOL:  char first = value.charAt(0 );  thisStr = first == '0' ? “FALSE”：“TRUE”；  break；  case ERROR：  thisStr = "\"ERROR:" + value.toString() + '"';  break;  case FORMULA:_x 0 / 公式可能会产生字符串值，  // 所以总是添加双引号字符。  thisStr = '"' + value.toString() + '"';  break;  case INLINESTR:  // TODO: 已经看到了这个例子，所以它是未经测试的 break;  case SSTINDEX:  String sstIndex = value.toString();  try {  int idx = Integer.parseInt(sstIndex);  XSSFRichTextString rtss = new XSSFRichTextString(sharedStringsTable.getEntryAt(idx)) ;  thisStr = '"' + rtss.toString() + '"';  }  catch (NumberFormatExc eption ex) {  output.println("无法解析 SST 索引 '" + sstIndex + "': " + ex.toString());  }  break;  case NUMBER:  String = value.toString();  if (this.formatString != null)  thisStr = formatter.formatRawCellContents(Double.parseDouble(n), this.formatIndex, this.formatString);  else x0Str = n;  break;  default:  thisStr = "(TODO: Unexpected type: " + nextDataType + ")";  break;  }  // 在我们看到 string000d contents_x00 后输出 //此行上缺少的任何字段的逗号  if (lastColumnNumber == -1) {  lastColumnNumber = 0;  }  for (int i = lastColumnNumber;我 < 这列; ++i)  output.print(',');  // 可能是空字符串。  output.print(thisStr);  // 更新 column  if (thisColumn > -1) d_ _x0 lastColumnNumber = thisColumn;  } else if ("row".equals(name)) {  // 如果需要打印出任何缺失的逗号  if (minColumns > 0) {  // 列为 0 based _ _x ( lastColumnNumber == -1) {  lastColumnNumber = 0;  }  for (int i = lastColumnNumber; i < (this.minColumnCount); i++) {  output.print(',');  }   }  // We're onto a new row  output.println();  lastColumnNumber = -1;  }  }  /**  * Captures characters only if a suitable element is open.  * 原来只是“v”；也为 inlineStr 扩展。   }  /**  * Converts an Excel column name like "C" to a zero-based index.  *  * @param name  * @return Index corresponding to the specified name  */  private int nameToColumn(字符串名称) {  int column = -1;  for (int i = 0; i < name.length(); ++i) {  int c = name.charAt(i) ;  列 = (列 + 1) * 26 + c - 'A';  }  返回列;  }  }  } _x000d///////////////// ///////////////  private OPCPackage xlsxPackage;  private int minColumns;  private PrintStream 输出;  /**_x0 00d_  * Creates a new XLSX -> CSV converter  *  * @param pkg The XLSX package to process  * @param output The PrintStream to output the CSV to  * @param minColumns The minimum number of columns to output, or -1 for no minimum  */  public ApacheXLSX2CSV(OPCPackage pkg, PrintStream output, int minColumns) {  this.xlsxPackage = pkg;  this.output = output;  this.minColumns = minColumns;  }   /**  * Parses and shows the content of one sheet  * using the specified styles and shared-strings tables.  *  * @param styles  * @param strings  * @param sheetInputStream  */   public void processSheet(  StylesTable 样式，  ReadOnlySharedStringsTable 字符串，  InputStream sheetInputStream)  throws IOException, ParserConfigurationException, SAXException {  InputSource sheetSource = new InputSource(sheetInputStream);  SAXParserFactory saxFactory = SAXParserFactory.newInstance();  SAXParser saxParser = saxFactory.newSAXParser();  XMLReader sheetParser = saxParser .getXMLReader();  ContentHandler handler = new MyXSSFSheetHandler(styles, strings, this.minColumns, this.output);  sheetParser.setContentHandler(处理程序);  sheetParser.parse(sheetSource);  sheetParser.setContentHandler(处理程序);  sheetParser.parse(sheetSource); 0_d_x00 **  * Initiates the processing of the XLS workbook file to CSV.  *  * @throws IOException  * @throws OpenXML4JException  * @throws ParserConfigurationException  * @throws SAXException  */  public void process()   抛出 IOException，打开XML4JException, ParserConfigurationException, SAXException {  ReadOnlySharedStringsTable strings = new ReadOnlySharedStringsTable(this.xlsxPackage);  XSSFReader xssfReader = new XSSFReader(this.xlsxPackage);  StylesTable styles = xssfReader.getStylesTable();  XSSFReader.SheetIterator iter = (XSSFReader.SheetIterator) xssfReader.getSheetsData();  int index = 0;  而 (iter.hasNext()) {  InputStream stream = iter.next();  String sheetName = iter.getSheetName() ;  this.output.println();  this.output.println(sheetName + " [index=" + index + "]:");  processSheet(样式、字符串、流);  流。 close();  ++index;  }  }  public static void main(String[] args) throws Exception  {  String data/fethworks/fethworks = " converttocsv/data/";  File xlsxFile = new File(dataPath + "workbook.xls");  if (!xlsxFile.exists())  {  System.err.println("未找到或未找到文件：“+ xlsxFile.getPath());  return;  }  int minColumns = -1;  if (args.length >= 2)  minColumns[Inte]( );  // 包打开是瞬间的，它应该是。 ，mincolumns）; _ X000D__X000D_ XLSX2CSV.PROCESS（）; _ X000D__X000D_} _X000D_X000D__X000D__X000D__X000D_ _X000D_ 0761616163481_X000D _ - [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/download/Aspose.Cells_Java_vs_POI_SS_v1.4/Convert.Worksheet.t o.CSV.Aspose.Cells.vs.Apache.POI.SS.zip)  {{% alert color="primary" %}}   有关详细信息，请访问[保存文件](/cells/java/saving-excel-files-to-csv-pdf-and-other-formats00d/)._x {{% /alert %}}