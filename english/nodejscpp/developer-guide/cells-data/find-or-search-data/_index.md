---  
title: Find or Search Data
type: docs  
weight: 50  
url: /nodejs-cpp/find-or-search-data/  
description: Learn how to find or search cells in a worksheet that contains specified data through the Aspose.Cells for Node.js via C++ API.  
keywords: Find data Node.js via C++, Search data Node.js via C++, Find Cells Containing a Formula Node.js via C++, Search Cells Containing a Formula Node.js via C++, Find Data or Formulas using FindOptions Node.js via C++, Search Data or Formulas using FindOptions Node.js via C++, Find or Search Cells Containing Specified String Value or Number Node.js via C++, Find or Search cells contains specified data  
---  

{{% alert color="primary" %}}  
Microsoft Excel allows users to find cells in a worksheet that contain specified data.  
{{% /alert %}}  

## **Finding Cells Containing Specified Data**  

### **Using Microsoft Excel**  

Microsoft Excel allows users to find cells in a worksheet that contain specified data. If you select **Edit** from the **Find** menu in Microsoft Excel, you will see a dialog where you can specify the search value.  

Here, we are looking for the value "Oranges". Aspose.Cells also allows developers to find cells in the worksheet containing specified values.  

### **Using Aspose.Cells for Node.js via C++**  

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class contains a [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class provides a [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) collection that represents all cells in the worksheet. The [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) collection provides several methods for finding cells in a worksheet containing user-specified data. A few of these methods are discussed below in more detail.  

{{% alert color="primary" %}}  
All Find methods return the references of the cells containing the specified data to search.  
{{% /alert %}}  

## **Finding Cells Containing a Formula**  

Developers can find a specified formula in the worksheet by calling the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) collection's [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-) method. Typically, the [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-) method accepts three parameters:  

- **Object:** The object to search for. The type should be int, double, DateTime, string, bool.  
- **Previous cell:** Previous cell with the same object. This parameter can be set to null if searching from the start.  
- **FindOptions:** Options for finding the required object.  

The examples below use worksheet data for practicing find methods:  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-FindCellsContainFormula.js" >}}


## **Finding Data or Formulas using FindOptions**  

It is possible to find specified values using the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) collection's [**Cells.find(object, Cell)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-) method with various [**FindOptions**](https://reference.aspose.com/cells/nodejs-cpp/findoptions). Typically, the [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-) method accepts the following parameters:  

- **Search value**, the data or value to be searched for.  
- **Previous cell**, the last cell that contained the same value. This parameter can be set to null when searching from the start.  
- **Find options**, the find options.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-FindDataUsingFindOptions.js" >}}


## **Finding Cells Containing Specified String Value or Number**  

It is possible to find specified string values by calling the same [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-) method found in the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) collection with various [**FindOptions**](https://reference.aspose.com/cells/nodejs-cpp/findoptions).  

Specify the [**FindOptions.setLookInType**](https://reference.aspose.com/cells/nodejs-cpp/findoptions/#setLookInType-lookintype-) and [**FindOptions.setLookAtType**](https://reference.aspose.com/cells/nodejs-cpp/findoptions/#setLookAtType-lookattype-) properties. The following example code illustrates how to use these properties to find cells with various number of strings at the **beginning** or at the **center** or at the **end** of the cell's string.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-FindCellsContainSpecifyString.js" >}}



## **Advance topics**  
- [Find Cells with Specific Style](/cells/nodejs-cpp/find-cells-with-specific-style/)  
- [Find if the cell value starts with single quote mark](/cells/nodejs-cpp/find-if-the-cell-value-starts-with-single-quote-mark/)  
- [Search Data using Original Values](/cells/nodejs-cpp/search-data-using-original-values/)  
  
{{< app/cells/assistant language="nodejs-cpp" >}}