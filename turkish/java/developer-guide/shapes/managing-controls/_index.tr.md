---
title: Kontrolleri Yönetme
type: docs
weight: 120
url: /tr/java/managing-controls/
---
## **giriiş**

Geliştiriciler, metin kutuları, onay kutuları, radyo düğmeleri, açılan kutular, etiketler, düğmeler, çizgiler, dikdörtgenler, yaylar, ovaller, döndürücüler, kaydırma çubukları, grup kutuları vb. gibi farklı çizim nesneleri ekleyebilir. tüm çizim nesneleri. Ancak, henüz desteklenmeyen birkaç çizim nesnesi veya şekli vardır. Bu çizim nesnelerini Microsoft Excel kullanarak bir tasarımcı elektronik tablosunda oluşturun ve ardından tasarımcı elektronik tablosunu Aspose.Cells'e aktarın. Aspose.Cells, bu çizim nesnelerini bir tasarımcı elektronik tablosundan yüklemenize ve oluşturulmuş bir dosyaya yazmanıza olanak tanır.

## **Çalışma Sayfasına Metin Kutusu Denetimi Ekleme**

Bir rapordaki önemli bilgileri vurgulamanın bir yolu, bir metin kutusu kullanmaktır. Örneğin, şirket adını vurgulamak veya satışların en yüksek olduğu coğrafi bölgeyi vb. belirtmek için metin ekleyin. Aspose.Cells, koleksiyona yeni bir metin kutusu eklemek için kullanılan TextBoxes sınıfını sağlar. Başka bir sınıf var,[**Metin kutusu**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox), tüm ayar türlerini tanımlamak için kullanılan bir metin kutusunu temsil eder. Bazı önemli üyeleri vardır:

-  bu[**getTextÇerçevesi**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#TextFrame) yöntem bir döndürür[**MsoTextÇerçevesi**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoTextFrame) metin kutusunun içeriğini ayarlamak için kullanılan nesne.
-  bu[**yerleşimi ayarla**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Placement) method yerleştirme tipini belirtir.
-  bu[**setFont**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Font) method font özniteliklerini belirtir.
-  bu[**köprü ekle**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#addHyperlink(java.lang.String)) yöntemi, metin kutusu için bir köprü ekler.
-  bu[**Doldurma Biçimi**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#FillFormat) mülkiyet iadeleri[**MsoFillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoFillFormat) metin kutusu için dolgu formatını ayarlamak için kullanılan nesne.
-  bu[**Çizgi Biçimi**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#LineFormat) özellik döndürür[**MsoLineFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoLineFormat) genellikle metin kutusu satırının stilini ve ağırlığını belirlemek için kullanılan nesne.
-  bu[**Metin ayarla**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Text)method, metin kutusu için giriş metnini belirtir.

Aşağıdaki örnek, çalışma kitabının ilk çalışma sayfasında iki metin kutusu oluşturur. İlk metin kutusu, farklı biçim ayarlarıyla iyi bir şekilde döşenmiştir. İkincisi basit bir tanesidir.

Aşağıdaki çıktı, kod yürütülerek oluşturulur:

**Çalışma sayfasında iki metin kutusu oluşturulur** 

![yapılacaklar:resim_alternatif_Metin](managing-controls_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingTextBoxControl-1.java" >}}

## **Tasarımcı Elektronik Tablolarında Metin Kutusu Kontrollerini Değiştirme**

 Aspose.Cells ayrıca tasarımcı çalışma sayfalarındaki metin kutularına erişmenizi ve bunları değiştirmenizi sağlar. Kullan[**Worksheet.getTextBoxes**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#TextBoxes) sayfadaki metin kutuları koleksiyonunu alma özelliği.

Aşağıdaki örnek, yukarıdaki örnekte oluşturduğumuz Microsoft Excel dosyasını – tsttextboxes.xls – kullanır. İki metin kutusunun metin dizelerini alır ve dosyayı kaydetmek için ikinci metin kutusunun metnini değiştirir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-ManipulatingTextBoxControls-1.java" >}}

## **Çalışma Sayfasına CheckBox Denetimi Ekleme**

Bir kullanıcıya doğru veya yanlış gibi iki seçenek arasında seçim yapması için bir yol sağlamak istiyorsanız, onay kutuları kullanışlıdır; Evet veya Hayır. Aspose.Cells, çalışma sayfalarında onay kutularını kullanmanıza izin verir. Örneğin, belirli bir satın almayı açıklayabileceğiniz ya da açıklamayabileceğiniz bir finansal projeksiyon çalışma sayfası geliştirmiş olabilirsiniz. Bu durumda, çalışma sayfasının en üstüne bir onay kutusu yerleştirmek isteyebilirsiniz. Daha sonra bu onay kutusunun durumunu başka bir hücreye bağlayabilirsiniz, böylece onay kutusu seçilirse hücrenin değeri True olur; seçili değilse hücrenin değeri False olur.

### **Microsoft Excel'i kullanma**

Çalışma sayfanıza bir onay kutusu denetimi yerleştirmek için şu adımları izleyin:

1. Formlar araç çubuğunun görüntülendiğinden emin olun.
1.  Tıkla**Onay Kutusu** Formlar araç çubuğundaki aracı.
1. Çalışma sayfası alanınızda, onay kutusunu ve onay kutusunun yanındaki etiketi tutacak dikdörtgeni tanımlamak için tıklayın ve sürükleyin.
1. Onay kutusu yerleştirildikten sonra, fare imlecini etiket alanına getirin ve etiketi değiştirin.
1.  İçinde**Cell Bağlantı**alanında, bu onay kutusunun bağlanması gereken hücrenin adresini belirtin.
1.  Tıklamak**TAMAM**.

### **Aspose.Cells'i kullanma**

 Aspose.Cells şunları sağlar:[**Onay Kutusu Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/checkboxcollection) koleksiyona yeni bir onay kutusu eklemek için kullanılan sınıf. Başka bir sınıf var,[**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/java/com.aspose.cells/CheckBox), bir onay kutusunu temsil eder. Bazı önemli üyeleri vardır:

-  bu[**setLinkedCell**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#LinkedCell) yöntemi, onay kutusuna bağlı bir hücreyi belirtir.
-  bu[**Metin ayarla**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#Text) yöntem, onay kutusuyla ilişkili metin dizesini belirtir. Onay kutusunun etiketidir.
-  bu[**değer ayarla**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#Value) yöntem, onay kutusunun işaretlenip işaretlenmediğini belirtir.

Aşağıdaki örnek, çalışma sayfasına bir onay kutusunun nasıl ekleneceğini gösterir. Aşağıdaki çıktı, kod yürütüldükten sonra oluşturulur.

**Çalışma sayfasına bir CheckBox eklendi** 

![yapılacaklar:resim_alternatif_Metin](managing-controls_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingCheckBoxControl-1.java" >}}

## **Çalışma Sayfasına RadioButton Kontrolü Ekleme**

Bir radyo düğmesi veya bir seçenek düğmesi, yuvarlak bir kutudan yapılmış bir denetimdir. Kullanıcı yuvarlak kutuyu seçerek kararını verir. Bir radyo düğmesine, her zaman olmasa da genellikle başkaları eşlik eder. Bu tür radyo düğmeleri bir grup olarak görünür ve davranır. Kullanıcı bunlardan sadece birini seçerek hangi butonun geçerli olduğuna karar verir. Kullanıcı bir düğmeyi tıkladığında, doldurulur. Gruptaki bir düğme seçildiğinde, aynı grubun düğmeleri boştur.

### **Microsoft Excel'i kullanma**

Çalışma sayfanıza bir Radyo Düğmesi denetimi yerleştirmek için şu adımları izleyin:

1.  Emin ol**Formlar** araç çubuğu görüntülenir.
1.  Tıkla**Seçenek tuşu** alet.
1. Çalışma sayfasında, seçenek düğmesini ve seçenek düğmesinin yanındaki etiketi tutacak dikdörtgeni tanımlamak için tıklayın ve sürükleyin.
1. Radyo düğmesi çalışma sayfasına yerleştirildikten sonra, fare imlecini etiket alanına getirin ve etiketi değiştirin.
1.  İçinde**Cell Bağlantı** alanında, bu radyo düğmesinin bağlanması gereken hücrenin adresini belirtin.
1.  Tıklamak**TAMAM**.

### **Aspose.Cells'i kullanma**

 bu[**Şekil Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)class, bir çalışma sayfasına bir radyo düğmesi denetimi eklemek için kullanılabilecek addShape adlı bir yöntem sağlar. Yöntem, bir RadioButton nesnesi döndürebilir. RadioButton sınıfı, bir seçenek düğmesini temsil eder. Bazı önemli üyeleri vardır:

- setLinkedCell yöntemi, radyo düğmesine bağlı bir hücreyi belirtir.
- setText yöntemi, radyo düğmesiyle ilişkili metin dizesini belirtir. Radyo düğmesinin etiketidir.
- Checked özelliği, radyo düğmesinin işaretli olup olmadığını belirtir.
- setFillFormat yöntemi, radyo düğmesinin doldurma biçimini belirtir.
- setLineFormat yöntemi, seçenek düğmesinin satır biçimi stillerini belirtir.

Aşağıdaki örnek, bir çalışma sayfasına radyo düğmelerinin nasıl ekleneceğini gösterir. Örnek, yaş gruplarını temsil eden üç radyo düğmesi ekler. Kod çalıştırıldıktan sonra aşağıdaki çıktı üretilecektir.

**Çalışma sayfasına bazı Radyo Düğmeleri eklendi** 

![yapılacaklar:resim_alternatif_Metin](managing-controls_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingRadioButtonControl-1.java" >}}

## **Çalışma Sayfasına Birleşik Giriş Kutusu Denetimi Ekleme**

Veri girişini kolaylaştırmak veya girişleri tanımladığınız belirli öğelerle sınırlamak için, çalışma sayfasının herhangi bir yerindeki hücrelerden derlenen geçerli girişlerin açılır listesini veya birleşik giriş kutusunu oluşturabilirsiniz. Bir hücre için açılır liste oluşturduğunuzda, o hücrenin yanında bir ok görüntülenir. Bu hücreye bilgi girmek için oku tıklatın ve ardından istediğiniz girişi tıklatın.

### **Microsoft Excel'i kullanma**

Çalışma sayfanıza birleşik giriş kutusu denetimi yerleştirmek için şu adımları izleyin:

1.  Emin ol**Formlar** araç çubuğu görüntülenir.
1.  Tıkla**Açılan kutu** alet.
1. Çalışma sayfası alanınızda, birleşik giriş kutusunu tutacak dikdörtgeni tanımlamak için tıklayın ve sürükleyin.
1.  Birleşik giriş kutusu çalışma sayfasına yerleştirildikten sonra, kontrolü sağ tıklatarak**Biçim Kontrolü** ve giriş aralığını belirtin.
1.  İçinde**Cell Bağlantı** alanında, bu açılan kutunun bağlanması gereken hücrenin adresini belirtin.
1.  Tıklamak**TAMAM**.

### **Aspose.Cells'i kullanma**

 bu[**Şekil Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)class, çalışma sayfasına birleşik giriş kutusu denetimi eklemek için kullanılabilen addShape adlı bir yöntem sağlar. Yöntem, ComboBox nesnesini döndürebilir. ComboBox sınıfı, bir açılan kutuyu temsil eder. Bazı önemli üyeleri vardır:

- setLinkedCell yöntemi, birleşik giriş kutusuna bağlı bir hücreyi belirtir.
- setInputRange yöntemi, açılan kutuyu doldurmak için kullanılan çalışma sayfası hücre aralığını belirtir.
- setDropDownLines yöntemi, birleşik giriş kutusunun açılır bölümünde görüntülenen liste satırlarının sayısını belirtir.
- setShadow yöntemi, birleşik giriş kutusunun 3B gölgelendirmeye sahip olup olmadığını gösterir.

Aşağıdaki örnek, çalışma sayfasına birleşik giriş kutusunun nasıl ekleneceğini gösterir. Kod yürütülürken aşağıdaki çıktı oluşturulur.

**Çalışma sayfasına açılan kutu eklendi** 

![yapılacaklar:resim_alternatif_Metin](managing-controls_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingComboBoxControl-1.java" >}}

## **Çalışma Sayfasına Etiket Denetimi Ekleme**

 Etiketler, kullanıcılara bir elektronik tablonun içeriği hakkında bilgi vermenin bir yoludur. Aspose.Cells, bir çalışma sayfasına etiket eklemeyi ve düzenlemeyi mümkün kılar. bu[**Şekil Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)class, çalışma sayfasına bir etiket denetimi eklemek için kullanılan addShape adlı bir yöntem sağlar. Yöntem bir Label nesnesi döndürür. Label sınıfı, çalışma sayfasındaki bir etiketi temsil eder. Bazı önemli üyeleri vardır:

- setText yöntemi, bir etiketin başlık dizesini belirtir.
- setPlacement yöntemi, etiketin çalışma sayfasındaki hücrelere eklenme biçimi olan PlacementType'ı belirtir.

Aşağıdaki örnek, çalışma sayfasına nasıl etiket ekleneceğini gösterir. Kod yürütülürken aşağıdaki çıktı oluşturulur.

**Çalışma sayfasına bir etiket eklenir**

![yapılacaklar:resim_alternatif_Metin](managing-controls_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingLabelControl-1.java" >}}

## **Bir Çalışma Sayfasına Liste Kutusu Denetimi Ekleme**

Liste kutusu denetimi, tekli veya çoklu öğe seçimine izin veren bir liste denetimi oluşturur.

### **Microsoft Excel'i kullanma**

Çalışma sayfasına bir liste kutusu denetimi yerleştirmek için:

1.  Emin ol**Formlar** araç çubuğu görüntülenir.
1.  Tıkla**Liste kutusu** alet.
1. Çalışma sayfası alanınızda, liste kutusunu tutacak dikdörtgeni tanımlamak için tıklayın ve sürükleyin.
1.  Liste kutusu çalışma sayfasına yerleştirildikten sonra, kontrole sağ tıklayın.**Biçim Kontrolü** ve giriş aralığını belirtin.
1.  İçinde**Cell Bağlantı**alanında, bu liste kutusunun bağlanması gereken hücrenin adresini belirtin ve seçim tipi (Tek, Çoklu, Genişlet) özniteliğini ayarlayın.
1.  Tıklamak**TAMAM**.

### **Aspose.Cells'i kullanma**

 bu[**Şekil Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) class, bir çalışma sayfasına liste kutusu denetimi eklemek için kullanılan addShape adlı bir yöntem sağlar. Yöntem bir ListBox nesnesi döndürür. ListBox sınıfı bir liste kutusunu temsil eder. Bazı önemli üyeleri vardır:

- setLinkedCell yöntemi, liste kutusuna bağlı bir hücreyi belirtir.
- setInputRange yöntemi, liste kutusunu doldurmak için kullanılan çalışma sayfası hücre aralığını belirtir.
- setSelectionType yöntemi, liste kutusunun seçim modunu belirtir.
- setShadow yöntemi, liste kutusunun 3B gölgelendirmeye sahip olup olmadığını gösterir.

Aşağıdaki örnek, çalışma sayfasına bir liste kutusunun nasıl ekleneceğini gösterir. Kod yürütülürken aşağıdaki çıktı oluşturulur.

**Çalışma sayfasına bir liste kutusu eklendi** 

![yapılacaklar:resim_alternatif_Metin](managing-controls_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingListBoxControl-1.java" >}}

## **Bir Çalışma Sayfasına Düğme Denetimi Ekleme**

Düğmeler, bazı eylemleri gerçekleştirmek için kullanışlıdır. Bazen, bir web sayfasını açmak için düğmeye bir VBA Makrosu atamak veya bir köprü atamak yararlı olabilir.

### **Microsoft Excel'i kullanma**

Çalışma sayfanıza bir düğme denetimi yerleştirmek için:

1.  Emin ol**Formlar** araç çubuğu görüntülenir.
1.  Tıkla**Buton** alet.
1. Çalışma sayfası alanınızda, düğmeyi tutacak dikdörtgeni tanımlamak için tıklayın ve sürükleyin.
1.  Liste kutusu çalışma sayfasına yerleştirildikten sonra, kontrole sağ tıklayın ve seçin.**Biçim Kontrolü**, ardından bir VBA Makrosu ve yazı tipi, hizalama, boyut, kenar boşluğu vb. ile ilgili öznitelikleri belirtin.
1.  Tıklamak**TAMAM**.

### **Aspose.Cells'i kullanma**

 bu[**Şekil Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) class, çalışma sayfasına düğme denetimi eklemek için kullanılan addShape adlı bir yöntem sağlar. Yöntem, bir Button nesnesi döndürebilir. Button sınıfı bir düğmeyi temsil eder. Bazı önemli üyeleri vardır:

- setText yöntemi, düğmenin başlığını belirtir.
- setPlacement yöntemi, düğmenin çalışma sayfasındaki hücrelere eklenme biçimi olan PlacementType'ı belirtir.
- addHyperlink yöntemi, düğme denetimi için bir köprü ekler. Düğmeye tıklandığında ilgili URL'ye gidilecektir.

Aşağıdaki örnek, çalışma sayfasına nasıl düğme ekleneceğini gösterir. Kod yürütülürken aşağıdaki çıktı üretilir

**Çalışma sayfasına bir düğme eklendi**

![yapılacaklar:resim_alternatif_Metin](managing-controls_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingButtonControl-1.java" >}}

## **Çalışma Sayfasına Hat Kontrolü Ekleme**

Aspose.Cells, çalışma sayfalarınıza otomatik şekiller çizmenizi sağlar. Kolayca bir çizgi oluşturabilirsiniz. Ayrıca satırı biçimlendirmenize de izin verilir. Örneğin ipin rengini değiştirebilir, ihtiyacınıza göre ipin ağırlığını ve stilini belirleyebilirsiniz.

### **Microsoft Excel'i kullanma**

1.  Üzerinde**Resim çizme** araç çubuğu, tıklayın**Otomatik Şekiller** , işaret etmek**çizgiler**ve istediğiniz çizgi stilini seçin.
1. Çizgiyi çizmek için sürükleyin.
1. Aşağıdakilerden birini veya her ikisini yapın:
 1. Çizgiyi başlangıç noktasından 15 derecelik açılarla çizmek üzere sınırlamak için sürüklerken SHIFT tuşunu basılı tutun.
 1. Çizgiyi ilk bitiş noktasından zıt yönlerde uzatmak için sürüklerken CTRL tuşunu basılı tutun.

### **Aspose.Cells'i kullanma**

 bu[**Şekil Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)class, çalışma sayfasına bir çizgi şekli eklemek için kullanılan addShape adlı bir yöntem sağlar. Yöntem, bir LineShape nesnesi döndürebilir. LineShape sınıfı bir çizgiyi temsil eder. Bazı önemli üyeleri vardır:

- setDashStyle yöntemi, bir satırın biçimini belirtir.
- setPlacement yöntemi, satırın çalışma sayfasındaki hücrelere eklenme biçimi olan PlacementType'ı belirtir.

Aşağıdaki örnek, çalışma sayfasına nasıl satır ekleneceğini gösterir. Farklı stillerde üç çizgi oluşturur. Aşağıdaki çıktı kodu yürüttükten sonra oluşturulur

**Çalışma sayfasına birkaç satır eklenir** 

![yapılacaklar:resim_alternatif_Metin](managing-controls_8.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingLineControl-1.java" >}}

### **Bir Çizgiye Ok Başı Ekleme**

Aspose.Cells ayrıca ok çizgileri çizmenize de olanak tanır. Bir satıra ok ucu eklemek ve satırı biçimlendirmek mümkündür. Örneğin, çizginin rengini değiştirebilir veya çizginin ağırlığını ve stilini belirleyebilirsiniz.

Aşağıdaki örnek, bir satıra ok ucunun nasıl ekleneceğini gösterir. Kod yürütülürken aşağıdaki çıktı oluşturulur.

**Çalışma sayfasına ok başlı bir satır eklenir** 

![yapılacaklar:resim_alternatif_Metin](managing-controls_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddinganArrowHead.java" >}}

## **Çalışma Sayfasına Dikdörtgen Denetimi Ekleme**

Aspose.Cells, çalışma sayfalarınıza dikdörtgen şekiller çizmenizi sağlar. Dikdörtgen, kare vb. oluşturabilirsiniz. Ayrıca kontrolün dolgu rengini ve kenar çizgisi rengini biçimlendirmenize izin verilir. Örneğin dikdörtgenin rengini değiştirebilir, gölgelendirme rengini ayarlayabilir, dikdörtgenin ağırlığını ve stilini ihtiyacınıza göre belirleyebilirsiniz.

### **Microsoft Excel'i kullanma**

1.  Üzerinde**Resim çizme** araç çubuğu, tıklayın**Dikdörtgen**.
1. Dikdörtgeni çizmek için sürükleyin.
1. Aşağıdakilerden birini veya her ikisini yapın:
 1. Dikdörtgeni başlangıç noktasından kare çizmeye zorlamak için sürüklerken SHIFT tuşunu basılı tutun.
 1. Merkez noktadan bir dikdörtgen çizmek için sürüklerken CTRL tuşunu basılı tutun.

### **Aspose.Cells'i kullanma**

 bu[**Şekil Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) class, çalışma sayfasına bir dikdörtgen şekli eklemek için kullanılan addShape adlı bir yöntem sağlar. Yöntem bir RectangleShape nesnesi döndürebilir. RectangleShape sınıfı bir dikdörtgeni temsil eder. Bazı önemli üyeleri vardır:

- setLineFormat yöntemi, bir dikdörtgenin çizgi biçimi özniteliklerini belirtir.
- setPlacement yöntemi, dikdörtgenin çalışma sayfasındaki hücrelere eklenme biçimi olan PlacementType'ı belirtir.
- FillFormat özelliği, bir dikdörtgenin dolgu biçimi stillerini belirtir.

Aşağıdaki örnek, çalışma sayfasına bir dikdörtgenin nasıl ekleneceğini gösterir. Kod yürütülürken aşağıdaki çıktı oluşturulur.

**Çalışma sayfasına bir dikdörtgen eklenir** 

![yapılacaklar:resim_alternatif_Metin](managing-controls_10.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingRectangleControl-1.java" >}}

## **Çalışma Sayfasına Yay Kontrolü Ekleme**

Aspose.Cells, çalışma sayfalarınıza yay şekilleri çizmenizi sağlar. Basit ve dolgun yaylar oluşturabilirsiniz. Kontrolün dolgu rengini ve kenar çizgisi rengini biçimlendirmenize izin verilir. Örneğin, yayın rengini belirleyebilir / değiştirebilir, gölgeleme rengini ayarlayabilir, şeklin ağırlığını ve stilini ihtiyacınıza göre belirleyebilirsiniz.

### **Microsoft Excel'i kullanma**

1.  Üzerinde**Resim çizme** araç çubuğu, tıklayın**ark** içinde**Otomatik Şekiller**.
1. Yayı çizmek için sürükleyin.

### **Aspose.Cells'i kullanma**

 bu[**Şekil Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) class, çalışma sayfasına bir yay şekli eklemek için kullanılan addShape adlı bir yöntem sağlar. Yöntem bir ArcShape nesnesi döndürebilir. ArcShape sınıfı bir yayı temsil eder. Bazı önemli üyeleri vardır:

- setLineFormat yöntemi, bir yay şeklinin çizgi formatı niteliklerini belirtir.
- setPlacement yöntemi, yayın çalışma sayfasındaki hücrelere eklenme biçimi olan PlacementType'ı belirtir.
- FillFormat özelliği, şeklin dolgu biçimi stillerini belirtir.

Aşağıdaki örnek, çalışma sayfasına yay şekillerinin nasıl ekleneceğini gösterir. Örnek iki yay şekli oluşturur: biri dolu, diğeri basit. Kod yürütülürken aşağıdaki çıktı üretilir

**Çalışma sayfasına iki yay şekli eklenir** 

![yapılacaklar:resim_alternatif_Metin](managing-controls_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingArcControl-1.java" >}}

## **Çalışma Sayfasına Oval Kontrol Ekleme**

Aspose.Cells, çalışma sayfalarında oval şekiller çizmenizi sağlar. Basit ve doldurulmuş oval şekiller oluşturun ve kontrolün dolgu rengini ve kenar çizgisi rengini biçimlendirin. Örneğin ovalin rengini belirleyebilir / değiştirebilir, gölgeleme rengini ayarlayabilir, şeklin ağırlığını ve stilini belirleyebilirsiniz.

### **Microsoft Excel'i kullanma**

1.  Üzerinde**Resim çizme** araç çubuğu, tıklayın**Oval** .
1. Oval çizmek için sürükleyin.
1. Aşağıdakilerden birini veya her ikisini yapın:
 1. Ovali başlangıç noktasından bir daire çizmeye zorlamak için sürüklerken SHIFT tuşunu basılı tutun.
1. Bir merkez noktadan oval çizmek için sürüklerken CTRL tuşunu basılı tutun.

### **Aspose.Cells'i kullanma**

 bu[**Şekil Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) class, çalışma sayfasına oval bir şekil eklemek için kullanılan addShape adlı bir yöntem sağlar. Yöntem bir Oval nesnesi döndürebilir. Oval sınıfı, oval bir şekli temsil eder. Bazı önemli üyeleri vardır:

- setLineFormat yöntemi, bir oval şeklin çizgi formatı niteliklerini belirtir.
-  setPlacement yöntemi şunu belirtir:**Yerleşim Türü** , ovalin çalışma sayfasındaki hücrelere bağlanma biçimi.
- FillFormat özelliği, şeklin dolgu biçimi stillerini belirtir.

Aşağıdaki örnek, çalışma sayfasına oval şekillerin nasıl ekleneceğini gösterir. Örnek iki oval şekil oluşturur: biri dolu oval, diğeri basit bir dairedir. Kod yürütülürken aşağıdaki çıktı oluşturulur.

**Çalışma sayfasına iki oval şekil eklendi** 

![yapılacaklar:resim_alternatif_Metin](managing-controls_12.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddinganOvalControl-1.java" >}}

## **ileri konular**
- [Aspose.Cells'i kullanarak ActiveX Denetimleri ekleyin](/cells/tr/java/add-activex-controls-using-aspose-cells/)
- [ActiveX Denetimini Kaldır](/cells/tr/java/remove-activex-control/)
