---
title: Konvertieren Sie das Arbeitsblatt in CSV
type: docs
weight: 30
url: /de/java/convert-worksheet-to-csv/
---
## **Aspose.Cells - Konvertieren Sie das Arbeitsblatt in CSV**
Wenn Entwickler ihre Dateien an einem Speicherort speichern müssen, können sie einfach den Dateinamen (mit vollständigem Speicherpfad) und das gewünschte Dateiformat (unter Verwendung der**Dateiformattyp**Aufzählung) beim Aufrufen der**speichern**Methode von**Arbeitsmappe**Objekt.

**Java**

{{< highlight "java" >}}

 //Instantiate a new workbook with Excel file path

Workbook workbook = new Workbook(dataPath + "workbook.xls");

//Save the document in PDF format

workbook.save(dataPath + "AsposeWorkbookCSV.csv", SaveFormat.CSV);

{{< /highlight >}}
## **Apache POI SS - HSSF & XSSF - Konvertieren Sie das Arbeitsblatt in CSV**
Der folgende Code zeigt, wie das Arbeitsblatt mit Apache POI HSSF und XSSF API in CSV konvertiert werden kann, im Vergleich zu Aspose.Cells Java API.

**Java**

{{< highlight "java" >}}

 /**

\* Ein rudimentärer XLSX -> CSV Prozessor nach Vorbild des

\* POI-Beispielprogramm XLS2CSVmra von Nick Burch aus der

\* Paket org.apache.poi.hssf.eventusermodel.examples.

\* Im Gegensatz zur HSSF-Version ignoriert diese vollständig

\* fehlende Zeilen.

\* <p/>

\* Datenblätter werden mit einem SAX-Parser gelesen, um die

\* Speicherbedarf relativ klein, also sollte das sein

\* in der Lage, riesige Arbeitsmappen zu lesen. Die Stiltabelle und

\* Die Shared-String-Tabelle muss im Speicher gehalten werden. Das

\* Standard-POI-Stiltabellenklasse wird verwendet, aber eine benutzerdefinierte

\* (schreibgeschützte) Klasse wird für die gemeinsam genutzte Zeichenfolgentabelle verwendet

\* weil die Standard POI SharedStringsTable sehr wächst

\* schnell mit der Anzahl der eindeutigen Zeichenfolgen.

\* <p/>

\* Danke an Eric Smith für einen Patch, der ein Problem behebt

\* ausgelöst durch Zellen mit mehreren "t"-Elementen, das heißt

\* wie Excel verschiedene Formate darstellt (z. B. ein Wort

\* einfach und ein Wort fett).

\*

\* @Autor Chris Lott

*/

öffentliche Klasse ApacheXLSX2CSV {  /**  * Der Typ des Datenwerts wird durch ein Attribut in der Zelle angegeben.  * Der Wert befindet sich normalerweise in einem "v"-Element innerhalb der Zelle.  */  enum xssfDataType {  BOOL,  ERROR,  FORMULA,  INLINESTR,  SSTINDEX,  NUMBER,  }   /**  * Derived from http://poi.apache.org /spreadsheet/how-to.html#xssf_sax_api  * <p/>  * Siehe auch Standard ECMA-376, 1. Ausgabe, Teil 4, Seiten 1928ff, at  * http://www.ecma-international.org/ publications/standards/Ecma-376.htm  * <p/>  * Eine webfreundliche Version ist http://openiso.org/Ecma/376/Part4  */  Klasse MyXSSFSheetHandler erweitert DefaultHandler {d **  * Tabelle mit Stilen  */  privat te StylesTable stylesTable;  /**  * Table with unique strings  */  private ReadOnlySharedStringsTable sharedStringsTable;  /**  * Destination for data  */  private final PrintStream output;  /* *  * Anzahl der zu lesenden Spalten, beginnend mit ganz links  */  private final int minColumnCount;  // Gesetzt, wenn V-Startelement gesehen wird  private boolean vIsOpen; _x0 Gesetzt // Startd0, wenn Zelle0d0 gesehen wird;   // verwendet, wenn das Zellschließelement zu sehen ist. private int thisColumn = -1;  // Die letzte Spalte, die an die Ausgabe ausgegeben wird stream  private int lastcolumnnumber = -1;   // sammelt Zeichen, wie sie gesehen werden. of styles  * @param strings Table of shared strings  * @param cols Minimum number of columns to show  * @param target Sink for output  */  public MyXSSFSheetHandler(  StylesTable styles,  ReadOnlySharedStringsTable strings,  int Spalten,  PrintStream-Ziel) {  this.stylesTable = Stile;  this.sharedStringsTable = Zeichenfolgen;  this.minColumnCount = Spalten;  this.output = Ziel;_x0d_Bux0.0 neu = Zeichenfolge );  this.nextDataType = xssfDataType.NUMBER;  this.formatter = new DataFormatter();_x000 d_  }  /*  * (Nicht-Javadoc)  * @see org.xml.sax.helpers.DefaultHandler#startElement(java.lang.String, java.lang.String, java.lang.String, org.xml.sax.Attributes)  */  public void startElement(String uri, String localName, String name,  Attribute attributes) löst SAXException {  if ("inlineStr".equals(name) || "v".equals(name)) {  vIsOpen = true;  // Inhalte löschen cache  value.setLength(0);  }  // c => cell else. equals(name)) {  // Hole die Zellreferenz  String r = attributes.getValue("r");  int firstDigit = -1;  for (int c = 0; c < r.length( ); ++c) {  if (Character.isDigit(r.charAt(c))) {  firstDigit = c;  break;  }  }  name(r.substring. 0, firstDigit));  // Standardwerte einrichten.  this.nextDataType = xssfDataType.NUMBER;  this.formatIndex = -1;  this.formatString = null; get String(Attribute = cellType "t");  String cellStyleStr = attributes.getValue("s");  if ("b".equals(cellType))  nextDataType = xssfDataType.BOOL; _x00 0d_ else if ("e".equals(cellType))  nextDataType = xssfDataType.ERROR;  else if ("inlineStr".equals(cellType))  nextDataType = xssfDataType.INLINESTR;  else if ("s ".equals(cellType))  nextDataType = xssfDataType.SSTINDEX;  else if ("str".equals(cellType))  nextDataType = xssfDataType.FORMULA;  else if (cellStr_x00 _x00) {cellStr _x00) // Es ist eine Zahl, aber ziemlich sicher eine  // mit einem speziellen Stil oder Format  int styleIndex = Integer.parseInt(cellStyleStr);  XSSFCellStyle style = stylesTable.getStyleAt(styleIndex);  this.formatIndex = style. getDataFormat();  this.formatString = style.getDataFormatString();  if (this.formatString == null)  this.formatString = BuiltinFormats.getBuiltinFormat(this.formatIndex);  }_x00d_ _x0 _d0 _x0 _d0 } _x000 d_ /*  * (Nicht-Javadoc)  * @see org.xml.sax.helpers.DefaultHandler#endElement(java.lang.String, java.lang.String, java.lang.String)  */   public void endElement(String uri, String localName, String name)  löst SAXException aus {  String thisStr = null;  // v => Inhalt einer Zelle  if ("v".equals(name)) {  // Werteinhalte nach Bedarf verarbeiten.  // Jetzt tun, da characters() mehrfach aufgerufen werden darf  switch (nextDataType) {  case BOOL:  char first = value.charAt(0 );  thisStr = first == '0' ? "FALSE" : "TRUE";  break;  case ERROR:  thisStr = "\"ERROR:" + value.toString() + '"';  break;  case 0 / Eine Formel könnte zu einem Stringwert führen,  // also immer doppelte Anführungszeichen hinzufügen.  thisStr = '"' + value.toString() + '"';  break;  case INLINESTR:  // TODO: Ich habe ein Beispiel dafür gesehen, also ist es ungetestet.  XSSFRichTextString rtsi = new XSSFRichTextString(value.toString());  thisStr = '"' + rtsi.toString() + '"';  break;  case SSTINDEX:  String sstIndex = value.toString();  try {  int idx = Integer.parseInt(sstIndex);  XSSFRichTextString rtss = new XSSFRichTextString(sharedStringsTable.getEntryAt(idx)) ;  thisStr = '"' + rtss.toString() + '"';  }  catch (NumberFormatExc eption ex) {  output.println("Fehler beim Parsen des SST-Index '" + sstIndex + "': " + ex.toString());  }  break;  case NUMBER: _x00d_ String n = 0.d_ value.toString();  if (this.formatString != null)  thisStr = formatter.formatRawCellContents(Double.parseDouble(n), this.formatIndex, this.formatString);  else  thisStr0 = 0d_x00  break;  default:  thisStr = "(TODO: Unexpected type: " + nextDataType + ")";  break;  }  // Ausgabe nachdem wir den String-Inhalt gesehen haben _x0 // Ausgabe, nachdem wir den Inhalt der Zeichenfolge gesehen haben _d0 // Kommas für fehlende Felder in dieser Zeile  if (lastColumnNumber == -1) {  lastColumnNumber = 0;  }  for (int i = lastColumnNumber; i < dieseSpalte; ++i)  output.print(',');  // Könnte der leere String sein.  lastColumnNumber = thisColumn;  } else if ("row".equals(name)) {  // Gegebenenfalls fehlende Kommas ausgeben  if (minColumns > 0) {  // Spalten basieren auf 0 (000d_  lastColumnNumber == -1) {  lastColumnNumber = 0;  }  for (int i = lastColumnNumber; i < (this.minColumnCount); i++) {  output.print(',');_x00d_ 00d_  }   // Wir sind auf einem neuen row  output.println (); _ x000d_ x000dx000dx000dx000dx000dx000dx000dx000dx000dx000dx000dx000dx000dx000dx000dx000dx000dx000dx000dx000dx000dx000d_x000ds. open.  * Ursprünglich nur "v"; erweitert für inlineStr also.  */  public void characters(char[] ch, int start, int length)  löst SAXException {  if (vIsOpen)  value.append(ch, start, length);  }   /** _ x000d_   private int nameToColumn(String name) {  int column = -1;  for (int i = 0; i < name.length(); ++i) {  int c = name.charAt(i) ;  Spalte = (Spalte + 1) * 26 + c - 'A';  }  Rückgabespalte;  }  } _x000d/ ///// ///// ////////////////////////  private OPCPackage xlsxPackage;  private int minColumns;  private PrintStream-Ausgabe;  /**_x0 00d_  * Creates a new XLSX -> CSV converter  *  * @param pkg The XLSX package to process  * @param output The PrintStream to output the CSV to  * @param minColumns The minimum number of columns to output, or -1 for no minimum  */  public ApacheXLSX2CSV(OPCPackage pkg, PrintStream output, int minColumns) {  this.xlsxPackage = pkg;  this.output = output;  this.minColumns = minColumns;  }   /**  * Parses and shows the content of one sheet  * using the specified styles and shared-strings tables.  *  * @param styles  * @param strings  * @param sheetInputStream  */   public void processSheet(  StylesTable-Stile,   ReadOnlySharedStringsTable-Strings,   InputStream sheetInputStream)  throws IOException, ParserConfigurationException, SAXException {  InputSource sheetSource = new InputSource(sheetInputStream);  SAXParserFactory saxFactory = SAXParserFactory.newInstance();  SAXParser saxParser = saxFactory.newSAXParser();  XMLReader sheetParser = saxParser .getXMLReader();  ContentHandler Handler = new MyXSSFSheetHandler(styles, strings, this.minColumns, this.output);  sheetParser.setContentHandler(handler);  sheetParser.parse(sheetSource);_x0 _x0 _d 00}0 **  * Initiates the processing of the XLS workbook file to CSV.  *  * @throws IOException  * @throws OpenXML4JException  * @throws ParserConfigurationException  * @throws SAXException  */  public void process()   löst IOException, Open aus XML4JException, ParserConfigurationException, SAXException {  ReadOnlySharedStringsTable strings = new ReadOnlySharedStringsTable(this.xlsxPackage);  XSSFReader xssfReader = new XSSFReader(this.xlsxPackage);  StylesTable styles = xssfReader.getStylesTable();  XSSFReader.SheetIterator iter = (XSSFReader.SheetIterator) xssfReader.getSheetsData();  int index = 0;  while (iter.hasNext()) {  InputStream stream = iter.next();  String sheetName = iter.getSheetName() ;  this.output.println();  this.output.println(sheetName + " [index=" + index + "]:");  processSheet(styles, strings, stream);  stream. close();  ++index;  }  }  public static void main(String[] args) throws Exception  { rc String data/path = "comparisonsfeatures/ature converttocsv/data/";  File xlsxFile = new File(dataPath + "workbook.xls");  if (!xlsxFile.exists())  {  System.err.println("Not found or not eine Datei: " + xlsxFile.getPath());  return;  }  int minColumns = -1;  if (args.length >= 2)  minColumns = Integer.pars[1] ). , minColumns);   xlsx2csv.process();  }   {{< /highlight >}} ## - [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/download/Aspose.Cells_Java_vs_POI_SS_v1.4/Convert.Worksheet.t o.CSV.Aspose.Cells.vs.Apache.POI.SS.zip)  {{% alert color="primary" %}}   Weitere Informationen finden Sie unter [Speichern von Dateien](/cells/java/saving-excel-files-to-csv-pdf-and-other-formats0d_x00/)._x0d_x0 {{% /alert %}}