---  
title: Output Blank Page when there is Nothing to Print with Golang via C++  
linktitle: Output Blank Page when there is Nothing to Print  
type: docs  
weight: 90  
url: /go-cpp/output-blank-page-when-there-is-nothing-to-print/  
description: Handle empty worksheets and print blank pages with Aspose.Cells using C++.  
---  

## **Possible Usage Scenarios**  

If the sheet is empty, then Aspose.Cells will not print anything when you export the worksheet to an image. You can change this behavior by using [**ImageOrPrintOptions.GetOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/getoutputblankpagewhennothingtoprint/) property. When you set it **to** true, it will print the blank page.  

## **Output Blank Page when there is Nothing to Print**  

The following sample code creates an empty workbook **that** has an empty worksheet and renders the empty worksheet to an image after setting the [**ImageOrPrintOptions.GetOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/getoutputblankpagewhennothingtoprint/) property **to** true. Consequently, it generates a blank page, **as** there is nothing to print, which you can see in the image below.  

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)  

## **Sample Code**  

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OutputBlankPageWhenThereIsNothingToPrint.go" >}}  
{{< app/cells/assistant language="go" >}}
