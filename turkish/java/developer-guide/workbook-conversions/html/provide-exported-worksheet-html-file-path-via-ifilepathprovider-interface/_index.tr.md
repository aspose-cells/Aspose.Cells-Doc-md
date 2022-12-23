---
title: IFilePathProvider arabirimi aracılığıyla dışa aktarılan çalışma sayfası HTML dosya yolunu sağlayın
type: docs
weight: 870
url: /tr/java/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---
## **Olası Kullanım Senaryoları**
 Birden fazla sayfa içeren bir excel dosyanız olduğunu ve her bir sayfayı ayrı HTML dosyasına aktarmak istediğinizi varsayalım. Sayfalarınızdan herhangi birinin diğer sayfalara bağlantıları varsa, bu bağlantılar dışa aktarılan HTML'de kırılacaktır. Bu sorunu çözmek için Aspose.Cells şunları sağlar:[IFilePathSağlayıcı](https://reference.aspose.com/cells/java/com.aspose.cells/IFilePathProvider)bozuk bağlantıları düzeltmek için uygulayabileceğiniz arayüz.
## **IFilePathProvider arabirimi aracılığıyla dışa aktarılan çalışma sayfası HTML dosya yolunu sağlayın**
 Lütfen indirin[örnek excel dosyası](5473417.zip) aşağıdaki kodda ve dışa aktarılan HTML dosyalarında kullanılır. Tüm bu dosyalar içinde*Sıcaklık* dizin. üzerine çıkarmalısın*C:* sürmek. Sonra olacak*C:\Sıcaklık* dizin. sonra açacaksın*Sheet1.html* tarayıcıda dosya ve içindeki iki bağlantıya tıklayın. Bu bağlantılar, dışa aktarılan bu iki HTML çalışma sayfasına atıfta bulunur.*C:\Sıcaklık\Diğer Sayfalar*dizin.

{{< highlight "java" >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

Aşağıdaki ekran görüntüsü,*C:\Temp\Sheet1.html*ve bağlantıları şuna benzer:

![yapılacaklar:resim_alternatif_metin](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

 Aşağıdaki ekran görüntüsü HTML kaynağını göstermektedir. Gördüğünüz gibi, bağlantıların şimdi atıfta bulunduğu*C:\Sıcaklık\Diğer Sayfalar* dizin. Bu, kullanılarak elde edildi[IFilePathSağlayıcı](https://reference.aspose.com/cells/java/com.aspose.cells/IFilePathProvider)arayüz.

![yapılacaklar:resim_alternatif_metin](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **Basit kod**
 lütfen aklınızda bulundurun*C:\Sıcaklık* dizin sadece açıklama amaçlıdır. İstediğiniz herhangi bir dizini ve yeri kullanabilirsiniz.[örnek excel dosyası](5473414.xlsx) orada ve verilen örnek kodu yürütün. Daha sonra oluşturacak*DiğerSayfalar* dizininizdeki alt dizini açın ve içindeki ikinci ve üçüncü çalışma sayfalarını HTML dışa aktarın. lütfen değiştir*dirPath*sağlanan kodun içindeki değişken ve çalıştırmadan önce onu seçtiğiniz dizine yönlendirin.

{{% alert color="primary" %}} 

Örnek kod sadece Aspose.Cells lisansı ayarladığınızda çalışacaktır. Lisans ayarlamadan kodu çalıştırmayı denerseniz sonsuz döngüye girecektir. Bu nedenle, lisans ayarlanmadığında bir mesaj yazdırmak ve yürütmeyi durdurmak için bir kontrol ekledik. Aspose.Purchase ekibinden lisans satın alabilir veya 30 günlük geçici lisans talebinde bulunabilirsiniz.

{{% /alert %}} 

 Lütfen kodun içindeki bu satırları yorumlamaya bakın, içindeki bağlantıları kıracaktır.*Sheet1.html* ve*Sheet2.html* veya*Sheet3.html*içindeki linklere tıklandığında açılmayacak*Sheet1.html*



{{< highlight "java" >}}

 //If you will comment this line, then hyperlinks will be broken

options.setFilePathProvider(new FilePathProvider());

{{< /highlight >}}



 Sağlananlarla çalıştırabileceğiniz eksiksiz örnek kod[örnek excel dosyası](5473414.xlsx).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-handling-OpeningFilesThroughPath-1.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilePathProvider-FilePathProvider.java" >}}
