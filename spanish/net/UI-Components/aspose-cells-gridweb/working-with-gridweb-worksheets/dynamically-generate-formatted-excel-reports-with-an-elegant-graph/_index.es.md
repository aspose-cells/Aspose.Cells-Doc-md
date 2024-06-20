---
title: Generar dinámicamente informes de Excel formateados con un elegante gráfico
type: docs
weight: 130
url: /es/net/aspose-cells-gridweb/dynamically-generate-formatted-excel-reports-with-an-elegant-graph/
keywords: GridWeb, generar informe, informe
description: Este artículo presenta cómo generar informes en GridWeb.
---

{{% alert color="primary" %}} 

Este documento está diseñado para proporcionar la información necesaria sobre cómo podemos extraer datos de alguna fuente de datos a un magnífico control tipo hoja de cálculo, pegar un gráfico en él y exportar el informe con el gráfico a MS Excel para realizar análisis, comparaciones e impresión.

{{% /alert %}} 
## **Visión general**
Hay ciertos escenarios web que demandan tanto informes como presentaciones, una combinación de partes u objetos que pueden funcionar bien juntos. El artículo explica lo fácil que es diseñar y generar informes de Excel con estilo de forma dinámica de manera WYSIWYG. Exporta datos de un archivo XML (también puede utilizar otras fuentes de datos) al control Aspose.Cells.GridWeb que le proporciona el entorno real que le permite aplicar formato rico y atractivo a los datos y calcular los resultados de las fórmulas como MS Excel. También genera un gráfico sofisticado basado en los datos de origen de la hoja de cálculo utilizando el componente [Aspose.Cells](https://products.aspose.com/cells/) y pega la imagen del gráfico en el Informe de Ventas. Finalmente, el informe de Excel con el gráfico adjunto se guarda en el disco utilizando el componente Aspose.Cells.

Este artículo incluye el código fuente y un proyecto de demostración completamente funcional para tal funcionalidad.

Permite a los usuarios tener una percepción detallada sobre cómo crear un informe comercial para ingresar datos en una hoja de cálculo de la cuadrícula y aplicar algún formato a las celdas en las filas y columnas, incrustar un gráfico basado en el rango de datos de origen antes de guardar el informe de Excel en el disco.
## **Los componentes de Aspose**
Utilizo tres de [Aspose](http://www.aspose.com/) componentes para realizar la tarea con facilidad. [Aspose](http://www.aspose.com/), el publicador de componentes .NET y Java, proporciona una variedad de componentes ricos en características. [Aspose](http://www.aspose.com/) ofrece una gran línea de componentes .NET y Java. Confiados por miles de clientes en todo el mundo, los productos incluyen Componentes de Formato de Archivo, Productos de Reportes, Componentes Visuales y Componentes de Utilidad que permiten abrir, modificar, generar, guardar, fusionar, convertir, etc. documentos en varios formatos, incluyendo DOC, RTF, WordML, HTML, PDF, XLS, SpreadsheetML, Tabulados, CSV, PPT, SWF, EMF, WMF, MPX, MPD y otros formatos.

Aprovecharé esta oportunidad para presentarte tres de estos componentes que se han utilizado en esta búsqueda.
## **Controles de Grilla Aspose.Cells**
Los Controles de Grilla Aspose.Cells son una solución de grilla total. Los Controles de Grilla Aspose.Cells vienen empaquetados con dos componentes GUI .NET diferentes (Aspose.Cells.GridDesktop y Aspose.Cells.GridWeb): uno para soportar aplicaciones de escritorio y otro para soportar aplicaciones web. Ambas versiones están igualmente emparejadas para facilitar la implementación en cualquiera de las plataformas. Aspose.Cells.GridWeb ofrece la capacidad de importar y exportar hojas de cálculo de Excel. Entonces, cualquier persona familiarizada con Excel (incluso los usuarios finales) puede diseñar la apariencia de una grilla. Aspose.Cells.GridWeb también ofrece una API fácil de usar y rica en características que brinda a los desarrolladores un control completo sobre la apariencia, sensación y comportamiento de su grilla. Para obtener más información sobre el producto, sus funciones y una guía para programadores, consulta el resumen del Listado de Funciones, la Documentación de Aspose.Cells.GridWeb y las características en línea [Demos](https://aspose.github.io/).
## **Aspose.Cells**
**Aspose.Cells** es un componente de informes de hojas de cálculo de Excel que te permite leer y escribir hojas de cálculo de Excel sin necesidad de tener Microsoft Excel instalado en el cliente o en el servidor. **Aspose.Cells** es un componente rico en funciones que ofrece mucho más que la simple exportación de datos. Con **Aspose.Cells** los desarrolladores pueden exportar datos, dar formato a hojas de cálculo en cada detalle y a cada nivel, importar imágenes, importar gráficos, crear gráficos, manipular gráficos, transmitir datos de Excel, guardar en varios formatos, incluyendo XLS, CSV, SpreadsheetML, TabDelimited, TXT, XML (integrado con [Aspose.Pdf](https://products.aspose.com/pdf/)) y muchos más. **Aspose.Cells** ofrece una API fácil de usar y rica en funciones para los programadores. Tiene una gran lista de funciones. Para obtener más información sobre el producto, sus funciones y una guía para programadores, consulta el resumen del **Listado de Funciones**, la **Documentación de Aspose.Cells** y los Demos en línea destacados. Puedes [descargar](https://downloads.aspose.com/cells) su versión de evaluación de forma gratuita.
## **Diseñando la Interfaz**
Comenzamos creando una nueva aplicación web Asp.Net en Visual Studio.Net.

Agrego referencia a los tres componentes, es decir, Aspose.Cells.GridWeb.dll, Aspose.Chart.dll y Aspose.Cells.dll al proyecto primero. Coloco algunos controles en la página y establezco sus propiedades, es decir, un cuadro desplegable, un botón de comando y una etiqueta. Luego coloco el control de **Aspose.Cells.GridWeb** (GridWeb) desde la caja de herramientas, ya que después de agregar referencias a los tres componentes, el control GridWeb aparece en la caja de herramientas. Los otros dos componentes (Aspose.Chart y Aspose.Cells) son solo bibliotecas, solo se hacen referencia al proyecto.

También creo dos carpetas "archivo" e "imágenes", añado "Products.xml" y "chart.gif" a estas carpetas respectivamente. El archivo xml es un archivo fuente de datos del que se extraerán los datos para llenar la hoja de trabajo de **GridWeb**. El archivo de imagen proporcionará una imagen para un botón personalizado colocado en el control **GridWeb**.

Ahora, creo un botón de comando personalizado. Simplemente hago clic con el botón derecho en el control **GridWeb** y selecciono la opción "Botones de Comando Personalizados...".

Se activará el editor de Botón de Comando Personalizado, el editor te permite crear botones de imagen de comando personalizados con una descripción. Especifico los valores para algunas propiedades del botón, por ejemplo, Comando (Nombre) -> "btnChart", URLimagen -> dar la ruta al archivo de imagen ("chart.gif") y Descripción -> dar la descripción.

Entonces, el botón de comando personalizado se agrega como puedes verlo (encerrado con un color rojo) en la siguiente captura de pantalla.

|![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_1.png)|
| :- |


Finalmente, establezco algunos atributos de fuente (negrita) para la etiqueta y el botón de comando. También ajusto el tamaño de los controles para obtener el aspecto final.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_2.png)
## **Recuperación de datos de un archivo XML**
A continuación se muestra la estructura del archivo XML utilizada en el proyecto.
### **Estructura del archivo XML**
**XML**

{{< highlight csharp >}}

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

{{< highlight java >}}

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

private object[] GetDistinctValues(DataTable dtable, string colName)

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
## **Llenando la Hoja de Trabajo del control Aspose.Cells.GridWeb con Datos**
Utilizo algunas API del control **GridWeb** para llenar una hoja de cálculo con datos del archivo XML de origen. Escribo código en el control del botón de comando (etiquetado como "Mostrar Reporte") en el manejador del evento clic. El reporte de datos se filtra según el elemento seleccionado en el cuadro desplegable.



{{< highlight java >}}

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
## **Formateando Datos en las Celdas**
Para distinguir entre diferentes tipos de información en una hoja de cálculo, para la visualización óptima de los datos en tu hoja de cálculo y para que sea más fácil de escanear, se formatea la hoja de cálculo. Un **Formato** representa un estilo y se define como un conjunto de características, como fuentes y tamaños de fuente, formatos numéricos, bordes de celdas, sombreado de celdas con color de fondo sólido o un patrón de color específico, sangría, alineación y orientación del texto en las celdas.

Agrego algunas líneas más de código a lo anterior. Coloco el título / subtítulo del informe, realizo algún formateo para los títulos, subtítulos y celdas de detalle. También aplico el formato numérico a los dos campos (establezco el formato numérico de moneda a los campos PrecioUnitario y Venta) y ajusto la altura/anchura de las filas y columnas usando la API de **Aspose.Cells.GridWeb**.



{{< highlight java >}}

 //Create the title cell (A1) in the sheet and apply formattings.

//The following lines input a string value to the cell, specify

//font size, specify horizontal and vertical align settings, set

//foreground and background colors and merge cells (A1:E2).

WebWorksheet sheet = GridWeb1.WebWorksheets[0];

sheet.Cells["A1"].PutValue("Product Sales By Category");

sheet.Cells["A1"].Style.Font.Size = new FontUnit("20pt");

sheet.Cells["A1"].Style.HorizontalAlign = HorizontalAlign.Center;

sheet.Cells["A1"].Style.VerticalAlign = VerticalAlign.Middle;

sheet.Cells["A1"].Style.BackColor = Color.SkyBlue;

sheet.Cells["A1"].Style.ForeColor = Color.Blue;

sheet.Cells.Merge(0, 0, 2, 5);

//Create the subtitle cell (A3) in the sheet and apply formattings.

//The following lines input a string value to the cell, specify

//font size with attributes, specify horizontal and vertical align

//settings, set foreground and background colors and merge cells

//(A3:E3).

sheet.Cells["A3"].PutValue(DropDownList1.SelectedItem.Text);

sheet.Cells["A3"].Style.Font.Size = new FontUnit("13pt");

sheet.Cells["A3"].Style.Font.Bold = true;

sheet.Cells["A3"].Style.Font.Italic = true;

sheet.Cells["A3"].Style.HorizontalAlign = HorizontalAlign.Left;

sheet.Cells["A3"].Style.VerticalAlign = VerticalAlign.Middle;

sheet.Cells["A3"].Style.BackColor = Color.SeaGreen;

sheet.Cells["A3"].Style.ForeColor = Color.Yellow;

sheet.Cells.Merge(2, 0, 1, 5);

//Obtain the last row and column (which contain data) indexes.

int totalrow = sheet.Cells.MaxRow +1;

int totalcol = sheet.Cells.MaxColumn;

//Get the sheet Cells collections

WebCells cells = sheet.Cells;

//Define the Cell object.

WebCell cell;

//Loop through the data in the sheet and format two fields with

//Currency number style.

for (int i = 4;i<=totalrow;i++)

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
## **Produciendo el Reporte Formateado (.XLS) con Gráficos usando el componente Aspose.Cells**
Ahora, escribiré algo de código para guardar el reporte formateado con gráficos en el disco. Utilizaré el botón **Guardar** de **GridWeb**, el evento **GuardarComando** de **GridWeb** se dispara cuando haces clic en el botón Guardar, así que lo manejaré. Aquí, utilizo el componente **Aspose.Cells** para exportar el reporte formateado a MS Excel, generar un gráfico y incrustarlo en el archivo de Excel de salida. No he insertado la imagen del gráfico (creada por el componente **Aspose.Chart**) sino que creo un gráfico similar utilizando la API de **Aspose.Cells**, para que puedas editar el gráfico en MS Excel según tus necesidades.





{{< highlight java >}}

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
## **Ejecutando la Aplicación**
Ahora, ejecuto la aplicación. El cuadro desplegable se llena con las categorías distintas.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_3.png)

Selecciono una categoría por la que quiero mostrar el reporte de ventas y hago clic en el botón "Mostrar Reporte".

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_4.png)

Entonces, el reporte se muestra en el **GridWeb** según la categoría seleccionada. El reporte se formatea automáticamente según el código (escrito anteriormente).

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_5.png)

Si deseas dar formato a los datos en algunas de las celdas de manera WYSIWYG, puedes hacerlo con facilidad. **Aspose.Cells.GridWeb** proporciona el editor **Formato de Celdas**, selecciona tu(s) celda(s) deseada(s) y haz clic con el botón derecho, selecciona la opción "Formato Celda...".

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_6.png)

Se muestra el diálogo de Formato de Celda.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_7.png)

Especifico algunos atributos de fuente y hago clic en Aceptar.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_8.png)

Y obtengo el resultado.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_9.png)

Aparte del formato de celdas, también puedes editar los valores de tus celdas. Haz doble clic en la celda deseada y edita el valor.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_10.png)

Para enviar el resultado de la edición y recalcular todas las fórmulas, hago clic en el botón relacionado (encerrado con color rojo) para actualizar el informe.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_11.png)

Ahora crearé el gráfico y lo pegaré en el control. Hago clic en el botón de comando personalizado (encerrado con color rojo) para crear el gráfico circular basado en el rango de datos.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_12.png)

Finalmente, exportaré este informe de datos con gráfico a MS Excel. Hago clic en el botón **Guardar** (encerrado con color rojo). Al hacer clic en el botón **Guardar**, se mostrará el cuadro de diálogo de **Descarga de archivos**, donde puedes **Abrir** el informe resultante (archivo de Excel de salida con gráfico) en MS Excel o Guardarlo en el disco.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_13.png)

Cuando hago clic en el botón Abrir (cuadro de diálogo de descarga de archivos), se exporta el informe de Excel con gráfico a MS Excel. Se muestra la parte superior del informe.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_14.png)

Se muestra la parte inferior del informe de Excel.

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_15.png)
