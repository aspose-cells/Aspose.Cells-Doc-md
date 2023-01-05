---
title: Akıllı İşaretleyiciler ile Verileri Birleştirirken Bildirim Alma
type: docs
weight: 20
url: /tr/net/getting-notifications-while-merging-data-with-smart-markers/
---
{{% alert color="primary" %}} 

 Aspose.Cells API'ler şunları sağlar:[Çalışma KitabıTasarımcısı](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) sınıf[Akıllı İşaretleyicilerle çalışın](https://docs.aspose.com/cells/net/smart-markers/) biçimlendirme ve formüllerin yerleştirildiği yer[tasarımcı elektronik tabloları](/cells/tr/net/what-is-a-designer-spreadsheet/) ve sonra ile işlenir[Çalışma KitabıTasarımcısı](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) belirtilen Akıllı İşaretleyicilere göre verileri doldurmak için sınıf. Bazen, hücre referansı veya işlenmekte olan belirli Akıllı İşaretleyici ile ilgili bildirimlerin alınması gerekebilir. Bu kullanılarak elde edilebilir[WorkbookDesigner.CallBack](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/properties/callback) mülkiyet ve[ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback) Aspose.Cells for .NET 8.6.2 sürümüyle kullanıma sunulan arabirim.

{{% /alert %}} 

 Aşağıdaki kod parçası, kullanımını gösterir.[ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback) için geri aramayı işleyen yeni bir sınıf tanımlamak için arayüz[WorkbookDesigner.Process](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process)yöntem.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-ISmartMarkerCallBack.cs" >}}



 Sürecin geri kalanı, Akıllı İşaretleyicileri içeren tasarımcı elektronik tablosunun yüklenmesini içerir.[Çalışma KitabıTasarımcısı](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)ve veri kaynağını ayarlayarak işleyin. Örneği basit tutmak için, aşağıdaki anlık görüntüde gösterildiği gibi yalnızca iki Akıllı İşaretleyici içeren önceden tanımlanmış bir tasarımcı elektronik tablosu kullandık; burada veri kaynağı, verileri belirtilen Akıllı İşaretleyicilere göre birleştirmek için dinamik olarak oluşturuluyor.

|![yapılacaklar:resim_alternatif_metin](getting-notifications-while-merging-data-with-smart-markers_1.png)|
|:- |
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-1.cs" >}}
