---
title : "Filtering the kind of data while loading the workbook from template file" 
description : "" 
weight : 20461 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/mngworkbooksandworksheets/filtering+the+kind+of+data+while+loading+the+workbook+from+template+file/
---

# Aspose.Cells for .NET : Filtering the kind of data while loading the workbook from template file


Sometimes, you want to specify which kind of data should be loaded when building the workbook from the template file. Filtering loaded data can improve the performance for your special purpose, especially when using [LightCells APIs](https://docs2.aspose.com/cells/net/developerguide/technicalarticles/general/using+lightcells+api). Please use the [LoadOptions.LoadFilter](https://apireference.aspose.com/net/cells/aspose.cells/loadoptions/properties/loadfilter) property for this purpose.

The following sample code loads only shape objects while loading the workbook from the [template file](https://docs2.aspose.com/cells/net/attachments/5013590/5115552.xlsx) which you can download from the given link. The following screenshot shows the [template file](https://docs2.aspose.com/cells/net/attachments/5013590/5115552.xlsx) contents and also explains that the data in Red color and Yellow background will not be loaded because [LoadOptions.LoadFilter](https://apireference.aspose.com/net/cells/aspose.cells/loadoptions/properties/loadfilter) property has been set to [LoadDataFilterOptions.Shape](https://apireference.aspose.com/net/cells/aspose.cells/loaddatafilteroptions)

![image](5115554.png)

The following screenshot shows the [output PDF](https://docs2.aspose.com/cells/net/attachments/5013590/5115555.pdf) which you can download from the given link. Here you can see, the data in Red color and Yellow background is not present but all shapes are there.

![image](5115553.png)

