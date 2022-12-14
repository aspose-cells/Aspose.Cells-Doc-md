---
title: Çalışma Sayfaları GridWeb ile Çalışma
type: docs
weight: 30
url: /tr/java/working-with-worksheets-gridweb/
---
## **Çalışma Sayfalarına Erişim**

Bu konu, GridWeb denetiminin çalışma sayfalarına erişmeyi tartışır. Bu worksheet'lere GridWeb'e ait oldukları ve web uygulamalarında kullanıldığı için web worksheets de diyebiliriz.

GridWeb denetiminde bulunan tüm çalışma sayfaları, GridWeb denetiminin GridWorksheetCollection'ında depolanır. Sayfa dizinine göre belirli bir çalışma sayfasına erişmek kolaydır.

Geliştiriciler, aşağıda örnek kod parçacığında gösterildiği gibi sayfa dizinini belirterek belirli bir çalışma sayfasına erişebilirler.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingWorksheet-AccessingWorksheet.jsp" >}}

## **Bir Çalışma Sayfasını Kaldırma**

Bu konu, GridWeb API'i kullanarak Microsoft Excel dosyalarından çalışma sayfalarını kaldırma hakkında kısa bilgiler sağlar. Sayfa dizinini belirterek bir çalışma sayfasını kaldırın.

Geliştiriciler, aşağıda örnek kod parçacığında gösterildiği gibi GridWorksheetCollection koleksiyonunun removeAt yöntemini kullanarak sayfa dizinini belirterek belirli bir çalışma sayfasını kaldırabilir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingWorksheet-RemovingWorksheet.jsp" >}}

## **Çalışma Sayfaları Ekleme**

Çalışma sayfaları, GridWeb'in ayrılmaz bir parçasıdır. Tüm veriler çalışma sayfaları biçiminde yönetilir ve saklanır. GridWeb, geliştiricilerin Aspose.Cells.GridWeb denetimine bir veya daha fazla çalışma sayfası eklemesine olanak tanır. Bu konuda, GridWeb'e çalışma sayfası eklemeye yönelik basit yaklaşımlar gösterilmektedir.

### **Sayfa Adını Belirtmeden**

Aspose.Cells.GridWeb'e çalışma sayfası eklemenin en basit yolu, GridWeb denetiminde GridWorksheetCollection sınıfının add yöntemini çağırmaktır. Bu, varsayılan adları (Sayfa1, Sayfa2, Sayfa3 vb.) kullanan çalışma sayfaları oluşturur ve bunları GridWeb denetimine ekler.

**Çıktı: GridWeb'e varsayılan ada sahip bir çalışma sayfası eklendi** 

![yapılacaklar:resim_alternatif_Metin](working-with-worksheets-gridweb_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithoutSpecificName-AddingWorksheetWithoutSpecificName.jsp" >}}

### **Belirtilen Sayfa Adıyla**

Varsayılan adlandırma şemasını kullanmak yerine GridWeb denetimine belirli bir ada sahip bir çalışma sayfası eklemek için, belirtilen SheetName dizesini alan add yönteminin aşırı yüklenmiş bir sürümünü çağırın. Örneğin, aşağıdaki örnek Fatura adlı bir çalışma sayfası ekler.

**Çıktı: Belirtilen ada sahip bir çalışma sayfası GridWeb'e eklendi** 

![yapılacaklar:resim_alternatif_Metin](working-with-worksheets-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithSpecificName-AddingWorksheetWithSpecificName.jsp" >}}

{{% alert color="primary" %}}

 add() yöntemi, bu çalışma sayfasının örneğine erişmek için kullanılabilecek yeni çalışma sayfasının dizinini döndürür. Çalışma sayfalarına nasıl erişileceği hakkında daha fazla bilgi için, okuyun[Çalışma Sayfalarına Erişim](/cells/tr/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

## **Çalışma Sayfasını Yeniden Adlandırma**

Bir çalışma sayfasını yeniden adlandırmak, GridWeb'de birçok çalışma sayfasıyla çalışırken ve daha anlamlı hale getirmek için adlarını değiştirmeye karar verirken çok yararlı olabilir. Örneğin, fatura içeren bir çalışma sayfası, Sayfa1 yerine Fatura olarak yeniden adlandırılabilir. Bu konuda, bu basit ama kullanışlı özellik açıklanmaktadır.

### **Çalışma Sayfasını Yeniden Adlandırma**

Tüm çalışma sayfaları, geliştiricilerin çalışma sayfalarının adlarına erişmesine veya bu adları değiştirmesine izin veren bir Ad özelliği içerir. Bir çalışma sayfasını yeniden adlandırmak için:

1. GridWorksheetCollection'dan bir çalışma sayfasına erişin.
1. Seçilen çalışma sayfasını yeniden adlandırın.

{{% alert color="primary" %}}

 Aspose.Cells.GridWeb'deki çalışma sayfalarına nasıl erişileceği hakkında daha fazla bilgi için lütfen şu adrese bakın:[Çalışma Sayfalarına Erişim](/cells/tr/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

Kodu çalıştırmadan önce, çalışma sayfasının Sayfa1 gibi varsayılan bir adı vardır.

**Giriş dosyası: varsayılan adı Sheet1 olan bir çalışma sayfası** 

![yapılacaklar:resim_alternatif_Metin](working-with-worksheets-gridweb_3.png)

Kodu çalıştırdıktan sonra, çalışma sayfası Fatura olarak yeniden adlandırılır.

**Çıktı: çalışma sayfasının adı Fatura olarak değiştirildi** 

![yapılacaklar:resim_alternatif_Metin](working-with-worksheets-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RenamingWorksheet-RenamingWorksheet.jsp" >}}

## **Çalışma Sayfasını Kopyalama**

[Çalışma Sayfaları Ekleme](/cells/tr/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-addingworksheets)GridWeb'e yeni çalışma sayfalarının nasıl ekleneceğini açıklar. Aspose.Cells.GridWeb denetimine başka bir çalışma sayfasının bir kopyasını (veya eşlemesini) eklemek de mümkündür. Bu özellik, bir çalışma sayfasındaki aynı veya benzer verilerin başka bir çalışma sayfasında da gerekli olduğu durumlarda faydalı olabilir. Bu durumda, mevcut bir çalışma sayfasını sıfırdan oluşturmak yerine kopyalayıp Aspose.Cells.GridWeb'e yeni bir çalışma sayfası olarak eklemek daha kolaydır.

### **Sayfa dizinini kullanma**

Aşağıdaki örnek kod, GridWorksheetCollection'ın addCopy yönteminde çalışma sayfasının dizinini belirterek GridWeb denetimine bir çalışma sayfasının bir kopyasının nasıl ekleneceğini gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetIndex-CopyWorksheetUsingSheetIndex.jsp" >}}
### **Sayfa Adını Kullanma**
Aşağıdaki örnek kod, GridWorksheetCollection'ın addCopy yönteminde çalışma sayfasının adını belirterek bir çalışma sayfasının bir kopyasının GridWeb denetimine nasıl ekleneceğini gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetName-CopyWorksheetUsingSheetName.jsp" >}}

{{% alert color="primary" %}}

 addCopy yöntemi, çalışma sayfası örneğine erişmek için kullanılabilecek yeni eklenen çalışma sayfasının dizinini döndürür. Çalışma sayfalarına nasıl erişileceği hakkında daha fazla bilgi için, okuyun[Çalışma Sayfalarına Erişim](/cells/tr/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

## **Adlandırılmış Aralıklarla Çalışma**

Normalde sütun ve satır etiketleri, hücrelere benzersiz bir şekilde atıfta bulunmak için kullanılır. Ancak hücreleri, hücre aralıklarını, formülleri veya sabit değerleri temsil etmek için açıklayıcı adlar oluşturabilirsiniz.

 Kelime**isim** bir hücreyi, hücre aralığını, formülü veya sabit değeri temsil eden bir karakter dizisine atıfta bulunabilir. Örneğin, Satış!C20:C30 gibi anlaşılması zor aralıklara atıfta bulunmak için Ürünler gibi anlaşılması kolay adlar kullanın.

 Etiketler, aynı çalışma sayfasındaki verilere atıfta bulunan formüllerde kullanılabilir; başka bir çalışma sayfasındaki bir aralığı temsil etmek istiyorsanız, bir ad kullanabilirsiniz.**Adlandırılmış aralıklar** Microsoft Excel'in en güçlü özelliklerinden biridir.

Kullanıcılar bir aralığa bir ad atayabilir ve bu adı formüllerde kullanabilir. Aspose.Cells.GridWeb bu özelliği destekler.

### **Formüllerde Adlandırılmış Aralıkları Ekleme/Başvuruda Bulunma**

GridWeb denetimi, adlandırılmış aralıklarla çalışmak için iki sınıf (GridName ve GridNameCollection) sağlar.

Aşağıdaki kod parçacığı, bunları nasıl kullanacağınızı anlamanıza yardımcı olacaktır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingNamedRangesinFormulas-AddingNamedRangesinFormulas.jsp" >}}

## **Çalışma Sayfasında Yorumları Yönetme**

Bu konuda, çalışma sayfalarına yorum ekleme, çalışma sayfalarına erişme ve çalışma sayfalarından yorum kaldırma anlatılmaktadır. Yorumlar, sayfa ile çalışacak kullanıcılar için notlar veya faydalı bilgiler eklemek için kullanışlıdır. Geliştiriciler, çalışma sayfasının herhangi bir hücresine yorum ekleme esnekliğine sahiptir.

### **Yorumlarla Çalışmak**

#### **Yorum Ekleme**

Çalışma sayfasına yorum eklemek için lütfen aşağıdaki adımları izleyin:

1. Aspose.Cells.GridWeb denetimini Web Formuna ekleyin.
1. Yorum eklediğiniz çalışma sayfasına erişin.
1. Bir hücreye yorum ekleyin.
1. Yeni yorum için bir not ayarlayın.

**Çalışma sayfasına bir yorum eklendi** 

![yapılacaklar:resim_alternatif_Metin](working-with-worksheets-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingComments-AddingComments.jsp" >}}

#### **Yorumlara Erişim**

Bir yoruma erişmek için:

1. Yorumu içeren hücreye erişin.
1. Hücrenin referansını alın.
1. Yoruma erişmek için referansı Yorum koleksiyonuna iletin.
1. Yorumun özelliklerini değiştirmek artık mümkün.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingComments-AccessingComments.jsp" >}}

#### **Yorumları Kaldırma**

Bir yorumu kaldırmak için:

1. Yukarıda açıklandığı gibi hücreye erişin.
1. Yorumu kaldırmak için Yorum koleksiyonunun removeAt yöntemini kullanın.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingComments-RemovingComments.jsp" >}}

## **Çalışma Sayfasında Köprüleri Yönetme**

Bu konuda, Aspose.Cells.GridWeb'de ne tür köprülerin desteklendiği ve bunların programlı olarak nasıl yönetileceği anlatılmaktadır. Köprüler, web URL'lerine bağlantılar oluşturmak veya bir sunucuya geri gönderme gerçekleştirmek için kullanılabilir.

### **Köprü Türleri**

Aşağıdaki köprüler Aspose.Cells.GridWeb tarafından desteklenir:

- Metin URL köprüleri, metne uygulanan URL köprüleri.
- Resim URL köprüleri, resimlere uygulanan URL köprüleri.

#### **Metin URL Köprüleri**

 Aşağıdaki örnek, bir çalışma sayfasına iki köprü ekler. biri var_ diğeri ayarlıyken boş hedef_ebeveyn.

![yapılacaklar:resim_alternatif_Metin](working-with-worksheets-gridweb_6.png)

**Çıktı: çalışma sayfasına eklenen metin köprüleri**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-TextURLHyperlinks-TextURLHyperlinks.jsp" >}}

#### **Resim URL Köprüleri**

Aşağıdaki örnek, bir çalışma sayfasına resim URL köprüsü ekler.

![yapılacaklar:resim_alternatif_Metin](working-with-worksheets-gridweb_7.png)

**Çıktı: çalışma sayfasına eklenen görüntü köprüsü**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-ImageURLHyperlinks-ImageURLHyperlinks.jsp" >}}

## **Verileri Sıralama**

Sıralama, veri işleme söz konusu olduğunda çok değerli bir özelliktir. Sıralanmamış veriler, belirli bilgileri ararken kullanıcılar için bir sıkıntıdır. Aspose.Cells.GridWeb, güçlü sıralama özelliklerini destekler. Bu konuda, Aspose.Cells.GridWeb API kullanılarak verilerin sıralanması ele alınmaktadır.

Aspose.Cells.GridWeb, geliştiricilerin verileri yukarıdan aşağıya veya soldan sağa sıralayabilmeleri için verileri yatay ve dikey olarak sıralamasına olanak tanır.

### **Baştan aşağı**

Verileri yukarıdan aşağıya doğru sıralamak için:

1. Aspose.Cells.GridWeb denetimini Web Formunuza ekleyin.
1. Sıralamak istediğiniz çalışma sayfasına erişin.
1. Veri aralığını herhangi bir sırayla (artan veya azalan) sıralayın. Yukarıdan aşağıya yönlendirmeyi seçtiğinizden emin olun.

Aşağıdaki örnek, verileri bir çalışma sayfasının iki sütununda (Öğrenci Kimliği ve Öğrenci Adı) artan düzende sıralar. Yukarıdan aşağıya yönde yalnızca iki sütunun on iki satırı sıralanır.

Kodu uygulamadan önce, çalışma sayfası sıralanmamış veriler içerir.

**Giriş: sıralanmamış veriler** 

![yapılacaklar:resim_alternatif_Metin](working-with-worksheets-gridweb_8.png)

Kodu çalıştırdıktan sonra, veriler artan düzende sıralanır.

**Çıktı: veriler yukarıdan aşağıya artan sırada sıralanır** 

![yapılacaklar:resim_alternatif_Metin](working-with-worksheets-gridweb_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromtoptobottomascendingorder-datasortedfromtoptobottomascendingorder.jsp" >}}

### **Soldan sağa**

Verileri soldan sağa sıralamak için:

1. Aspose.Cells.GridWeb denetimini Web Formunuza ekleyin.
1. Sıralamak istediğiniz çalışma sayfasına erişin.
1. Veri aralığını herhangi bir sırayla (artan veya azalan) sıralayın. Soldan sağa seçtiğinizden emin olun.

Aşağıdaki örnek, verileri iki satırda (Öğrenci Kimliği ve Öğrenci Adı) artan düzende sıralar. Dört sütundan oluşan yalnızca iki satır soldan sağa sıralanır.

Kodu uygulamadan önce, çalışma sayfası sıralanmamış veriler içerir.

**Girdi: kod parçacığını yürütmeden önce sıralanmamış veriler** 

![yapılacaklar:resim_alternatif_Metin](working-with-worksheets-gridweb_10.png)

Kodu çalıştırdıktan sonra, veriler artan düzende sıralanır.

**Çıktı: artan düzende soldan sağa sıralanmış veriler** 

![yapılacaklar:resim_alternatif_Metin](working-with-worksheets-gridweb_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromleftrightascendingorder-datasortedfromleftrightascendingorder.jsp" >}}

## **Arama ve Değiştirme**

Büyük bir e-tabloda yinelenen değişiklikler yapmanın en hızlı yollarından biri, bul ve değiştir özelliğini kullanmaktır. Bul, bir metin dizesini veya verileri bulmanıza yardımcı olur ve onu yeni bir değerle değiştirir. Aspose.Cells.GridWeb bu özelliği sağlar. Basit bir iletişim kutusu aracılığıyla çalışma sayfası istemci tarafında belirli bir metin dizesi veya değeri aramanıza ve bunlarla değiştirmenize olanak tanır. Kısmi verileri aramanıza bile izin verir.

### **Bul/Değiştir İletişim Kutusu**

Bul/Değiştir iletişim kutusunu açmanın iki yolu vardır:

1.  Kontrol aktifken, basın**CTRL+F** iletişim kutusunu açmak için veya tuşuna basın.**CTRL+R** diyalog kutusunu açmak için tuşu**Yer değiştirmek** düğme etkinleştirildi.
1.  İmleci çalışma sayfasındaki hücre alanına getirin, ardından sağ tıklayın. Seçme**Bulmak** veya**Yer değiştirmek** menüden.

**Bul'u Seçmek**

![yapılacaklar:resim_alternatif_Metin](working-with-worksheets-gridweb_12.png)

Bir bul ve değiştir iletişim kutusu görüntülenir.

**Bul/Değiştir iletişim kutusu**

![yapılacaklar:resim_alternatif_Metin](working-with-worksheets-gridweb_13.png)

**Bul'u Kullanma**

Aramak:

1. Bul/Değiştir iletişim kutusunu açın.
1. Aranan alanına aramak istediğiniz dizeyi yazın.
1. Aramak için Sonrakini Bul'a tıklayın.

Bulma koşulunuzla eşleşen bir sonraki hücre vurgulanır.

{{% alert color="primary" %}}

Arama kriteriniz bulunamazsa, bunu size söylemek için bir iletişim kutusu görüntülenir.

{{% /alert %}}

### **Arama Seçenekleri**

İletişim kutusunda özelleştirebileceğiniz bazı arama seçenekleri vardır. Aşağıdaki tablo bunları listeler.

|**Numara.**|**Seçenek Adı**|**Tanım**|
|:- |:- |:- |
|1|Maç durumu|Aramada büyük/küçük harf duyarlılığının kullanılıp kullanılmayacağını gösterir.|
|2|Tüm kelimeyi eşleştir|Aramada kelimenin tamamıyla eşleşip eşleşmeyeceğini belirtir.|
|3|yukarı ara|Aramanın aşağıdan yukarıya doğru yapılıp yapılmayacağını belirtir.|
|4|Düzenli ifade|İşaretlendiğinde, denetim, Aranan metin kutusundaki dizeyi arama sürecinde normal bir ifade olarak ele alır.|
|5|Formüllerde/Değerlerde Bul|Formüller seçildiğinde, formül veya biçimlendirilmemiş değer varsa kontrol, hücrelerin formül veya biçimlendirilmemiş değeriyle eşleşir. Değerler seçildiğinde, kontrol yalnızca hücrelerin görüntülenen değeriyle eşleşecektir.|

### **Değiştir'i Kullanma**

Metni veya değerleri değiştirmek için:

1.  düğmesine basarak Bul/Değiştir iletişim kutusunu açın.**CTRL+F** veya bir hücreyi sağ tıklayıp seçin**Bulmak** tıklamadan önce**Yer değiştirmek**.
1.  Değiştirme dizesini şuraya yazın:**İle değiştirin**alan.
1.  Tıklamak**Yer değiştirmek**.

Metni değiştirmek için:

1. İletişim kutusunu açın.
1.  Bulmak istediğiniz metni girin**Ne buldun** alan ve onu değiştirmek istediğiniz metin**İle değiştirin** alan.
1.  Tıklayarak her seferinde bir oluşumu değiştirin**Sonraki Bul** bunu takiben**Yer değiştirmek**.
1.  Çalışma sayfasının ne içerdiğinden çok eminseniz, tıklayın.**Hepsini değiştir**.

{{% alert color="primary" %}}

 Çalışma sayfası düzenleme modunda değilse,**Yer değiştirmek** düğmesi görüntülenmez.

{{% /alert %}}

## İstemci Tarafından Köprü Ekleme/Kaldırma

Aspose.Cells GridWeb artık istemci tarafında köprü eklemeyi ve kaldırmayı destekliyor. Bunun için API, "addCelllink" ve "delCelllink" işlevlerini sağlar. Aşağıdaki kod parçacıkları, GridWeb'de istemci tarafından köprülerin eklenmesini ve kaldırılmasını göstermektedir.

### Basit kod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-1.jsp" >}}

Aşağıdaki kod parçacığını kullanarak sayfaya da bağlantı verebilirsiniz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-2.jsp" >}}

## Yazı Tipi Ayarlarını İstemci Tarafından Güncelleyin

Aspose.Cells GridWeb artık yazı tipi ayarlarını istemci tarafından değiştirmeyi destekliyor. Bunun için API aşağıdaki işlevleri sağlar

- **updateCellFontStyle**: Parametreler - normal/italik/kalın/italik&&kalın için r/i/b/ib
- **updateCellFontSize**: Parametreler - yazı tipi adı, vb. 'Sistem'
- **updateCellFontName**: Parametreler - yazı tipi boyutu, vb. "12pt"
- **updateCellFontColor**: Parametreler - yok/u/l/ul/ için hiçbiri/altı çizili/üstü çizili/altı çizili&&üstü çizili
- **updateCellFontLine**: Params - #aa22ee gibi html rengi veya yeşil, kırmızı,...
- **updateCellBackGroundColor**: Params - #aa22ee gibi html rengi veya yeşil, kırmızı,...

Aşağıdaki kod parçacığı, GridWeb'de istemci tarafından değişen yazı tipi ayarlarını gösterir.

### Basit kod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-update_font_from_client_side-1.jsp" >}}

## İstemci Tarafından Yorum Ekle/Kaldır

Aspose.Cells GridWeb artık istemci tarafında Yorum eklemeyi ve kaldırmayı destekliyor. Bunun için API, "addcomments" ve "decomments" fonksiyonlarını sağlar. Aşağıdaki kod parçacığı, GridWeb'de istemci tarafında yorum eklemeyi ve kaldırmayı gösterir.

### Basit kod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add_remove_comments_from_client_side.jsp" >}}

## Çalışma Sayfası Ekleme/Kaldırma düğmelerini göster

 Aspose.Cells GridWeb artık araç çubuğundaki düğmeleri kullanarak sayfa eklemeyi ve kaldırmayı destekliyor. Ön uçta düğmelerin görünür olması için ayarlamanız gerekir.**GridWeb1.ShowAddButton** ile**doğru**. Aşağıdaki kod parçacığı, GridWeb araç çubuğuna Ekle/Kaldır düğmelerinin eklenmesini gösterir.

### Basit kod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "GridWeb-show_add_remove_worksheet_buttons.java" >}}
