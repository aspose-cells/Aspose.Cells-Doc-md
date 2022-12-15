---
title: Çalışma Sayfasını CSV'ye Dönüştür
type: docs
weight: 30
url: /tr/java/convert-worksheet-to-csv/
---
## **Aspose.Cells - Çalışma Sayfasını CSV'ye Dönüştür**
Geliştiricilerin dosyalarını bir depolama konumuna kaydetmeleri gerekiyorsa, dosya adını (tam depolama yolu ile birlikte) ve istenen dosya biçimini (kullanarak) belirtebilirler.**Dosya Biçimi Türü**numaralandırma) çağrılırken**kaydetmek**yöntemi**Çalışma kitabı**nesne.

**Java**

{{< highlight "java" >}}

 //Instantiate a new workbook with Excel file path

Workbook workbook = new Workbook(dataPath + "workbook.xls");

//Save the document in PDF format

workbook.save(dataPath + "AsposeWorkbookCSV.csv", SaveFormat.CSV);

{{< /highlight >}}
## **Apache POI SS - HSSF & XSSF - Çalışma Sayfasını CSV'ye Dönüştür**
Aşağıdaki kod, çalışma sayfasının Apache POI HSSF ve XSSF API kullanılarak Aspose.Cells Java API ile karşılaştırıldığında nasıl CSV'ye dönüştürülebileceğini gösterir.

**Java**

{{< highlight "java" >}}

 /**

\* İlkel bir XLSX -> CSV işlemcisi

\* POI örnek programı XLS2CSVmra, Nick Burch tarafından

\* org.apache.poi.hssf.eventusermodel.examples paketi.

\* HSSF versiyonundan farklı olarak, bu tamamen yok sayar

\* eksik satırlar.

\* <p/>

\* Veri sayfaları, SAX çözümleyici kullanılarak okunur.

\* bellek alanı nispeten küçük, yani bu olmalı

\* çok büyük çalışma kitaplarını okuyabilir. Stiller tablosu ve

\* paylaşılan dize tablosu bellekte tutulmalıdır. bu

\* standart POI stilleri tablo sınıfı kullanılır, ancak özel

\* (salt okunur) sınıfı, paylaşılan dize tablosu için kullanılır

\* çünkü standart POI SharedStringsTable çok büyür

\* benzersiz dizelerin sayısıyla hızlı bir şekilde.

\* <p/>

\* Bir sorunu çözen yama için Eric Smith'e teşekkürler

\* birden çok "t" öğesi olan hücreler tarafından tetiklenir;

\* Excel'in farklı biçimleri nasıl temsil ettiği (örneğin, bir sözcük

\* düz ve bir kelime kalın).

\*

\* @yazar Chris Lott

*/

public class ApacheXLSX2CSV {  /**  * Veri değerinin türü hücredeki bir öznitelik tarafından belirtilir.  * Değer genellikle hücre içindeki bir "v" öğesindedir.  */  enum xssfDataType {  BOOL,  ERROR,  FORMULA,  INLINESTR,  SSTINDEX,  NUMBER,  }   /**  * Derived from http://poi.apache.org /spreadsheet/how-to.html#xssf_sax_api  * <p/>  * Ayrıca bkz. Standart ECMA-376, 1. baskı, bölüm 4, sayfa 1928ff, at  * http://www.ecma-international.org/ yayınlar/standartlar/Ecma-376.htm  * <p/>  * Web dostu bir sürüm: http://openiso.org/Ecma/376/Part4  */  class MyXSSFSheetHandler _x0d_x00d {_x000d DefaultHandler **  * Stilleri içeren tablo  */  özel te StylesTable stylesTable;  /**  * Table with unique strings  */  private ReadOnlySharedStringsTable sharedStringsTable;  /**  * Destination for data  */  private final PrintStream output;  /* *  * leftmost  */  private final int minColumnCount;  // V start öğesi görüldüğünde ayarla  private boolean vIsOpen; öğesi görüldüğünde set;   // hücre kapanış öğesi görüldüğünde kullanılır. private int thisColumn = -1;  // Çıktıya yazdırılan son sütun Stream  private int lastcolumnnumber = -1;   // karakterleri gördükleri gibi toplar. of styles  * @param strings Table of shared strings  * @param cols Minimum number of columns to show  * @param target Sink for output  */  public MyXSSFSheetHandler(  StylesTable styles,  ReadOnlySharedStringsTable strings,  int cols,   printstream hedef) {  this.stylestable = styles;   this.sharedstringstable = strings; );  this.nextDataType = xssfDataType.NUMBER;  this.formatter = yeni DataFormatter();_x000 d_  }  /*  * (Javadoc dışı)  * @see org.xml.sax.helpers.DefaultHandler#startElement(java.lang.String, java.lang.String, java.lang.String, org.xml.sax.Attributes)  */  public void startElement(String uri, String localName, String name,  Attributes öznitelikleri) SAXException {  if ("inlineStr".equals(ad) || "v".equals(ad)) {  vIsOpen = true;  // İçeriği temizle cache  value.setLength(0);  }  // c => cell  // c => cell _x000 ". else" eşittir(isim)) {  // Hücreyi al reference  String r = nitelikler.getValue("r");  int firstDigit = -1;  for (int c = 0; c < r.uzunluk( ++c) {  if (Character.isDigit(r.charAt(c))) {  firstDigit = c;  break;  }  _sublum name this(rConlum name this.Conlum name this(rConlum name this) 0, firstDigit));  // Varsayılanları ayarla.  this.nextDataType = xssfDataType.NUMBER;  this.formatIndex = -1;  this.formatString = null; Type Celluel öznitelikleri. "t");  Dize cellStyleStr = nitelikler.getValue("s");  if ("b".equals(cellType))  nextDataType = xssfDataType.BOOL; _x00 0d_ else if ("e".equals(cellType))  nextDataType = xssfDataType.ERROR;  else if ("inlineStr".equals(cellType))  nextDataType = xssfDataType.INLINESTR;  if ("s ".equals(cellType))  nextDataType = xssfDataType.SSTINDEX;  else if ("str".equals(cellType))  nextDataType = xssfDataType.FORMULA;  else if (cellStyleStr !=0 boş) {_x0d_0 null) // Bu bir sayıdır, ancak neredeyse kesin olarak one  // özel bir stille veya format  int styleIndex = Integer.parseInt(cellStyleStr);  XSSFCellStyle style = stylesTable.getStyleAt(styleIndex); _formatIndex = style. getDataFormat (); _ x000d_  this.formatstring = style.getdataFormatString (); _ x000d_  if (this.formatstring == null) d_d_d_} _xd_ _xd_ _xd_ _xd_ _xd_ _xds _xds _xds _xd_ _xds _xd_ _xdsetbuiltinformat (this.formatats; _ _x000 d_ /*  * (Javadoc dışı)  * @see org.xml.sax.helpers.DefaultHandler#endElement(java.lang.String, java.lang.String, java.lang.String)  */   public void endElement(String uri, String localName, String name)  throws SAXException {  String thisStr = null;  // v => cell  if ("v".equals(ad)) {  // Değer içeriğini gerektiği gibi işleyin.  // şimdi yapın, çünkü character() birden fazla çağrılabilir  switch (nextDataType) {  case BOOL:  char first = value.charAt(0 );  thisStr = ilk == '0'? "FALSE" : "TRUE";  break;  case HATA:  thisStr = "\"ERROR:" + value.toString() + '"';  break;  case FORMULA00d_x00 / Bir formül, bir dize değeriyle sonuçlanabilir,  // bu nedenle her zaman çift tırnaklı karakterler ekleyin.  thisStr = '"' + value.toString() + '"';  break;  case INLINESTR:  // YAPILACAKLAR: bunun bir örneğini gördük, yani denenmedi.  XSSFRichTextString rtsi = new XSSFRichTextString(value.toString());  thisStr = '"' + rtsi.toString() + '"';  break;  case SSTINDEX:  String sstIndex = value.toString();  try {  int idx = Integer.parseInt(sstIndex);  XSSFRichTextString rtss = new XSSFRichTextString(sharedStringsTable.getEntryAt(idx)) ;  thisStr = '"' + rtss.toString() + '"';  }  catch (NumberFormatExc) eption ex) {  output.println("SST dizini ayrıştırılamadı '" + sstIndex + "': " + ex.toString());  }  break;  vaka NUMBER:  String n = value.toString();  if (this.formatString != null)  thisStr = formatter.formatRawCellContents(Double.parseDouble(n), this.formatIndex, this.formatString);  else 0; thisStr =000d_0; thisStr  break;  default:  thisStr = "(TODO: Unexpected type: " + nextDataType + ")";  break;  }  // Çıktı dizi içeriğini gördükten sonra bu satırda eksik olan alanlar için virgüller   if (lastColumnNumber == -1) {  lastColumnNumber = 0;  }  for (int i = lastColumnNumber; i < thisColumn; ++i)  output.print(',');  // Boş dize olabilir.  output.print(thisStr);  // Sütun  if (thisColumn > -1)  _ lastColumnNumber = thisColumn;  } else if ("row".equals(ad)) {  // Gerekirse eksik virgülleri yazdırın  if (minColumns > 0) {  // Sütunlar 0 tabanlıysa x000d_ lastColumnNumber == -1) {  lastColumnNumber = 0;  }  için (int i = lastColumnNumber; i < (this.minColumnCount); i++) { }d_0 0);_x0   }  // We're onto a new row  output.println();  lastColumnNumber = -1;  }  }  /**  * Captures characters only if a suitable element is open.  * Başlangıçta yalnızca "v" idi; inlineStr için de genişletildi.  */  genel geçersiz karakterler(char[] ch, int start, int length) , SAXException {  if (vIsOpen)  value.append(ch, start, length) atar;  }   /** _ x000d_  *"C" gibi bir Excel sütun adını "C" gibi bir adda dönüştürür.  private int nameToColumn(Dize adı) {  int sütun = -1;  for (int i = 0; i < name.length(); ++i) {  int c = name.charAt(i) ;  sütun = (sütun + 1) * 26 + c - 'A';  }  dönüş sütunu;  }  }  ///////// ///////////////////////  özel OPCPackage xlsxPackage;  özel int minColumns;  özel PrintStream çıkışı;  /**_x0 00d_  * Yeni bir XLSX oluşturur -> CSV converter  *  * @param pkg Process  * @param çıktısı için XLSX paketi CSV'yi  * çıktısı için minimum sütun sayısı veya minimum sütun sayısı @param minColumns -1 for no minimum  */  public ApacheXLSX2CSV(OPCPackage pkg, PrintStream output, int minColumns) {  this.xlsxPackage = pkg;  this.output = output;  this.minColumns = minColumns;  }   /** _ x000d_  * Bir sayfa  * 'nin içeriğini ve paylaşılan telleri kullanarak içeriğini gösterir.   genel geçersiz işlem Sayfası(  StylesTable styles,  ReadOnlySharedStringsTable dizeleri,  InputStream sayfasıInputStream)_x000 d_  throws IOException, ParserConfigurationException, SAXException {  InputSource sheetSource = new InputSource(sheetInputStream);  SAXParserFactory saxFactory = SAXParserFactory.newInstance();  SAXParser saxParser = saxFactory.newSAXParser();  XMLReader sheetParser = saxParser.getXMLReader ();  ContentHandler işleyicisi = new MyXSSFSheetHandler(stilleri, dizeleri, this.minColumns, this.output);  sheetParser.setContentHandler(handler);  sheetParser.parse(sheetSource);    * Initiates the processing of the XLS workbook file to CSV.  *  * @throws IOException  * @throws OpenXML4JException  * @throws ParserConfigurationException  * @throws SAXException  */  public void process()  IOException, OpenXML4JException, ParserConfiguratio atar nException, SAXException {  ReadOnlySharedStringsTable strings = new ReadOnlySharedStringsTable(this.xlsxPackage);  XSSFReader xssfReader = new XSSFReader(this.xlsxPackage);  StylesTable styles = xssfReader.getStylesTable();  XSSFReader.SheetIterator iter = (XSSFReader .SheetIterator) xssfReader.getSheetsData();  int dizini = 0;  while (iter.hasNext()) {  InputStream akışı = iter.next();  String SheetName = iter.x0000()d;  this.output.println();  this.output.println(sheetName + " [index=" + index + "]:");  processSheet(styles, strings, stream);  stream.close( );  ++index;  }  }  public static void main(String[] args) throws Exception  {  String dataPath = "src/featurescomparison/workingwithworksheets/converttocsv/data/"; _x000d _ Dosya xlsxFile = yeni Dosya(dataPath + "workbook.xls");  if (!xlsxFile.exists())  {  System.err.println("Dosya bulunamadı veya yok: " + xlsxFile. getPath());  return;  }  int minColumns = -1;  if (args.length >= 2)  minColumns = Integer.parseInt(x0/00]); _ Thed_parseInt(x0/00]); paket açılışı olması gerektiği gibi anlıktır.  OPCPackage p = OPCPackage.open(xlsxFile.getPath(), PackageAccess.READ);  ApacheXLSX2CSV xlsx2csv = new ApacheXLSX2CSV(p, System.out, minColumns);  xvsx2cs .process();  }   {{< /highlight >}} ## **Çalışma Kodunu İndirin** **Çalışma Sayfasını CSV'ye Dönüştür**'ü aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden indirin:  - [GitHub](https: //github.com/aspose-cells/Aspose.Cells-for-Java/releases/download/Aspose.Cells_Java_vs_POI_SS_v1.4/Convert.Worksheet.to.CSV.Aspose.Cells.vs.Apache.POI.SS.zip)_x00 0d_  {{% alert color="primary" %}}   Daha fazla ayrıntı için [Dosyaları Kaydetme](/cells/java/saving-excel-files-to-csv-pdf-and-other-formats/).  {{% /alert %}} adresini ziyaret edin.