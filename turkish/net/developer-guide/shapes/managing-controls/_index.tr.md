---
title: Kontrolleri Yönetme
type: docs
weight: 150
url: /tr/net/managing-controls/
---

## **Giriş**

Geliştiriciler metin kutuları, onay kutuları, radyo düğmeleri, açılır kutular, etiketler, düğmeler, çizgiler, dikdörtgenler, yarıçapları, ovaları, kaydırma çubuklarını, grup kutularını vb. gibi farklı çizim nesneleri ekleyebilir. Aspose.Cells, tüm çizim nesnelerini içeren Aspose.Cells.Drawing ad alanını sağlar. Ancak henüz desteklenmeyen bazı çizim nesneleri veya şekiller vardır. Bu çizim nesnelerini Microsoft Excel kullanarak bir tasarımcı çalışma sayfasında oluşturun ve ardından tasarımcı çalışma sayfasını Aspose.Cells'e aktarın. Aspose.Cells, bir tasarımcı çalışma sayfasından bu çizim nesnelerini yüklemenize ve bunları oluşturulan bir dosyaya yazmanıza olanak tanır.

## **Bir Çalışma Sayfasına Metin Kutusu Denetimi Ekleme**

Raporda önemli bilgileri vurgulamanın bir yolu metin kutusu kullanmaktır. Örneğin, şirket adını vurgulamak veya en yüksek satışı olan coğrafi bölgeyi belirtmek için metin ekleyebilirsiniz. Aspose.Cells, yeni bir metin kutusu eklemek için kullanılan [**TextBoxCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textboxcollection) sınıfını sağlar. Tüm türde ayarları tanımlamak için kullanılan başka bir sınıf olan [**TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox) vardır. Önemli üyeleri vardır:

- [**TextFrame**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textframe) özelliği, metin kutusunun içeriğini ayarlamak için kullanılan bir [**MsoTextFrame**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msotextframe) nesnesi döndürür.
- [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) özelliği yerleştirme türünü belirtir.
- [**Font**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/font) özelliği yazı tipi özelliklerini belirtir.
- [**AddHyperlink**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/addhyperlink) methodu, metin kutusu için bir bağlantıyı ekler.
- [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) özelliği, metin kutusunun dolgu biçimini ayarlamak için kullanılan bir [**MsoFillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msofillformat) nesnesini döndürür.
- [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) özelliği, metin kutusu çizgisi için stil ve kalınlık genellikle kullanılan bir [**MsoLineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msolineformat) nesnesi döndürür.
- [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) özelliği giriş metnini belirtir.

Aşağıdaki örnek, çalışma kitabının ilk çalışma sayfasında iki metin kutusu oluşturur. İlk metin kutusu farklı biçim ayarlarıyla donatılmıştır. İkincisi ise basit bir tanedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingTextBoxControl-1.cs" >}}

## **Tasarımcı Elektronik Tablolarda Metin Kutusu Denetimlerini Manipüle Etme**

Aspose.Cells, ayrıca tasarımcı elektronik tablolardaki metin kutularına erişmenizi ve bunları manipüle etmenizi sağlar. Levhada metin kutuları koleksiyonunu almak için [**Worksheet.TextBoxes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/textboxes) özelliğini kullanın.

Aşağıdaki örnek yukarıdaki örnekte oluşturduğumuz Microsoft Excel dosyasını kullanır. İki metin kutusunun metin dizelerini alır ve ikinci metin kutusunun metnini değiştirerek dosyayı kaydeder.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-ManipulatingTextBoxControls-1.cs" >}}

## **Bir Çalışma Sayfasına Onay Kutusu Denetimi Ekleme**

Onay kutuları, bir kullanıcının doğru veya yanlış gibi iki seçenek arasında seçim yapmasına olanak tanımak istiyorsanız kullanışlıdır. Örneğin, belirli bir edinimi hesaba katıp katmayacağını belirtmek istediğiniz bir finansal projeksiyon çalışma sayfası geliştirdiniz. Bu durumda, çalışma sayfasının üst kısmına bir onay kutusu yerleştirmek isteyebilirsiniz. Daha sonra bu onay kutusunun durumunu başka bir hücreye bağlayabilirsiniz; böylece onay kutusu seçiliyken, hücrenin değeri True olur; seçilmediğinde, hücrenin değeri False olur.

### **Microsoft Excel Kullanımı**

Çalışma sayfanıza bir onay kutusu denetimi yerleştirmek için şu adımları izleyin:

1. Formlar araç çubuğunun görüntülendiğinden emin olun.
1. Formlar araç çubuğunda **Onay Kutusu** aracını tıklayın.
1. Çalışma sayfanızda, onay kutusunu ve onay kutusunun yanındaki etiketi içerecek dikdörtgeni tanımlamak için tıklayın ve sürükleyin.
1. Onay kutusu yerleştirildikten sonra fare imleci etiket alanına kaydırın ve etiketi değiştirin.
1. **Hücre Bağlantısı** alanında, bu onay kutusunun bağlanması gereken hücrenin adresini belirtin.
1. **Tamam**'ı tıklayın.

### **Aspose.Cells Kullanımı**

Aspose.Cells, yeni bir onay kutusu eklemek için kullanılan [**CheckBoxCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkboxcollection) sınıfını sağlar. İşte onay kutusunu temsil eden başka bir sınıf olan [**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkbox). Önemli bazı üyelere sahiptir:

- [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) özelliği, onay kutusuna bağlı olan bir hücreyi belirtir.
- [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) özelliği, onay kutusu ile ilişkilendirilmiş metin dizisini belirtir. Bu, onay kutusunun etiketidir.
- [**Value**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkbox/properties/value) özelliği, onay kutusunun işaretli olup olmadığını belirtir.

Aşağıdaki örnek, bir çalışma sayfasına onay kutusu eklemenin nasıl yapıldığını göstermektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingCheckBoxControl-1.cs" >}}

## **Çalışma Sayfasına Radyo Düğmesi Denetimi Ekleme**

Radyo düğmesi veya seçenek düğmesi, yuvarlak bir kutudan oluşan bir denetimdir. Kullanıcı, yuvarlak kutuyu seçerek kararını verir. Radyo düğmesi genellikle, diğerleri ile birlikte olacak şekilde, eğer her zaman değilse eşlik eder. Bu tür radyo düğmeleri grup olarak görünür ve davranır. Kullanıcı, sadece birini seçerek hangi düğmenin geçerli olduğuna karar verir. Kullanıcı bir düğmeye tıkladığında doldurulur. Grubun içindeki bir düğme seçildiğinde, aynı gruba ait düğmeler boş olur.

### **Microsoft Excel Kullanımı**

Çalışma sayfanıza bir Radyo Düğmesi denetimi yerleştirmek için şu adımları izleyin:

1. **Formlar** araç çubuğunun görüntülendiğinden emin olun.
1. **Seçenek Düğmesi** aracına tıklayın.
1. Çalışma sayfasında, seçenek düğmesini ve yanındaki etiketi tutacak dikdörtgeni tanımlamak için tıklayın ve sürükleyin.
1. Radyo düğmesi çalışma sayfasına yerleştirildikten sonra, fare imleci etiket bölgesine hareket ettirin ve etiketi değiştirin.
1. **Hücre Bağlantısı** alanında, bu radyo düğmesinin bağlanması gereken hücrenin adresini belirtin.
1. **Tamam**'a tıklayın.

### **Aspose.Cells Kullanımı**

[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) sınıfı, bir çalışma sayfasına bir radyo düğmesi denetimi eklemek için kullanılan [**AddRadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addradiobutton) adında bir yöntem sağlar. Yöntem bir [**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton) nesnesi döndürür. [**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton) sınıfı, bir seçenek düğmesini temsil eder. Önemli bazı üyelere sahiptir:

- [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) özelliği, radyo düğmesine bağlı olan bir hücreyi belirtir.
- [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) özelliği, radyo düğmesi ile ilişkilendirilmiş metin dizisini belirtir. Bu, radyo düğmesinin etiketidir.
- [**IsChecked**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton/properties/ischecked) özelliği, radyo düğmesinin işaretli olup olmadığını belirtir.
- [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) özelliği, seçenek düğmesinin doldurma biçimini belirtir.
- [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) özelliği, seçenek düğmesinin çizgi biçimi stillerini belirtir.

Aşağıdaki örnek, bir çalışma sayfasına radyo düğmeleri eklemenin nasıl yapıldığını göstermektedir. Örnek, yaş gruplarını temsil eden üç radyo düğmesi ekler.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingRadioButtonControl-1.cs" >}}

## **Çalışma Sayfasına Kombinasyon Kutusu Denetimi Ekleme**

Veri girişini kolaylaştırmak veya tanımladığınız belirli öğelerle girişleri sınırlamak için, işte çalışma sayfanızda başka yerlerdeki hücrelerden derlenen geçerli girişlerin bir combo kutusu veya açılır liste oluşturabilirsiniz. Bir hücre için bir açılır liste oluşturduğunuzda, o hücrenin yanında bir ok gösterilir. O hücredeki bilgiyi girmek için ok'a tıklayın ve ardından istediğiniz girişi tıklayın.

### **Microsoft Excel Kullanımı**

Çalışma sayfanıza bir kombinasyon kutusu denetimi yerleştirmek için şu adımları izleyin:

1. **Formlar** araç çubuğunun görüntülendiğinden emin olun.
1. **Kombo Kutusu** aracını tıklayın.
1. Çalışma sayfanızda, kombo kutusunu içerecek dikdörtgeni tanımlamak için tıklayıp sürükleyin.
1. Kombo kutusu çalışma sayfasına yerleştirildikten sonra, denetimi sağ tıklayarak **Format Kontrolü** tıklayın ve girdi aralığını belirtin.
1. **Hücre Bağlantısı** alanında, bu kombo kutusunun bağlanacağı hücrenin adresini belirtin.
1. **Tamam**'ı tıklayın.

### **Aspose.Cells Kullanımı**

[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) sınıfı, çalışma sayfasına kombo kutu denetimi eklemek için kullanılan [**AddComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcombobox) adında bir yöntem sağlar. Yöntem bir [**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox) nesnesi döndürür. [**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox) sınıfı bir kombo kutusunu temsil eder. Önemli bazı üyeleri vardır:

- [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) özelliği kombo kutusuna bağlı olan bir hücreyi belirtir.
- [**InputRange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/inputrange) özelliği, kombo kutusunu doldurmak için kullanılan çalışma sayfası aralığını belirtir.
- [**DropDownLines**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox/properties/dropdownlines) özelliği, bir kombo kutusunun açılır kısmında görüntülenen liste satırlarının sayısını belirtir.
- [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox/properties/shadow) özelliği, kombo kutusunun 3B gölgelendirmeye sahip olup olmadığını belirtir.

Aşağıdaki örnek, çalışma sayfasına bir kombo kutusu eklemenin nasıl yapıldığını göstermektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingComboBoxControl-1.cs" >}}

## **Etiket Denetimi Ekleme**

Etiketler, kullanıcılara bir elektronik tablonun içeriği hakkında bilgi vermenin bir yolu olarak kullanılır. Aspose.Cells, çalışma sayfasına etiket eklemeyi ve bunları manipüle etmeyi mümkün kılar. [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) sınıfı, çalışma sayfasına etiket denetimi eklemek için kullanılan [**AddLabel**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabel) adında bir yöntem sağlar. Yöntem bir [**Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) nesnesi döndürür. [**Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) sınıfı, çalışma sayfasında bir etiketi temsil eder. Önemli bazı üyeleri vardır:

- [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) yöntemi, bir etiketin açıklama dizgisini belirtir.
- [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) yöntemi, etiketin çalışma sayfasındaki hücrelere bağlanma şeklini belirtir.

Aşağıdaki örnek, çalışma sayfasına bir etiket eklemenin nasıl yapıldığını göstermektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingLabelControl-1.cs" >}}

## **Liste Kutusu Denetimi Ekleme**

Bir liste kutusu denetimi, tek ya da çoklu öğe seçimine izin veren bir liste denetimi oluşturur.

### **Microsoft Excel Kullanımı**

Bir liste kutusu denetimini çalışma sayfasına yerleştirmek için:

1. **Formlar** araç çubuğunun görüntülendiğinden emin olun.
1. **Liste Kutusu** aracını tıklayın.
1. Çalışma sayfanızda, liste kutusunu içerecek dikdörtgeni tanımlamak için tıklayıp sürükleyin.
1. Liste kutusu çalışma sayfasına yerleştirildikten sonra, denetimi sağ tıklayarak **Format Kontrolü** tıklayın ve girdi aralığını belirtin.
1. **Hücre Bağlantısı** alanında, bu liste kutusunun bağlanacağı hücrenin adresini belirtin ve seçim tipi (Tekli, Çoklu, Genişlet) özniteliğini belirtin.
1. **Tamam**'a tıklayın.

### **Aspose.Cells Kullanımı**

[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) sınıfı, çalışma sayfasına liste kutusu denetimi eklemek için kullanılan [**AddListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlistbox) adında bir yöntem sağlar. Yöntem bir [**Aspose.Cells.Drawing.ListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox) nesnesi döndürür. [**ListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox) sınıfı bir liste kutusunu temsil eder. Önemli bazı üyeleri vardır:

- [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) method, bir liste kutusuna bağlı olan hücreyi belirtir.
- [**InputRange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/inputrange) method, liste kutusunu doldurmak için kullanılan çalışma sayfası hücre aralığını belirtir.
- [**SelectionType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox/properties/selectiontype) method, liste kutusunun seçim kipini belirtir.
- [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox/properties/shadow) methodı, liste kutusunun 3D gölgelemeye sahip olup olmadığını gösterir.

Aşağıdaki örnek, çalışma sayfasına liste kutusu nasıl eklenir gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingListBoxControl-1.cs" >}}

## **Bir Çalışma Sayfasına Düğme Kontrolü Ekleme**

Düğmeler bazı işlemleri gerçekleştirmek için kullanışlıdır. Bazen düğmeye VBA Makrosu atamak veya bir web sayfasını açmak için bir bağlantı atamak faydalı olabilir.

### **Microsoft Excel Kullanımı**

Bir düğme kontrolünü çalışma sayfanıza yerleştirmek için:

1. **Formlar** araç çubuğunun görüntülendiğinden emin olun.
1. **Düğme** aracını tıklayın.
1. Çalışma sayfanızdaki alanda, düğmeyi tutacak dikdörtgeni tanımlamak için tıklayın ve sürükleyin.
1. Liste kutusu çalışma sayfasına yerleştirildikten sonra, denetim üzerinde sağ tıklayın ve sonra **Denetim Biçimi'ni** seçin, ardından VBA Makrosunu ve ilgili yazı tipi, hizalama, boyut, kenar boşluğu vb. özellikleri belirtin.
1. **Tamam**'ı tıklayın.

### **Aspose.Cells Kullanımı**

[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) sınıfı, çalışma sayfasına bir düğme kontrolü eklemek için kullanılan [**AddButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addbutton) adında bir yöntem sağlar. Yöntem bir [**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/net/aspose.cells.drawing/button) nesnesi döndürür. [**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/net/aspose.cells.drawing/button) sınıfı bir düğmeyi temsil eder. Bazı önemli üyelere sahiptir:

- [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) özelliği, düğmenin başlığını belirtir.
- [**Font**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/font) özelliği, düğme denetiminin etiketi için yazı tipi özniteliklerini belirtir.
- [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) özelliği, [**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), düğmenin çalışma sayfasındaki hücrelere nasıl bağlandığını belirtir.
- [**AddHyperlink**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/addhyperlink) özelliği, düğme denetimi için bir bağlantı ekler. Düğmeye tıklamak ilgili URL'ye gid will navigate to related URL.

Aşağıdaki örnek, çalışma sayfasına bir düğme eklemenin nasıl yapılacağını gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingButtonControl-1.cs" >}}

## **Çalışma Sayfasına Satır Kontrolü Ekleme**

### **Microsoft Excel Kullanımı**

1. **Çizim** araç çubuğunda, **Şekiller**'e tıklayın, ardından **Satırlar**'a gelin ve istediğiniz çizgi stiline tıklayın.
1. Çizmek için sürükleyin.
1. Aşağıdakilerden birini veya her ikisinden birini yapın:
   1. Çizginin başlangıç noktasından 15 derece açılarla çizilmesini sınırlamak için, sürüklerken **SHIFT** tuşunu basılı tutun.
   1. İlk uç noktasından zıt yönlere doğru çizgiyi uzatmak için, sürüklerken **CTRL** tuşunu basılı tutun.

### **Aspose.Cells Kullanımı**

[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) sınıfı, çalışma sayfasına bir çizgi şekli eklemek için kullanılan [**AddLine**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline) adında bir yöntem sağlar. Yöntem bir [**LineShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) nesne döndürür. [**LineShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) sınıfı bir çizgiyi temsil eder. Bazı önemli üyelere sahiptir:

- [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) yöntemi bir satırın formatını belirtir.
- [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) yöntemi, satırın hücrelere bağlandığı [**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype) biçimini belirtir.

Aşağıdaki örnek, çalışma sayfasına satır eklemenin nasıl yapıldığını gösterir. Farklı stillerde üç satır oluşturur.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingLineControl-1.cs" >}}

### **Bir ok başlığı eklemek**

Aspose.Cells, oklu satırlar çizmenize de olanak tanır. Bir satıra bir ok başlığı eklemek ve satırın biçimlendirilmesi mümkündür. Örneğin, satırın rengini değiştirebilir veya satırın ağırlığını ve stilini belirtebilirsiniz.

Aşağıdaki örnek, bir satıra bir ok başlığı eklemenin nasıl yapıldığını gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddinganArrowHead-1.cs" >}}

## **Çalışma Sayfasına Dikdörtgen Kontrolü Ekleme**

Aspose.Cells, çalışma sayfalarınızda dikdörtgen şekilleri çizmenize olanak tanır. Bir dikdörtgen, kare vb. oluşturabilirsiniz. Ayrıca kontrolün doldurma rengini, sınır çizgisi rengini biçimlendirmenize izin verilir. Örneğin, dikdörtgenin rengini değiştirebilir, gölgelendirme rengini ayarlayabilir veya dikdörtgenin ağırlığını ve stilini belirleyebilirsiniz.

### **Microsoft Excel Kullanımı**

1. **Çizim** araç çubuğunda, **Dikdörtgen**'e tıklayın.
1. Dikdörtgen çizmek için sürükleyin.
1. Aşağıdakilerden birini veya her ikisinden birini yapın:
   1. Dikdörtgeni başlangıç noktasından karesel çizmeyi kısıtlamak için sürükleme sırasında SHIFT tuşunu basılı tutun.
   1. Dikdörtgeni merkez noktasından çizmek için sürükleme sırasında CTRL tuşunu basılı tutun.

### **Aspose.Cells Kullanımı**

[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) sınıfı, çalışma sayfasına bir dikdörtgen şekli eklemek için kullanılan [**AddRectangle**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle) adında bir yöntem sağlar. Yöntem bir [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) nesnesi döndürür. [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) sınıfı bir dikdörtgeni temsil eder. Bazı önemli üyelere sahiptir:

- [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) özelliği bir dikdörtgenin satır formatı özelliklerini belirtir.
- [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) özelliği, dikdörtgenin çalışma sayfasındaki hücrelere bağlandığı [**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype) biçimini belirtir.
- [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) özelliği bir dikdörtgenin doldurma biçimi stillerini belirtir.

Aşağıdaki örnek, bir dikdörtgenin çalışma sayfasına nasıl eklendiğini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingRectangleControl-1.cs" >}}

## **Çalışma Sayfasına Yay Kontrolü Ekleme**

Aspose.Cells, çalışma sayfalarında yay şekilleri çizmenize olanak tanır. Basit ve dolu yaylar oluşturabilirsiniz. Kontrolün doldurma rengini ve sınır çizgisi rengini biçimlendirmenize izin verilir. Örneğin, yayın rengini belirleyebilir, gölgelendirme rengini ayarlayabilir veya şeklin ağırlığını ve stilini belirleyebilirsiniz.

### **Microsoft Excel Kullanımı**

1. **Çizim** araç çubuğunda, **Otomatik Şekiller** içinde **Yay**'e tıklayın.
1. Yay çizmek için sürükleyin.

### **Aspose.Cells Kullanımı**

[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) sınıfı, çalışma sayfasına bir yay şekli eklemek için kullanılan [**AddArc**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addarc) adında bir yöntem sağlar. Yöntem bir [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/arcshape) nesnesi döndürür. [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/arcshape) sınıfı bir yayı temsil eder. Bazı önemli üyelere sahiptir:

- [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) özelliği bir yayın satır formatı özelliklerini belirtir.
- [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) özelliği, yayın çalışma sayfasındaki hücrelere bağlandığı [**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype) biçimini belirtir.
- [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) özelliği şeklin doldurma biçimi stillerini belirtir.
- [**LowerRightRow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightrow) özelliği sağ alt köşe satır indisini belirtir.
- [**LowerRightColumn**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightcolumn) özelliği sağ alt köşe sütun indisini belirtir.

Aşağıdaki örnek, çalışma sayfasına yay şekilleri eklemenin nasıl yapıldığını göstermektedir. Örnek iki yay şekli oluşturur: biri doldurulmuş ve diğeri basit.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingArcControl-1.cs" >}}

## **Çalışma Sayfasına Oval Kontrolü Ekleme**

Aspose.Cells, çalışma sayfalarında oval şekilleri çizmenize olanak tanır. Basit ve dolu oval şekiller oluşturun ve kontrolün doldurma rengini ve kenar çizgisi rengini biçimlendirin. Örneğin, ovalin rengini belirleyebilir, gölgelendirme rengini ayarlayabilir, şeklin ağırlığını ve stilini belirleyebilirsiniz.

### **Microsoft Excel Kullanımı**

- *Çizim* araç çubuğunda, *Oval* a tıklayın.
- Oval çizmek için sürükleyin.
- Aşağıdakilerden birini veya her ikisini yapın:
- Ovalin başlangıç noktasından bir daire çizmek için sürükleme işlemini yaparken SHIFT tuşunu basılı tutun.
- Bir ovalı merkez noktasından çizmek için sürükleme işlemi yaparken CTRL tuşunu basılı tutun.

### **Aspose.Cells Kullanımı**

[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) sınıfı, çalışma sayfasına oval bir şekil eklemek için kullanılan [**AddOval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addoval) adında bir yöntem sağlar. Yöntem, bir [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oval) nesnesi döndürür. [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oval) sınıfı bir oval şekli temsil eder. Bazı önemli üyelere sahiptir:

- [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) özelliği bir oval şeklin çizgi biçimi özniteliklerini belirtir.
- [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) özelliği, ovalin çalışma sayfasındaki hücrelere bağlandığı [**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype) şeklini belirtir.
- [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) özelliği şeklin doldurma biçimi stillerini belirtir.
- [**LowerRightRow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightrow) özelliği sağ alt köşe satır indisini belirtir.
- [**LowerRightColumn**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightcolumn) özelliği sağ alt köşe sütun indisini belirtir.

Aşağıdaki örnek, çalışma sayfasına oval şekiller eklemenin nasıl yapıldığını göstermektedir. Örnek iki oval şekli oluşturur: biri doldurulmuş oval diğeri basit daire.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingOvalControl-1.cs" >}}

## **Çalışma Sayfasına Spinner Kontrolü Ekleme**

Bir spin kutusu, bir yukarı ok ve aşağı ok içeren bir düğmeye (spin düğmesi denir) bağlı bir metin kutusudur. Finansal modelinizde girdilerin değişiminin model çıktılarını nasıl değiştireceğini görebilirsiniz. Bir spin kutusunu belirli bir girdi hücresine bağlayabilirsiniz. Spin düğmesine tıkladığınızda, hedef girdi hücresindeki tam sayı değeri artar veya azalır. *Aspose.Cells*, çalışma sayfalarınızda spinner'lar oluşturmanıza olanak tanır.

### **Microsoft Excel Kullanımı**

Çalışma sayfanıza bir spin kutusu kontrolü yerleştirmek için:

- *Formlar* araç çubuğunun görüntülendiğinden emin olun.
- *Spinner* aracına tıklayın.
- Çalışma sayfanızdaki alanda, spinner'ı tutacak dikdörtgeni tanımlamak için tıklayın ve sürükleyin.
- Spinner çalışma sayfasına yerleştirildiğinde, kontrolün üzerine sağ tıklayın ve *Kontrolü Biçimlendir* i tıklayın ve maksimum, minimum ve artış değerlerini belirtin.
- *Bağlantı Hücresi* alanında, bu spin kutusunun bağlanması gereken hücrenin adresini belirtin.
- *Tamam* a tıklayın.

### **Aspose.Cells Kullanımı**

Sınıf [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection), bir çalışma sayfasına bir spin kutu denetimini eklemek için kullanılan [**AddSpinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addspinner) adında bir yöntem sağlar. Yöntem bir [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner) nesnesi döndürür. [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner) sınıfı bir spin kutusunu temsil eder. Bazı önemli üyeleri vardır:

- [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) özelliği, spin kutusuyla bağlantılı bir hücreyi belirtir.
- [**Max**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/max) özelliği, spin kutusu aralığı için maksimum değeri belirtir.
- [**Min**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/min) özelliği, spin kutusu aralığı için minimum değeri belirtir.
- [**IncrementalChange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/incrementalchange) özelliği, bir kaydırıcının bir satır kaydırılacak değer miktarını belirtir.
- [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/shadow) özelliği, spin kutusunun 3B gölgeli olup olmadığını belirtir.
- [**CurrentValue**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/currentvalue) özelliği, spin kutusunun geçerli değerini belirtir.

Aşağıdaki örnek, çalışma sayfasına bir spin kutusu eklemenin nasıl yapıldığını gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingSpinnerControl-1.cs" >}}

## **Bir Çalışma Sayfasına Kaydırma Çubuğu Denetimi Ekleme**

Bir kaydırma çubuğu denetimi, bir çalışma sayfasında bir spin kutu denetimiyle benzer şekilde veri seçmeye yardımcı olmak için kullanılır. Denetimi bir çalışma sayfasına ekleyerek ve bir hücreye bağlayarak, denetimin mevcut konumunun sayısal bir değerini döndürmek mümkün olur.

### **Microsoft Excel Kullanımı**

- Excel 2003 ve daha önceki sürümlerde bir kaydırma çubuğu eklemek için, *Formlar* araç çubuğunda *Kaydırma Çubuğu* düğmesine tıklayın, ardından B2:B6 hücrelerini kaplayan ve sütunun genişliğinin yaklaşık dörtte biri uzunluğunda bir kaydırma çubuğu oluşturun.
- Excel 2007'de bir kaydırma çubuğu eklemek için *Geliştirici* sekmesine, ardından *Ekle* düğmesine ve ardından Form Kontrolleri bölümünde *Kaydırma Çubuğu*na tıklayın.
- Kaydırma çubuğuna sağ tıklayın ve ardından *Biçimlendirme Denetimi*ne tıklayın.
- Aşağıdaki bilgileri girin ve *Tamam* 'a tıklayın:
  - *Mevcut değer* kutusuna 1 yazın.
  - *Minimum değer* kutusuna 1 yazın. Bu değer, listedeki ilk öğenin üstünü kaydırma çubuğuna kısıtlar.
  - *Maksimum değer* kutusuna 20 yazın. Bu sayı, listedeki maksimum giriş sayısını belirtir.
  - *Artış değişikliği* kutusuna 1 yazın. Bu değer, kaydırma çubuğu denetimi mevcut değeri kaç sayı arttırırı belirler.
  - *Sayfa değişikliği* kutusuna 5 yazın. Bu giriş, kaydırma çubuğunda kaydırma kutusunun her iki tarafına tıklandığında mevcut değerin ne kadar artacağını kontrol eder.
  - Listenin seçilen öğesine bağlı olarak G1 hücresine bir sayı değeri koymak için, *Hücre bağlantısı* kutusuna G1 yazın.
- Kaydırma çubuğu seçilmediğinde herhangi bir hücreye tıklayın.

Kaydırma çubuğundaki yukarı veya aşağı kontrolüne tıkladığınızda, G1 hücresi, kaydırma çubuğunun artı veya eksi kaydırma çubuğu değişikliğinin mevcut değerini gösteren bir sayıya güncellenir.

### **Aspose.Cells Kullanımı**

Sınıf [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection), bir çalışma sayfasına bir kaydırma çubuğu denetimini eklemek için kullanılan [**AddScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addscrollbar) adında bir yöntem sağlar. Yöntem bir [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar) nesnesi döndürür. [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar) sınıfı bir kaydırma çubuğunu temsil eder. Bazı önemli üyeleri vardır:

- [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) özelliği, kaydırma çubuğuyla bağlantılı bir hücreyi belirtir.
- [**Max**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/max) özelliği, kaydırma çubuğu aralığı için maksimum değeri belirtir.
- [**Min**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/min) özelliği, kaydırma çubuğu aralığı için minimum değeri belirtir.
- [**IncrementalChange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/incrementalchange) özelliği, bir kaydırmanın bir satır kaydırılacak değer miktarını belirtir.
- [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/shadow) özelliği, bir kaydırma çubuğunun 3B gölgeli olup olmadığını belirtir.
- [**CurrentValue**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/currentvalue) özelliği, kaydırma çubuğunun mevcut değerini belirtir.
- [**PageChange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/pagechange) özelliği, kaydırma çubuğunun her iki yanına da tıklarsanız mevcut değerin ne kadar artırılacağını belirtir.

Aşağıdaki örnek, çalışma sayfasına bir kaydırma çubuğu nasıl ekleyeceğinizi gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingScrollBarControl-1.cs" >}}

## **Çalışma Sayfasındaki Grup Kontrollerine GroupBox Kontrolü Ekleme**

Bazen belirli bir gruba ait radyo düğmeleri veya diğer kontrolleri uygulamanız gerekebilir, bunu grup kutusu veya dikdörtgen kontrolünü dahil ederek uygulayabilirsiniz. Bu iki nesneden herhangi biri grup sınırlandırıcısı olarak hizmet eder. Bu şekillerden birini ekledikten sonra, ardından iki veya daha fazla radyo düğmesi veya diğer grup nesnelerini ekleyebilirsiniz.

### **Microsoft Excel Kullanımı**

Çalışma sayfanıza bir grup kutu kontrolü eklemek ve içine kontroller yerleştirmek için:

- Bir form başlatmak için ana menüde *Görünüm*ü, ardından *Araç Çubukları* ve *Formlar*ı tıklayın.
- *Formlar* araç çubuğunda, *Grup Kutu*nu tıklayın ve çalışma sayfasında bir dikdörtgen çizin.
- Kutu için bir başlık dizesi yazın.
- *Formlar* araç çubuğunda, *Seçenek Düğmesi*ne tıklayın ve başlık dizesinin hemen altına *Grup Kutusu*na tıklayın.
- *Formlar* araç çubuğunda tekrar *Seçenek Düğmesi*ne tıklayın ve önceki radyo düğmesinin altında *Grup Kutusu*na tıklayın.
- *Formlar* araç çubuğunda tekrar *Seçenek Düğmesi*ne tıklayın ve önceki radyo düğmesinin altında *Grup Kutusu*na tıklayın.

### **Aspose.Cells Kullanımı**

[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) sınıfı, çalışma sayfasına bir grup kutu kontrolü eklemek için kullanılan [**AddGroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addgroupbox) adında bir yöntem sağlar. Yöntem bir [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox) nesnesi döndürür. Ayrıca, [**Group**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/group) yöntemi, şekilleri gruplar, bu, bir [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) dizisi alır ve bir [**Shape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) nesnesi döndürür. [**GroupShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupshape) sınıfı bir grup kutusunu temsil eder. Önemli bazı üyelere sahiptir:

- [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) özelliği grup kutusunun başlık dizesini belirtir.
- [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox/properties/shadow) özelliği grup kutusunun 3B gölgeleme olup olmadığını belirtir.

Aşağıdaki örnek, çalışma sayfasına bir grup kutu eklemeyi ve kontrolleri gruplamayı gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingGroupBoxControl-1.cs" >}}

## **Gelişmiş Konular**
- [Aspose.Cells Kullanarak ActiveX Kontrolleri Ekleme](/cells/tr/net/add-activex-controls-using-aspose-cells/)
- [ActiveX Kontrolü Kaldırma](/cells/tr/net/remove-activex-control/)
- [ActiveX ComboBox Kontrolünü Güncelleme](/cells/tr/net/update-activex-combobox-control/)
{{< app/cells/assistant language="csharp" >}}
