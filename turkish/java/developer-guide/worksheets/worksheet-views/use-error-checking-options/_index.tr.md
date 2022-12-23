---
title: Hata Denetimi Seçeneklerini Kullanın
type: docs
weight: 60
url: /tr/java/use-error-checking-options/
---
{{% alert color="primary" %}} 

Microsoft Excel, kullanıcıların hata denetimi seçeneklerini ve kurallarını tanımlamasına olanak tanır. Kullanıcılar genellikle formül oluştururken hata kontrolleri görürler; hücrede bir sorun olduğunda hücrenin sağ üst köşesindeki küçük bir üçgen vurgulanır. Excel, kullanıcıların yaygın sorunları düzeltmesine yardımcı olan bilgiler sağlar.

{{% /alert %}} 
## **Hata Türleri**
Bir sayıyı sıfıra bölmek gibi formülün bir sonuç döndüremeyeceği anlamına gelen hatalar derhal ilgilenilmesini gerektirir ve hücrede bir hata değeri görüntülenir. Yeşil üçgene tıklamak bir ünlem işareti gösterir, buna tıklamak seçenekler listesini açar.

Hata, seçenekler kullanılarak çözülebilir veya göz ardı edilebilir. Bir hatayı yok saymak, o hatanın sonraki hata kontrollerinde görünmeyeceği anlamına gelir.

Aspose.Cells, hata kontrol seçeneği özellikleri sağlar. ErrorCheckOptions sınıfı, örneğin metin olarak depolanan sayılar, formül hesaplama hataları ve doğrulama hataları gibi farklı türde hata denetimlerini yönetir. İstenen hata denetimini ayarlamak için ErrorCheckType numaralandırmasını kullanın.
## **Numbers Metin Olarak Saklandı**
Bazen sayılar biçimlendirilebilir ve hücrelerde metin olarak saklanabilir. Bu, hesaplamalarda sorunlara neden olabilir veya kafa karıştırıcı sıralama düzenleri oluşturabilir. Metin olarak biçimlendirilen Numbers, hücrede sağa hizalanmak yerine sola hizalanır. Hücreler üzerinde matematiksel işlem gerçekleştirmesi gereken bir formül bir değer döndürmezse, formülün başvurduğu hücrelerdeki hizalamayı kontrol edin; bu hücrelerin bazıları veya tümü metin olarak biçimlendirilmiş sayılar olabilir.

Metin olarak saklanan sayıları hızla gerçek sayılara dönüştürmek için hata denetimi seçeneklerini kullanabilirsiniz. Microsoft Excel 2003'te:

1.  Üzerinde**Araçlar** menü, tıklayın**Seçenekler**.
1. Hata Denetimi sekmesini seçin.
   **Metin olarak saklanan sayı** seçeneği varsayılan olarak işaretlidir.
1. Devre dışı bırakın.
 MS Excel'deki veriler için yeşil üçgenin nasıl görüntülendiğini gösteren aşağıdaki resme bakın.

![yapılacaklar:resim_alternatif_metin](use-error-checking-options_1.png)

 Aşağıdaki örnek kod, Aspose.Cells API'leri kullanılarak şablon XLS dosyasındaki bir çalışma sayfası için metin hatası denetimi seçeneği olarak saklanan sayıların nasıl devre dışı bırakılacağını gösterir.

**Java**

{{< highlight "csharp" >}}

 //Create a workbook and opening a template spreadsheet

Workbook workbook = new Workbook("d:\\files\\Book1.xls");

//Get the first worksheet

Worksheet sheet = workbook.getWorksheets().get(0);

//Instantiate the error checking options

ErrorCheckOptionCollection opts = sheet.getErrorCheckOptions();

int index = opts.add();

ErrorCheckOption opt = opts.get(index);

//Disable the numbers stored as text option

opt.setErrorCheck(ErrorCheckType.TEXT_NUMBER, false);

//Set the range

opt.addRange(CellArea.createCellArea(0, 0, 65535, 255));

//Save the Excel file

workbook.save("d:\\files\\out_test.xls");



{{< /highlight >}}
