---
title: Çalışma Sayfalarını Koruma
type: docs
weight: 10
url: /tr/net/protecting-worksheets/
---

{{% alert color="primary" %}}

Bir çalışma sayfası korunduğunda, bir kullanıcının yapabileceği eylemler kısıtlanır. Örneğin, veri giremezler, satır veya sütun ekleyemez veya silemezler vb.

{{% /alert %}}

## **Çalışma Sayfalarını Koruma**

### **Giriş**

Microsoft Excel'de genel koruma seçenekleri:

- İçerik
- Nesneler
- Senaryolar

Korunan çalışma sayfaları hassas verileri gizlemez veya korumaz, bu nedenle dosya şifrelemesinden farklıdır. Genellikle, çalışma sayfası koruması sunumsal amaçlar için uygundur. Kullanıcının çalışma sayfasındaki veri, içerik ve biçimlendirmeyi değiştirmesini önler.

### **Bir Çalışma Sayfasını Koruma**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir sınıf olan [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sağlar. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı tarafından temsil edilir.

[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıfı, çalışma sayfasına koruma uygulamak için kullanılan [**Protect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index) yöntemini sağlar. [**Protect**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/protect/methods/1) yöntemi aşağıdaki parametreleri kabul eder:

- Koruma Türü, çalışma sayfasına uygulanacak koruma türü. Koruma türü, [**ProtectionType**](https://reference.aspose.com/cells/net/aspose.cells/protectiontype) numaralandırma yardımıyla uygulanır.
- Yeni Parola, çalışma sayfasını korumak için kullanılan yeni parola.
- Eski Parola, çalışma sayfası zaten parola korumalıysa eski paroladır. Çalışma sayfası zaten korunmamışsa sadece null geçirin.

[**ProtectionType**](https://reference.aspose.com/cells/net/aspose.cells/protectiontype) numaralandırma, aşağıdaki önceden tanımlanmış koruma türlerini içerir:

|**Koruma Türleri**|**Açıklama**|
| :- | :- |
|All|Kullanıcı bu çalışma sayfasında herhangi bir şeyi değiştiremez|
|Contents|Kullanıcı bu çalışma sayfasında veri giremez|
|Objects|Kullanıcı çizim nesnelerini değiştiremez|
|Scenarios|Kullanıcı, kaydedilmiş senaryoları değiştiremez|
|Structure|Kullanıcı yapıyı değiştiremez|
|Windows|Koruma, pencerelere uygulanır|
|None|Koruma uygulanmaz|

Aşağıdaki örnek, bir çalışma sayfasını bir şifre ile korumanın nasıl yapıldığını göstermektedir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingWorksheet-1.cs" >}}

Yukarıdaki kod çalışma sayfasını korumak için kullanıldıktan sonra, çalışma sayfasının korumasını açarak kontrol edebilirsiniz. Dosyayı açtığınızda çalışma sayfasına bazı veriler eklemeye çalıştığınızda aşağıdaki iletişim kutusunu göreceksiniz:

|**Kullanıcının çalışma sayfasını değiştiremeyeceği konusunda uyarı veren iletişim kutusu**|
| :- |
|![todo:image_alt_text](protecting-worksheets_1.png)|

Çalışma sayfasında çalışmak için **Koruma**, ardından **Sayfayı Korumayı Kaldır** öğesini **Araçlar** menü öğesinden seçerek çalışma sayfasının korumasını kaldırın.

**Sayfayı Korumayı Kaldır** menü öğesini seçtikten sonra, bir iletişim kutusu açılacaktır ve size çalışma sayfasında çalışmanız için şifreyi girmenizi isteyecektir, aşağıda gösterildiği gibi:

|![todo:image_alt_text](protecting-worksheets_2.png)|

### **Microsoft Excel Kullanarak Çalışma Sayfasındaki Birkaç Hücreyi Koruma**

Çalışma sayfasında sadece birkaç hücreyi kilitlemeniz gereken belirli senaryolar olabilir. Çalışma sayfasında belirli hücreleri kilitlemek istiyorsanız, çalışma sayfasındaki tüm diğer hücreleri kilitlemeniz gerekir. Bir çalışma sayfasındaki tüm hücreler zaten kilitlemek için başlatılmış durumda, bunu MS Excel'e herhangi bir Excel dosyasını açarak kontrol edebilir ve **Biçim | Hücreler...**'e tıklayarak **Hücreleri Biçimlendir** iletişim kutusunu gösterin ve sonra **Koruma** sekmesine tıklayarak "Kilitli" olarak adlandırılan bir onay kutusunun varsayılan olarak işaretlenip işaretlenmediğini kontrol edebilirsiniz.

MS Excel kullanarak birkaç hücreyi kilitlemenin aşağıdaki adımları açıklar. Bu yöntem, Microsoft Office Excel 97, 2000, 2002, 2003 ve daha yüksek sürümlerine uygulanır.

1. Satır numarası için doğrudan üzerindeki gri dikdörtgen (satır 1'in hemen üstündeki ve A sütun harfinin solundaki). **Tümünü Seç** düğmesine tıklayarak tüm çalışma sayfasını seçin.
1. **Biçim** menüsünde **Hücreler**'e tıklayın, **Koruma** sekmesine tıklayın ve sonra **Kilitli** onay kutusunu kaldırın.
   Bu, çalışma sayfasındaki tüm hücreleri kilidini açar.
   **Hücreler** komutu kullanılamıyorsa, çalışma sayfasının bazı bölümleri zaten kilitli olabilir. **Araçlar** menüsünde **Koruma**'ya gelin ve ardından **Sayfayı Korumayı Kaldır**'a tıklayın.
1. Kilitlemek istediğiniz hücreleri seçin ve adım 2'yi tekrarlayın, ancak bu sefer **Kilitli** onay kutusunu işaretleyin.
1. **Araçlar** menüsünde **Koruma**'ya gelin, **Sayfayı Koruma**'yı tıklayın ve ardından **Tamam**'ı tıklayın.
1. **Sayfayı Koruma** iletişim kutusunda, kullanıcıların değiştirebileceği öğeleri belirleme seçeneğine sahip olacaksınız.

### **Aspose Cells Kullanarak Çalışma Sayfasındaki Birkaç Hücreyi Korumak**

Bu yöntemde, yalnızca görevi gerçekleştirmek için Aspose.Cells API kullanıyoruz.

Örnek: Aşağıdaki örnek, çalışma sayfasındaki birkaç hücreyi nasıl koruyacağını göstermektedir. İlk olarak çalışma sayfasındaki tüm hücreleri kilidini açar ve ardından (A1, B1, C1) 3 hücreyi kilitleyerek korur. Son olarak, çalışma sayfasını korur. [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnesi, bir boolean özelliğini, [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) adlı bir özellik içerir. *Column/Row.ApplyStyle()* yöntemini kullanarak satır/sütunun kilidini açmak veya kilitlemek için [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) özelliğini true ya da false olarak ayarlayabilirsiniz.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingSpecificCellsinaWorksheet-1.cs" >}}

### **Çalışma Sayfasında Bir Satırı Koruma**

Aspose.Cells, çalışma sayfasındaki herhangi bir satırı kolayca kilitlemenize olanak tanır. Burada, çalışma sayfasındaki belirli bir satıra uygulamak için [**Aspose.Cells.Row**](https://reference.aspose.com/cells/net/aspose.cells/row) sınıfının [**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) yöntemini kullanabiliriz. Bu yöntem, uygulanan biçimlendirme ile ilgili tüm üyelere sahip olan bir [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnesi ve bir [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnesi olmak üzere iki argüman alır.

Aşağıdaki örnek, çalışma sayfasındaki bir satırı nasıl koruyacağını göstermektedir. İlk olarak, çalışma sayfasındaki tüm hücreleri kilidini açar ve ardından ilk satırı kilitleyerek korur. Son olarak, çalışma sayfasını korur. [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnesi, bir [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) adlı bir özellik içerir. Satır/sütunun kilidini açmak veya kilitlemek için [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) özelliğini true ya da false olarak ayarlayabilirsiniz.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingSpecificRowInWorksheet-1.cs" >}}

### **Çalışma Sayfasında Bir Sütunu Koruma**

Aspose.Cells, çalışma sayfasındaki herhangi bir sütunu kolayca kilitlemenize olanak tanır. Burada, çalışma sayfasındaki belirli bir sütuna uygulamak için [**Aspose.Cells.Column**](https://reference.aspose.com/cells/net/aspose.cells/column) sınıfının [**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/column/methods/applystyle) yöntemini kullanabiliriz. Bu yöntem, uygulanan biçimlendirme ile ilgili tüm üyelere sahip olan bir [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnesi ve bir [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnesi olmak üzere iki argüman alır.

Aşağıdaki örnek, çalışma sayfasındaki bir sütunu nasıl koruyacağını göstermektedir. İlk olarak, çalışma sayfasındaki tüm hücreleri kilidini açar ve ardından ilk sütunu kilitleyerek korur. Son olarak, çalışma sayfasını korur. [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnesi, bir [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) adlı bir özelliğe sahiptir. Satır/sütunun kilidini açmak veya kilitlemek için [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) özelliğini true ya da false olarak ayarlayabilirsiniz.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectColumnWorksheet-1.cs" >}}

### **Kullanıcılara Düzenleme Aralığı Izin Ver**

Aşağıdaki örnek, korunan bir çalışma sayfasında kullanıcılara bir aralığı düzenleme izni vermenin nasıl yapıldığını göstermektedir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-EditRangesWorksheet-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
