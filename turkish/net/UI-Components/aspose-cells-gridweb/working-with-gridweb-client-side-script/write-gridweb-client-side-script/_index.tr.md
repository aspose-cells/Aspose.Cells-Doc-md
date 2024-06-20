---
title: GridWeb İstemci Tarafı Betik Yazma
type: docs
weight: 10
url: /tr/net/aspose-cells-gridweb/write-gridweb-client-side-script/
keywords: GridWeb,client,js,javascript
description: Bu makale, GridWeb de istemci js api leriyle nasıl çalışılacağını tanıtıyor.
---

{{% alert color="primary" %}} 

Geliştiriciler, Aspose.Cells.GridWeb denetimi için istemci tarafı betiklerini yazabilir. Bu, bir JavaScript işlevini istemci tarafında çağırarak GridWeb denetimi ile ilgili belirli bir görevi gerçekleştirmenin mümkün olduğu anlamına gelir. Örneğin, geliştiriciler, GridWeb verilerini sunucuya göndermek veya bir doğrulama hatası oluştuğunda bir uyarı iletmek gibi JavaScript işlevleri yazabilirler vb.

Bu konu, örneklerin yardımıyla bu özelliği açıklar.

{{% /alert %}} 
## **Aspose.Cells.GridWeb için İstemci Tarafı Scriptleri Yazma**
### **Temel Bilgiler**
Aspose.Cells.GridWeb, özellikle istemci tarafında betikleri desteklemek üzere oluşturulmuş iki özellik sağlar:

- OnSubmitClientFunction
- OnValidationErrorClientFunction

ASPX sayfasında JavaScript işlevleri oluşturun ve bu işlevlerin adlarını OnSubmitClientFunction ve OnValidationErrorClientFunction özelliklerine atayın.

{{% alert color="primary" %}} 

OnSubmitClientFunction özelliğine atanacak JavaScript işlevi aşağıdaki gibi düzgün bir şekilde tanımlanmalıdır:

**JavaScript**

{{< highlight csharp >}}

 function function_name(arg, cancelEdit)

 {

   //Add javascript code here

 }



{{< /highlight >}}

[arg] parametresi, kontrol tarafından oluşturulan komutu temsil eder. Komut, "Kaydet", "Gönder", "Geri Al" vb. olabilir ve [cancelEdit] parametresi, kullanıcının girişinin iptal edilip edilmediğini gösteren Boolean bir değerdir.

OnSubmitClientFunction özelliğine atanan herhangi bir JavaScript işlevi, GridWeb denetimi sunucuya GridWeb verilerini göndermeden önce her zaman çağrılır. Benzer şekilde, OnValidationErrorClientFunction özelliğine bir işlev atanmışsa, bu işlev her doğrulama hatası oluştuğunda çağrılır.

{{% /alert %}} 
### **İstemci Tarafı Betikler İçin İşlevler**
Aspose.Cells.GridWeb, özellikle istemci tarafı betikleri için işlevler de sunar. Bu istemci tarafı işlevleri, JavaScript fonksiyonlarında Aspose.Cells.GridWeb'in daha fazla kontrolünü elde etmek için kullanılabilir. Bu istemci tarafı işlevleri aşağıdakileri içerir:

|**İşlevler**|**Açıklama**|
| :- | :- |
|updateData(bool cancelEdit)|Aspose.Cells.GridWeb'in tüm istemci verilerini sunucuya göndermeden önce günceller. Eğer cancelEdit parametresi true ise, GridWeb tüm kullanıcı girdisini reddeder. |
|validateAll()|Kullanıcı girişinde herhangi bir doğrulama hatası olup olmadığını kontrol etmek için kullanılır. Eğer bir hata varsa, fonksiyon false döner, aksi halde true. |
|submit(string arg, bool cancelEdit)|Sunucuya veri göndermek veya postback yapmak için bu fonksiyonu çağırın. Bu fonksiyon, veriyi güncellemek ve kullanıcı girişini doğrulamak gibi her iki görevi de yerine getirir. Bu fonksiyon ayrıca sunucu tarafında bir komut olayı tetikleyebilir. Komutunuzu iletmek için arg parametresini kullanın. Örneğin: SAVE komutu, GridWeb kontrolünün komut çubuğundaki **Kaydet** düğmesine tıklamak için kullanılır ve CCMD:MYCOMMAND komutu, ÖzelKomut olayını tetikler. |
|setActiveCell(int row, int column)|Belirli bir hücreyi etkinleştirmek için kullanılır.
|setCellValue(int row, int column, string value)|Belirtilen satır ve sütun numaralarını kullanarak herhangi bir hücreye bir değer atamak için kullanılır.
|getCellValue(int row, int column)|Belirli bir hücrenin değerini döndürür.
|getActiveRow()|getActiveColumn() fonksiyonu ile birlikte kullanılarak etkin hücrenin konumunu belirlemek için kullanılır.
|getActiveColumn()|getActiveRow() fonksiyonu ile birlikte kullanılarak etkin hücrenin konumunu belirlemek için kullanılır.
|getSelectRange()|Son seçili aralığı döndürür.
|setSelectRange()|Verilen aralığı seçer.
|clearSelections()|Mevcut etkin hücre haricinde tüm seçimi temizler.|
|getCellsArray()|Bu, getCellName(), getCellValueByCell(), getCellRow() ve getCellColumn() gibi diğer ilgili işlevlerle birlikte kullanılır. Bu işlevin kullanımı hakkında daha fazla bilgi için lütfen şu makaleyi okuyun: [İstemci Tarafında GridWeb Hücrelerinin Değerlerini Okuyun](/cells/tr/net/aspose-cells-gridweb/read-the-values-of-the-gridweb-cells-on-client-side/)|
Aspose.Cells.GridWeb ile çalışan istemci tarafı betikleri içeren test uygulaması oluşturmak için aşağıdaki adımları izleyin:

1. GridWeb tarafından çağrılacak JavaScript işlevlerini oluşturun.
   These functions will be added to the ASP.NET page's <script></script> tag.
1. İşlevlerin adlarını OnSubmitClientFunction ve OnValidationErrorClientFunction özelliklerine atayın.

Kod örneğinin çıktısı aşağıda gösterilmiştir:

**C1 hücresine eklenen bir doğrulama** 

![todo:image_alt_text](write-gridweb-client-side-script_1.png)

Geçersiz bir değer ekleyin ve **Kaydet**e tıklayın. Bir doğrulama hatası oluşur ve ValidationErrorFunction çalıştırılır.

**Doğrulama hatası oluştuğunda ValidationErrorFunction çağrıldı** 

![todo:image_alt_text](write-gridweb-client-side-script_2.png)

Geçerli bir değer girmediğiniz sürece, hiçbir veri sunucuya gönderilmez. Geçerli bir değer girin ve **Kaydet**e tıklayın. ConfirmFunction çalıştırılır.

**Sunucuya GridWeb verilerini göndermeden önce ConfirmFunction çağrıldı** 

![todo:image_alt_text](write-gridweb-client-side-script_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript-WriteClientSideScript.aspx" >}}

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript.aspx-WriteClientSideScript.cs" >}}
