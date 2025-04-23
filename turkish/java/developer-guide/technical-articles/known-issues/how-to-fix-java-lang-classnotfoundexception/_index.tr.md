---
title: java.lang.ClassNotFoundException Hatasını Nasıl Çözebilirim
type: docs
weight: 30
url: /tr/java/how-to-fix-java-lang-classnotfoundexception/ 
description: Aspose.Cells for Java içinde java.lang.ClassNotFoundException ı nasıl düzelteceğinizi öğrenin.
keywords: BouncyCastleProvider Java da ClassNotFoundException ını Nasıl Düzeltebilirsiniz, Java kullanarak BouncyCastleProvider istisnasını çözün, Java ClassNotFoundException BouncyCastleProvider ı çözün.
---

Aspose.Cells for Java API'sı bazı ek kütüphanelere bağlıdır, eksikler varsa "java.lang.ClassNotFoundException" olarak bir istisna atılabilir.
Bu makale, bu tür istisnaları listeler ve bunları çözmek için hangi kütüphanelerin yüklendiğini açıklar.

## ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider Hatasını Nasıl Çözebilirim
### **Özet**
Aspose.Cells for Java API, şifreleme ve şifre çözme özellikleri için Bouncy Castle'a bağlıdır, yani programın şifreli elektronik tabloları yüklemesi veya kaydetmesi gerekiyorsa, projenin sınıf yoluna bcprov-jdk16-146.jar referansı eklenmesi gereklidir.
### **Belirtiler**
java.lang.ClassNotFoundException: org.bouncycastle.jce.provider.BouncyCastleProvider hatası alabilirsiniz. 
### **Çözüm**
Çözüm aslında aşağıda detaylı olarak belirtilmiştir.

1. [Aspose.Cells for Java](https://downloads.aspose.com/cells/java)'ın herhangi bir ana sürümünü indirin.
1. İndirilen arşivi çıkarın ve \JDK 1.6\aspose-cells-x.x.0-java\lib dizinine göz atın.
1. Projenin sınıf yolundaki bcprov-jdk16-146.jar dosyasını referans olarak ekleyin.

Alternatif olarak, pom.xml dosyasına bağımlılığı ekleyebilir ve projeyi maven üzerinden bağımlılığı çözmesine izin verebilirsiniz.

{{< highlight java >}}

 <dependencies>

	<dependency>

		<groupId>org.bouncycastle</groupId>

		<artifactId>bcprov-jdk16</artifactId>

		<version>1.46</version>

		<type>jar</type>

	</dependency>

</dependencies>

{{< /highlight >}}

{{< app/cells/assistant language="java" >}}
