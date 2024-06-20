---
title: Aspose.Cells Java for Jython
type: docs
weight: 70
url: /tr/java/aspose-cells-java-for-jython/
---

## **Giriş**

### **Jython Nedir?**

Jython, açıklığın yanı sıra ifade gücünü birleştiren Python'un Java uygulamasıdır. Jython ticari ve ticari olmayan kullanım için ücretsiz olarak dağıtılır ve kaynak kodu ile birlikte dağıtılır. Jython, Java'ya bir tamamlayıcıdır ve özellikle aşağıdaki görevler için uygundur:

- **Gömülü betikleme** - Java programcıları, kullanıcıların uygulamaya işlev eklemelerine izin vermek için Jython kütüphanelerini sistemlerine ekleyebilirler.
- **Etkileşimli deney** - Jython, Java paketleriyle veya çalışan Java uygulamalarıyla etkileşime girebilecek şekilde kullanılabilen etkileşimli bir yorumlayıcı sağlar. Bu, programcıların Jython'u kullanarak herhangi bir Java sistemi üzerinde deney yapmasına ve hata ayıklamasına olanak tanır.
- **Hızlı uygulama geliştirme** - Python programları genellikle karşılık gelen Java programından 2-10 kat daha kısadır. Bu doğrudan artan programcı üretkenliğine dönüşür. Python ve Java arasındaki sorunsuz etkileşim, geliştiricilere geliştirme sırasında ve ürünlerin gönderilmesi sırasında iki dili serbestçe karıştırma imkanı tanır.

### **Aspose.Cells for Java**

Aspose.Cells for Java, Java içinde doğrudan bir dizi belge işleme görevini gerçekleştirmenizi sağlayan gelişmiş bir sınıf kütüphanesidir
uygulamalar.

Aspose.Cells for Java, Hücrelerin (DOC, DOCX, OOXML, RTF) HTML, OpenDocument, PDF, EPUB, XPS, SWF ve tüm görüntü biçimlerinin işlenmesini destekler. Aspose.Cells ile Microsoft Cells kullanmadan belge oluşturabilir, değiştirebilir ve dönüştürebilirsiniz.
Microsoft Cells kullanmadan belge oluşturabilir, değiştirebilir ve dönüştürebilirsiniz.

### **Aspose.Cells Java for Jython**

Aspose.Cells Java for Jython, Aspose.Cells for Java API kullanım örneklerini Jython'da gösteren / sağlayan bir projedir.

## **Sistem Gereksinimleri ve Desteklenen Platformlar**

### **Sistem Gereksinimleri**

**Aspose.Cells Java for Jython kullanmak için aşağıdaki sistem gereksinimleri bulunmaktadır:**

- Java 1.5 veya üstü yüklü
- Aspose.Cells bileşeni indirildi
- Jython 2.7.0

### **Desteklenen Platformlar**

**Aşağıdakiler desteklenen platformlardır:**

- Aspose.Cells 15.4 ve daha üstü.
- Java IDE (Eclipse, NetBeans ...)

## **İndirme, Kurulum ve Kullanım**

### **İndirme**

**Sosyal kodlama sitelerinden örnekleri indirin**

Çalışan örnek sürümlerini aşağıda belirtilen tüm sosyal kodlama sitelerinden indirebilirsiniz:

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)

**Aspose.Cells for Java bileşenini indirin**

- [Aspose.Cells for Java](https://releases.aspose.com/cells/java/)

### **Yüklemek**

- İndirilen Aspose.Cells for Java jar dosyasını "lib" dizinine yerleştirin.
- _*init*_.py dosyasında "your-lib" yerine indirilen jar dosya adını değiştirin.

### **Kullanarak**

Aşağıdaki örnek kodu kullanarak HelloWorld belgesi oluşturabilirsiniz:

{{< highlight java >}}

 from aspose-cells  import Settings

from com.aspose.Cells import Document

from com.aspose.Cells import DocumentBuilder

class HelloWorld:

    def __init__(self):

        dataDir = Settings.dataDir + 'quickstart/'



        workbook = Workbook()



        sheet = workbook.getWorksheets().get(0)



        cell = sheet.getCells().get("A1")



        cell.setValue("Hello World!")



        file_format_type = FileFormatType



        workbook.save(dataDir + "HelloWorld.xls" , file_format_type.EXCEL_97_TO_2003 )



        print "Document has been saved, please check the output file.";

if __name__ == '__main__':

    HelloWorld()

{{< /highlight >}}

## **Destek, Genişletme ve Katkıda Bulunma**

### **Destek**

Aspose'un ilk günlerinden itibaren, müşterilerimize sadece iyi ürünler sunmanın yeterli olmayacağını biliyorduk. Ayrıca iyi bir hizmet sunmamız gerekiyordu. Kendi geliştiricileri olduğumuz için, teknik bir sorun veya yazılımdaki bir tuhaflık sizi yapmanız gereken şeyden alıkoyduğunda ne kadar sinir bozucu olduğunu anlıyoruz. Sorunları çözmek için buradayız, onları yaratmak için değil.

Bu nedenle ücretsiz destek sunuyoruz. Ürünlerimizi kullanan herkes, bunları satın almış olsun veya değerlendirme yapılıyor olsun, tam dikket ve saygıyı hak ediyor.

Aspose.Cells Java için Jython ile ilgili herhangi bir sorunu veya öneriyi aşağıdaki platformlardan birini kullanarak kaydedebilirsiniz:

- [Github](https://github.com/aspose-words/Aspose.Words-for-Java/issues)

### **Genişletme ve Katkı Sağlama**

Aspose.Cells Java for Jython açık kaynak kodlu ve kaynak kodları aşağıda listelenen büyük sosyal kodlama sitelerinde mevcuttur. Geliştiriciler, kaynak kodunu indirerek yeni özellikler önererek veya ekleyerek mevcut olanları iyileştirerek katkıda bulunmaya teşvik edilir, böylece diğerleri de bundan faydalanabilir.

### **Kaynak Kodu**

En son kaynak kodunu aşağıdaki konumlardan birinden edinebilirsiniz

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)
