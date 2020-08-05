---
title : "Render Unicode Supplementary characters in output Pdf by Aspose.Cells" 
description : "" 
weight : 20390 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/rnd-prt/render+unicode+supplementary+characters+in+output+pdf+by+aspose.cells/
---

# Aspose.Cells for .NET : Render Unicode Supplementary characters in output Pdf by Aspose.Cells


Normal Unicode characters are 2-bytes long while Unicode Supplementary characters are 4-bytes long. Aspose.Cells now supports rendering of these 4-bytes Unicode characters.

In the Unicode Character Standard, Supplementary Characters are the characters assigned code points from U+10000 to U+10FFFF. In other words, these are the Unicode characters greater than U+FFFF.

*   In UTF-8 these characters are each 4 bytes long.
*   In UTF-16 these characters require 2 surrogates (16-bit units).

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Render Unicode Supplementary characters in output Pdf by Aspose.Cells](#render-unicode-supplementary-characters-in-output-pdf-by-aspose.cells)
    *   1.1 [Programming Sample](#programming-sample)
{{< /panel >}}
 

 

## Render Unicode Supplementary characters in output Pdf by Aspose.Cells

The following screenshot shows how Aspose.Cells rendered the [source excel file](https://docs2.aspose.com/cells/net/attachments/5013576/5115563.xlsx) into the [output pdf](https://docs2.aspose.com/cells/net/attachments/5013576/5115564.pdf). As you can see all three Unicode Supplementary characters have been rendered exactly same as done by Microsoft Excel.

![image](http://i.imgsafe.org/20ee6a3f85.png)

### Programming Sample

You can use this sample code to convert [source excel file](https://docs2.aspose.com/cells/net/attachments/5013576/5115563.xlsx) into [output pdf](https://docs2.aspose.com/cells/net/attachments/5013576/5115564.pdf).

  
  

