---
title: Başlarken
type: docs
weight: 10
url: /tr/cpp/getting-started/
description: Aspose Cells for C++ nasıl kurulur ve Hello World uygulaması nasıl oluşturulur?
---
{{% alert color="primary" %}} 

Bu sayfada Aspose Cells for C++'in nasıl kurulacağı ve Hello World uygulamasının nasıl oluşturulacağı gösterilecektir.

{{% /alert %}}

##  **Kurulum**

###  **Aspose Cells ila NuGet'i yükleyin**

 NuGet, Aspose.Cells for C++'i indirip kurmanın en kolay yoludur.
1. Bir Microsoft Visual Studio projesi for C++ oluşturun.
2. "Aspose.Cells.h" başlık dosyasını ekleyin.
3. Microsoft Visual Studio ve NuGet paket yöneticisini açın.
 4. İstediğiniz Aspose.Cells for C++'i bulmak için "aspose.cells.cpp"yi arayın.
5. "Yükle"ye tıklayın, Aspose.Cells for C++ indirilecek ve projenizde referans alınacaktır.

**![Yükle Aspose Cells - NuGet](InstallThroughNuget.png)**

 Ayrıca aspose.cells'in nuget web sayfasından da indirebilirsiniz:
[Aspose.Cells for C++ NuGet Paket](https://www.nuget.org/packages/Aspose.Cells.Cpp/)

[Ayrıntılar için daha fazla adım](/cells/tr/cpp/installation/)

###  **Windows'de Aspose.Cells for C++'i kullanmak için bir demo**

1. Aspose.Cells for C++'i aşağıdaki sayfadan indirin:
[İndir Aspose.Cells for C++(Windows)](https://downloads.aspose.com/cells/cpp/)
2. Paketi açın ve Aspose.Cells for C++'in nasıl kullanılacağını gösteren bir örnek bulacaksınız.
3. example.sln dosyasını Visual Studio 2017 veya daha yüksek bir sürümle açın
4. main.cpp: bu dosya Aspose.Cells for C++'i test etmek için nasıl kod yazılacağını gösterir

###  **Linux'ta Aspose.Cells for C++'i kullanmak için bir demo**

1. Aspose.Cells for C++'i aşağıdaki sayfadan indirin:
[İndir Aspose.Cells for C++(Linux)](https://downloads.aspose.com/cells/cpp/)
2. Paketi açın ve Linux için Aspose.Cells for C++'in nasıl kullanılacağını gösteren bir örnek bulacaksınız.
3. Örneğin bulunduğu yolda olduğunuzdan emin olun.
4. "cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release" komutunu çalıştırın
5. "cmake --build example/build" komutunu çalıştırın

###  **Mac OS'ta Aspose.Cells for C++'i kullanmaya yönelik bir demo**

1. Aspose.Cells for C++'i aşağıdaki sayfadan indirin:
[İndir Aspose.Cells for C++(MacOS)](https://downloads.aspose.com/cells/cpp/)
2. Paketi açın ve MacOS için Aspose.Cells for C++'in nasıl kullanılacağını gösteren bir örnek bulacaksınız.
3. Örneğin bulunduğu yolda olduğunuzdan emin olun.
4. "cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release" komutunu çalıştırın
5. "cmake --build example/build" komutunu çalıştırın

##  **Hello World Uygulamasının Oluşturulması**

Aşağıdaki adımlar, Aspose.Cells API'i kullanarak Hello World uygulamasını oluşturur:

1.  Bir örneğini oluşturun[Çalışma kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıf.
1.  Ehliyetin varsa o zaman[Uygula](/cells/tr/cpp/licensing/).
 Değerlendirme sürümünü kullanıyorsanız lisansla ilgili kod satırlarını atlayın.
1. Excel dosyasındaki bir çalışma sayfasının istediğiniz herhangi bir hücresine erişin.
1. Erişilen bir hücreye "**Hello World!**" sözcüklerini ekleyin.
1. Değiştirilen Microsoft Excel dosyasını oluşturun.

Yukarıdaki adımların uygulanması aşağıdaki örneklerde gösterilmiştir.

###  **Kod Örneği: Yeni Bir Çalışma Kitabı Oluşturma**

Aşağıdaki örnekte sıfırdan yeni bir çalışma kitabı oluşturulur, ilk çalışma sayfasındaki A1 hücresine "**Hello World!**" eklenir ve Excel dosyası kaydedilir.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-FirstApplication-1-new.cpp" >}}

###  **Kod Örneği: Mevcut Bir Dosyayı Açma**

Aşağıdaki örnek, mevcut bir Microsoft Excel şablon dosyasını açar, bir hücre alır ve A1 hücresindeki değeri kontrol eder.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-OpenExistingFile-1-new.cpp" >}}
