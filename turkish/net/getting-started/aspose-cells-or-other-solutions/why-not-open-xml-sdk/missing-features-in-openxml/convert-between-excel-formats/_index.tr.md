---
title: Excel biçimleri arasında dönüştürme
type: docs
weight: 20
url: /tr/net/convert-between-excel-formats/
---
## **Excel'i PDF'ye Dönüştürme**

**PDF** dosyalar, kuruluşlar, devlet sektörleri ve bireyler arasında belge alışverişi için yaygın olarak kullanılır. Standart bir belge biçimidir ve yazılım geliştiricilerden genellikle Microsoft Excel dosyalarını Excel'e dönüştürmenin bir yolunu bulmaları istenir.**PDF** belgeler.
**Aspose.Cells** Excel dosyalarının PDF'ye dönüştürülmesini destekler ve dönüştürmede yüksek görsel doğruluğu korur.

Aspose.Cells for .NET, diğer yazılımlardan bağımsız olarak elektronik tablolardan PDF'ye dönüştürmeyi destekler. Workbook sınıfının Save yöntemini kullanarak bir Excel dosyasını PDF'ye kaydedin. Save yöntemi, yerel Excel dosyalarını PDF biçimine dönüştüren SaveFormat.Pdf enum üyesini sağlar.

**dönüştürme** üçüncü taraf bir araç veya harici API kullanmak yerine doğrudan e-tablodan PDF'ye**avantajlar**:

1. Tüm işlem bellekte yapılabildiğinden, doğrudan dönüştürme geçici dosyalar gerektirmez.
1. Büyük dosyaların kolayca dönüştürülebilmesi için XML dosyası gerekmez.
1. Dönüşüm hızı çok daha hızlı.

**Dosyaları PDF'ye dönüştürmek için:**

1.  nesnesinin örneğini oluşturun**Çalışma kitabı** boş kurucusunu çağırarak sınıf.
1.  Yapabilirsin**aç/yükle** varolan bir şablon dosyası oluşturun veya çalışma kitabını sıfırdan oluşturuyorsanız bu adımı atlayın.
1. Aspose.Cells' API'lerini kullanarak e-tabloda istediğiniz işi yapın (verileri girin, biçimlendirme uygulayın, formüller ayarlayın, resimler veya diğer çizim nesneleri ekleyin, vb.).
1.  Elektronik tablo kodu tamamlandığında,**Çalışma kitabı sınıfının Kaydetme yöntemi** e-tabloyu kaydetmek için. Dosya biçimi PDF olmalıdır, bu nedenle son PDF belgesini oluşturmak için SaveFormat numaralandırmasından Pdf'yi (önceden tanımlanmış bir değer) seçin.

{{< highlight "csharp" >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  workbook.Save(saveFileDialog1.FileName, SaveFormat.Pdf);

{{< /highlight >}}

## **Excel'i MHTML'ye Dönüştürme**

**MHTML** normal HTML'yi harici kaynaklarla (yani resimler, animasyonlar, ses vb. genellikle bağlantılı olan içerik) tek bir dosyada birleştirir. .mht dosya uzantılı e-postalar için kullanılırlar.
Aspose.Cells, MHTML dosyalarını okumayı ve yazmayı destekler.

{{< highlight "csharp" >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  //Specify the HTML Saving Options

  HtmlSaveOptions sv = new HtmlSaveOptions(SaveFormat.MHtml);

  workbook.Save(saveFileDialog1.FileName, sv);

{{< /highlight >}}

## **Excel'i XPS'ye Dönüştürme**

Bazen, birden çok çalışma sayfası içeren bir çalışma kitabını metin biçimine dönüştürmek veya kaydetmek istersiniz. Metin biçimleri için (örneğin TXT, TabDelim, CSV vb.), varsayılan olarak hem Microsoft Excel hem de Aspose.Cells yalnızca etkin çalışma sayfasının içeriğini kaydeder.

{{< highlight "csharp" >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

 workbook.Save(saveFileDialog1.FileName, SaveFormat.CSV);

{{< /highlight >}}

## **Örnek Kodu İndir**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Convert%20between%20Excel%20formats%20%28Aspose.Cells%29.zip)
