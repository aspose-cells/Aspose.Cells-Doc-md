---
title: Convertir la feuille de calcul en CSV
type: docs
weight: 30
url: /fr/java/convert-worksheet-to-csv/
---
## **Aspose.Cells - Convertir la feuille de calcul en CSV**
Si les développeurs ont besoin d'enregistrer leurs fichiers dans un emplacement de stockage, ils peuvent simplement spécifier le nom du fichier (avec son chemin de stockage complet) et le format de fichier souhaité (en utilisant le**TypeFormatFichier**énumération) en appelant le**sauvegarder**méthode de**Cahier**objet.

**Java**

{{< highlight "java" >}}

 //Instantiate a new workbook with Excel file path

Workbook workbook = new Workbook(dataPath + "workbook.xls");

//Save the document in PDF format

workbook.save(dataPath + "AsposeWorkbookCSV.csv", SaveFormat.CSV);

{{< /highlight >}}
## **Apache POI SS - HSSF & XSSF - Convertir la feuille de calcul en CSV**
Le code ci-dessous montre comment la feuille de calcul peut être convertie en CSV en utilisant Apache POI HSSF et XSSF API par rapport à Aspose.Cells Java API.

**Java**

{{< highlight "java" >}}

 /**

\* Un processeur rudimentaire XLSX -> CSV calqué sur le

\* Exemple de programme POI XLS2CSVmra par Nick Burch du

\* package org.apache.poi.hssf.eventusermodel.examples.

\* Contrairement à la version HSSF, celle-ci ignore complètement

\* lignes manquantes.

\* <p/>

\* Les fiches techniques sont lues à l'aide d'un analyseur SAX pour conserver

\* empreinte mémoire relativement petite, donc cela devrait être

\* capable de lire d'énormes classeurs. La table des styles et

\* la table de chaînes partagées doit être conservée en mémoire. Le

\* la classe de table de styles de POI standard est utilisée, mais une

La classe \* (lecture seule) est utilisée pour la table de chaînes partagées

\* parce que le POI standard SharedStringsTable se développe très

\* rapidement avec le nombre de chaînes uniques.

\* <p/>

\* Merci à Eric Smith pour un correctif qui corrige un problème

\* déclenché par des cellules avec plusieurs éléments "t", ce qui est

\* comment Excel représente différents formats (par exemple, un mot

\* clair et un mot en gras).

\*

\* @auteur Chris Lott

*/

public class ApacheXLSX2CSV {  /**  * Le type de la valeur de données est indiqué par un attribut sur la cellule.  * La valeur est généralement dans un élément "v" dans la cellule.  */  enum xssfDataType {  BOOL,  ERROR,  FORMULA,  INLINESTR,  SSTINDEX,  NUMBER,  }   /**  * Derived from http://poi.apache.org /spreadsheet/how-to.html#xssf_sax_api  * <p/>  * Voir également la norme ECMA-376, 1ère édition, partie 4, pages 1928ff, at  * http://www.ecma-international.org/ publications/standards/Ecma-376.htm  * <p/>  * Une version adaptée au Web est http://openiso.org/Ecma/376/Part4  */  class MyXSSFSheetHandler étend DefaultHandler {_x000d **  * Tableau avec styles  */  priva te StylesTable stylesTable;  /**  * Table with unique strings  */  private ReadOnlySharedStringsTable sharedStringsTable;  /**  * Destination for data  */  private final PrintStream output;  /* *  * Nombre de colonnes à lire en commençant par le plus à gauche  */  private final int minColumnCount;  // Définir lorsque l'élément de début V est vu  private boolean vIsOpend_ élément de début de cellule défini; _ //x00   // Utilisé lorsque l'élément de fermeture des cellules est vu.  Private XSSFDatatype NextDatatype;   // Utilisé pour formater les valeurs de cellules numériques.  Format de short privé private int thisColumn = -1;  // La dernière colonne imprimée sur la sortie stream  private int lastColumnNumber = -1;   // rassemble des caractères tels qu'ils sont vu of styles  * @param strings Table of shared strings  * @param cols Minimum number of columns to show  * @param target Sink for output  */  public MyXSSFSheetHandler(  StylesTable styles,  ReadOnlySharedStringsTable strings,  int cols,  PrintStream target) {  this.stylesTable = styles;  this.sharedStringsTable = strings;  this.minColumnCount = cols; =0  this.output. );  this.nextDataType = xssfDataType.NUMBER;  this.formatter = new DataFormatter();_x000 d_  }  /*  * (non-Javadoc)  * @voir org.xml.sax.helpers.DefaultHandler#startElement(java.lang.String, java.lang.String, java.lang.String, org.xml.sax.Attributes)  */  public void startElement(String uri, String localName, String name, Attributes attributs) throws SAXException {  if ("inlineStr".equals(name) || "v".equals(name)) {  vIsOpen = true;  // Effacer le contenu du cache  value.setLength(0);  }  // c => cell  if ("d". equals(name)) {  // Obtient la cellule reference  String r = attributs.getValue("r");  int firstDigit = -1;  for (int c = 0; c < r.length( ); ++c) {  if (Character.isDigit(r.charAt(c))) {  firstDigit = c;  break;  }  =r name.To.Column(d_  0, firstDigit));  // Configurer les valeurs par défaut.  this.nextDataType = xssfDataType.NUMBER;  this.formatIndex = -1;  this.formatString = null; get StringValue type( "t");  String cellStyleStr = attributs.getValue("s");  if ("b".equals(cellType))  nextDataType = xssfDataType.BOOL; _x00 0d_ sinon si ("e".equals(cellType))  nextDataType = xssfDataType.ERROR;  else if ("inlineStr".equals(cellType))  nextDataType = xssfDataType.INLINESTR;  else if ("s ".equals(cellType))  nextDataType = xssfDataType.SSTINDEX;  sinon si ("str".equals(cellType))  nextDataType = xssfDataType.FORMULA;  sinon si (cellStyleStr != null) {_x0 // C'est un nombre, mais presque certainement un  // avec un style ou un format spécial  int styleIndex = Integer.parseInt(cellStyleStr);  XSSFCellStyle style = stylesTable.getStyleAt(styleIndex);  this.formatIndex = style. getDataFormat (); _ x000d_  this.formatString = style.getDataFormatString (); _ x000d_  if (this.formatString == null)   this.formatStStrString = bestidinInformAts.getBuilTinformat } _x000 d_ /*  * (non Javadoc)  * @voir org.xml.sax.helpers.DefaultHandler#endElement(java.lang.String, java.lang.String, java.lang.String)  */   public void endElement(String uri, String localName, String name)  throws SAXException {  String thisStr = null;  // v => contenu d'une cellule  if ("v".equals(name)) {  // Traiter le contenu de la valeur comme requis.  // Faites maintenant, car characters() peut être appelé plus d'une fois  switch (nextDataType) {  case BOOL:  char first = value.charAt(0 );  thisStr = premier == '0' ? "FALSE" : "TRUE" ;  break ;  case ERROR :  thisStr = "\"ERROR :" + value.toString() + '"';  break;  case /FORMULA :  case /FORMULA :  case /FORMULA :  case / Une formule peut donner une valeur de chaîne,  // donc toujours ajouter des guillemets doubles.  thisStr = '"' + value.toString() + '"';  break;  case INLINESTR:  // TODO : j'ai vu un exemple de ceci, donc il n'a pas été testé.  XSSFRichTextString rtsi = new XSSFRichTextString(value.toString());  thisStr = '"' + rtsi.toString() + '"';  Break;   case ssTindex:   String ssTindex = value.tostring (); _ x000d_  try {  int idx = INTERGRIGT ;  thisStr = '"' + rtss.toString() + '"';  }  catch (NumberFormatExc eption ex) {  output.println("Impossible d'analyser l'index SST '" + sstIndex + "' : " + ex.toString());  }  break ;  case NUMBER :  _x00 value.toString();  if (this.formatString != null)  thisStr = formatter.formatRawCellContents(Double.parseDouble(n), this.formatIndex, this.formatString);  else  thisStr = n;  break;  default:  thisStr = "(TODO : type inattendu : " + nextDataType + ")" ;  break;  }  //Emit_00 //d // Sortie après avoir vu le contenu de la chaîne_x0d // des virgules pour tous les champs manquants sur cette ligne  if (lastColumnNumber == -1) {  lastColumnNumber = 0;  }  for (int i = lastColumnNumber; i < cetteColonne ; ++i)  output.print(',');  // Peut être la chaîne vide.  output.print(thisStr);  // Mettre à jour la colonne  si (thisColumn > -1) _x000 lastColumnNumber = thisColumn;  } else if ("row".equals(name)) {  // Imprimer les virgules manquantes si nécessaire  if (minColumns > 0) {  // Les colonnes sont basées sur 0 _x00 lastColumnNumber == -1) {  lastColumnNumber = 0;  }  for (int i = lastColumnNumber; je < (this.minColumnCount); i++) {  output.print(','); _  }   // Nous sommes sur une nouvelle ROW_X000D_  output.println (); _ x000d_  lastColumnNumber = -1;  }  }  _ _x _x _ _ _ _ _ _ _ _x) open.  * À l'origine, c'était juste "v" ; étendu pour inlineStr également.  */  public void characters(char[] ch, int start, int length)  throws SAXException {  if (vIsOpen)  value.append(ch, start, length);  }   / ** _ x000d_  * Converte un nom de colonne Excel comme "C" en un index basé sur un zéro.  *   * @param name  private int nameToColumn(String name) {  int column = -1;  for (int i = 0; i < name.length(); ++i) {  int c = name.charAt(i) ;  colonne = (colonne + 1) * 26 + c - 'A';  }  colonne de retour;  }  }_/////////////////// //////////////////////  private OPCPackage xlsxPackage;  private int minColumns;  private PrintStream output;  /**_x0 00d_  * Crée un nouveau XLSX -> CSV Converter_X000D_  *   * @param pkg the XLSX package à process  * @param ouvroput le strepstream to a publié le CSV3131313 à la Columnn, @ParmUMMe * -1 for no minimum  */  public ApacheXLSX2CSV(OPCPackage pkg, PrintStream output, int minColumns) {  this.xlsxPackage = pkg;  this.output = output;  this.minColumns = minColumns;  }   / ** _ x000d_  * analyse et affiche le contenu d'une sheet  * en utilisant les styles et les strings partagés spécifiés tables.  *  @x000d_ @Param Styles_X000d_  * @Param_xput_xput_xput_xput_xput_xput_xput_xput_xput_xput_xput_xput_xput_xput_xput_xput_xput_xput_xut_xut_xut_xut_xut_xut_xut_xputh   public void processSheet(  StylesTable styles,  ReadOnlySharedStringsTable strings,  InputStream sheetInputStream)  throws IOException, ParserConfigurationException, SAXException {  InputSource sheetSource = new InputSource(sheetInputStream);  SAXParserFactory saxFactory = SAXParserFactory.newInstance();  SAXParser saxParser = saxFactory.newSAXParser();  XMLReader sheetParser = saxParser .getXmlReader (); _ x000d_  Handler de contenuhandler = new MyXssfSheThandler (Styles, Strings, this.Mincolumns, this.output); _ x000d_  sheetparser.setContenthandler (Handler);   **  * Initiates the processing of the XLS workbook file to CSV.  *  * @throws IOException  * @throws OpenXML4JException  * @throws ParserConfigurationException  * @throws SAXException  */  public void process()   lève IOException, Open XML4JException, ParserConfigurationException, SAXException {  ReadOnlySharedStringsTable strings = new ReadOnlySharedStringsTable(this.xlsxPackage);  XSSFReader xssfReader = new XSSFReader(this.xlsxPackage);  StylesTable styles = xssfReader.getStylesTable();  XSSFReader.SheetIterator iter = (XSSFReader.SheetIterator) xssfReader.getSheetsData();  int index = 0;  while (iter.hasNext()) {  InputStream stream = iter.next();  String sheetName = iter.getSheetName() ;  this.output.println();  this.output.println(sheetName + " [index=" + index + "]:");  processSheet(styles, strings, stream);  stream. close();  ++index;  }  }  public static void main(String[] args) throws Exception  {  String dataPath = "parissonrcfeatures/worksheet/dataPath" converttocsv/data/";  File xlsxFile = new File(dataPath + "workbook.xls");  if (!xlsxFile.exists())  {  System.err.println("Not found or not un fichier : " + xlsxFile.getPath());  return;  }  int minColumns = -1;  if (args.length >= 2) _eIgs1 minColumns = Integer.pars] );  // L'ouverture du package est instantanée, comme il se doit.  OPCPackage p = OPCPackage.open(xlsxFile.getPath(), PackageAccess.READ);  ApacheXLSX2CSV xlsx2csv = new ApacheXLSX2CSV(p, System.out , minColumns); _ x000d_  xlsx2csv.process (); _ x000d_ }    {{< /highlight >}} ## ** Télécharger le code en cours d'exécution ** _ x000d_ téléchargement ** Converti - [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/download/Aspose.Cells_Java_vs_POI_SS_v1.4/Convert.Worksheet.t o.CSV.Aspose.Cells.vs.Apache.POI.SS.zip)  {{% alert color="primary" %}}   Pour plus de détails, visitez [Enregistrement de fichiers](/cells/java/saving-excel-files-to-csv-d_0_0_and-other-formats/)._x0 {{% /alert %}}