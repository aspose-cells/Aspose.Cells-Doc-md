---
title: Aspose.Cells te Excel XP den beri gelişmiş koruma ayarları
type: docs
weight: 20
url: /tr/net/advanced-protection-settings-since-excel-xp-in-aspose-cells/
---

{{% alert color="primary" %}}

- Satırları veya sütunları sil.
- İçerik, nesneler veya senaryoları düzenle.
- Hücreleri, satırları veya sütunları biçimlendir.
- Satırları, sütunları veya hyperlinkleri ekle.
- Kilitli veya kilitsiz hücreleri seç.
- Özet tabloları ve çok daha fazlasını kullanın.

Aspose.Cells, Excel XP veya sonraki sürümlerinin sunduğu tüm gelişmiş koruma ayarlarını destekler.

{{% /alert %}}

## **Excel XP'de bulunan koruma ayarlarını görüntülemek için:**

**Araçlar** menüsünden **Koruma** ardından **Sayfayı Koru**'yu seçin.

Bir iletişim kutusu görüntülenir.
   Bir iletişim kutusu görüntülenir.

   **Excel XP'de koruma seçeneklerini gösteren iletişim kutusu**

![todo:image_alt_text](advanced-protection-settings-since-excel-xp-in-aspose-cells_1.png)

1. İzinleri belirleyin veya kısıtlayın veya bir şifre uygulayın.

### **Aspose.Cells Kullanarak Gelişmiş Koruma Ayarları**

Aspose.Cells, tüm gelişmiş koruma ayarlarını destekler.

Aspose.Cells, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her bir çalışma sayfasına erişim izni veren bir [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı tarafından temsil edilir.

[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı, bu gelişmiş koruma ayarlarını uygulamak için kullanılan [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) özelliğini sağlar. Aslında, [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) özelliği, engelleme veya kısıtlamaları etkinleştirmek veya devre dışı bırakmak için birkaç Boolean özelliği kapsayan [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/protection) sınıfından bir nesnedir.

Aşağıda küçük bir örnek uygulama bulunmaktadır. Bir Excel dosyası açar ve Excel XP ve sonraki sürümler tarafından desteklenen gelişmiş koruma ayarlarının çoğunu kullanır.

**C#**

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook excel = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = excel.Worksheets[0];

//Restricting users to delete columns of the worksheet

worksheet.Protection.AllowDeletingColumn = false;

//Restricting users to delete row of the worksheet

worksheet.Protection.AllowDeletingRow = false;

//Restricting users to edit contents of the worksheet

worksheet.Protection.AllowEditingContent = false;

//Restricting users to edit objects of the worksheet

worksheet.Protection.AllowEditingObject = false;

//Restricting users to edit scenarios of the worksheet

worksheet.Protection.AllowEditingScenario = false;

//Restricting users to filter

worksheet.Protection.AllowFiltering = false;

//Allowing users to format cells of the worksheet

worksheet.Protection.AllowFormattingCell = true;

//Allowing users to format rows of the worksheet

worksheet.Protection.AllowFormattingRow = true;

//Allowing users to insert columns in the worksheet

worksheet.Protection.AllowFormattingColumn = true;

//Allowing users to insert hyperlinks in the worksheet

worksheet.Protection.AllowInsertingHyperlink = true;

//Allowing users to insert rows in the worksheet

worksheet.Protection.AllowInsertingRow = true;

//Allowing users to select locked cells of the worksheet

worksheet.Protection.AllowSelectingLockedCell = true;

//Allowing users to select unlocked cells of the worksheet

worksheet.Protection.AllowSelectingUnlockedCell = true;

//Allowing users to sort

worksheet.Protection.AllowSorting = true;

//Allowing users to use pivot tables in the worksheet

worksheet.Protection.AllowUsingPivotTable = true;

//Saving the modified Excel file

excel.Save("output.xls", SaveFormat.Excel97To2003);

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Advanced%20Protection%20Settings)

## **Örnek Kod İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
{{< app/cells/assistant language="csharp" >}}
