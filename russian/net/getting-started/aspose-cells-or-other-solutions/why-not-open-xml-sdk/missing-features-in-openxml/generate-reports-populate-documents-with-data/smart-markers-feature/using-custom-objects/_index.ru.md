---
title: Использование анонимных типов или пользовательских объектов в Aspose.Cells
type: docs
weight: 30
url: /ru/net/using-anonymous-types-or-custom-objects-in-aspose-cells/
---

Aspose.Cells также поддерживает анонимные типы или пользовательские объекты в умных маркерах. В приведенном ниже примере класс Product должен быть определен перед использованием.

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
## **Загрузить образец кода**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Using%20Custom%20Objects%20%28Aspose.Cells%29.zip)
