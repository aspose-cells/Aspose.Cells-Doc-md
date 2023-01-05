---
title: IFilePathProvider arabirimi aracılığıyla dışa aktarılan çalışma sayfası html dosyası yolu sağlayın
type: docs
weight: 70
url: /tr/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---
## **Olası Kullanım Senaryoları**
 Birden fazla sayfa içeren bir excel dosyanız olduğunu ve her bir sayfayı ayrı HTML dosyasına aktarmak istediğinizi varsayalım. Sayfalarınızdan herhangi birinin diğer sayfalara bağlantıları varsa, bu bağlantılar dışa aktarılan HTML'de kırılacaktır. Bu sorunu çözmek için Aspose.Cells şunları sağlar:[IFilePathSağlayıcı](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider)bozuk bağlantıları düzeltmek için uygulayabileceğiniz arayüz.
## **IFilePathProvider arabirimi aracılığıyla dışa aktarılan çalışma sayfası HTML dosya yolunu sağlayın**
 Lütfen indirin[örnek excel dosyası](5115213.zip)aşağıdaki kodda ve dışa aktarılan HTML dosyalarında kullanılır. Tüm bu dosyalar Temp dizininin içindedir. C: sürücüsüne çıkartmalısınız. Sonra C:\Temp dizini olur. Ardından Sheet1.html dosyasını tarayıcıda açacak ve içindeki iki bağlantıya tıklayacaksınız. Bu bağlantılar, C:\Temp\OtherSheets dizininde bulunan, dışa aktarılan bu iki HTML çalışma sayfasına atıfta bulunur.

{{< highlight "java" >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

Aşağıdaki ekran görüntüsü, C:\Temp\Sheet1.html ve bağlantılarının nasıl göründüğünü gösterir.

![yapılacaklar:resim_alternatif_metin](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

 Aşağıdaki ekran görüntüsü HTML kaynağını göstermektedir. Gördüğünüz gibi bağlantılar artık C:\Temp\OtherSheets dizinine atıfta bulunuyor. Bu, kullanılarak elde edildi[IFilePathSağlayıcı](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider)arayüz.

![yapılacaklar:resim_alternatif_metin](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **Basit kod**
 Lütfen C:\Temp dizininin yalnızca açıklama amaçlı olduğunu unutmayın. İstediğiniz herhangi bir dizini ve yeri kullanabilirsiniz.[örnek excel dosyası](5115211.xlsx)orada ve verilen örnek kodu yürütün. Daha sonra dizininizde OtherSheets alt dizini oluşturacak ve içindeki ikinci ve üçüncü çalışma sayfalarını HTML dışa aktaracaktır. Lütfen sağlanan kodun içindeki dirPath değişkenini değiştirin ve çalıştırmadan önce onu istediğiniz dizine yönlendirin.

{{% alert color="primary" %}} 

Örnek kod sadece Aspose.Cells lisansı ayarladığınızda çalışacaktır. Lisans ayarlamadan kodu çalıştırmayı denerseniz sonsuz döngüye girecektir. Bu nedenle, lisans ayarlanmadığında bir mesaj yazdırmak ve yürütmeyi durdurmak için bir kontrol ekledik. Aspose.Purchase ekibinden lisans satın alabilir veya 30 günlük geçici lisans talebinde bulunabilirsiniz.

{{% /alert %}} 

Lütfen kodun içindeki bu satırları yorumlamaya bakın Sheet1.html ve Sheet2.html'deki linkleri kıracak veya Sheet1.html içindeki linklere tıklandığında Sheet3.html açılmayacak



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-hyperlinks.cs" >}}



 Sağlananlarla çalıştırabileceğiniz tam örnek kod[örnek excel dosyası](5115211.xlsx).



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-ExportedWorkSheetViaIFilePathProvider.cs" >}}
