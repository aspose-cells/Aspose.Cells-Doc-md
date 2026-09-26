---  
title: Copy VBA Macro UserForm DesignerStorage from Template to Target Workbook with Golang via C++  
linktitle: Copy VBA Macro UserForm DesignerStorage  
type: docs  
weight: 130  
url: /go-cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/  
description: Learn how to copy VBA Macro UserForm DesignerStorage from a template to a target workbook using Aspose.Cells for Go via C++.  
---  

## **Possible Usage Scenarios**  

Aspose.Cells allows you to copy a VBA project from one Excel file into another Excel file. A VBA project consists of various types of modules, such as Document, Procedural, Designer, etc. All modules can be copied with simple code, but for the Designer module there is extra data called Designer Storage that must be accessed or copied. The following two methods deal with Designer Storage:  

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/go-cpp/vbamodulecollection/getdesignerstorage/)  
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/go-cpp/vbamodulecollection/adddesignerstorage/)  

## **Copy VBA Macro UserForm DesignerStorage from Template to Target Workbook**  

Please see the following sample code. It copies the VBA project from the [template Excel file](50528345.xlsm) into an empty workbook and saves it as the [output Excel file](50528346.xlsm). If you open the VBA project inside the template Excel file, you will see a User Form as shown below. The User Form consists of Designer Storage, so it will be copied using [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/go-cpp/vbamodulecollection/getdesignerstorage/) and [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/go-cpp/vbamodulecollection/adddesignerstorage/) methods.  

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**  

The following screenshot shows the output Excel file and its contents, which were copied from the template file. When you click Button 1, it opens the VBA User Form, which contains a command button that displays a message box when clicked.  

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**  

## **Sample Code**  

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyVbaMacroUserformDesignerstorageFromTemplateToTargetWorkbook.go" >}}
{{< app/cells/assistant language="go" >}}
