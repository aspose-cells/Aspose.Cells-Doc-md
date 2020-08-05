---
title : "Render Unicode Supplementary characters in output PDF by Aspose.Cells" 
description : "" 
weight : 12536 
toc : false
type: docs
url: /java/developerguide/technicalarticles/render+unicode+supplementary+characters+in+output+pdf+by+aspose.cells/
---

# Aspose.Cells for Java : Render Unicode Supplementary characters in output PDF by Aspose.Cells


Normal Unicode characters are 2-bytes long while Unicode Supplementary characters are 4-bytes long. Aspose.Cells now supports rendering of these 4-bytes Unicode characters.

In the Unicode Character Standard, Supplementary Characters are the characters assigned code points from U+10000 to U+10FFFF. In other words, these are the Unicode characters greater than U+FFFF.

*   In UTF-8 these characters are each 4 bytes long.
*   In UTF-16 these characters require 2 surrogates (16-bit units).

#### Render Unicode Supplementary characters in output PDF by Aspose.Cells

The following screenshot shows how Aspose.Cells rendered the [source excel file](https://docs2.aspose.com/cells/java/attachments/5276130/5473390.xlsx) into the [output PDF](https://docs2.aspose.com/cells/java/attachments/5276130/5473391.pdf). As you can see all three Unicode Supplementary characters have been rendered exactly the same as done by Microsoft Excel.

![image](https://docs2.aspose.com/cells/java/attachments/5276130/5473392.png)

You can use this sample code to convert the [source excel file](https://docs2.aspose.com/cells/java/attachments/5276130/5473390.xlsx) into [output PDF](https://docs2.aspose.com/cells/java/attachments/5276130/5473391.pdf).


