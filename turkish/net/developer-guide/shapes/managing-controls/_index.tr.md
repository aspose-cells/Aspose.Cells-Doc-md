---
title: Kontrolleri Yönetme
type: docs
weight: 150
url: /tr/net/managing-controls/
---
## **Giriş**

Geliştiriciler, metin kutuları, onay kutuları, radyo düğmeleri, açılan kutular, etiketler, düğmeler, çizgiler, dikdörtgenler, yaylar, ovaller, döndürücüler, kaydırma çubukları, grup kutuları vb. gibi farklı çizim nesneleri ekleyebilir. tüm çizim nesneleri. Ancak, henüz desteklenmeyen birkaç çizim nesnesi veya şekli vardır. Bu çizim nesnelerini Microsoft Excel kullanarak bir tasarımcı elektronik tablosunda oluşturun ve ardından tasarımcı elektronik tablosunu Aspose.Cells'e aktarın. Aspose.Cells, bu çizim nesnelerini bir tasarımcı elektronik tablosundan yüklemenize ve oluşturulmuş bir dosyaya yazmanıza olanak tanır.

## **Çalışma Sayfasına Metin Kutusu Denetimi Ekleme**

 Bir rapordaki önemli bilgileri vurgulamanın bir yolu, bir metin kutusu kullanmaktır. Örneğin, şirket adını vurgulamak veya en çok satış yapılan coğrafi bölgeyi vb. belirtmek için metin ekleyin. Aspose.Cells,[**Metin Kutusu Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textboxcollection) sınıf, koleksiyona yeni bir metin kutusu eklemek için kullanılır. Başka bir sınıf var,[**Metin kutusu**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox)tüm ayar türlerini tanımlamak için kullanılan bir metin kutusunu temsil eder. Bazı önemli üyeleri vardır:

-  bu[**Metin Çerçevesi**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textframe) özellik bir döndürür[**MsoTextÇerçevesi**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msotextframe) metin kutusunun içeriğini ayarlamak için kullanılan nesne.
-  bu[**Atama**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) özellik yerleşim tipini belirtir.
-  bu[**Yazı tipi**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/font) özelliği yazı tipi özniteliklerini belirtir.
-  bu[**Köprü Ekle**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/addhyperlink) yöntem, metin kutusu için bir köprü ekler.
-  bu[**Doldurma Biçimi**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) özellik bir döndürür[**MsoFillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msofillformat) metin kutusu için dolgu formatını ayarlamak için kullanılan nesne.
-  bu[**Çizgi Biçimi**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) özellik döndürür[**MsoLineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msolineformat) genellikle metin kutusu satırının stilini ve ağırlığını belirlemek için kullanılan nesne.
-  bu[**Metin**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) özelliği, metin kutusu için giriş metnini belirtir.

Aşağıdaki örnek, çalışma kitabının ilk çalışma sayfasında iki metin kutusu oluşturur. İlk metin kutusu, farklı biçim ayarlarıyla iyi bir şekilde döşenmiştir. İkincisi basit bir tanesidir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingTextBoxControl-1.cs" >}}

## **Tasarımcı Elektronik Tablolarında Metin Kutusu Kontrollerini Değiştirme**

 Aspose.Cells ayrıca tasarımcı çalışma sayfalarındaki metin kutularına erişmenizi ve bunları değiştirmenizi sağlar. Kullan[**Worksheet.TextBoxes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/textboxes) sayfadaki metin kutuları koleksiyonunu alma özelliği.

Aşağıdaki örnek, yukarıdaki örnekte oluşturduğumuz Microsoft Excel dosyasını kullanır. İki metin kutusunun metin dizelerini alır ve dosyayı kaydetmek için ikinci metin kutusunun metnini değiştirir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-ManipulatingTextBoxControls-1.cs" >}}

## **Çalışma Sayfasına Onay Kutusu Denetimi Ekleme**

Bir kullanıcıya doğru veya yanlış gibi iki seçenek arasında seçim yapması için bir yol sağlamak istiyorsanız, onay kutuları kullanışlıdır; Evet veya Hayır. Aspose.Cells, çalışma sayfalarında onay kutularını kullanmanıza izin verir. Örneğin, belirli bir satın almayı açıklayabileceğiniz ya da açıklamayabileceğiniz bir finansal projeksiyon çalışma sayfası geliştirmiş olabilirsiniz. Bu durumda, çalışma sayfasının en üstüne bir onay kutusu yerleştirmek isteyebilirsiniz. Daha sonra bu onay kutusunun durumunu başka bir hücreye bağlayabilirsiniz, böylece onay kutusu seçilirse hücrenin değeri True olur; seçili değilse hücrenin değeri False olur.

### **Microsoft Excel'i kullanma**

Çalışma sayfanıza bir onay kutusu denetimi yerleştirmek için şu adımları izleyin:

1. Formlar araç çubuğunun görüntülendiğinden emin olun.
1.  Tıkla**Onay Kutusu** Formlar araç çubuğundaki aracı.
1. Çalışma sayfası alanınızda, onay kutusunu ve onay kutusunun yanındaki etiketi tutacak dikdörtgeni tanımlamak için tıklayın ve sürükleyin.
1. Onay kutusu yerleştirildikten sonra, fare imlecini etiket alanına getirin ve etiketi değiştirin.
1.  İçinde**Cell Bağlantı**alanında, bu onay kutusunun bağlanması gereken hücrenin adresini belirtin.
1.  Tıklamak**Tamam**.

### **Aspose.Cells'i kullanma**

 Aspose.Cells şunları sağlar:[**Onay Kutusu Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkboxcollection) koleksiyona yeni bir onay kutusu eklemek için kullanılan sınıf. Başka bir sınıf var,[**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkbox), bir onay kutusunu temsil eder. Bazı önemli üyeleri vardır:

-  bu[**Bağlantılı Hücre**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) özelliği, onay kutusuna bağlı bir hücreyi belirtir.
-  bu[**Metin**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) özelliği, onay kutusuyla ilişkili metin dizesini belirtir. Onay kutusunun etiketidir.
-  bu[**Değer**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkbox/properties/value) özellik, onay kutusunun işaretlenip işaretlenmediğini belirtir.

Aşağıdaki örnek, çalışma sayfasına bir onay kutusunun nasıl ekleneceğini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingCheckBoxControl-1.cs" >}}

## **Çalışma Sayfasına Radyo Düğmesi Denetimi Ekleme**

Bir radyo düğmesi veya bir seçenek düğmesi, yuvarlak bir kutudan yapılmış bir kontroldür. Kullanıcı yuvarlak kutuyu seçerek kararını verir. Bir radyo düğmesine, her zaman olmasa da genellikle başkaları eşlik eder. Bu tür radyo düğmeleri bir grup olarak görünür ve davranır. Kullanıcı bunlardan sadece birini seçerek hangi butonun geçerli olduğuna karar verir. Kullanıcı bir düğmeyi tıkladığında, doldurulur. Gruptaki bir düğme seçildiğinde, aynı grubun düğmeleri boştur.

### **Microsoft Excel'i kullanma**

Çalışma sayfanıza bir Radyo Düğmesi denetimi yerleştirmek için şu adımları izleyin:

1.  Emin ol**Formlar** araç çubuğu görüntülenir.
1.  Tıkla**Seçenek tuşu** alet.
1. Çalışma sayfasında, seçenek düğmesini ve seçenek düğmesinin yanındaki etiketi tutacak dikdörtgeni tanımlamak için tıklayın ve sürükleyin.
1. Radyo düğmesi çalışma sayfasına yerleştirildikten sonra, fare imlecini etiket alanına getirin ve etiketi değiştirin.
1.  İçinde**Cell Bağlantı** alanında, bu radyo düğmesinin bağlanması gereken hücrenin adresini belirtin.
1.  Tıklamak**Tamam**.

### **Aspose.Cells'i kullanma**

[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) sınıf adlı bir yöntem sağlar[**RadyoDüğmesi Ekle**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addradiobutton) , bir çalışma sayfasına bir radyo düğmesi denetimi eklemek için kullanılır. Yöntem bir döndürür[**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton) nesne. Sınıf[**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton) bir seçenek düğmesini temsil eder. Bazı önemli üyeleri vardır:

-  bu[**Bağlantılı Hücre**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) özelliği, radyo düğmesine bağlı bir hücreyi belirtir.
-  bu[**Metin**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)özelliği, radyo düğmesiyle ilişkili metin dizesini belirtir. Radyo düğmesinin etiketidir.
-  bu[**kontrol edildi**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton/properties/ischecked) özellik, radyo düğmesinin işaretlenip işaretlenmediğini belirtir.
-  bu[**Doldurma Biçimi**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) özelliği, radyo düğmesinin doldurma biçimini belirtir.
-  bu[**Çizgi Biçimi**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) özelliği, seçenek düğmesinin çizgi biçimi stillerini belirtir.

Aşağıdaki örnek, bir çalışma sayfasına radyo düğmelerinin nasıl ekleneceğini gösterir. Örnek, yaş gruplarını temsil eden üç radyo düğmesi ekler.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingRadioButtonControl-1.cs" >}}

## **Çalışma Sayfasına Birleşik Giriş Kutusu Denetimi Ekleme**

Veri girişini kolaylaştırmak veya girişleri tanımladığınız belirli öğelerle sınırlamak için, çalışma sayfasının herhangi bir yerindeki hücrelerden derlenen geçerli girişlerin açılır listesini veya birleşik giriş kutusunu oluşturabilirsiniz. Bir hücre için açılır liste oluşturduğunuzda, o hücrenin yanında bir ok görüntülenir. Bu hücreye bilgi girmek için oku tıklatın ve ardından istediğiniz girişi tıklatın.

### **Microsoft Excel'i kullanma**

Çalışma sayfanıza birleşik giriş kutusu denetimi yerleştirmek için şu adımları izleyin:

1.  Emin ol**Formlar** araç çubuğu görüntülenir.
1.  Tıkla**Açılan kutu** alet.
1. Çalışma sayfası alanınızda, birleşik giriş kutusunu tutacak dikdörtgeni tanımlamak için tıklayın ve sürükleyin.
1.  Birleşik giriş kutusu çalışma sayfasına yerleştirildikten sonra, kontrolü sağ tıklatarak**Biçim Kontrolü** ve giriş aralığını belirtin.
1.  İçinde**Cell Bağlantı** alanında, bu açılan kutunun bağlanması gereken hücrenin adresini belirtin.
1.  Tıklamak**Tamam**.

### **Aspose.Cells'i kullanma**

 bu[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) sınıf adlı bir yöntem sağlar[**ComboBox Ekle**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcombobox) , bir çalışma sayfasına birleşik giriş kutusu denetimi eklemek için kullanılır. Yöntem bir döndürür[**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox) nesne. Sınıf[**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox) açılan kutuyu temsil eder. Bazı önemli üyeleri vardır:

-  bu[**Bağlantılı Hücre**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) özelliği, birleşik giriş kutusuna bağlı bir hücreyi belirtir.
-  bu[**Giriş aralığı**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/inputrange) özelliği, açılan kutuyu doldurmak için kullanılan çalışma sayfası hücre aralığını belirtir.
-  bu[**DropDownLines**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox/properties/dropdownlines) özelliği, birleşik giriş kutusunun açılır bölümünde görüntülenen liste satırlarının sayısını belirtir.
-  bu[**Gölge**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox/properties/shadow) özelliği, birleşik giriş kutusunun 3B gölgelendirmeye sahip olup olmadığını gösterir.

Aşağıdaki örnek, çalışma sayfasına birleşik giriş kutusunun nasıl ekleneceğini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingComboBoxControl-1.cs" >}}

## **Çalışma Sayfasına Etiket Denetimi Ekleme**

 Etiketler, kullanıcılara elektronik tablonun içeriği hakkında bilgi vermenin bir yoludur. Aspose.Cells, bir çalışma sayfasına etiket eklemeyi ve düzenlemeyi mümkün kılar. bu[**Şekil Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) sınıf adlı bir yöntem sağlar[**Etiket Ekle**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabel) , çalışma sayfasına bir etiket denetimi eklemek için kullanılır. Yöntem bir döndürür[**Etiket**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) nesne. Sınıf[**Etiket**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) çalışma sayfasındaki bir etiketi temsil eder. Bazı önemli üyeleri vardır:

-  bu[**Metin**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) yöntem, bir etiketin başlık dizesini belirtir.
-  bu[**Atama**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) yöntemi belirtir[**Yerleşim Türü**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), etiketin çalışma sayfasındaki hücrelere eklenme şekli.

Aşağıdaki örnek, çalışma sayfasına nasıl etiket ekleneceğini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingLabelControl-1.cs" >}}

## **Bir Çalışma Sayfasına Liste Kutusu Denetimi Ekleme**

Liste kutusu denetimi, tekli veya çoklu öğe seçimine izin veren bir liste denetimi oluşturur.

### **Microsoft Excel'i kullanma**

Çalışma sayfasına bir liste kutusu denetimi yerleştirmek için:

1.  Emin ol**Formlar** araç çubuğu görüntülenir.
1.  Tıkla**Liste kutusu** alet.
1. Çalışma sayfası alanınızda, liste kutusunu tutacak dikdörtgeni tanımlamak için tıklayın ve sürükleyin.
1.  Liste kutusu çalışma sayfasına yerleştirildikten sonra, kontrole sağ tıklayın.**Biçim Kontrolü** ve giriş aralığını belirtin.
1.  İçinde**Cell Bağlantı**alanında, bu liste kutusunun bağlanması gereken hücrenin adresini belirtin ve seçim tipi (Tek, Çoklu, Genişlet) özniteliğini ayarlayın.
1.  Tıklamak**Tamam**.

### **Aspose.Cells'i kullanma**

 bu[**Şekil Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) sınıf adlı bir yöntem sağlar[**Liste Kutusu Ekle**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlistbox) , bir çalışma sayfasına bir liste kutusu denetimi eklemek için kullanılır. Yöntem bir döndürür[**Aspose.Cells.Drawing.ListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox) nesne. Sınıf[**Liste kutusu**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox) bir liste kutusunu temsil eder. Bazı önemli üyeleri vardır:

-  bu[**Bağlantılı Hücre**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) yöntem, liste kutusuna bağlı bir hücreyi belirtir.
-  bu[**Giriş aralığı**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/inputrange) yöntem, liste kutusunu doldurmak için kullanılan çalışma sayfası hücre aralığını belirtir.
-  bu[**Seçim Türü**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox/properties/selectiontype)method, liste kutusunun seçim kipini belirtir.
-  bu[**Gölge**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox/properties/shadow) yöntemi, liste kutusunun 3B gölgelendirmeye sahip olup olmadığını gösterir.

Aşağıdaki örnek, çalışma sayfasına bir liste kutusunun nasıl ekleneceğini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingListBoxControl-1.cs" >}}

## **Bir Çalışma Sayfasına Düğme Denetimi Ekleme**

Düğmeler, bazı eylemleri gerçekleştirmek için kullanışlıdır. Bazen, bir web sayfasını açmak için düğmeye bir VBA Makrosu atamak veya bir köprü atamak yararlı olabilir.

### **Microsoft Excel'i kullanma**

Çalışma sayfanıza bir düğme denetimi yerleştirmek için:

1.  Emin ol**Formlar** araç çubuğu görüntülenir.
1.  Tıkla**Buton** alet.
1. Çalışma sayfası alanınızda, düğmeyi tutacak dikdörtgeni tanımlamak için tıklayın ve sürükleyin.
1.  Liste kutusu çalışma sayfasına yerleştirildikten sonra, kontrole sağ tıklayın ve seçin.**Biçim Kontrolü**, ardından bir VBA Makrosu ve yazı tipi, hizalama, boyut, kenar boşluğu vb. ile ilgili öznitelikleri belirtin.
1.  Tıklamak**Tamam**.

### **Aspose.Cells'i kullanma**

 bu[**Şekil Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) sınıf adlı bir yöntem sağlar[**EkleDüğmesi**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addbutton) , çalışma sayfasına bir düğme denetimi eklemek için kullanılır. Yöntem bir döndürür[**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/net/aspose.cells.drawing/button) nesne. Sınıf[**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/net/aspose.cells.drawing/button) bir düğmeyi temsil eder. Bazı önemli üyeleri vardır:

-  bu[**Metin**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) özellik, düğmenin başlığını belirtir.
-  bu[**Yazı tipi**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/font) özelliği, düğme denetiminin etiketi için yazı tipi niteliklerini belirtir.
-  bu[**Atama**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) özelliği belirtir[**Yerleşim Türü**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), düğmenin çalışma sayfasındaki hücrelere eklenme şekli.
-  bu[**Köprü Ekle**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/addhyperlink) özelliği, düğme denetimi için bir köprü ekler. Düğmeye tıklandığında ilgili URL'ye gidilecektir.

Aşağıdaki örnek, çalışma sayfasına nasıl düğme ekleneceğini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingButtonControl-1.cs" >}}

## **Çalışma Sayfasına Hat Kontrolü Ekleme**

### **Microsoft Excel'i kullanma**

1.  Üzerinde**Çizim** araç çubuğu, tıklayın**Otomatik Şekiller** , odaklan**çizgiler**ve istediğiniz çizgi stilini seçin.
1. Çizgiyi çizmek için sürükleyin.
1. Aşağıdakilerden birini veya her ikisini yapın:
 1. Çizgiyi başlangıç noktasından 15 derecelik açılarla çizmek üzere sınırlamak için sürüklerken SHIFT tuşunu basılı tutun.
 1. Çizgiyi ilk bitiş noktasından zıt yönlerde uzatmak için sürüklerken CTRL tuşunu basılı tutun.

### **Aspose.Cells'i kullanma**

 bu[**Şekil Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) sınıf adlı bir yöntem sağlar[**Ek Satır**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline) , çalışma sayfasına bir çizgi şekli eklemek için kullanılır. Yöntem bir döndürür[**Çizgi Şekli**](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) nesne. Sınıf[**Çizgi Şekli**](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) bir çizgiyi temsil eder. Bazı önemli üyeleri vardır:

-  bu[**Çizgi Biçimi**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) method bir satırın biçimini belirtir.
-  bu[**Atama**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) yöntemi belirtir[**Yerleşim Türü**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)çizginin çalışma sayfasındaki hücrelere eklenme şekli.

Aşağıdaki örnek, çalışma sayfasına nasıl satır ekleneceğini gösterir. Farklı stillerde üç çizgi oluşturur.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingLineControl-1.cs" >}}

### **Bir Çizgiye Ok Başı Ekleme**

Aspose.Cells ayrıca ok çizgileri çizmenize de olanak tanır. Bir satıra ok ucu eklemek ve satırı biçimlendirmek mümkündür. Örneğin, çizginin rengini değiştirebilir veya çizginin ağırlığını ve stilini belirleyebilirsiniz.

Aşağıdaki örnek, bir satıra ok ucunun nasıl ekleneceğini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddinganArrowHead-1.cs" >}}

## **Çalışma Sayfasına Dikdörtgen Denetimi Ekleme**

Aspose.Cells, çalışma sayfalarınıza dikdörtgen şekiller çizmenizi sağlar. Dikdörtgen, kare vb. oluşturabilirsiniz. Ayrıca kontrolün dolgu rengini ve kenar çizgisi rengini biçimlendirmenize izin verilir. Örneğin dikdörtgenin rengini değiştirebilir, gölgelendirme rengini ayarlayabilir, dikdörtgenin ağırlığını ve stilini ihtiyacınıza göre belirleyebilirsiniz.

### **Microsoft Excel'i kullanma**

1.  Üzerinde**Çizim** araç çubuğu, tıklayın**Dikdörtgen**.
1. Dikdörtgeni çizmek için sürükleyin.
1. Aşağıdakilerden birini veya her ikisini yapın:
 1. Dikdörtgeni başlangıç noktasından kare çizmeye zorlamak için sürüklerken SHIFT tuşunu basılı tutun.
 1. Merkez noktadan bir dikdörtgen çizmek için sürüklerken CTRL tuşunu basılı tutun.

### **Aspose.Cells'i kullanma**

 bu[**Şekil Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) sınıf adlı bir yöntem sağlar[**Dikdörtgen Ekle**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle) , çalışma sayfasına bir dikdörtgen şekli eklemek için kullanılır. Yöntem döndürür[**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) nesne. Sınıf[**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) bir dikdörtgeni temsil eder. Bazı önemli üyeleri vardır:

-  bu[**Çizgi Biçimi**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) özelliği, bir dikdörtgenin çizgi biçimi özniteliklerini belirtir.
-  bu[**Atama**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) özelliği belirtir[**Yerleşim Türü**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), dikdörtgenin çalışma sayfasındaki hücrelere eklenme şekli.
-  bu[**Doldurma Biçimi**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) özelliği, bir dikdörtgenin dolgu biçimi stillerini belirtir.

Aşağıdaki örnek, çalışma sayfasına bir dikdörtgenin nasıl ekleneceğini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingRectangleControl-1.cs" >}}

## **Çalışma Sayfasına Yay Kontrolü Ekleme**

Aspose.Cells, çalışma sayfalarınıza yay şekilleri çizmenizi sağlar. Basit ve dolgun yaylar oluşturabilirsiniz. Kontrolün dolgu rengini ve kenar çizgisi rengini biçimlendirmenize izin verilir. Örneğin, yayın rengini belirleyebilir / değiştirebilir, gölgeleme rengini ayarlayabilir, şeklin ağırlığını ve stilini ihtiyacınıza göre belirleyebilirsiniz.

### **Microsoft Excel'i kullanma**

1.  Üzerinde**Çizim** araç çubuğu, tıklayın**ark** içinde**Otomatik Şekiller**.
1. Yayı çizmek için sürükleyin.

### **Aspose.Cells'i kullanma**

 bu[**Şekil Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) sınıf adlı bir yöntem sağlar[**EklemeArc**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addarc) , bir çalışma sayfasına bir yay şekli eklemek için kullanılır. Yöntem bir döndürür[**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/arcshape) nesne. Sınıf[**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/arcshape) bir yayı temsil eder. Bazı önemli üyeleri vardır:

-  bu[**Çizgi Biçimi**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) özelliği, bir yay şeklinin çizgi formatı niteliklerini belirtir.
-  bu[**Atama**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) özelliği belirtir[**Yerleşim Türü**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), yayın çalışma sayfasındaki hücrelere iliştirilme şekli.
-  bu[**Doldurma Biçimi**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat)özelliği, şeklin dolgu biçimi stillerini belirtir.
-  bu[**AltSağSatır**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightrow) özelliği, sağ alt köşe satır dizinini belirtir.
-  bu[**AltSağSütun**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightcolumn) özelliği, sağ alt köşedeki sütun dizinini belirtir.

Aşağıdaki örnek, çalışma sayfasına yay şekillerinin nasıl ekleneceğini gösterir. Örnek iki yay şekli oluşturur: biri dolu, diğeri basit.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingArcControl-1.cs" >}}

## **Çalışma Sayfasına Oval Kontrol Ekleme**

Aspose.Cells, çalışma sayfalarında oval şekiller çizmenizi sağlar. Basit ve doldurulmuş oval şekiller oluşturun ve kontrolün dolgu rengini ve kenar çizgisi rengini biçimlendirin. Örneğin ovalin rengini belirleyebilir / değiştirebilir, gölgeleme rengini ayarlayabilir, şeklin ağırlığını ve stilini belirleyebilirsiniz.

### **Microsoft Excel'i kullanma**

-  Üzerinde*Çizim* araç çubuğu, tıklayın*Oval*.
- Oval çizmek için sürükleyin.
- Aşağıdakilerden birini veya her ikisini yapın:
- Ovali başlangıç noktasından bir daire çizmeye zorlamak için sürüklerken SHIFT tuşunu basılı tutun.
- Bir merkez noktadan oval çizmek için sürüklerken CTRL tuşunu basılı tutun.

### **Aspose.Cells'i kullanma**

 bu[**Şekil Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) sınıf adlı bir yöntem sağlar[**Oval Ekle**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addoval) , çalışma sayfasına oval bir şekil eklemek için kullanılır. Yöntem bir döndürür[**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oval) nesne. Sınıf[**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oval) oval bir şekli temsil eder. Bazı önemli üyeleri vardır:

-  bu[**Çizgi Biçimi**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) özelliği, bir oval şeklin çizgi formatı niteliklerini belirtir.
-  bu[**Atama**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) özelliği belirtir[**Yerleşim Türü**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), ovalin çalışma sayfasındaki hücrelere bağlanma biçimi.
-  bu[**Doldurma Biçimi**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat)özelliği, şeklin dolgu biçimi stillerini belirtir.
-  bu[**AltSağSatır**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightrow) özelliği, sağ alt köşe satır dizinini belirtir.
-  bu[**AltSağSütun**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightcolumn) özelliği, sağ alt köşedeki sütun dizinini belirtir.

Aşağıdaki örnek, çalışma sayfasına oval şekillerin nasıl ekleneceğini gösterir. Örnek iki oval şekil oluşturur: biri dolu oval, diğeri basit bir dairedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingOvalControl-1.cs" >}}

## **Çalışma Sayfasına Döndürücü Denetimi Ekleme**

 Döndürme kutusu, metin kutusundaki değeri artımlı olarak değiştirmek için tıkladığınız yukarı ve aşağı oklardan oluşan bir düğmeye (döndürme düğmesi adı verilir) iliştirilmiş bir metin kutusudur. Döndürme kutularını kullanarak, finansal modelinizdeki girdi değişikliklerinin model çıktılarını nasıl değiştireceğini görebilirsiniz. Belirli bir giriş hücresine bir döndürme düğmesi ekleyebilirsiniz. Döndür düğmesinde yukarı veya aşağı oku tıklattığınızda, hedeflenen giriş hücresindeki tamsayı değeri artar veya azalır.*Aspose.Cells* çalışma sayfalarınızda iplikçiler oluşturmanıza olanak tanır.

### **Microsoft Excel'i kullanma**

Çalışma sayfanıza bir döndürme kutusu denetimi yerleştirmek için:

-  Emin ol*Formlar* araç çubuğu görüntülenir.
-  Tıkla*Döndürücü* alet.
- Çalışma sayfası alanınızda, döndürücüyü tutacak dikdörtgeni tanımlamak için tıklayın ve sürükleyin.
-  Döndürücü çalışma sayfasına yerleştirildikten sonra, kontrolü sağ tıklayın ve tıklayın.*Biçim Kontrolü* ve maksimum, minimum ve artımlı değerleri belirtin.
-  İçinde*Cell Bağlantı* alanında, bu döndürme kutusunun bağlanması gereken hücrenin adresini belirtin.
-  Tıklamak*Tamam*.

### **Aspose.Cells'i kullanma**

 bu[**Şekil Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) sınıf adlı bir yöntem sağlar[**EkleSpinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addspinner) bir çalışma sayfasına bir döndürme kutusu denetimi eklemek için kullanılır. Yöntem bir döndürür[**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner) nesne. Sınıf[**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner) bir döndürme kutusunu temsil eder. Bazı önemli üyeleri vardır:

-  bu[**Bağlantılı Hücre**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) özelliği, döndürme kutusuna bağlı bir hücreyi belirtir.
-  bu[**maks.**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/max) özelliği, döndürme kutusu aralığı için maksimum değeri belirtir.
-  bu[**dak.**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/min) özelliği, döndürme kutusu aralığı için minimum değeri belirtir.
-  bu[**ArtımlıDeğişim**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/incrementalchange) özelliği, bir döndürücünün bir satır kaydırmayla artırıldığı değer miktarını belirtir.
-  bu[**Gölge**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/shadow) özelliği, döndürme kutusunun 3B gölgelendirmeye sahip olup olmadığını gösterir.
-  bu[**Mevcut değer**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/currentvalue) özelliği, döndürme kutusunun geçerli değerini belirtir.

Aşağıdaki örnek, çalışma sayfasına bir döndürme kutusunun nasıl ekleneceğini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingSpinnerControl-1.cs" >}}

## **Çalışma Sayfasına Kaydırma Çubuğu Denetimi Ekleme**

Döndürme kutusu denetimine benzer şekilde çalışma sayfasındaki verileri seçmeye yardımcı olmak için bir kaydırma çubuğu denetimi kullanılır. Denetimi bir çalışma sayfasına ekleyerek ve onu bir hücreye bağlayarak, denetimin geçerli konumu için sayısal bir değer döndürmek mümkündür.

### **Microsoft Excel'i kullanma**

- Excel 2003 ve önceki sürümlerde kaydırma çubuğu eklemek için*Kaydırma çubuğu* üzerindeki düğme*Formlar* araç çubuğu ve ardından B2:B6 hücrelerini kaplayan ve yüksekliği sütunun genişliğinin dörtte biri kadar olan bir kaydırma çubuğu oluşturun.
-  Excel 2007'de kaydırma çubuğu eklemek için*Geliştirici* sekme, tıklayın*Sokmak* ve ardından tıklayın*Kaydırma çubuğu* Form Kontrolleri bölümünde.
-  Kaydırma çubuğuna sağ tıklayın ve ardından*Biçim Kontrolü*.
-  Aşağıdaki bilgileri yazın ve tıklayın*Tamam*:
 - İçinde*Mevcut değer* kutu, tip 1.
 - İçinde*En az değer* kutusuna 1 yazın. Bu değer, kaydırma çubuğunun üst kısmını listedeki ilk öğeyle sınırlar.
 - İçinde*Maksimum değer* kutusuna 20 yazın. Bu sayı, listedeki maksimum giriş sayısını belirtir.
 - İçinde*artımlı değişiklik* kutusuna 1 yazın. Bu değer, kaydırma çubuğu kontrolünün geçerli değeri kaç sayı artıracağını kontrol eder.
 - İçinde*sayfa değişikliği* kutusuna 5 yazın. Bu giriş, kaydırma kutusunun her iki tarafındaki kaydırma çubuğunun içini tıklatırsanız geçerli değerin ne kadar artırılacağını kontrol eder.
 G1 hücresine bir sayı değeri koymak için (listede hangi öğenin seçili olduğuna bağlı olarak), hücreye G1 yazın.*Cell bağlantı* Kutu.
- Kaydırma çubuğunun seçili olmaması için herhangi bir hücreye tıklayın.

Kaydırma çubuğundaki yukarı veya aşağı kontrolünü tıklattığınızda, G1 hücresi, kaydırma çubuğunun geçerli değeri artı veya eksi kaydırma çubuğunun artımlı değişimini gösteren bir sayıya güncellenir.

### **Aspose.Cells'i kullanma**

 bu[**Şekil Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) sınıf adlı bir yöntem sağlar[**Kaydırma Çubuğu Ekle**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addscrollbar) , çalışma sayfasına bir kaydırma çubuğu denetimi eklemek için kullanılır. Yöntem bir döndürür[**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar) nesne. Sınıf[**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar) kaydırma çubuğunu temsil eder. Bazı önemli üyeleri vardır:

-  bu[**Bağlantılı Hücre**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) özelliği, kaydırma çubuğuna bağlı bir hücreyi belirtir.
-  bu[**maks.**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/max) özelliği, kaydırma çubuğu aralığı için maksimum değeri belirtir.
-  bu[**dak.**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/min) özelliği, kaydırma çubuğu aralığı için minimum değeri belirtir.
-  bu[**ArtımlıDeğişim**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/incrementalchange) özelliği, bir kaydırma çubuğunun bir satır kaydırmaya artırıldığı değer miktarını belirtir.
-  bu[**Gölge**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/shadow) özelliği, kaydırma çubuğunun 3B gölgelendirmeye sahip olup olmadığını gösterir.
-  bu[**Mevcut değer**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/currentvalue) özelliği, kaydırma çubuğunun geçerli değerini belirtir.
-  bu[**Sayfa Değişikliği**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/pagechange)özelliği, kaydırma kutusunun her iki tarafındaki kaydırma çubuğunun içini tıklatırsanız geçerli değerin ne kadar artırılacağını belirtir.

Aşağıdaki örnek, çalışma sayfasına nasıl kaydırma çubuğu ekleneceğini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingScrollBarControl-1.cs" >}}

## **Bir Çalışma Sayfasındaki Grup Kontrollerine GroupBox Kontrolü Ekleme**

Bazen belirli bir gruba ait olan radyo düğmelerini veya diğer kontrolleri uygulamanız gerekir, bir grup kutusu veya dikdörtgen kontrol ekleyerek uygulayabilirsiniz. Bu iki nesneden herhangi biri, grubun sınırlayıcısı olarak işlev görür. Bu şekillerden birini ekledikten sonra, iki veya daha fazla radyo düğmesi veya başka grup nesneleri ekleyebilirsiniz.

### **Microsoft Excel'i kullanma**

Çalışma sayfanıza bir grup kutusu denetimi yerleştirmek ve içine denetimler yerleştirmek için:

-  Bir formu başlatmak için ana menüde simgesine tıklayın.*görüş* , bunu takiben*araç çubukları* ve*Formlar*.
-  Üzerinde*Formlar* araç çubuğunda*Grup Kutusu* ve çalışma sayfasına bir dikdörtgen çizin.
- Kutu için bir başlık dizesi yazın.
-  Üzerinde*Formlar* araç çubuğu, tıklayın*Seçenek tuşu* ve içine tıklayın*Grup Kutusu* başlık dizesinin hemen altında.
-  itibaren*Formlar* araç çubuğunda tekrar tıklayın*Seçenek tuşu* ve içine tıklayın*Grup Kutusu*ilk radyo düğmesinin altında.
-  üzerinde bir kez daha*Formlar* araç çubuğu, tıklayın*Seçenek tuşu* ve içine tıklayın*Grup Kutusu* önceki radyo düğmesinin altında.

### **Aspose.Cells'i kullanma**

 bu[**Şekil Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) sınıf adlı bir yöntem sağlar[**Grup Kutusu Ekle**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addgroupbox) , çalışma sayfasına bir grup kutusu denetimi eklemek için kullanılır. Yöntem bir döndürür[**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox) nesne. Ayrıca,[**Grup**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/group) yöntemi[**Şekil Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) sınıf şekilleri gruplandırır,[**Şekil**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) parametre olarak dizi ve bir döndürür[**Grup Şekli**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupshape) nesne. Sınıf[**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox) bir grup kutusunu temsil eder. Bazı önemli üyeleri vardır:

-  bu[**Metin**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) özelliği, grup kutusunun başlık dizesini belirtir.
-  bu[**Gölge**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox/properties/shadow) özelliği, grup kutusunun 3B gölgelendirmeye sahip olup olmadığını gösterir.

Aşağıdaki örnek, bir grup kutusunun nasıl ekleneceğini ve çalışma sayfasındaki denetimlerin nasıl gruplanacağını gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingGroupBoxControl-1.cs" >}}

## **ileri konular**
- [Aspose.Cells'i kullanarak ActiveX Denetimleri ekleyin](/cells/tr/net/add-activex-controls-using-aspose-cells/)
- [ActiveX Denetimini Kaldır](/cells/tr/net/remove-activex-control/)
- [ActiveX ComboBox Denetimini Güncelle](/cells/tr/net/update-activex-combobox-control/)
