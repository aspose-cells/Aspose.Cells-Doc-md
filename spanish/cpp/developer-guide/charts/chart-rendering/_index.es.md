---
title: Representación de gráficos
type: docs
weight: 30
url: /es/cpp/chart-rendering/
---
## **Creación de gráficos**

Aspose.Cells Compatibilidad con API para crear gráficos de Excel como se detalla en el tema[Creación y personalización de gráficos de Excel](/cells/es/cpp/creating-and-customizing-charts/)Para demostrar el uso de las API Aspose.Cells para representar los gráficos en formato de imagen y PDF, crearemos un gráfico de tipo Columna según el siguiente fragmento.

{{< highlight "cpp" >}}

     // Create a new workbook

	intrusive_ptr<IWorkbook> workbook = Factory::CreateIWorkbook();

	// Get first worksheet which is created by default

	intrusive_ptr<IWorksheet> worksheet = workbook->GetIWorksheets()->GetObjectByIndex(0);

	// Adding sample values to cells

	worksheet->GetICells()->GetObjectByIndex(new String("A1"))->PutValue(50);

	worksheet->GetICells()->GetObjectByIndex(new String("A2"))->PutValue(100);

	worksheet->GetICells()->GetObjectByIndex(new String("A3"))->PutValue(150);

	worksheet->GetICells()->GetObjectByIndex(new String("B1"))->PutValue(4);

	worksheet->GetICells()->GetObjectByIndex(new String("B2"))->PutValue(20);

	worksheet->GetICells()->GetObjectByIndex(new String("B3"))->PutValue(50);

	// Adding a chart to the worksheet

	int chartIndex = worksheet->GetICharts()->Add(Aspose::Cells::Charts::ChartType::ChartType_Column, 5, 0, 20, 8);

	// Accessing the instance of the newly added chart

	intrusive_ptr<Aspose::Cells::Charts::IChart> chart = worksheet->GetICharts()->GetObjectByIndex(chartIndex);

	// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"

	chart->GetNISeries()->Add(new String("A1:B3"), true);

{{< /highlight >}}

## **Representación de gráficos**

Aspose.Cells Soporte de API para convertir los gráficos de Excel a imágenes y formatos PDF sin necesidad de herramientas o aplicaciones adicionales. Para brindar soporte de representación, la clase Chart ha expuesto los métodos ToImage y ToPdf con una gran cantidad de sobrecargas para adaptarse mejor a los requisitos de la aplicación.

### **Representación de gráficos en imágenes**

El método Chart.toImage tiene una gran cantidad de sobrecargas para admitir la representación simple y avanzada. Si el requisito de la aplicación es representar el gráfico en sus dimensiones predeterminadas, le sugerimos que utilice el método Chart.toImage de la siguiente manera.

{{< highlight "cpp" >}}

 // Output directory path

StringPtr outDir = new String("..\\Data\\02_OutputDirectory\\");

// Path of output image file

StringPtr outputChartImage = outDir->StringAppend(new String("out1image.png"));

// Saving the chart to image file

chart->ToImage(outputChartImage, Aspose::Cells::System::Drawing::Imaging::ImageFormat::GetPng());

{{< /highlight >}}

### **Gráfico de renderizado a PDF**

Para representar el gráfico en formato PDF, las API Aspose.Cells han expuesto el método Chart.ToPdf con la capacidad de almacenar el PDF resultante en la ruta del disco o Stream.

{{< highlight "cpp" >}}

 // Path of output pdf file

StringPtr outputPdfFile = outDir->StringAppend(new String("out1pdf.pdf"));

// Saving chart to PDF

chart->ToPdf(outputPdfFile);

{{< /highlight >}}

## **Tipos de gráficos admitidos para la representación**

Hay algunos tipos de gráficos que actualmente no son compatibles con la representación. Dichos tipos de gráficos contienen**N** en el**Columna admitida** de la siguiente tabla.

|**Tipo de gráfico**|**Subtipo de gráfico**|**Soportado**|
|:- |:- |:- |
|**Columna**|Columna|**Y**|
||Columna apilada|**Y**|
||Columna100PorcentajeApilado|**Y**|
||Columna 3D agrupada|**Y**|
||Columna3Dapilada|**Y**|
||Columna3D100PorcentajeApilado|**Y**|
||Columna3D|**Y**|
|**Bar**|Bar|**Y**|
||Barra apilada|**Y**|
||Bar100Por CientoApilado|**Y**|
||Bar3D Agrupado|**Y**|
||Bar3DSapilado|**Y**|
||Bar3D100Por CientoApilado|**Y**|
|**Línea**|Línea|**Y**|
||línea apilada|**Y**|
||Línea100PorcentajeApilado|**Y**|
||LíneaConMarcadoresDeDatos|**Y**|
||Línea apilada con marcadores de datos|**Y**|
||Línea100PorcentajeApiladoConMarcadoresDeDatos|**Y**|
||Línea3D|**Y**|
|**Tarta**|Tarta|**Y**|
||Pie3D|**Y**|
||Pastel Pastel|**Y**|
||PastelExplotado|**Y**|
||Pie3DExplotado|**Y**|
||PieBar|**Y**|
|**Dispersión**|Dispersión|**Y**|
||ScatterConnectedByCurvesWithDataMarker|**Y**|
||DispersiónConectadoPorCurvasSinMarcador de datos|**Y**|
||ScatterConnectedByLinesWithDataMarker|**Y**|
||ScatterConnectedByLinesWithoutDataMarker|**Y**|
|**Área**|Área|**Y**|
||Área apilada|**Y**|
||Área100PorcentajeApilado|**Y**|
||Área3D|**Y**|
||Area3DSapilado|**Y**|
||Área3D100PorcentajeApilado|**Y**|
|**Rosquilla**|Rosquilla|**Y**|
||RosquillaExplotó|**Y**|
|**Radar**|Radar|**Y**|
||RadarConMarcadoresDeDatos|**Y**|
||Lleno de radar|**Y**|
|**Superficie**|Superficie3D|norte|
||SuperficieAlambrado3D|norte|
||SuperficieContorno|norte|
||SuperficieContornoEstructura metálica|norte|
|**Burbuja**|Burbuja|**Y**|
||Burbuja3D|norte|
|Valores|InventarioAltoBajoCerrar|**Y**|
||InventarioAbiertoAltoBajoCerrar|**Y**|
||InventarioVolumenAltoBajoCerrar|**Y**|
||StockVolumenAbiertoAltoBajoCerrar|**Y**|
|**Cilindro**|Cilindro|**Y**|
||CilindroApilado|**Y**|
||Cilindro100PorcentajeApilado|**Y**|
||CilíndricoBar|**Y**|
||CilíndricoBarApilado|**Y**|
||CilíndricoBar100PorcentajeApilado|**Y**|
||CilíndricoColumna3D|**Y**|
|**Cono**|Cono|**Y**|
||ConoApilado|**Y**|
||Cono100Por CientoApilado|**Y**|
||Barracónica|**Y**|
||Barra CónicaApilada|**Y**|
||CónicoBar100PorcentajeApilado|**Y**|
||ColumnaCónica3D|**Y**|
|**Pirámide**|Pirámide|**Y**|
||Pirámide apilada|**Y**|
||Pirámide100Por CientoApilado|**Y**|
||PirámideBar|**Y**|
||PirámideBarApilado|**Y**|
||PirámideBar100PorcentajeApilado|**Y**|
||PirámideColumna3D|**Y**|
|**cajabigotes**|cajabigotes|Y|
|**Embudo**|Embudo|**Y**|
|**Línea de Pareto**|Línea de Pareto|**Y**|
|**rayos de sol**|rayos de sol|**Y**|
|**Mapa de árbol**|Mapa de árbol|**Y**|
|**Cascada**|Cascada|**Y**|
|**Histograma**|Histograma|Y|
|**Mapa**|Mapa|**NORTE**|

{{% alert color="primary" %}}

En caso de que intente representar los tipos de gráficos no admitidos en imágenes o PDF, puede terminar con imágenes de tamaño 0 o PDF en blanco.

{{% /alert %}}
