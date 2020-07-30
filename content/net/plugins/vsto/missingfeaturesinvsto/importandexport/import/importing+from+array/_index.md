---
title : "Importing from Array" 
description : "" 
weight : 24831 
toc : false
type: docs
url: /net/plugins/vsto/missingfeaturesinvsto/importandexport/import/importing+from+array/
---

# Aspose.Cells for .NET : Importing from Array


Developers can import data from an array to their worksheets by calling the **ImportArray** method of the Cells collection. There are many overloaded versions of the ImportArray method but a typical overload takes the following parameters:

*   Array, represents the array object whose contents need to import
*   Row Number, represents the row number of the first cell where the data will be imported
*   Column Number, represents the column number of the first cell where the data will be imported
*   Is Vertical, a boolean value that specifies to import data vertically or horizontally

{{< code lang="cs" >}}
//Instantiating a Workbook object
Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object
int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index
Worksheet worksheet = workbook.Worksheets[i];

//Creating an array containing names as string values
string[] names = new string[] { "laurence chen", "roman korchagin", "kyle huang" };

//Importing the array of names to 1st row and first column vertically
worksheet.Cells.ImportArray(names, 0, 0, true);

//Saving the Excel file
workbook.Save("DataImport from Array.xls");
{{< /code >}}

