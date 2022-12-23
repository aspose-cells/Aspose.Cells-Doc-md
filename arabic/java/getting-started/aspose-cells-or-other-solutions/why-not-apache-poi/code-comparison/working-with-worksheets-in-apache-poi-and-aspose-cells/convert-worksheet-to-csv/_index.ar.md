---
title: تحويل ورقة العمل إلى CSV
type: docs
weight: 30
url: /ar/java/convert-worksheet-to-csv/
---
## **Aspose.Cells - تحويل ورقة العمل إلى CSV**
إذا احتاج المطورون إلى حفظ ملفاتهم في بعض مواقع التخزين ، فيمكنهم ببساطة تحديد اسم الملف (بمسار التخزين الكامل) وتنسيق الملف المطلوب (باستخدام**نوع الملف**تعداد) أثناء استدعاء**حفظ**طريقة**دفتر العمل**موضوع.

**Java**

{{< highlight "java" >}}

 //Instantiate a new workbook with Excel file path

Workbook workbook = new Workbook(dataPath + "workbook.xls");

//Save the document in PDF format

workbook.save(dataPath + "AsposeWorkbookCSV.csv", SaveFormat.CSV);

{{< /highlight >}}
## **Apache POI SS - HSSF & XSSF - تحويل ورقة العمل إلى CSV**
يوضح الكود أدناه كيف يمكن تحويل ورقة العمل إلى CSV باستخدام Apache POI HSSF و XSSF API مقارنة بـ Aspose.Cells Java API.

**Java**

{{< highlight "java" >}}

 /**

\ * معالج بدائي XLSX -> CSV مصمم على طراز

\ * برنامج عينة POI XLS2CSVmra بواسطة Nick Burch من

\ * package org.apache.poi.hssf.eventusermodel.examples.

* على عكس إصدار HSSF ، يتجاهل هذا الإصدار تمامًا

\ * صفوف مفقودة.

\ * <p />

\ * تتم قراءة أوراق البيانات باستخدام محلل SAX للاحتفاظ بملحق

\ * مساحة الذاكرة صغيرة نسبيًا ، لذا يجب أن يكون هذا

\ * قادر على قراءة مصنفات هائلة. جدول الأنماط و

\ * يجب الاحتفاظ بجدول السلسلة المشتركة في الذاكرة. ال

\ * يتم استخدام فئة جدول أنماط POI القياسية ، ولكنها مخصصة

يتم استخدام فئة \ * (للقراءة فقط) لجدول السلسلة المشتركة

\ * لأن POI SharedStringsTable القياسي ينمو بشكل كبير

\ * بسرعة مع عدد السلاسل الفريدة.

\ * <p />

\ * شكرا لإريك سميث على التصحيح الذي يصلح مشكلة

\ * يتم تشغيلها بواسطة خلايا بها عناصر "t" متعددة ، وهي

\ * كيف يمثل Excel تنسيقات مختلفة (على سبيل المثال ، كلمة واحدة

\ * عادي وكلمة واحدة جريئة).

\*

\ * @ المؤلف كريس لوت

*/

فئة عامة ApacheXLSX2CSV {  / ** _ x000d_  * تتم الإشارة إلى نوع قيمة البيانات بواسطة سمة على الخلية. enum xssfDataType {  BOOL،   ERROR،   FORMULA،   INLINESTR،   SSTINDEX،  _x000_000_000_xdoi_doi_000x /spreadsheet/how-to.html#xssf_sax_api  * <p /> _ x000d_  * انظر أيضًا المعيار ECMA-376 ، الإصدار الأول ، الجزء 4 ، الصفحات 1928ff ، at  * http://www.ecma-international.org/ المنشورات / المعايير / Ecma-376.htm  * <p /> _ x000d_  * الإصدار الملائم للويب هو http://openiso.org/Ecma/376/Part4  * / _ x000d_  class MyXSSFSheetHandler {extends_andler / ** _ x000d_  * الجدول مع الأنماط  * / _ x000d_  priva te StylesTable StylesTable؛   / ** _ x000d_  * جدول مع سلاسل فريدة  * / _ x000d_  خاص للقراءة OnlySharedStringsTable SharedStringsTable ؛   / ** _d000_d_dream * *   * عدد الأعمدة المراد قراءتها بدءًا من أقصى اليسار  * / _ x000d_  الخاص النهائي int minColumnCount ؛   // تعيين وقت رؤية عنصر البداية V  عنصر منطقي خاص vIsOpen _x000_   // يُستخدم عند رؤية عنصر إغلاق الخلية.   خاص xssfDataType nextDataType ؛   // يُستخدم لتنسيق قيم الخلايا الرقمية. خاص int thisColumn = -1 ؛   // العمود الأخير المطبوع على الإخراج stream  private int lastColumnNumber = -1 ؛   // يجمع الأحرف كما يتم رؤيتها. of styles  *param strings جدول السلاسل المشتركة   *param cols الحد الأدنى لعدد الأعمدة المراد إظهارها  *param target Sink for output  * / _ x000d_ Starx000_dles_dings_000 ، int cols،   PrintStream target) {  this.stylesTable = Styles؛   this.sharedStringsTable = strings؛   this.minColumnCount = cols؛  _x000 = this.vue. )؛ _ x000d_  this.nextDataType = xssfDataType.NUMBER؛   this.formatter = new DataFormatter ()؛ _ x000 d_ }   / * _ x000d_  * (non-Javadoc)   * @ see org.xml.sax.helpers.DefaultHandler # startElement (java.lang.String، java.lang.String.String، java.lang.String، java. org.xml. "v" .equals (name)) {  vIsOpen = true؛   // مسح محتويات ذاكرة التخزين المؤقت  value.setLength (0) ؛ _ x000d_ }   // c => cell_x000. يساوي (الاسم)) {  // احصل على مرجع الخلية  String r = attributes.getValue ("r") ؛ _ x000d_  int firstDigit = -1 ؛   لـ (int c = 0 ؛ c <r.length ("r") )؛ ++ c) {  if (Character.isDigit (r.charAt (c))) {  firstDigit = c؛   break؛  }  umn (x000d_olxing.umn = 0، firstDigit))؛ _ x000d_  // إعداد الإعدادات الافتراضية. "t") ؛ _ x000d_  String cellStyleStr = attributes.getValue ("s") ؛ _ x000d_  if ("b" .equals (cellType)) _ x000d_  nextDataType = xssfDataType.BOOL؛  _x00 0d_ else if ("e" .equals (cellType)) _ x000d_  nextDataType = xssfDataType.ERROR؛   else if ("inlineStr" .equals (cellType)) _ x000d_  nextDataType = xssfDataType.INES ".equals (cellType)) _ x000d_  nextDataType = xssfDataType.SSTINDEX؛   else if (" str ".equals (cellType)) _ x000d_  nextDataType = xssfDataType.FORMULA cell _x000_ else _x000d // إنه رقم ، ولكن من المؤكد تقريبًا أن one  // بنمط خاص أو تنسيق  int styleIndex = Integer.parseInt (cellStyleStr) ؛ _ x000d_  XSSFCellStyle style = stylesTable.getStyleAt (style_dex_000. getDataFormat ()؛ _ x000d_  this.formatString = style.getDataFormatString ()؛ _ x000d_  if (this.formatString == null)   this.formatString = BuiltinFormats.getBuiltinFormat (this.dd000_000} _dd_000} }  _x000 d_ / * _ x000d_  * (non-Javadoc)   *see org.xml.sax.helpers.DefaultHandler # endElement (java.lang.String، java.lang.String، java.lang.String)     endElement عام باطل (String uri، String localName، String name)   يطرح SAXException {  String thisStr = null؛   // v => محتويات خلية _x000 ". {  // معالجة محتويات القيمة على النحو المطلوب.   // افعل الآن ، حيث يمكن استدعاء الأحرف () أكثر من مرة  switch (nextDataType) {  case BOOL:   char أولاً = value.charAt (0 ) ؛ _ x000d_  thisStr = الأول == '0'؟ "FALSE": "TRUE"؛ _ x000d_  break؛   case ERROR:   thisStr = "\" ERROR: "+ value.toString () + '"'؛   break؛  _M_000x_d_country / يمكن أن ينتج عن الصيغة قيمة سلسلة ،   // لذا أضف دائمًا أحرف اقتباس مزدوجة.  // TODO: لقد رأيت مثالًا على ذلك ، لذلك لم يتم اختباره.   XSSFRichTextString rtsi = جديد XSSFRichTextString (value.toString ()) ؛ _ x000d_  thisStr = '"" + rtsi.toString () +' "  break؛   case SSTINDEX:   String sstIndex = value.toString ()؛ _ x000d_  try {  int idx = Integer.parseInt (sstIndex) ؛   thisStr = "" + rtss.toString () + '"'؛  }   catch (NumberFormatExc الاستقبال) {  output.println ("فشل تحليل فهرس SST '" + sstIndex + "':" + ex.toString ()) ؛ _ x000d_ }   break ؛   casering NUMBER: _x000_d_ _x value.toString () ؛ _ x000d_  if (this.formatString! = null)   thisStr = formatter.formatRawCellContents (Double.parseDouble (n)، this.formatIndex، this.formatString)؛ _ x000d_ Str000 = nx000d_  break؛  _ افتراضي:   thisStr = "(TODO: نوع غير متوقع:" + nextDataType + ")"؛ _ x000d_  break؛  }   // Output بعد أن رأينا محتوى السلسلة_000 فواصل لأي حقول كانت مفقودة في هذا الصف   if (lastColumnNumber == -1) {  lastColumnNumber = 0 ؛  }   لـ (int i = lastColumnNumber ؛ أنا <هذا العمود ؛ ++ i)   output.print ('،')؛ _ x000d_  // قد تكون السلسلة الفارغة. lastColumnNumber = thisColumn؛  } else if ("row" .equals (name)) {  // اطبع أي فاصلات مفقودة إذا لزم الأمر  if (minColumns> 0) {  // Column_d_000_d lastColumnNumber == -1) {  lastColumnNumber = 0؛  }   لـ (int i = lastColumnNumber؛ i <(this.minColumnCount)؛ i ++) {  output.000؛  }   // نحن في صف جديد  output.println () ؛ _ x000d_  lastColumnNumber = -1 ؛  }  } عنصر مناسب فقط ifx000d_  open.  * في الأصل كانت "v" فقط ؛ ممتد لـ inlineStr أيضًا.   * / _ x000d_  أحرف الفراغ العامة (char [] ch ، int start ، int length)   يطرح SAXException {  if (vIsOpen)   value.append)  }   / ** _ x000d_  * يحول اسم عمود Excel مثل "C" إلى فهرس صفري.  private int nameToColumn (اسم السلسلة) {  int العمود = -1 ؛   لـ (int i = 0 ؛ i <name.length () ؛ ++ i) {  int c = name.charAt (i) ؛   العمود = (العمود + 1) * 26 + ج - "أ" ؛ _ x000d_ }   عمود الإرجاع ؛  }  }   /////////////// ////////////////////////// _ x000d_  خاص OPCPackage xlsxPackage ؛   private int minColumns ؛   إخراج PrintStream الخاص ؛   / ** _ x0 00d_  * ينشئ XLSX جديدًا -> CSV converter  *   *param pkg الحزمة XLSX to process  *param output يقوم PrintStream بإخراج الحد الأدنى لعدد الأعمدة من CSV to_x -1 لعدم وجود حد أدنى   * / _ x000d_  ApacheXLSX2CSV (OPCPackage pkg، إخراج PrintStream، int minColumns) {  this.xlsxPackage = pkg؛   this.oldout_000؛   / ** _ x000d_  * يوزع ويظهر محتوى ورقة واحدة  * باستخدام الأنماط المحددة وجداول السلاسل المشتركة.   ورقة عملية عامة باطلة (  أنماط الجدول ،   ReadOnlySharedStringsTable strings ،   InputStream sheetInputStream)  throws IOException, ParserConfigurationException, SAXException {  InputSource sheetSource = new InputSource(sheetInputStream);  SAXParserFactory saxFactory = SAXParserFactory.newInstance();  SAXParser saxParser = saxFactory.newSAXParser();  XMLReader sheetParser = saxParser .getXMLReader ()؛ _ x000d_  ContentHandler handler = new MyXSSFSheetHandler (الأنماط ، السلاسل ، this.minColumns ، this.output) ؛ _ x000d_  sheetParser.setContentHandler (handler) ؛ _ x000d_  sheet_dse_000. **  * Initiates the processing of the XLS workbook file to CSV.  *  * @throws IOException  * @throws OpenXML4JException  * @throws ParserConfigurationException  * @throws SAXException  */  public void process()   يلقي IOException ، Open XML4JException, ParserConfigurationException, SAXException {  ReadOnlySharedStringsTable strings = new ReadOnlySharedStringsTable(this.xlsxPackage);  XSSFReader xssfReader = new XSSFReader(this.xlsxPackage);  StylesTable styles = xssfReader.getStylesTable();  XSSFReader.SheetIterator iter = (XSSFReader.SheetIterator) xssfReader.getSheetsData () ؛ _ x000d_  int index = 0 ؛   while (iter.hasNext ()) {  InputStream stream = iter.next () ؛ _ x000d_name) . close ()؛ _ x000d_  ++ index؛  }  }   main (String [] args) يطرح Exception  {  String dataPathworkets = "working / converttocsv / data / "؛ _ x000d_  File xlsxFile = ملف جديد (dataPath +" workbook.xls ") ؛ _ x000d_  if (! xlsxFile.exists ()) _ x000d_  {  System.err.println (" ملف: "+ xlsxFile.getPath ()) ؛ _ x000d_  return ؛  }   int minColumns = -1 ؛   if (args.length> = 2)   mings.Int (1) ) ؛ _ x000d_  // فتح الحزمة فوري ، كما ينبغي أن يكون. ، minColumns)؛ _ x000d_  xlsx2csv.process ()؛ _ x000d_ }    {{< /highlight >}} ## ** قم بتنزيل كود التشغيل ** _ x000d_ تنزيل ** تحويل ورقة العمل أدناه إلى CSV_d ** - [GitHub] (https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/download/Aspose.Cells_Java_vs_POI_SS_v1.4/Convert.Worksheet.t o.CSV.Aspose.Cells.vs.Apache.POI.SS.zip)   {{% alert color="primary" %}}   لمزيد من التفاصيل ، تفضل بزيارة [حفظ الملفات] (/ cells / java / save-excel-files-to-csv-pdf-and-other-format /)._d_d_ _x {{% /alert %}}