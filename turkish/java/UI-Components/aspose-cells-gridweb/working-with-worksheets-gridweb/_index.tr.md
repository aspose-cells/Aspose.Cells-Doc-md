---
title: GridWeb ile Çalışma Sayfaları
type: docs
weight: 30
url: /tr/java/working-with-worksheets-gridweb/
---

## **Çalışma Sayfalarına Erişme**

Bu konu, GridWeb kontrolünün çalışma sayfalarına erişimini tartışmaktadır. Bu sayfalar web uygulamalarında kullanıldığından bunlara web sayfaları da diyebiliriz.

GridWeb kontrolünde bulunan tüm çalışma sayfaları, GridWeb kontrolünün GridWorksheetCollection'ında depolanır. Bir çalışma sayfasına, sayfa indeksi ile basitçe erişmek mümkündür.

Geliştiriciler, örnek kod parçasında gösterildiği gibi, belirli bir çalışma sayfasına sayfa indeksi belirterek erişebilirler.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingWorksheet-AccessingWorksheet.jsp" >}}

## **Bir Çalışma Sayfasını Kaldırmak**

Bu konu, Microsoft Excel dosyalarından GridWeb API'si kullanılarak çalışma sayfalarının kaldırılması hakkında kısa bilgi sağlar. Bir çalışma sayfasını, sayfa indeksi belirterek kaldırabilirsiniz.

Geliştiriciler, örnek kod parçasında gösterildiği gibi, GridWorksheetCollection koleksiyonunun removeAt yöntemini kullanarak belirli bir çalışma sayfasını kaldırabilirler.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingWorksheet-RemovingWorksheet.jsp" >}}

## **Çalışma Sayfaları Ekleme**

Çalışma sayfaları GridWeb'ın ayrılmaz bir parçasıdır. Tüm veri, çalışma sayfaları şeklinde yönetilir ve depolanır. GridWeb, geliştiricilere Aspose.Cells.GridWeb kontrolüne bir veya daha fazla çalışma sayfası ekleme olanağı tanır. Bu konu, GridWeb'a çalışma sayfaları eklemenin basit yaklaşımlarını gösterir.

### **Sayfa Adı Belirtmeden**

Aspose.Cells.GridWeb'e bir çalışma sayfası eklemenin en basit yolu, GridWeb kontrolündeki GridWorksheetCollection sınıfının add yöntemini çağırmaktır. Bu, varsayılan adları kullanan çalışma sayfaları oluşturur (yani, Sheet1, Sheet2, Sheet3 vb.) ve bunları GridWeb kontrolüne ekler.

**Çıktı: varsayılan adlı bir çalışma sayfası, GridWeb'e eklenmiştir** 

![todo:image_alt_text](working-with-worksheets-gridweb_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithoutSpecificName-AddingWorksheetWithoutSpecificName.jsp" >}}

### **Belirtilen Sayfa Adıyla**

Varsayılan adlandırma düzeni yerine GridWeb kontrolüne belirli bir ad ile çalışma sayfası eklemek için, belirtilen dize SayfaAdı'nı alabilen add yönteminin aşırı yüklenmiş bir sürümünü çağırın. Örneğin, aşağıdaki örnek, Invoice adında bir çalışma sayfası ekler.

**Çıktı: belirtilen adlı bir çalışma sayfası, GridWeb'e eklenmiştir** 

![todo:image_alt_text](working-with-worksheets-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithSpecificName-AddingWorksheetWithSpecificName.jsp" >}}

{{% alert color="primary" %}}

add() yöntemi, eklenen yeni çalışma sayfasının indeksini döndürür; bu indeks, bu çalışma sayfasının örneğine erişmek için kullanılabilir. Aspose.Cells.GridWeb'de çalışma sayfalarına erişim hakkında daha fazla bilgi için [Çalışma Sayfalarına Erişme](/cells/tr/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets) konusuna bakın.

{{% /alert %}}

## **Çalışma Sayfasını Yeniden Adlandırma**

Çalışma sayfasını yeniden adlandırmak, GridWeb'de birçok çalışma sayfası ile çalışırken onların adlarını daha anlamlı hale getirmeye karar verdiğinizde çok faydalı olabilir. Örneğin, Sheet1 yerine Fatura adı taşıyan bir çalışma sayfası, Invoice olarak yeniden adlandırılabilir. Bu konu, bu basit ancak kullanışlı özelliği açıklar.

### **Çalışma Sayfasını Yeniden Adlandırma**

Tüm çalışma sayfaları, geliştiricilerin çalışma sayfalarının adlarını erişebilmesini veya değiştirebilmesini sağlayan bir Name özelliğine sahiptir. Bir çalışma sayfasını yeniden adlandırmak için:

1. GridWorksheetCollection'dan bir çalışma sayfasına erişin.
1. Seçili çalışma sayfasını yeniden adlandırın.

{{% alert color="primary" %}}

Aspose.Cells.GridWeb'de çalışma sayfalarına erişim hakkında daha fazla bilgi için lütfen [Çalışma Sayfalarına Erişme](/cells/tr/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets) konusuna başvurun.

{{% /alert %}}

Kodu çalıştırmadan önce, çalışma sayfasının varsayılan adı olan Sheet1 olarak adlandırıldığını unutmayın.

**Giriş dosyası: varsayılan adı Sheet1 olan bir çalışma sayfası** 

![todo:image_alt_text](working-with-worksheets-gridweb_3.png)

Kodu çalıştırdıktan sonra, çalışma sayfası Invoice olarak yeniden adlandırılmıştır.

**Çıktı: çalışma sayfası Invoice olarak yeniden adlandırılmıştır** 

![todo:image_alt_text](working-with-worksheets-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RenamingWorksheet-RenamingWorksheet.jsp" >}}

## **Çalışsayfalarını Kopyalama**

[Çalışsayfası Ekleme](/cells/tr/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-addingworksheets), GridWeb'e yeni çalışsayfaları nasıl ekleyeceğinizi anlatır. Ayrıca Aspose.Cells.GridWeb denetimine başka bir çalışsayfanın kopyasını (veya replikasını) eklemek de mümkündür. Bu özellik, aynı veya benzer verilerin bir çalışsayfada başka bir çalışsayfada da gereklidir durumda işe yarayabilir. Bu durumda, var olan bir çalışsayfanın kopyasını kopyalamak ve Aspose.Cells.GridWeb'e yeni bir çalışsayfa olarak eklemek, sıfırdan oluşturmaktan daha kolaydır.

### **Sayfa indeksi Kullanma**

Aşağıdaki örnek kod, GridWorksheetCollection'ın addCopy yönteminde çalışsayfanın indeksini belirterek GridWeb denetimine bir çalışsayfa kopyası nasıl ekleyeceğinizi gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetIndex-CopyWorksheetUsingSheetIndex.jsp" >}}
### **Sayfa Adını Kullanma**
Aşağıdaki örnek kod, GridWorksheetCollection'ın addCopy yönteminde çalışsayfanın adını belirterek GridWeb denetimine bir çalışsayfa kopyası nasıl ekleyeceğinizi gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetName-CopyWorksheetUsingSheetName.jsp" >}}

{{% alert color="primary" %}}

addCopy yöntemi, yeni eklenen çalışsayfanın indeksini döndürür ve bu indeksi kullanarak çalışsayfa örneğine erişilebilir. Çalışsayfalara erişim hakkında daha fazla bilgi için [Çalışsayfalara Erişme](/cells/tr/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets) bölümünü okuyun.

{{% /alert %}}

## **Adlandırılmış Aralıklarla Çalışma**

Genellikle sütun ve satır etiketleri hücrelere benzersiz bir şekilde atıfta bulunmak için kullanılır. Ancak hücreleri, hücre aralıklarını, formülleri veya sabit değerleri temsil etmek için betimleyici adlar oluşturabilirsiniz.

Kelime **adı**, bir hücreyi, hücre aralığını, formülü veya sabit değeri temsil eden bir karakter dizisine atıfta bulunabilir. Örneğin, Satışlar!C20:C30 gibi anlaşılması zor aralıklara atıfta bulunmak için, Ürünler gibi anlaşılması kolay adlar kullanın.

Etiketler, aynı çalışsayfadaki verilere atıfta bulunan formüllerde kullanılabilir; başka bir çalışsayfadaki bir aralığı temsil etmek isterseniz bir ad kullanabilirsiniz. **Adlandırılmış aralıklar**, Microsoft Excel'in en güçlü özelliklerinden biridir.

Kullanıcılar bir aralığa ad atayabilir ve bu adı formüllerde kullanabilir. Aspose.Cells.GridWeb bu özelliği destekler.

### **Formüllerde İsimli Aralıkları Ekleme/Başvuru Yapma**

GridWeb denetimi, adlandırılmış aralıklarla çalışmak için iki sınıf (GridName ve GridNameCollection) sağlar.

Aşağıdaki kod parçacığı, bunları nasıl kullanacağınızı anlamanıza yardımcı olacaktır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingNamedRangesinFormulas-AddingNamedRangesinFormulas.jsp" >}}

## **Çalışsayfadaki Yorumları Yönetme**

Bu konu, çalışsayfalardan yorum eklemeyi, erişmeyi ve kaldırmayı tartışır. Yorumlar, çalışsayfa ile çalışacak olan kullanıcılar için not veya kullanışlı bilgiler eklemek için kullanışlıdır. Geliştiriciler, çalışsayfanın herhangi bir hücresine yorum eklemekte esneklik sahip olurlar.

### **Yorumlarla Çalışma**

#### **Yorum Ekleme**

Bir çalışsayfaya yorum eklemek için lütfen aşağıdaki adımları izleyin:

1. Aspose.Cells.GridWeb denetimini Web Formuna ekleyin.
2. Yorum eklemek istediğiniz çalışsayfaya erişin.
1. Bir hücreye yorum ekleyin.
4. Yeni yorum için bir not ayarlayın.

**Çalışsayfaya bir yorum eklenmiştir** 

![todo:image_alt_text](working-with-worksheets-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingComments-AddingComments.jsp" >}}

#### **Yorumlara Erişme**

Bir yoruma erişmek için:

1. Yorum içeren hücreye erişin.
2. Hücrenin referansını alın.
3. Yoruma erişmek için referansı Comment koleksiyonuna iletil.
1. Artık yorumun özelliklerini değiştirmek mümkün.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingComments-AccessingComments.jsp" >}}

#### **Yorumları Kaldırma**

Bir yorumu kaldırmak için:

1. Yukarıda açıklandığı gibi hücreye erişin.
1. Yorum koleksiyonunun removeAt yöntemini kullanarak yorumu kaldırın.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingComments-RemovingComments.jsp" >}}

## **Çalışma Sayfasındaki Bağlantıları Yönetme**

Bu konu Aspose.Cells.GridWeb'de desteklenen bağlantı türlerini ve bunları programlı olarak nasıl yöneteceğinizi tartışmaktadır. Bağlantılar, web URL'lerine bağlantı oluşturmak veya sunucuya postback yapmak için kullanılabilir.

### **Bağlantı Türleri**

Aspose.Cells.GridWeb tarafından desteklenen aşağıdaki bağlantılar:

- Metin URL bağlantıları, metne uygulanan URL bağlantıları.
- Görüntü URL bağlantıları, resimlere uygulanan URL bağlantıları.

#### **Metin URL Bağlantıları**

Aşağıdaki örnek bir çalışma sayfasına iki bağlantı ekler. Birinde _blank hedefi varken diğeri _parent'e ayarlanmıştır.

![todo:image_alt_text](working-with-worksheets-gridweb_6.png)

**Çıktı: çalışma sayfasına eklenen metin bağlantıları**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-TextURLHyperlinks-TextURLHyperlinks.jsp" >}}

#### **Görüntü URL Bağlantıları**

Aşağıdaki örnek, bir çalışma sayfasına görüntü URL bağlantısını ekler.

![todo:image_alt_text](working-with-worksheets-gridweb_7.png)

**Çıktı: çalışma sayfasına eklenen görüntü bağlantısı**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-ImageURLHyperlinks-ImageURLHyperlinks.jsp" >}}

## **Veri Sıralama**

Sıralama, veri işleme konusunda çok değerli bir özelliktir. Sırasız veri, belirli bilgileri ararken kullanıcılar için bir baş ağrısıdır. Aspose.Cells.GridWeb güçlü sıralama özelliklerini destekler. Bu konu, Aspose.Cells.GridWeb API'sını kullanarak veri sıralamanın nasıl yapıldığını tartışmaktadır.

Aspose.Cells.GridWeb, geliştiricilere verileri yatay ve dikey olarak sıralama imkanı tanır, böylece geliştiriciler verileri yukarıdan aşağıya veya soldan sağa sıralayabilirler.

### **Yukarıdan Aşağıya**

Verileri yukarıdan aşağıya doğrultusunda sıralamak için:

1. Aspose.Cells.GridWeb denetimini Web Formunuza ekleyin.
1. Sıralamak istediğiniz çalışsayfaya erişin.
1. Veri aralığını herhangi bir düzende (artan veya azalan) sıralayın. Yukarıdan aşağıya doğrultusunda sıralamayı seçtiğinizden emin olun.

Aşağıdaki örnek, bir çalışma sayfasının iki sütununu (Öğrenci Kimliği ve Öğrenci Adı) artan düzende yukarıdan aşağıya doğrultusunda sıralar. İki sütunun sadece on iki satırı artan düzende sıralanmıştır.

Kod uygulanmadan önce çalışsayfa düzensiz veri içerir.

**Giriş: sıralanmamış veri** 

![todo:image_alt_text](working-with-worksheets-gridweb_8.png)

Kodun çalıştırılmasından sonra, veri artan düzende sıralanmıştır.

**Çıktı: yukarıdan aşağıya doğrultusunda artan düzende sıralanmış veri** 

![todo:image_alt_text](working-with-worksheets-gridweb_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromtoptobottomascendingorder-datasortedfromtoptobottomascendingorder.jsp" >}}

### **Soldan Sağa**

Verileri soldan sağa sıralamak için:

1. Aspose.Cells.GridWeb denetimini Web Formunuza ekleyin.
1. Sıralamak istediğiniz çalışsayfaya erişin.
1. Veri aralığını istenen düzende sıralayın (artan veya azalan). Soldan sağa seçtiğinizden emin olun.

Aşağıdaki örnek, iki satırda (Öğrenci ID ve Öğrenci Adı) bulunan verileri artan sırada sıralar. Dört sütunun sadece iki satırı soldan sağa sıralanır.

Kod uygulanmadan önce çalışsayfa düzensiz veri içerir.

**Giriş: kod parçasını uygulamadan önce sıralanmamış veri** 

![todo:image_alt_text](working-with-worksheets-gridweb_10.png)

Kod uygulandıktan sonra veri artan sırada sıralanır.

**Çıkış: soldan sağa artan sırada sıralanmış veri** 

![todo:image_alt_text](working-with-worksheets-gridweb_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromleftrightascendingorder-datasortedfromleftrightascendingorder.jsp" >}}

## **Arama ve Değiştirme**

Büyük bir elektronik tabloda tekrarlayan değişiklikler yapmanın en hızlı yollarından biri bul ve değiştir özelliğini kullanmaktır. Bul, bir metin dizesini veya veriyi bulmanıza ve değiştir, yeni bir değerle değiştirmenize yardımcı olur. Aspose.Cells.GridWeb bu özelliği sağlar. Basit bir iletişim kutusu aracılığıyla çalışsayfada metin dizesi veya değeri bulmanıza ve değiştirme olanağı sağlar. Hatta kısmi veri aramanıza bile izin verir.

### **Bul/Değiştir İletişim Kutusu**

Bul/Değiştir iletişim kutusunu açmanın iki yolu vardır:

1. Denetim etkin olduğunda, iletişim kutusunu açmak için **CTRL+F** tuşuna basın veya **CTRL+R** tuşuna basarak Değiştir düğmesini etkinleştirin.
1. Çalışsayfadaki hücre alanına imleci taşıyın, ardından sağ tıklayın. Menüden **Bul** veya **Değiştir** i seçin.

**Bul seçimi**

![todo:image_alt_text](working-with-worksheets-gridweb_12.png)

Bul ve değiştirme iletişim kutusu görüntülenir.

**Bul/Değiştir iletişim kutusu**

![todo:image_alt_text](working-with-worksheets-gridweb_13.png)

**Bulma Kullanma**

Arama yapmak için:

1. Bul/Değiştir iletişim kutusunu açın.
1. Aramak istediğiniz dizesini Bul alanına yazın.
1. Aramak için Bul Next ü tıklayın.

Arama koşulunuzu karşılayan sonraki hücre vurgulanır.

{{% alert color="primary" %}}

Arama kriteriniz bulunamazsa, size bildirmek için bir iletişim kutusu görüntülenir.

{{% /alert %}}

### **Arama Seçenekleri**

İleride özelleştirebileceğiniz bazı arama seçenekleri bulunmaktadır. Aşağıdaki tabloda bunlar listelenmiştir.

|**No.**|**Seçenek Adı**|**Açıklama**|
| :- | :- | :- |
|1|Büyük/küçük harf eşleşmesi|Aramada büyük/küçük harf duyarlı olup olunmayacağını gösterir.|
|2|Tam kelime eşleştir|Aramada tam kelime eşleştirip eşleştirmediğini belirtir.|
|3|Yukarıdan aşağıya ara|Aramanın aşağıdan yukarıya yapılıp yapılmayacağını belirtir.|
|4|Düzenli ifade|İşlem sırasında Bul alandaki metni düzenli ifade olarak işleyip işlemediğini belirtir.|
|5|Formüller/Değerlerde Bul|Formüller seçildiğinde, kontrol, hücrelerin formülünü veya biçimsiz değerini eşleştirir. Değerler seçildiğinde, kontrol yalnızca hücrelerin görüntülenen değerini eşleştirir.|

### **Değiştirme Kullan**

Metni veya değerleri değiştirmek için:

1. **CTRL+F** tuşuna basarak Bul/Değiştir iletişim kutusunu açın veya Değiştir'e tıklamadan önce bir hücreye sağ tıklayın ve ardından **Bul**'ü seçin.
1. Yerine yazılacak dizeyi **Yerine Yaz** alanına yazın.
1. **Yerine Yaz**'a tıklayın.

Metni değiştirmek için:

1. İletişim kutusunu açın.
1. **Bul** alanına bulmak istediğiniz metni girin ve **Yerine Yaz** alanına değiştirmek istediğiniz metni girin.
1. **Sonrakini Bul**'e tıklayarak bir seferinde bir önceği değiştirerek **Sonrakini Bul**'e tıklayın.
1. Çalışma sayfasının ne içerdiğinden eminseniz, **Tümünü Değiştir**'e tıklayın.

{{% alert color="primary" %}}

Eğer çalışma sayfası düzenleme modunda değilse, **Değiştir** düğmesi görüntülenmez.

{{% /alert %}}

## İstemci Tarafından Bağlantıları Ekle/Kaldır

Aspose.Cells GridWeb artık istemci tarafından bağlantı ekleme ve kaldırma işlemini destekler. Bunun için API, "addCelllink" ve "delCelllink" işlevlerini sağlar. Aşağıdaki kod parçaları, GridWeb'de istemci tarafından bağlantı ekleme ve kaldırma işlemini göstermektedir.

### Örnek Kod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-1.jsp" >}}

Ayrıca, aşağıdaki kod parçasını kullanarak sayfaya bağlantı kurabilirsiniz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-2.jsp" >}}

## İstemci Tarafından Yazı Tipi Ayarlarını Güncelle

Aspose.Cells GridWeb artık istemci tarafından yazı tipi ayarlarını değiştirme işlemini destekler. Bunun için API aşağıdaki işlevleri sağlar

- **updateCellFontStyle**: Parametreler - r/i/b/ib: normal/italik/kalın/italik&&kalın
- **updateCellFontSize**: Parametreler - yazıtipi, vb. 'Sistem'
- **updateCellFontName**: Parametreler - yazı boyutu, vb. '12pt'
- **updateCellFontColor**: Parametreler - yok/u/l/ul/ for yok/altı çizili/üzeri çizili/altı&&üzeri çizili
- **updateCellFontLine**: Parametreler - html rengi #aa22ee veya yeşil, kırmızı gibi yaygın olarak bilinen renk ismi
- **updateCellBackGroundColor**: Parametreler - html rengi #aa22ee veya yeşil, kırmızı gibi yaygın olarak bilinen renk ismi

Aşağıdaki kod parçacığı, GridWeb'de istemci tarafından yazı tipi ayarlarını değiştirme işlemini göstermektedir.

### Örnek Kod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-update_font_from_client_side-1.jsp" >}}

## İstemci Tarafından Yorumları Ekle/Kaldır

Aspose.Cells GridWeb artık istemci tarafından Yorum eklemeyi ve kaldırmayı destekler. Bu amaçla, API "addcomments" ve "delcomments" işlevlerini sağlar. Aşağıdaki kod parçacığı, istemci tarafından GridWeb'de yorum eklemeyi ve kaldırmayı göstermektedir.

### Örnek Kod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add_remove_comments_from_client_side.jsp" >}}

## Çalışsayı Ekle/Kaldır Düğmelerini Göster

Aspose.Cells GridWeb artık araç çubuğundaki düğmeleri kullanarak sayfa eklemeyi ve kaldırmayı destekler. Ön tarafta düğmelerin görünmesi için **GridWeb1.ShowAddButton**'ı **true** olarak ayarlamanız gerekir. Aşağıdaki kod parçacığı, GridWeb araç çubuğuna Ekle/Kaldır düğmeleri eklemeyi göstermektedir.

### Örnek Kod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "GridWeb-show_add_remove_worksheet_buttons.java" >}}
