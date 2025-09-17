##Find Type of X and Y Values of Points in Chart Series
Learn how to determine the type of X and Y values in chart series points using Aspose.Cells for Python via .NET. Our guide will explain the different types of data values and show you how to access and work with them in your charts.
## **Possible Usage Scenarios**
Sometime, you want to know the type of X and Y values of chart points in a series. Aspose.Cells for Python via .NET provides [**ChartPoint.x_value_type**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/x_value_type/) and [**ChartPoint.y_value_type**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/y_value_type/) properties that can be used for this purpose. Please note, you will have to call [**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate/#) method before you could use these properties effectively.
## **Find Type of X and Y Values of Points in Chart Series**
The following sample code loads the [sample Excel file](64716905.xlsx) and accesses the first chart inside the first worksheet. It then calls the [**Chart.calculate()**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/calculate/#) method and finds the type of X and Y values of first chart point and prints them on console. Please see the console output shown below for a reference.
## **Sample Code**
## **Console Output**
X Value Type: IsString
Y Value Type: IsNumeric
