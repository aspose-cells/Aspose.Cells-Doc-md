---
title: Uso de Tipos Anónimos u Objetos Personalizados en Aspose.Cells
type: docs
weight: 30
url: /es/net/using-anonymous-types-or-custom-objects-in-aspose-cells/
---

Aspose.Cells también admite tipos anónimos u objetos personalizados en los marcadores inteligentes. En el siguiente ejemplo, se necesita definir la clase Producto antes de su uso.

{{< highlight csharp >}}

 //Instantiate the workbookdesigner object.

WorkbookDesigner report = new WorkbookDesigner();

//Get the first worksheet(default sheet) in the workbook.

Aspose.Cells.Worksheet w = report.Workbook.Worksheets[0];

//Input some markers to the cells.

w.Cells["A1"].PutValue("Test");

w.Cells["A2"].PutValue("&=MyProduct.Name");

w.Cells["B2"].PutValue("&=MyProduct.Age");

//Instantiate the list collection based on the custom class.

IList<MyProduct> list = new List<MyProduct>();

//Provide values for the markers using the custom class object.

list.Add(new MyProduct("Simon", 30));

list.Add(new MyProduct("Johnson", 33));

//Set the data source.

report.SetDataSource("MyProduct", list);

//Process the markers.

report.Process(false);

//Save the excel file.

report.Workbook.Save("Smart Marker Customobjects.xls");

{{< /highlight >}}
## **Descargar Código de Ejemplo**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Using%20Custom%20Objects%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
