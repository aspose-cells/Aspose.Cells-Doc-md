---
title: Ruby de Grafikleri Görüntüye Dönüştürme
type: docs
weight: 10
url: /tr/java/converting-chart-to-image-in-ruby/
---

## **Aspose.Cells - Grafikleri Resme Dönüştürme**
Ruby'de Aspose.Cells for Java kullanarak Grafikleri Resme Dönüştürmek için, Converter modülünü basitçe çağırın.

**Ruby Kodu**

{{< highlight ruby >}}

 def chart_to_image()

    # Create a new Workbook.

    workbook = Rjb::import('com.aspose.cells.Workbook').new

    # Get the first worksheet.

    sheet = workbook.getWorksheets().get(0)

    # Set the name of worksheet

    sheet.setName("Data")

    # Get the cells collection in the sheet.

    cells = workbook.getWorksheets().get(0).getCells()

    # Put some values into a cells of the Data sheet.

    cells.get("A1").setValue("Region")

    cells.get("A2").setValue("France")

    cells.get("A3").setValue("Germany")

    cells.get("A4").setValue("England")

    cells.get("A5").setValue("Sweden")

    cells.get("A6").setValue("Italy")

    cells.get("A7").setValue("Spain")

    cells.get("A8").setValue("Portugal")

    cells.get("B1").setValue("Sale")

    cells.get("B2").setValue(70000)

    cells.get("B3").setValue(55000)

    cells.get("B4").setValue(30000)

    cells.get("B5").setValue(40000)

    cells.get("B6").setValue(35000)

    cells.get("B7").setValue(32000)

    cells.get("B8").setValue(10000)

    # Create chart

    chart_type = Rjb::import('com.aspose.cells.ChartType')

    chart_index = sheet.getCharts().add(chart_type.COLUMN, 12, 1, 33, 12)

    chart = sheet.getCharts().get(chart_index)

    # Set properties of chart title

    chart.getTitle().setText("Sales By Region")

    chart.getTitle().getFont().setBold(true)

    chart.getTitle().getFont().setSize(12)

    # Set properties of nseries

    chart.getNSeries().add("Data!B2:B8", true)

    chart.getNSeries().setCategoryData("Data!A2:A8")

    # Set the fill colors for the series's data points (France - Portugal(7 points))

    chart_points = chart.getNSeries().get(0).getPoints()

    color = Rjb::import('com.aspose.cells.Color')

    point = chart_points.get(0)

    point.getArea().setForegroundColor(color.getCyan())

    point = chart_points.get(1)

    point.getArea().setForegroundColor(color.getBlue())

    point = chart_points.get(2)

    point.getArea().setForegroundColor(color.getYellow())

    point = chart_points.get(3)

    point.getArea().setForegroundColor(color.getRed())

    point = chart_points.get(4)

    point.getArea().setForegroundColor(color.getBlack())

    point = chart_points.get(5)

    point.getArea().setForegroundColor(color.getGreen())

    point = chart_points.get(6)

    point.getArea().setForegroundColor(color.getMaroon())

    # Set the legend invisible

    chart.setShowLegend(false)

    # Get the Chart image

    img_opts = Rjb::import('com.aspose.cells.ImageOrPrintOptions').new

    image_format = Rjb::import('com.aspose.cells.ImageFormat')

    img_opts.setImageFormat(image_format.getPng())

    # Save the chart image file.

    chart.toImage(@data_dir + "MyChartImage.png", img_opts)

    # Print message

    puts "Convert chart to image successfully."

end   

{{< /highlight >}}
## **Çalışan Kodu İndir**
**Aspose.Cells ile Grafikleri Resme Dönüştürme**'yi aşağıda belirtilen sosyal kodlama sitelerinden herhangi birinden indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
