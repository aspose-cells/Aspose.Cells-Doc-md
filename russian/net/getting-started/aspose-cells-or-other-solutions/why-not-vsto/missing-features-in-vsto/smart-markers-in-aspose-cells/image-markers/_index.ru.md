---
title: Маркеры изображений
type: docs
weight: 20
url: /ru/net/image-markers/
---

Умные маркеры Aspose.Cells также поддерживают изображения. Этот раздел покажет вам, как вставлять изображения с помощью умных маркеров.
## **Параметры изображения**
Умные маркеры для управления изображениями.

- **Изображение:FitToCell** - Автоматически подгонять изображение под высоту строки и ширину столбца.
- **Изображение:МасштабN** - Масштабировать высоту и ширину до N процентов.
- **Изображение:Ширина:Nдюймов&Высота:Nдюймов** - Отобразить изображение высотой N дюймов и шириной N дюймов. Вы также можете
  указать позиции Left и Top (в точках).

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Image Markers.xlsx";

//Get the image data.

byte[] imageData = File.ReadAllBytes(FilePath + "Aspose.Cells.png");

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

//imageData = File.ReadAllBytes(FilePath + "Desert.jpg");

//row = t.NewRow();

//row[0] = imageData;

//t.Rows.Add(row);

//Create WorkbookDesigner object.

WorkbookDesigner designer = new WorkbookDesigner();

//Open the temple Excel file.

designer.Workbook = new Workbook(FileName);

//Set the datasource.

designer.SetDataSource(t);

//Process the markers.

designer.Process();

//Save the Excel file.

designer.Workbook.Save(FileName);

{{< /highlight >}}
## **Загрузить образец кода**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Image%20Markers%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
