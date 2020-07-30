---
title : "Reading CSV File with Multiple Encodings" 
description : "" 
weight : 20441 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/mngworkbooksandworksheets/reading+csv+file+with+multiple+encodings/
---

# Aspose.Cells for .NET : Reading CSV File with Multiple Encodings


Sometimes, your CSV file contains multiple Encodings (Unicode, ANSI, UTF8, UTF7, etc). Aspose.Cells allows you to load such CSV files and converting them into other formats, for example, PDF or XLSX.

Aspose.Cells provides the [TxtLoadOptions.IsMultiEncoded](https://apireference.aspose.com/net/cells/aspose.cells/txtloadoptions/properties/ismultiencoded) property, which you need to set to **true** to load your CSV file with multiple encodings properly.

The following screenshot shows a sample CSV file that contains two lines. The first line is in **ANSI** encoding and the second line is in **Unicode** encoding

{{< table style="table-striped" >}}
|Input file|
|:----|
|![](https://docs2.aspose.com/cells/net/attachments/5017651/5112225.png)|
{{< /table >}}

The following screenshot shows the XLSX file converted from the above CSV file without setting the [TxtLoadOptions.IsMultiEncoded](https://apireference.aspose.com/net/cells/aspose.cells/txtloadoptions/properties/ismultiencoded) property to **true**. As you can see, the Unicode text was not converted properly.

{{< table style="table-striped" >}}
|Output file 1: no accommodation made for multiple encoding|
|:----|
|![](https://docs2.aspose.com/cells/net/attachments/5017651/5112226.png)|
{{< /table >}}

The following screenshot shows the XSLX file converted from the above CSV file after setting the [TxtLoadOptions.IsMultiEncoded](https://apireference.aspose.com/net/cells/aspose.cells/txtloadoptions/properties/ismultiencoded) property to **true**. As you can see, the Unicode text is now converted properly.

{{< table style="table-striped" >}}
|Output file 2: IsMultiEncoded is set to true|
|:----|
|![](https://docs2.aspose.com/cells/net/attachments/5017651/5112227.png)|
{{< /table >}}

Below is the sample code that converts the above CSV file into XLSX format properly.

  
  

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Muti-Encoded-CSV-File.Png](https://docs2.aspose.com/cells/net/attachments/5017651/5112225.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [CSV-File-Coverted-To-XLSX-Without-Setting-IsMultiEncoded-True.Png](https://docs2.aspose.com/cells/net/attachments/5017651/5112226.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [CSV-File-Converted-To-XLSX.Png](https://docs2.aspose.com/cells/net/attachments/5017651/5112227.png) (image/png)  

