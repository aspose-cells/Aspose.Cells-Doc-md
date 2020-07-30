---
title : "Converting To MHTML Files in Python" 
description : "" 
weight : 24752 
toc : false
type: docs
url: /java/plugins/python/guide/files/utility/converting+to+mhtml+files+in+python/
---

# Aspose.Cells for Java : Converting To MHTML Files in Python


## Aspose.Cells - Converting To MHTML

To convert Worksheet to MHTML file using Aspose.Cells for Java in Python, simply invoke worksheet\_to\_mhtml() method of Converter module.

**Python Code**

saveFormat = self.SaveFormat#Specify the file pathfilePath = self.dataDir + "Book1.xlsx"#Specify the HTML saving optionssv = self.HtmlSaveOptions(saveFormat.M\_HTML)#Instantiate a workbook and open the template XLSX filewb = self.Workbook(filePath)#Save the MHT filewb.save(filePath + ".out.mht", sv)# Print messageprint "Excel to MHTML conversion performed successfully."

## Download Running Code

Download **Converting To MHTML (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
*   [CodePlex](https://asposecellsjavapython.codeplex.com/releases/view/620185)

