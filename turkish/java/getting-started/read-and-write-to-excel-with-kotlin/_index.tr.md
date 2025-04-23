---
title: Kotlin ile Excel Okuma ve Yazma
type: docs
weight: 189
url: /tr/java/read-and-write-to-excel-with-kotlin/
description: Kotlin de Excel dosyalarını Aspose.Cells for Java kullanarak okumayı, yazmayı ve biçimlendirmeyi öğrenin. Formüller ve biçimlendirme için kod örnekleri içerir.
keywords: Kotlin Excel, Aspose.Cells Kotlin, Kotlin ile Excel Okuma, Kotlin ile Excel Yazma, Excel Formülleri Kotlin, Excel Hücre Biçimlendirme, Aspose.Cells Kurulumu.
---

Aspose.Cells for Java, geliştiricilerin Excel dosyalarını programatik olarak manipüle etmelerini sağlayan güçlü bir kütüphanedir. Java için tasarlanmıştır, ancak Kotlin ile tamamen uyumlu olduğu için sorunsuz entegre olur. Bu belge, Kotlin ve Aspose.Cells for Java kullanarak Excel dosyalarını okuma ve yazma adımlarını sağlar.

## Önkoşullar
- Kotlin ve Java Geliştirme Kiti (JDK) yüklü.
- Bağımlılık yönetimi için yapı aracı (Maven veya Gradle) yapılandırılmış.

## Kotlin'de Aspose.Cells Kurulumu

Projeye Aspose.Cells bağımlılığını ekleyin:

### Maven için (`pom.xml`):
```xml
<repositories>
    <repository>
        <id>AsposeJavaAPI</id>
        <name>Aspose Java API</name>
        <url>https://releases.aspose.com/java/repo/</url>
    </repository>
</repositories>

<dependencies>
    <!-- Aspose.Cells for Java -->
    <dependency>
        <groupId>com.aspose</groupId>
        <artifactId>aspose-cells</artifactId>
        <version>25.2</version>
    </dependency>

    <!-- Mandatory Bouncy Castle Libraries -->
    <dependency>
        <groupId>org.bouncycastle</groupId>
        <artifactId>bcprov-jdk15on</artifactId>
        <version>1.68</version>
    </dependency>
    <dependency>
        <groupId>org.bouncycastle</groupId>
        <artifactId>bcpkix-jdk15on</artifactId>
        <version>1.68</version>
    </dependency>
</dependencies>
```
### Gradle için (`build.gradle.kts`):
```kotlin
repositories {
    maven { url = uri("https://releases.aspose.com/java/repo/") }
}

dependencies {
    // Aspose.Cells for Java
    implementation("com.aspose:aspose-cells:25.2")

    // Mandatory Bouncy Castle Libraries
    implementation("org.bouncycastle:bcprov-jdk15on:1.68")
    implementation("org.bouncycastle:bcpkix-jdk15on:1.68")
}
```
## Excel'e Yazma

Bu örnek, yeni bir Excel çalışma kitabı oluşturmayı, hücreleri veriyle doldurmayı ve dosyayı diske kaydetmeyi gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Kotlin-WriteToExcel.kt" >}}

## Excel'den Okuma

Bu örnek, mevcut bir Excel dosyasını yüklemeyi, hücre değerlerini okumayı ve sonuçları yazdırmayı gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Kotlin-ReadFromExcel.kt" >}}

## İleri Düzey İşlemler

### Formülleri İşleme

Bu örnek, bir hücreye formül (`SUM`) ekler, çalışma kitabını yeniden hesaplar ve sonucu yazdırır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Kotlin-HandleFormulas.kt" >}}

### Hücreleri Biçimlendir

Bu örnek, bir hücreye stil uygular (kalın yazı, kırmızı renk ve ortalanmış hizalama).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Kotlin-FormatCells.kt" >}}

{{< app/cells/assistant language="java" >}}
