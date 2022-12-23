---
title: Преобразовать рабочий лист в CSV
type: docs
weight: 30
url: /ru/java/convert-worksheet-to-csv/
---
## **Aspose.Cells - преобразовать рабочий лист в CSV**
Если разработчикам необходимо сохранить свои файлы в каком-либо месте хранения, они могут просто указать имя файла (с указанием полного пути к нему) и желаемый формат файла (используя параметр**FileFormatType**перечисление) при вызове**спасти**метод**Рабочая тетрадь**объект.

**Java**

{{< highlight "java" >}}

 //Instantiate a new workbook with Excel file path

Workbook workbook = new Workbook(dataPath + "workbook.xls");

//Save the document in PDF format

workbook.save(dataPath + "AsposeWorkbookCSV.csv", SaveFormat.CSV);

{{< /highlight >}}
## **Apache POI SS — HSSF и XSSF — преобразование рабочего листа в CSV**
В приведенном ниже коде показано, как рабочий лист можно преобразовать в CSV с помощью Apache POI HSSF и XSSF API по сравнению с Aspose.Cells Java API.

**Java**

{{< highlight "java" >}}

 /**

\* Элементарный процессор XLSX -> CSV по образцу

\* Образец программы POI XLS2CSVmra Ника Берча из

\* пакет org.apache.poi.hssf.eventusermodel.examples.

\* В отличие от версии HSSF, эта полностью игнорирует

\* пропущенные строки.

\* <р/>

\* Листы данных считываются с помощью синтаксического анализатора SAX, чтобы сохранить

\* объем памяти относительно небольшой, так что это должно быть

\* способен читать огромные рабочие тетради. Таблица стилей и

\* таблица разделяемых строк должна храниться в памяти.

\* используется стандартный класс таблицы стилей POI, но пользовательский

\* (только для чтения) класс используется для общей таблицы строк

\* потому что стандартная POI SharedStringsTable сильно разрастается

\* быстро с количеством уникальных строк.

\* <р/>

\* Спасибо Эрику Смиту за патч, исправляющий проблему

\* запускается ячейками с несколькими элементами "t", т.е.

\* как Excel представляет разные форматы (например, одно слово

\* простой и одно слово жирным шрифтом).

\*

\* @author Крис Лотт

*/

public class ApacheXLSX2CSV {  /**  * Тип значения данных указывается атрибутом в ячейке.  * Значение обычно находится в элементе "v" внутри ячейки.  */  enum xssfDataType {  BOOL,  ERROR,  FORMULA,  INLINESTR,  SSTINDEX,  NUMBER,  }   /**  * Derived from http://poi.apache.org /spreadsheet/how-to.html#xssf_sax_api  * <p/>  * См. также стандарт ECMA-376, 1-е издание, часть 4, страницы 1928ff, at  * http://www.ecma-international.org/ публикации/стандарты/Ecma-376.htm  * <p/>  * Веб-версия http://openiso.org/Ecma/376/Part4  */  class MyXSSFSheetHandler extends _x00d_ **  * Таблица со стилями  */  priva te StylesTable stylesTable;  /**  * Table with unique strings  */  private ReadOnlySharedStringsTable sharedStringsTable;  /**  * Destination for data  */  private final PrintStream output;  /* *  * Количество столбцов для чтения, начиная с крайнего левого  */  private final int minColumnCount;  // Устанавливается при просмотре начального элемента V  private boolean vIsOpen; cell Set set;   // используется, когда виден элемент закрытия ячейки. private int thisColumn = -1;  // Последний столбец, напечатанный на выходе Stream  private int intcolumnnumber = -1;   // Собегивает символы, как они видят. of styles  * @param strings Table of shared strings  * @param cols Minimum number of columns to show  * @param target Sink for output  */  public MyXSSFSheetHandler(  StylesTable styles,  ReadOnlySharedStringsTable strings,  int cols,   printstream target) {  this.stylestable = styles;   this.sharedStringstable = strings;   this.mincolumncount = cols;   this. );  this.nextDataType = xssfDataType.NUMBER;  this.formatter = new DataFormatter();_x000 d_  }  /*  * (не-Javadoc)  * @see org.xml.sax.helpers.DefaultHandler#startElement(java.lang.String, java.lang.String, java.lang.String, org.xml.sax.Attributes)  */  public void startElement(String uri, String localName, String name,   Атрибуты атрибутов) throws SAXException {  if ("inlineStr".equals(name) || "v".equals(name)) {  vIsOpen = true;  // Очистить содержимое cache  value.setLength(0);  }  // c => cell (" else"). equals(name)) {  // Получить ссылку на ячейку   String r = attribute.getValue("r");  int firstDigit = -1;  for (int c = 0; c < r.length( ); ++c) {  if (Character.isDigit(r.charAt(c))) {  firstDigit = c;  break;  }  }  } thissubnameTo(Columndstr._ _x000 0, firstDigit));  // Установить значения по умолчанию.  this.nextDataType = xssfDataType.NUMBER;  this.formatIndex = -1;  this.formatString = null;  атрибуты ячейки "t");  String cellStyleStr = attribute.getValue("s");  if ("b".equals(cellType))  nextDataType = xssfDataType.BOOL; _x00 0d_ else if ("e".equals(cellType))  nextDataType = xssfDataType.ERROR;  else if ("inlineStr".equals(cellType))  nextDataType = xssfDataType.INLINESTR;  else if ("s ".equals(cellType))  nextDataType = xssfDataType.SSTINDEX;  else if ("str".equals(cellType))  nextDataType = xssfDataType.FORMULA;  else if (cellStyleStr x0_00d !=0 null) {_d_00d_0_0 null) // Это число, но почти наверняка one  // со специальным стилем или форматом  int styleIndex = Integer.parseInt(cellStyleStr);  XSSFCellStyle style = stylesTable.getStyleAt(styleIndex); = styleIndex.format.format. getDataFormat (); _ x000d_  this.formatString = style.getDataFormatString (); _ x000d_  if (this.formatstring == null)   this.formatstring = buildinformats.getbuiltinformat (this.formAtex); } _x000 d_ /*  * (не-Javadoc)  * @see org.xml.sax.helpers.DefaultHandler#endElement(java.lang.String, java.lang.String, java.lang.String)  */   public void endElement(String uri, String localName, String name)  throws SAXException {  String thisStr = null;  // v => содержимое ячейки  if ("v".equals(name)) {  // Обработайте содержимое значения по мере необходимости.   // Сделайте сейчас, так как character() может вызываться более одного раза );  thisStr = first == '0' ? "ЛОЖЬ" : "ИСТИНА";  break;  case ERROR:  thisStr = "\"ERROR:" + value.toString() + '"';  break; /x000d_x0 case FORMULA:__dx0 / Результатом формулы может быть строковое значение,   // поэтому всегда добавляйте символы в двойных кавычках.  thisStr = '"' + value.toString() + '"';  break;  case INLINESTR:  // TODO: видел пример этого, поэтому он не проверен.  break;  case SSTINDEX:  String sstIndex = value.toString();  try {  int idx = Integer.parseInt(sstIndex);  XSSFRichTextString rtss = new XSSFRichTextString(sharedStringsTable.getEntryAt(idx)) ;  thisStr = '"' + rtss.toString() + '"';  }  catch (NumberFormatExc eption ex) {  output.println("Не удалось проанализировать индекс SST '" + sstIndex + "': " + ex.toString());  }  break;  case NUMBER: _x000d = _ value.toString();  if (this.formatString != null)  thisStr = formatter.formatRawCellContents(Double.parseDouble(n), this.formatIndex, this.formatString);  else  thisS0 = 0n  break;  default:  thisStr = "(TODO: Unexpected type: " + nextDataType + ")";  break;  }  } 0 // Вывод после того, как мы увидели строку contents_0d_x0d_0 // запятые для любых полей, которые отсутствовали в этой строке   if (lastColumnNumber == -1) {  lastColumnNumber = 0;  }  for (int i = lastColumnNumber; я < эта колонка; ++i)  output.print(',');  // Может быть пустой строкой.  output.print(thisStr);  // Обновить столбец  if (thisColumn > -1) _x0000d_  lastColumnNumber = thisColumn;  } else if ("row".equals(name)) {  // При необходимости распечатать все пропущенные запятые  if (minColumns > 0) {  // Столбцы равны 0 base  if ( lastColumnNumber == -1) {  lastColumnNumber = 0;  }  for (int i = lastColumnNumber; i < (this.minColumnCount); i++) {  output.print(',');  }  }   // Мы на новом ROW_X000D_ _X000D_ output.println (); _ x000d_  LastColumnnumb open.  * Первоначально было просто "v"; расширен для inlineStr также.  }   /** _ x000d_  *преобразует имя столбца Excel, подобное «C» в индекс на основе нуля.  private int nameToColumn (имя строки) {  int column = -1;   for (int i = 0; i < name.length(); ++i) {  int c = name.charAt(i) ;  столбец = (столбец + 1) * 26 + c - 'A';  }  столбец возврата;  }  }_x000d/////////////////////////////////////////////////////////////////////////////////////// ////////////////////////  private OPCPackage xlsxPackage;  private int minColumns;  private PrintStream output;  /**_x0 00d_  * Создает новый XLSX -> CSV Converter  *   * @param pkg the XLSX TORCEST_X000D_  * @Param Выходной -1 for no minimum  */  public ApacheXLSX2CSV(OPCPackage pkg, PrintStream output, int minColumns) {  this.xlsxPackage = pkg;  this.output = output;  this.minColumns = minColumns;  }   /** _ x000d_  * Диаграммы и показывает содержимое One Sheet  * Использование указанных стилей и таблиц Share-strings.  *   * @param styles_0000d_bliing_ @paramd_slists @pal_bliings @pal_ weled_bliings @pal_bliings @pal_bliings @pal_bliings @pal_ wispli_ wispl_bliings.   public void processSheet(  StylesTable styles,   ReadOnlySharedStringsTable strings,   InputStream sheetInputStream)  throws IOException, ParserConfigurationException, SAXException {  InputSource sheetSource = new InputSource(sheetInputStream);  SAXParserFactory saxFactory = SAXParserFactory.newInstance();  SAXParser saxParser = saxFactory.newSAXParser();  XMLReader sheetParser = saxParser .getXmlReader (); _ x000d_  contentHandler handler = new Myxssfsheethandler (styles, Strings, this.mincolumns, this.output); _ x000d_  sheateparser.setcontenthandler (handler); _ x000d_  setail.SerseNTENTENTERTENTERNTENTERNENTENTENTENTENTENTENTENTENTERSE (HANDLER); **  * Initiates the processing of the XLS workbook file to CSV.  *  * @throws IOException  * @throws OpenXML4JException  * @throws ParserConfigurationException  * @throws SAXException  */  public void process()   выдает IOException, Open XML4JException, ParserConfigurationException, SAXException {  ReadOnlySharedStringsTable strings = new ReadOnlySharedStringsTable(this.xlsxPackage);  XSSFReader xssfReader = new XSSFReader(this.xlsxPackage);  StylesTable styles = xssfReader.getStylesTable();  XSSFReader.SheetIterator iter = (XSSFReader.SheetIterator) xssfReader.getSheetsData();  int index = 0;  while (iter.hasNext()) {  InputStream stream = iter.next();_x000Shed_  String sheetName = iter.get.get ;  this.output.println();  this.output.println(sheetName + " [index=" + index + "]:");  processSheet(стили, строки, поток);  поток. close();  ++index;  }  }  public static void main(String[] args) throws Exception  {    String dataPathing = " converttocsv/data/";  File xlsxFile = new File(dataPath + "workbook.xls");  if (!xlsxFile.exists())  {  System.err.println("Не найдено или нет файл: " + xlsxFile.getPath());  return;  }  int minColumns = -1;  if (args.length >= 2)  minColumns = Integer.parseInt] );  // Пакет открывается мгновенно, как и должно быть. , mincolumns); _ x000d_  xlsx2csv.process (); _ x000d_ }    {{< /highlight >}} ## ** Загрузка. - [GitHub] (https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/download/Aspose.Cells_Java_vs_POI_SS_v1.4/Convert.Worksheet.t o.CSV.Aspose.Cells.vs.Apache.POI.SS.zip)  {{% alert color="primary" %}}   Дополнительные сведения см. на странице [Сохранение файлов](/cells/java/saving-excel-files-to-csv-pdf-and-0d_other-formats/).__x00d {{% /alert %}}