---  
title: Converting Chart to Image in PHP  
type: docs  
weight: 10  
url: /java/converting-chart-to-image-in-php/  
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Aspose.Cells - Converting Chart to Image**  
To convert a chart to an image using Aspose.Cells for Java in PHP, simply invoke the converter module.  

**PHP Code**  

{{< highlight php >}}  

$chartType = new ChartType();  

$color = new Color();  

$imageFormat = new ImageFormat();  

//Create a new Workbook.  
$workbook = new Workbook();  

//Get the first worksheet.  
$sheet = $workbook->getWorksheets()->get(0);  

//Set the name of the worksheet  
$sheet->setName("Data");  

//Get the cells collection in the sheet.  
$cells = $workbook->getWorksheets()->get(0)->getCells();  

//Put some values into cells of the Data sheet.  
$cells->get("A1")->setValue("Region");  
$cells->get("A2")->setValue("France");  
$cells->get("A3")->setValue("Germany");  
$cells->get("A4")->setValue("England");  
$cells->get("A5")->setValue("Sweden");  
$cells->get("A6")->setValue("Italy");  
$cells->get("A7")->setValue("Spain");  
$cells->get("A8")->setValue("Portugal");  

$cells->get("B1")->setValue("Sale");  
$cells->get("B2")->setValue(70000);  
$cells->get("B3")->setValue(55000);  
$cells->get("B4")->setValue(30000);  
$cells->get("B5")->setValue(40000);  
$cells->get("B6")->setValue(35000);  
$cells->get("B7")->setValue(32000);  
$cells->get("B8")->setValue(10000);  

//Create chart  
$chartIndex = $sheet->getCharts()->add($chartType->COLUMN, 12, 1, 33, 12);  
$chart = $sheet->getCharts()->get($chartIndex);  

//Set properties of the chart title  
$chart->getTitle()->setText("Sales By Region");  
$chart->getTitle()->getFont()->setBold(true);  
$chart->getTitle()->getFont()->setSize(12);  

//Set properties of NSeries  
$chart->getNSeries()->add("Data!B2:B8", true);  
$chart->getNSeries()->setCategoryData("Data!A2:A8");  

//Set the fill colors for the series' data points (France - Portugal, 7 points)  
$chartPoints = $chart->getNSeries()->get(0)->getPoints();  

$point = $chartPoints->get(0);  
$point->getArea()->setForegroundColor(java_values($color->getCyan()));  

$point = $chartPoints->get(1);  
$point->getArea()->setForegroundColor($color->getBlue());  

$point = $chartPoints->get(2);  
$point->getArea()->setForegroundColor($color->getYellow());  

$point = $chartPoints->get(3);  
$point->getArea()->setForegroundColor($color->getRed());  

$point = $chartPoints->get(4);  
$point->getArea()->setForegroundColor($color->getBlack());  

$point = $chartPoints->get(5);  
$point->getArea()->setForegroundColor($color->getGreen());  

$point = $chartPoints->get(6);  
$point->getArea()->setForegroundColor($color->getMaroon());  

//Make the legend invisible  
$chart->setShowLegend(false);  

//Get the chart image  
$imgOpts = new ImageOrPrintOptions();  
$imgOpts->setImageFormat($imageFormat->getEmf());  

$fs = new FileOutputStream($dataDir . "Chart.emf");  

//Save the chart image file.  
$chart->toImage($fs, $imgOpts);  

$fs->close();  

{{< /highlight >}}  

## **Download Running Code**  
Download **Converting Chart to Image (Aspose.Cells)** from any of the following social coding sites:  

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ChartToImage.php)
