---
title: Konvertera arbetsblad till CSV
type: docs
weight: 30
url: /sv/java/convert-worksheet-to-csv/
---
## **Aspose.Cells - Konvertera kalkylblad till CSV**
Om utvecklare behöver spara sina filer på någon lagringsplats kan de helt enkelt ange filnamnet (med dess fullständiga lagringssökväg) och önskat filformat (med hjälp av**FileFormatType**uppräkning) medan du anropar**spara**metod av**Arbetsbok**objekt.

**Java**

{{< highlight "java" >}}

 //Instantiate a new workbook with Excel file path

Workbook workbook = new Workbook(dataPath + "workbook.xls");

//Save the document in PDF format

workbook.save(dataPath + "AsposeWorkbookCSV.csv", SaveFormat.CSV);

{{< /highlight >}}
## **Apache POI SS - HSSF & XSSF - Konvertera arbetsblad till CSV**
Nedanstående kod visar hur kalkylblad kan konverteras till CSV med Apache POI HSSF och XSSF API jämfört med Aspose.Cells Java API.

**Java**

{{< highlight "java" >}}

 /**

\* En rudimentär XLSX -> CSV-processor modellerad på

\* POI-exempelprogram XLS2CSVmra av Nick Burch från

\* paket org.apache.poi.hssf.eventusermodel.examples.

\* Till skillnad från HSSF-versionen ignorerar denna helt

\* saknade rader.

\* <p/>

\* Datablad läses med en SAX-parser för att behålla

\* minnesfotavtryck relativt litet, så detta borde vara

\* kunna läsa enorma arbetsböcker. Stiltabellen och

\* tabellen med delad sträng måste sparas i minnet. De

\* standard tabellklass för POI-stilar används, men en anpassad

\* (skrivskyddad) klass används för den delade strängtabellen

\* eftersom standard POI SharedStringsTable växer mycket

\* snabbt med antalet unika strängar.

\* <p/>

\* Tack till Eric Smith för en patch som åtgärdar ett problem

\* triggas av celler med flera "t"-element, dvs

\* hur Excel representerar olika format (t.ex. ett ord

\* vanligt och ett ord fetstilt).

\*

\* @författare Chris Lott

*/

public class ApacheXLSX2CSV {  /**  * Typen av datavärde indikeras av ett attribut på cellen.  * Värdet är vanligtvis i ett "v"-element i cellen.___00/0d0d___00d0d0d enum xssfDataType {  BOOL,  ERROR,  FORMULA,  INLINESTR,  SSTINDEX,  NUMBER,  }   /**  * Derived from http://poi.apache.org /spreadsheet/how-to.html#xssf_sax_api  * <p/>  * Se även Standard ECMA-376, 1:a utgåvan, del 4, sidorna 1928ff, atnational. publications/standards/Ecma-376.htm  * <p/>  * En webbvänlig version är http://openiso.org/Ecma/376/Part4  *0dx000d0d_x0d_x0d_x0d_x0d_x0d_x0d_x0d_x0d_x0d_x0d_x0d_x0_0d_00_00_00_0 **  * Tabell med stilar  */  privat te StylesTable stylesTable;  /**  * Table with unique strings  */  private ReadOnlySharedStringsTable sharedStringsTable;  /**  * Destination for data  */  private final PrintStream output;  /* *  * Antal kolumner som ska läsas som börjar med längst till vänster  */  privat final int minColumnCount;  // Ställ in när V startelement seen_0_00 är seen_0d_00 cell seen_0d_00;   // Används när cellstängelement ses. privat int thisColumn = -1;  // Den sista kolumnen skrivs ut till utgången stream  private int lastColumnNumber = -1;  // Gathers characters as they are seen.  private StringBuffer value;  /**  * Accepts objects needed while parsing.  *  * @param styles Table of styles  * @param strings Table of shared strings  * @param cols Minimum number of columns to show  * @param target Sink for output  */  public MyXSSFSheetHandler(  StylesTable styles,  ReadOnlySharedStringsTable strings,  int cols,  PrintStream target) {  this.stylesTable = styles;  this.sharedStringsTable = strings;  this.minColumnCount = cols;  this.output = target;  this.value = new StringBuffer( );  this.nextDataType = xssfDataType.NUMBER;  this.formatter = new DataFormatter();_x000 d_  }  /*  * (icke-Javadoc)  * @see org.xml.sax.helpers.DefaultHandler#startElement(java.lang,lang.lang.String,java.lang.lang.lang.String,java.lang.lang.lang. org.xml.sax.Attributes)  */  public void startElement(String uri, String localName, String name,  Attributes attributes) throws SAXExceptiond_00_0. "v".equals(name)) {  vIsOpen = true;  // Rensa innehållet cache  value.setLength(0); =   // Rensa innehållet cache  value.setLength(0); =  0}_0}_d_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0. är lika med(namn)) {  // Hämta cellens referens  String r = attributes.getValue("r");  int firstDigit = -1; _0;(int = c ); ++c) {  if (Character.isDigit(r.charAt(c))) {  firstDigit = c;  break; _0}_d_0}_d_0}_d_x0}_d 0, firstDigit));  // Set up defaults.  this.nextDataType = xssfDataType.NUMBER;  this.formatIndex = -1;  this.formatString = null;  String cellType = attributes.getValue( "t");  String cellStyleStr = attributes.getValue("s");  if ("b".equals(cellType))  nästaDataType = x_ypssfa_0Data_000;d 0d_ else if ("e".equals(cellType))  nextDataType = xssfDataType.ERROR;  else if ("inlineStr".equals(cellType))0yps.IN ".equals (celltype)) _ x000d_  nextDatatype = xssfdatatype.sstindex;   annars om (" str ". (celltype)) _ x000d_  nextdatatyp // Det är en siffra, men nästan säkert one  // med en speciell stil eller format  int styleIndex = Integer.parseInt(cellStyleStr);  XSSFCellA_stil_stil_stil_stil_0_stil.xd getDataFormat();  this.formatString = style.getDataFormatString();  if (this.formatString == null)  this.formatString = BuiltinFormats.getBuiltinFormat(this.formatIndex);  }  }   _x000 d_ /*  * (icke-Javadoc)  * @see org.xml.sax.helpers.DefaultHandler#endElement(java.lang.String, java.lang.String, java.lang.String)_x000d)_x000d   public void endElement(String uri, String localName, String name)  kastar SAXException {  String thisStr = null;  s /000d_kval. {  // Bearbeta värdeinnehållet efter behov.  // Gör det nu, eftersom tecken() kan kallas mer än en gång  switch (nextDataType) { _x000 första char = _x000 = A );  thisStr = första == '0' ? "FALSE" : "TRUE";  break;  case FEL:  thisStr = "\"FEL:" + value.toString() + '"';  case FEL:  thisStr = "\"FEL:" + value.toString() + '"'; case FOR _x _000d_d_0 / En formel kan resultera i ett strängvärde,  // så lägg alltid till dubbla citattecken.  thisStr = '"' + value.toString() + '"';  break; break; case IN     // TODO: har sett ett exempel på detta, så det är opröstat.  XSSFRichTextString rtsi = new XSSFRichTextString(value.toString()); _x000d" to 'String_xtsi" +String_xtsi;  break;  case SSTINDEX:  String sstIndex = value.toString();  try {  int idx = Integer.parseInt(sstIndex);  XSSFRichTextString rtss = new XSSFRichTextString(sharedStringsTable.getEntryAt(idx)) ;  thisStr = '"' + rtss.toString() + '"';  }  catch (NumberFormatExc eption ex) {  output.println("Det gick inte att analysera SST-index '" + sstIndex + "': " + ex.toString());  _x000 x000_d_x000d0_0_0_0:_x0 fall_nummer _x0_0_0_0_0d:_x0 fall value.toString()  break;   standard:   thisstr = "(TODO: Oväntad typ:" + NextDatatype + ")"; _ x000d_  break;  }}  _ _xd_ / / / / / / / se upp. kommatecken för eventuella fält som saknades på denna rad  if (lastColumnNumber == -1) {  lastColumnNumber = 0;  _d_x _d =int__x för i < denna kolumn; ++i)  output.print(',') lastColumnNumber = thisColumn;  } else if ("row".equals(name)) {  // Skriv ut eventuella saknade kommatecken om det behövs  if (minkolumner _x_0) (minkolumner _x_0) {0_0_0) {0_0 last ColumnNumber == -1) {  lastColumnNumber = 0;  }  för (int i = lastColumnNumber; i < (this.minColumnNumber) {_0;_0 utdata _0;_0'0;_0;_0;   }  // We're onto a new row  output.println();  lastColumnNumber = -1;  }  }  /**  * Captures characters only if a suitable element is open.  * Ursprungligen var det bara "v"; utökad för inlineStr also.  */  public void characters(char[] ch, int start, int length)  kastar SAXException {      _x0_0d_0d_0d_0d_0d_0d_0d_0d_0d_0d_0d_0);  }   /** _ x000d_  *konverterar ett excel-kolumnnamn som "c" till en nollbaserad index.x000d_ *  *@param namn *@return index correspect  privat int nameToColumn(String name) {  int kolumn = -1;  för (int i = 0; i < name.length(); ++i) {  char ;  kolumn = (kolumn + 1) * 26 + c - 'A';  }  returkolumn;  //_x000}_/0}_x000}_/0}__/0}_0}_//0}_x000}_/0}__/0}_0}_/0 //////////////////////  privat OPCPackage xlsxPackage;  privat int minColumns;  privat PrintStream output0d_x0_0d_0 00d_  * Skapar en ny XLSX -> CSV-omvandlare  *  * @param pkg XLSX-paketet för process  * @param utdata 0 CSV-värdet till min_0m_x utdata från CSV till min_0m_x utdata från CSV till min_0m_x utdata från CSV till min_0m_x. -1 for no minimum  */  public ApacheXLSX2CSV(OPCPackage pkg, PrintStream output, int minColumns) {  this.xlsxPackage = pkg;  this.output = output;  this.minColumns = minColumns;  }   /**  * Parses and shows the content of one sheet  * using the specified styles and shared-strings tables.  *  * @param styles  * @param strings  * @param sheetInputStream  */   public void processSheet(  StylesTable styles,  ReadOnlySharedStringsTable-strängar,  InputStream sheet) d_  throws IOException, ParserConfigurationException, SAXException {  InputSource sheetSource = new InputSource(sheetInputStream);  SAXParserFactory saxFactory = SAXParserFactory.newInstance();  SAXParser saxParser = saxFactory.newSAXParser();  XMLReader sheetParser = saxParser.getXMLReader ();  ContentHandler-hanterare = new MyXSSFSheetHandler(stilar, strängar, this.minColumns, this.output);  sheetParser.setContentHandler(hanterare _et0_0__d_0 _etParssheet 0__d _etParssheet 0__d_0 0;   * Initiates the processing of the XLS workbook file to CSV.  *  * @throws IOException  * @throws OpenXML4JException  * @throws ParserConfigurationException  * @throws SAXException  */  public void process()  kastar IOException, OpenXML4JException, ParserConfiguratio nException, SAXException {  ReadOnlySharedStringsTable strings = new ReadOnlySharedStringsTable(this.xlsxPackage);  XSSFReader xssfReader = new XSSFReader(this.xlsxPackage);  StylesTable styles = xssfReader.getStylesTable();  XSSFReader.SheetIterator iter = (XSSFReader .SheetIterator) xssfReader.getSheetsData();  int index = 0;  while (iter.hasNext()) {  Input_Stream0.next_0);  this.output.println();  this.output.println(sheetName + " [index=" + index + "]:");  processSheet(stilar, strängar, ström);_x000d0_ _x0 );  ++index;  }  }  public static void main(String[] args) throws Exception  {  String dataPath = "src/featurescomparison/workingwithworksheets/converttocsv/data/"; _x000d _ File xlsxFile = new File(dataPath + "workbook.xls");  if (!xlsxFile.exists())  {  System.err.println("Nej.fil: funnen eller ej. getPath());  return;  }  int minColumns = -1;  if (args.längd >= 2)__x000ds/Inte _x000ds/Inte _x000ds; Kolumn x000d ==2)_x000ds paketet öppet är omedelbart, som det borde vara.  OPCPackage p = OPCPackage.open(xlsxFile.getPath(), PackageAccess.READ);  ApacheXLSX2CSV xlsx2csv. .process();  }   {{< /highlight >}} ## **Ladda ner körkod** Ladda ner **Konvertera arbetsblad till CSV_x nedan nämnt CSV_x**0 från någon av _d_0 webbplatser:0_d_0 sociala sidor:0 //github.com/aspose-cells/Aspose.Cells-for-Java/releases/download/Aspose.Cells_Java_vs_POI_SS_v1.4/Convert.Worksheet.to.CSV.Aspose.Cells.vs.Apache.POI.SS.zip) _ x000d_ {{% alert color="primary" %}}   För mer information, besök [Spara filer](/cells/java/saving-excel-files-to-csv-pdf-and-other-formats/). _x000_x00_ 4816_