---
title: Generate Conditional Formatting DataBars Images
description: Aspose.Cells for Python via .NET is a Python library for working with spreadsheet files. It supports the generation of conditionally formatted data bars and images, allowing users to customize the display of the spreadsheet based on the value of the cells. This article will introduce how to use the Aspose.Cells for Python via library to generate conditionally formatted data bars and images.
keywords: Aspose.Cells for Python via .NET, Conditional Formatting, Data Bars, Images, Spreadsheets
type: docs
weight: 40
url: /python-net/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

Sometimes, you need to generate images of Conditional Formatting DataBars. You can use Aspose.Cells [**DataBar.to_image()**](https://reference.aspose.com/cells/python-net/aspose.cells/databar/to_image) method to generate these images. This article shows how to generate a DataBar image using Aspose.Cells for Python via .NET.

{{% /alert %}}

The following sample code generates the DataBar image of cell C1. First, it accesses the format condition object of the cell, and then from that object, it accesses the [**DataBar**](https://reference.aspose.com/cells/python-net/aspose.cells/databar) object and uses its [**to_image()**](https://reference.aspose.com/cells/python-net/aspose.cells/databar/to_image) method to generate the image of the cell. Finally, it saves the image on disk.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-GenerateDatabarImage-1.py" >}}
