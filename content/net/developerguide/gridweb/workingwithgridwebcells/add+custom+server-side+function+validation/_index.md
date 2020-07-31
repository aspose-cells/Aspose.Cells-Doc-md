---
title : "Add Custom Server-side Function Validation" 
description : "" 
weight : 16720 
toc : false
type: docs
url: /net/developerguide/gridweb/workingwithgridwebcells/add+custom+server-side+function+validation/
---

# Aspose.Cells for .NET : Add Custom Server-side Function Validation


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Add Custom Server-side Function Validation](#add-custom-server-side-function-validation)
*   3 [Sample Code](#sample-code)
{{< /panel >}}
 

## Possible Usage Scenarios

Sometimes, you might require to implement data validation on server-side. Aspose.Cells.GridWeb allows you to add custom server-side data validation. You have to specify the cell range or area. You can also set client-side validation functions for callbacks with custom server side validation.

## Add Custom Server-side Function Validation

You need to set the server validation class which implements the **GridCustomServerValidation** interface via **GridValidation.ServerValidation** attribute. You also need to set the client-side validation function (it should be written in JavaScript on client-side), this function is compulsory to validate the data on client end on callback. You can set the error message string via **GridValidation.ErrorMessage** and title via **GridValidation.ErrorTitle** properties for your needs. Please see a series of screenshots that show how it works (step by step) in a given scenario after executing the sample code below.  In the example, you cannot update data in B2:C3 cells. When you try to edit those cells in the sheet, you will be prompted some error messages and previous value would be restored. You may open Console window (in your browser) to print cell's info/details for certain events. 

![](https://docs2.aspose.com/cells/net/attachments/64455551/64716863.png)

![](https://docs2.aspose.com/cells/net/attachments/64455551/64716864.png)

![](https://docs2.aspose.com/cells/net/attachments/64455551/64716865.png)

![](https://docs2.aspose.com/cells/net/attachments/64455551/64716866.png)

![](https://docs2.aspose.com/cells/net/attachments/64455551/64716867.png)

## Sample Code

