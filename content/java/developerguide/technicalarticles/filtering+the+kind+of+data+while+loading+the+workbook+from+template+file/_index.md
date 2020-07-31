---
title : "Filtering the kind of data while loading the workbook from template file" 
description : "" 
weight : 12535 
toc : false
type: docs
url: /java/developerguide/technicalarticles/filtering+the+kind+of+data+while+loading+the+workbook+from+template+file/
---

# Aspose.Cells for Java : Filtering the kind of data while loading the workbook from template file


Sometimes, you want to specify which kind of data should be loaded when building the workbook from a template file. Filtering loaded data can improve the performance for your special purpose, especially when using [LightCells APIs](https://docs2.aspose.com/cells/java/developerguide/technicalarticles/using+lightcells+api). Please use the [LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/loadfilter#LoadDataFilterOptions) property for this purpose.

#### Filtering the kind of data while loading the workbook from a template file

The following sample code loads only shape objects while loading the workbook from the [template file](https://docs2.aspose.com/cells/java/attachments/5275666/5472556.xlsx) which you can download from the given link.

The following screenshot shows the [template file](https://docs2.aspose.com/cells/java/attachments/5275666/5472556.xlsx) contents and also explains that the data in Red color and Yellow background will not be loaded because the [LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://apireference.aspose.com/java/cells/com.aspose.cells/loadfilter#LoadDataFilterOptions)property has been set to [LoadDataFilterOptions.SHAPE](https://apireference.aspose.com/java/cells/com.aspose.cells/loaddatafilteroptions#SHAPE).

![](https://docs2.aspose.com/cells/java/attachments/5275666/5472555.png)

The following screenshot shows the [output PDF](https://docs2.aspose.com/cells/java/attachments/5275666/5472554.pdf) which you can download from the given link. Here you can see, the data in Red color and Yellow background is not present but all shapes are there.

![](https://docs2.aspose.com/cells/java/attachments/5275666/5472553.png)


