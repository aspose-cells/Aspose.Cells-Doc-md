---
title : "Converting Excel Files to HTML in Python" 
description : "" 
weight : 24750 
toc : false
type: docs
url: /java/plugins/python/guide/files/utility/converting+excel+files+to+html+in+python/
---

# Aspose.Cells for Java : Converting Excel Files to HTML in Python


## Aspose.Cells - Converting Excel File to HTML

To convert Excel to HTML using Aspose.Cells for Java in Python, simply invoke worksheet\_to\_html() method of Converter module.

**Python Code**

saveFormat = self.SaveFormatworkbook = self.Workbook(self.dataDir + "Book1.xls")#Save the document in PDF formatworkbook.save(self.dataDir + "OutBook1.html", saveFormat.HTML)# Print messageprint "\\n Excel to HTML conversion performed successfully."

## Download Running Code

Download **Converting Excel File to HTML (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
*   [CodePlex](https://asposecellsjavapython.codeplex.com/releases/view/620185)

