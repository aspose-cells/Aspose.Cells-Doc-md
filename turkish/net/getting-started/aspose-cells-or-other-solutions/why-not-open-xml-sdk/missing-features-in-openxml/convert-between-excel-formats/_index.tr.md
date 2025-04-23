---
title: Excel Formatları Arasında Dönüştürme
type: docs
weight: 20
url: /tr/net/convert-between-excel-formats/
---

## **Excel'i PDF'ye Dönüştürme**

**PDF** dosyaları, kuruluşlar, devlet sektörleri ve bireyler arasında belge alışverişi için yaygın olarak kullanılır. Standart bir belge formatıdır ve yazılım geliştiricileri genellikle Microsoft Excel dosyalarını **PDF** belgelerine dönüştürmenin bir yolunu bulmaları istenir.
**Aspose.Cells**, Excel dosyalarını PDF'ye dönüştürmeyi destekler ve dönüşümde yüksek görüntü sadakatini korur.

Aspose.Cells for .NET, diğer yazılım bağımsız elektronik tablolardan PDF'e dönüşümü destekler. Bir Excel dosyasını PDF biçimine dönüştüren Save method'unu kullanın. Save methodu, native Excel dosyalarını PDF formatına dönüştüren SaveFormat.Pdf enum üyesini sağlar.

**Üçüncü parti bir araç veya harici bir API** kullanmadan doğrudan elektronik tablodan **PDF'ye dönüştürme**, birkaç **avantaja** sahiptir:

1. Doğrudan dönüşüm, tüm sürecin bellekte yapılabilmesi nedeniyle geçici dosyalara ihtiyaç duymaz.
1. XML dosyası gerekli değildir, bu nedenle büyük dosyalar kolayca dönüştürülebilir.
1. Dönüştürme hızı çok daha hızlıdır.

**Dosyaları PDF'ye dönüştürmek için:**

1. Boş kurucuyu çağırarak **Workbook** sınıfının bir nesnesini oluşturun.
1. Varolan bir şablon dosyasını açabilir/yükleyebilir veya çalışma kitabını sıfırdan oluşturuyorsanız bu adımı atlayabilirsiniz.
1. Aspose.Cells'ın API'lerini kullanarak elektronik tablodaki istediğiniz işlemi yapın (veri girişi, biçimlendirme uygulama, formüller belirleme, resimler veya diğer çizim nesneleri ekleme vb.).
1. Elektronik tablo kodu tamamlandığında, **Workbook** sınıfının **Save** yöntemini çağırarak elektronik tabloyu kaydedin. Dosya formatı PDF olmalı, bu nedenle nihai PDF belgesini oluşturmak için SaveFormat numaralandırmasından Pdf'i (önceden tanımlanmış bir değer) seçin.

{{< highlight csharp >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  workbook.Save(saveFileDialog1.FileName, SaveFormat.Pdf);

{{< /highlight >}}

## **Excel'in MHTML'e dönüştürülmesi**

**MHTML**, normal HTML'i dış kaynaklarla (yani genellikle bağlantılı olan resimler, animasyonlar, sesler vb. gibi içerik) bir dosyada birleştirir. Genellikle .mht dosya uzantılı e-postalar için kullanılır.
Aspose.Cells, MHTML dosyalarını okuma ve yazma desteği sağlamaktadır.

{{< highlight csharp >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  //Specify the HTML Saving Options

  HtmlSaveOptions sv = new HtmlSaveOptions(SaveFormat.MHtml);

  workbook.Save(saveFileDialog1.FileName, sv);

{{< /highlight >}}

## **Excel'i XPS'e Dönüştürme**

Bazı durumlarda, birden çok çalışma sayfasına sahip bir çalışma kitabını metin formatına dönüştürmek veya kaydetmek isteyebilirsiniz. Metin formatları (örneğin TXT, TabDelim, CSV vb.) için, varsayılan olarak hem Microsoft Excel hem de Aspose.Cells yalnızca etkin çalışma sayfasının içeriğini kaydeder.

{{< highlight csharp >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

 workbook.Save(saveFileDialog1.FileName, SaveFormat.CSV);

{{< /highlight >}}

## **Örnek Kod İndir**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Convert%20between%20Excel%20formats%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
