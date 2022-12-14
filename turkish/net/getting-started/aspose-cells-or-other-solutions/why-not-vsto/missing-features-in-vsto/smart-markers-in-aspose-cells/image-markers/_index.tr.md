---
title: Görüntü İşaretleyicileri
type: docs
weight: 20
url: /tr/net/image-markers/
---
Aspose.Cells akıllı işaretleyiciler, görüntü işaretleyicilerini de destekler. Bu bölüm, akıllı işaretleyicileri kullanarak nasıl resim ekleyeceğinizi gösterir.
## **Görüntü Parametreleri**
Görüntüleri yönetmek için akıllı işaretleyici parametreleri.

- **Resim:Hücreye Sığdır** - Görüntüyü hücrenin satır yüksekliğine ve sütun genişliğine otomatik olarak sığdırın.
- **Resim:ÖlçekN** - Yüksekliği ve genişliği yüzde N olarak ölçeklendirin.
- **Resim:Genişlik:Nin&Yükseklik:Nin** - Görüntüyü N inç yüksekliğinde ve N inç genişliğinde oluşturun. ayrıca yapabilirsin
 Sol ve Üst konumları (puan olarak) ayırın.

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Image Markers.xlsx";

//Get the image data.

byte[]imageData = File.ReadAllBytes(FilePath + "Aspose.Cells.png");

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

//imageData = File.ReadAllBytes(FilePath + "Desert.jpg");

//row = t.NewRow();

//row[0]= imageData;

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
## **Örnek Kodu İndir**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Image%20Markers%20%28Aspose.Cells%29.zip)
