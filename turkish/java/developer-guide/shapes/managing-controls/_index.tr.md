---
title: Kontrolleri Yönetme
type: docs
weight: 120
url: /tr/java/managing-controls/
---

## **Giriş**

Geliştiriciler metin kutuları, onay kutuları, radyo düğmeleri, açılır kutular, etiketler, düğmeler, çizgiler, dikdörtgenler, yarıçapları, ovaları, kaydırma çubuklarını, grup kutularını vb. gibi farklı çizim nesneleri ekleyebilir. Aspose.Cells, tüm çizim nesnelerini içeren Aspose.Cells.Drawing ad alanını sağlar. Ancak henüz desteklenmeyen bazı çizim nesneleri veya şekiller vardır. Bu çizim nesnelerini Microsoft Excel kullanarak bir tasarımcı çalışma sayfasında oluşturun ve ardından tasarımcı çalışma sayfasını Aspose.Cells'e aktarın. Aspose.Cells, bir tasarımcı çalışma sayfasından bu çizim nesnelerini yüklemenize ve bunları oluşturulan bir dosyaya yazmanıza olanak tanır.

## **Çalışma Sayfasına Metin Kutusu Kontrolü Ekleme**

Raporlarda önemli bilgileri vurgulamanın bir yolu, bir metin kutusu kullanmaktır. Örneğin, şirket adını vurgulamak veya en yüksek satış yapılan coğrafi bölgeyi belirtmek için bir metin ekleyin. Aspose.Cells, yeni bir metin kutusu eklemek için kullanılan TextBoxes sınıfını sağlar. [**TextBox**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox) isminde başka bir sınıf vardır ve tüm türdeki ayarları tanımlamak için kullanılan bir metin kutusunu temsil eder. Bazı önemli üyeleri vardır:

- [**getTextFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#TextFrame) methodu, metin kutusunun içeriğini ayarlamak için kullanılan bir [**MsoTextFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoTextFrame) nesnesi döndürür.
- [**setPlacement**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Placement) methodu, yerleşim tipini belirtir.
- [**setFont**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Font) methodu, yazı tipi özniteliklerini belirtir.
- [**addHyperlink**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#addHyperlink-java.lang.String-) methodu, metin kutusu için bir bağlantıyı ekler.
- [**FillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#FillFormat) özelliği, metin kutusu için doldurma biçimini ayarlamak için kullanılan bir [**MsoFillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoFillFormat) nesnesi döndürür.
- [**LineFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#LineFormat) özelliği, metin kutusu çizgisi için stil ve kalınlık genellikle kullanılan bir [**MsoLineFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoLineFormat) nesnesi döndürür.
- [**setText**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Text) yöntemi metin kutusu için giriş metnini belirtir.

Aşağıdaki örnek, çalışma kitabının ilk çalışma sayfasında iki metin kutusu oluşturur. İlk metin kutusu farklı biçim ayarlarıyla donatılmıştır. İkincisi ise basit bir tanedir.

Kodun çalıştırılmasıyla oluşturulan aşağıdaki çıktı:

**İş sayfasında iki metin kutusu oluşturuldu** 

![todo:image_alt_text](managing-controls_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingTextBoxControl-1.java" >}}

## **Tasarımcı İş Sayfalarında Metin Kutusu Kontrollerini Manipüle Etme**

Aspose.Cells, ayrıca tasarımcı elektronik tablolardaki metin kutularına erişmenizi ve bunları manipüle etmenizi sağlar. Levhada metin kutuları koleksiyonunu almak için [**Worksheet.getTextBoxes**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#TextBoxes) özelliğini kullanın.

Aşağıdaki örnek yukarıdaki örnekte oluşturduğumuz Microsoft Excel dosyası olan - tsttextboxes.xls - kullanır. İki metin kutusunun metin dizelerini alır ve ikinci metin kutusunun metnini değiştirerek dosyayı kaydeder.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-ManipulatingTextBoxControls-1.java" >}}

## **İş Sayfasına Onay Kutusu Ekleme**

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

Aspose.Cells, yeni bir onay kutusu eklemek için kullanılan [**CheckBoxCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/checkboxcollection) sınıfını sağlar. İşte onay kutusunu temsil eden başka bir sınıf olan [**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/java/com.aspose.cells/CheckBox). Önemli bazı üyelere sahiptir:

- [**setLinkedCell**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#LinkedCell) yöntemi onay kutusuna bağlı olan hücreyi belirtir.
- [**setText**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#Text) yöntemi onay kutusu ile ilişkilendirilen metin dizisini belirtir. Bu, onay kutusunun etiketidir.
- [**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#Value) yöntemi onay kutusunun işaretli olup olmadığını belirtir.

Aşağıdaki örnek, iş sayfasına bir onay kutusu eklemenin nasıl yapıldığını gösterir. Aşağıdaki çıktı kodun çalıştırılmasından sonra oluşturulur.

**İş sayfasına bir Onay Kutusu eklendi** 

![todo:image_alt_text](managing-controls_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingCheckBoxControl-1.java" >}}

## **İş Sayfasına Radyo Düğmesi Kontrolü Ekleme**

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

[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) sınıfı, çalışma sayfasına bir radyo düğmesi denetimi eklemek için kullanılabilecek addShape adında bir metod sağlar. Metod bir RadioButton nesnesi döndürebilir. RadioButton sınıfı, bir seçenek düğmesini temsil eder. Bazı önemli üyelere sahiptir:

- The setLinkedCell metodu, radyo düğmesine bağlı olan bir hücreyi belirtir.
- The setText metodu, radyo düğmesiyle ilişkilendirilmiş metin dizisini belirtir. Bu radyo düğmesinin etiketidir.
- The Checked özelliği, radyo düğmesinin işaretli olup olmadığını belirtir.
- The setFillFormat metodu, radyo düğmesinin doldurma formatını belirtir.
- The setLineFormat metodu, seçenek düğmesinin çizgi formatını belirtir.

Aşağıdaki örnek, çalışma sayfasına radyo düğmeleri eklemenin nasıl yapıldığını gösterir. Örnek, yaş gruplarını temsil eden üç radyo düğmesi ekler. Kodun çalıştırılmasından sonra aşağıdaki çıktı oluşturulur.

**Çalışma sayfasına bazı Radyo Düğmeleri eklenmiş** 

![todo:image_alt_text](managing-controls_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingRadioButtonControl-1.java" >}}

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

[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) sınıfı, çalışma sayfasına bir combo box denetimi eklemek için kullanılabilecek addShape adında bir metod sağlar. Metod bir ComboBox nesnesi döndürebilir. ComboBox sınıfı, bir combo box'u temsil eder. Bazı önemli üyelere sahiptir:

- The setLinkedCell metodu, combo box'a bağlı olan bir hücreyi belirtir.
- The setInputRange metodu, combo box'u doldurmak için kullanılan çalışma sayfası aralığını belirtir.
- The setDropDownLines metodu, bir combo box'un açılır kısmında gösterilen liste satırlarının sayısını belirtir.
- The setShadow metodu, combo box'un 3B gölgelendirmeye sahip olup olmadığını belirtir.

Aşağıdaki örnek, çalışma sayfasına bir combo box eklemenin nasıl yapıldığını gösterir. Kodun çalıştırılmasından sonra aşağıdaki çıktı oluşturulur.

**Çalışma sayfasına bir combobox eklenir** 

![todo:image_alt_text](managing-controls_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingComboBoxControl-1.java" >}}

## **Etiket Denetimi Ekleme**

Etiketler, bir elektronik tablonun içeriği hakkında kullanıcılara bilgi vermenin bir yoludur. Aspose.Cells, çalışma sayfasına etiket eklemeyi ve bunları manipüle etmeyi mümkün kılar. [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) sınıfı, çalışma sayfasına etiket kontrolü eklemek için kullanılan addShape adında bir yöntem sağlar. Yöntem, bir Etiket nesnesi döndürür. Etiket sınıfı, çalışma sayfasındaki bir etiketi temsil eder. Bazı önemli üyelere sahiptir:

- setText yöntemi, bir etiketin başlık dizesini belirtir.
- setPlacement yöntemi, etiketin çalışma sayfasındaki hücrelere bağlanma şeklini belirtir.

Aşağıdaki örnek, çalışma sayfasına bir etiket eklemenin nasıl bir sonuç doğurduğunu gösterir. Kodu yürüttüğünüzde aşağıdaki çıktı oluşturulur.

**Çalışma sayfasına bir etiket eklenir**

![todo:image_alt_text](managing-controls_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingLabelControl-1.java" >}}

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

[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) sınıfı, çalışma sayfasına liste kutusu kontrolü eklemek için kullanılan addShape adında bir yöntem sağlar. Yöntem, bir ListBox nesnesi döndürür. ListBox sınıfı, bir liste kutusunu temsil eder. Bazı önemli üyelere sahiptir:

- setLinkedCell yöntemi, liste kutusu ile ilişkilendirilen bir hücre belirtir.
- setInputRange yöntemi, liste kutusunu doldurmak için kullanılan çalışma sayfası aralığını belirtir.
- setSelectionType yöntemi, liste kutusunun seçim modunu belirtir.
- setShadow yöntemi, liste kutusunun 3D gölge olup olmadığını belirtir.

Aşağıdaki örnek, çalışma sayfasına bir liste kutusu eklemenin nasıl bir sonuç doğurduğunu gösterir. Kodu yürüttüğünüzde aşağıdaki çıktı oluşturulur.

**Çalışma sayfasına bir liste kutusu eklenir** 

![todo:image_alt_text](managing-controls_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingListBoxControl-1.java" >}}

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

[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) sınıfı, çalışma sayfasına bir düğme denetimi eklemek için kullanılan addShape adında bir yöntem sağlar. Yöntem bir Düğme nesnesi döndürebilir. Düğme sınıfı bir düğmeyi temsil eder. Bazı önemli üyeleri vardır:

- setText yöntemi düğmenin başlığını belirtir.
- setPlacement yöntemi, düğmenin çalışma sayfasındaki hücrelere bağlanma şeklini belirtir.
- addHyperlink yöntemi, düğme denetimi için bir bağlantı ekler. Düğmeye tıklamak bağlantılı URL'ye gezinir.

Aşağıdaki örnek, çalışma sayfasına bir düğme eklemenin nasıl yapılacağını gösterir. Kodu yürüttüğünüzde, aşağıdaki çıktı oluşturulur.

**Çalışma sayfasına bir düğme eklenir**

![todo:image_alt_text](managing-controls_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingButtonControl-1.java" >}}

## **Çalışma sayfasına Satır Denetimi Ekleme**

Aspose.Cells, çalışma sayfalarınızda otomatik şekiller çizmenize olanak tanır. Kolayca bir çizgi oluşturabilirsiniz. Ayrıca çizgiyi biçimlendirmenize izin verilir. Örneğin, çizginin rengini değiştirebilir, çizginin ağırlığını ve stiline göre belirleyebilirsiniz.

### **Microsoft Excel Kullanımı**

1. **Çizim** araç çubuğunda, **Şekiller**'e tıklayın, ardından **Satırlar**'a gelin ve istediğiniz çizgi stiline tıklayın.
1. Çizmek için sürükleyin.
1. Aşağıdakilerden birini veya her ikisinden birini yapın:
   1. Çizginin başlangıç noktasından 15 derece açılarla çizilmesini sınırlamak için, sürüklerken **SHIFT** tuşunu basılı tutun.
   1. İlk uç noktasından zıt yönlere doğru çizgiyi uzatmak için, sürüklerken **CTRL** tuşunu basılı tutun.

### **Aspose.Cells Kullanımı**

[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) sınıfı, çalışma sayfasına bir çizgi şekli eklemek için kullanılan addShape adında bir yöntem sağlar. Yöntem bir LineShape nesnesi döndürebilir. LineShape sınıfı bir çizgiyi temsil eder. Bazı önemli üyeleri vardır:

- setDashStyle yöntemi, bir çizginin biçimini belirtir.
- setPlacement yöntemi, çizginin çalışma sayfasındaki hücrelere bağlanma şeklini belirtir.

Aşağıdaki örnek, çalışma sayfasına çizgiler eklemenin nasıl yapılacağını gösterir. Farklı stillerde üç çizgi oluşturur. Kodu yürüttüğünüzde, aşağıdaki çıktı oluşturulur.

**Çalışma sayfasına birkaç çizgi eklenir** 

![todo:image_alt_text](managing-controls_8.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingLineControl-1.java" >}}

### **Çizgiye Yön Gösteren Başlık Ekleme**

Aspose.Cells, oklu satırlar çizmenize de olanak tanır. Bir satıra bir ok başlığı eklemek ve satırın biçimlendirilmesi mümkündür. Örneğin, satırın rengini değiştirebilir veya satırın ağırlığını ve stilini belirtebilirsiniz.

Aşağıdaki örnek, bir çizgiye başlık eklemenin nasıl yapılacağını gösterir. Kodu yürüttüğünüzde, aşağıdaki çıktı oluşturulur.

**Ok başlıklı bir çizgi çalışma sayfasına eklenir** 

![todo:image_alt_text](managing-controls_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddinganArrowHead.java" >}}

## **Çalışma Sayfasına Dikdörtgen Kontrolü Ekleme**

Aspose.Cells, çalışma sayfalarınızda dikdörtgen şekilleri çizmenize olanak tanır. Bir dikdörtgen, kare vb. oluşturabilirsiniz. Ayrıca kontrolün doldurma rengini, sınır çizgisi rengini biçimlendirmenize izin verilir. Örneğin, dikdörtgenin rengini değiştirebilir, gölgelendirme rengini ayarlayabilir veya dikdörtgenin ağırlığını ve stilini belirleyebilirsiniz.

### **Microsoft Excel Kullanımı**

1. **Çizim** araç çubuğunda, **Dikdörtgen**'e tıklayın.
1. Dikdörtgen çizmek için sürükleyin.
1. Aşağıdakilerden birini veya her ikisinden birini yapın:
   1. Dikdörtgeni başlangıç noktasından karesel çizmeyi kısıtlamak için sürükleme sırasında SHIFT tuşunu basılı tutun.
   1. Dikdörtgeni merkez noktasından çizmek için sürükleme sırasında CTRL tuşunu basılı tutun.

### **Aspose.Cells Kullanımı**

[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) sınıfı, çalışma sayfasına dikdörtgen şekli eklemek için kullanılan addShape adında bir yöntem sağlar. Yöntem, bir RectangleShape nesnesi döndürebilir. RectangleShape sınıfı bir dikdörtgeni temsil eder. Bazı önemli üyelere sahiptir:

- setLineFormat metodu bir dikdörtgenin çizgi biçim özelliklerini belirtir.
- setPlacement metodu, dikdörtgenin çalışma sayfasındaki hücrelere bağlanma şeklini belirtir.
- FillFormat özelliği, bir dikdörtgenin doldurma biçim stillerini belirtir.

Aşağıdaki örnek, çalışma sayfasına bir dikdörtgen eklemenin nasıl olduğunu göstermektedir. Kodu yürüttüğünüzde aşağıdaki çıktı üretilir.

**Çalışma sayfasına bir dikdörtgen eklenir** 

![todo:image_alt_text](managing-controls_10.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingRectangleControl-1.java" >}}

## **Çalışma Sayfasına Yay Kontrolü Ekleme**

Aspose.Cells, çalışma sayfalarında yay şekilleri çizmenize olanak tanır. Basit ve dolu yaylar oluşturabilirsiniz. Kontrolün doldurma rengini ve sınır çizgisi rengini biçimlendirmenize izin verilir. Örneğin, yayın rengini belirleyebilir, gölgelendirme rengini ayarlayabilir veya şeklin ağırlığını ve stilini belirleyebilirsiniz.

### **Microsoft Excel Kullanımı**

1. **Çizim** araç çubuğunda, **Otomatik Şekiller** içinde **Yay**'e tıklayın.
1. Yay çizmek için sürükleyin.

### **Aspose.Cells Kullanımı**

[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) sınıfı, çalışma sayfasına yay şekli eklemek için kullanılan addShape adında bir yöntem sağlar. Yöntem, bir ArcShape nesnesi döndürebilir. ArcShape sınıfı bir yayı temsil eder. Bazı önemli üyelere sahiptir:

- setLineFormat metodu, yay şeklinin çizgi biçim özelliklerini belirtir.
- setPlacement metodu, yayın çalışma sayfasındaki hücrelere bağlanma şeklini belirtir.
- FillFormat özelliği, şeklin doldurma biçimi stillerini belirtir.

Aşağıdaki örnek, çalışma sayfasına yay şekilleri nasıl eklenir göstermektedir. Örnek, iki yay şekli oluşturur: biri dolu ve diğeri basittir. Kodu yürüttüğünüzde aşağıdaki çıktı üretilir

**Çalışma sayfasına iki yay şekli eklenir** 

![todo:image_alt_text](managing-controls_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingArcControl-1.java" >}}

## **Çalışma Sayfasına Oval Kontrolü Ekleme**

Aspose.Cells, çalışma sayfalarında oval şekilleri çizmenize olanak tanır. Basit ve dolu oval şekiller oluşturun ve kontrolün doldurma rengini ve kenar çizgisi rengini biçimlendirin. Örneğin, ovalin rengini belirleyebilir, gölgelendirme rengini ayarlayabilir, şeklin ağırlığını ve stilini belirleyebilirsiniz.

### **Microsoft Excel Kullanımı**

1. **Çizim** araç çubuğunda, **Oval** 'e tıklayın.
1. Ovalı çizmek için sürükleyin.
1. Aşağıdakilerden birini veya her ikisinden birini yapın:
   1. Ovalı çizmek için başlangıç noktasından çember çizmek için sürüklerken SHIFT tuşunu basılı tutun.
   1. Bir merkez noktasından oval çizmek için sürüklerken CTRL tuşuna basılı tutun.

### **Aspose.Cells Kullanımı**

[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) sınıfı, bir çalışma sayfasına oval şekli eklemek için kullanılan addShape adında bir yöntem sağlar. Yöntem, bir Oval nesnesi döndürebilir. Oval sınıfı, bir oval şekli temsil eder. Önemli bazı üyelere sahiptir:

- setLineFormat yöntemi, bir oval şeklinin çizgi biçimi özniteliklerini belirtir.
- setPlacement yöntemi, ovalın çalışma sayfasındaki hücrelere bağlandığı yer olan PlacementType'u belirtir.
- FillFormat özelliği, şeklin doldurma biçimi stillerini belirtir.

Aşağıdaki örnek, çalışma sayfasına oval şekiller eklemeyi gösterir. Örnek, iki oval şekil oluşturur: biri dolu oval, diğeri basit bir daire. Kodu çalıştırdığınızda aşağıdaki çıktı oluşturulur.

**Çalışma sayfasına iki oval şekil eklenmiştir** 

![todo:image_alt_text](managing-controls_12.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddinganOvalControl-1.java" >}}

## **Gelişmiş Konular**
- [Aspose.Cells Kullanarak ActiveX Kontrolleri Ekleme](/cells/tr/java/add-activex-controls-using-aspose-cells/)
- [ActiveX Kontrolü Kaldırma](/cells/tr/java/remove-activex-control/)
{{< app/cells/assistant language="java" >}}
