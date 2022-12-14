---
title: Çalışma Kitabını Aspose.Cells'de Metin veya CSV Biçiminde Kaydet
type: docs
weight: 110
url: /tr/net/save-workbook-to-text-or-csv-format-in-aspose-cells/
---
{{% alert color="primary" %}} 

Bazen, birden çok çalışma sayfası içeren bir çalışma kitabını metin biçimine dönüştürmek veya kaydetmek istersiniz. Metin biçimleri için (örneğin TXT, TabDelim, CSV vb.), varsayılan olarak hem Microsoft Excel hem de Aspose.Cells yalnızca etkin çalışma sayfasının içeriğini kaydeder.

{{% /alert %}} 

Aşağıdaki kod örneği, tüm çalışma kitabının metin biçiminde nasıl kaydedileceğini açıklar. Herhangi bir sayıda çalışma sayfası içeren herhangi bir Microsoft Excel veya OpenOffice elektronik tablo dosyası (yani XLS, XLSX, XLSM, XLSB, ODS vb.) olabilecek kaynak çalışma kitabını yükleyin.

Kod yürütüldüğünde, çalışma kitabındaki tüm sayfaların verilerini TXT biçimine dönüştürür.

Dosyanızı CSV'ye kaydetmek için aynı örneği değiştirebilirsiniz. Varsayılan olarak, TxtSaveOptions.Separator virgüldür, bu nedenle CSV biçiminde kaydediyorsanız ayırıcı belirtmeyin.

**C#**

{{< highlight "csharp" >}}

 string filePath = "kaynak.xlsx";

//Kaynak çalışma kitabınızı yükleyin

Çalışma kitabı çalışma kitabı = yeni Çalışma Kitabı(filePath);

//0 baytlık dizi

bayt[]çalışma kitabıVerileri = yeni bayt[0];

//Metin kaydetme seçenekleri. Her türlü ayırıcıyı kullanabilirsiniz

TxtSaveOptions seçimleri = new TxtSaveOptions();

opts.Separator = '\t';

//Her çalışma sayfası verisini, çalışma kitabı veri dizisinin içindeki metin biçiminde kopyalayın

 için (int idx = 0; idx< workbook.Worksheets.Count; idx++)

{

    //Save the active worksheet into text format

    MemoryStream ms = new MemoryStream();

    workbook.Worksheets.ActiveSheetIndex = idx;

    workbook.Save(ms, opts);

    //Save the worksheet data into sheet data array

    ms.Position = 0;

    byte[] sheetData = ms.ToArray();

    //Combine this worksheet data into workbook data array

    byte[] combinedArray = new byte[workbookData.Length + sheetData.Length];

    Array.Copy(workbookData, 0, combinedArray, 0, workbookData.Length);

    Array.Copy(sheetData, 0, combinedArray, workbookData.Length, sheetData.Length);

    workbookData = combinedArray;

}

//Save entire workbook data into file

File.WriteAllBytes(filePath + ".out.txt", workbookData);


{{< /highlight >}}
## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Save%20Workbook%20to%20Text%20or%20CSV%20Format)
## **Örnek Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
