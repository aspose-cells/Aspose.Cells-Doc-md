---
title: Aspose.Cells'de Excel XP'den bu yana Gelişmiş Koruma Ayarları
type: docs
weight: 20
url: /tr/net/advanced-protection-settings-since-excel-xp-in-aspose-cells/
---
{{% alert color="primary" %}}

- Satırları veya sütunları silin.
- İçeriği, nesneleri veya senaryoları düzenleyin.
- Hücreleri, satırları veya sütunları biçimlendirin.
- Satırları, sütunları veya köprüleri ekleyin.
- Kilitli veya kilidi açılmış hücreleri seçin.
- Pivot tabloları ve çok daha fazlasını kullanın.

Aspose.Cells, Excel XP veya sonraki sürümleri tarafından sunulan tüm gelişmiş koruma ayarlarını destekler.

{{% /alert %}}

## **Excel XP ve Sonraki Sürümleri Kullanan Gelişmiş Koruma Ayarları**

Excel XP'de bulunan koruma ayarlarını görüntülemek için:

1.  itibaren**Aletler** menü, seç**Koruma** bunu takiben**Sayfayı Koruyun**.
 Bir iletişim kutusu görüntülenir.

   **Excel XP'de koruma seçeneklerini gösteren iletişim kutusu**

![yapılacaklar:resim_alternatif_Metin](advanced-protection-settings-since-excel-xp-in-aspose-cells_1.png)

1. Çalışma sayfası özelliklerine izin verin veya bunları kısıtlayın ya da bir parola uygulayın.

### **Aspose.Cells Kullanarak Gelişmiş Koruma Ayarları**

Aspose.Cells, tüm gelişmiş koruma ayarlarını destekler.

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon. Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf.

 bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf sağlar[**Koruma**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection)Bu gelişmiş koruma ayarlarını uygulamak için kullanılan özellik. bu[**Koruma**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) mülkiyet aslında bir nesnedir[**Koruma**](https://reference.aspose.com/cells/net/aspose.cells/protection) kısıtlamaları devre dışı bırakmak veya etkinleştirmek için çeşitli Boolean özelliklerini kapsayan sınıf.

Aşağıda küçük bir örnek uygulama var. Bir Excel dosyasını açar ve Excel XP ve sonraki sürümleri tarafından desteklenen gelişmiş koruma ayarlarının çoğunu kullanır.

**C#**

{{< highlight "csharp" >}}

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

## **Örnek Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
