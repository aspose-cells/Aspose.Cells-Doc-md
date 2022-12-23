---
title: Jython için Aspose.Cells Java
type: docs
weight: 70
url: /tr/java/aspose-cells-java-for-jython/
---
## **Giriş**

### **Jython nedir?**

Jython, ifade gücünü netlikle birleştiren, Python'in Java uygulamasıdır. Jython, hem ticari hem de ticari olmayan kullanım için ücretsiz olarak mevcuttur ve kaynak koduyla birlikte dağıtılır. Jython, Java'i tamamlayıcı niteliktedir ve özellikle aşağıdaki görevler için uygundur:

- **Gömülü komut dosyası** - Java programcılar, son kullanıcıların uygulamaya işlevsellik katan basit veya karmaşık komut dosyaları yazmasına izin vermek için Jython kitaplıklarını sistemlerine ekleyebilirler.
- **Etkileşimli deney** - Jython, Java paketleriyle veya çalışan Java uygulamalarıyla etkileşime geçmek için kullanılabilecek etkileşimli bir tercüman sağlar. Bu, programcıların Jython kullanarak herhangi bir Java sistemini denemesine ve hata ayıklamasına olanak tanır.
- **Hızlı uygulama geliştirme** Python programları genellikle eşdeğer Java programından 2-10 kat daha kısadır. Bu, doğrudan artan programcı üretkenliği anlamına gelir. Python ve Java arasındaki kusursuz etkileşim, geliştiricilerin hem geliştirme sırasında hem de ürünleri gönderirken iki dili serbestçe karıştırmalarına olanak tanır.

### **Aspose.Cells for Java**

Aspose.Cells for Java, doğrudan Java içinde çok çeşitli belge işleme görevlerini gerçekleştirmenizi sağlayan gelişmiş bir sınıf kitaplığıdır for Java
uygulamalar.

Aspose.Cells for Java, Cells (DOC, DOCX, OOXML, RTF) HTML, OpenDocument, PDF, EPUB, XPS, SWF ve tüm görüntü biçimlerinin işlenmesini destekler. Aspose.Cells ile yapabilirsiniz
Microsoft Cells kullanmadan belgeler oluşturun, değiştirin ve dönüştürün.

### **Jython için Aspose.Cells Java**

Jython için Aspose.Cells Java, Jython'da Aspose.Cells for Java API kullanım örneklerini gösteren / sağlayan bir projedir.

## **Sistem Gereksinimleri ve Desteklenen Platformlar**

### **sistem gereksinimleri**

**Jython için Aspose.Cells Java'i kullanmak için sistem gereksinimleri aşağıdadır:**

- Java 1.5 veya üstü yüklü
- Aspose.Cells bileşeni indirildi
- Jython 2.7.0

### **Desteklenen Platformlar**

**Desteklenen platformlar aşağıdadır:**

- Aspose.Cells 15.4 ve üstü.
- Java IDE (Eclipse, NetBeans ...)

## **Kurulum ve Kullanımı İndirin**

### **indiriliyor**

**Sosyal kodlama web sitelerinden örnekler indirin**

Çalışan örneklerin aşağıdaki yayınları, aşağıda belirtilen sosyal kodlama sitelerinin tümünde indirilebilir:

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)

**Aspose.Cells for Java bileşenini indir**

- [Aspose.Cells for Java](https://releases.aspose.com/cells/java/)

### **yükleme**

- İndirdiğiniz Aspose.Cells for Java jar dosyasını "lib" dizinine atın.
- _*init*_.py dosyasında "your-lib" ifadesini indirilen jar dosya adıyla değiştirin.

### **kullanma**

Aşağıdaki örnek kodu kullanarak HelloWorld belgesi oluşturabilirsiniz:

{{< highlight "java" >}}

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

## **Destekleyin, Genişletin ve Katkıda Bulunun**

### **Destek olmak**

Aspose'in ilk günlerinden itibaren müşterilerimize sadece iyi ürünler vermenin yeterli olmayacağını biliyorduk. Ayrıca iyi hizmet vermemiz gerekiyordu. Biz de geliştiriciyiz ve teknik bir sorun veya yazılımdaki bir tuhaflık, yapmanız gerekeni yapmanızı engellediğinde bunun ne kadar sinir bozucu olduğunu anlıyoruz. Sorunları çözmek için buradayız, onları yaratmak için değil.

Bu nedenle ücretsiz destek sunuyoruz. İster satın almış olsun ister bir değerlendirme yapıyor olsun, ürünümüzü kullanan herkes, tüm dikkatimizi ve saygımızı hak ediyor.

Aşağıdaki platformlardan herhangi birini kullanarak Jython için Aspose.Cells Java ile ilgili sorunları veya önerileri günlüğe kaydedebilirsiniz:

- [Github](https://github.com/aspose-words/Aspose.Words-for-Java/issues)

### **Genişletin ve Katkıda Bulunun**

Aspose.Cells Java for Jython açık kaynaktır ve kaynak kodu aşağıda listelenen başlıca sosyal kodlama web sitelerinde mevcuttur. Geliştiricilerin kaynak kodunu indirmeleri ve yeni özellikler önererek veya ekleyerek veya mevcut olanları geliştirerek katkıda bulunmaları teşvik edilir, böylece diğerleri de bundan faydalanabilir.

### **Kaynak kodu**

En son kaynak kodunu aşağıdaki konumlardan birinden alabilirsiniz.

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)
