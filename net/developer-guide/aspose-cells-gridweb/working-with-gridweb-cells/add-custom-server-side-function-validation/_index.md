---
title: Add Custom Server-side Function Validation
type: docs
weight: 110
url: /net/add-custom-server-side-function-validation/
---

## **Possible Usage Scenarios**
Sometimes, you might require to implement data validation on server-side. Aspose.Cells.GridWeb allows you to add custom server-side data validation. You have to specify the cell range or area. You can also set client-side validation functions for callbacks with custom server side validation.
## **Add Custom Server-side Function Validation**
You need to set the server validation class which implements the **GridCustomServerValidation** interface via **GridValidation.ServerValidation** attribute. You also need to set the client-side validation function (it should be written in JavaScript on client-side), this function is compulsory to validate the data on client end on callback. You can set the error message string via **GridValidation.ErrorMessage** and title via **GridValidation.ErrorTitle** properties for your needs. Please see a series of screenshots that show how it works (step by step) in a given scenario after executing the sample code below.  In the example, you cannot update data in B2:C3 cells. When you try to edit those cells in the sheet, you will be prompted some error messages and previous value would be restored. You may open Console window (in your browser) to print cell's info/details for certain events. 

![todo:image_alt_text](add-custom-server-side-function-validation_1.png)

![todo:image_alt_text](add-custom-server-side-function-validation_2.png)

![todo:image_alt_text](add-custom-server-side-function-validation_3.png)

![todo:image_alt_text](add-custom-server-side-function-validation_4.png)

![todo:image_alt_text](add-custom-server-side-function-validation_5.png)
## **Sample Code**
{{< gist "aspose-cells" "18f6c28b77ee30c773fb2199168e73ed" "Cells-AddCustomServerSideFunctionValidation.aspx.cs" >}}
