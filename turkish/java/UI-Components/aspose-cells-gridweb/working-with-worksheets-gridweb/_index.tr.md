---
title: Çalışma Sayfalarıyla Çalışma GridWeb
type: docs
weight: 30
url: /tr/java/working-with-worksheets-gridweb/
---
##  **Çalışma Sayfalarına Erişim**

Bu konuda GridWeb denetiminin çalışma sayfalarına erişim anlatılmaktadır. Bu çalışma sayfalarına GridWeb'e ait olması ve web uygulamalarında kullanılması nedeniyle web çalışma sayfaları da diyebiliriz.

GridWeb denetiminde bulunan tüm çalışma sayfaları, GridWeb denetiminin GridWorksheetCollection'ında depolanır. Belirli bir çalışma sayfasına sayfa dizininden erişmek kolaydır.

Geliştiriciler, aşağıda örnek kod parçacığında gösterildiği gibi sayfa dizinini belirterek belirli bir çalışma sayfasına erişebilirler.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingWorksheet-AccessingWorksheet.jsp" >}}

##  **Çalışma Sayfasını Kaldırma**

Bu konu, GridWeb API'i kullanarak Microsoft Excel dosyalarından çalışma sayfalarını kaldırma hakkında kısa bilgi sağlar. Bir çalışma sayfasını, sayfa dizinini belirterek kaldırın.

Geliştiriciler, aşağıda örnek kod parçacığında gösterildiği gibi GridWorksheetCollection koleksiyonunun RemoveAt yöntemini kullanarak sayfa dizinini belirterek belirli bir çalışma sayfasını kaldırabilir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingWorksheet-RemovingWorksheet.jsp" >}}

##  **Çalışma Sayfaları Ekleme**

Çalışma sayfaları GridWeb'in ayrılmaz bir parçasıdır. Tüm veriler çalışma sayfaları biçiminde yönetilir ve saklanır. GridWeb, geliştiricilerin Aspose.Cells.GridWeb denetimine bir veya daha fazla çalışma sayfası eklemesine olanak tanır. Bu konu, GridWeb'e çalışma sayfaları eklemeye yönelik basit yaklaşımları gösterir.

###  **Sayfa Adı Belirtilmeden**

Aspose.Cells.GridWeb'e çalışma sayfası eklemenin en basit yolu, GridWeb denetiminde GridWorksheetCollection sınıfının ekleme yöntemini çağırmaktır. Bu, varsayılan adları (Sayfa1, Sayfa2, Sayfa3 vb.) kullanan çalışma sayfaları oluşturur ve bunları GridWeb denetimine ekler.

**Çıktı: GridWeb'e varsayılan ada sahip bir çalışma sayfası eklendi** 

![yapılacak şey:image_alt_text](working-with-worksheets-gridweb_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithoutSpecificName-AddingWorksheetWithoutSpecificName.jsp" >}}

###  **Belirtilen Sayfa Adıyla**

Varsayılan adlandırma şemasını kullanmak yerine GridWeb denetimine belirli bir ada sahip bir çalışma sayfası eklemek için, belirtilen SheetName dizesini alan add yönteminin aşırı yüklenmiş bir sürümünü çağırın. Örneğin, aşağıdaki örnekte Fatura adında bir çalışma sayfası eklenmiştir.

**Çıktı: GridWeb'e belirtilen ada sahip bir çalışma sayfası eklendi** 

![yapılacak şey:image_alt_text](working-with-worksheets-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithSpecificName-AddingWorksheetWithSpecificName.jsp" >}}

{{% alert color="primary" %}}

 add() yöntemi, bu çalışma sayfasının örneğine erişmek için kullanılabilecek yeni çalışma sayfasının dizinini döndürür. Çalışma sayfalarına nasıl erişileceğine ilişkin daha fazla ayrıntı için bkz.[Çalışma Sayfalarına Erişim](/cells/tr/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

##  **Çalışma Sayfasını Yeniden Adlandırma**

GridWeb'de birçok çalışma sayfasıyla çalışırken ve onları daha anlamlı hale getirmek için adlarını değiştirmeye karar verdiğinizde, bir çalışma sayfasını yeniden adlandırmak çok yararlı olabilir. Örneğin, fatura içeren bir çalışma sayfası Sayfa1 yerine Fatura olarak yeniden adlandırılabilir. Bu konu, bu basit ama kullanışlı özelliği açıklamaktadır.

###  **Çalışma Sayfasını Yeniden Adlandırma**

Tüm çalışma sayfaları, geliştiricilerin çalışma sayfalarının adlarına erişmesine veya bunları değiştirmesine olanak tanıyan bir Ad özelliği içerir. Bir çalışma sayfasını yeniden adlandırmak için:

1. GridWorksheetCollection'dan bir çalışma sayfasına erişin.
1. Seçilen çalışma sayfasını yeniden adlandırın.

{{% alert color="primary" %}}

 Aspose.Cells.GridWeb'deki çalışma sayfalarına nasıl erişileceğine ilişkin daha fazla ayrıntı için lütfen şu adrese bakın:[Çalışma Sayfalarına Erişim](/cells/tr/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

Kodu çalıştırmadan önce çalışma sayfasının Sayfa1 gibi varsayılan bir adı vardır.

**Giriş dosyası: Varsayılan adı Sayfa1 olan bir çalışma sayfası** 

![yapılacak şey:image_alt_text](working-with-worksheets-gridweb_3.png)

Kodu çalıştırdıktan sonra çalışma sayfası Fatura olarak yeniden adlandırıldı.

**Çıktı: çalışma sayfası Fatura olarak yeniden adlandırıldı** 

![yapılacak şey:image_alt_text](working-with-worksheets-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RenamingWorksheet-RenamingWorksheet.jsp" >}}

##  **Çalışma Sayfasını Kopyalamak**

[Çalışma Sayfaları Ekleme](/cells/tr/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-addingworksheets)GridWeb'e yeni çalışma sayfalarının nasıl ekleneceğini açıklar. Aspose.Cells.GridWeb denetimine başka bir çalışma sayfasının kopyasını (veya kopyasını) eklemek de mümkündür. Bu özellik, bir çalışma sayfasındaki aynı veya benzer verilere başka bir çalışma sayfasında da ihtiyaç duyulduğunda yararlı olabilir. Durum böyle olduğunda, mevcut bir çalışma sayfasını sıfırdan oluşturmak yerine kopyalayıp Aspose.Cells.GridWeb'e yeni bir çalışma sayfası olarak eklemek daha kolaydır.

###  **Sayfa dizinini kullanma**

Aşağıdaki örnek kod, GridWorksheetCollection'ın addCopy yönteminde çalışma sayfasının dizinini belirterek çalışma sayfasının bir kopyasının GridWeb denetimine nasıl ekleneceğini gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetIndex-CopyWorksheetUsingSheetIndex.jsp" >}}
###  **Sayfa Adını Kullanma**
Aşağıdaki örnek kod, çalışma sayfasının adını GridWorksheetCollection'ın addCopy yönteminde belirterek GridWeb denetimine bir çalışma sayfasının kopyasının nasıl ekleneceğini gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetName-CopyWorksheetUsingSheetName.jsp" >}}

{{% alert color="primary" %}}

 addCopy yöntemi, çalışma sayfası örneğine erişmek için kullanılabilecek yeni eklenen çalışma sayfasının dizinini döndürür. Çalışma sayfalarına nasıl erişileceğine ilişkin daha fazla ayrıntı için bkz.[Çalışma Sayfalarına Erişim](/cells/tr/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

##  **Adlandırılmış Aralıklarla Çalışma**

Normalde sütun ve satır etiketleri hücrelere benzersiz şekilde atıfta bulunmak için kullanılır. Ancak hücreleri, hücre aralıklarını, formülleri veya sabit değerleri temsil edecek açıklayıcı adlar oluşturabilirsiniz.

 Kelime**isim** bir hücreyi, hücre aralığını, formülü veya sabit değeri temsil eden bir karakter dizisine atıfta bulunabilir. Örneğin, Satış!C20:C30 gibi anlaşılması zor aralıklara atıfta bulunmak için Ürünler gibi anlaşılması kolay adlar kullanın.

 Etiketler aynı çalışma sayfasındaki verilere başvuran formüllerde kullanılabilir; Başka bir çalışma sayfasında bir aralığı temsil etmek istiyorsanız bir ad kullanabilirsiniz.**Adlandırılmış aralıklar** Microsoft Excel'in en güçlü özelliklerinden biridir.

Kullanıcılar bir aralığa ad atayabilir ve bu adı formüllerde kullanabilir. Aspose.Cells.GridWeb bu özelliği desteklemektedir.

###  **Formüllerde Adlandırılmış Aralıkları Ekleme/Referans Alma**

GridWeb kontrolü, adlandırılmış aralıklarla çalışmak için iki sınıf (GridName ve GridNameCollection) sağlar.

Aşağıdaki kod parçacığı, bunları nasıl kullanacağınızı anlamanıza yardımcı olacaktır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingNamedRangesinFormulas-AddingNamedRangesinFormulas.jsp" >}}

##  **Çalışma Sayfasındaki Yorumları Yönetme**

Bu konuda çalışma sayfalarındaki yorumların eklenmesi, bunlara erişilmesi ve yorumların kaldırılması anlatılmaktadır. Yorumlar, sayfayla çalışacak kullanıcılar için not veya faydalı bilgi eklemek açısından faydalıdır. Geliştiriciler çalışma sayfasının herhangi bir hücresine yorum ekleme esnekliğine sahiptir.

###  **Yorumlarla Çalışmak**

####  **Yorum Ekleme**

Çalışma sayfasına yorum eklemek için lütfen aşağıdaki adımları izleyin:

1. Aspose.Cells.GridWeb denetimini Web Formuna ekleyin.
1. Yorum eklediğiniz çalışma sayfasına erişin.
1. Bir hücreye yorum ekleyin.
1. Yeni yorum için bir not ayarlayın.

**Çalışma sayfasına bir yorum eklendi** 

![yapılacak şey:image_alt_text](working-with-worksheets-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingComments-AddingComments.jsp" >}}

####  **Yorumlara Erişim**

Bir yoruma erişmek için:

1. Yorumu içeren hücreye erişin.
1. Hücrenin referansını alın.
1. Yoruma erişmek için referansı Yorum koleksiyonuna iletin.
1. Artık yorumun özelliklerini değiştirmek mümkün.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingComments-AccessingComments.jsp" >}}

####  **Yorumları Kaldırma**

Bir yorumu kaldırmak için:

1. Yukarıda açıklandığı gibi hücreye erişin.
1. Yorumu kaldırmak için Yorum koleksiyonunun RemoveAt yöntemini kullanın.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingComments-RemovingComments.jsp" >}}

##  **Çalışma Sayfasındaki Köprüleri Yönetme**

Bu konu, Aspose.Cells.GridWeb'de hangi tür köprülerin desteklendiğini ve bunların programlı olarak nasıl yönetileceğini açıklamaktadır. Köprüler, web URL'lerine bağlantılar oluşturmak veya bir sunucuya geri gönderme gerçekleştirmek için kullanılabilir.

###  **Köprü Türleri**

Aşağıdaki köprüler Aspose.Cells.GridWeb tarafından desteklenir:

- Metin URL köprüleri, metne uygulanan URL köprüleri.
- Resim URL köprüleri, resimlere uygulanan URL köprüleri.

####  **Metin URL'si Köprüleri**

Aşağıdaki örnek, bir çalışma sayfasına iki köprü ekler. Birinin _blank hedefi varken diğerinin _parent olarak ayarlı olması.

![yapılacak şey:image_alt_text](working-with-worksheets-gridweb_6.png)

**Çıktı: çalışma sayfasına eklenen metin köprüleri**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-TextURLHyperlinks-TextURLHyperlinks.jsp" >}}

####  **Resim URL'si Köprüleri**

Aşağıdaki örnek, bir çalışma sayfasına resim URL'si köprüsü ekler.

![yapılacak şey:image_alt_text](working-with-worksheets-gridweb_7.png)

**Çıktı: çalışma sayfasına resim köprüsü eklendi**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-ImageURLHyperlinks-ImageURLHyperlinks.jsp" >}}

##  **Verileri Sıralama**

Sıralama, veri işleme söz konusu olduğunda çok değerli bir özelliktir. Sıralanmamış veriler, belirli bilgileri ararken kullanıcılar için sıkıntı yaratır. Aspose.Cells.GridWeb güçlü sıralama özelliklerini destekler. Bu konuda Aspose.Cells.GridWeb API kullanılarak verilerin sıralanması anlatılmaktadır.

Aspose.Cells.GridWeb, geliştiricilerin verileri yatay ve dikey olarak sıralamasına olanak tanır, böylece geliştiriciler verileri yukarıdan aşağıya veya soldan sağa sıralayabilir.

###  **Baştan aşağı**

Verileri yukarıdan aşağıya doğru sıralamak için:

1. Aspose.Cells.GridWeb denetimini Web Formunuza ekleyin.
1. Sıralamak istediğiniz çalışma sayfasına erişin.
1. Veri aralığını herhangi bir sıraya göre (artan veya azalan) sıralayın. Yukarıdan aşağıya yönlendirmeyi seçtiğinizden emin olun.

Aşağıdaki örnek, bir çalışma sayfasının iki sütunundaki (Öğrenci Kimliği ve Öğrenci Adı) verileri artan düzende sıralar. İki sütundan oluşan yalnızca on iki satır yukarıdan aşağıya doğru sıralanır.

Kodu uygulamadan önce çalışma sayfası sıralanmamış veriler içeriyor.

**Giriş: sıralanmamış veriler** 

![yapılacak şey:image_alt_text](working-with-worksheets-gridweb_8.png)

Kodun çalıştırılmasından sonra veriler artan düzende sıralanır.

**Çıktı: veriler yukarıdan aşağıya doğru artan sırada sıralanır** 

![yapılacak şey:image_alt_text](working-with-worksheets-gridweb_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromtoptobottomascendingorder-datasortedfromtoptobottomascendingorder.jsp" >}}

###  **Soldan sağa**

Verileri soldan sağa sıralamak için:

1. Aspose.Cells.GridWeb denetimini Web Formunuza ekleyin.
1. Sıralamak istediğiniz çalışma sayfasına erişin.
1. Veri aralığını herhangi bir sıraya göre (artan veya azalan) sıralayın. Soldan sağa seçtiğinizden emin olun.

Aşağıdaki örnek, verileri iki satırda (Öğrenci Kimliği ve Öğrenci Adı) artan düzende sıralar. Dört sütundan yalnızca iki satır soldan sağa sıralanır.

Kodu uygulamadan önce çalışma sayfası sıralanmamış veriler içeriyor.

**Giriş: kod pasajını çalıştırmadan önce sıralanmamış veriler** 

![yapılacak şey:image_alt_text](working-with-worksheets-gridweb_10.png)

Kodun çalıştırılmasından sonra veriler artan sırada sıralanır.

**Çıktı: veriler soldan sağa artan sırada sıralanır** 

![yapılacak şey:image_alt_text](working-with-worksheets-gridweb_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromleftrightascendingorder-datasortedfromleftrightascendingorder.jsp" >}}

##  **Arama ve Değiştirme**

Büyük bir e-tabloda tekrarlayan değişiklikler yapmanın en hızlı yollarından biri bul ve değiştir özelliğini kullanmaktır. Bul, bir metin dizesini veya veriyi bulmanıza yardımcı olur ve onu yeni bir değerle değiştirir. Aspose.Cells.GridWeb bu özelliği sağlar. Basit bir iletişim kutusu aracılığıyla çalışma sayfasının istemci tarafında belirli bir metin dizesini veya değeri aramanıza ve değiştirmenize olanak tanır. Kısmi verileri aramanıza bile olanak tanır.

###  **Bul/Değiştir İletişim Kutusu**

Bul/Değiştir iletişim kutusunu açmanın iki yolu vardır:

1.  Kontrol aktif olduğunda tuşuna basın.**CTRL+F** iletişim kutusunu açmak için veya tuşuna basın.**CTRL+R** ile diyalogu açmak için tuşuna basın.**Yer değiştirmek** düğmesi etkinleştirildi.
1.  İmleci çalışma sayfasındaki hücre alanına taşıyın, ardından sağ tıklayın. Seçme**Bulmak** veya**Yer değiştirmek** menüden.

**Bul'u Seçme**

![yapılacak şey:image_alt_text](working-with-worksheets-gridweb_12.png)

Bul ve değiştir iletişim kutusu görüntülenir.

**Bul/Değiştir iletişim kutusu**

![yapılacak şey:image_alt_text](working-with-worksheets-gridweb_13.png)

**Bul'u kullanma**

Aramak:

1. Bul/Değiştir iletişim kutusunu açın.
1. Aramak istediğiniz dizeyi Aranan alanına yazın.
1. Aramak için Sonrakini Bul'u tıklayın.

Bulma koşulunuzla eşleşen bir sonraki hücre vurgulanır.

{{% alert color="primary" %}}

Arama kriteriniz bulunamazsa bunu size bildiren bir iletişim kutusu görüntülenir.

{{% /alert %}}

###  **Arama Seçenekleri**

İletişim kutusunda özelleştirebileceğiniz bazı arama seçenekleri vardır. Aşağıdaki tablo bunları listelemektedir.

|**HAYIR.**|**Seçenek Adı**|**Tanım**|
| :- | :- | :- |
|1|Maç durumu|Aramada büyük/küçük harfe duyarlı kullanılıp kullanılmayacağını belirtir.|
|2|Tüm kelimeyi eşleştir|Aramada kelimenin tamamının eşleştirilip eşleştirilmeyeceğini belirtir.|
|3|Yukarı ara|Aramanın aşağıdan yukarıya doğru yapılıp yapılmayacağını belirtir.|
|4|Düzenli ifade|İşaretlendiğinde denetim, Arama sürecinde Aranan metin kutusundaki dizeyi normal ifade olarak ele alır.|
|5|Formüllerde/Değerlerde Bul|Formüller seçildiğinde, formül veya biçimlendirilmemiş değer mevcutsa denetim, hücrelerin formülüyle veya biçimlendirilmemiş değeriyle eşleşir. Değerler seçildiğinde kontrol yalnızca hücrelerin görüntülenen değeriyle eşleşir.|

###  **Değiştir'i kullanma**

Metni veya değerleri değiştirmek için:

1.  Bul/Değiştir iletişim kutusunu tuşuna basarak açın.**CTRL+F** veya bir hücreye sağ tıklayıp **Bul'u seçin** *Değiştir**'e tıklamadan önce.
1.  Değiştirilecek dizeyi şuraya yazın:**İle değiştirin**alan.
1. *Değiştir**'i tıklayın.

Metni değiştirmek için:

1. İletişim kutusunu açın.
1.  Bulmak istediğiniz metni girin**Ne buldun** alanı ve onu değiştirmek istediğiniz metni seçin.**İle değiştirin** alan.
1.  Tıklayarak aynı anda bir örneği değiştirin**Sonraki Bul** ardından *Değiştir**.
1. Çalışma sayfasının içeriğinden tam olarak eminseniz *Tümünü Değiştir**'i tıklayın.

{{% alert color="primary" %}}

 Çalışma sayfası düzenleme modunda değilse,**Yer değiştirmek** düğmesi görüntülenmiyor.

{{% /alert %}}

## İstemci Tarafından Köprü Ekleme/Kaldırma

Aspose.Cells GridWeb artık istemci tarafından köprü ekleme ve kaldırma işlemlerini destekliyor. Bunun için API "addCelllink" ve "delCelllink" fonksiyonlarını sağlar. Aşağıdaki kod parçacıkları, GridWeb'de istemci tarafından köprülerin eklenmesini ve kaldırılmasını gösterir.

###  Basit kod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-1.jsp" >}}

Aşağıdaki kod parçacığını kullanarak da sayfaya bağlantı verebilirsiniz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-2.jsp" >}}

##  Yazı Tipi Ayarlarını İstemci Tarafından Güncelleyin

Aspose.Cells GridWeb artık yazı tipi ayarlarının istemci tarafından değiştirilmesini destekliyor. Bunun için API aşağıdaki fonksiyonları sağlar

- *updateCellFontStyle**: Params - normal/italik/kalın/italik&&kalın için r/i/b/ib
- *updateCellFontSize**: Parametreler - yazı tipi adı vb. 'Sistem'
- *updateCellFontName**: Parametreler - yazı tipi boyutu vb. '12pt'
- *updateCellFontColor**: Params - yok/u/l/ul/ yok için/altı çizili/üstü çizili/altı çizili&&üstünü çizili
- *updateCellFontLine**: Params - #aa22ee gibi html rengi veya yeşil, kırmızı, gibi iyi bilinen renk adı...
- *updateCellBackGroundColor**: Params - #aa22ee gibi html rengi veya yeşil, kırmızı, gibi iyi bilinen renk adı...

Aşağıdaki kod parçacığı, GridWeb'de istemci tarafından yazı tipi ayarlarının değiştirilmesini göstermektedir.

###  Basit kod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-update_font_from_client_side-1.jsp" >}}

##  İstemci Tarafından Yorum Ekle/Kaldır

Aspose.Cells GridWeb artık istemci tarafından Yorum eklemeyi ve kaldırmayı destekliyor. Bunun için API "eklemeler" ve "silmeler" fonksiyonlarını sağlar. Aşağıdaki kod parçacığı, GridWeb'de istemci tarafından yorumların eklenmesini ve kaldırılmasını gösterir.

###  Basit kod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add_remove_comments_from_client_side.jsp" >}}

##  Çalışma Sayfası Eklemek/Kaldırmak için düğmeleri göster

 Aspose.Cells GridWeb artık araç çubuğundaki düğmeleri kullanarak sayfa eklemeyi ve kaldırmayı destekliyor. Düğmelerin ön uçta görünmesi için ayarlamanız gerekir.**GridWeb1.ShowAddButton** *doğruya**. Aşağıdaki kod parçacığı, GridWeb araç çubuğuna Ekle/Kaldır düğmelerinin eklenmesini gösterir.

###  Basit kod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "GridWeb-show_add_remove_worksheet_buttons.java" >}}
