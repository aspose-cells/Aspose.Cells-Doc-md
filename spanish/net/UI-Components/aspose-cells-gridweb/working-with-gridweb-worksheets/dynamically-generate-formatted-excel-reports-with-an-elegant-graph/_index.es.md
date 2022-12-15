---
title: Genere dinámicamente informes de Excel con formato con un gráfico elegante
type: docs
weight: 130
url: /es/net/dynamically-generate-formatted-excel-reports-with-an-elegant-graph/
---
{{% alert color="primary" %}} 

Este documento está diseñado para proporcionar la información necesaria sobre cómo podemos extraer datos de alguna fuente de datos a una cuadrícula espléndida como control, pegar un gráfico en él y exportar el informe con el gráfico a MS Excel para realizar análisis, comparaciones e imprimir.

{{% /alert %}} 
## **Visión general**
Hay ciertos escenarios web que exigen informes y presentaciones, una combinación de partes u objetos que pueden funcionar bien juntos. El artículo explica lo fácil que es diseñar y generar informes de Excel con estilo dinámicamente de manera WYSIWYG. Exporta datos desde un archivo XML (también puede utilizar otras fuentes de datos) al control Aspose.Cells.GridWeb que le brinda el entorno real que le permite aplicar un formato rico y atractivo a los datos y calcular resultados de fórmulas como MS Excel. También genera un gráfico sofisticado basado en los datos de origen de la hoja de trabajo utilizando[Aspose.Cells](https://products.aspose.com/cells/) y pega la imagen del gráfico en el Informe de ventas. Finalmente, el informe de Excel con el gráfico adjunto se guarda en el disco utilizando el componente Aspose.Cells.

Este artículo incluye el código fuente y el proyecto de demostración con todas las funciones para dicha funcionalidad.

Permite a los usuarios con una percepción detallada sobre cómo crear un informe comercial para ingresar datos en una hoja de trabajo de la cuadrícula y aplicar algún formato a las celdas en las filas y columnas, incrustar un gráfico basado en el rango de fuente de datos antes de guardar el informe excel al disco.
## **Los componentes Aspose**
 Yo uso tres de[Aspose](http://www.aspose.com/) Los componentes para realizar la tarea con facilidad.[Aspose](http://www.aspose.com/) , El editor de componentes .NET y Java proporciona una variedad de componentes ricos en características.[Aspose](http://www.aspose.com/) proporciona una gran línea de componentes .NET y Java. Con la confianza de miles de clientes en todo el mundo, los productos incluyen componentes de formato de archivo, productos de informes, componentes visuales y componentes de utilidad que permiten abrir, modificar, generar, guardar, fusionar, convertir, etc., mediante programación, documentos en varios formatos, incluidos DOC, RTF, WordML, HTML, PDF, XLS, SpreadsheetML, delimitado por tabuladores, CSV, PPT, SWF, EMF, WMF, MPX, MPD y otros formatos.

Aprovecharía esta oportunidad para presentarles tres de estos componentes que se han utilizado en esta búsqueda.
## **Aspose.Cells Controles de rejilla**
 Aspose.Cells Grid Controls es una solución de red total. Aspose.Cells Grid Controls vienen empaquetados con dos componentes GUI .NET diferentes (Aspose.Cells.GridDesktop y Aspose.Cells.GridWeb): uno para admitir aplicaciones de escritorio y otro para admitir aplicaciones web. Ambas versiones se combinan por igual para que la implementación en cualquiera de las plataformas sea muy sencilla. Aspose.Cells.GridWeb brinda la capacidad de importar y exportar a hojas de cálculo de Excel. Así que cualquiera que esté familiarizado con Excel (incluso los usuarios finales) puede diseñar la apariencia de una cuadrícula. Aspose.Cells.GridWeb también ofrece un API fácil de usar y rico en funciones que brinda a los desarrolladores un control total sobre la apariencia y el comportamiento de su cuadrícula. Para obtener más información sobre el producto, sus características y una guía para programadores, consulte el resumen de la Lista de características, Aspose.Cells. Documentación de GridWeb y destacados en línea[Población](https://aspose.github.io/)
## **Aspose.Cells**
**Aspose.Cells**es un componente de informes de hojas de cálculo de Excel que le permite leer y escribir hojas de cálculo de Excel sin utilizar Microsoft Excel para instalarlo en el lado del cliente o del servidor.**Aspose.Cells** es un componente rico en funciones que ofrece mucho más que la exportación básica de datos. Con**Aspose.Cells** los desarrolladores pueden exportar datos, formatear hojas de cálculo con todos los detalles y en todos los niveles, importar imágenes, importar gráficos, crear gráficos, manipular gráficos, transmitir datos de Excel, guardar en varios formatos, incluidos XLS, CSV, SpreadsheetML, TabDelimited, TXT, XML ([Aspose.Pdf](https://products.aspose.com/pdf/) integrado) y muchos más.**Aspose.Cells** ofrece un fácil de usar, rico en características**API** para los programadores. Tiene una enorme lista de características. Para obtener más información sobre el producto, sus características y para obtener una guía del programador, consulte el resumen de**Lista de funciones**, **Aspose.Cells Documentación** y demostraciones destacadas en línea. Puedes[descargar](https://downloads.aspose.com/cells) su versión de evaluación de forma gratuita.
## **Diseño de la interfaz**
Comenzamos a crear una nueva aplicación web Asp.Net en Visual Studio.Net.

 yo**Añadir referencia** los tres componentes, es decir, Aspose.Cells.GridWeb.dll, Aspose.Chart.dll y Aspose.Cells.dll al proyecto primero. Coloco algún control en la página y establezco sus propiedades, es decir, una lista desplegable, un botón de comando y una etiqueta. entonces coloco**Aspose.Cells.GridWeb****control**(**GridWeb**) a él desde la caja de herramientas, ya que después de agregar referencias a los tres componentes, el**GridWeb**el control aparece en la caja de herramientas. Los otros dos componentes (**Aspose.Chart**y**Aspose.Cells**) son solo bibliotecas, solo se hace referencia al proyecto.

También creo dos carpetas "archivo" e "imágenes", agrego "Productos.xml" y "chart.gif" a estas carpetas respectivamente. El archivo xml es un archivo de origen de datos del que se extraerán los datos para llenar el**GridWeb**hoja de cálculo. El archivo de imagen proporcionará una imagen para un botón personalizado colocado en el**GridWeb**control.

Yo, ahora, creo un botón de comando personalizado. Simplemente hago clic derecho en el**GridWeb**control y haga clic en la opción "Botones de comando personalizados...".

Activará el editor de botón de comando personalizado, el editor le permite crear botones de imagen de comando personalizados con información sobre herramientas adjunta. Especifico los valores para algunas propiedades del botón, por ejemplo, Comando (Nombre) ->"btnChart", ImageUrl -> dar la ruta al archivo de imagen ("chart.gif") y ToolTip -> dar la información sobre herramientas.

Por lo tanto, el botón de comando personalizado se agrega como puede verlo (encerrado en color rojo) en la siguiente captura de pantalla.

|![todo:imagen_alternativa_texto](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_1.png)|
|:- |


Finalmente, configuré algunos atributos de fuente (negrita) para la etiqueta y el botón de comando. También ajusto el tamaño de los controles para obtener el aspecto final.

![todo:imagen_alternativa_texto](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_2.png)
## **Recuperación de datos de un archivo XML**
A continuación se muestra la estructura del archivo XML utilizada en el proyecto.
### **Estructura del archivo XML**
**XML**

{{< highlight "csharp" >}}

 <?xml version="1.0" standalone="yes"?>

<SalesData>

  <Products>

    <ProductName>Data</ProductName>

    <QuantityPerUnit>Data</QuantityPerUnit>

    <CategoryName>Data</CategoryName>

    <UnitPrice>Data</UnitPrice>

    <Sale>Data</Sale>

  </Products>

 .........

</SalesData>



{{< /highlight >}}

{{< highlight "java" >}}

 private void Page_Load(object sender, System.EventArgs e)

{

if (!IsPostBack)

{

	// Uncomment the code below when you have purchased license

	// for Aspose.Cells.GridWeb, Aspose.Chart and Aspose.Cells. You need

	// to deploy the licenses in the same folder as your executable,

      // alternatively you can add the license files as an embedded

      // resource to your project.

	//

	// Set the license for Aspose.Cells.GridWeb

	// Aspose.Cells.GridWeb.License gridwebLicense = new

	// Aspose.Cells.GridWeb.License();

	// gridwebLicense.SetLicense("Aspose.Grid.lic");

	//

	// // Set the license for Aspose.Chart

	// Aspose.Chart.License chartLicense = new

	// Aspose.Chart.License();

	// chartLicense.SetLicense("Aspose.Chart.lic");

	//

	// // Set the license for Aspose.Cells

	// Aspose.Cells.License cellsLicense = new

	// Aspose.Cells.License();

	// cellsLicense.SetLicense("Aspose.Cells.lic");

	//Create a DataSet object.

	DataSet ds = new DataSet();

	//Get the Virtual Folder Path.

	string path = MapPath(".");

	//Reads XML data from xml file into DataSet object.

	ds.ReadXml(path + "\\file\\Products.xml");

	//Call the custom method to obtain distinct values from

	//CategoryName field and store data into an object array.

	object [] drs = GetDistinctValues(ds.Tables[0],"CategoryName");

	//Fill the drop down list with distinct field items.

	for(int i = 0;i<drs.Length;i++)

	{

		DropDownList1.Items.Add(drs[i].ToString());

	}

}

}

//This method is used to filter distinct values from CategoryName field in the datatable.

private object[]GetDistinctValues(DataTable dtable, string colName)

{

	// Create a Hashtable object.

	Hashtable hTable = new Hashtable();

	// Loop through the datatable rows and add distinct values to

	// Hashtable object minimizing the duplicates in the field.

	foreach (DataRow drow in dtable.Rows)

	if(!hTable.ContainsKey(drow[colName]))

	hTable.Add(drow[colName], string.Empty);

	// Create an object array based on the distinct key values of the Hashtable object.

	object[] objArray = new object[hTable.Keys.Count];

	// Copy the disctinct values to fill the array.

	hTable.Keys.CopyTo(objArray, 0);

	// Return the array object.

	return objArray;

}

{{< /highlight >}}
## **Llenar la hoja de trabajo del control Aspose.Cells.GridWeb con datos**
Yo uso algunos API de la**GridWeb**para llenar una hoja de cálculo con datos del archivo XML de origen. Escribo código en el controlador de eventos de clic del botón de comando (etiquetado como "Mostrar informe"). El informe de datos se filtra según el elemento seleccionado de la lista desplegable.



{{< highlight "java" >}}

 //Clears datasheets of the GridWeb control.

GridWeb1.WebWorksheets.Clear();

//Create a DataSet object.

DataSet ds = new DataSet();

//Get the Virtual Folder path.

string path = MapPath(".");

//Reads XML data from xml file into DataSet object.

ds.ReadXml(path + "\\file\\Products.xml");

//Create a DataView based on the datatable.

DataView dv = new DataView(ds.Tables[0]);

//Filter data in the DataView object based on the selected drop down list item.

dv.RowFilter = "CategoryName ='" + DropDownList1.SelectedItem.Text + "'";

//Importing data from the filtered DataView object to create and

//fill "Products" Worksheet start from A4 cell.

GridWeb1.WebWorksheets.ImportDataView(dv, null, null,"Products",3,0);

{{< /highlight >}}
## **Formateo de datos en el Cells**
Para distinguir entre diferentes tipos de información en una hoja de trabajo, para la visualización óptima de los datos en su hoja de trabajo y para hacer una hoja de trabajo más fácil de escanear, formatee la hoja de trabajo. A**Formato**representa un estilo y se define como un conjunto de características, como fuentes y tamaños de fuentes, formatos de números, bordes de celdas, sombreado de celdas con un color de fondo sólido o un patrón de color específico, sangría, alineación y orientación del texto en las celdas.

Amalgamo algunas líneas más de código a las anteriores. Coloco el título/subtítulo del informe, doy formato al título, subtítulo y celdas de detalle. También aplico el formato de número a los dos campos (configuro el formato de número de moneda en los campos Precio por unidad y Venta) y ajusto el alto/ancho de filas y columnas usando**Aspose.Cells.GridWeb**API.



{{< highlight "java" >}}

 //Cree la celda de título (A1) en la hoja y aplique formatos.

//Las siguientes líneas ingresan un valor de cadena a la celda, especifique

// tamaño de fuente, especifique la configuración de alineación horizontal y vertical, establezca

//colores de primer plano y de fondo y fusionar celdas (A1:E2).

Hoja de WebWorksheet = GridWeb1.WebWorksheets[0];

sheet.Cells["A1"].PutValue("Ventas de productos por categoría");

sheet.Cells["A1"].Style.Font.Size = new FontUnit("20pt");

hoja.Cells["A1"].Estilo.HorizontalAlign = HorizontalAlign.Center;

hoja.Cells["A1"].Estilo.VerticalAlign = VerticalAlign.Middle;

sheet.Cells["A1"].Style.BackColor = Color.SkyBlue;

hoja.Cells["A1"].Estilo.ForeColor = Color.Azul;

hoja.Cells.Fusionar(0, 0, 2, 5);

//Cree la celda de subtítulos (A3) en la hoja y aplique formatos.

//Las siguientes líneas ingresan un valor de cadena a la celda, especifique

//tamaño de fuente con atributos, especificar alineación horizontal y vertical

//configuraciones, establecer colores de primer plano y de fondo y fusionar celdas

//(A3:E3).

hoja.Cells["A3"].PutValue(DropDownList1.SelectedItem.Text);

sheet.Cells["A3"].Style.Font.Size = new FontUnit("13pt");

hoja.Cells["A3"].Estilo.Fuente.Negrita = verdadero;

hoja.Cells["A3"].Estilo.Fuente.Cursiva = verdadero;

sheet.Cells["A3"].Style.HorizontalAlign = HorizontalAlign.Left;

hoja.Cells["A3"].Estilo.VerticalAlign = VerticalAlign.Middle;

sheet.Cells["A3"].Style.BackColor = Color.SeaGreen;

hoja.Cells["A3"].Estilo.ForeColor = Color.Amarillo;

hoja.Cells.Fusionar(2, 0, 1, 5);

//Obtenga los índices de la última fila y columna (que contienen datos).

int totalrow = hoja.Cells.MaxRow +1;

int totalcol = hoja.Cells.MaxColumn;

//Obtener la hoja Cells colecciones

Celdas WebCells = hoja.Cells;

//Definir el objeto Cell.

celda WebCell;

//Recorrer los datos en la hoja y formatear dos campos con

//Estilo de número de moneda.

para (int i = 4; i<=totalrow;i++)

{

	//Format the Sale Column.

	cell = cells[i,totalcol];

	cell.PutValue(cell.StringValue,true);

	cell.NumberType = NumberType.Currency1;

	//Format the UnitPrice Column.

	cell = cells[i,totalcol-1];

	cell.PutValue(cell.StringValue,true);

	cell.NumberType = NumberType.Currency1;

}

//Insert the Total row with data, formula and formatting style.

//It will calculate the total Sales of a Category.

cells[totalrow,0].PutValue( DropDownList1.SelectedItem.Text + " Total" );

cells[totalrow,0].Style.Font.Bold = true;

cells[totalrow,totalcol].Formula = "=SUM(E5:E" + totalrow.ToString() + ")";

cells[totalrow,totalcol].Style.Font.Bold = true;

//Specify some Row and Column formattings. It will set row height

//and column width accordingly.

cells.SetRowHeight(2, new Unit("17pt"));

cells.SetColumnWidth(0, new Unit("157pt"));

cells.SetColumnWidth(1, new Unit("106pt"));

cells.SetColumnWidth(2, new Unit("87pt"));

cells.SetColumnWidth(3, new Unit("56pt"));

cells.SetColumnWidth(4, new Unit("50pt"));



{{< /highlight >}}
## **Producir el informe formateado (archivo .XLS) con gráfico utilizando el componente Aspose.Cells**
Ahora, escribiré un código para guardar el informe formateado con el gráfico en el disco. yo utilizo**GridWeb** 's**Ahorrar**botón, El**GridWeb** 's**GuardarComando**El evento se activa cuando hace clic en el botón Guardar, así que lo manejaré. Aquí, uso**Aspose.Cells**componente para exportar el informe formateado a MS Excel, generar un gráfico e incrustarlo en el archivo de salida de Excel. No he insertado la imagen del gráfico (creado por**Aspose.Chart**componente) en lugar de crear el gráfico similar utilizando el API de**Aspose.Cells**para que pueda editar el gráfico en MS Excel según sus necesidades.





{{< highlight "java" >}}

 //This GridWeb control event is fired when you click on the "Save" button

//of the control. After Clicking this button "File Download" dialog is

//displayed and you may open into MS Excel / save the output excel file //with graph to disk.

private void GridWeb1_SaveCommand(object sender, System.EventArgs e)

{

	//Create MemoryStream object.

	System.IO.MemoryStream ms = new System.IO.MemoryStream();

	//Save the GridWeb's Report to the stream.

	this.GridWeb1.WebWorksheets.SaveToExcelFile(ms);

	//Create a new Workbook.

	Workbook workbook = new Workbook();

	//Open the stream into the Workbook.

	workbook.Open(ms);

	//Call the custom method which creates Chart.

	Workbook book = CellsChart(workbook);

	//Save the excel file displaying "File Download" dialog box.

	book.Save(ms, FileFormatType.Default);

	this.Response.ContentType = "application/vnd.ms-excel";

	this.Response.AddHeader("content-disposition", "attachment; filename=Export.xls");

	this.Response.BinaryWrite(ms.ToArray());

}

//This custom method is used to create the Chart based on the data source

//range in the GridWeb control. In this method we will use Aspose.Cells

//APIs to create the graph which will be saved later into the output //excel file.

private Workbook CellsChart(Workbook workbook)

{

	//Get the first Worksheet.

	Aspose.Cells.Worksheet sheet = workbook.Worksheets[0];

	//Get the Cells collection in the sheet.

	Aspose.Cells.Cells cells = workbook.Worksheets[0].Cells;

	//Get the last row index.

	int maxrow = sheet.Cells.MaxDataRow;

	//Unmerge the cells.

	sheet.Cells.UnMerge(maxrow,0,15,10);

	int chartIndex = 0;

	//Add a new Chart into the sheet's Chart Collection.

chartIndex = sheet.Charts.Add(Aspose.Cells.ChartType.Pie,maxrow,0,maxrow+28,5);

	//Get the Chart object.

	Aspose.Cells.Chart chart = sheet.Charts[chartIndex];

	//Set the Chart Area.

	Aspose.Cells.ChartArea chartarea = chart.ChartArea;

	chartarea.Area.Formatting = FormattingType.Custom;

	chartarea.Border.IsVisible = false;

		chartarea.Area.FillFormat.SetTwoColorGradient(Color.PowderBlue, Color.LightSkyBlue, GradientStyleType.FromCenter,1);

	//Set some properties of Chart Plot Area.

	chart.PlotArea.Area.Formatting = FormattingType.None;

	chart.PlotArea.Border.IsVisible = false;

	//Set properties of Chart Title.

	chart.Title.Text = DropDownList1.SelectedItem.Text + " Sales";

	chart.Title.TextFont.Size = 20;

	//Set properties of NSeries

	int lastdatarow = maxrow-1;

	chart.NSeries.Add("E5:E" + lastdatarow.ToString(), true);

	chart.NSeries.CategoryData = "A5:A" + lastdatarow.ToString();

	//Set the Data Labels in the chart

	Aspose.Cells.DataLabels datalabels;

	for ( int i = 0; i < chart.NSeries.Count ;i ++ )

	{

		datalabels = chart.NSeries[i].DataLabels;

		datalabels.Postion = Aspose.Cells.LabelPositionType.Center;

		datalabels.IsPercentageShown = true;

	}

	//Set the Legend settings.

	Aspose.Cells.Legend legend = chart.Legend;

	legend.Position = Aspose.Cells.LegendPositionType.Bottom;

	legend.Height = 85;

	legend.Width = 330;

	legend.AutoScaleFont = true;

	legend.Border.Color = Color.Blue;

	legend.Area.Formatting = FormattingType.Custom;

	FillFormat fillformat = legend.Area.FillFormat;

	legend.Area.Formatting = FormattingType.None;

	legend.Border.IsVisible = false;

	//Autofit the first column.

	sheet.AutoFitColumn(0);

	//Return the Workbook.

	return workbook;

}



{{< /highlight >}}
## **Ejecutar la aplicación**
Ahora, ejecuto la aplicación. La lista desplegable se llena con las distintas categorías.

![todo:imagen_alternativa_texto](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_3.png)

Selecciono una categoría por la que quiero mostrar el informe de ventas y hago clic en el botón "Mostrar informe".

![todo:imagen_alternativa_texto](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_4.png)

Por lo tanto, el informe se muestra en el**GridWeb**según la categoría seleccionada. El informe tiene un formato predeterminado basado en el código (escrito anteriormente).

![todo:imagen_alternativa_texto](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_5.png)

Si desea formatear datos en algunas de las celdas de manera WYSIWYG, puede hacerlo con bastante facilidad.**Aspose.Cells.GridWeb**proporciona**Formato Cells**editor, seleccione la(s) celda(s) deseada(s) y haga clic derecho sobre ella, haga clic en la opción "Formatear Cell...".

![todo:imagen_alternativa_texto](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_6.png)

Se muestra el cuadro de diálogo Formato Cell.

![todo:imagen_alternativa_texto](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_7.png)

Especifico algunos atributos de fuente y hago clic en Aceptar.

![todo:imagen_alternativa_texto](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_8.png)

Y obtener el resultado.

![todo:imagen_alternativa_texto](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_9.png)

Además del formato de celdas, también puede editar los valores de sus celdas. Haga doble clic en la(s) celda(s) deseada(s) y edite el valor.

![todo:imagen_alternativa_texto](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_10.png)

Para enviar el resultado de la edición y volver a calcular toda la fórmula, hago clic en el botón relacionado (rodeado de color rojo) para actualizar el informe.

![todo:imagen_alternativa_texto](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_11.png)

Ahora crearé el gráfico y lo pegaré en el control. Hago clic en el botón de comando personalizado (rodeado de color rojo) para crear el gráfico circular basado en el rango de datos.

![todo:imagen_alternativa_texto](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_12.png)

Finalmente, exportaré este informe de datos con gráfico a MS Excel. hago clic en el**Ahorrar**botón (rodeado de color rojo). Al hacer clic en el**Ahorrar**se mostrará el botón**Descarga de archivos**diálogo, puede**Abierto**el informe resultante (archivo de Excel de salida con gráfico) en MS Excel o guárdelo en el disco.

![todo:imagen_alternativa_texto](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_13.png)

Cuando hago clic en el botón Abrir (cuadro de diálogo Descargar archivo), el informe de Excel con el gráfico se exporta a MS Excel. Se muestra la parte superior del informe.

![todo:imagen_alternativa_texto](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_14.png)

Se muestra la parte inferior del informe de Excel.

![todo:imagen_alternativa_texto](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_15.png)
