---
title: Başlarken
type: docs
weight: 10
url: /tr/cpp/getting-started/
description: C++ ve Hello World uygulaması oluşturmak için Aspose Cells ı nasıl kuracağınızı gösterir.
---

{{% alert color="primary" %}} 

Bu sayfa, C++ için Aspose Cells'ı nasıl kuracağınızı ve Hello World uygulaması oluşturacağınızı gösterecektir.

{{% /alert %}}

## **Kurulum**

### **NuGet üzerinden Aspose Cells kurun**

NuGet, Aspose.Cells for C++'ı indirmenin ve yüklemenin en kolay yoludur. 
1. C++ için bir Microsoft Visual Studio projesi oluşturun.
2. "Aspose.Cells.h" başlık dosyasını dahil edin.
3. Microsoft Visual Studio ve NuGet paket yöneticisini açın.
4. Aramak için "aspose.cells.cpp" yazın, istenen Aspose.Cells for C++'i bulun. 
5. "Yükle"'ye tıklayın, Aspose.Cells for C++ indirilecek ve projenizde referans olarak alınacaktır.

**![Aspose Cells'u NuGet Üzerinden Yükleyin](InstallThroughNuget.png)**

Aspose.Cells için nuget web sayfasından da indirebilirsiniz: 
[Aspose.Cells for C++ NuGet Paketi](https://www.nuget.org/packages/Aspose.Cells.Cpp/)

[Detaylar için daha fazla adım](/cells/tr/cpp/installation/)

### **Windows'ta Aspose.Cells for C++ kullanımı için bir demo**

1. Aspose.Cells for C++'yi aşağıdaki sayfadan indirin:
[Aspose.Cells for C++'i İndir (Windows)](https://downloads.aspose.com/cells/cpp/)
2. Paketi açın ve Aspose.Cells for C++'i nasıl kullanılacağına dair bir örnek bulacaksınız.
3. Visual Studio 2017 veya daha yeni sürümü ile example.sln dosyasını açın
4. main.cpp: Bu dosya Aspose.Cells for C++'i test etmek için nasıl kod yazılacağını gösterir

### **Linux'ta Aspose.Cells for C++ kullanımı için bir demo**

1. Aspose.Cells for C++'yi aşağıdaki sayfadan indirin:
[Aspose.Cells for C++'i İndir (Linux)](https://downloads.aspose.com/cells/cpp/)
2. Paketi açın ve Aspose.Cells for C++'i nasıl kullanılacağına dair bir örnek bulacaksınız.
3. Örnek dosyasının bulunduğu dizinde olduğunuzdan emin olun.
4. "cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release" komutunu çalıştırın
4. "cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release" komutunu çalıştırın

### **Mac OS'ta Aspose.Cells for C++ kullanımı için bir demo**

1. Aspose.Cells for C++'yi aşağıdaki sayfadan indirin:
[Aspose.Cells for C++'i İndir (MacOS)](https://downloads.aspose.com/cells/cpp/)
2. Paketi açın ve Aspose.Cells for C++'i nasıl kullanılacağına dair bir örnek bulacaksınız.
3. Örnek dosyasının bulunduğu dizinde olduğunuzdan emin olun.
4. "cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release" komutunu çalıştırın
4. "cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release" komutunu çalıştırın

## **Merhaba Dünya Uygulamasını Oluşturma**

Aşağıdaki adımlar, Aspose.Cells API'sini kullanarak Merhaba Dünya uygulamasını oluşturur:

Aşağıdaki adımlar, Aspose.Cells API'sini kullanarak Hello World uygulamasını oluşturur:
1. [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfından bir örnek oluşturun.
   Eğer değerlendirme sürümünü kullanıyorsanız, lisansla ilgili kod satırlarını atlayın.
1. Excel dosyasındaki istenen hücreye erişin.
1. Hücreye erişildiğinde "**Merhaba Dünya!**" kelimesini ekleyin.
1. Değiştirilmiş Microsoft Excel dosyasını oluşturun.

Yukarıdaki adımların uygulanışı aşağıdaki örneklerde gösterilmektedir.

### **Kod Örneği: Yeni Bir Workbook Oluşturma**

Aşağıdaki örnek, baştan yeni bir çalışma kitabı oluşturur, ilk çalışma sayfasındaki A1 hücresine "**Merhaba Dünya!**" ekler ve Excel dosyasını kaydeder.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-FirstApplication-1-new.cpp" >}}

### **Kod Örneği: Mevcut Bir Dosyayı Açma**

Aşağıdaki örnek, mevcut bir Microsoft Excel şablon dosyasını açar, bir hücre alır ve A1 hücresindeki değeri kontrol eder.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-OpenExistingFile-1-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
