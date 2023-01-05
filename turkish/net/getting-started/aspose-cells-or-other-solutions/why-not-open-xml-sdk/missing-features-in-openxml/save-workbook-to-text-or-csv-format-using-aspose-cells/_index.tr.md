---
title: Aspose.Cells'i kullanarak Çalışma Kitabını Metne veya CSV Formatına Kaydet
type: docs
weight: 80
url: /tr/net/save-workbook-to-text-or-csv-format-using-aspose-cells/
---
{{% alert color="primary" %}} 

Bazen, birden çok çalışma sayfası içeren bir çalışma kitabını metin biçimine dönüştürmek veya kaydetmek istersiniz. Metin biçimleri için (örneğin TXT, TabDelim, CSV vb.), hem Microsoft Excel hem de Aspose.Cells varsayılan olarak yalnızca etkin çalışma sayfasının içeriğini kaydeder.

{{% /alert %}} 

Aşağıdaki kod örneği, tüm çalışma kitabının metin biçiminde nasıl kaydedileceğini açıklar. Herhangi bir sayıda çalışma sayfası içeren herhangi bir Microsoft Excel veya OpenOffice elektronik tablo dosyası (yani XLS, XLSX, XLSM, XLSB, ODS vb.) olabilecek kaynak çalışma kitabını yükleyin.

Kod yürütüldüğünde, çalışma kitabındaki tüm sayfaların verilerini TXT biçimine dönüştürür.

Dosyanızı CSV'e kaydetmek için aynı örneği değiştirebilirsiniz. Varsayılan olarak, TxtSaveOptions.Separator virgüldür, bu nedenle CSV biçiminde kaydediyorsanız ayırıcı belirtmeyin.

**C#**

{{< highlight "csharp" >}}

string FilePath = @"..\..\..\Örnek Dosyalar\";

string FileName = FilePath + "Çalışma Kitabını Metne veya CSV Format.xlsx'e Kaydet";

string destFileName = FilePath + "Çalışma Kitabını Metne veya CSV Format.txt'ye Kaydet";

//Kaynak çalışma kitabınızı yükleyin

Çalışma kitabı çalışma kitabı = yeni Çalışma Kitabı(DosyaAdı);

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

File.WriteAllBytes(destFileName, workbookData);

{{< /highlight >}}
## **Örnek Kodu İndir**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Save%20Workbook%20to%20Text%20or%20CSV%20Format)

## **Çalışan Örneği İndirin**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
