---
title: Convertir hoja de trabajo a CSV
type: docs
weight: 30
url: /es/java/convert-worksheet-to-csv/
---
## **Aspose.Cells - Convertir hoja de trabajo a CSV**
Si los desarrolladores necesitan guardar sus archivos en alguna ubicación de almacenamiento, simplemente pueden especificar el nombre del archivo (con su ruta de almacenamiento completa) y el formato de archivo deseado (usando el**Tipo de formato de archivo**enumeración) mientras llama al**ahorrar**método de**Libro de trabajo**objeto.

**Java**

{{< highlight "java" >}}

 //Instantiate a new workbook with Excel file path

Workbook workbook = new Workbook(dataPath + "workbook.xls");

//Save the document in PDF format

workbook.save(dataPath + "AsposeWorkbookCSV.csv", SaveFormat.CSV);

{{< /highlight >}}
## **Apache POI SS - HSSF y XSSF - Convertir hoja de trabajo a CSV**
El siguiente código muestra cómo la hoja de trabajo se puede convertir a CSV usando Apache POI HSSF y XSSF API en comparación con Aspose.Cells Java API.

**Java**

{{< highlight "java" >}}

 /**

\* Un procesador rudimentario XLSX -> CSV modelado en el

\* Programa de muestra POI XLS2CSVmra de Nick Burch de la

\* paquete org.apache.poi.hssf.eventusermodel.examples.

\* A diferencia de la versión HSSF, esta ignora por completo

\* filas faltantes.

\* <p/>

\* Las hojas de datos se leen usando un analizador SAX para mantener la

\* huella de memoria relativamente pequeña, por lo que debería ser

\* capaz de leer libros de trabajo enormes. La tabla de estilos y

\* la tabla de cadenas compartidas debe mantenerse en la memoria. Él

\* se utiliza la clase de tabla de estilos de puntos de interés estándar, pero

La clase \* (solo lectura) se usa para la tabla de cadenas compartida

\* porque el POI SharedStringsTable estándar crece mucho

\* rápidamente con el número de cadenas únicas.

\* <p/>

\* Gracias a Eric Smith por un parche que soluciona un problema

\* activado por celdas con múltiples elementos "t", que es

\* cómo Excel representa diferentes formatos (p. ej., una palabra

\* simple y una palabra en negrita).

\*

\* @autor Chris Lott

*/

public class ApacheXLSX2CSV {  /**  * El tipo de valor de datos se indica mediante un atributo en la celda.  * El valor suele estar en un elemento "v" dentro de la celda.  */  enum xssfDataType {  BOOL,  ERROR,  FORMULA,  INLINESTR,  SSTINDEX,  NUMBER,  }   /**  * Derived from http://poi.apache.org /spreadsheet/how-to.html#xssf_sax_api  * <p/>  * Consulte también el estándar ECMA-376, 1.ª edición, parte 4, páginas 1928ff, at  * http://www.ecma-international.org/ publicaciones/standards/Ecma-376.htm  * <p/>  * Una versión compatible con la web es http://openiso.org/Ecma/376/Part4  */  class MyXSSFSheetHandler extends DefaultHandler0_d _x000 **  * Tabla con estilos  */  priva te StylesTable stylesTable;  /**  * Table with unique strings  */  private ReadOnlySharedStringsTable sharedStringsTable;  /**  * Destination for data  */  private final PrintStream output;  /* *  * Número de columnas para leer comenzando con el más a la izquierda  */  private final int minColumnCount;  // Se establece cuando se ve el elemento de inicio V  private boolean vIsOpen;_x000d0_ _ _ Se establece cuando se ve el elemento de inicio de celda _X000D_ _X000D_ // Usado cuando el elemento de cierre de la celda se ve._X000D_ _X000D_ Private XSSFDATAType NextDatatype; _X000D_ _X000D_ // Usado para formatear valores de celda numeric._X000D_  private private int thisColumn = -1;  // La última columna impresa en la salida stream  private int LastColumnnumber = -1; _X000D_ _X000D_ // Los caracteres de Gathers como se ven. of styles  * @param strings Table of shared strings  * @param cols Minimum number of columns to show  * @param target Sink for output  */  public MyXSSFSheetHandler(  StylesTable styles,  ReadOnlySharedStringsTable strings,  int cols,  PrintStream destino) {  this.stylesTable = estilos;  this.sharedStringsTable = cadenas;  this.minColumnCount = cols;  this.output =0d;_x00value =0_d String _x00value );  this.nextDataType = xssfDataType.NUMBER;  this.formatter = new DataFormatter();_x000 d_  }  /*  * (no Javadoc)  * @ver org.xml.sax.helpers.DefaultHandler#startElement(java.lang.String, java.lang.String, java.lang.String, org.xml.sax.Attributes)  */  public void startElement(String uri, String localName, String name,  Attributes atributos) arroja SAXException {  if ("inlineStr".equals(name) || "v".equals(name)) {  vIsOpen = true;  // Borrar contenido cache  value.setLength(0);  }  // c => cell __ else if ("dx000". equals(name)) {  // Obtenga la referencia de celda  String r = atributos.getValue("r");  int firstDigit = -1;  for (int c = 0; c < r.length( ); ++c) {  if (Character.isDigit(r.charAt(c))) {  firstDigit = c;  break;  }  } _sublumn0 =(TorColumn0 0, firstDigit));  // Configurar valores predeterminados.  this.nextDataType = xssfDataType.NUMBER;  this.formatIndex = -1;  this.formatString = null; _x000d._get String cellType atributos( "t");  String cellStyleStr = atributos.getValue("s");  if ("b".equals(cellType))  nextDataType = xssfDataType.BOOL; _x00 0d_ else if ("e".equals(cellType))  nextDataType = xssfDataType.ERROR;  else if ("inlineStr".equals(cellType))  nextDataType = xssfDataType.INLINESTR;  else if ("s ".equals(cellType))  nextDataType = xssfDataType.SSTINDEX;  else if ("str".equals(cellType))  nextDataType = xssfDataType.FORMULA;  else if (cellStyleStr_d _x00d_0) { // Es un número, pero casi seguro uno  // con un estilo o formato especial  int styleIndex = Integer.parseInt(cellStyleStr);  XSSFCellStyle style = stylesTable.getStyleAt(styleIndex);  this.formatIndex = style. getDataFormat();  this.formatString = style.getDataFormatString();  if (this.formatString == null)  this.formatString = BuiltinFormats.getBuiltinFormat(this.formatIndex);  }  }  } _x000 */   public void endElement(String uri, String localName, String name)  throws SAXException {  String thisStr = null;  // v => contenido de una celda  if ("v".equals(name)) {  // Procese el contenido del valor según sea necesario.  // Hágalo ahora, ya que se puede llamar a characters() más de una vez  switch (nextDataType) {  case BOOL:  char first = value.charAt(0 );  thisStr = primero == '0' ? "FALSO" : "VERDADERO";  break;  case ERROR:  thisStr = "\"ERROR:" + value.toString() + '"';  break;  case 0FORMULAd:_x0 / Una fórmula podría dar como resultado un valor de cadena,   // así que siempre agregue caracteres de comillas dobles.  thisStr = '"' + value.toString() + '"';  break;  case INLINESTR:  // TODO: he visto un ejemplo de esto, por lo que no se ha probado.  XSSFRichTextString rtsi = new XSSFRichTextString(value.toString());  thisStr = '"' + rtsi.toString() + '"';  break;  case SSTINDEX:  String sstIndex = value.toString();  try {  int idx = Integer.parseInt(sstIndex);  XSSFRichTextString rtss = new XSSFRichTextString(sharedStringsTable.getEntryAt(idx)) ;  thisStr = '"' + rtss.toString() + '"';  }  catch (NumberFormatExc epción ex) {  salida.println("Error al analizar el índice SST '" + sstIndex + "': " + ex.toString());  }  break;  NÚMERO de caso: _x000 value.toString();  if (this.formatString != null)  thisStr = formatter.formatRawCellContents(Double.parseDouble(n), this.formatIndex, this.formatString);  else  thisStr = 0_n;  break;  default:  thisStr = "(TODO: tipo inesperado: " + nextDataType + ")";  break;  }  // Salida después de haber visto el contenido de la cadena_x00000_d //_0x0000_d comas para los campos que faltaban en esta fila  if (lastColumnNumber == -1) {  lastColumnNumber = 0;  }  for (int i = lastColumnNumber; i <estaColumna; ++i)  output.print(',');  // Podría ser la cadena vacía.  output.print(thisStr);  // Actualizar columna  si (thisColumn > -1) _x000 lastColumnNumber = thisColumn;  } else if ("row".equals(name)) {  // Imprima las comas que faltan si es necesario  if (minColumns > 0) {  // Las columnas están basadas en 0_x000d0_ _x último número de columna == -1) {  último número de columna = 0;  }  for (int i = último número de columna; i < (this.minColumnCount); i++) {  salida.print(',');    }  // We're onto a new row  output.println();  lastColumnNumber = -1;  }  }  /**  * Captures characters only if a suitable element is open.  * Originalmente era solo "v"; extendido para inlineStr también.  */  public void characters(char[] ch, int start, int length)  throws SAXException {  if (vIsOpen)  value.append(ch, start, length);   }  /**  * Converts an Excel column name like "C" to a zero-based index.  *  * @param name  * @return Index corresponding to the specified name  */  private int nameToColumn(String nombre) {  int columna = -1;  for (int i = 0; i < nombre.longitud(); ++i) {  int c = nombre.charAt(i) ;  columna = (columna + 1) * 26 + c - 'A';  }  volver columna;  }  } _x000///////////////////////////////////////////////////////// /////////////////////////  private OPCPackage xlsxPackage;  private int minColumns;  private PrintStream salida;  /**_x0 00D_ _X000D_ * Crea un nuevo XLSX -> CSV converter  *   * @param pkg el XLSX paquete a procesos  * @param salida la salida a la salida de XLSX a procesos -1 for no minimum  */  public ApacheXLSX2CSV(OPCPackage pkg, PrintStream output, int minColumns) {  this.xlsxPackage = pkg;  this.output = output;  this.minColumns = minColumns;  }   /**  * Parses and shows the content of one sheet  * using the specified styles and shared-strings tables.  *  * @param styles  * @param strings  * @param sheetInputStream  */   public void processSheet(  StylesTable estilos,  ReadOnlySharedStringsTable cadenas,  InputStream sheetInputStream)  throws IOException, ParserConfigurationException, SAXException {  InputSource sheetSource = new InputSource(sheetInputStream);  SAXParserFactory saxFactory = SAXParserFactory.newInstance();  SAXParser saxParser = saxFactory.newSAXParser();  XMLReader sheetParser = saxParser .getXMLReader();  ContentHandler handler = new MyXSSFSheetHandler(estilos, cadenas, this.minColumns, this.output);  sheetParser.setContentHandler(handler);  sheetParser.parse(sheetSource);_x000x0_ _0_0_d0} **  * Initiates the processing of the XLS workbook file to CSV.  *  * @throws IOException  * @throws OpenXML4JException  * @throws ParserConfigurationException  * @throws SAXException  */  public void process()   lanza IOException, Abrir XML4JException, ParserConfigurationException, SAXException {  ReadOnlySharedStringsTable strings = new ReadOnlySharedStringsTable(this.xlsxPackage);  XSSFReader xssfReader = new XSSFReader(this.xlsxPackage);  StylesTable styles = xssfReader.getStylesTable();  XSSFReader.SheetIterator iter = (XSSFReader.SheetIterator) xssfReader.getSheetsData();  int index = 0;  while (iter.hasNext()) {  InputStream stream = iter.next();  String sheetName = iter.getSheetName() ;  this.output.println();  this.output.println(sheetName + " [index=" + index + "]:");  processSheet(estilos, cadenas, secuencia);  secuencia. close();  ++index;  }  }  public static void main(String[] args) throws Exception  { workwithparisson/features =s string/workwith/features converttocsv/data/";  File xlsxFile = new File(dataPath + "workbook.xls");  if (!xlsxFile.exists())  {  System.err.println("No encontrado o no un archivo: " + xlsxFile.getPath());  return;  }  int minColumns = -1;  if (args.length >= 2)  minColumns[arg.parse1 = Int );  // La apertura del paquete es instantánea, como debe ser.  OPCPackage p = OPCPackage.open(xlsxFile.getPath(), PackageAccess.READ);  ApacheXLSX2CSV xlsx2csv = new ApacheXLSX2CSV(p, System.out , mincolumns); _ x000d_  xlsx2csv.process (); _ x000d_ }    {{< /highlight >}} ## ** Descargar el código ** _ x000d_ Descargar ** convert sheetsheet a 07617 - [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/download/Aspose.Cells_Java_vs_POI_SS_v1.4/Convert.Worksheet.t o.CSV.Aspose.Cells.vs.Apache.POI.SS.zip)  {{% alert color="primary" %}}   Para obtener más detalles, visite [Guardar archivos](/cells/java/guardar-archivos-de-excel-en-csv-pdf-y-otros-formatos/_d)._x0 {{% /alert %}}