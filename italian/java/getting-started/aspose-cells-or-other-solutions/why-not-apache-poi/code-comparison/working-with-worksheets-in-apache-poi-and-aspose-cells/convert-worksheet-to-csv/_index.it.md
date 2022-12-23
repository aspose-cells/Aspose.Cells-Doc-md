---
title: Converti foglio di lavoro in CSV
type: docs
weight: 30
url: /it/java/convert-worksheet-to-csv/
---
## **Aspose.Cells - Converti foglio di lavoro in CSV**
Se gli sviluppatori devono salvare i propri file in una posizione di archiviazione, possono semplicemente specificare il nome del file (con il relativo percorso di archiviazione completo) e il formato del file desiderato (utilizzando il**FileFormatType**enumerazione) mentre si chiama il**Salva**metodo di**Cartella di lavoro**oggetto.

**Java**

{{< highlight "java" >}}

 //Instantiate a new workbook with Excel file path

Workbook workbook = new Workbook(dataPath + "workbook.xls");

//Save the document in PDF format

workbook.save(dataPath + "AsposeWorkbookCSV.csv", SaveFormat.CSV);

{{< /highlight >}}
## **Apache POI SS - HSSF e XSSF - Converti foglio di lavoro in CSV**
Il codice seguente mostra come il foglio di lavoro può essere convertito in CSV utilizzando Apache POI HSSF e XSSF API rispetto a Aspose.Cells Java API.

**Java**

{{< highlight "java" >}}

 /**

\* Un rudimentale processore XLSX -> CSV modellato sul

\* Programma di esempio POI XLS2CSVmra di Nick Burch dal

\* pacchetto org.apache.poi.hssf.eventusermodel.examples.

\* A differenza della versione HSSF, questa la ignora completamente

\* righe mancanti.

\* <p/>

\* Le schede tecniche vengono lette utilizzando un parser SAX per conservare i file

\* footprint di memoria relativamente piccolo, quindi dovrebbe essere così

\* in grado di leggere enormi cartelle di lavoro. La tabella degli stili e

\* la tabella delle stringhe condivise deve essere tenuta in memoria. Il

\* Viene utilizzata la classe della tabella degli stili POI standard, ma viene utilizzata una classe personalizzata

La classe \* (sola lettura) viene utilizzata per la tabella delle stringhe condivise

\* perché lo standard POI SharedStringsTable cresce molto

\* rapidamente con il numero di stringhe univoche.

\* <p/>

\* Grazie a Eric Smith per una patch che risolve un problema

\* attivato da celle con più elementi "t", ovvero

\* come Excel rappresenta diversi formati (ad esempio, una parola

\* semplice e una parola in grassetto).

\*

\* @autore Chris Lott

*/

public class ApacheXLSX2CSV {  /**  * Il tipo di valore dei dati è indicato da un attributo sulla cella.  * Il valore si trova solitamente in un elemento "v" all'interno della cella.  */  enum xssfDataType {  BOOL,  ERROR,  FORMULA,  INLINESTR,  SSTINDEX,  NUMBER,  }   /**  * Derived from http://poi.apache.org /spreadsheet/how-to.html#xssf_sax_api  * <p/>  * Vedi anche Standard ECMA-376, 1a edizione, parte 4, pagine 1928ff, at  * http://www.ecma-international.org/ publishings/standards/Ecma-376.htm  * <p/>  * Una versione web-friendly è http://openiso.org/Ecma/376/Part4  */  class MyXSSFSheetHandler extends DefaultHandler {_ / **  * Tabella con stili  */  priva te StylesTable stylesTable;  /**  * Table with unique strings  */  private ReadOnlySharedStringsTable sharedStringsTable;  /**  * Destination for data  */  private final PrintStream output;  /* *  * Numero di colonne da leggere a partire dalla più a sinistra  */  private final int minColumnCount;  // Imposta quando viene visualizzato l'elemento iniziale V  private boolean vIsOpen;  // Imposta quando viene visualizzato l'elemento iniziale V    // used when cell close element is seen.  private xssfDataType nextDataType;  // Used to format numeric cell values.  private short formatIndex;  private String formatString;  private final DataFormatter formatter;  private int thisColumn = -1;  // L'ultima colonna stampata nell'output stream  private int lastColumnNumber = -1;  // Raccoglie i caratteri così come vengono visualizzati.  private StringBuffer value;  /**  * Accetta gli oggetti necessari durante l'analisi._x0 *d *00d_ _x0 _0parad__ of styles  * @param strings Table of shared strings  * @param cols Minimum number of columns to show  * @param target Sink for output  */  public MyXSSFSheetHandler(  StylesTable styles,  ReadOnlySharedStringsTable strings,  int cols,  PrintStream target) {  this.stylesTable = styles;  this.sharedStringsTable = strings;  this.minColumnCount = cols;  new. =output = target;_x0ffer_ this. );  this.nextDataType = xssfDataType.NUMBER;  this.formatter = new DataFormatter();_x000 d_  }  /*  * (non Javadoc)  * @see org.xml.sax.helpers.DefaultHandler#startElement(java.lang.String, java.lang.String, java.lang.String, org.xml.sax.Attributes)  */  public void startElement(String uri, String localName, String name,  Attributes attribute) genera SAXException {  if ("inlineStr".equals(name) || "v".equals(nome)) {  vIsOpen = true;  // Cancella contenuti cache  value.setLength(0);  }  // c => cell_x000".d_  else if ("c" equals(name)) {  // Ottieni il riferimento della cella  String r = attribute.getValue("r");  int firstDigit = -1;  for (int c = 0; c < r.length( ); ++c) {  if (Character.isDigit(r.charAt(c))) {  firstDigit = c;  break;  }  } _x000d name = thissubColumn(thissubColumn(r 0, firstDigit));  // Imposta valori predefiniti.  this.nextDataType = xssfDataType.NUMBER;  this.formatIndex = -1;  this.formatString = null; get Stringa attributi cella = "t");  Stringa cellStyleStr = attribute.getValue("s");  if ("b".equals(cellType))  nextDataType = xssfDataType.BOOL; _x00 0d_ else if ("e".equals(cellType))  nextDataType = xssfDataType.ERROR;  else if ("inlineStr".equals(cellType))  nextDataType = xssfDataType.INLINESTR;  else if ("s ".equals(cellType))  nextDataType = xssfDataType.SSTINDEX;  else if ("str".equals(cellType))  nextDataType = xssfDataType.FORMULA;  else if (cellStyleStr != null) {_ // È un numero, ma quasi certamente one  // con uno stile speciale o format  int styleIndex = Integer.parseInt(cellStyleStr);  XSSFCellStyle style = stylesTable.getStyleAt(styleIndex);  this.formatIndex = style. getDataFormat (); _ x000d_  this.formatString = style.getDataFormatString (); _ x000d_  if (this.formatString == null)   this.getString = builtinformats.getBuiltInFormAt (this.c000; } _x000 d_ /*  * (non Javadoc)  * @see org.xml.sax.helpers.DefaultHandler#endElement(java.lang.String, java.lang.String, java.lang.String)  */   public void endElement(String uri, String localName, String name)  throws SAXException {  String thisStr = null;  // v => contenuto di una cella  if ("v.equals(name)) {  // Elabora il contenuto del valore come richiesto.  // Eseguire ora, poiché characters() può essere chiamato più di una volta  switch (nextDataType) {  case BOOL:  char first = value.charAt(0 );  thisStr = primo == '0' ? "FALSO" : "VERO";  break;  case ERRORE:  thisStr = "\"ERRORE:" + value.toString() + '"';  break;  case FORMULA:  /x000d_ / Una formula potrebbe risultare in un valore stringa,  // quindi aggiungi sempre le virgolette doppie.  thisStr = '"' + value.toString() + '"';  break;  case INLINESTR:  // TODO: ne ho visto un esempio, quindi non è stato testato.  XSSFRichTextString rtsi = new XSSFRichTextString(value.toString());  thisStr = '"' + rtsi.toString() + '"';  break;  case SSTINDEX:  String sstIndex = value.toString();  try {  int idx = Integer.parseInt(sstIndex);  XSSFRichTextString rtss = new XSSFRichTextString(sharedStringsTable.getEntryAt(idx)) ;  thisStr = '"' + rtss.toString() + '"';  }  catch (NumberFormatExc eption ex) {  output.println("Impossibile analizzare l'indice SST '" + sstIndex + "': " + ex.toString());  }  break;  case NUMBER:  Stringa n = value.toString();  if (this.formatString != null)  thisStr = formatter.formatRawCellContents(Double.parseDouble(n), this.formatIndex, this.formatString);  else  thisStr = n;__x000d  break;  default:  thisStr = "(TODO: tipo inaspettato: " + nextDataType + ")";  break;  }  // Output dopo aver visto il contenuto della stringa  /x000d_ virgole per i campi mancanti in questa riga  if (lastColumnNumber == -1) {  lastColumnNumber = 0;  }  for (int i = lastColumnNumber; i < thisColumn; ++i)  output.print(',');  // Potrebbe essere la stringa vuota.  output.print(thisStr);  // Aggiorna colonna  if (thisColumn > -1)  lastColumnNumber = thisColumn;  } else if ("row".equals(name)) {  // Stampa eventuali virgole mancanti se necessario  if (minColumns > 0) {  // Le colonne sono basate su 0  if ( lastColumnNumber == -1) {  lastColumnNumber = 0;  }  for (int i = lastColumnNumber; i < (this.minColumnCount); i++) {  output.print(','); _x0}  }   // siamo su un nuovo row  output.println (); _ x000d_  ultimacolumnumber = -1;  *_ _} _} _S000D_ _ #. open.  * Originariamente era solo "v"; esteso anche per inlineStr.  */  public void characters(char[] ch, int start, int length)  throws SAXException {  if (vIsOpen)  value.append(ch, start, length);   }  /**  * Converte un nome di colonna Excel come "C" in un indice a base zero.  *  * @param name  * @return * Indice corrispondente al nome specificato_00dx000  private int nameToColumn(String name) {  int column = -1;  for (int i = 0; i < name.length(); ++i) {  int c = name.charAt(i) ;  colonna = (colonna + 1) * 26 + c - 'A';  }  ritorno colonna;  }  }  /////////// //////////////////////////  private OPCPackage xlsxPackage;  private int minColumns;  private PrintStream output;  /**_x0 00d_  * crea un nuovo XLSX -> CSV Converter  *   * @param pkg il pacchetto XLSX su elaborare il pacchetto di elabora  @param su output del 07616161616161616161616161616161616161613 -1 for no minimum  */  public ApacheXLSX2CSV(OPCPackage pkg, PrintStream output, int minColumns) {  this.xlsxPackage = pkg;  this.output = output;  this.minColumns = minColumns;  }   /**  * Parses and shows the content of one sheet  * using the specified styles and shared-strings tables.  *  * @param styles  * @param strings  * @param sheetInputStream  */   public void processSheet(  StylesTable styles,  ReadOnlySharedStringsTable strings,  InputStream sheetInputStream)  throws IOException, ParserConfigurationException, SAXException {  InputSource sheetSource = new InputSource(sheetInputStream);  SAXParserFactory saxFactory = SAXParserFactory.newInstance();  SAXParser saxParser = saxFactory.newSAXParser();  XMLReader sheetParser = saxParser .getXMLReader();  ContentHandler handler = new MyXSSFSheetHandler(styles, strings, this.minColumns, this.output);  sheetParser.setContentHandler(handler);  sheetParser.parse(sheetSource); _x00_x0d_0 } **  * Initiates the processing of the XLS workbook file to CSV.  *  * @throws IOException  * @throws OpenXML4JException  * @throws ParserConfigurationException  * @throws SAXException  */  public void process()   genera IOException, Open XML4JException, ParserConfigurationException, SAXException {  ReadOnlySharedStringsTable strings = new ReadOnlySharedStringsTable(this.xlsxPackage);  XSSFReader xssfReader = new XSSFReader(this.xlsxPackage);  StylesTable styles = xssfReader.getStylesTable();  XSSFReader.SheetIterator iter = (XSSFReader.SheetIterator) xssfReader.getSheetsData();  int index = 0;  while (iter.hasNext()) {  InputStream stream = iter.next();  String sheetName = iter.getSheetName() ;  this.output.println();  this.output.println(sheetName + " [index=" + index + "]:");  processSheet(styles, strings, stream);  stream. close();  ++index;  }  }  public static void main(String[] args) getta Exception  {  String dataPath = "src/featuresworkconfronts converttocsv/data/";  File xlsxFile = new File(dataPath + "workbook.xls");  if (!xlsxFile.exists())  {  System.err.println("Non trovato o non un file: " + xlsxFile.getPath());  return;  }  int minColumns = -1;  if (args.length >= 2)  minColumns = Integer.parse1]t(args[Int] );  // L'apertura del pacchetto è istantanea, come dovrebbe essere.  OPCPackage p = OPCPackage.open(xlsxFile.getPath(), PackageAccess.READ);  ApacheXLSX2CSV xlsx2csv = new ApacheXLSX2CSV(p, System.out , minColumns);  xlsx2csv.process();  }   {{< /highlight >}} ## **Scarica il codice di esecuzione** Scarica **Converti foglio di lavoro in CSV**0 00 da uno qualsiasi dei seguenti siti: d_x _x - [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/download/Aspose.Cells_Java_vs_POI_SS_v1.4/Convert.Worksheet.t o.CSV.Aspose.Cells.vs.Apache.POI.SS.zip)  {{% alert color="primary" %}}   Per maggiori dettagli, visita [Salvataggio dei file](/cells/java/saving-excel-files-to-csv-pdf-and-other-formats/).__  {{% /alert %}}