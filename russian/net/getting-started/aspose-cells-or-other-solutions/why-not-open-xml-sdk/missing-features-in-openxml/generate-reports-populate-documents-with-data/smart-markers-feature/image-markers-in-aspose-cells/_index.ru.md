---
title: Маркеры изображений в Aspose.Cells
type: docs
weight: 20
url: /ru/net/image-markers-in-aspose-cells/
---
Aspose.Cells интеллектуальные маркеры также поддерживают маркеры изображений. В этом разделе показано, как вставлять изображения с помощью интеллектуальных маркеров.
## **Параметры изображения**
Параметры интеллектуального маркера для управления изображениями.

- **Изображение: FitToCell** - Автоматически подгонять изображение к высоте строки ячейки и ширине столбца.
- **Изображение:ScaleN** - Масштабировать высоту и ширину до N процентов.
- **Изображение:Ширина:НинВысота:Нин** - Визуализация изображения N дюймов в высоту и N дюймов в ширину. Вы также можете
 укажите Левое и Верхнее положение (в пунктах).

{{< highlight "csharp" >}}

 //Get the image data.

byte[]imageData = File.ReadAllBytes("Thumbnail.jpg");

//Create a datatable.

DataTable t = new DataTable("Table1");

//Add a column to save pictures.

DataColumn dc = t.Columns.Add("Picture");

//Set its data type.

dc.DataType = typeof(object);

//Add a new new record to it.

DataRow row = t.NewRow();

row[0]= imageData;

t.Rows.Add(row);

//Add another record (having picture) to it.

imageData = File.ReadAllBytes("Desert.jpg");

row = t.NewRow();

row[0]= imageData;

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
## **Скачать пример кода**
- [Битбакет](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Image%20Markers%20%28Aspose.Cells%29.zip)
