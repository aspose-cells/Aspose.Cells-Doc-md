---
title: Kontrolleri Yönetme
type: docs
weight: 150
url: /tr/python-net/managing-controls/
---

## **Giriş**

Geliştiriciler, metin kutuları, onay kutuları, radyo düğmeleri, açılır kutular, etiketler, düğmeler, çizgiler, dikdörtgenler, yaylar, elipsler, dönen çubuklar, kaydırıcılar, grup kutuları vb. gibi farklı çizim nesneleri ekleyebilirler. Aspose.Cells for Python via .NET, tüm çizim nesnelerini içeren Aspose.Cells.Drawing ad alanını sağlar. Ancak, henüz desteklenmeyen birkaç çizim nesnesi veya şekil vardır. Bu çizim nesnelerini tasarımcı çalışma kitabında Microsoft Excel kullanarak oluşturun ve ardından tasarımcı çalışma kitabını Aspose.Cells'e aktarın. Aspose.Cells for Python via .NET, bu çizim nesnelerini tasarımcı çalışma kitabından yükleyip, oluşturulan dosyaya yazmanıza olanak tanır.

## **Bir Çalışma Sayfasına Metin Kutusu Denetimi Ekleme**

Raporlarda önemli bilgileri vurgulamanın bir yolu, bir metin kutusu kullanmaktır. Örneğin, şirket adını vurgulamak veya en yüksek satış bölgesini göstermek için metin ekleyin vb. Aspose.Cells for Python via .NET, yeni bir metin kutusu eklemek için kullanılan [**TextBoxCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/textboxcollection) sınıfını sağlar. Ayrıca, tüm ayarları tanımlayan bir metin kutusunu temsil eden başka bir [**TextBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/textbox) sınıfı da vardır. Bu sınıfın bazı önemli üyeleri bulunmaktadır:

- [**text_frame**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text_frame) özelliği, metin kutusunun içeriğini ayarlamak için kullanılan bir [**MsoTextFrame**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/msotextframe) nesnesi döndürür.
- [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) özelliği yerleştirme türünü belirtir.
- [**font**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/font) özelliği yazı tipi özelliklerini belirtir.
- [**add_hyperlink**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/add_hyperlink) methodu, metin kutusu için bir bağlantıyı ekler.
- [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) özelliği, metin kutusunun dolgu biçimini ayarlamak için kullanılan bir [**MsoFillFormat**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/msofillformat) nesnesini döndürür.
- [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) özelliği, metin kutusu çizgisi için stil ve kalınlık genellikle kullanılan bir [**MsoLineFormat**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/msolineformat) nesnesi döndürür.
- [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) özelliği giriş metnini belirtir.

Aşağıdaki örnek, çalışma kitabının ilk çalışma sayfasında iki metin kutusu oluşturur. İlk metin kutusu farklı biçim ayarlarıyla donatılmıştır. İkincisi ise basit bir tanedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingTextBoxControl-1.py" >}}

## **Tasarımcı Elektronik Tablolarda Metin Kutusu Denetimlerini Manipüle Etme**

Aspose.Cells for Python via .NET ayrıca tasarımcı çalışma sayfalarındaki metin kutularına erişmenize ve onları değiştirmenize olanak tanır. Sayfadaki metin kutuları koleksiyonunu almak için [**Worksheet.TextBoxes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/text_boxes) özelliğini kullanın.

Aşağıdaki örnek yukarıdaki örnekte oluşturduğumuz Microsoft Excel dosyasını kullanır. İki metin kutusunun metin dizelerini alır ve ikinci metin kutusunun metnini değiştirerek dosyayı kaydeder.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-ManipulatingTextBoxControls-1.py" >}}

## **Bir Çalışma Sayfasına Onay Kutusu Denetimi Ekleme**

Onay kutuları, kullanıcıya doğru veya yanlış, evet veya hayır gibi iki seçenek arasından seçim yapma imkanı sunmak istediğinizde kullanışlıdır. Aspose.Cells for Python via .NET, çalışma sayfalarında onay kutuları kullanmanızı sağlar. Örneğin, belirli bir satın alma işlemini hesaba katıp katmamaya karar verdiğiniz finansal projeksiyon çalışma kitabınız olduğunu varsayalım. Bu durumda, çalışma sayfasının en üstüne bir onay kutusu yerleştirmek isteyebilirsiniz. Durumunu bu onay kutusuna bağlayabilir ve böylece onay kutusu seçilirse hücrenin değeri True, seçilmezse False olur.

### **Microsoft Excel Kullanımı**

Çalışma sayfanıza bir onay kutusu denetimi yerleştirmek için şu adımları izleyin:

1. Formlar araç çubuğunun görüntülendiğinden emin olun.
1. Formlar araç çubuğunda **Onay Kutusu** aracını tıklayın.
1. Çalışma sayfanızda, onay kutusunu ve onay kutusunun yanındaki etiketi içerecek dikdörtgeni tanımlamak için tıklayın ve sürükleyin.
1. Onay kutusu yerleştirildikten sonra fare imleci etiket alanına kaydırın ve etiketi değiştirin.
1. **Hücre Bağlantısı** alanında, bu onay kutusunun bağlanması gereken hücrenin adresini belirtin.
1. **Tamam**'ı tıklayın.

### **Aspose.Cells for Python via .NET Kullanılarak**

Aspose.Cells for Python via .NET, koleksiyona yeni bir onay kutusu eklemek için kullanılır [**CheckBoxCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/checkboxcollection) sınıfını sağlar. Başka bir sınıf, [**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/checkbox), bir onay kutusunu temsil eder. Bazı önemli üyeleri vardır:

- [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) özelliği, onay kutusuna bağlı olan bir hücreyi belirtir.
- [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) özelliği, onay kutusu ile ilişkilendirilmiş metin dizisini belirtir. Bu, onay kutusunun etiketidir.
- [**value**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/checkbox/value) özelliği, onay kutusunun işaretli olup olmadığını belirtir.

Aşağıdaki örnek, bir çalışma sayfasına onay kutusu eklemenin nasıl yapıldığını göstermektedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingCheckBoxControl-1.py" >}}

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

### **Aspose.Cells for Python via .NET Kullanılarak**

[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) sınıfı, bir çalışma sayfasına bir radyo düğmesi denetimi eklemek için kullanılan [**add_radio_button**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_radio_button) adında bir yöntem sağlar. Yöntem bir [**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/radiobutton) nesnesi döndürür. [**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/radiobutton) sınıfı, bir seçenek düğmesini temsil eder. Önemli bazı üyelere sahiptir:

- [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) özelliği, radyo düğmesine bağlı olan bir hücreyi belirtir.
- [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) özelliği, radyo düğmesi ile ilişkilendirilmiş metin dizisini belirtir. Bu, radyo düğmesinin etiketidir.
- [**is_checked**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/radiobutton/is_checked) özelliği, radyo düğmesinin işaretli olup olmadığını belirtir.
- [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) özelliği, seçenek düğmesinin doldurma biçimini belirtir.
- [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) özelliği, seçenek düğmesinin çizgi biçimi stillerini belirtir.

Aşağıdaki örnek, bir çalışma sayfasına radyo düğmeleri eklemenin nasıl yapıldığını göstermektedir. Örnek, yaş gruplarını temsil eden üç radyo düğmesi ekler.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingRadioButtonControl-1.py" >}}

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

### **Aspose.Cells for Python via .NET Kullanılarak**

[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) sınıfı, çalışma sayfasına kombo kutu denetimi eklemek için kullanılan [**add_combo_box**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_combo_box) adında bir yöntem sağlar. Yöntem bir [**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox) nesnesi döndürür. [**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox) sınıfı bir kombo kutusunu temsil eder. Önemli bazı üyeleri vardır:

- [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) özelliği kombo kutusuna bağlı olan bir hücreyi belirtir.
- [**input_range**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/input_range) özelliği, kombo kutusunu doldurmak için kullanılan çalışma sayfası aralığını belirtir.
- [**drop_down_lines**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox/drop_down_lines) özelliği, bir kombo kutusunun açılır kısmında görüntülenen liste satırlarının sayısını belirtir.
- [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox/shadow) özelliği, kombo kutusunun 3B gölgelendirmeye sahip olup olmadığını belirtir.

Aşağıdaki örnek, çalışma sayfasına bir kombo kutusu eklemenin nasıl yapıldığını göstermektedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingComboBoxControl-1.py" >}}

## **Etiket Denetimi Ekleme**

Etiketler, kullanıcılara bir elektronik tablonun içeriği hakkında bilgi verme aracıdır. Aspose.Cells for Python via .NET, bir çalışma sayfasında etiketler eklemeyi ve bunları manipüle etmeyi mümkün kılar. [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) sınıfı, çalışma sayfasına bir etiket kontrolü eklemek için kullanılan [**add_label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_label) adlı bir yöntem sağlar. Bu yöntem bir [**Label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/label) nesnesi döner. [**Label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/label) sınıfı, çalışma sayfasındaki bir etiketi temsil eder. Bazı önemli üyeleri vardır:

- [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) yöntemi, bir etiketin açıklama dizgisini belirtir.
- [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) yöntemi, etiketin çalışma sayfasındaki hücrelere bağlanma şeklini belirtir.

Aşağıdaki örnek, çalışma sayfasına bir etiket eklemenin nasıl yapıldığını göstermektedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingLabelControl-1.py" >}}

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

### **Aspose.Cells for Python via .NET Kullanılarak**

[**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) sınıfı, çalışma sayfasına liste kutusu denetimi eklemek için kullanılan [**add_list_box**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_list_box) adında bir yöntem sağlar. Yöntem bir [**Aspose.Cells.Drawing.ListBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/listbox) nesnesi döndürür. [**ListBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/listbox) sınıfı bir liste kutusunu temsil eder. Önemli bazı üyeleri vardır:

- [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) method, bir liste kutusuna bağlı olan hücreyi belirtir.
- [**input_range**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/input_range) method, liste kutusunu doldurmak için kullanılan çalışma sayfası hücre aralığını belirtir.
- [**selection_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/listbox/selection_type) method, liste kutusunun seçim kipini belirtir.
- [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/listbox/shadow) methodı, liste kutusunun 3D gölgelemeye sahip olup olmadığını gösterir.

Aşağıdaki örnek, çalışma sayfasına liste kutusu nasıl eklenir gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingListBoxControl-1.py" >}}

## **Bir Çalışma Sayfasına Düğme Kontrolü Ekleme**

Düğmeler bazı işlemleri gerçekleştirmek için kullanışlıdır. Bazen düğmeye VBA Makrosu atamak veya bir web sayfasını açmak için bir bağlantı atamak faydalı olabilir.

### **Microsoft Excel Kullanımı**

Bir düğme kontrolünü çalışma sayfanıza yerleştirmek için:

1. **Formlar** araç çubuğunun görüntülendiğinden emin olun.
1. **Düğme** aracını tıklayın.
1. Çalışma sayfanızdaki alanda, düğmeyi tutacak dikdörtgeni tanımlamak için tıklayın ve sürükleyin.
1. Liste kutusu çalışma sayfasına yerleştirildikten sonra, denetim üzerinde sağ tıklayın ve sonra **Denetim Biçimi'ni** seçin, ardından VBA Makrosunu ve ilgili yazı tipi, hizalama, boyut, kenar boşluğu vb. özellikleri belirtin.
1. **Tamam**'ı tıklayın.

### **Aspose.Cells for Python via .NET Kullanılarak**

[**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) sınıfı, çalışma sayfasına bir düğme kontrolü eklemek için kullanılan [**add_button**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_button) adında bir yöntem sağlar. Yöntem bir [**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/button) nesnesi döndürür. [**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/button) sınıfı bir düğmeyi temsil eder. Bazı önemli üyelere sahiptir:

- [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) özelliği, düğmenin başlığını belirtir.
- [**font**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/font) özelliği, düğme denetiminin etiketi için yazı tipi özniteliklerini belirtir.
- [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) özelliği, [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype), düğmenin çalışma sayfasındaki hücrelere nasıl bağlandığını belirtir.
- [**add_hyperlink**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/add_hyperlink) özelliği, düğme denetimi için bir bağlantı ekler. Düğmeye tıklamak ilgili URL'ye gid will navigate to related URL.

Aşağıdaki örnek, çalışma sayfasına bir düğme eklemenin nasıl yapılacağını gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingButtonControl-1.py" >}}

## **Çalışma Sayfasına Satır Kontrolü Ekleme**

### **Microsoft Excel Kullanımı**

1. **Çizim** araç çubuğunda, **Şekiller**'e tıklayın, ardından **Satırlar**'a gelin ve istediğiniz çizgi stiline tıklayın.
1. Çizmek için sürükleyin.
1. Aşağıdakilerden birini veya her ikisinden birini yapın:
   1. Çizginin başlangıç noktasından 15 derece açılarla çizilmesini sınırlamak için, sürüklerken **SHIFT** tuşunu basılı tutun.
   1. İlk uç noktasından zıt yönlere doğru çizgiyi uzatmak için, sürüklerken **CTRL** tuşunu basılı tutun.

### **Aspose.Cells for Python via .NET Kullanılarak**

[**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) sınıfı, çalışma sayfasına bir çizgi şekli eklemek için kullanılan [**add_line**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_line) adında bir yöntem sağlar. Yöntem bir [**LineShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/lineshape) nesne döndürür. [**LineShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/lineshape) sınıfı bir çizgiyi temsil eder. Bazı önemli üyelere sahiptir:

- [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) yöntemi bir satırın formatını belirtir.
- [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) yöntemi, satırın hücrelere bağlandığı [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype) biçimini belirtir.

Aşağıdaki örnek, çalışma sayfasına satır eklemenin nasıl yapıldığını gösterir. Farklı stillerde üç satır oluşturur.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingLineControl-1.py" >}}

### **Bir ok başlığı eklemek**

Aspose.Cells for Python via .NET ayrıca ok ve okyan çizgilerini çizmenize olanak sağlar. Bir çizgiye ok başlığı eklemek ve çizgiyi biçimlendirmek mümkündür. Örneğin, çizginin rengini değiştirebilir veya çizgi kalınlığı ve stilini belirtebilirsiniz.

Aşağıdaki örnek, bir satıra bir ok başlığı eklemenin nasıl yapıldığını gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddinganArrowHead-1.py" >}}

## **Çalışma Sayfasına Dikdörtgen Kontrolü Ekleme**

Aspose.Cells for Python via .NET, çalışma sayfalarınızda dikdörtgen şekiller çizebilmenizi sağlar. Bir dikdörtgen, kare vb. oluşturabilirsiniz. Ayrıca, kontrolün doldurma rengi ve kenarlık çizgi rengini biçimlendirmeye izin verilir. Örneğin, dikdörtgenin rengini değiştirebilir, gölgeleme rengini ayarlayabilir ve ihtiyacınıza göre dikdörtgenin kalınlığı ve stilini belirleyebilirsiniz.

### **Microsoft Excel Kullanımı**

1. **Çizim** araç çubuğunda, **Dikdörtgen**'e tıklayın.
1. Dikdörtgen çizmek için sürükleyin.
1. Aşağıdakilerden birini veya her ikisinden birini yapın:
   1. Dikdörtgeni başlangıç noktasından karesel çizmeyi kısıtlamak için sürükleme sırasında SHIFT tuşunu basılı tutun.
   1. Dikdörtgeni merkez noktasından çizmek için sürükleme sırasında CTRL tuşunu basılı tutun.

### **Aspose.Cells for Python via .NET Kullanılarak**

[**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) sınıfı, çalışma sayfasına bir dikdörtgen şekli eklemek için kullanılan [**add_rectangle**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_rectangle) adında bir yöntem sağlar. Yöntem bir [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/rectangleshape) nesnesi döndürür. [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/rectangleshape) sınıfı bir dikdörtgeni temsil eder. Bazı önemli üyelere sahiptir:

- [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) özelliği bir dikdörtgenin satır formatı özelliklerini belirtir.
- [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) özelliği, dikdörtgenin çalışma sayfasındaki hücrelere bağlandığı [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype) biçimini belirtir.
- [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) özelliği bir dikdörtgenin doldurma biçimi stillerini belirtir.

Aşağıdaki örnek, bir dikdörtgenin çalışma sayfasına nasıl eklendiğini gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingRectangleControl-1.py" >}}

## **Çalışma Sayfasına Yay Kontrolü Ekleme**

Aspose.Cells for Python via .NET kullanırken

### **Microsoft Excel Kullanımı**

1. **Çizim** araç çubuğunda, **Otomatik Şekiller** içinde **Yay**'e tıklayın.
1. Yay çizmek için sürükleyin.

### **Aspose.Cells for Python via .NET Kullanılarak**

[**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) sınıfı, çalışma sayfasına bir yay şekli eklemek için kullanılan [**add_arc**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_arc) adında bir yöntem sağlar. Yöntem bir [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/arcshape) nesnesi döndürür. [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/arcshape) sınıfı bir yayı temsil eder. Bazı önemli üyelere sahiptir:

- [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) özelliği bir yayın satır formatı özelliklerini belirtir.
- [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) özelliği, yayın çalışma sayfasındaki hücrelere bağlandığı [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype) biçimini belirtir.
- [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) özelliği şeklin doldurma biçimi stillerini belirtir.
- [**lower_right_row**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/lower_right_row) özelliği sağ alt köşe satır indisini belirtir.
- [**lower_right_column**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/lower_right_column) özelliği sağ alt köşe sütun indisini belirtir.

Aşağıdaki örnek, çalışma sayfasına yay şekilleri eklemenin nasıl yapıldığını göstermektedir. Örnek iki yay şekli oluşturur: biri doldurulmuş ve diğeri basit.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingArcControl-1.py" >}}

## **Çalışma Sayfasına Oval Kontrolü Ekleme**

Aspose.Cells for Python via .NET, çalışma sayfalarında oval şekiller çizmenize izin verir. Basit ve doldurulmuş oval şekiller oluşturabilir ve doldurma rengi ile kenarlık renkleri biçimlendirebilirsiniz. Örneğin, ovalin rengini belirtebilir/değiştirebilir, gölgeleme rengini ayarlayabilir ve şeklin kalınlık ve stilini belirleyebilirsiniz.

### **Microsoft Excel Kullanımı**

- *Çizim* araç çubuğunda, *Oval* a tıklayın.
- Oval çizmek için sürükleyin.
- Aşağıdakilerden birini veya her ikisini yapın:
- Ovalin başlangıç noktasından bir daire çizmek için sürükleme işlemini yaparken SHIFT tuşunu basılı tutun.
- Bir ovalı merkez noktasından çizmek için sürükleme işlemi yaparken CTRL tuşunu basılı tutun.

### **Aspose.Cells for Python via .NET Kullanılarak**

[**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) sınıfı, çalışma sayfasına oval bir şekil eklemek için kullanılan [**add_oval**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_oval) adında bir yöntem sağlar. Yöntem, bir [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oval) nesnesi döndürür. [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oval) sınıfı bir oval şekli temsil eder. Bazı önemli üyelere sahiptir:

- [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) özelliği bir oval şeklin çizgi biçimi özniteliklerini belirtir.
- [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) özelliği, ovalin çalışma sayfasındaki hücrelere bağlandığı [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype) şeklini belirtir.
- [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) özelliği şeklin doldurma biçimi stillerini belirtir.
- [**lower_right_row**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/lower_right_row) özelliği sağ alt köşe satır indisini belirtir.
- [**lower_right_column**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/lower_right_column) özelliği sağ alt köşe sütun indisini belirtir.

Aşağıdaki örnek, çalışma sayfasına oval şekiller eklemenin nasıl yapıldığını göstermektedir. Örnek iki oval şekli oluşturur: biri doldurulmuş oval diğeri basit daire.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingOvalControl-1.py" >}}

## **Çalışma Sayfasına Spinner Kontrolü Ekleme**

Bir döndürme kutusu, yukarı oka ve aşağı oka tıklayarak değerleri artırıp azaltabileceğiniz bir döndürme düğmesine (döndürme düğmesi) bağlı bir metin kutusudur. Döndürme kutuları kullanarak finansal modelinizdeki girişlerin nasıl değişeceğini görebilirsiniz. Belirli bir giriş hücresine bir döndürme düğmesi ekleyebilirsiniz. Döndürme düğmesinin yukarı veya aşağı oka tıkladığınızda, hedef giriş hücresindeki tam sayı değeri artar veya azalır. *Aspose.Cells for Python via .NET* çalışma sayfalarınızda döndürücüler oluşturmaya olanak tanır.

### **Microsoft Excel Kullanımı**

Çalışma sayfanıza bir spin kutusu kontrolü yerleştirmek için:

- *Formlar* araç çubuğunun görüntülendiğinden emin olun.
- *Spinner* aracına tıklayın.
- Çalışma sayfanızdaki alanda, spinner'ı tutacak dikdörtgeni tanımlamak için tıklayın ve sürükleyin.
- Spinner çalışma sayfasına yerleştirildiğinde, kontrolün üzerine sağ tıklayın ve *Kontrolü Biçimlendir* i tıklayın ve maksimum, minimum ve artış değerlerini belirtin.
- *Bağlantı Hücresi* alanında, bu spin kutusunun bağlanması gereken hücrenin adresini belirtin.
- *Tamam* a tıklayın.

### **Aspose.Cells for Python via .NET Kullanılarak**

Sınıf [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection), bir çalışma sayfasına bir spin kutu denetimini eklemek için kullanılan [**add_spinner**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_spinner) adında bir yöntem sağlar. Yöntem bir [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner) nesnesi döndürür. [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner) sınıfı bir spin kutusunu temsil eder. Bazı önemli üyeleri vardır:

- [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) özelliği, spin kutusuyla bağlantılı bir hücreyi belirtir.
- [**max**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/max) özelliği, spin kutusu aralığı için maksimum değeri belirtir.
- [**min**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/min) özelliği, spin kutusu aralığı için minimum değeri belirtir.
- [**incremental_change**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/incremental_change) özelliği, bir kaydırıcının bir satır kaydırılacak değer miktarını belirtir.
- [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/shadow) özelliği, spin kutusunun 3B gölgeli olup olmadığını belirtir.
- [**current_value**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/current_value) özelliği, spin kutusunun geçerli değerini belirtir.

Aşağıdaki örnek, çalışma sayfasına bir spin kutusu eklemenin nasıl yapıldığını gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingSpinnerControl-1.py" >}}

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

### **Aspose.Cells for Python via .NET Kullanılarak**

Sınıf [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection), bir çalışma sayfasına bir kaydırma çubuğu denetimini eklemek için kullanılan [**add_scroll_bar**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_scroll_bar) adında bir yöntem sağlar. Yöntem bir [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar) nesnesi döndürür. [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar) sınıfı bir kaydırma çubuğunu temsil eder. Bazı önemli üyeleri vardır:

- [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) özelliği, kaydırma çubuğuyla bağlantılı bir hücreyi belirtir.
- [**max**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/max) özelliği, kaydırma çubuğu aralığı için maksimum değeri belirtir.
- [**min**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/min) özelliği, kaydırma çubuğu aralığı için minimum değeri belirtir.
- [**incremental_change**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/incremental_change) özelliği, bir kaydırmanın bir satır kaydırılacak değer miktarını belirtir.
- [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/shadow) özelliği, bir kaydırma çubuğunun 3B gölgeli olup olmadığını belirtir.
- [**current_value**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/current_value) özelliği, kaydırma çubuğunun mevcut değerini belirtir.
- [**page_change**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/page_change) özelliği, kaydırma çubuğunun her iki yanına da tıklarsanız mevcut değerin ne kadar artırılacağını belirtir.

Aşağıdaki örnek, çalışma sayfasına bir kaydırma çubuğu nasıl ekleyeceğinizi gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingScrollBarControl-1.py" >}}

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

### **Aspose.Cells for Python via .NET Kullanılarak**

[**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) sınıfı, çalışma sayfasına bir grup kutu kontrolü eklemek için kullanılan [**add_group_box**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_group_box) adında bir yöntem sağlar. Yöntem bir [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupbox) nesnesi döndürür. Ayrıca, [**group**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/group) yöntemi, şekilleri gruplar, bu, bir [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) dizisi alır ve bir [**Shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape) nesnesi döndürür. [**GroupShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupshape) sınıfı bir grup kutusunu temsil eder. Önemli bazı üyelere sahiptir:

- [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) özelliği grup kutusunun başlık dizesini belirtir.
- [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupbox/shadow) özelliği grup kutusunun 3B gölgeleme olup olmadığını belirtir.

Aşağıdaki örnek, çalışma sayfasına bir grup kutu eklemeyi ve kontrolleri gruplamayı gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingGroupBoxControl-1.py" >}}

## **Gelişmiş Konular**
- [AktifX Kontrolleri Ekle](/cells/tr/python-net/add-activex-controls-using-aspose-cells/)
- [ActiveX Kontrolü Kaldırma](/cells/tr/python-net/remove-activex-control/)
- [ActiveX ComboBox Kontrolünü Güncelleme](/cells/tr/python-net/update-activex-combobox-control/)
{{< app/cells/assistant language="python-net" >}}
