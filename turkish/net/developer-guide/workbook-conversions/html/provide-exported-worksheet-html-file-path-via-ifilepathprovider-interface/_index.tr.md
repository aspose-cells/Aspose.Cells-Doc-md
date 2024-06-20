---
title: IFilePathProvider arabirimini kullanarak dışa aktarılan çalışma sayfasının HTML dosya yolunu sağlayın
type: docs
weight: 70
url: /tr/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---

## **Olası Kullanım Senaryoları**
Örneğin, her bir sayfanın ayrı bir HTML dosyasına dışa aktarılmak istediği bir Excel dosyanız var. Herhangi bir sayfanızın diğer sayfalara bağlantıları varsa, o bağlantılar dışa aktarılan HTML'de bozulur. Bu sorunu çözmek için, Aspose.Cells [IFilePathProvider](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider) arayüzünü sağlar, bu arayüzü uygulayarak bozulmuş bağlantıları düzeltebilirsiniz.
## **IFilePathProvider arayüzü aracılığıyla dışa aktarılan çalışma sayfası HTML dosya yolunu sağlayın**
Aşağıdaki kodda kullanılan [örnek excel dosyasını](5115213.zip) ve dışa aktarılan HTML dosyalarını indirin. Tüm bu dosyalar Temp dizini içindedir. Onu C: sürücüsüne çıkarmanız gerekmektedir. Daha sonra C:\Temp dizini haline gelecektir. Ardından tarayıcıda Sheet1.html dosyasını açacak ve içindeki iki bağlantıya tıklayacaksınız. Bu bağlantılar, C:\Temp\OtherSheets dizini içerisinde bulunan iki dışa aktarılmış HTML çalışma sayfasına işaret eder.

{{< highlight java >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

Aşağıdaki ekran görüntüsü, C:\Temp\Sheet1.html ve bağlantılarının nasıl göründüğünü göstermektedir

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

Aşağıdaki ekran görüntüsü, HTML kaynağını göstermektedir. Bağlantıların şimdi C:\Temp\OtherSheets dizinine işaret ettiğini görebilirsiniz. Bu, [IFilePathProvider](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider) arayüzünü kullanarak başarılmıştır.

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **Örnek Kod**
Lütfen unutmayın, C:\Temp dizini sadece gösterim amaçlıdır. Kendi seçtiğiniz herhangi bir dizini kullanabilir ve [örnek excel dosyasını](5115211.xlsx) içeriye yerleştirebilir ve sağlanan örnek kodu çalıştırabilirsiniz. Ardından, kendi dizininiz içerisine OtherSheets alt dizinini oluşturacak ve ikinci ve üçüncü sayfa HTML'lerini içerisine dışa aktaracaktır. Lütfen kod içerisinde dirPath değişkenini değiştirerek ve çalıştırmadan önce kendi seçtiğiniz dizine yönlendirdiğinizden emin olun.

{{% alert color="primary" %}} 

Örnek kod sadece Aspose.Cells lisansını ayarlarsanız çalışacaktır. Lisansı ayarlamadan kodu çalıştırmaya çalışırsanız, sonsuz bir döngüye girecektir. Bu nedenle, lisans ayarlanmadığında bir mesaj yazdırmak ve işlemi durdurmak için bir kontrol ekledik. Lisans satın alabilir veya Aspose.Purchase ekibinden 30 günlük geçici bir lisans talep edebilirsiniz.

{{% /alert %}} 

Lütfen bu satırların kod içerisinde yorum satırı olarak işaretlenmesi, Sheet1.html içindeki bağlantıları bozacaktır ve Sheet2.html veya Sheet3.html, içindeki bağlantılara tıklandığında açılmayacaktır.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-hyperlinks.cs" >}}



Aşağıdaki, [örnek excel dosyası](5115211.xlsx) ile birlikte çalıştırabileceğiniz tam örnek kod bulunmaktadır.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-ExportedWorkSheetViaIFilePathProvider.cs" >}}
