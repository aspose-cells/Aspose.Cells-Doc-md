---
title: Görsel İşaretleyiciler
type: docs
weight: 20
url: /tr/net/image-markers/
---

Aspose.Cells akıllı işaretçileri ayrıca görüntü işaretçilerini de destekler. Bu bölüm size akıllı işaretçileri kullanarak resim eklemenin nasıl yapıldığını gösterir.
## **Görüntü Parametreleri**
Resimleri yönetmek için akıllı işaretçi parametreleri.

- **Resim:HücreyeSığdır** - Resmi hücrenin satır yüksekliğine ve sütun genişliğine otomatik sığdır.
- **Resim:ÖlçekN** - Yüksekliği ve genişliği N yüzde ölçekle.
- **Resim:Genişlik:Nin&Yükseklik:Nin** - Görüntüyü N inç yükseklikte ve N inç genişlikte oluşturun. Ayrıca sol ve üst pozisyonları (noktalarda) belirtebilirsiniz.
  Örnek Kodunu İndir

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
## **Örnek Kod İndir**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Image%20Markers%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
