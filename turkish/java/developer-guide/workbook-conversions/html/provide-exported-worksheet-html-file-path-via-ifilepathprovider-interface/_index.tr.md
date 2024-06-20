---
title: IFilePathProvider arayüzü aracılığıyla dışa aktarılan çalışma sayfası HTML dosyası yolunu sağlayın
type: docs
weight: 870
url: /tr/java/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---

## **Olası Kullanım Senaryoları**
Varsayalım ki, birden fazla sayfaya sahip bir excel dosyanız var ve her sayfayı ayrı HTML dosyasına dışa aktarmak istiyorsunuz. Sayfalarınızın herhangi birinde diğer sayfalara bağlantılar varsa, bu bağlantılar dışa aktarılan HTML'de bozulacaktır. Bu sorunla başa çıkmak için Aspose.Cells, bozuk bağlantıları düzeltmek için uygulayabileceğiniz [IFilePathProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IFilePathProvider) arayüzünü sağlar.
## **IFilePathProvider arayüzü aracılığıyla dışa aktarılan çalışma sayfası HTML dosya yolunu sağlayın**
Lütfen aşağıdaki kodda kullanılan [örnek excel dosyasını](5473417.zip) ve dışa aktarılan HTML dosyalarını indirin. Tüm bu dosyalar *Temp* klasörünün içindedir. Bunun C: sürücüsüne çıkarılması gerekmektedir. Böylece C:\Temp klasörü olacaktır. Ardından tarayıcıda *Sheet1.html* dosyasını açacak ve içindeki iki bağlantıya tıklayacaksınız. Bu bağlantılar, *C:\Temp\OtherSheets* klasörünün içindeki iki dışa aktarılmış HTML çalışma sayfasına atıfta bulunmaktadır.

{{< highlight java >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

Aşağıdaki ekran görüntüsü, *C:\Temp\Sheet1.html* ve bağlantılarının nasıl göründüğünü göstermektedir

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

Aşağıdaki ekran görüntüsü, HTML kaynağını göstermektedir. Bağlantıların şimdi *C:\Temp\OtherSheets* klasörüne atıfta bulunduğunu görebilirsiniz. Bu, [IFilePathProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IFilePathProvider) arayüzü kullanılarak başarılmıştır.

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **Örnek Kod**
Lütfen *C:\Temp* klasörünün sadece bir gösterim amacıyla olduğunu unutmayın. Kendi seçtiğiniz herhangi bir klasörü kullanabilir ve [örnek excel dosyasını](5473414.xlsx) oraya yerleştirebilir ve sağlanan örnek kodu yürütebilirsiniz. Bu, o zamanın içinde kendi klasörünüzün içine *OtherSheets* alt klasörünü oluşturacak ve içindeki ikinci ve üçüncü çalışma sayfası HTML'sini dışa aktaracaktır. Lütfen yürütmeden önce sağlanan kod içinde *dirPath* değişkenini değiştirerek ve kendi tercihiniz olan dizinle ilişkilendirdiğinizden emin olun.

{{% alert color="primary" %}} 

Örnek kod sadece Aspose.Cells lisansını ayarlarsanız çalışacaktır. Lisansı ayarlamadan kodu çalıştırmaya çalışırsanız, sonsuz bir döngüye girecektir. Bu nedenle, lisans ayarlanmadığında bir mesaj yazdırmak ve işlemi durdurmak için bir kontrol ekledik. Lisans satın alabilir veya Aspose.Purchase ekibinden 30 günlük geçici bir lisans talep edebilirsiniz.

{{% /alert %}} 

Lütfen bu satırları kodun içinde yorum satırı olarak eklerken, *Sheet1.html* ve *Sheet2.html* veya *Sheet3.html* içindeki bağlantıları bozacak veya *Sheet1.html* içindeki bağlantıları tıklatamayacaksınız



{{< highlight java >}}

 //If you will comment this line, then hyperlinks will be broken

options.setFilePathProvider(new FilePathProvider());

{{< /highlight >}}



Aşağıda, sağlanan [örnek excel dosyası](5473414.xlsx) ile birlikte yürütebileceğiniz tam örnek kod bulunmaktadır.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-handling-OpeningFilesThroughPath-1.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilePathProvider-FilePathProvider.java" >}}
