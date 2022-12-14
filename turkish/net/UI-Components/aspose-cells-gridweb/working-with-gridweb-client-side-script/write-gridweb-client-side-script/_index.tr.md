---
title: GridWeb İstemci Tarafı Komut Dosyası Yazma
type: docs
weight: 10
url: /tr/net/write-gridweb-client-side-script/
---
{{% alert color="primary" %}} 

Geliştiriciler, Aspose.Cells.GridWeb denetimi için istemci tarafı komut dosyaları yazabilir. Bu, GridWeb denetimiyle ilgili belirli bir görevi gerçekleştirmek için istemci tarafında bir JavaScript işlevi çağırmanın mümkün olduğu anlamına gelir. Örneğin geliştiriciler, GridWeb verilerini bir sunucuya göndermek veya bir doğrulama hatası oluştuğunda vb. bir uyarı mesajı göstermek için JavaScript işlevleri yazabilir.

Bu konuda, bu özellik örnekler yardımıyla açıklanmaktadır.

{{% /alert %}} 
## **Aspose.Cells.GridWeb için İstemci Taraflı Komut Dosyaları Yazma**
### **Temel Bilgiler**
Aspose.Cells.GridWeb, istemci tarafı komut dosyalarını desteklemek için özel olarak oluşturulmuş iki özellik sağlar:

- OnSubmitClientFonksiyonu
- OnValidationErrorClientFunction

Bir ASPX sayfasında JavaScript işlevleri oluşturun ve bu işlevlerin adlarını OnSubmitClientFunction ve OnValidationErrorClientFunction özelliklerine atayın.

{{% alert color="primary" %}} 

OnSubmitClientFunction özelliğine atanacak JavaScript işlevi, aşağıda gösterildiği gibi düzgün bir şekilde tanımlanmalıdır:

**JavaScript**

{{< highlight "csharp" >}}

 function function_name(arg, cancelEdit)

 {

   //Add javascript code here

 }



{{< /highlight >}}

burada [arg]parametresi, kontrol tarafından oluşturulan komutu temsil eder. Komut "Kaydet", "Gönder", "Geri Al" vb. olabilir ve [cancelEdit] parametresi, kullanıcı girişinin iptal edilip edilmediğini gösteren bir Boole değeridir.

OnSubmitClientFunction özelliğine atanan herhangi bir JavaScript işlevi, GridWeb verilerini bir sunucuya göndermeden önce her zaman GridWeb denetimi tarafından çağrılır. Benzer şekilde, OnValidationErrorClientFunction özelliğine bir işlev atanırsa, her doğrulama hatası oluştuğunda bu işlev çağrılır.

{{% /alert %}} 
### **İstemci Tarafında Komut Dosyası Oluşturma İşlevleri**
Aspose.Cells.GridWeb ayrıca özellikle istemci tarafı komut dosyası çalıştırma için işlevler sunar. Bu işlevler, Aspose.Cells.GridWeb üzerinde daha fazla denetim elde etmek için JavaScript işlevleri içinde kullanılabilir. Bu istemci tarafı işlevleri şunları içerir:

|**Fonksiyonlar**|**Tanım**|
|:- |:- |
|updateData(bool cancelDüzenle)|Aspose.Cells.GridWeb'in tüm istemci verilerini sunucuya göndermeden önce günceller. cancelEdit parametresi doğruysa, GridWeb tüm kullanıcı girdilerini atar.|
|validall()|Kullanıcı girişinde herhangi bir doğrulama hatası olup olmadığını kontrol etmek için kullanılır. Bir hata varsa, işlev false döndürür, aksi takdirde true .|
|gönder(string arg, bool cancelDüzenle)|Verileri geri göndermek veya sunucuya göndermek için bu işlevi çağırın. Bu işlev, hem verileri güncelleyen hem de kullanıcı girişini onaylayan görevleri gerçekleştirir. Bu işlev aynı zamanda sunucu tarafında bir komut olayını tetikleyebilir. Komutunuzu iletmek için arg parametresini kullanın. Örneğin: KAYDET komutu, düğmeyi tıklatmak için kullanılır.**Kaydetmek** GridWeb denetiminin komut çubuğundaki düğmesine basın ve CCMD:MYCOMMAND komutu bir CustomCommand olayı başlatır.|
|setActiveCell(int satır, int sütun)|Belirli bir hücreyi etkinleştirmek için kullanılır.|
|setCellValue(int satır, int sütun, dize değeri)|Satır ve sütun numaraları kullanılarak belirtilen herhangi bir hücreye değer koymak için kullanılır.|
|getCellValue(int satır, int sütun)|Belirtilen herhangi bir hücrenin değerini döndürür.|
|getActiveRow()|Etkin bir hücrenin konumunu belirlemek için getActiveColumn() işleviyle birlikte kullanılır.|
|getActiveColumn()|Etkin bir hücrenin konumunu belirlemek için getActiveRow() işleviyle birlikte kullanılır.|
|getSelectRange()|Son seçilen aralığı döndürür.|
|setSelectRange()|Verilen aralığı seçer.|
|clearSelections()|Geçerli etkin hücre hariç tüm seçimi temizler.|
|getCellsArray()| getCellName(), getCellValueByCell(), getCellRow() ve getCellColumn() gibi diğer ilgili işlevlerle birlikte kullanılır. Bu işlevin kullanımıyla ilgili daha fazla bilgi için lütfen bu makaleyi okuyun:[İstemci Tarafındaki GridWeb hücrelerinin değerlerini okuyun](/cells/tr/net/read-the-values-of-the-gridweb-cells-on-client-side/)|
Aspose.Cells.GridWeb ile çalışan istemci tarafı komut dosyaları içeren bir test uygulaması oluşturmak için aşağıdaki adımları izleyin:

1. GridWeb tarafından çağrılacak JavaScript işlevleri oluşturun.
 Bu işlevler ASP.NET sayfasına eklenecektir.<script></script>etiket.
1. İşlevlerin adlarını OnSubmitClientFunction ve OnValidationErrorClientFunction özelliklerine atayın.

Kod örneğinin çıktısı aşağıda gösterilmiştir:

**C1 hücresine bir doğrulama eklendi** 

![yapılacaklar:resim_alternatif_Metin](write-gridweb-client-side-script_1.png)

 Geçersiz bir değer ekleyin ve tıklayın**Kaydetmek**. Bir doğrulama hatası oluşur ve ValidationErrorFunction yürütülür.

**ValidationErrorFunction, doğrulama hatasında çağrıldı** 

![yapılacaklar:resim_alternatif_Metin](write-gridweb-client-side-script_2.png)

 Siz geçerli bir değer girene kadar sunucuya hiçbir veri gönderilmez. Geçerli bir değer girin ve tıklayın**Kaydetmek**. Onay İşlevi yürütülür.

**GridWeb verilerini sunucuya göndermeden önce Onay İşlevi çağrıldı** 

![yapılacaklar:resim_alternatif_Metin](write-gridweb-client-side-script_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript-WriteClientSideScript.aspx" >}}

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-WriteClientSideScript.aspx-WriteClientSideScript.cs" >}}
