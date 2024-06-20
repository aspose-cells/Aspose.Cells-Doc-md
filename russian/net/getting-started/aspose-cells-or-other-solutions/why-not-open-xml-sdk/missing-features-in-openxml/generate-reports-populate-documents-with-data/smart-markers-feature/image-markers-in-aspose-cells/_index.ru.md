---
title: Изображения в Aspose.Cells
type: docs
weight: 20
url: /ru/net/image-markers-in-aspose-cells/
---

Умные маркеры Aspose.Cells также поддерживают изображения. Этот раздел покажет вам, как вставлять изображения с помощью умных маркеров.
## **Параметры изображения**
Умные маркеры для управления изображениями.

- **Изображение:FitToCell** - Автоматически подгонять изображение под высоту строки и ширину столбца.
- **Изображение:МасштабN** - Масштабировать высоту и ширину до N процентов.
- **Изображение:Ширина:Nдюймов&Высота:Nдюймов** - Отобразить изображение высотой N дюймов и шириной N дюймов. Вы также можете
  указать позиции Left и Top (в точках).

{{< highlight csharp >}}

 //Get the image data.

byte[] imageData = File.ReadAllBytes("Thumbnail.jpg");

//Create a datatable.

DataTable t = new DataTable("Table1");

//Add a column to save pictures.

DataColumn dc = t.Columns.Add("Picture");

//Set its data type.

dc.DataType = typeof(object);

//Add a new new record to it.

DataRow row = t.NewRow();

row[0] = imageData;

t.Rows.Add(row);

//Add another record (having picture) to it.

imageData = File.ReadAllBytes("Desert.jpg");

row = t.NewRow();

row[0] = imageData;

t.Rows.Add(row);

//Create WorkbookDesigner object.

WorkbookDesigner designer = new WorkbookDesigner();

//Open the temple Excel file.

designer.Workbook = new Workbook("ImageSmartBook.xls");

//Set the datasource.

designer.SetDataSource(t);

//Process the markers.

designer.Process();

//Save the Excel file.

designer.Workbook.Save("out_ImageSmartBook.xls");

{{< /highlight >}}
## **Загрузить образец кода**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Image%20Markers%20%28Aspose.Cells%29.zip)
