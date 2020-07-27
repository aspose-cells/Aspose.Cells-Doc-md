+++
title = "Copy Sparkline by Specifying Data Range and Location of Sparkline Group" 
description = "" 
weight = 20527 
+++

Aspose.Cells for .NET : Copy Sparkline by Specifying Data Range and Location of Sparkline Group  

# Aspose.Cells for .NET : Copy Sparkline by Specifying Data Range and Location of Sparkline Group


Microsoft Excel allows you to copy a sparkline by specifying the data range and location of a sparkline group. Aspose.Cells supports this feature.

To copy a sparkline to other cells in Microsoft Excel:

1.  Select the cell containing the sparkline.
2.  Select **Edit Data** from the **Sparkline** section of the **Design** tab.
3.  Select **Edit Group Location & Data**.
4.  Specify the data range and location.
5.  Click **OK**.

Aspose.Cells provides the `SparklineCollection.Add(dataRange, row, column)` method to specify a sparkline group's data range and location. The following sample code loads the source Excel file as shown in the screenshot above, then accesses the first sparkline group and adds data ranges and locations in the sparkline group. Finally, it writes the output Excel file on disk which is also shown in the screenshot above.

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [sparklines-source-excel-file.png](https://docs2.aspose.com/cells/net/attachments/5017335/5112344.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [sparklines-output-excel-file.png](https://docs2.aspose.com/cells/net/attachments/5017335/5112345.png) (image/png)  

