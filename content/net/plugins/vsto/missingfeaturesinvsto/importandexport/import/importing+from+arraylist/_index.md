---
title : "Importing from ArrayList" 
description : "" 
weight : 24832 
toc : false
type: docs
url: /net/plugins/vsto/missingfeaturesinvsto/importandexport/import/importing+from+arraylist/
---

# Aspose.Cells for .NET : Importing from ArrayList


Developers can import data from an ArrayList to their worksheets by calling the **ImportArrayList** method of the Cells collection. ImportArray method takes the following parameters: **ArrayList** , represents the ArrayList object whose contents need to import

*   Row Number , represents the row number of the first cell where the data will be imported
*   Column Number , represents the column number of the first cell where the data will be imported
*   Is Vertical , a boolean value that specifies to import data vertically or horizontally

{{< code lang="cs" >}}
//Instantiating a Workbook object
Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object
int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index
Worksheet worksheet = workbook.Worksheets[i];
//Instantiating an ArrayList object
ArrayList list = new ArrayList();

//Add few names to the list as string values
list.Add("laurence chen");
list.Add("roman korchagin");
list.Add("kyle huang");
list.Add("tommy wang");

//Importing the contents of ArrayList to 1st row and first column vertically
worksheet.Cells.ImportArrayList(list, 0, 0, true);

//Saving the Excel file
workbook.Save("DataImport from Array List.xls");

{{< /code >}}

